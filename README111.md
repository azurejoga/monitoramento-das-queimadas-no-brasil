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

## Dados Diários - Página 111

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f4b024c0-0551-3fae-8d1b-2904075226eb | -3.56633 | -54.34462 | 2024-10-08 05:21:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9afbf61d-bfb7-3d91-8aec-35a2f3b0e736 | -3.46666 | -53.80569 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 926a46eb-dd1d-3c0b-ab5d-7c072f50655b | -3.44018 | -54.0635 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19792408-d735-3e9a-a230-44cb403fe926 | -3.38155 | -54.90446 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6725d42e-9cc7-375b-b8a9-8cbc73f5a1ee | -3.38102 | -54.90796 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6d2ce0d2-aef1-3539-8e23-92fd8ca18ce0 | -3.37755 | -54.90388 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c82de320-8f4d-37cc-822a-185c50f5f8bb | -3.37701 | -54.90741 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f5617faa-5185-3f68-8a07-d0555ba8bb60 | -3.373 | -54.9069 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b07cfdd-0772-373b-88a1-7c64ab627bd2 | -3.37246 | -54.91045 | 2024-10-08 05:21:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d53863-746e-3a09-a764-8cd10db54be8 | -3.07233 | -54.77681 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20477df4-a8d9-3d45-a29e-d585cff12454 | -3.07125 | -54.78384 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e78e91d-b9fa-3b57-ad5f-d2ffd7f55a8f | -3.06831 | -54.7762 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 10211ba7-9ab4-34f3-b3a5-2722809886af | -3.0643 | -54.77556 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a92476c5-1bdf-35a2-9389-1e10fe9e9533 | -2.90433 | -54.00304 | 2024-10-08 05:21:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 710259b1-0d29-3049-887c-e368b23662f5 | -2.81536 | -54.35998 | 2024-10-08 05:21:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18023110-6ab1-3b96-a718-ff030d68660e | -1.66724 | -55.14085 | 2024-10-08 05:21:00 | NOAA-20 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e236252c-caa1-3bd3-ae47-e9c92ce52203 | -1.26158 | -55.85485 | 2024-10-08 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e04d5c81-8298-3efe-9ad6-f2a7405d945c | -1.25791 | -55.85428 | 2024-10-08 05:21:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f07477ce-83e0-3af9-bbb0-85ca65077b23 | -3.86129 | -55.79022 | 2024-10-08 05:21:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 224d63de-b4ca-320d-9228-941d0b662e4e | -2.74324 | -58.18408 | 2024-10-08 05:21:00 | NOAA-20 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5fee38ae-254c-3c3b-9434-83146acede09 | -2.543 | -57.87242 | 2024-10-08 05:21:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f480c9f8-cdcd-36ca-8848-3c219fe6965c | -2.36353 | -57.12834 | 2024-10-08 05:21:00 | NOAA-20 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2d6e103b-57ad-3fd5-a7ff-2bd651270575 | -3.46631 | -59.81726 | 2024-10-08 05:21:00 | NOAA-20 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9d6fcc33-fa60-3c41-a76e-c0ee60af0d22 | -3.17784 | -58.96948 | 2024-10-08 05:21:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ffedca9d-bd78-32c3-a55c-57eeb1abfbdb | -3.1158 | -59.43083 | 2024-10-08 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6664f6b8-8f27-3f79-85aa-d54c56307201 | -2.68487 | -59.57826 | 2024-10-08 05:21:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5534c457-eab5-3b29-b6c8-9f44f09aa00e | -4.28727 | -60.01986 | 2024-10-08 05:21:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1758475c-3b3a-3297-99c4-15ca8163605e | -4.54414 | -59.91944 | 2024-10-08 05:21:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bac34ab7-15e8-388c-a7f1-ae90e1fcfdaa | -2.95598 | -60.01538 | 2024-10-08 05:21:00 | NOAA-20 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e38d0bf9-25e5-315f-ab9f-efe687e5dd50 | -2.2475 | -60.02763 | 2024-10-08 05:21:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8b4408ea-1fca-317e-b26d-3ad3c704e5ba | -3.3235 | -60.22829 | 2024-10-08 05:21:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0b06cfdf-a00d-3b8d-8549-d03fb5f84ead | -3.09579 | -61.02588 | 2024-10-08 05:21:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 60667246-d717-34d7-a0bf-a547f39f8181 | -2.24804 | -60.02419 | 2024-10-08 05:21:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7255041b-6367-31c8-bde8-b2dbc3c7a939 | -3.89432 | -60.59458 | 2024-10-08 05:21:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87371ff5-9507-31c9-a3d7-0ec7f914afd0 | -3.88437 | -60.59303 | 2024-10-08 05:21:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 62d7ec90-bc80-36b5-8934-903631211f3b | -3.891 | -60.59406 | 2024-10-08 05:21:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4e09db7a-cd56-39b3-801f-472237c5985f | -3.88768 | -60.59354 | 2024-10-08 05:21:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a4872fb-b015-368d-946b-c99eb4e93785 | -3.29011 | -61.59545 | 2024-10-08 05:21:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d49f4421-0e65-37b6-9b63-7adaecc9885c | -3.60111 | -64.42708 | 2024-10-08 05:21:00 | NOAA-20 | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6294ee5c-3301-39c2-b2a7-70578670625f | -9.40449 | -66.54866 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df72f3dc-289e-3822-b58c-c37cd6648432 | -9.40191 | -66.54543 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cc970f79-17d9-3020-afbc-307330b98193 | -9.40128 | -66.54916 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e39294fe-e677-3f9b-8eec-9bbbc688b1aa | -9.40104 | -66.54424 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dcccfce8-5763-344b-af30-e6d134c4457b | -9.40066 | -66.55287 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4f782a81-abd7-3573-a2ed-fc719453a033 | -9.40039 | -66.54795 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a0f8d19b-7219-341b-a87f-3d8a5bf9a6dc | -9.39974 | -66.55167 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a07a2c9f-ccf7-377e-8c08-4172291ac731 | -9.39718 | -66.54845 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| dfa9100d-d115-3a77-9e8f-ec067e7fea84 | -9.15744 | -66.06161 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 906caa03-4b84-34d6-8bfe-2dc1cfc14035 | -8.74832 | -66.59577 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0cba7ac1-4c51-30f5-ab34-0ad79e1acd55 | -10.34534 | -67.54597 | 2024-10-08 05:23:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d59edfb7-ebe0-371a-9867-1083037b229d | -9.71744 | -66.58076 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 27e8bc33-2d18-3cf3-b6f2-1b34d073af8e | -9.71727 | -66.57634 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 4d47f976-c117-32c9-873a-ee51322fca80 | -9.71662 | -66.58002 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5faa9c83-96c3-360d-82f1-664b55c85e63 | -9.71399 | -66.57626 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf2eefad-b992-3e09-b910-ee36e165393d | -9.71337 | -66.57993 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 12c0f0fc-c077-398d-a0d0-d0c7c49b6aa7 | -9.71274 | -66.58364 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4c050ccd-de57-3f5b-abf0-91e914427787 | -9.61516 | -66.41945 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4877399-a87e-3393-891b-9deb74313ab8 | -9.58963 | -66.42225 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 775af7cc-8e20-3259-b544-4d12329b3dee | -9.58621 | -66.41787 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fa4e0c7-707e-374b-ba40-949df0b59f4e | -9.58558 | -66.4215 | 2024-10-08 05:23:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b75894d-822e-342f-bbbe-18e3ddcdeb45 | -9.40514 | -66.54495 | 2024-10-08 05:23:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3952c76f-b72f-3bc3-bf36-423193ee4233 | -9.04764 | -67.75124 | 2024-10-08 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a7570783-f1b6-3796-9260-beeb36243952 | -9.04395 | -67.74593 | 2024-10-08 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 29750151-4edd-3b04-a84d-0bd803bc657c | -9.04317 | -67.75044 | 2024-10-08 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 433ee45c-769a-37c1-a0cf-2884a39abd35 | -8.80617 | -67.50298 | 2024-10-08 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 530f6989-8541-37bb-b0d3-f210b518f83f | -8.79174 | -67.73659 | 2024-10-08 05:23:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c1a90a7-0e5f-32c9-8f6d-5c62f65938fd | -10.82742 | -68.36145 | 2024-10-08 05:23:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc863449-69b6-357f-b8cc-691f901713b7 | -10.82658 | -68.35843 | 2024-10-08 05:23:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7650128b-f1ae-3b01-9448-44ca1fdb403b | -10.82578 | -68.36297 | 2024-10-08 05:23:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 20ba30d8-fe79-34cf-9d47-91e411d38570 | -10.82291 | -68.36062 | 2024-10-08 05:23:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 461493f2-71ec-381a-bbd2-5a189b7709fd | -12.16334 | -47.76292 | 2024-10-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bebe7d55-9b44-337f-ac89-5ab7f40e28e3 | -12.16235 | -47.77184 | 2024-10-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| aff4c73f-8c5a-3242-b303-5118e089a90c | -12.1589 | -47.76152 | 2024-10-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c44ace65-1840-35b1-b537-5d257ccb1a5a | -12.158 | -47.77021 | 2024-10-08 05:23:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f6a8512c-ecb3-3116-9c85-f4230c4da1c0 | -6.66651 | -47.11322 | 2024-10-08 05:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 212758af-235f-32ad-88b2-b8081e1626ff | -6.661 | -47.11062 | 2024-10-08 05:23:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e04e60e-28bc-3ff8-9677-c61d286786a4 | -6.65954 | -47.11204 | 2024-10-08 05:23:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4654e436-e4e0-36f1-9f6b-66937df48919 | -19.71205 | -50.38192 | 2024-10-08 05:23:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| d42c0747-3d0d-37cc-80bd-7779255b9c48 | -19.71151 | -50.38845 | 2024-10-08 05:23:00 | NOAA-20 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 1d2bf843-6cee-3c2c-92e7-49a33ab4fb13 | -8.74855 | -49.78299 | 2024-10-08 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f04c5825-d775-33e7-8955-496c39c20f44 | -8.74825 | -49.78338 | 2024-10-08 05:23:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 3462a439-fbe9-34e1-b904-da80c014f0fb | -8.16535 | -49.46833 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 54fa24f4-e87c-351e-9393-522423981c68 | -8.16472 | -49.47309 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b9811036-0969-3ccb-8719-bfd35bdaa08f | -8.16463 | -49.46535 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1d1310fd-7da3-38ec-83ab-4ff66aaf1676 | -8.16403 | -49.47015 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 4cf7a48c-d2a9-39f3-9062-5923673f6526 | -8.15979 | -49.46284 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 94a2c5fc-158b-3b9d-aa43-810051428e21 | -8.15915 | -49.46763 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 7335bb6f-6dd7-3ab0-b4d2-8fe385a5f76e | -8.15844 | -49.46458 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fc908567-99a0-3a0b-929c-604aa62687c1 | -8.15783 | -49.46938 | 2024-10-08 05:23:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 528e2455-bc98-32f9-aec9-dc0fb19adbca | -8.60496 | -48.8486 | 2024-10-08 05:23:00 | NOAA-20 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dd08f6a5-6d7f-341b-bb5f-7f6189b11646 | -8.59852 | -48.84756 | 2024-10-08 05:23:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f32aa55-8053-3729-8633-c04f50042685 | -12.11015 | -50.89966 | 2024-10-08 05:23:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bac77ef-914b-30a4-b5f6-fe9d2df55b4d | -12.10962 | -50.90407 | 2024-10-08 05:23:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 240fcd17-6f7e-31cc-b9a5-ea1e9ac45618 | -16.30276 | -51.45678 | 2024-10-08 05:23:00 | NOAA-20 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cd975618-b2c6-3caa-9984-0e32cb62bfdc | -16.30231 | -51.46126 | 2024-10-08 05:23:00 | NOAA-20 | DIORAMA | GOIÁS | Brasil | 5207105 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 289e2c46-56eb-3840-9181-068febc63a91 | -17.36412 | -52.00465 | 2024-10-08 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42a24c6b-ccda-31f6-8ab0-18c1d9bb0816 | -17.36366 | -52.00914 | 2024-10-08 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5a329f53-f186-32d3-a698-637d14af2467 | -17.3582 | -52.00412 | 2024-10-08 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c4b035ea-0eac-3989-8f79-b301a2167a48 | -17.35772 | -52.00875 | 2024-10-08 05:23:00 | NOAA-20 | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e1dc97d3-fa7b-32be-8e0c-71b8a332a783 | -19.38628 | -51.69934 | 2024-10-08 05:23:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README112.md)
