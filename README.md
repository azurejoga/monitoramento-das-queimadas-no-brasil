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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c6d29053-bdee-3749-ad68-2480f580004f | -18.6573 | -41.6456 | 2026-10-02 00:00:00 | GOES-19 | GOVERNADOR VALADARES | MINAS GERAIS | Brasil | 3127701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 129.0 |
| 4c4afe95-1f67-3f30-a527-7c31b31f1d53 | -12.8435 | -51.4869 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 0763db90-082a-3ae6-94d6-1b2ac6305914 | -7.8308 | -55.1262 | 2026-10-02 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 350ddcfa-672d-35df-85ad-632a7343b106 | -5.8966 | -53.4975 | 2026-10-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 313a9593-a9d4-3969-ba88-00dd6cef8050 | -7.0478 | -55.6302 | 2026-10-02 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 117.6 |
| fbc68cb0-2b6a-3080-9694-d1ef537fb26b | -11.4691 | -43.4299 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 125.0 |
| d4f584a4-64ff-3d9a-9fa0-8ae242d2f1b5 | 1.8037 | -55.6051 | 2026-10-02 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 97.4 |
| a8398d2c-15d5-3ebd-9e1a-5dbad044b934 | -3.0192 | -53.887 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 4c27e179-e9eb-3177-81fd-2e0c06a0e874 | -11.1615 | -44.6002 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 326.9 |
| 4348d605-1944-35a4-80c7-b36b4a141ea8 | -11.6981 | -43.4891 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 76.3 |
| f7a2cc13-429d-3877-b067-85b0d7ce7316 | -11.4695 | -43.4062 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 67.7 |
| b0a1f6f8-b4ff-3869-bc1e-b135f8510530 | -7.0477 | -55.6501 | 2026-10-02 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 8836ef6a-dc40-3086-9a3f-a75462e70dd7 | -12.8069 | -51.385 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 97.1 |
| bc36ecfe-60c9-3d4d-b06b-271f210d7d7d | -3.2767 | -53.84 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| ca8c2eef-c6d1-333a-804f-77082f4c4713 | -9.5146 | -45.3427 | 2026-10-02 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 180.6 |
| a9703f6b-f480-3fd4-9baa-29e7104a2e4f | -11.7567 | -43.4325 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 101.0 |
| be233105-b0b8-32d2-9760-2d64cb1a10ae | -4.286 | -50.7707 | 2026-10-02 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 74.0 |
| 14d51ad6-0601-3363-89eb-42153daf728b | -6.914 | -43.6816 | 2026-10-02 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.3 |
| db44a4d5-1ad2-3cb0-95bd-a39c21be045e | -12.7877 | -51.3873 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.5 |
| ccd02198-24fb-3111-8ab2-40ce2b879b21 | -9.5149 | -45.3199 | 2026-10-02 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 70f1e460-60fd-32d2-b9ec-7473018c1e7c | -12.5329 | -43.091 | 2026-10-02 00:00:00 | GOES-19 | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | 132.3 |
| d269de8a-c734-358a-8c1d-7e67c5d4a036 | -12.8052 | -51.4915 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 55.9 |
| 421c37b6-cf34-32dc-ba83-5cadb7a7983e | -14.8908 | -47.1087 | 2026-10-02 00:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 7c594490-d20e-3c2a-bbff-abbcef616cec | -4.2676 | -50.7506 | 2026-10-02 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 112.2 |
| d5071f40-02c8-3943-ac3f-b258a86811e8 | -12.8244 | -51.4892 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 126.1 |
| 2b5c3b42-c503-3140-9d6c-ec148db03033 | -4.2953 | -49.1021 | 2026-10-02 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 152.5 |
| 41a10867-b619-3b19-8faf-f1c0be2fba92 | -12.8439 | -51.4656 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 71.3 |
| d8559929-f905-3645-8b93-92caa19957e3 | -9.844 | -44.8449 | 2026-10-02 00:00:00 | GOES-19 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 71.6 |
| b79ad302-8f47-3796-8df4-5d2473f9cb00 | -12.2126 | -47.9669 | 2026-10-02 00:00:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 9ed205e1-46d5-3384-aff1-e4200b351f8c | -2.8897 | -54.1313 | 2026-10-02 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 60.2 |
| eae844b9-730e-342f-bbcc-9dd1c59828cd | -4.2859 | -50.7916 | 2026-10-02 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 33cd952a-011b-370b-8181-55b107ffaf2d | -11.1427 | -44.5796 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 91.2 |
| d1ebae71-027e-3868-8add-19a1d19da5ea | 1.8037 | -55.5854 | 2026-10-02 00:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| 5ea69e89-5dc6-350e-8c56-3fa61ba47412 | -11.142 | -44.6261 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| c27dfe36-54c5-3f10-8218-23f990f0f90a | -3.0189 | -53.9675 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 82.5 |
| d899bcb9-5ca8-3e94-8f4a-a2db311c4570 | -2.8897 | -54.1514 | 2026-10-02 00:00:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| f4d669ca-719a-3141-a758-ed612e8076f9 | -12.8072 | -51.3637 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 88.1 |
| 5a5f0ae3-6e71-3880-830e-97b0be248c53 | -9.4959 | -45.3221 | 2026-10-02 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 83.0 |
| b6abd8be-9f09-3e7a-8de6-7bc1ec15e470 | -11.7169 | -43.5098 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 91.5 |
| feb621e0-a76c-32f6-b459-17bd69e8185e | -6.8952 | -43.6833 | 2026-10-02 00:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 3d0d7584-00b7-32e5-b3a8-51a71dcba77a | -3.1655 | -54.0844 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 20cbca32-f372-37d3-8011-75987584f5be | -9.5335 | -45.3405 | 2026-10-02 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 137.2 |
| eb734cd0-2930-383c-a4ab-6e40e515cb86 | -7.2013 | -52.6066 | 2026-10-02 00:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| b6dbaf73-c6a8-3302-bb59-6b5cc4e9a02d | -6.9317 | -59.2798 | 2026-10-02 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.3 |
| 403cb4d2-74bc-3829-befe-7270dfeb296d | -11.1232 | -44.6056 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1f398682-a818-32d5-9e93-7494021f1f73 | -3.1838 | -54.104 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.9 |
| e34d5c67-8fa2-3da4-ac8e-ffd45a1622c9 | -12.1861 | -48.4124 | 2026-10-02 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 64.9 |
| 7750046f-b580-304c-884a-c461c2a18b77 | -11.1611 | -44.6234 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 106.0 |
| cb0662de-1692-328f-a734-33e0070d7b09 | -14.8903 | -47.1315 | 2026-10-02 00:00:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 189.8 |
| da8dbe1a-148c-3875-9f27-bcc24ef6a2b5 | -3.0188 | -53.9876 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.2 |
| b367118a-dad8-3d0d-b7d6-c117b1aab25e | -11.7182 | -43.4386 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| 3e5669b5-7853-3a77-a379-e6ff860a7466 | -11.737 | -43.4593 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 260f7085-9580-38d9-a6d1-edc6e2211e2d | -11.6977 | -43.5128 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 67ac1701-dc87-3211-ba8b-dbaf1748dbd4 | -3.1839 | -54.0839 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.4 |
| 987c5372-327a-3bf5-9391-db802569402a | -7.2889 | -55.5973 | 2026-10-02 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 84.1 |
| f3a043c1-715a-36d6-9a57-d339e7b7cea7 | -4.2677 | -50.7297 | 2026-10-02 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| b50ad793-2f5f-363a-848b-daa8d6daedd4 | -2.0577 | -56.8591 | 2026-10-02 00:00:00 | GOES-19 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 69.7 |
| fee4b824-c878-3661-88f8-294861b58179 | -12.8056 | -51.4702 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| a3f47f47-4e6d-38c0-b02b-e2c8dc23592f | -11.7563 | -43.4563 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 82.0 |
| d6fa7925-1a08-3efe-8a6e-c6f4ce9ba5c0 | -7.4188 | -55.5902 | 2026-10-02 00:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| adba87f3-8744-3699-8495-ec5ef5641219 | -6.3952 | -56.4158 | 2026-10-02 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 96.9 |
| f369ad8a-180a-35e2-8f40-c2cf1dcd7675 | -12.8247 | -51.4679 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 154.4 |
| e7ca99e6-58b5-392e-8031-c35ded9e1c9b | -6.9132 | -59.2806 | 2026-10-02 00:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.4 |
| 5eed7387-861e-3f65-a759-cf7ed97eaf28 | -9.5338 | -45.3176 | 2026-10-02 00:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 93d00c11-fd2f-3fc7-be46-8543fd1aca28 | -11.7375 | -43.4356 | 2026-10-02 00:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 181.9 |
| 8abf04f3-e5b7-3358-a204-36aee56160cd | -4.2954 | -49.0807 | 2026-10-02 00:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 105.9 |
| 3e3c8230-5ca6-30ff-90d3-2a78d1374f8f | -12.1857 | -48.4345 | 2026-10-02 00:00:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 1109a4f8-fe86-3d44-86d2-ea1e6c3390d9 | -6.4137 | -56.415 | 2026-10-02 00:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 81.9 |
| dd476ac2-9d55-3194-8ce1-24853d026f1c | -8.0745 | -54.8902 | 2026-10-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 72b69414-8fa9-336a-8de9-44e1108767b5 | -8.543 | -54.557 | 2026-10-02 00:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| 76f6ff21-c041-3a7f-bad1-803ea4333049 | -3.0008 | -53.8874 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| f5233ca2-e1e4-35ed-a231-c73517edb68a | -5.7563 | -45.152 | 2026-10-02 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 88.6 |
| 8082510b-b91b-3cef-95c6-0f4d87c5c8a7 | -12.7881 | -51.366 | 2026-10-02 00:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 4f2626db-2668-36fd-9ee3-0a7e51f01804 | -3.295 | -53.8597 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 4aa25c47-0a6d-3792-a207-47592d36b250 | -4.2491 | -50.7514 | 2026-10-02 00:00:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 66.5 |
| 7d75569c-a6bb-3532-a575-b8751544e4b0 | -11.1424 | -44.6029 | 2026-10-02 00:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 480.6 |
| f4197158-6a25-3d5e-bec7-b881032a5c35 | -5.5499 | -45.257 | 2026-10-02 00:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 99a39356-c262-396e-8a3d-25c22836bc10 | -3.2951 | -53.8395 | 2026-10-02 00:00:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 61.5 |
| c797aa30-3c9a-33be-a0af-d809dcd04642 | -6.8672 | -57.7297 | 2026-10-02 00:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d75330d3-70ec-3e0f-a5e4-6165f4ba4c94 | -4.2676 | -50.7506 | 2026-10-02 00:10:00 | GOES-19 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 116.3 |
| e85a1225-98a6-3353-950f-622bc74f17ea | -6.8952 | -43.6833 | 2026-10-02 00:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.5 |
| 77d1741e-a94b-346d-898a-dcc7219d4259 | -14.8903 | -47.1315 | 2026-10-02 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 118.0 |
| 4e90bd9d-15dc-34d5-86f9-d162ddacb042 | -14.8908 | -47.1087 | 2026-10-02 00:10:00 | GOES-19 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 98.7 |
| 785dce41-3e10-3e03-9e24-1bf72a1551d8 | -9.5338 | -45.3176 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| 1461c39e-a4d8-3ec7-b814-a8e4fbb10724 | -6.7199 | -44.2771 | 2026-10-02 00:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 57.4 |
| b6306bce-1959-350f-a3bd-507e58149df1 | -7.8308 | -55.1262 | 2026-10-02 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| addd26c2-ab5d-35a8-bd92-4d059b8c0fc4 | -12.8052 | -51.4915 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 07884358-1f14-339b-bad0-095949b8f25b | -11.6767 | -43.6106 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 198.1 |
| e5a444cb-b2a7-39c5-b686-adb3e2170eae | -9.5146 | -45.3427 | 2026-10-02 00:10:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 211.1 |
| f75392ce-4c44-3808-829f-83c836059a54 | -2.8897 | -54.1514 | 2026-10-02 00:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| b5dc6930-4fc9-350a-a24a-9fb0bb641445 | -7.0477 | -55.6501 | 2026-10-02 00:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 1401f297-3194-3a12-b54b-882e8daa1bea | 1.8037 | -55.6051 | 2026-10-02 00:10:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 906a0d46-dc8c-3f9b-93dd-0390697420a9 | -12.1857 | -48.4345 | 2026-10-02 00:10:00 | GOES-19 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 74.8 |
| 7ca9fa32-0af2-367f-9d25-0fa9537e548c | -12.8056 | -51.4702 | 2026-10-02 00:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 91.6 |
| 52408c3f-9b9d-37a4-8322-0a3d7cc5de4e | -12.6838 | -49.5292 | 2026-10-02 00:10:00 | GOES-19 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 66.0 |
| f17781f4-7de1-3b2a-91c9-9f5356534840 | -11.7375 | -43.4356 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 143.5 |
| 294ba431-519a-3850-aadb-afd752034a25 | -11.4691 | -43.4299 | 2026-10-02 00:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 115.5 |
| b5c57a29-5741-3b7b-bffa-1f1207813fa6 | -3.1655 | -54.0844 | 2026-10-02 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 86.7 |
| 694ed41e-ccd8-3bd0-b330-6064315fc8c7 | -11.1427 | -44.5796 | 2026-10-02 00:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 3cfe974d-23ef-3bd0-b021-6debf2476f4f | -3.0189 | -53.9675 | 2026-10-02 00:10:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 87.3 |


[Clique aqui para ver as próximas entradas](README2.md)
