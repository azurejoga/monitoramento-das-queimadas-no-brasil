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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39434038-60dd-3d02-aebe-4535255d5875 | -2.8401 | -49.547501 | 2024-10-18 00:55:57 | METOP-C | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96396ae3-0dcb-3fab-8245-22b530cf832d | -9.4198 | -35.8074 | 2024-10-18 00:55:58 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| c8bdb7ff-8b40-3e0f-89c5-f42ad96e936e | -9.4203 | -35.7801 | 2024-10-18 00:55:58 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.5 |
| c1a2e3e3-f41b-38d9-b02f-b4a57c453169 | -3.2082 | -51.508099 | 2024-10-18 00:55:58 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 732ab96e-c1cf-3b2c-8c09-8e3e6d31aca7 | -3.2098 | -51.514999 | 2024-10-18 00:55:58 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc1f6b8b-7e85-3d67-b500-511e99d8a33c | -3.2113 | -51.521801 | 2024-10-18 00:55:58 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 514d375a-7342-3aff-8728-2a1dc7ff99c8 | -9.4965 | -35.8214 | 2024-10-18 00:55:59 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| d020fb78-b13f-3b4c-9e98-f1e1786aceef | -9.497 | -35.7942 | 2024-10-18 00:55:59 | GOES-16 | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| 2f1ff350-5008-3585-82f5-8ba90525c335 | -2.4602 | -48.3517 | 2024-10-18 00:55:59 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d9764805-1077-33e0-91c6-9cc9f8fd5889 | -2.462 | -48.3596 | 2024-10-18 00:55:59 | METOP-C | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3638431b-77c9-3ba0-af78-21b277ec4be5 | -2.6264 | -49.069302 | 2024-10-18 00:55:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aac95859-4660-3efe-bf1f-a2a76839ef4a | -2.6281 | -49.076698 | 2024-10-18 00:55:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28a4cae5-db20-3e69-911e-888200cfb829 | -2.6298 | -49.084099 | 2024-10-18 00:55:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 72cfc4f1-12d9-3156-9c27-86653c656186 | -2.6313 | -49.268799 | 2024-10-18 00:55:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b897677-8aca-31e5-9733-5699a8051cc9 | -2.633 | -49.2761 | 2024-10-18 00:55:59 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 630a395d-eb92-344c-b43e-49c34d638a59 | -3.1415 | -51.4869 | 2024-10-18 00:55:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 420276a0-8824-3078-9d7a-902665a71892 | -3.143 | -51.493801 | 2024-10-18 00:55:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9a826698-7d5d-3656-9746-9046c12632d8 | -3.1446 | -51.500599 | 2024-10-18 00:55:59 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f427c17d-bcfb-3ae1-b229-f4d103dc3d6c | -2.4478 | -48.609402 | 2024-10-18 00:56:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6517291c-945d-3897-8aff-ad5ecd9165c0 | -2.4495 | -48.6171 | 2024-10-18 00:56:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2acc9e2-b3c6-3e4a-9275-cf2e99a1aca4 | -2.5671 | -49.214199 | 2024-10-18 00:56:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2e6c2263-96c4-3606-9ab0-96cfae1451b4 | -2.5688 | -49.2215 | 2024-10-18 00:56:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3a37fdcb-2c09-3eea-8d34-0aedb7f9441f | -2.5705 | -49.228802 | 2024-10-18 00:56:00 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e44472f6-92db-3472-a7ef-b99c00fe96b4 | -2.422 | -48.6315 | 2024-10-18 00:56:00 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ba63317c-9488-31e2-bead-b3ce7256efc8 | -2.6078 | -49.4795 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0ce961b2-5b76-33f2-8782-15e20dc6997c | -2.6094 | -49.486698 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| add180f1-6a0f-35e7-bcb5-3cf2429f52d3 | -2.6111 | -49.493801 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a8325bf1-cfeb-3bd4-843d-e42ab2f9abe0 | -2.5979 | -49.481701 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97f68796-dc94-3b8c-b921-8b69e5295836 | -2.5996 | -49.488899 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9cb9e124-13c0-3da3-9e9a-5093f67267bd | -2.6012 | -49.495998 | 2024-10-18 00:56:01 | METOP-C | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4f9d287e-7bf4-39b3-af39-e3898a527386 | -2.4161 | -48.873402 | 2024-10-18 00:56:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 682fca66-0ade-374e-9954-86da1e27f427 | -2.4178 | -48.880901 | 2024-10-18 00:56:01 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9effc27-52aa-3df6-8258-d4360adedee4 | -2.9681 | -51.360401 | 2024-10-18 00:56:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7499bb72-b3a2-3269-bc89-32b4f3fe9222 | -2.9689 | -51.453602 | 2024-10-18 00:56:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 20454c3a-9f9d-395a-a9c2-194897810457 | -2.9704 | -51.4604 | 2024-10-18 00:56:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e548a35d-4644-377e-ac9e-83aabac6ac7f | -2.4814 | -49.379002 | 2024-10-18 00:56:02 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| aab3f38f-7c96-33dd-9a0a-072a9e4e4991 | -2.4831 | -49.386299 | 2024-10-18 00:56:02 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b2572b7f-e0f0-3d7b-ba9f-e32ce4e95b4c | -2.9606 | -51.462601 | 2024-10-18 00:56:02 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7633f15c-56dd-3db4-a7bf-b33aff7bbeef | -3.3611 | -53.219002 | 2024-10-18 00:56:02 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5ea493e-c757-35b8-b3ff-0a1364c76d26 | -2.528 | -49.715 | 2024-10-18 00:56:03 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05741273-ce2c-3a63-9a60-a9bd57f37b9d | -2.9828 | -51.920101 | 2024-10-18 00:56:04 | METOP-C | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e62a5e3a-adff-319c-b745-f50f04d8db6a | -2.1645 | -48.410301 | 2024-10-18 00:56:04 | METOP-C | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0be9f00-50e7-300a-9657-a38b065ddbcd | -3.5897 | -54.6847 | 2024-10-18 00:56:04 | METOP-C | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 355468d0-adff-3523-8f1d-26609d979960 | -2.8199 | -51.343201 | 2024-10-18 00:56:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 581079d5-fdb7-3b24-b108-230f769b959d | -2.8215 | -51.350101 | 2024-10-18 00:56:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4da9ff37-e5a1-3233-bb6f-6d419cfd63d7 | -2.8951 | -51.6716 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bf987c2d-cf8c-37c9-8d3a-adcd95cc5992 | -2.8966 | -51.678501 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3b4edb51-a101-35ed-930e-9a23b9cbaad5 | -2.8982 | -51.685398 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bb77c249-093d-358a-99d0-6dbd7ab5ff00 | -2.8101 | -51.345402 | 2024-10-18 00:56:04 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad1a0f22-5149-38b0-818e-83046ea6e66f | -2.8712 | -51.612 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 13bc2e9b-5f54-3b09-bbf9-5c585978770d | -2.8727 | -51.6189 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f85b09d2-a732-347f-97eb-38d310b9650d | -2.879 | -51.646301 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 072dbd7c-1b43-3146-97d8-0f0be9ea7809 | -2.8806 | -51.653198 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48562806-96a8-3f42-9b15-2d2f7633ae0a | -2.8853 | -51.673801 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f711534-d402-34ab-982a-a34d0230977c | -2.8868 | -51.680599 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 84b49ceb-d6b6-316c-a3e8-7815b81d78fc | -2.8884 | -51.6875 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4e3895cd-001f-3ab3-b148-b891abf2991b | -2.8755 | -51.675999 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4ff34802-9021-3688-aeb9-c99130457255 | -2.877 | -51.6828 | 2024-10-18 00:56:04 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a2a7d730-15ec-34a8-bfb1-dd1d237ce753 | -2.1859 | -48.725201 | 2024-10-18 00:56:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 82218606-caa0-30ee-8663-282e09866bfd | -2.1876 | -48.732899 | 2024-10-18 00:56:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2ff6272f-7ff7-3e94-a6e5-657a5c9fccea | -2.8625 | -51.664398 | 2024-10-18 00:56:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 11495219-84ac-301e-b249-630c79b50233 | -2.864 | -51.671299 | 2024-10-18 00:56:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 89594989-9fa2-389c-83d0-03e68b5128ba | -2.8656 | -51.678101 | 2024-10-18 00:56:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 66a64c30-1ffb-3b9a-97bc-05916c89c984 | -2.8672 | -51.685001 | 2024-10-18 00:56:05 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b0b36168-8c5a-3367-a75b-94c47f65f5ea | -2.1761 | -48.727402 | 2024-10-18 00:56:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bed8bb33-ebef-332f-a406-b07ccbf7df4b | -2.1779 | -48.7351 | 2024-10-18 00:56:05 | METOP-C | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f9a83eb-3d59-3bbe-9df3-b45342e89326 | -2.3874 | -49.641998 | 2024-10-18 00:56:05 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a5dee8d7-d69f-324f-ab04-409ec5b4abee | -2.389 | -49.649101 | 2024-10-18 00:56:05 | METOP-C | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9b9b8648-2210-3c82-bb38-c8ec3e51e1b9 | -2.7058 | -51.340099 | 2024-10-18 00:56:06 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 88c08ecb-0a57-3a8b-82f5-00e4c19a9cf1 | -2.7073 | -51.346901 | 2024-10-18 00:56:06 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e9e668a-a1b5-30a3-b4b8-ef7d596d827e | -1.8673 | -47.839901 | 2024-10-18 00:56:06 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 287af200-b61f-3b1a-b34c-02cc65fe91c7 | -1.8791 | -47.890598 | 2024-10-18 00:56:06 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4b177203-d353-3be9-85dc-bf7b35714f5a | -1.8575 | -47.842098 | 2024-10-18 00:56:07 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8489205-9520-3bbf-9cdd-92cd79190adf | -1.8595 | -47.850601 | 2024-10-18 00:56:07 | METOP-C | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1aec994-9c3a-33dd-a151-f51204140329 | -3.0567 | -53.2388 | 2024-10-18 00:56:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7897b228-42d8-3462-8391-21388f5daf3c | -3.0584 | -53.2463 | 2024-10-18 00:56:07 | METOP-C | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 122c2c31-4baa-31a0-88b1-433fdbf67a1b | -1.6184 | -47.078999 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85e77fff-101e-3bc0-9d03-cf5e7d29758e | -1.6206 | -47.088402 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 846f9ec6-d80f-3193-b834-4cff528bdd98 | -1.6228 | -47.097801 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 030b3805-6a1b-3489-a1b9-aa680eec4bc5 | -1.6086 | -47.0812 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 08c9b107-4d01-3e03-9641-a5059f0bade7 | -1.6108 | -47.090599 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 21fe75d7-803a-3706-bb0a-ab12e61b2d48 | -1.613 | -47.099998 | 2024-10-18 00:56:08 | METOP-C | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 43ecbf34-d523-37ab-834e-ce4b1911aea9 | -2.5485 | -51.239101 | 2024-10-18 00:56:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9409eee1-04cd-31af-8879-66b1dd31090a | -2.5501 | -51.245899 | 2024-10-18 00:56:08 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 826bad7a-a53c-3a7a-af7a-c1f884bd6315 | -3.1428 | -53.9813 | 2024-10-18 00:56:09 | METOP-C | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3964426b-2735-3b68-8550-324019169a55 | -1.5344 | -47.293598 | 2024-10-18 00:56:10 | METOP-C | BONITO | PARÁ | Brasil | 1501600 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6239c4fa-7212-323d-9668-0ee5f7b03b45 | -11.4859 | -65.1198 | 2024-10-18 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 59.9 |
| eb72db47-e8f6-367c-ba5d-7594d7062c49 | -11.5046 | -65.1189 | 2024-10-18 00:56:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 42331b6a-bd3d-3c92-ba19-73c473d6877a | -2.1463 | -50.835098 | 2024-10-18 00:56:13 | METOP-C | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 788b5891-4310-3cb9-9d0d-5e17091f973b | -2.3642 | -52.145302 | 2024-10-18 00:56:14 | METOP-C | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f4d4cce3-6f5c-3fcc-9d5f-b503885145f5 | -12.5048 | -55.1846 | 2024-10-18 00:56:17 | GOES-16 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 75.5 |
| bda9b890-15c3-3a27-8064-a12cea56dc87 | -12.4775 | -63.2268 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 50.1 |
| 56b1258f-adab-35a5-84a6-ea7c28f0a7e7 | -12.4964 | -63.2258 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| e0821150-8e2b-337c-959a-57e2b7065e13 | -12.4966 | -63.2066 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 94.5 |
| fd11ca66-ad14-34dc-978f-64d519be8ae0 | -12.4967 | -63.1874 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 112a880e-c158-382f-82dc-5925cafcf519 | -12.5155 | -63.2055 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 70.6 |
| eca5f882-d21b-3697-9bb3-26181ca10bf2 | -12.5156 | -63.1864 | 2024-10-18 00:56:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 0fbaa545-f1ea-3117-96af-a499575a82c1 | -2.7075 | -54.648102 | 2024-10-18 00:56:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 351f70d4-b734-3f9e-b200-4b8e22c7f397 | -2.7095 | -54.656799 | 2024-10-18 00:56:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 78e79c13-a93f-3e63-bda0-41b1c1cd169f | -2.7114 | -54.665501 | 2024-10-18 00:56:18 | METOP-C | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README12.md)
