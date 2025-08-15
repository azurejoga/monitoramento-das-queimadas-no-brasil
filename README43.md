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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9b55b7fb-a68f-3cfd-ac26-4310916bd510 | -13.56809 | -46.95142 | 2025-08-15 04:51:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0aa35fba-c005-3d4e-951e-7d3be92d809b | -9.15546 | -59.66922 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 07d45ab1-48aa-30da-ad1f-0e24ff19cbaa | -6.88281 | -59.8867 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4a143b20-fea5-3a63-a14c-4a83f715f9e6 | -9.74733 | -48.57623 | 2025-08-15 04:51:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 50779fef-5d5a-33da-b3ed-88f72608cac5 | -11.34305 | -55.41335 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b02cbd27-738e-3f9c-bc25-76b396fa81ab | -10.47049 | -61.32137 | 2025-08-15 04:51:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c481b4b-7db7-3d50-8b27-1bcbf7054301 | -6.9079 | -59.63038 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 067c1674-106c-3247-9a6b-31fbb1bdeb4f | -9.1787 | -59.69095 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0b5360c5-d077-39e7-9800-f6a58b32df1d | -7.86855 | -61.80986 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 05eb60c7-65fc-3c98-ac46-21f8840be3e3 | -7.94376 | -46.85064 | 2025-08-15 04:51:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e1c13d6-886a-34cc-b403-857e39b519ff | -6.69884 | -58.84726 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0fbd0e71-c213-3c2e-a275-8a79eed8eb2d | -10.35991 | -50.80717 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19be58f3-966c-3cbf-a536-f433caa0a45b | -6.87257 | -59.15156 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4c1d66d-885f-3a0f-80ff-990d4cf05584 | -7.88118 | -61.82026 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd8bd2c1-d260-3dbc-abc5-6640ccece989 | -7.94837 | -61.75079 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eac36ebd-bd69-36e2-8610-e5cfad26147c | -7.52784 | -61.33881 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68c335e8-52ae-33f5-81fc-a3157fc9a9f3 | -9.19627 | -59.66769 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2a64dd6e-5cc5-32d6-879e-e542589fdde6 | -6.69595 | -58.83822 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8196477b-11a1-365c-b451-fdf58bbce3d9 | -7.8828 | -61.81097 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 27028c57-9f97-303c-89d3-bda475f3fb8b | -6.47876 | -62.94346 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 71605de3-5740-3d41-8377-43b6bd196c33 | -7.12463 | -59.63004 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f73b2c45-8ba0-39df-947c-4b25d42c88a4 | -9.85038 | -44.68689 | 2025-08-15 04:51:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 32c9eb3a-a744-3d6c-9ba1-e7d361591607 | -10.04784 | -59.36362 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5fdce547-f699-3a7f-86ab-12528617ab5e | -8.10138 | -61.18346 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4a6c7237-d361-341a-8bad-1f172ba68674 | -11.94378 | -58.76379 | 2025-08-15 04:51:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ce07c0b8-69e9-38cb-ae7a-c31a36081510 | -9.50663 | -60.53496 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9c3d6287-0b30-3795-ab7f-a2e8f3f41102 | -7.43725 | -60.02611 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44e7f88f-a2cf-3c10-a03b-f3c2e7364f83 | -8.18849 | -42.26175 | 2025-08-15 04:51:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4291c093-8b06-32cc-88da-2efdf460c8f0 | -7.08749 | -59.21541 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e1005d77-df74-32c5-b6a4-ca6d6aea94fb | -13.26223 | -57.253 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 939c7c0d-8cf4-321e-a2d3-e063dcb1a8c3 | -9.94008 | -60.48112 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| fef3f28b-092d-3fc2-aad1-00d03a5c4d1a | -9.50579 | -60.5398 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0b9d0d04-5498-3d5b-987a-52c2f24f50b2 | -7.4263 | -60.03425 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a35a65c9-f162-3c04-9c49-52270a7f9357 | -9.34668 | -62.58537 | 2025-08-15 04:51:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2d97ddc8-a4ab-33d6-8309-06cfdd411a0f | -13.11847 | -57.14059 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86ac4aff-e524-3060-839c-7e87807fac2c | -13.11718 | -57.17021 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d571d8a6-7341-3583-b050-2db127d5446b | -6.72453 | -58.82639 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f9619ef4-d5fb-3c66-ac4f-756fe62029b8 | -7.45164 | -60.41184 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2aa38b93-6cbb-33b5-b5c3-e225e4052b96 | -13.47364 | -56.66774 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 61ce9b3d-1a0a-3d8f-8635-cf80435c8d80 | -12.49787 | -47.0214 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2f00f49-b961-3ccf-a587-90c9ae6afbdb | -6.67103 | -59.08869 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3c4854d4-3814-3d39-a818-107e4e0ee3fe | -13.88431 | -45.55883 | 2025-08-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a10e78ae-efb2-3db5-81e5-eecd3ac91c7b | -6.07397 | -59.9622 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0dd44f83-9b4b-3ea9-bdb7-c435e0f49aad | -7.92786 | -61.74691 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a60e9a5a-202a-3401-be4c-19a40212ae55 | -11.35599 | -55.41927 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| af1c700e-013d-39ae-b983-7a6db3a43d16 | -7.59619 | -63.50251 | 2025-08-15 04:51:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 33d4741d-ee3b-385b-bbc8-5f23f713012e | -12.42682 | -48.70079 | 2025-08-15 04:51:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1a664a30-9595-3f81-b1fc-1f2149060fe3 | -8.51236 | -43.32437 | 2025-08-15 04:51:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d72b4c19-30bb-3e03-8bd4-9f0f8525816f | -13.47775 | -56.66447 | 2025-08-15 04:51:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| be2b6083-2770-37f7-a87e-c7329bef2778 | -7.53288 | -61.33969 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1c718eee-9dcb-3a94-a20d-f65129f325f8 | -6.96403 | -60.12958 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b5be4de4-ee47-36b0-867d-72a45b9820ed | -6.0795 | -59.95816 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be198d1a-2472-3423-9655-a8a066b8ae19 | -7.05968 | -59.21941 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22a558d8-a315-3b93-8eaa-8c0ec6891929 | -10.35222 | -50.81018 | 2025-08-15 04:51:00 | NOAA-20 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dae8f22a-861a-3f69-99ad-7bfcd1399a72 | -9.20646 | -59.66084 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5e629f30-51aa-3a0d-8253-4f55ef979347 | -12.59338 | -46.9686 | 2025-08-15 04:51:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0692c47e-30f6-356a-983a-721e4afe396a | -6.91926 | -59.14217 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7838dcd0-ac01-3d83-bcb6-eabd5d148575 | -7.43812 | -60.02122 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3eb4c4f-4f29-3e48-b6f5-3460df24519f | -7.52724 | -61.33758 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc511163-b35d-3d72-b7e9-419719378b52 | -9.63116 | -63.09348 | 2025-08-15 04:51:00 | NOAA-20 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4ee004a-b705-3653-b3de-df81f46e8dcb | -13.13931 | -55.69557 | 2025-08-15 04:51:00 | NOAA-20 | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| dc6c6874-f5d5-3676-9c59-8bcc264fa9bd | -9.60481 | -55.14463 | 2025-08-15 04:51:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| dd28bcc7-356f-39aa-8ee5-f732ecf7988d | -13.8847 | -45.55556 | 2025-08-15 04:51:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 30feba9c-385e-3313-a0dd-8d80577c39ab | -11.34584 | -55.41758 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8a12d0ee-3ced-3a0b-b033-4166acf0cdfd | -9.5041 | -60.54945 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 53f7c3b2-db74-3e96-b83a-e2c177271a69 | -14.06835 | -46.31215 | 2025-08-15 04:51:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 191e2859-e892-32a3-adf0-c4cf70d3a640 | -6.63893 | -58.82185 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 976dadea-8478-334d-9dd2-40c639762b3c | -8.56091 | -63.91537 | 2025-08-15 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3586fcca-0c9c-3c80-b34e-da0f23408b5a | -9.2036 | -59.65142 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48116cf8-e73e-3daa-a744-14572e813e44 | -8.46542 | -60.58316 | 2025-08-15 04:51:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 041ab189-a868-37ae-bc26-dcef0ef1f88e | -6.48588 | -62.93663 | 2025-08-15 04:51:00 | NOAA-20 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| cbe5bd55-872e-3c3a-9f26-a04aaa8c4501 | -8.10733 | -61.20078 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c9a071-0ee5-39dd-9aa6-47b02120ae5d | -8.10337 | -61.19426 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 46f9605a-4026-3e5d-9d2d-5c24da030a90 | -13.31671 | -45.22437 | 2025-08-15 04:51:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| c706d4a1-b18e-3776-b1f5-022575ae8496 | -9.50727 | -60.52595 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c371da60-3783-30d5-a215-3522f857e9fd | -10.04855 | -59.35916 | 2025-08-15 04:51:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a4e427c3-2396-3411-a3d2-e40b8cb83d3d | -5.80872 | -59.22537 | 2025-08-15 04:51:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 59c62212-7e72-360e-a791-61c4e8b52bda | -13.12557 | -57.14185 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a1008b2-db89-34b6-a13c-59cf905835ea | -7.31595 | -60.62375 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 42f2b22f-27b6-396a-a942-3a8ad7851854 | -9.18457 | -59.68316 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0070897-3fd8-39f9-8ded-71da8020c745 | -7.31214 | -60.62285 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4079ada7-9c78-3f15-a77d-c9752ecfd221 | -9.18033 | -45.32218 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d76b1f27-64dd-34db-9ac3-767c81dfe80f | -9.17082 | -59.65875 | 2025-08-15 04:51:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 13.5 |
| e6d5c481-360b-37e4-aee0-c499d4531ee1 | -6.69236 | -58.83335 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8e990470-1ef8-374b-b6ae-0446e0793cd7 | -7.30065 | -60.63196 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 95f3828a-481f-3e47-b890-8bb53891cc60 | -11.94664 | -62.83495 | 2025-08-15 04:51:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8285e720-f443-3ffc-b2fe-454aa2ad85b5 | -11.36145 | -55.43531 | 2025-08-15 04:51:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b173edd1-2ca5-3527-a6c3-87eb752d67f8 | -7.94727 | -61.75696 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e48000ac-16c0-3c9e-862a-0b83dd49f740 | -6.53778 | -56.19574 | 2025-08-15 04:51:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7a839ac7-483a-3156-8459-b97204d035b8 | -6.65253 | -58.81992 | 2025-08-15 04:51:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c56bd7c-8582-3e79-a0a6-2b8b1f95979e | -7.45726 | -60.40755 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a828ecbb-a491-3a9e-a0f2-b2e7bc9d1e79 | -7.80396 | -61.34739 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3b2dd665-711c-3508-9cac-3414fcb574c8 | -8.10539 | -61.21201 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 004b0862-2487-37ae-8ff1-734344fd9598 | -7.4564 | -60.41253 | 2025-08-15 04:51:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fa14f75f-b9ea-3e56-af3c-775b5a7bb37c | -10.53554 | -42.55246 | 2025-08-15 04:51:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 5.8 |
| a2ea08d8-e3ec-3161-8e4d-fd726aff942c | -9.85339 | -47.8271 | 2025-08-15 04:51:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd63f0f6-f3af-316d-bf4a-9bb7f9b1b08c | -13.11362 | -57.16958 | 2025-08-15 04:51:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 90ec0628-b233-36e8-8971-8a7789a92dd7 | -7.87202 | -61.82005 | 2025-08-15 04:51:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1f5e7903-31ea-3009-a159-7b42f84070a9 | -12.75982 | -44.41038 | 2025-08-15 04:51:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| cdcf5277-bf8e-33a1-8645-66bd2123b6a5 | -9.18527 | -45.32286 | 2025-08-15 04:51:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |


[Clique aqui para ver as próximas entradas](README44.md)
