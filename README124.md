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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06d4aa7e-d61d-322e-859a-f73d928c4335 | -13.2787 | -51.795 | 2026-09-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 182.6 |
| a9a4995e-1901-338e-8be5-9938c6906fc8 | -9.9768 | -50.2694 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| 42117a73-87e6-3741-8ba6-a29fbc4e6e3b | -12.2723 | -50.1657 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| eee0d2f9-9ca2-39b4-9f7c-07374e3e1ac5 | -11.0412 | -54.1362 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 92.7 |
| dfd2ca94-a026-3201-a1f3-74fe932b9cce | -10.09 | -50.2581 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 28285215-4dd6-37bf-86c6-4ca50be10c91 | -3.6632 | -58.8643 | 2026-09-21 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 91.4 |
| bdf9dbc0-c94b-33aa-aef5-cd529db2ed4b | -10.8746 | -50.9227 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 8cc02d42-8abe-32d2-8a87-d1b12b1a3dc0 | -7.3291 | -55.1955 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.6 |
| 5e76fbfe-0e54-3aaa-82e6-264048ac5baa | -11.3419 | -51.3606 | 2026-09-21 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 114.8 |
| 5225140e-8a81-35c8-8bce-96a934d0d936 | -3.7856 | -60.7335 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 54.0 |
| e64d82be-e12a-39e4-b6ff-898d8c2f4c32 | -8.7726 | -44.28 | 2026-09-21 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 156.3 |
| d6a573dc-b80f-317f-942a-5a391bea4d23 | -10.0898 | -50.2795 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 128.6 |
| 2a3bb8ad-0972-3d3b-8369-7d0f8fbb0965 | -3.3454 | -42.7597 | 2026-09-21 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 157.0 |
| 7995c57b-c656-3b17-b9f1-6fb2b5acea31 | -11.6798 | -43.4446 | 2026-09-21 14:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 195.7 |
| 58f9d4ab-932f-3ece-87f8-69e33396b5ac | -3.3823 | -50.4486 | 2026-09-21 14:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 272a6207-c150-3006-89e1-0822c7b017b8 | -11.36 | -51.4221 | 2026-09-21 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 89.8 |
| 1f3142c0-9ac6-3658-85a8-301467d0e2f6 | -6.4485 | -59.9909 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.2 |
| 376b6266-5033-3a30-8d71-9fca5d1f2be3 | -13.3443 | -51.2973 | 2026-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 188.4 |
| dccd46ef-33a7-3e64-a106-124f4aa5f1b6 | -10.6889 | -50.6658 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 1141edca-38b0-3b4c-b0c8-dc03603a8684 | -8.7729 | -44.2568 | 2026-09-21 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 90.9 |
| c2f08883-8917-3212-88d1-8e30456800bd | -6.1359 | -59.9446 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.5 |
| b180207b-d469-35ce-a14c-05dd0d1b4fe1 | -6.467 | -59.9902 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 7c6cbbaa-a911-3300-8bad-5bf81246035f | -7.4092 | -44.7885 | 2026-09-21 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 143.9 |
| 23fc3043-3cb1-3e8c-9162-15d0653ee14f | -14.1815 | -51.808 | 2026-09-21 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 96.0 |
| 9584b18c-0c28-3137-b087-a8dc9014546a | -12.3025 | -50.6774 | 2026-09-21 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 77a18e36-42a1-30b1-92ca-b3465d7ed513 | -12.3102 | -50.1826 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| ffb471db-e3c8-322e-96f6-28f7c6285773 | -8.7267 | -44.8836 | 2026-09-21 14:00:00 | GOES-19 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 90eeba12-f182-366e-a014-94126e5117c7 | -10.4675 | -50.2624 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 89.3 |
| d9953b8f-e0b1-3898-ae17-3efee97362bf | -9.238 | -46.1894 | 2026-09-21 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 4865587a-0d01-3d67-a037-88d122dd0579 | -5.804 | -53.5223 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 4fc66499-ca92-34f6-8572-71c7ebca316d | -6.4671 | -59.9711 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 64.1 |
| e387b5de-4162-394e-8396-98494eb05169 | -12.8711 | -50.9505 | 2026-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 118.9 |
| ff17cab5-9f20-38ee-8076-19f7bf623f02 | -8.8735 | -62.4305 | 2026-09-21 14:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 51.8 |
| dfa4f22a-3bac-3cf6-b8b1-2581eb52a7cd | -5.9335 | -59.9515 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 123.2 |
| dc2bad89-1ee8-3ccd-9042-5143e4eb751c | -4.9533 | -45.16 | 2026-09-21 14:00:00 | GOES-19 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 163.3 |
| 6518565a-63f4-3aa1-a985-3657b633cc73 | -12.8056 | -54.0462 | 2026-09-21 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 811205a7-203c-3421-be72-f6366f30bc03 | -7.4217 | -42.1239 | 2026-09-21 14:00:00 | GOES-19 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 88.1 |
| 0aa8f263-4f07-3dc2-b340-5dcb66ab68e9 | -5.9151 | -59.9522 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.7 |
| 953a4a52-7573-3ec1-aa03-846bb557eef9 | -8.1876 | -54.7219 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| a5422aaa-7e4d-31f9-af93-14ea489cdac3 | -12.3018 | -50.7203 | 2026-09-21 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.1 |
| a76bc214-b6bc-31d8-9176-f3880f6f3825 | -11.3603 | -51.4009 | 2026-09-21 14:00:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| b1a2b503-a5b4-3c7a-8237-46c7107eb5fb | -7.5704 | -57.6766 | 2026-09-21 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 106.3 |
| 48b099e1-7066-32e5-82a2-8b8a826d9d24 | -3.6449 | -58.8647 | 2026-09-21 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 08eff0f9-479c-3d0f-acc5-32abbc7e73d9 | -6.7119 | -58.9992 | 2026-09-21 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 18264c47-070f-3316-badc-f3bb063cee88 | -14.1819 | -51.7866 | 2026-09-21 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 113.7 |
| 57bf9031-4c58-34a0-9b8d-2e0b67c35ee5 | -10.4486 | -50.2644 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 99.8 |
| 730f5d1a-76e1-3b09-b60c-9a66360b6006 | -11.662 | -47.7737 | 2026-09-21 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 130.3 |
| da02f360-d6b8-31be-b1d6-04d4a8bf386f | -9.977 | -50.248 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 43ee070f-f71d-3777-98e7-4b74ab9f0f67 | -11.6429 | -47.7761 | 2026-09-21 14:00:00 | GOES-19 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 109.0 |
| c26efaa3-10ae-3083-976c-c0dee465046b | -5.8411 | -53.5002 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 95685247-f6d1-3910-87f1-b876b37d7b8c | -2.8791 | -57.8184 | 2026-09-21 14:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 131.7 |
| 2914f7c2-1e5e-3e44-ad46-a2da376cb99e | -12.9091 | -50.9672 | 2026-09-21 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 108.7 |
| 83d2384b-e91a-38a0-b73c-fd9e5e86048f | -9.8307 | -48.451 | 2026-09-21 14:00:00 | GOES-19 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 179.0 |
| 94ac71a8-c29b-3d30-adaf-d3689220752a | -8.7912 | -44.301 | 2026-09-21 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 85.6 |
| a3b8de22-568e-3b34-9eca-e6dfa83c5ee6 | -10.8853 | -51.5347 | 2026-09-21 14:00:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 104.6 |
| 4f127571-81af-3e7d-b971-d4c6e8f8b9f9 | -3.7129 | -60.6022 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| dfa6f751-d555-3fc2-abbd-44a3f1dfcfdc | -10.4672 | -50.2838 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.3 |
| 9a5fadd5-0b4c-3968-81f6-6999f1accfac | -5.6221 | -43.3934 | 2026-09-21 14:00:00 | GOES-19 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 244.6 |
| f33d5588-088a-3595-b810-d8c68ac0a67f | -3.7129 | -60.5832 | 2026-09-21 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 74.6 |
| e5e3ea41-9d10-3d5f-8237-fda37bec3015 | -13.2791 | -51.7737 | 2026-09-21 14:00:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 135.4 |
| 4fd0657a-6a3e-32c5-9fc6-70bf44febbb5 | -6.5569 | -45.566 | 2026-09-21 14:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 5e713bc4-fb32-3747-ac10-35ca1ef03265 | -6.8448 | -55.5411 | 2026-09-21 14:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 74.1 |
| 8fc6a17f-c936-32a4-bc34-517652f72a6f | -12.3105 | -50.161 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 141.9 |
| 1d1bfdff-192c-3dbd-99b3-e35e0285aca1 | -5.9334 | -59.9707 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 140.7 |
| 8074c744-445e-32a9-9e0a-0d5ddb26fbc2 | -8.7911 | -48.7502 | 2026-09-21 14:00:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 173.0 |
| 2c51b4e2-5a8c-3aff-8d68-cb1c0a1688dc | -9.247 | -57.1488 | 2026-09-21 14:00:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 7350b63b-4c48-362b-9f15-f3e4cffaf4da | -10.7259 | -50.7257 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 137.8 |
| 8db938e5-53a1-3522-b52c-984fd61fde9f | -11.7823 | -49.8152 | 2026-09-21 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 82.5 |
| b8327fe7-7036-3bbd-9d1d-35dff0745187 | -3.3267 | -42.7606 | 2026-09-21 14:00:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 87.5 |
| ef130c52-c181-3c01-b4a3-38999091664c | -11.118 | -54.0268 | 2026-09-21 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 794e3cfd-f6b6-355d-8394-f72d4dd1bc7d | -6.4301 | -59.9916 | 2026-09-21 14:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 64044acc-bf91-38ab-be35-451fd7251409 | -8.1874 | -54.742 | 2026-09-21 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 110.9 |
| 464a7af5-4606-3db4-84ef-be937db5a2d0 | -10.7652 | -50.6153 | 2026-09-21 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 114.3 |
| bd768d78-5c3a-3d89-9f61-102330e701c9 | -3.2162 | -42.4833 | 2026-09-21 14:00:00 | GOES-19 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 112.8 |
| a7648315-81b0-33b7-be22-0e58fb6b6873 | -10.279 | -50.2391 | 2026-09-21 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 96.1 |
| d01e921d-7505-35a7-b357-d29bcbfe5642 | -3.1698 | -58.5859 | 2026-09-21 14:10:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| 5d7a4d4c-a793-3f75-8fb6-cf6e3557c17e | -4.2239 | -48.6127 | 2026-09-21 14:10:00 | GOES-19 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 48fd0c99-b151-311b-8c0d-2ac207ad8c6e | -7.5059 | -46.2269 | 2026-09-21 14:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 71a76abd-1c61-30b7-9da1-5c20ffde2c2f | -7.3289 | -55.2155 | 2026-09-21 14:10:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 62.8 |
| b141001a-9ab2-311a-94f8-567b654dd281 | -6.4486 | -59.9717 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 98b59aba-374b-3e12-81cb-fb3198996d58 | -9.2759 | -46.1852 | 2026-09-21 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| c4d6204b-6d2b-35bc-8416-a48c9a7142be | -6.4485 | -59.9909 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 6b99c119-fdbe-36bb-a1e7-c7c8ea19c4d7 | -10.8002 | -50.8243 | 2026-09-21 14:10:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 2034f5ce-3fe4-3121-be90-605bb2a62945 | -10.3549 | -50.2099 | 2026-09-21 14:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 108.3 |
| 2015d104-6ab8-3e26-b7e4-a300046937ec | -8.7914 | -48.7285 | 2026-09-21 14:10:00 | GOES-19 | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 103.0 |
| 1c7d8388-ff3b-38ce-98fa-29c07b7378f7 | -6.8985 | -41.6976 | 2026-09-21 14:10:00 | GOES-19 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 135.5 |
| 15d8ae06-8afb-3b3a-a828-34b6ced87700 | -11.4537 | -45.3892 | 2026-09-21 14:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 9d1333b9-de27-3694-b0c5-aee491b0355d | -3.6632 | -58.8643 | 2026-09-21 14:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 92.0 |
| 6e6b20b4-ef94-35da-a657-d17a601ebf4f | -6.4301 | -59.9916 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.9 |
| b7d0088d-0b1e-3289-afc0-6ba1319a44d5 | -8.3167 | -45.9934 | 2026-09-21 14:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 63.7 |
| 3aa33a9f-74c6-3fe1-adce-fa42cac1987d | -9.0239 | -48.1622 | 2026-09-21 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 123.5 |
| 9bf2897c-ba06-3ad0-9ea2-8f987704f814 | -8.7706 | -45.8567 | 2026-09-21 14:10:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 117.5 |
| 5aba6237-8f3c-3be3-a9b3-eae70b95bd77 | -6.467 | -59.9902 | 2026-09-21 14:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 93043fca-9d0a-3f5e-b1e4-01fff2f71028 | -10.473 | -51.2808 | 2026-09-21 14:10:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 110.8 |
| fb616bed-b2b4-3477-bf1a-509c334f4638 | -8.1874 | -54.742 | 2026-09-21 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 99.7 |
| c5417bec-262d-3494-bbbb-c6d2ee863732 | -3.3267 | -42.7606 | 2026-09-21 14:10:00 | GOES-19 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 6151e2d4-2a0a-38bd-b871-1cfaf6aa667e | -9.0428 | -48.1603 | 2026-09-21 14:10:00 | GOES-19 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 157.6 |
| 1246f6b4-efe5-36ad-8f65-eefc4ce86514 | -6.5759 | -45.5419 | 2026-09-21 14:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 1515c340-9630-3e86-a0f6-44143d2e03f7 | -7.3734 | -44.6316 | 2026-09-21 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 128.0 |
| 640be7bf-b545-3e8d-abf3-0e8c7996e45c | -10.8921 | -53.9857 | 2026-09-21 14:10:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 70.0 |


[Clique aqui para ver as próximas entradas](README125.md)
