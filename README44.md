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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e2888a94-b734-3cea-a287-f27c39c5ea71 | -3.27043 | -50.39677 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| efc58a9c-83b6-3586-a67e-2301d7931f69 | -5.02879 | -43.5717 | 2026-10-06 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d887b671-a456-3432-80a5-814fd29d61e3 | -1.10371 | -54.15386 | 2026-10-06 04:38:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f3094a94-fe3e-3537-a7ed-4881217d66dd | -3.05089 | -54.22457 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a51bc1b1-8d5e-37c1-ae37-2dcef9314d97 | -2.8405 | -54.07436 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 05164fd2-e497-355f-847d-8ba92c7e6b9f | -3.16658 | -50.43628 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a17bee7-f1d5-32e9-a790-b4e02ad8be9f | -3.68242 | -55.96358 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7376ac5a-df19-391e-8c71-54dd34e9fe25 | -3.16594 | -50.44036 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 524a3e5a-99f8-31d6-abca-443fb682086d | -3.22072 | -53.87469 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e82fcba4-3332-343d-b469-f1ba0920fe49 | -3.67164 | -54.53895 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f463c4e-7336-33cf-9ae9-1a53204e0756 | -3.42549 | -50.43979 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2dfa2a87-f84e-345a-b4d5-26034644e5a6 | -2.87323 | -54.1617 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 51dce4f8-9db4-3031-ad27-875dae761396 | -3.50493 | -54.60357 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f30753c-4dda-3837-b8c3-5a0543711e73 | -3.05319 | -54.21049 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5fa51de4-29a9-3fb0-a85d-089bfe3cc8ed | -2.77498 | -54.10184 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e646f993-0501-3673-8f6d-b7fda0aa7665 | -3.10046 | -54.17987 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| fa1ef9c9-b908-35fc-bb6e-978ebc03b5ce | -0.99698 | -47.65854 | 2026-10-06 04:38:00 | NOAA-20 | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 01965b0c-4c2c-39a9-8161-efdc1fc45fb8 | -2.87249 | -54.13707 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| afb2604f-83f6-3fba-8619-f03918e6231c | -2.99544 | -54.13375 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 107f8c31-c8e9-3493-a589-366e3d8a7a4a | -3.29013 | -42.2645 | 2026-10-06 04:38:00 | NOAA-20 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 308eff75-3b13-31dc-bce1-1ba17435f806 | 1.04204 | -50.02401 | 2026-10-06 04:38:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0b94a0c4-e90e-35a0-b35a-b74d8228a3a4 | -2.80309 | -54.13037 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8b55b4b3-f1de-3582-8413-ad4d500c2e0d | -3.89355 | -49.7145 | 2026-10-06 04:38:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e3bf5233-2e51-3302-bf82-b3b205489270 | 2.46488 | -50.84291 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 621b14c1-8f79-317a-9e8d-c43d00af1817 | -3.10719 | -53.74051 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 137ae446-fa62-3133-b815-26adcd04d527 | -3.67325 | -55.95562 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e0f29ca4-6a03-3253-b0fa-81f03e909c80 | -2.77577 | -54.09716 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 17febdf0-862b-3058-92b6-e7e890345850 | -3.12248 | -53.70284 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a1a0c12-cd75-3a52-99c6-ca62885c7b2d | -3.67993 | -55.94737 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2c4d1ef1-6ce4-3d08-b2ea-9420939de349 | -3.0264 | -53.89512 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a958a849-d48b-3d33-ab8d-465421763ade | -3.13734 | -53.72316 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2c6aff0-fb25-3ad1-ad46-f102e3cdb39b | -2.55938 | -54.73696 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4d3d01e7-fd72-3c58-b536-5176ea96f4c9 | -3.07829 | -54.25559 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| d176bb21-f5b6-348a-8f44-3fa4cf9c03af | -3.6131 | -54.60379 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cb30e560-1733-3a42-9b6e-ca98d5565f05 | 2.26519 | -50.82044 | 2026-10-06 04:38:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 214e01e9-bd92-3c11-a9dc-7ecef9308b78 | -4.35932 | -47.77482 | 2026-10-06 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4bd6d52a-c484-3dbd-9faa-e66eb5616917 | -5.22899 | -48.39541 | 2026-10-06 04:38:00 | NOAA-20 | SÃO SEBASTIÃO DO TOCANTINS | TOCANTINS | Brasil | 1720309 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bbb0e39b-3533-3140-bc35-0d60993b6b29 | -3.59034 | -54.31657 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 81ad4825-049d-347a-ad81-7077bbf3e82f | 1.15487 | -50.74931 | 2026-10-06 04:38:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7820a1ae-4406-3899-a91b-4ecc9fc8a003 | -3.4931 | -54.61683 | 2026-10-06 04:38:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0bbc2ad2-b1a3-3103-8b32-e46b1a14852f | -2.84127 | -54.06973 | 2026-10-06 04:38:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 98ad2ccd-7359-3ca5-b3e2-5d81bab40115 | -2.99617 | -54.09769 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fadbf22f-4e41-33c8-86ab-71aaa4c664e1 | -3.68347 | -55.95741 | 2026-10-06 04:38:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| faa3783c-f331-3e0b-a417-f9a2a03a846a | -4.25457 | -50.80199 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 853f5494-5dbd-3006-a91a-ea0bedee344b | -2.99623 | -54.12909 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 39a75595-004a-325e-aa1a-d366a1a9192c | -2.8991 | -54.11745 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7ee4ff2c-2890-3ae4-a24f-8e9a1fd229bd | -3.16169 | -50.44382 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc9656e0-27bb-3ed1-b305-7fbd7d54c591 | -3.07679 | -54.15219 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 56bf8a9f-c20f-3066-a351-4c60eb3b9d6a | -2.94907 | -54.15684 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6cd59652-5848-3adb-9fe2-2bfe366a7aed | -2.87782 | -54.13314 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 303e295a-e209-36aa-873e-6cf8b18c1570 | -4.06155 | -54.05287 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 96218174-7fe4-3340-9725-5f78ec7a0635 | -3.09256 | -54.17121 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1c0f0e9-37f2-3d23-8f0b-de7a263ca50e | -3.11247 | -53.76382 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7acd3485-9244-3d13-b002-caa0900389e3 | -3.07527 | -54.16156 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0dbf2bf-6a87-3a18-861c-bab116ae2cc8 | -3.16391 | -50.43906 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0f7513b4-b1e7-3260-b64c-7b8939e46f23 | -5.60159 | -45.37421 | 2026-10-06 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8747e298-e272-30f1-93ad-376356ea830e | -2.87422 | -54.15453 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| eee65d6d-22d0-3766-95b7-af27292f8b94 | -5.97544 | -41.36613 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| bd06246d-249b-3e62-b15c-ce36087fd709 | -3.00536 | -54.13056 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| ece52634-bbbd-36de-9703-9dbbb47ebf3a | -3.15743 | -50.44735 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 89331d96-e19a-355a-82cc-786ca15c8d42 | -4.02195 | -44.82432 | 2026-10-06 04:38:00 | NOAA-20 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6d52bc52-6699-3970-9923-6c9d90b5f74f | -3.09636 | -54.17654 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 16db78fb-933b-3961-b922-d18730c7b015 | -3.57581 | -53.131 | 2026-10-06 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0f3ffaf7-9d30-3a79-bcf7-08b6d22b5d3a | -3.05548 | -54.22533 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 34778437-2653-3b5f-9f9b-644130a28961 | -2.92094 | -54.1281 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 2cb1c826-7e43-336c-85b7-5a31fe69866f | -2.17733 | -48.14119 | 2026-10-06 04:38:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee1be490-0875-3d18-93eb-af9f017858cf | -3.16529 | -50.44442 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b49d6e69-7e29-3df2-a2f9-0408f0dacff8 | -4.14999 | -54.03462 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3c51bab1-dc00-38fc-896c-a0cfa72ec249 | -3.06074 | -54.25096 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 084ef505-95d7-3716-b740-ef7154c2f5c9 | -3.10192 | -53.71729 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6b54d25-ce1f-3f8c-82ae-41abf7aad246 | -3.46143 | -50.10544 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a6b1d62-ff9d-3b40-8c51-4677ffcf424d | -3.28238 | -50.40152 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32f9c18a-e045-3c94-81b1-8e25a0563a5c | -3.09822 | -53.71222 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 42dfd6f3-2416-3b88-8b53-b185340a940d | -3.27643 | -50.01722 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb7fd80-0223-3166-90b1-176cabb6b369 | -3.2691 | -54.01456 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cb9029e0-d7eb-3a04-b6d0-47dc0570265a | -4.2323 | -49.97827 | 2026-10-06 04:38:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8fa25d9e-cce0-303b-a3db-6e4c709f104f | -3.00079 | -54.12982 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 52865205-5e5a-33b8-9540-0a11558842d8 | -3.12207 | -53.7609 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a6312a5c-07f3-377d-811a-27e4d6c0b6c2 | -3.22123 | -54.30251 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 21723acc-805b-336e-8e3c-82fa44feed2c | -3.16298 | -50.43568 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fffd33e4-9248-3312-bfca-2f1a75d3b737 | -3.07382 | -54.25764 | 2026-10-06 04:38:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6664f986-5f16-3093-a2e2-8b26f47646ca | -5.12303 | -43.99562 | 2026-10-06 04:38:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0332e8a8-2308-3c8f-81ff-bba407644eab | -3.0463 | -54.22381 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 74aa1b4f-0ea3-3b36-9638-ca6462476119 | -5.08586 | -46.04411 | 2026-10-06 04:38:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2e1e9c0-19fe-3a0f-bfb6-8c83ecb0e26b | -2.79616 | -54.14374 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 914d88f1-5f50-3c8f-8940-b47cacb7b0ea | -3.35161 | -59.50186 | 2026-10-06 04:38:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 94e85113-5d15-363a-a24f-38d5cca8d034 | -4.5084 | -43.6886 | 2026-10-06 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc19d361-8cc5-3b98-9ec9-4ee4368b28a6 | -2.9187 | -54.11334 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 15f71d25-b429-376c-92b3-6562f19c6b36 | -5.94796 | -41.36646 | 2026-10-06 04:38:00 | NOAA-20 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6596e60d-4e87-3a51-83ea-6caa478e717d | -4.50394 | -43.69257 | 2026-10-06 04:38:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3c1ec7e4-c6f4-3e32-b83f-6e69dc91ca6a | -3.50679 | -51.67566 | 2026-10-06 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 24331263-b071-31e5-b807-e0bfd20dacc8 | -3.47107 | -50.09072 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cc911fda-f3ea-3bd5-93e2-5918149eaae5 | -5.07799 | -45.17517 | 2026-10-06 04:38:00 | NOAA-20 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb7edec5-2e72-3732-b9de-1236d7eeea1b | -3.02467 | -53.89183 | 2026-10-06 04:38:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 70a8d197-a86f-3a7b-865e-b2fb00213624 | -3.27272 | -50.40555 | 2026-10-06 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6e737260-e6f2-32b0-bedd-6323ec5e403a | -3.00007 | -54.13169 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 9b7c5b8a-7979-3f23-9ee9-be01d28e45ac | -3.09558 | -54.18119 | 2026-10-06 04:38:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e531f570-b93e-3a67-8b72-b239854d30fa | -1.62405 | -55.13076 | 2026-10-06 04:38:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2dcf0abb-563e-3885-8d3b-275945e05fbc | -3.38317 | -58.20308 | 2026-10-06 04:38:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| fd9840ef-e711-31fb-a4cb-e5c8dda9d306 | -3.84034 | -50.31447 | 2026-10-06 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README45.md)
