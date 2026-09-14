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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 21083f6b-6618-368c-a66e-39119da701bd | -2.88444 | -50.43316 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 884de36b-d547-3042-a6ed-9aa685ac1170 | -5.84713 | -52.10014 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9089f3eb-79fa-3408-949f-0452c0b30e27 | -6.65905 | -54.98099 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 150bc14d-14c5-3b88-a4b6-e0350e55caa7 | -2.94009 | -50.44107 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0753f365-d569-389e-8e33-96c49cc34952 | -2.91812 | -50.45236 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| ae62c009-d93c-36ad-a45c-b26779662954 | -5.84801 | -52.09493 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| b38643f2-5318-36ad-b4ac-62a299ca27cb | -9.4531 | -50.12997 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dcffced8-84e9-3bdb-bc58-5334f57c18f1 | -6.74233 | -50.9281 | 2026-09-14 04:32:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 211bc2d4-fcde-307f-ab97-190f3f990825 | -3.79327 | -44.11362 | 2026-09-14 04:32:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3eae626b-32d3-3e72-9994-2c5b5f86bbc2 | -7.09544 | -55.62089 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c0f43b1-ee77-3c92-b7b1-bfb4872480b1 | -2.93925 | -50.3912 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 547b21a6-0ebd-34f1-8950-d729fd48f037 | -2.92189 | -50.45751 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8d96ef6a-06d1-3c5b-b040-204e57eac959 | -9.4461 | -50.1235 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bbae5069-3b45-3b38-a744-8a57e1fd4e63 | -7.09749 | -41.79837 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 0694aa56-3746-3092-82e8-1e74097f2d82 | -2.92888 | -50.42568 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| 457bc07d-cb1a-3d31-ae5a-515a80e5fe02 | -7.10472 | -41.79944 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 9c761fab-440b-3451-b053-e79735828f3e | -2.78026 | -51.36699 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a32744f6-7370-3c31-8322-c6eeca341cf8 | -6.15128 | -57.69548 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c97c0ee0-6bad-3979-b4db-0575aa8cf39a | -7.42413 | -41.92427 | 2026-09-14 04:32:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5121a074-f407-3dce-8e7d-c11701336149 | -7.96381 | -43.98831 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8a204eb8-d613-3b0e-b8e4-6be5314a21b7 | -2.92069 | -50.41977 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.7 |
| 43c6f43a-7b5d-35fe-8c30-ddd6c115c0a0 | -3.55081 | -48.17934 | 2026-09-14 04:32:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7fd4b2d-b80d-3d8e-b152-dd08bf4151b2 | -7.08237 | -43.53946 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dded6a26-3f3d-3347-904f-0099b8cf671e | -6.85618 | -55.5712 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3579c206-c347-3d82-bed7-f031c2a78d9b | -9.02361 | -49.81225 | 2026-09-14 04:32:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 15651bd5-a7e7-36c0-8b5d-401be8d7cc99 | -6.30032 | -55.2826 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 19ef71a2-052a-31f2-af74-e575acd936cb | -2.92441 | -50.42495 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 30.3 |
| d5b3980a-d8ad-39f5-95b9-4d1e206205d4 | -2.92379 | -50.41703 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 133.6 |
| 2aaead75-e425-3cfa-9893-5140e8fa2364 | -2.93562 | -50.44033 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 68972792-3cb5-3382-9bdb-dd2d76816764 | -6.15194 | -57.69452 | 2026-09-14 04:32:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 74e9067d-9ac9-3d38-8a8a-c71d919876a5 | -6.29595 | -55.27344 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 82b0ce09-d24d-3ba0-8f09-1e3530d485f0 | -6.78549 | -47.88623 | 2026-09-14 04:32:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e6e0a41d-7eac-3912-a284-426f39e8ee4d | -2.88731 | -50.41553 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7125539b-b31a-3e1e-83d4-76a8df4e6c05 | -8.12295 | -54.8026 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ed6cb313-d187-3672-aa74-f2c5f82cc778 | -9.48594 | -45.46483 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9ad319fa-d189-3467-9f44-8f3157166b43 | -2.91599 | -50.46565 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e7b0fd51-dfc3-3c85-98cb-2036159bf78b | -7.68383 | -46.65008 | 2026-09-14 04:32:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c0928504-67b8-3e70-b826-6c62ce8bb037 | -7.11696 | -41.7953 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6f41121c-fd41-3c9f-8949-4ee35695640d | -9.40778 | -50.16788 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 42282eda-9381-3f34-b104-eac29304d5ba | -5.1208 | -55.96047 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 590c6a9d-e0f6-38f9-af0f-7528a82d40b1 | -5.76101 | -44.05809 | 2026-09-14 04:32:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 0c227c41-d24a-39c4-a065-76ab91559be9 | -2.69947 | -57.54862 | 2026-09-14 04:32:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 24bd6ea9-35dc-325c-8192-e547e20af77d | -2.87996 | -50.43242 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9198d24a-9df3-3904-8832-43d7ab085b9b | -9.41564 | -50.12189 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c0854b4-c567-3642-9973-2528fd76245c | -2.94604 | -50.43295 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9321f248-c211-36f8-a1d2-1696bf761516 | -2.90932 | -50.47851 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b7af7128-dca9-38f4-8f4c-4d8d74ab9e6a | -2.94596 | -50.40591 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 69132d81-2a9c-3ccf-a343-b3ee020b1613 | -2.92236 | -50.42589 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 108.6 |
| 967f74bf-1154-35cc-a40f-279bde2aa8a4 | -9.4389 | -47.85575 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94b6179b-1b8a-3dfc-9d35-a6c48947082d | -2.61888 | -54.72683 | 2026-09-14 04:32:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6ce6162f-faad-3b86-9d00-9ed5edc9ef6b | -6.66277 | -43.65461 | 2026-09-14 04:32:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d6b026-7ec0-3140-ba54-c83df45d4fdf | -2.92293 | -50.43376 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| 41326b4d-fec0-3c3b-88ad-d303ed0abcd4 | -7.99929 | -43.78428 | 2026-09-14 04:32:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5877a027-198c-3ffa-b901-38588ff4c34e | -2.9445 | -50.41466 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e50ed6b0-06da-3c7b-aa02-918c49e962c6 | -7.11813 | -41.78446 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 41a699ec-1524-3aea-804e-456543d2c17e | -6.58485 | -58.84001 | 2026-09-14 04:32:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4f276ca8-6848-3cf2-8086-9783175b5800 | -4.38117 | -55.20284 | 2026-09-14 04:32:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a7f417e6-9d2e-31a0-b0c5-1a5be55e37b6 | -2.90844 | -50.45535 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8eff7ccf-24ef-3b9b-9f7c-ed30b15f4953 | -2.93414 | -50.44918 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 76943795-a871-3acf-a980-a681308a8206 | -9.43454 | -50.13042 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 2087640f-0e10-3df2-9c22-e2256a84f644 | -9.32689 | -44.36423 | 2026-09-14 04:32:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0f169359-c11a-31f3-bfb8-becd255f4708 | -6.91584 | -55.6316 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8c32456d-9f63-33cc-9383-7b3adadba827 | -3.22922 | -50.59197 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 966c911f-2c9d-33a7-8c3b-ca477d49dfda | -6.85368 | -45.03928 | 2026-09-14 04:32:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f6a8eb31-3c34-37c2-8b91-b4250d61dacf | -2.90681 | -50.43694 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 54ad540b-1c86-3450-bccd-48bbb9a3867e | -4.26795 | -48.64147 | 2026-09-14 04:32:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ca63bb6b-4b36-375c-99f7-083c7e8f385f | -5.4246 | -51.32867 | 2026-09-14 04:32:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb3912c0-5fb5-3faf-b7bc-0297baadbb79 | -8.5428 | -54.70491 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46598fc9-9c44-32b7-983f-ebd7323aaf02 | -9.49425 | -45.47693 | 2026-09-14 04:32:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 076a4a41-5bc7-3611-90c3-1672b8241ad7 | -7.96773 | -43.98528 | 2026-09-14 04:32:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05c83ad6-173d-3854-9522-683db9f203d9 | -2.89411 | -50.43024 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 6e21d717-28e7-3e43-ad2e-132b77305a94 | -5.13419 | -55.95752 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2c2d23fd-d5ea-30dd-a906-2d259f84866e | -6.17671 | -43.34926 | 2026-09-14 04:32:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b1e98388-fc08-38e4-a24d-2b900161edc9 | -2.8866 | -50.41993 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 43f77fb0-ff0d-37eb-aff6-4a104c0dfd1f | -4.59446 | -47.17793 | 2026-09-14 04:32:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5a9f3491-4e2b-3822-be22-03bb96b468eb | -7.5604 | -41.83998 | 2026-09-14 04:32:00 | NPP-375D | CAMPINAS DO PIAUÍ | PIAUÍ | Brasil | 2202109 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6c07ba16-70e6-397f-b7dd-0b86cc8ec044 | -9.40252 | -50.19862 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 20214ec8-e77b-3753-8676-6c7b53f922f3 | -7.09685 | -41.80251 | 2026-09-14 04:32:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 748b107d-cb65-3bfd-9e56-509bc65b4ffd | -6.85696 | -47.42415 | 2026-09-14 04:32:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6a5a461-3474-3b1d-8ab8-14328ed1f59f | -2.88588 | -50.42434 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 6baf4c4a-9b19-3f96-a2ad-f7b4d91ce010 | -2.95051 | -50.43369 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7d29c178-926c-3db6-adbc-c7e32153f8cb | -2.92592 | -50.44333 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.6 |
| f2afd075-e31f-3979-8156-3a1f80339453 | -2.91556 | -50.41112 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 81.0 |
| 62f17f7d-ac0b-31a1-a6d9-5e42948d2841 | -9.40206 | -50.17741 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 18a230b1-e876-3b0c-b092-ddd190af0877 | -6.29449 | -55.28138 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3cb61bb3-9179-3c12-aa47-7fd82e997e89 | -2.94897 | -50.41537 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 668e40ad-49a7-3ae8-b965-cb58d93a563b | -2.89912 | -50.39938 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6558e236-89a9-3e49-98cb-42c10b725cf1 | -2.93061 | -50.43174 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 75d7ed54-99e6-3f40-b91d-86e766cd3b47 | -3.07651 | -51.20191 | 2026-09-14 04:32:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 64708f12-ae8e-3852-8ced-a8545976937f | -9.4354 | -47.85518 | 2026-09-14 04:32:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 144c1154-2f0e-3a0c-a2f3-53862781e2ea | -2.92472 | -50.43985 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 96fc5112-73eb-3f59-b786-4dcd00895068 | -5.12795 | -55.95644 | 2026-09-14 04:32:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 6cc855d8-518d-3954-8606-19508a24c390 | -6.40683 | -44.03818 | 2026-09-14 04:32:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f567e375-9bf6-3fdf-90b5-9220832999a3 | -8.53936 | -54.71865 | 2026-09-14 04:32:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d9d1e113-cdc0-34a8-848e-3f427a1141e9 | -9.37826 | -50.17323 | 2026-09-14 04:32:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| fdf1ff15-4135-3887-8aaf-d35afb08c621 | -6.85361 | -55.57092 | 2026-09-14 04:32:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b26632a-6be0-3395-9c83-67544e3fb843 | -2.95644 | -50.42561 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2ed240c5-8f3e-3d19-8f88-b6e0bdc1dcb2 | -3.38367 | -50.39423 | 2026-09-14 04:32:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| cf972984-2f5a-36ea-8763-7b87039c75ef | -7.0869 | -43.5549 | 2026-09-14 04:32:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 83a6e1a5-ae61-39f9-9feb-e0671f5a8d26 | -9.44888 | -48.10157 | 2026-09-14 04:32:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README23.md)
