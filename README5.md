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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eda8f23f-33d3-3768-be32-5eea69cf19db | 1.51754 | -59.94049 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 17fa7cbb-e321-3f74-9c5c-f5e1ff5ecda4 | 1.8815 | -60.91741 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3d2c6076-48cc-3f06-a714-697ade51d177 | 1.93826 | -60.86122 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd148c2c-c05c-33ff-94c3-733b549dc145 | 1.94138 | -60.8513 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d81769c7-9606-3e5a-b3a0-e4543ef70451 | 1.94234 | -60.36484 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79caf4c3-72fe-37a0-ac47-a65942cdac8d | 1.30688 | -60.39788 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cba49c5a-b32e-3257-868a-39e57b7e8a72 | 1.49636 | -59.94267 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 1c8d373f-c491-3f36-bd73-b55864efcbb6 | 1.88079 | -60.91272 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a388f9e1-a549-335e-a543-cc2d9c4dedd1 | 1.30754 | -60.4021 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc29f4f2-d74a-3e28-8918-3a1fe6f4bf76 | 3.13861 | -59.98672 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0294365f-2791-3427-8e27-0befe3f032a5 | 3.44976 | -59.89635 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 23e466fa-3210-389f-87fd-2b9c25b976d7 | 1.49399 | -59.95522 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 23.1 |
| c4c2ad81-5649-3df5-a324-9b351e8f26c3 | 1.49628 | -59.94355 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 32559b1b-8593-35a0-975d-f8d53c5d8864 | 1.49997 | -59.93802 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 43.8 |
| d73da07d-5325-3b60-974b-36622d8a8112 | 1.29331 | -60.4259 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93d05751-537c-3b93-90c4-bb1acac556d1 | 1.50478 | -59.94231 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 065d9877-3ed2-3ea6-86f2-f36c01993d9d | 2.23766 | -60.69939 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 489ba455-fd1d-3f29-b644-75dc466e6e80 | 1.63181 | -60.28267 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1e44a68a-6905-32b4-ad88-9c262b020aa8 | 3.13985 | -59.96495 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3a1eef2-7cc9-3c15-83d4-a9bb270754c0 | 3.13312 | -59.98627 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b6364b8c-1f8c-3060-a1ab-eef2e07f085a | 2.71768 | -60.2449 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 21f7db08-aeb6-34c9-96e7-972a9465d947 | 1.47635 | -59.95367 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| ad60facb-de17-3100-b215-0b85108e5275 | 1.48424 | -59.94853 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.0 |
| c6b86cdf-9f9e-35ac-8c2c-7815d1508287 | 3.4938 | -60.28966 | 2026-02-25 05:03:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ce83802e-185c-3f94-9b3e-1fd2f6ca9b40 | -2.71701 | -48.36092 | 2026-02-25 05:03:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd65dc53-9789-3b0e-8542-2cf068d75e3e | 3.05015 | -60.88411 | 2026-02-25 05:03:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dcea67d8-e692-3da4-82b0-74f16fdab846 | 1.49211 | -59.94328 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 38.7 |
| 20e8c8bf-e144-3b6b-8316-fc5c63984f29 | 1.49203 | -59.94418 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.2 |
| 9e1f68a7-b503-3b52-b62d-c25ba95b5d41 | 1.51814 | -59.94443 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| eccfc33a-ff58-3139-8b5c-6b55d31e9f5d | 1.94101 | -60.3562 | 2026-02-25 05:03:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae32fc57-3326-3464-9fd3-3550c49952d3 | 1.51874 | -59.94841 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73effb59-ff00-37ef-9e43-997529653a7b | 1.36387 | -60.2961 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| c4536a53-75bc-3d2c-abb5-35dd4cd8e3b4 | 1.50356 | -59.93421 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 18.3 |
| 7bd60ea1-6e3f-3250-beac-a4a004bab490 | 1.49082 | -59.93607 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 045ac14b-f699-3e28-a59b-ac3ebfcddd84 | 1.50173 | -59.9509 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 079c591a-78c6-3bdf-bb7a-9ecfd767ff42 | 1.51207 | -59.93309 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.5 |
| fe4dcc2c-2750-307a-b878-04d4c66f5946 | 1.51509 | -59.95302 | 2026-02-25 05:03:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 16565cc8-ca46-3b90-85df-fd27eb0b326c | 3.26399 | -59.92228 | 2026-02-25 05:03:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4cc0478c-bcd6-3c5d-9ef6-ce76d5d7dfc1 | 1.5046 | -59.9497 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 150.0 |
| bfb2dcca-b4c3-3902-aba0-e98a3a1dc78e | 1.4864 | -59.9498 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 123.8 |
| c6b2bead-d19f-3ba8-a8c4-1212808bb686 | 1.5047 | -59.9116 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 1c8d1d59-d60a-3279-9cc9-e2ecfbd4c04e | 1.5229 | -59.9305 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 68.6 |
| b6b29613-2ee9-3c78-81df-f44452f1ee49 | 1.5046 | -59.9306 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 286.8 |
| b4a8405b-3435-37bc-818e-9afd95d48be3 | 1.4864 | -59.9308 | 2026-02-25 05:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 170.3 |
| 5aa75c9f-1123-3538-911c-8c00b883cb61 | 1.4864 | -59.9498 | 2026-02-25 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 167.2 |
| 31fe674c-ddb8-3fe9-a8f5-237f224a6722 | 1.5229 | -59.9305 | 2026-02-25 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 591fa7d3-f089-3e36-9d92-8b1337ef9029 | 1.5046 | -59.9306 | 2026-02-25 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 242.8 |
| 9f346e5d-4213-3b75-90f6-d4a51554a63d | 1.5046 | -59.9497 | 2026-02-25 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 206.8 |
| 42eec3ac-2845-3322-8bc4-653588bc47bf | 1.4864 | -59.9308 | 2026-02-25 05:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 132.8 |
| 9b768134-daec-322f-be90-a9b9048c3f5e | 1.5046 | -59.9497 | 2026-02-25 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 166.4 |
| acaccbc7-1f05-34a8-851b-c2e66d45a22d | 1.4864 | -59.9498 | 2026-02-25 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 188.4 |
| 2fbb979a-e75c-3b96-b91d-b152a6cd90dd | 1.5229 | -59.9305 | 2026-02-25 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 010fd30d-5658-3d84-8061-0844b3f15feb | 1.4864 | -59.9308 | 2026-02-25 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 149.5 |
| a790f91d-b6e2-3163-97f1-2351b6145c71 | 1.5046 | -59.9306 | 2026-02-25 05:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 206.9 |
| ea3f5015-f4fd-3d27-81e1-63733cd97b31 | 4.23455 | -60.1882 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8f7d9d8e-fe0d-304d-a930-98e56687828a | 4.77767 | -60.15603 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 231f4f67-450e-3ac2-b183-f9fc37152681 | 4.25264 | -60.28115 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ac8c683-4338-372d-9a93-e3d0ed733977 | 3.88269 | -59.74154 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c197160a-028f-3036-b137-089c7df5c925 | 4.15339 | -60.29671 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25c4041f-7ce0-3485-9f97-93ebb4931ce0 | 4.0645 | -60.18652 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6325f42b-0d97-32ca-b661-0b77ad73712e | 4.2338 | -60.29125 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47259818-046d-3875-a504-9c08468b1f89 | 3.88546 | -59.73756 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae311e7c-56a1-36f6-bb84-a8ae5068bd23 | 4.06559 | -60.19344 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4bc43808-ad5f-3b36-b7e8-ea31e5218314 | 3.88215 | -59.73809 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 38444695-18f4-326e-95b6-90f5d7f4a846 | 4.06505 | -60.18998 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b04d89b3-6a3d-31e4-a594-53642fbc3da8 | 3.92015 | -60.4938 | 2026-02-25 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 48b000e5-2d18-30f0-a8f2-d049609fde80 | 4.29184 | -60.7686 | 2026-02-25 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a272e36c-cc0b-34b7-bd2f-518c5fead824 | 4.29574 | -60.77159 | 2026-02-25 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 46b7d65e-daa3-3915-a789-036dd810efc1 | 4.17574 | -61.40981 | 2026-02-25 05:31:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 6a736a52-3ab9-3165-9234-2447b074309d | 3.9329 | -60.05893 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 887d0487-969e-3e62-80ba-62a85ff44f0e | 4.23123 | -60.18873 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b7ed94ab-91e5-3a54-9b5c-d85da248959a | 3.92958 | -60.05944 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5afb3aa1-0fd3-3b3c-9061-85ce5f80be03 | 4.15284 | -60.29325 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6c4fa4c3-40bb-3485-b3e8-da97e738b779 | 4.12729 | -61.07797 | 2026-02-25 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb713d5a-ad99-3fd3-976b-b3128f1ee9de | 4.06891 | -60.19289 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35ba8449-a375-3ba2-8b8c-2f2276707e43 | 3.87937 | -59.74206 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8a6b35f0-726b-3711-99e0-7f4089400011 | 3.92626 | -60.05996 | 2026-02-25 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f359fdb-f8dc-3d5a-9962-b4de442a1c59 | 4.13122 | -61.08101 | 2026-02-25 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bb046b07-2132-3a2c-897f-f75c62eadf80 | 4.24932 | -60.2817 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a5d1d194-ed29-3bb0-9f8a-b09a1b0d9792 | 4.23712 | -60.29073 | 2026-02-25 05:31:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d8aab014-6716-38a2-8b2d-7a85e491cde9 | 3.05135 | -60.45904 | 2026-02-25 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 62cc1290-ad1a-37fb-9191-22886c6e5915 | 3.49924 | -60.29004 | 2026-02-25 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 024916b1-196a-33c5-9d35-fd5d2a6ea597 | 1.9396 | -60.35838 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7c860fb-a151-3dbe-b3d5-febd76198d89 | 1.51022 | -59.93419 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 60ded73a-6406-31da-ac4c-5f0805f13d28 | 1.51684 | -59.95439 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 405f2197-ae88-3b42-9805-9b08b5e21b54 | 1.93932 | -60.84644 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 27f15e59-f3a5-3e83-91c2-b0f1d35cfa7c | 1.97641 | -60.69893 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 71568894-44d4-3e44-8958-ff98ce212862 | 3.44636 | -59.91294 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9c2999b2-441c-3d5e-ae6a-8db055653212 | 3.67214 | -60.05723 | 2026-02-25 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e00401c3-cee5-3e0c-83fc-9d7df5a239ed | 1.50799 | -59.94161 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 8f731d4e-4a80-30b2-9869-b71f153479be | 1.49365 | -59.93389 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 1109bea3-7e07-385b-96cb-2cf39633b05c | 3.44859 | -59.90552 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e04cfdd6-8544-3b87-887f-dd9974992826 | 1.93351 | -60.36285 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 442e195e-d730-34f1-b0d1-f2f02bbab091 | 1.48309 | -59.95325 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 6203c46a-e790-39fb-a108-4b7f278e8d36 | 1.66843 | -60.48167 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 439f411f-a3ca-3b2f-8041-f244eb53d0cd | 2.23417 | -60.7008 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fe335a71-02b1-3dbc-8d43-e078ad6cf4b2 | 1.52225 | -60.03138 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0c490f5-fee5-3139-8ee3-4930883cf92d | 2.41075 | -61.82032 | 2026-02-25 05:33:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec6ef1ad-bcee-3ca2-934f-1c0425cd9366 | 1.50854 | -59.94506 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 2b107457-aa43-3e06-a62c-b1326d7f7126 | 1.49752 | -59.93682 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |


[Clique aqui para ver as próximas entradas](README6.md)
