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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae8b3483-d8f0-3eb0-a39d-432b1f85cc6b | -3.33466 | -59.82839 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7f083cc1-9641-3d32-bb86-cd847ccd900a | -7.42334 | -44.77662 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b6fe523-e757-37df-9a29-8b418ab31533 | -6.15657 | -57.71237 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba747f7f-6c8f-3d7a-9cef-47cae01f7f7d | -7.34141 | -44.46077 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c828b7b5-7a62-3374-943b-4a6477d4121a | -6.09966 | -57.63211 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 33a1dd79-6aae-3115-946e-a21b094c30fa | -4.09395 | -52.12095 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6a4e9c6f-528e-35ff-853e-e79ec78ce765 | -6.15496 | -57.79179 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 68abfd24-decc-3c8a-a98c-5499bd573f3b | -6.17083 | -57.71499 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52d18fa3-3c97-335b-a71c-2946920f90be | -6.1892 | -57.77453 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae29679d-fd55-3181-830d-230fefdee9eb | -6.25456 | -55.4815 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 78fbae77-b518-3fcd-a4db-81b388859750 | -3.60279 | -59.05991 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4ed7feeb-bc2c-32cb-8316-fc8be63b40e1 | -5.81301 | -53.51698 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1b48671d-2016-3e07-bcee-6b1a35d5a340 | -6.41686 | -56.10125 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1792aeb7-292a-39ce-986d-54596b070f7b | -5.80799 | -57.74081 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 87e1f888-30aa-3680-99ef-3e55e82d7a98 | -4.41096 | -55.2418 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 949f5c9d-3e60-3a7d-9889-27ad0628afb0 | -3.05577 | -61.26972 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8beaee3c-ae45-368c-8b92-3ec7e410e39c | -6.49845 | -58.38268 | 2026-09-21 05:04:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5228f8af-af87-36b9-8b47-75f535466d18 | -6.07929 | -57.62891 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 060aa13d-76a6-3b6b-ad24-f4d59132e741 | -4.48858 | -55.48615 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| daf59317-e7b0-36e6-8586-d4f4f7e8fbdc | -6.30646 | -60.01842 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 898b6203-44b5-31eb-8934-e47cf10cc091 | -3.04912 | -61.25605 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 622b5e20-f059-3717-99fb-a0d1ddfd3071 | -3.40502 | -61.30128 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 13397c5a-2ec0-335b-862f-c781e85c7a10 | -6.29732 | -59.93165 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7ee661cc-d861-3281-ae77-236bb8c79bfa | -5.84601 | -53.54905 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7145ffe6-fa0f-393b-aed0-51883a5082b1 | -6.72855 | -55.05526 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 532f07c1-bbe5-34fa-a446-c0b59edf7e1c | -5.82848 | -52.075 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e59dabe1-c1a8-3c7b-9dc9-801ed666e387 | -5.85205 | -49.78557 | 2026-09-21 05:04:00 | NOAA-21 | CURIONÓPOLIS | PARÁ | Brasil | 1502772 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 16ab6ff4-0a40-3126-a0f9-407e0cac2118 | -6.14503 | -57.76338 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a89183d6-fadb-38d8-970d-f8483db93b26 | -2.96326 | -54.16079 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 61e28470-471f-384e-b4af-48c34aad8564 | -5.6118 | -44.847 | 2026-09-21 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 71e72fad-19f1-33ae-84b2-1a15bb7e28c9 | -3.66552 | -54.27979 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 557f4e82-cd97-3ac5-8c5c-dad3763d09e0 | -7.41294 | -44.76684 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8b4429a4-7519-3b55-b44d-5719c1bac4c2 | -6.26978 | -57.73409 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40fc339a-3472-3983-a398-ecff22de9c6b | -3.48979 | -59.56777 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7401d8e9-c467-3aa5-8877-7aa661f3f670 | -5.60582 | -44.84591 | 2026-09-21 05:04:00 | NOAA-21 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 18332888-96b4-3542-b4c8-d8d37b834c16 | -3.50052 | -59.18765 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29ee5420-b299-3956-b1b0-cf1ea4fa8f49 | -7.96836 | -47.46111 | 2026-09-21 05:04:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a4342b8-2ed1-37e5-9fc6-6829c2a60e05 | -4.56266 | -55.75178 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 56c4fd80-b4e9-31a4-aae2-919bbafbf56f | -6.09887 | -57.68062 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 62391d9d-ae2d-3566-ae37-d527a6dd88a4 | -3.16117 | -54.28825 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3db60b2b-2685-31d0-8fac-7b7dc88cefa0 | -3.6065 | -59.0605 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 39680b72-97ef-31d5-bb0a-3543d87a2530 | -2.64688 | -54.68704 | 2026-09-21 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| ca96838d-e4f9-363f-a29f-fc92ce5be616 | -6.15404 | -57.84095 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ca1c99d1-ab5b-3343-8cc1-ab5ffedb5a6e | -4.12594 | -54.29365 | 2026-09-21 05:04:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2feabea2-3cd5-355c-9146-d4deb31b90c9 | -4.23407 | -56.19882 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5a9d2e9b-7d98-3afe-a32c-ce34d335c64d | -5.84486 | -53.55671 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f132ecd-4f63-31b1-ae6c-41f893a57767 | -3.4014 | -61.29652 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 27384de5-2e96-3c75-a979-cb0b8a45e671 | -5.824 | -53.5147 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cb890af-d374-3047-9488-fbca297839ad | -2.17011 | -48.32347 | 2026-09-21 05:04:00 | NOAA-21 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f4d2f480-108b-3478-8ce5-62b3caebefb1 | -4.22597 | -48.61764 | 2026-09-21 05:04:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8adfb0b6-0737-318d-947b-7fdbfd0d9654 | -6.19772 | -55.45494 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5895ed43-2b79-3778-a613-6559ff2d8a48 | -6.32555 | -43.37788 | 2026-09-21 05:04:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 1d577ab4-a1e8-350a-b970-411fe47527e2 | -4.43336 | -55.07601 | 2026-09-21 05:04:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 54667fa3-3cf0-30c2-a20b-1e4995f55474 | -5.84198 | -53.55233 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d5dd6cd7-3f48-3485-8ffc-32e769854314 | -6.09585 | -55.56257 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| db80ce9f-05a5-3e9d-85dd-c31808b7d2d5 | -2.61492 | -51.72301 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 220366fe-9baf-3fcd-a0eb-1463a59f6a96 | -6.30716 | -57.74012 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| a6d02d41-61d6-3e2a-9591-126b6edd7dd2 | -3.36868 | -61.34656 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aba18dc-4c84-3ca3-8f64-47885466b914 | -5.8327 | -53.51955 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2acf0e4-7150-3f11-9236-8a85d8bf6675 | -5.75315 | -57.58133 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bf4bbb87-f4fa-39a8-a750-f2d327c48619 | -5.76571 | -57.45995 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6a535398-639a-35e1-8064-cd4d3c3eda6c | -6.46887 | -48.44713 | 2026-09-21 05:04:00 | NOAA-21 | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2700214b-0113-3114-8bfd-b8a535bda787 | -5.83901 | -53.47729 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 715c79d0-d68f-3e91-8581-c1731584e3f8 | -3.45183 | -50.5993 | 2026-09-21 05:04:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1164c2ae-056f-3324-ac48-9f3662eef0bf | -5.26046 | -55.92522 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd244533-5b8a-35d8-b8d8-b8a4be6863bb | -7.43951 | -44.74903 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2ec9f5ab-aa30-386d-aa10-b54be43ad8ed | -6.83723 | -55.76023 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d88e7cf4-1013-36ae-8f9b-601b90a89a50 | -7.42271 | -44.78155 | 2026-09-21 05:04:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a22390ab-00ea-3e11-888b-42aeb02135fc | -3.49056 | -59.56304 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 85b72ff5-2b73-3e51-a292-ec4a80259fca | -5.21364 | -56.11212 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 21fcde9b-b5bd-3881-8ae5-a9b310bf6a2e | -5.98724 | -57.69728 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dd32e723-43a0-3d89-a0a1-d8f68db81991 | -6.10083 | -57.6248 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 79a4e2d2-e8a0-33bf-ab3d-0714c390ed97 | -6.10226 | -57.68119 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19efa24a-c6e1-3df2-a636-624457b78c29 | -5.88149 | -52.05136 | 2026-09-21 05:04:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ef06cf3e-a9a5-3674-8df3-cce7a4c1b5c9 | -3.07603 | -61.28134 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 011d9045-fc57-3caa-bfe8-d882256c4004 | -2.46301 | -49.22805 | 2026-09-21 05:04:00 | NOAA-21 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 849eee39-a521-30b8-8c8c-6db8549cc284 | -3.42729 | -59.25988 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 19d8cf77-bfe5-3532-8d4f-21d316ca8238 | -6.34962 | -57.89074 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ece8a542-88f2-3f22-8c30-2fc9e3547244 | -3.68917 | -60.57233 | 2026-09-21 05:04:00 | NOAA-21 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 52763c5a-bbb5-387b-b207-6a13786a4022 | -5.8344 | -53.51629 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| be764ee2-fae9-3c4e-a89c-01f58553730b | -3.4226 | -59.19404 | 2026-09-21 05:04:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2b632d4e-6718-32aa-a13a-05a8425d4d87 | -6.72809 | -55.08036 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b233456b-e2c1-3460-9780-d3702ea67407 | -6.09192 | -55.5443 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d5e96337-b60c-3260-9d93-20b45394068f | -3.36802 | -61.35069 | 2026-09-21 05:04:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 50a4c4a9-2108-3b6e-8aba-85a2e54c43be | -3.04349 | -61.26358 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4787aaf0-e2c2-35e1-b0a0-fa1e785c4363 | -6.41632 | -56.1047 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a24169e5-e99b-3010-8d60-7b94babfd3a0 | -5.20582 | -56.07552 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05f98852-ff0a-3f44-b791-4bf25a916687 | -6.0702 | -57.7289 | 2026-09-21 05:04:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 86ab65c3-da8a-30ee-b504-39e0b7e53a2d | -6.72468 | -55.05824 | 2026-09-21 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0c37f02f-baea-3042-9efb-f5a4db33037e | -6.26155 | -55.43651 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5e0869b9-fc35-30e1-87a7-fa4d6d291951 | -2.08057 | -56.59251 | 2026-09-21 05:04:00 | NOAA-21 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 680daa1d-e094-3f44-9fa4-a45518ba7e3e | -6.32085 | -60.02557 | 2026-09-21 05:04:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d4429211-fb70-3062-b3e1-e3b3004e70d8 | -3.48974 | -59.6165 | 2026-09-21 05:04:00 | NOAA-21 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9b3ad420-cde2-3b40-a6e8-14ae62b23c82 | -4.15798 | -50.23624 | 2026-09-21 05:04:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b6cabbc-aa3e-3942-a2af-a58245ecba04 | -4.5632 | -55.74834 | 2026-09-21 05:04:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9d012db1-9ef5-3583-838d-e61ca56e8e22 | -2.91101 | -54.1456 | 2026-09-21 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f693a76f-f6b2-3191-8d59-2230bab15b83 | -3.19009 | -60.42984 | 2026-09-21 05:04:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95bf9fc1-d2dd-3b94-80f3-e795ae5d8142 | -5.01224 | -56.09778 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 139c5012-82f4-3bfa-8fdc-298e153a12c6 | -6.83412 | -55.53979 | 2026-09-21 05:04:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 051c1bdc-96dd-34e6-b140-555259c6e7b8 | -5.12086 | -55.96623 | 2026-09-21 05:04:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README68.md)
