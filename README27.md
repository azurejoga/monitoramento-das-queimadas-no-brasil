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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ece40ea9-e92b-3f88-84a1-cd188f9df623 | -9.56881 | -49.27102 | 2026-08-26 04:51:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 22c9a83b-e61d-315d-a7ca-2afa973252a9 | -7.79327 | -62.39341 | 2026-08-26 04:51:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f04041da-cd1a-36a4-b417-464762f09507 | -3.53644 | -48.18369 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| a6fdf996-0d47-3864-ab05-307b63ae50b7 | -7.37655 | -55.19148 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c382505b-1591-386d-aac3-d9bcf4d0217b | -6.99305 | -59.26908 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 23b68998-e19d-3af7-bc7e-9d72a5c31041 | -9.044 | -50.79487 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 6ff36b4b-325f-3770-824d-7bf529040789 | -6.62022 | -58.48671 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 575a6d2b-9b3e-342a-a120-1384b5e50ff7 | -6.12397 | -53.75311 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0208e681-a5d8-3c84-a3fd-189d59a527d4 | -8.03409 | -51.81102 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 822717a8-c84c-3301-bfc3-d71e1dc547f2 | -8.09194 | -51.67957 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e80bfa5f-2c1f-381a-a906-3b486af975b6 | -9.97536 | -48.32714 | 2026-08-26 04:51:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c952f48b-e637-3d31-9cd9-ab6b19a01988 | -9.18982 | -49.99471 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dac7e0ad-0f6e-3843-9afa-312161ac385c | -8.54232 | -54.77729 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f461990f-5680-35c8-8090-43bf31da2e24 | -6.12218 | -57.82991 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 60d8ca21-e841-3006-a3f8-f030219ff813 | -4.9466 | -43.19981 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f6e5f15b-dee4-3800-a15a-0ee46bbb936c | -6.63438 | -58.50941 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ec65a6d0-ca3b-3ff5-879d-51fb3713cb80 | -7.40539 | -55.16033 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e7bf3a27-5127-37e4-99f9-525bc5a53103 | -6.2761 | -53.37099 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f450f3b8-4815-3130-ba57-a3f77ed7bc1a | -5.44243 | -45.20213 | 2026-08-26 04:51:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 87b96381-e533-337b-9f9c-33acbe8c3566 | -7.75487 | -44.75864 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf8a9b9d-e1b6-33ed-a853-8db091f7b893 | -6.77799 | -59.43769 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 8983ba7a-f42b-3cc8-910f-e6b040652c49 | -9.01726 | -50.77557 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 917b98bb-aa2a-346f-943c-bf246a626925 | -3.13305 | -61.18307 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0973b694-0f5d-3b16-8c46-d584f205d5ea | -8.60286 | -54.85425 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 29efd4a3-b01b-3d5a-af59-6a39b257881a | -7.0504 | -44.89703 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 768cd4f9-6b61-3960-ab63-08ce107171f8 | -6.02834 | -58.04588 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9e55e2ee-70f7-3142-8c09-b3ee3ffb0f3e | -7.37593 | -55.19535 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c0e4ec9a-5323-32d5-94a0-dcda2aef966e | -8.77835 | -49.97054 | 2026-08-26 04:51:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 60849f30-e6b0-3c5a-974a-4082574ce0e8 | -6.12044 | -57.69126 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f551006d-26a1-3979-8e4d-cbfaa8a6a633 | -7.74986 | -44.75783 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| aed2b12c-ea59-3fef-b97a-4d67157a0cc4 | -7.4979 | -55.34848 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2a98599c-0b0a-318e-aeec-52d668e185ad | -6.7604 | -59.4442 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 99b53204-d0cd-3912-b6d1-11846a9fc0d9 | -6.61222 | -58.37844 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9c30a70d-98ca-32ee-8ee7-2684e147cf1f | -8.13704 | -47.51117 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 78f5d7ce-664c-3903-adfe-a03dc72168fe | -9.18618 | -49.99417 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11747963-d167-3a34-8a52-a658366efe22 | -8.57087 | -54.8155 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eeb7d7dc-37bb-315a-942e-d62e72693c4e | -9.42049 | -51.65557 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8cab66e1-dd23-35e9-aad7-5829274caa87 | -7.31415 | -42.99218 | 2026-08-26 04:51:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| f3a672d3-a3fd-3e43-b5e4-6c9084e1c8f7 | -7.29756 | -44.08562 | 2026-08-26 04:51:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c6b59313-e8c5-3e64-9b86-ba8f051f9060 | -7.76104 | -44.75085 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 8b0e8e64-a88f-3f04-9301-3ebbf4682622 | -10.37758 | -45.06672 | 2026-08-26 04:51:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e4c6aaff-4fea-3ab7-8a74-4eab9e2eb0c5 | -7.52143 | -61.38779 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 30.5 |
| b35fd0b6-9927-33a2-9bba-57be88ec02c7 | -6.83584 | -59.94511 | 2026-08-26 04:51:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 52e814d0-e40f-312f-abfc-a61356fe2cfd | -7.5228 | -61.38505 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 6ac5e55d-f1d3-3d25-bf7a-54ab36d981b2 | -6.44188 | -54.97069 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9a93ee88-7593-3d0d-a855-8345cf1942f9 | -6.12784 | -57.72119 | 2026-08-26 04:51:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd482099-7215-3d33-bacd-6a3067c24e3f | -8.22466 | -55.00215 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 208dd573-2590-33d8-931e-b0c8e0b82c91 | -6.70138 | -56.34231 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cbbfa28e-cc75-3963-af9d-60e7fcba8d4f | -6.25729 | -53.36092 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 698a410d-757a-3569-b2e0-dab2895cb8b3 | -6.72386 | -59.44265 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e4a2a8dc-96c3-3e1d-99b6-ca250b6ecdd4 | -9.02304 | -50.78477 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6b02cd04-54da-3212-ac72-b51d020a17f0 | -7.37371 | -55.18702 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 80d8c829-ab7f-3da3-a309-677b5943f263 | -6.70304 | -56.14885 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2bb07ed8-756e-3619-83a6-2fb187748f50 | -7.47292 | -61.37336 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ef4a051f-4e26-3bde-b94a-ab960bf7d0f6 | -7.45114 | -43.09473 | 2026-08-26 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5aa8ca16-cbff-3812-8060-67f04e51c9a9 | -6.26997 | -53.32367 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f446fed-4418-3b2f-affe-0ff3139595e8 | -7.25821 | -49.85744 | 2026-08-26 04:51:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5bc795ba-0975-3b62-a9c8-1005a9f2cc32 | -8.52571 | -55.31464 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 143db068-e102-3d18-9956-67ed8f08deb9 | -7.06796 | -59.22719 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2d89d0fd-85ef-3090-8893-d0764b4270cb | -3.13251 | -61.18642 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| da02fbca-a5c6-39e9-9e0b-752e3f648603 | -6.63218 | -58.49698 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 59494cbc-4207-3fea-b957-8c9426a4d6e7 | -8.11156 | -51.66409 | 2026-08-26 04:51:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 198eee4b-c130-3114-a7bf-c3c104cca1dd | -5.01963 | -46.08799 | 2026-08-26 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58e634da-bce0-3625-bd31-30662fe030eb | -6.18371 | -55.44148 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f48b1f4e-bd1f-35a2-8f4a-47c69fbb5d35 | -7.48362 | -55.28299 | 2026-08-26 04:51:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c57f4dc8-4cb2-3705-982e-4bd26723a865 | -9.03936 | -50.79539 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| d3660a7a-47a9-39a7-8765-6717d3757cb7 | -7.30286 | -45.35995 | 2026-08-26 04:51:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27ef300a-2648-31b1-86e0-c33c376b8ae9 | -2.79984 | -49.58085 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| a21729c1-f36d-3038-ab61-544e7fcb316f | -6.27665 | -53.36751 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e83acb5b-e1d1-3260-b9d6-cf8ac091bdd0 | -8.14651 | -54.98555 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3f3934b9-90a6-35cf-8eac-06641be36a72 | -7.75602 | -44.75002 | 2026-08-26 04:51:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| f5b76f5d-7977-37ce-8062-f75630841968 | -7.02591 | -59.23481 | 2026-08-26 04:51:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de18de16-fbe8-3529-abfd-175d8534564c | -9.41418 | -51.62826 | 2026-08-26 04:51:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4173e2a0-eaa8-38e2-ae92-e2ed41519f90 | -6.33506 | -54.74194 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 166b6bbf-8bab-3463-99fc-4afa75da79be | -4.80424 | -45.77066 | 2026-08-26 04:51:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| defaaade-d063-36f9-97a9-2dc935ff679e | -4.80532 | -43.16963 | 2026-08-26 04:51:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1c859a39-feaa-3371-9de7-185dab3733ee | -8.62323 | -54.70462 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ec0f2a7a-fe93-30c9-b703-bbd42d44adc7 | -8.5977 | -54.86479 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb34815e-46b0-329f-8965-a4400b2da942 | -3.20357 | -61.14318 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3aea51b9-aad7-39f1-8dcb-7f50d9acd528 | -3.59108 | -50.67744 | 2026-08-26 04:51:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f06526a6-1885-33c3-8ad2-5b0c7d42c633 | -5.91732 | -43.64511 | 2026-08-26 04:51:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 342def1c-c680-3da3-93cc-df02938cca3a | -2.79636 | -49.58033 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d7d3cbc4-625d-3015-84e9-3d438708e364 | -10.04229 | -46.04843 | 2026-08-26 04:51:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 08ca5008-4f33-300d-ae4c-add07c9a5b49 | -7.45011 | -43.10257 | 2026-08-26 04:51:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 874839fb-acb4-3d6f-be7f-4f2b5e940b96 | -6.65071 | -51.48875 | 2026-08-26 04:51:00 | NOAA-21 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 04c57b1f-9e31-31ae-b1a5-5b5f47838225 | -3.26953 | -49.52701 | 2026-08-26 04:51:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2a99d4b7-3f12-3eb4-ab46-94f46eca45de | -6.18083 | -55.4369 | 2026-08-26 04:51:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d098742b-292e-3654-82f1-e5f151ff7796 | -3.01276 | -51.05227 | 2026-08-26 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7e00ed96-5352-3180-b817-b3dec0b609f4 | -3.51638 | -48.0354 | 2026-08-26 04:51:00 | NOAA-21 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cca1389c-df72-3555-a402-de34da991041 | -9.03356 | -50.78632 | 2026-08-26 04:51:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| adaf0fa1-c52e-3748-bc73-0b9f135c9d6a | -6.26282 | -53.36892 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0656bf26-3002-35c5-ae04-f167e5e0b78c | -8.59488 | -54.75215 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 529ce7fe-4341-3c0f-86de-8b39e57c498e | -5.65841 | -46.95277 | 2026-08-26 04:51:00 | NOAA-21 | MONTES ALTOS | MARANHÃO | Brasil | 2107001 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 10cbab61-109a-3252-9805-91d6fce18910 | -6.63151 | -58.50089 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 97bffee2-d618-3d45-9e5e-b9fbe51dfe7e | -7.56605 | -61.42904 | 2026-08-26 04:51:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 81c08ca8-8a18-3a2d-b5d4-81d43a78642b | -8.14177 | -47.50796 | 2026-08-26 04:51:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 64a6e7de-76d4-390a-ad35-3f160f06b59e | -6.27056 | -53.36298 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 17f74a58-52ed-38d6-bf44-36f42a93c39d | -3.13476 | -61.19392 | 2026-08-26 04:51:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9b48a609-093f-360f-9bbb-0588b3660084 | -6.64964 | -58.49593 | 2026-08-26 04:51:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 17b5082f-6186-3956-9b9c-df8aae281f06 | -6.26726 | -53.38388 | 2026-08-26 04:51:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README28.md)
