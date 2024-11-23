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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 012a3f16-870e-3f96-9c5e-94947b14bb5e | -2.8237 | -54.015099 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| af25271e-a726-345e-8002-3be794fa123e | -1.2033 | -51.955898 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d195317b-3543-3df8-bd57-f1fccd8a7e01 | -3.808 | -51.991299 | 2024-11-23 00:45:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a3de8cd2-e739-3bfc-9e05-e2ac9dbd332a | -1.7879 | -53.627201 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ec62ff8c-9735-373d-b35c-5acec2a7209d | -3.1663 | -45.726799 | 2024-11-23 00:45:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 69ee602e-90c7-37d6-bc14-57b42fd08db9 | -2.7507 | -54.102901 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 274bf666-a25b-3e67-91c2-e46fcf6d3118 | -5.5671 | -50.939098 | 2024-11-23 00:45:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0356d50-3334-3586-b26c-91ef07e6850c | -1.3724 | -51.974998 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f6fd1ceb-0e2f-39d9-9a91-b36511e09ec7 | -2.7761 | -54.032799 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 04096328-2c3c-3a5d-8df2-6f13678b458c | -1.1855 | -51.967999 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f259032-2aed-3dc3-8382-ede35e1f4e11 | -0.2135 | -51.768902 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 494fc623-6480-3ab3-8063-cd2c8a665da8 | -4.7479 | -49.0919 | 2024-11-23 00:45:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2bd31315-8a23-375f-99f2-13f4917f9049 | -2.9438 | -45.089199 | 2024-11-23 00:45:00 | METOP-B | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f5fb2a33-b6e4-38c9-b18f-52138c3fe44a | -1.2604 | -51.753899 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 893bc0aa-5627-3fde-a740-176cae37a704 | -3.2773 | -45.719501 | 2024-11-23 00:45:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f97fcc9c-62bd-38d6-9136-8d961bbde52d | -3.3233 | -54.083099 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ae74ee07-6dd2-3e03-a36f-1a44936fb6f1 | -2.3778 | -54.4142 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66991f34-0148-39c7-9ab5-ff82edec0120 | -2.8221 | -45.18 | 2024-11-23 00:45:00 | METOP-B | SÃO BENTO | MARANHÃO | Brasil | 2110500 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7bd78068-15d0-3531-b000-03585c979a7c | -3.6406 | -50.2257 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9fa4f995-d922-38cf-a248-865013dab8b6 | -3.1563 | -50.583599 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61114955-6be7-3051-80f3-67a1211f9cfc | -4.2512 | -48.683399 | 2024-11-23 00:45:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a00a6703-8155-3002-8f86-7c424df3d638 | -4.6907 | -44.3951 | 2024-11-23 00:45:00 | METOP-B | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8543310f-042e-3c83-b1ff-98b8fdb0316c | -1.2211 | -51.943802 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d78a9950-585f-3aaf-b4cc-de5052b4d932 | -3.1912 | -54.319801 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d51f51ba-d3ff-3fff-a17c-22ccdf133974 | -4.0957 | -42.4562 | 2024-11-23 00:45:00 | METOP-B | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 1db4cdfc-3a00-33d8-b70b-c371061d208a | -0.9643 | -51.719799 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 3c417aaa-a9db-3a3a-af3d-3166aedb6b1e | -3.3096 | -54.4799 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afdb7ce8-1c4e-3ad8-a513-fd2bccea5877 | -2.7596 | -54.0508 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7569109d-b86a-30a1-80e8-c1e40de686b9 | -1.198 | -51.932598 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e7938b6-c4e0-3c9c-b7ff-8e28631e1f8c | -1.05 | -51.7342 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| b5934106-ea11-3910-b311-68c8ad66793d | -3.1799 | -54.315201 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ce6e4b1-55bb-33af-8279-efec6cdb5646 | -1.5092 | -52.033298 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa90ec97-f0df-3aed-89bb-51728694a488 | -3.1229 | -53.104801 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 468a6038-d02d-3b69-b113-0c0c03175d56 | -1.7801 | -53.592701 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 49e3a3c4-85cb-3e69-a4ca-8814348a0265 | -1.4458 | -53.390301 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d39d9d07-65dd-3501-b35b-e319c3630f75 | -1.3887 | -55.192299 | 2024-11-23 00:45:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9616648-a154-3f6c-9856-6020ce2ada4b | -1.214 | -51.730999 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 408c87fd-e095-30c8-9210-bd28b29ae6b2 | -3.4791 | -50.419498 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 52dfda4f-49f9-38dc-a1f8-3a86bc4337a2 | -2.9326 | -54.269798 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbdd120f-9198-3a66-9bc6-2112abb00cd4 | -1.6019 | -52.577599 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82b65744-1b5b-3955-8343-278ccd544ae0 | -1.4556 | -53.3881 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6117bc44-dc1b-3f47-b6ad-e00dfa055fb8 | -2.9341 | -54.2766 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 32fe79ef-5a65-3cff-afc9-c24890ff4892 | -1.1289 | -53.402 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 283d1db5-1b55-3a5c-88ae-2c3ba204caf7 | -3.7537 | -50.001499 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 70c21782-d284-35d2-930a-b658211225f3 | -3.1131 | -53.106998 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0c0a5fac-4cc4-3252-87bd-9bd803ff727d | -1.791 | -53.6409 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ef70ff4e-7fbc-3b91-b9f6-d8892a551ee1 | -2.7875 | -54.037498 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30451e90-3774-3883-ae60-2fe805bbc553 | -1.2844 | -51.723598 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0f437d13-c117-3085-8aac-5b0293c480f6 | -3.4707 | -48.248199 | 2024-11-23 00:45:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a40b46f4-082c-359b-b938-8a73e0c6c9bc | -1.296 | -51.729401 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6295f7d4-4544-3d7d-b7ef-e09272ab7b39 | -1.247 | -51.740299 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a33c9a17-7dfe-3bee-97cb-f411f37a855f | -0.9251 | -51.7285 | 2024-11-23 00:45:00 | METOP-B | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 979412fe-61dd-3b22-81a0-cac8368a1289 | -4.2732 | -46.287399 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2a8cba3c-b269-3972-895e-c9c5f39575d1 | -3.8477 | -43.953899 | 2024-11-23 00:45:00 | METOP-B | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 17990e90-4c61-3a3e-8448-87b2858578b1 | 0.1559 | -51.226601 | 2024-11-23 00:45:00 | METOP-B | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| bf021cba-0568-3943-8850-dd110bb6dfad | -2.7709 | -54.055401 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 870cbe13-65db-318a-82d2-8363f927629d | -3.0885 | -54.5504 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 23aaef79-39a6-3a12-8e42-bf2c5f62a321 | -3.1062 | -53.988201 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 638b47c7-8131-3dcd-8de7-ffe5bf28ba11 | -3.2244 | -53.918999 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f50a042-6435-3b7e-a10e-90ff841802da | -2.6012 | -45.6311 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2f3aeb90-5876-32e2-808c-fcd5968eadfa | -2.1701 | -54.452999 | 2024-11-23 00:45:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2a3424e-2824-3eeb-9594-bf49a7a432e6 | -2.2084 | -53.663799 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5019b859-e626-359d-a052-2ee6053c1fea | -3.3422 | -50.496101 | 2024-11-23 00:45:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 257131e5-cd57-321d-9f3b-1f069d9ca0b8 | -0.3978 | -51.582401 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 4be6daa0-5d95-340b-85c6-56e967c544f4 | -4.1031 | -51.072899 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3515b884-d25a-3835-9667-8c2a3464eed2 | -3.2348 | -54.238602 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01df5604-d18e-3200-938e-4406947467c9 | -4.6488 | -45.668098 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0fd42c4-8bfa-3b83-81ee-dba0813bf508 | -1.2256 | -51.736698 | 2024-11-23 00:45:00 | METOP-B | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c3909f6a-2991-3cc8-9eb0-c76bddb9b1b3 | -1.2113 | -51.9459 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a3f797f-7a70-3d1e-b511-1636426a394a | -1.6 | -52.251701 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b48a7822-19d2-3145-aa95-2ab540016310 | -4.0915 | -51.0672 | 2024-11-23 00:45:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7396e06-92c0-3817-b85f-07adb6111006 | -1.7329 | -52.701099 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19fcda26-534f-3e30-a5a7-cc6c71a4dafe | -0.9293 | -53.202702 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f26412e5-4f98-3f1b-9b56-17b83408a218 | -2.8537 | -53.9655 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e51d7b26-34bc-3a53-ac86-a8d07061eeaa | -3.5262 | -53.794701 | 2024-11-23 00:45:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 50573017-141d-3abd-8cd9-7a51188b6b97 | -1.7749 | -53.615601 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aebb2784-64cb-3046-99bf-c1df0cc0a549 | -2.5969 | -45.612801 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e96e1e93-f183-3cbf-9a49-ff1d0beca6b3 | -3.7234 | -46.045898 | 2024-11-23 00:45:00 | METOP-B | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53b0d9b6-1c78-3651-8e13-800a22af1b46 | -4.543 | -45.869301 | 2024-11-23 00:45:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 8f614503-f7cd-3bb6-bf0c-a76e82b36ff6 | -4.5124 | -42.908699 | 2024-11-23 00:45:00 | METOP-B | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f78c8d9-27f0-3d14-9335-4a1133858bc4 | -2.3762 | -54.407398 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac64c50e-1850-3008-b5fc-a503dc0f5ff0 | -3.2233 | -54.234001 | 2024-11-23 00:45:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78d21951-eef0-31f4-9ad8-deef7441a41f | -3.1829 | -54.3288 | 2024-11-23 00:45:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4252e88e-eca6-31a7-bdde-9e01a1575a3b | -6.143 | -46.672401 | 2024-11-23 00:45:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6b386fa2-fc2f-3bd3-b0b9-f4b71e361dea | -2.5402 | -53.992199 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 41300794-39be-304b-a7cb-aae627d1ad90 | -3.9754 | -49.002399 | 2024-11-23 00:45:00 | METOP-B | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab666083-9796-337a-acaa-420be4b470b2 | -3.287 | -45.717201 | 2024-11-23 00:45:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3906ddaf-438b-30c9-be13-10c569d06bd3 | -2.95 | -53.7076 | 2024-11-23 00:45:00 | METOP-B | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 073eeb71-6381-3e69-ab23-9c1789c7e5bb | -5.7416 | -46.242401 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 0f751db9-c5f3-38f2-a094-b026d015bc56 | -2.21 | -53.6707 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c706c43e-f61e-32e5-91f8-99b8c3da1dec | -1.1882 | -51.934799 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7348d392-cac6-3524-b279-6dcd2f9abeae | -2.9588 | -51.431301 | 2024-11-23 00:45:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 219dbb9b-ed5a-38ff-b5ef-30b8f4945fd9 | -1.1953 | -51.965801 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b3f9380e-289e-3971-b432-22cdd666905a | -2.7611 | -54.057598 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab600084-ac9a-325d-a683-a8612dd7c9f7 | -1.147 | -53.390598 | 2024-11-23 00:45:00 | METOP-B | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e4b4e168-8f05-3353-80c0-1be29dcbf1be | -4.6682 | -45.663399 | 2024-11-23 00:45:00 | METOP-B | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce117c2a-f8e2-348c-be76-adacdb738b1d | -5.7452 | -46.257198 | 2024-11-23 00:45:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 70cfc0e7-22cf-34fd-a356-35dd6f9ca703 | -2.5789 | -54.026501 | 2024-11-23 00:45:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1b7d7bee-4558-348a-a1b0-f331b4b6ecd4 | -0.2153 | -51.777 | 2024-11-23 00:45:00 | METOP-B | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 893802cc-d08f-343a-b7d9-41275f30733c | -2.6807 | -52.065102 | 2024-11-23 00:45:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README14.md)
