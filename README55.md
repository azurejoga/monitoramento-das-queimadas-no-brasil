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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab13e774-4352-3bad-abe1-e07b8b45e05f | -18.30006 | -56.14574 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b9de8b38-8a17-3c39-936b-3e44655b4fe1 | -18.26802 | -56.04928 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 0616521b-92c5-3f08-b585-2f587645b730 | -18.1726 | -56.3083 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0b9efddd-72e8-3ca0-877a-28505e93bb5b | -19.66312 | -56.85429 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| da9e5302-cad2-37b1-bd93-747aa2e5b674 | -19.66055 | -56.79973 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 79752ff1-69fa-3ffc-afc1-1405bdb2329e | -19.65944 | -56.98826 | 2024-10-24 04:38:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6de0ecb5-7919-3b4c-b4e1-c7eb9b07f870 | -19.65897 | -56.85341 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 66b36135-44db-32ec-886c-f6b46c085b11 | -19.65821 | -56.85742 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 36f678c3-2269-3e7f-b606-9a4a954f6626 | -19.65793 | -56.79089 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a23cf48b-7cd7-3562-b1eb-f897201637aa | -19.65717 | -56.79488 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 6c1fc590-6ee7-3555-9af2-cfbd53c8a777 | -19.65641 | -56.79886 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.1 |
| 2004ef37-676f-371c-87b2-0f0a1da90b97 | -19.65565 | -56.80285 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.4 |
| aae908b6-cf72-38bd-9aa6-9e7095e18891 | -19.65526 | -56.98737 | 2024-10-24 04:38:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 72b84442-566a-395d-b26a-6ffc23ed6516 | -19.65482 | -56.85254 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 03895990-cff6-314d-9b01-c4eea0112d0a | -19.65455 | -56.78605 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| f93155d2-c3c9-341b-9a0e-f6b620d78139 | -19.65448 | -56.99146 | 2024-10-24 04:38:00 | NOAA-21 | MIRANDA | MATO GROSSO DO SUL | Brasil | 5005608 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1269bac3-ee56-3cc1-ae2d-e0a441376a40 | -19.65405 | -56.85655 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 844f6258-9262-31ad-9de1-f49d73606482 | -19.65379 | -56.79002 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 9dd2e1af-58a5-35ab-95e3-d9ae184e219a | -19.65371 | -56.83565 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 2a02a4e9-69fa-3ab0-8cc0-b0b57feb7a0f | -19.65295 | -56.83965 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8214b665-9c34-309c-ab85-b203296798b3 | -19.65228 | -56.79799 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 2b1535ec-770f-38e8-871b-a19a6493a570 | -19.65219 | -56.84365 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f99f4f02-4080-3ff8-9a0a-136d2ff881ef | -19.65151 | -56.80197 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 7366f62b-e905-36ac-9dee-1258716d10a6 | -19.65143 | -56.84766 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 94d9a365-5fb6-35db-8afd-d52ed6c7aad2 | -19.65075 | -56.80596 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| af36772f-611f-3acd-898d-ef7242d6829c | -19.65067 | -56.85167 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 04960541-c906-35db-9b0a-b9998373ce0f | -19.65042 | -56.78518 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 991d6a06-48d4-3222-80ba-8e7ae750f2de | -19.64999 | -56.80995 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 51591d02-7b92-35ac-ade8-133afc024878 | -19.6499 | -56.85567 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 4b1b7c00-36ed-346b-b8a4-7d6373d742d0 | -19.64966 | -56.78916 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 21efda07-cdfb-33c5-8a74-cf435b246948 | -19.64957 | -56.83477 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 7caafc42-1f32-38b0-a65c-d456d5b866cf | -19.64923 | -56.81394 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 83363293-52a8-3f17-ae01-ffe1d46423c3 | -19.6489 | -56.79314 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 834e001d-4116-380d-9d02-2414f5254367 | -19.64881 | -56.83878 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 6f75eb79-7ada-332b-b06e-3078a69be18f | -19.64847 | -56.81792 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 7738e0fa-e471-3531-85b5-37e7d0a1683f | -19.64804 | -56.84277 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 836fe970-dd9f-37f3-8c39-b39e64372840 | -19.64738 | -56.8011 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| a02e53c2-b2ee-326e-957d-05dbd0160618 | -19.64728 | -56.84677 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| b2b9f4ea-b207-33d1-84fa-f4625d1e1a54 | -19.64662 | -56.80508 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 35d4ab62-05c7-3cc3-aee7-371c9bbfa61e | -19.64651 | -56.85079 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 77edc15c-a5cd-36ba-913a-4714b16833e3 | -19.64628 | -56.78431 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| b1bd849b-2a6d-3f0b-b7d8-9fa03cc29705 | -19.64585 | -56.80907 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| db71a275-c6ee-30d6-891d-388043507037 | -19.64575 | -56.8548 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.4 |
| cd795dd9-7eeb-35fe-8882-082f93d8ba93 | -19.64552 | -56.78829 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 707aae9c-5525-3c82-a192-94d351bddd8f | -19.64542 | -56.8339 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| ca1ef732-e8e0-3b54-858c-343b6f08ea92 | -19.64509 | -56.81306 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 0795c844-d38a-32d0-a9f2-e35fe0ba013a | -19.64476 | -56.79227 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2004c000-62a0-3305-8f2e-431aefda7871 | -19.64433 | -56.81705 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 285704a8-4a65-3f0b-883d-7afb09627783 | -19.644 | -56.79625 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 777c61e9-0976-3027-9f2b-fb2cdde61c64 | -19.64357 | -56.82104 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 959b9a26-97e2-35e3-88a8-192f5fc54444 | -19.64324 | -56.80023 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ba2a47fd-7f0a-322d-b144-8d73d352071d | -19.64313 | -56.8459 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| c725d777-94b8-3176-9543-00ad2c2f13eb | -19.64248 | -56.80421 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 2196a83b-8fa2-3abf-b9e0-ceb90afc6a6a | -19.64236 | -56.84991 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 818d8db4-61bb-3eac-af9a-f6425f07fe4a | -19.64171 | -56.8082 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ae0293fd-8c00-353b-9621-bc98ec7cbc56 | -19.6416 | -56.85392 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| bf9ec962-a075-3ed2-a680-1ed50bd822c1 | -19.64128 | -56.83303 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| fd2da29a-5ac2-37f3-910f-915b6c488926 | -19.64095 | -56.81219 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 586fef20-f15c-32a1-a713-d149b3c287a3 | -19.63942 | -56.82017 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5a5bb704-7d95-36cf-9e5f-e343162c1b50 | -19.63898 | -56.84504 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 74ad76a1-36a6-39cf-ae3f-dba0cc7ef85a | -19.63866 | -56.82417 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 12f7a8b7-5c36-3d26-9f61-5eb12926b3b7 | -19.63834 | -56.80335 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 21a095c0-bd15-35b0-8179-37d3935bcbd6 | -19.63821 | -56.84904 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| 0b49d1c3-4cc0-3d93-af39-e7362c117984 | -19.6379 | -56.82816 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 589ba3a9-462e-3cdd-9d47-cdbb14c61651 | -19.63774 | -56.98791 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 6.3 |
| 69d5ceed-b7d9-3fbf-9f7e-2b5db3ea871d | -19.63757 | -56.80733 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| a0e80177-82bd-343f-b830-0dcf22dab28e | -19.63745 | -56.85305 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 13.0 |
| b7f86453-fa7c-30c5-be9b-abf6389995b5 | -19.63713 | -56.83215 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 24cd3626-799a-3f63-b7e4-c61969a4060f | -19.63605 | -56.81531 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 9f78cc2b-73a6-3c95-b95d-f09a0aee553b | -19.63528 | -56.8193 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| baf5f0e8-f7d7-33a1-97f8-eb28c30b6ad9 | -19.63483 | -56.84417 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 75bdcccf-d91a-30e2-a3ee-3e381415d93b | -19.63451 | -56.8233 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 090afdea-d364-3ea8-b4c4-2fefd637f652 | -19.63406 | -56.84817 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| 1c990e62-03b3-3dac-ab58-4593b1ad5212 | -19.63375 | -56.82729 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| fba2814a-bf71-3c28-8c13-9211dc8c9cda | -19.63298 | -56.83128 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| a30a468d-0fa3-3ff5-b4d8-510be459b6d8 | -19.62991 | -56.8473 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 15.6 |
| d50c9607-0624-3e1d-b953-0ebbd37ac19c | -19.62576 | -56.84643 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| b2a358de-a904-39da-a26c-e0652031cf93 | -19.62238 | -56.84155 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 4ac39fb1-8daf-3ee7-b2ea-39657f7ee799 | -19.62161 | -56.84556 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.2 |
| 0959b1b0-dd49-3fb2-9e7f-0b9dae531111 | -19.61823 | -56.84068 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| c8720f43-075b-383f-8d7c-5520cae30079 | -19.57774 | -57.00507 | 2024-10-24 04:38:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.8 |
| d883e88c-cf75-310e-a850-1daab62d28eb | -19.59322 | -56.53321 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b79ff20e-8a64-3254-8ca7-29edfa4b3534 | -19.58842 | -56.53621 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 9771b102-7849-3394-a9b2-eb589cfd556d | -19.58507 | -56.53152 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 217bc223-3779-3f17-b21e-0b004b0ed7f2 | -19.581 | -56.53067 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| ae403276-2140-39fa-9f86-4115c665e76b | -19.58027 | -56.53452 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 35e9cbfe-c782-3d86-8afe-8e464cd81977 | -19.57757 | -56.68348 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 58761950-5647-3692-938d-ce4cd9de6bff | -19.57619 | -56.53367 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 60d8b10c-3967-35de-a2a4-67a00e759efd | -19.5742 | -56.67869 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 9996cb11-e07b-3d07-ac4f-648d7aba5db8 | -19.57346 | -56.68262 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 1d502e12-6f68-3792-beb9-41fe81f07f64 | -19.57271 | -56.68654 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| 3083b8c5-7427-3555-a22a-6128024c1c73 | -19.57267 | -56.64171 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |
| b8c39789-7604-3fbb-8f4e-2f1fa5468e78 | -19.57197 | -56.69048 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| f5928c7e-cb59-333a-990e-992f96d9be42 | -19.57039 | -56.60883 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 21.6 |
| d016bcdd-cd79-306b-8287-e8913e0f6e23 | -19.57005 | -56.63305 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| b162c316-1d09-3f68-ab7f-e400c02f9a22 | -19.56965 | -56.61272 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 10.1 |
| 3a6dad1a-2a02-3678-b3cc-b54df291a79d | -19.56934 | -56.68176 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 33.6 |
| 511e6da2-db20-3361-a17b-759a291c60e1 | -19.56925 | -56.59245 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 1e3eacd6-09ff-33c7-94dc-60071ba9442e | -19.5686 | -56.68568 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 19.9 |
| febb1f98-2e36-340c-8f49-da1095e6f9ac | -19.56856 | -56.64086 | 2024-10-24 04:38:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.4 |


[Clique aqui para ver as próximas entradas](README56.md)
