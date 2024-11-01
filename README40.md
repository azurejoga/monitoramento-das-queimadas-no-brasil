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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a38c26f9-db4f-30f6-a1f3-b4509c6a5c72 | -1.86193 | -52.31988 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd357b23-1474-3c30-9335-82d1a7c8ec9c | -1.86133 | -52.32364 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 052d5e1c-7f8a-30c6-b3dd-133f132ff3c7 | -1.85719 | -52.32297 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9899e0e7-9ed1-3f8a-9892-424bebd66c39 | -1.85644 | -52.03977 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0ed25034-7783-3ca6-9f76-3b2b602777b1 | -1.85069 | -52.31038 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48dc45d5-1be6-3088-a899-e9bb786f29ba | -1.85009 | -52.31413 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2bd41a32-3827-3554-918a-7a444236a460 | -1.84655 | -52.30971 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f0969104-3c25-3674-b230-4755d6a3cc50 | -1.83941 | -52.11868 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f269c90b-2b11-39d4-979f-00d3386b0b50 | -1.823 | -52.27139 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e281d28b-1bc2-3fe9-8d2e-028363ff72ee | -1.80375 | -52.03154 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1a44f1a6-2381-3186-a5cd-e313a32c62e1 | -2.87963 | -52.8908 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 59fd4dca-b512-3ab8-bb4d-232ab786c2b5 | -2.87901 | -52.89467 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0d9fbeab-6302-3d53-af49-5fccc9682318 | -2.87839 | -52.89858 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 52ee4bbe-865f-395c-a049-9e62855a3255 | -2.87539 | -52.89012 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 005e342b-4be1-3d9b-9283-b59ee9e39bba | -2.87476 | -52.89403 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40436636-69ba-35c7-9ea2-3fd276b6f7d9 | -2.87414 | -52.89796 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 67868ddf-4549-3e00-9d11-26a6c559d8e1 | -2.87115 | -52.8894 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 047bc810-499c-3d08-a740-6c44bd8fbc8f | -2.87052 | -52.89336 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 79364b3b-80f6-316c-a177-3d3e9b5c09d7 | -2.86988 | -52.89733 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55ea3f4e-bf72-39aa-92f1-9d93faf720b2 | -2.86878 | -53.32854 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 398ad30e-f59d-3a00-af97-946dde02f99b | -2.86444 | -53.32764 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5f0534fc-8fdb-34be-988a-8f34bef6294d | -2.85224 | -53.34727 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5e529f92-484d-3098-b667-c3266c888b14 | -2.84786 | -53.34657 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 34ef7017-33ea-3c7b-bf8c-22c1a648eb9e | -2.84712 | -53.3511 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5cec70f6-4e1b-3416-9e98-1d2d87740384 | -2.84419 | -53.34155 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83f4a3d8-1e49-372a-8ac7-2932eee387d7 | -2.81627 | -52.06507 | 2024-11-01 04:29:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8cb64f66-c03e-3e37-b55a-f79f2b9f1fe0 | -2.81506 | -52.06441 | 2024-11-01 04:29:00 | NOAA-20 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f572225a-f644-38e6-9a11-29e9453f4f5a | -3.06023 | -53.2548 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebdfb176-d3d7-3331-9279-66e28c211668 | -3.05771 | -53.2525 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ab83b299-dbf0-3d96-be85-2f6ab4df2d83 | -3.00814 | -53.44141 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 996c43e5-3b65-3b27-b430-2c5e8fa903fa | -3.00744 | -53.44578 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0ab43b63-0ef0-3e0e-b049-713ca3488290 | -3.00675 | -53.4501 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b64b4a2c-cf17-34ae-bd14-83382e1a8a8b | -2.99293 | -52.36041 | 2024-11-01 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c754e804-3ead-3314-b303-a8af9fb1d480 | -2.99113 | -52.37134 | 2024-11-01 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff8fe15d-f64a-3bc6-b0f0-4ed085018c63 | -2.97379 | -53.34785 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c4763a9d-454c-3f9d-ae9c-49ffbb5642d6 | -2.90922 | -52.59801 | 2024-11-01 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5af3295a-d1de-34cb-9b76-d0fb50f45f91 | -2.90862 | -52.60175 | 2024-11-01 04:29:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3e26ed5d-d6d5-360d-8246-8c1f11285772 | -2.36534 | -52.01088 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6b207f1-b7a0-3778-b995-c847065547a2 | -2.23658 | -52.76845 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 73cdd3e2-9b60-3ccb-972a-b3cd510d29de | -2.30201 | -52.04417 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a7bdd82a-0c4b-31e3-9926-4cd3e89989cc | -2.67612 | -53.01961 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf3ecadf-25e2-386c-955b-7fcd18b1d728 | -2.6202 | -52.45348 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1661965f-dd00-3663-b200-b3a4d93c4876 | -2.61666 | -52.44911 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8bf3eff5-e764-3e84-937f-34c0e353f15f | -2.61606 | -52.45284 | 2024-11-01 04:29:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7642660e-7ae6-36e6-9467-be54af1bd09e | -3.25266 | -53.07427 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9076f402-467d-315a-851f-4d71354ae344 | -3.24998 | -53.33803 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ed56e9d-4ec8-3a95-bb5a-ff2007bf3b6b | -3.24838 | -53.07363 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c5e89a3f-07bb-3f87-8f96-f03c27ecac2d | -3.24564 | -53.3373 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99a9c634-f738-3870-8092-a4c23d53fa8d | -3.2377 | -53.2758 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd304d74-b72c-3d0a-8cac-c1ee622c7966 | -3.23655 | -53.36615 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 26a7e105-672b-3859-9c13-40b31a052d45 | -3.23588 | -53.37038 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 79070893-a39d-35ab-88f9-48118e1f76f6 | -3.23518 | -53.37471 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.9 |
| 3d6cff79-12d1-343d-a2fe-08538019219c | -3.23337 | -53.2751 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 00b334fd-4cd0-3bd4-9bc9-cf72313a885c | -3.2322 | -53.36539 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30bda475-0647-31e6-b8f6-a58e8416fcb8 | -3.23152 | -53.36964 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 54f164f8-54ab-3090-9fb8-db071977f2b0 | -3.22289 | -52.20643 | 2024-11-01 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc735578-5b78-3bd3-923b-cd2e297ca7f1 | -3.2223 | -52.20995 | 2024-11-01 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 663a38fc-049e-3da8-bd33-5ba872d72046 | -3.22186 | -52.20679 | 2024-11-01 04:29:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 443221d8-719f-372f-bb52-3a9e42c64bcf | -3.21232 | -53.40541 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 926ed71b-596b-3058-bd0e-7c57a6f3662d | -3.20863 | -53.40052 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec09d516-0a83-396e-9594-585a490f39c0 | -3.20795 | -53.40469 | 2024-11-01 04:29:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2974a28a-67fa-3207-8132-a7376ed031f4 | -2.18355 | -53.72177 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 8717ec49-f87f-3876-adf2-d1b2a2aa0ddc | -2.15773 | -53.6799 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 14c399b3-11db-3c3a-b09c-647953b50e5e | -1.17024 | -53.68169 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 42b9928b-7f56-3470-9cd4-ef227dec0657 | -1.16954 | -53.68606 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2b421a73-e280-3dfa-8adb-2851836079aa | -1.16571 | -53.68057 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5b831459-8c59-32b9-abda-1d0794b843a1 | -1.14882 | -53.63954 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1ad6c46-2da0-3bbd-8397-225582b2ced2 | -1.13114 | -54.10373 | 2024-11-01 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 375cc2e3-c08d-328b-9c84-0d2ad7151e3d | -1.09058 | -53.65239 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 83a2d0a6-a908-3c4a-ae62-2f29cd2bc80b | -1.08527 | -53.65609 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2bb7d63-cef6-301a-a16b-65a633b2c366 | -1.08143 | -53.65068 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bc412364-ee4e-32fe-96c9-136d7cbd3cc3 | -1.0807 | -53.65517 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3fb7a01d-5a4c-39cf-935d-d16ea38d57e7 | -1.0661 | -53.65792 | 2024-11-01 04:29:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f71ffb9e-1082-34f5-a10a-340209876b14 | -1.42751 | -54.4925 | 2024-11-01 04:29:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8455075-54fa-3397-9cf6-748cbace84c7 | -2.16302 | -53.67594 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| af09e928-c2a7-3f53-b1ae-c94e0519cbe4 | -2.16227 | -53.68059 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| d73b150b-c7e2-3884-8a60-65cfcafd3860 | -2.15848 | -53.67529 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7ba325e6-10d9-3419-85ee-a7bce781003e | -2.8339 | -54.5624 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 4ed88345-f0fb-3b57-84ae-0f8bd53c9c31 | -2.83358 | -54.56121 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a6197de8-2dd0-3a85-a02c-b120ac7869d0 | -2.83275 | -54.56639 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 2ca8401e-8b80-3ea8-971d-cdbc30567455 | -2.80082 | -54.00325 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4dadeb9d-01aa-3167-9f78-a8a5bf6e2a87 | -2.47533 | -53.98168 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b7436600-8e85-3b99-a5fe-6e95e4b1eb29 | -2.47454 | -53.98655 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 072fe027-02e4-3ba5-bed1-b86bbabc3e1b | -2.47377 | -53.99141 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f651c060-f602-3277-82de-033058f85a38 | -2.46995 | -53.98574 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 44d553c4-7a7e-3e51-9872-f8c50c8a3b77 | -2.46917 | -53.99063 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc07a2f0-b763-3c9c-ab1c-458927d887e7 | -2.65635 | -54.62581 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2c8bb882-f67a-3cec-96b8-002e3c67b004 | -2.56045 | -54.00725 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c717acd1-2e57-3c20-92b0-827c40cc112a | -2.55585 | -54.00649 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 91a3f7ea-2af0-39a7-b77d-394a6947beab | -2.55508 | -54.01126 | 2024-11-01 04:29:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| efc96791-d554-3c71-9c29-50008b6ef923 | -3.48823 | -54.02724 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 28504605-79d9-3595-b64c-564507c44c81 | -3.48747 | -54.03178 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1685813e-aa56-37d8-866d-b1dc9af2cfcb | -3.48369 | -54.02647 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfd6196d-a244-3bea-857a-c7dbecacb28b | -3.40482 | -53.80852 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7640f10a-2a4c-397e-bc9e-a19d8997eb34 | -3.40304 | -53.80671 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d63681ae-e4b6-3c15-8c8b-575e82f36d5f | -3.40033 | -53.80785 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e533cb30-72a6-3994-8857-12e3c0e433b2 | -3.20664 | -53.85225 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aede5f1a-4db2-3f15-a561-ca0d77e206c0 | -3.20287 | -53.84705 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ec66512-a72d-38e2-834b-b494dfb992b9 | -3.20212 | -53.85157 | 2024-11-01 04:29:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2b2e207d-e501-3d1a-9f13-b707b16a861c | -3.11825 | -54.30009 | 2024-11-01 04:29:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README41.md)
