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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| efc53ae3-3806-3312-b8e5-599e20474c7d | -3.5037 | -51.095501 | 2024-10-17 00:22:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b240926-c4c5-3bb2-be4d-d9860743370a | -3.5061 | -51.1068 | 2024-10-17 00:22:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cb34f18c-a534-332d-b3e2-65e5ce92b7e1 | -3.5438 | -51.278 | 2024-10-17 00:22:07 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 138223f1-c312-3357-ba2b-eb0be5add4b5 | -3.4914 | -51.086498 | 2024-10-17 00:22:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3c69b5f4-f798-3b4f-bc32-f08c830ea256 | -3.4939 | -51.097698 | 2024-10-17 00:22:07 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 551a24fb-4d7c-3a1f-8055-916de0942ebc | -3.534 | -51.280102 | 2024-10-17 00:22:07 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 776df64b-d2bd-3f24-9b3f-30fe98f13cca | -2.6288 | -47.622601 | 2024-10-17 00:22:08 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fa09e65-2333-3271-8026-20d5f80c247f | -2.913 | -48.755501 | 2024-10-17 00:22:08 | METOP-B | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eff81777-e4e1-3678-b5e9-48f92fab53eb | -2.6304 | -47.629902 | 2024-10-17 00:22:08 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 778c6cf9-838a-3606-9427-abd72a18f3cc | -2.3729 | -46.483398 | 2024-10-17 00:22:08 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce12f005-efcd-3c51-88a3-7ac1bbb3a9d3 | -2.3615 | -46.478699 | 2024-10-17 00:22:09 | METOP-B | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8bffc735-d8ad-3d57-9ef2-191d2f82cc34 | -2.4481 | -46.909199 | 2024-10-17 00:22:09 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 635b2089-7453-31c3-803f-9eb2c1b39d18 | -2.5558 | -47.388901 | 2024-10-17 00:22:09 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 476d028e-aded-3942-bffe-5fdffa3b3c91 | -3.1807 | -50.190601 | 2024-10-17 00:22:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d3db156-57b6-35df-81f2-b52d6fb65b41 | -3.1829 | -50.200401 | 2024-10-17 00:22:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7394b669-4c84-3f9a-9d33-154191557e50 | -3.2157 | -50.348598 | 2024-10-17 00:22:09 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f45c4c91-6878-3a07-82fe-6a3a4c302d33 | -3.4926 | -51.650002 | 2024-10-17 00:22:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aa4c84aa-50c8-35e4-a22e-e678ae1ff431 | -3.4953 | -51.662201 | 2024-10-17 00:22:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 37d6165e-63bf-3cbf-a453-9b10d37494dd | -3.4855 | -51.664398 | 2024-10-17 00:22:09 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21b232db-8b80-301b-8f86-182860ca3a16 | -2.8434 | -49.134899 | 2024-10-17 00:22:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 427fb0ae-6a83-34f4-93d7-a8d2eaf60f47 | -2.8453 | -49.143398 | 2024-10-17 00:22:10 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7a73ad5-5239-31cd-bec0-ca2fdf960e39 | -2.8336 | -49.1371 | 2024-10-17 00:22:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ada8d80c-7263-3700-83c7-2414160022a9 | -2.8355 | -49.145599 | 2024-10-17 00:22:11 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c42256ab-d00e-391c-a932-18189a12ed5b | -2.6037 | -48.245701 | 2024-10-17 00:22:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c7c18e4-923a-383f-ba8d-68c2c0a143ea | -2.6054 | -48.2533 | 2024-10-17 00:22:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e72ff28d-d803-3a0c-bfcc-e77543c658b4 | -2.6071 | -48.261002 | 2024-10-17 00:22:11 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a157935-14fc-3d2f-84cc-d44e6b82c810 | -3.072 | -50.3484 | 2024-10-17 00:22:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 71d4b917-d46d-3898-a781-ec908ee27ead | -3.0742 | -50.358398 | 2024-10-17 00:22:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 95949b4c-40cd-3314-9e98-d82718f8466d | -2.2572 | -46.747398 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d865a59a-7f9c-3298-9a24-418074950a10 | -2.2588 | -46.754398 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 914dcdf2-0767-3aa4-bcd1-581be394519b | -3.0644 | -50.3605 | 2024-10-17 00:22:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| abec58aa-ded7-36ac-b6ff-f555ee741b6c | -3.0764 | -50.368301 | 2024-10-17 00:22:11 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e35d5d2-7f10-3ae9-ad81-f880d0d6afd1 | -2.251 | -46.719799 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cad9eb6-3b85-355e-beb7-8e2230f5f2b3 | -2.2525 | -46.7267 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c91e407-ce60-32d9-a9a0-d3219de2ff00 | -2.2541 | -46.733601 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e8933d8-9851-3c2f-b174-aa34530d529a | -2.2556 | -46.740501 | 2024-10-17 00:22:11 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc360cb7-07fb-34ff-9e8a-8f95f4156c93 | -2.4605 | -47.8363 | 2024-10-17 00:22:12 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a53760c0-f5a5-32e9-be72-395c5d130a8c | -2.834 | -49.508099 | 2024-10-17 00:22:12 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f1cc2c4c-9c87-33d4-bdad-04ae67dc95d7 | -2.8359 | -49.516899 | 2024-10-17 00:22:12 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cc54c6b-138a-39da-a8c1-23af29d3d668 | -2.4048 | -47.633801 | 2024-10-17 00:22:12 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 12525d1a-759a-3c47-a9b5-2254b7cf3eb2 | -2.8242 | -49.510201 | 2024-10-17 00:22:12 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1ccb288e-544f-3893-bac6-1c0b2e9472bf | -2.8261 | -49.519001 | 2024-10-17 00:22:12 | METOP-B | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| adb76811-74a2-367f-b267-5ca9563f3fb9 | -2.1921 | -46.7328 | 2024-10-17 00:22:12 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3e35db8d-6c80-356e-ac7c-9924aa456590 | -2.1936 | -46.7397 | 2024-10-17 00:22:12 | METOP-B | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8a4d279-6dcd-34b3-8b02-0a7abb037a48 | -2.3917 | -47.712898 | 2024-10-17 00:22:13 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6b38e37-d329-3b91-a419-29c81942f5df | -2.68 | -49.0476 | 2024-10-17 00:22:13 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 616070f4-9a16-30ff-95f9-4fbf4e11ef6c | -2.6819 | -49.055901 | 2024-10-17 00:22:13 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5eeebae7-9720-3a53-ab23-2a0e74104eeb | -2.4192 | -48.111 | 2024-10-17 00:22:14 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22c3a015-f24a-3083-a733-2770baf00506 | -2.6212 | -49.060501 | 2024-10-17 00:22:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1127b82a-d1d5-368f-bf29-80d0a9e499a0 | -2.623 | -49.068802 | 2024-10-17 00:22:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a226a0-6538-3346-9573-02189280c8ea | -2.5855 | -48.946899 | 2024-10-17 00:22:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84a9bf74-5794-3702-aa82-290348a53c46 | -2.6132 | -49.0709 | 2024-10-17 00:22:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 56214f7e-d5ea-3f5a-8240-b32aed11fa83 | -2.6151 | -49.079201 | 2024-10-17 00:22:14 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce8913fc-c2d2-3f4a-9349-03244c1f49b2 | -3.0857 | -51.197701 | 2024-10-17 00:22:14 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d4c7c0a-937a-3e07-bc3d-855547984167 | -2.4288 | -48.292099 | 2024-10-17 00:22:14 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 54c7e086-ce4f-3336-af75-25871bdebb5a | -2.6192 | -49.281898 | 2024-10-17 00:22:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91a55540-01f8-3c66-abcb-02da0180b5a3 | -2.6211 | -49.290401 | 2024-10-17 00:22:15 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 777aa4bd-b538-3935-bc90-95db8c93a97a | -2.9879 | -50.987202 | 2024-10-17 00:22:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 165859b4-5893-378a-9e2e-2ca8cc2ebf32 | -2.9903 | -50.9981 | 2024-10-17 00:22:15 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1eb225ca-419f-3f73-9ad2-e4ba8bec4b24 | -3.027 | -51.2104 | 2024-10-17 00:22:15 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78923285-bf3b-3aed-a80f-e44841bf2f88 | -3.0295 | -51.221699 | 2024-10-17 00:22:15 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 041c3fc7-614c-37eb-9c68-0c80714e99b2 | -2.6106 | -49.4739 | 2024-10-17 00:22:15 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0f54047-0fe0-39cc-a5cd-6dd3f154509f | -2.6126 | -49.4827 | 2024-10-17 00:22:15 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 09ce3af7-eef0-3399-b905-a7c1c4d99647 | -2.232 | -48.010799 | 2024-10-17 00:22:16 | METOP-B | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 691c0eed-0106-3bb1-9f21-d495ee3c74ed | -2.4148 | -48.873001 | 2024-10-17 00:22:16 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc748d06-45c3-3587-be39-86546b6dfdcf | -1.7527 | -46.154499 | 2024-10-17 00:22:17 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2ccd282c-5f17-337f-8885-157f167172f9 | -1.7542 | -46.161301 | 2024-10-17 00:22:17 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b666bc1b-cbe7-3f3d-baf4-4287385a4edc | -1.7413 | -46.149899 | 2024-10-17 00:22:17 | METOP-B | BOA VISTA DO GURUPI | MARANHÃO | Brasil | 2101970 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 5158ec20-639e-3e8a-a3a9-2a32b4e3ba64 | -2.4196 | -48.9403 | 2024-10-17 00:22:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04f11b45-cc56-3308-9b45-654441a2dbf6 | -2.4098 | -48.942402 | 2024-10-17 00:22:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b73c94f1-1e8e-385d-8dba-d7e3ab305dc5 | -2.4116 | -48.9506 | 2024-10-17 00:22:17 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| df316922-b48a-3e77-9fb6-61970c355670 | -3.3503 | -53.1889 | 2024-10-17 00:22:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ccd45fe-b9ce-30b5-9d0c-373da57ece8f | -3.3405 | -53.191002 | 2024-10-17 00:22:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d3d24e64-3325-35e4-9671-a41044641175 | -3.3439 | -53.206501 | 2024-10-17 00:22:17 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9695b15e-aa2a-3070-90bd-21d3e5a06c53 | -2.4837 | -49.365398 | 2024-10-17 00:22:17 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 901ac9df-ce56-3d43-bdd5-85b1c2aea0ea | -2.4856 | -49.374001 | 2024-10-17 00:22:17 | METOP-B | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 329f82d4-de6a-3594-8e4c-3af6b91b34a2 | -2.142 | -47.9762 | 2024-10-17 00:22:18 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a3ff86e-ec9a-3524-96ce-fc22aaef633b | -2.1436 | -47.983601 | 2024-10-17 00:22:18 | METOP-B | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3429875-13c0-38bc-976d-c81f8f4b696b | -1.6991 | -46.373901 | 2024-10-17 00:22:19 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 397c3647-27fd-3c9b-88d0-751b1104a4e5 | -1.7007 | -46.380699 | 2024-10-17 00:22:19 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8c90d240-5c76-3469-bdd3-3eb148929446 | -2.8824 | -51.667599 | 2024-10-17 00:22:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 716a8e7f-dd3f-3db3-821c-c2f88ddf82f6 | -2.1645 | -48.398399 | 2024-10-17 00:22:19 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 046fc860-a076-3aa2-be71-7fdb266cb54c | -2.8172 | -51.327 | 2024-10-17 00:22:19 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b75f58de-bb68-3eaf-98d7-2ce5f7943223 | -2.8921 | -51.665501 | 2024-10-17 00:22:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5fab517f-f281-38d1-9cff-41930eacefc4 | -2.8948 | -51.677502 | 2024-10-17 00:22:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 467df436-c172-374d-9f7c-1fb2b33e1e3b | -2.885 | -51.6796 | 2024-10-17 00:22:19 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6022a241-985b-3eb5-b7b7-2b86586c5830 | -3.0478 | -53.205399 | 2024-10-17 00:22:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 59e59edb-9562-3fbc-accd-bca503ae9b3c | -2.769 | -52.080601 | 2024-10-17 00:22:22 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 764826dc-47ea-32b8-932f-32dcfb10c05f | -2.7718 | -52.093399 | 2024-10-17 00:22:22 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 22e93cdf-19c0-36b1-a1ee-a1cfb0619cd5 | -3.061 | -53.2187 | 2024-10-17 00:22:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 26b9d644-c5a4-3f14-ae49-6c182988a23a | -1.7489 | -47.3727 | 2024-10-17 00:22:22 | METOP-B | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eaf6db6a-a711-3aa6-b67c-010e511c6244 | -3.0512 | -53.220798 | 2024-10-17 00:22:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2643cb7f-5e4f-3986-9665-fd2a401d80b1 | -3.0546 | -53.236198 | 2024-10-17 00:22:22 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0a83327-d81f-3b08-9bb1-62d585597815 | -2.7788 | -52.078499 | 2024-10-17 00:22:22 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfc45b5-8be4-30af-bd18-a261848c4f19 | -2.7816 | -52.091301 | 2024-10-17 00:22:22 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 40091efc-b975-3ab7-aca3-34561e345570 | -1.5537 | -46.9175 | 2024-10-17 00:22:23 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88fd70ae-1cd9-3ff7-af44-0be85dad1f26 | -3.1083 | -53.712399 | 2024-10-17 00:22:23 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cbb668a4-9a65-36c8-a0f2-3f89705dabff | -2.9446 | -54.126301 | 2024-10-17 00:22:27 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13215684-976c-37be-b9e3-e1a958e0d05e | -1.579 | -48.6325 | 2024-10-17 00:22:29 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fb21c83-bb5a-361e-8c02-9698c5412e03 | -1.5807 | -48.640202 | 2024-10-17 00:22:29 | METOP-B | BARCARENA | PARÁ | Brasil | 1501303 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
