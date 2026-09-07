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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f57bf169-9cd7-389d-894a-7c325711e293 | -13.2287 | -61.7355 | 2026-09-07 00:40:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 3d3ec79e-9cf5-32bb-b371-198cf4160936 | -9.7519 | -43.4143 | 2026-09-07 00:40:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 104.2 |
| e1465aa1-a11d-3017-a2e6-2aed1c341b82 | -2.6388 | -46.7597 | 2026-09-07 00:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 96.3 |
| 2f9986ed-c916-3b79-b703-d9e4f939f47f | -4.1102 | -49.0675 | 2026-09-07 00:40:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 61d75941-b566-3e12-8cc2-82292dd7f3de | -6.9474 | -59.7607 | 2026-09-07 00:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 55320919-3f07-3eb4-b9e3-606cec25f811 | -11.0323 | -44.3396 | 2026-09-07 00:50:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 83.6 |
| b2a0dd33-07b5-357a-80c8-d3d078b21929 | -2.6387 | -46.7817 | 2026-09-07 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 177.4 |
| 9025a1c0-5ba4-3255-9687-acd9851243e4 | -2.8654 | -50.4643 | 2026-09-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 52.0 |
| fe5e480d-db9d-3234-89aa-9de5cfe39b90 | -9.7332 | -43.3932 | 2026-09-07 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 141.6 |
| ba629071-90c0-32cb-a9f7-394d5ccfe152 | -6.6513 | -59.9642 | 2026-09-07 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 24a02f65-4f6c-30d9-bb19-5796aae68f25 | -3.6033 | -60.5664 | 2026-09-07 00:50:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| fc7e42cf-bc10-3f3b-8700-faea95e185d1 | -5.3646 | -56.0249 | 2026-09-07 00:50:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 621ca061-60c6-38d6-8428-362b57d38e2c | -6.6698 | -59.9443 | 2026-09-07 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 8185a029-d1a0-3560-b861-6110d71dbceb | -13.2287 | -61.7355 | 2026-09-07 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 91.5 |
| a4430d8f-e55a-3350-8e23-c33e17725797 | -9.7522 | -43.3907 | 2026-09-07 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 5bea3f81-4158-3d95-8b92-3b002c86b6a7 | -9.4777 | -40.2867 | 2026-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 140.5 |
| 15c924c7-2b7d-33af-9e86-355708229379 | -3.1462 | -60.6506 | 2026-09-07 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 1ea43f9c-283f-33ec-b9a7-a261e41635a5 | -6.6699 | -59.9251 | 2026-09-07 00:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 49.4 |
| 4468e0be-7a6b-34c2-9755-1b571fb02f94 | -9.7519 | -43.4143 | 2026-09-07 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 069bc34a-ec18-3dba-a2ca-5ddec46b5e05 | -6.0004 | -57.6884 | 2026-09-07 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 109.9 |
| 566da9a7-4c3c-3208-a01f-9cf21e837d73 | -2.6202 | -46.7822 | 2026-09-07 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 115.5 |
| 0e065f4f-87bb-3753-a64e-d956b5aa4f53 | -4.1102 | -49.0675 | 2026-09-07 00:50:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| a23f0a5e-596c-3afc-b666-3a85633da143 | -9.7328 | -43.4168 | 2026-09-07 00:50:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 210.8 |
| b210a330-2617-3175-be9c-a181785b805d | -12.0379 | -64.0327 | 2026-09-07 00:50:00 | GOES-19 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 091faa03-fe3c-3b8a-b4b2-51588aa8f659 | -6.0002 | -57.7079 | 2026-09-07 00:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 601d8fd5-9f58-3ac0-9e73-e09601c7f890 | -9.4972 | -40.259 | 2026-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 130.4 |
| d40b6f4e-89bf-32ca-ba9f-b1c2f657003e | -2.8839 | -50.4428 | 2026-09-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 208.7 |
| 342e71d5-474d-3f10-8e34-a2e3e391efaa | -2.6388 | -46.7597 | 2026-09-07 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 121.0 |
| 419488d8-641f-3e07-8090-7c33a717a657 | -9.4781 | -40.2618 | 2026-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 78.8 |
| 5918ff06-391e-3245-bf70-894ac0988a10 | -2.8655 | -50.4434 | 2026-09-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 88.7 |
| 15c8cabd-bb94-3838-82c8-7dadab2d49f6 | -3.1461 | -60.6696 | 2026-09-07 00:50:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 93.6 |
| 9baaa83e-79b5-39e7-8f4e-bcc0732d4ae5 | -6.6514 | -59.945 | 2026-09-07 00:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 4babc162-5a1a-314a-86b7-a2f31993e741 | -13.2477 | -61.7342 | 2026-09-07 00:50:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 91.1 |
| 095905ac-772f-3490-b2c5-c0b485a16f6a | -2.9645 | -48.7036 | 2026-09-07 00:50:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 79.9 |
| 20c4f00b-c3c7-317c-98b2-b64ec45e1854 | -9.4968 | -40.2839 | 2026-09-07 00:50:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 300.4 |
| a2cefc1d-caac-3d98-915e-6a110276565b | -2.8839 | -50.4638 | 2026-09-07 00:50:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 85.0 |
| ff379c78-ea4d-3c58-8587-ee640607169c | -2.6203 | -46.7602 | 2026-09-07 00:50:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 07700095-4e55-3f4e-b4fb-0f35a8526bc0 | -2.8839 | -50.4428 | 2026-09-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 135.9 |
| fe94bfad-8a71-3564-8ac0-c0084fa9b4f4 | -5.9818 | -57.7087 | 2026-09-07 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.7 |
| 09364388-f95b-3f7f-b455-1c2c0a1df6bf | -9.4972 | -40.259 | 2026-09-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 113.7 |
| cb04cfa8-e742-3e7a-afc4-a25f14102d3f | -11.0323 | -44.3396 | 2026-09-07 01:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 77.0 |
| 01124029-be89-3567-8815-56be20f1af02 | -2.6202 | -46.7822 | 2026-09-07 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 20047cd7-3ce5-34bd-85d5-136458e8d754 | -9.7519 | -43.4143 | 2026-09-07 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| a5910255-8c78-3ce4-93b8-66c1df957848 | -9.4968 | -40.2839 | 2026-09-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 353.0 |
| 9b6c24a4-8957-3529-9756-3206a0575046 | -7.0603 | -56.4827 | 2026-09-07 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 756e9a25-1784-37c9-86e2-57289c2f2e52 | -9.516 | -40.2812 | 2026-09-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 96.8 |
| 8cc55033-1276-3ac5-82a5-c42aab1f16a8 | -9.4777 | -40.2867 | 2026-09-07 01:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 177.4 |
| 60eea094-ddad-32e6-9a95-b09987b01fd6 | -2.9645 | -48.7036 | 2026-09-07 01:00:00 | GOES-19 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 82.6 |
| 8bf8a87e-f621-3282-84b1-5b24d6a53dd1 | -2.8839 | -50.4638 | 2026-09-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 65.2 |
| a9ca4dd1-986a-32b2-941d-63dcc56a2113 | -5.9819 | -57.6892 | 2026-09-07 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 70.9 |
| e873ae08-ebff-3836-bbeb-e53adedd1d0c | -4.1102 | -49.0675 | 2026-09-07 01:00:00 | GOES-19 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 22a06d50-1130-3b13-add6-a97de1f43e2d | -6.6514 | -59.945 | 2026-09-07 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 61728ed7-8e48-3b0b-aa52-b632490e3472 | -13.2477 | -61.7342 | 2026-09-07 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 805604b2-c052-378a-9de9-61534d74c0d4 | -3.1279 | -60.6509 | 2026-09-07 01:00:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 6311884a-2df0-3bfb-ab36-4bc5aeff3efc | -6.6513 | -59.9642 | 2026-09-07 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| ccaea49c-bdb4-377d-ac49-54185907229e | -13.2287 | -61.7355 | 2026-09-07 01:00:00 | GOES-19 | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 73.7 |
| c6b6cfa5-007e-3c77-94a2-182cdc2263a1 | -3.6215 | -60.566 | 2026-09-07 01:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b5563f1e-357a-3816-acf7-6f4970050474 | -3.1462 | -60.6506 | 2026-09-07 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 0d1bfd19-c03f-3fb1-97e3-f513427d23ed | -3.1461 | -60.6696 | 2026-09-07 01:00:00 | GOES-19 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 78.0 |
| 236f561b-f67c-304a-8906-a21e2d98152a | -2.8655 | -50.4434 | 2026-09-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 101.2 |
| 07b5eb5c-638f-3053-8594-963a96b5c3a1 | -9.7332 | -43.3932 | 2026-09-07 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 117.1 |
| 55860df6-5576-30c3-bbf9-8c060dc22b3c | -7.0605 | -56.4629 | 2026-09-07 01:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 61.2 |
| c56c9b42-659d-3ca0-8db0-875767403654 | -2.8654 | -50.4643 | 2026-09-07 01:00:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 2cbd0b58-21cc-335c-a2b2-a1cc8112968b | -6.0002 | -57.7079 | 2026-09-07 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.0 |
| 8e3af2ca-9b80-35d6-9c86-c3c09fb0c73a | -6.0004 | -57.6884 | 2026-09-07 01:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 90.7 |
| a749fa65-8a42-3a96-812a-9f8c883ce814 | -8.5321 | -63.8792 | 2026-09-07 01:00:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 52.3 |
| c42cf0cf-5255-306a-97c6-5886354f4a51 | -9.7328 | -43.4168 | 2026-09-07 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 191.4 |
| 4c5a9601-3981-333e-aace-0d4a1ae58b32 | -2.6388 | -46.7597 | 2026-09-07 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 108.2 |
| a69c25b0-ee4b-3a49-b62c-010cde15254a | -9.7522 | -43.3907 | 2026-09-07 01:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 83.7 |
| 803fd334-7ea0-3fc7-a4cf-f65a9fe45b65 | -2.6387 | -46.7817 | 2026-09-07 01:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 168.0 |
| 66a44342-8ef7-3025-b2bf-441f13da5dbd | -6.6698 | -59.9443 | 2026-09-07 01:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 57.6 |
| e741dc1f-a9c3-36a2-8bda-0bdfae36ee40 | -20.59459 | -58.0004 | 2026-09-07 01:00:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.5 |
| 43b6197b-f499-3356-9006-b24f4f31dfb7 | -13.24027 | -61.74512 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 25.5 |
| 547c721a-1f0f-337b-a19d-984e437862bb | -13.22745 | -61.7738 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 93690ebb-1863-376b-acff-b4f0cfbe0ae5 | -13.24802 | -61.73378 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 19.5 |
| e5e42cec-49a0-3543-b00c-335a7e6e577a | -13.23239 | -61.74266 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 26.4 |
| 965903a4-1c99-3ffe-8403-530adbc21e99 | -13.23665 | -61.77236 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 2c6deaf9-8d69-36c1-a50e-e4f5af6428e6 | -13.26175 | -61.14011 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 28a6b4d7-fa90-3fb8-b2b1-5644a9d6357e | -13.21048 | -61.78654 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 5f2363a5-a6a2-31c8-87c3-fc96de772167 | -13.33842 | -61.09999 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 8e0397e0-4306-3bc5-8d0b-909bf1c0360e | -13.21397 | -61.74554 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 14.5 |
| c8eb5032-f2fc-3306-896e-7be5340783e9 | -13.22175 | -61.73418 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 9.4 |
| ddf38a15-d58f-3de5-b160-a50c22fc328d | -13.23097 | -61.73274 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 24.4 |
| 297a1992-bde5-3c48-892a-8e981758655a | -13.22318 | -61.7441 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 19.2 |
| c8c7d5e7-83ee-3d85-8b84-72322c379058 | -13.23881 | -61.73521 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 45.2 |
| c9b5a22e-0331-3180-8189-d280ecacb3e8 | -13.24319 | -61.7649 | 2026-09-07 01:02:00 | TERRA_M-M | CEREJEIRAS | RONDÔNIA | Brasil | 1100056 | 11 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 53088b90-9fd8-360b-8114-5b7786c0fa67 | -6.05989 | -57.807 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 35.3 |
| ddd56ff7-976b-3b90-92e9-a92062461e34 | -7.61307 | -57.61564 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| a2644275-6fe2-3d81-91cb-88aa7edd88c8 | -3.37378 | -59.40312 | 2026-09-07 01:05:00 | TERRA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| 9ac0bd5e-729e-30e6-847e-464cd2476b9f | -12.03349 | -64.03238 | 2026-09-07 01:05:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 7d150bd6-13b4-3d79-bae5-f933202d96fd | -6.00344 | -57.71797 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.5 |
| c751e5dd-0ea7-3e06-a09b-6a67a616ccdc | -3.83421 | -60.76749 | 2026-09-07 01:05:00 | TERRA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 26.5 |
| fddf03fd-c096-3b2f-bdea-66a87a14d5a0 | -5.98952 | -57.72025 | 2026-09-07 01:05:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 27af70f4-1d03-3c06-9916-f8dbfdd55c8e | -4.2932 | -59.95916 | 2026-09-07 01:05:00 | TERRA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 1ccc5167-570b-3694-92e4-6c6652c9202e | -3.38656 | -61.34075 | 2026-09-07 01:05:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 75f87db4-98a7-3f60-a23c-1abac1e9c805 | -3.3846 | -61.32689 | 2026-09-07 01:05:00 | TERRA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ff68b30c-b5bd-350a-a59c-ee1a4732ed50 | -3.13738 | -60.64501 | 2026-09-07 01:05:00 | TERRA_M-M | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d8f70adc-9035-313b-af27-85517b5daee5 | -12.03472 | -64.04133 | 2026-09-07 01:05:00 | TERRA_M-M | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 85eaafac-4783-36e0-abcd-0f639692d963 | -5.14984 | -55.95733 | 2026-09-07 01:05:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| 78d328f7-0da1-3fa3-987e-aac78e856ba2 | -3.76938 | -61.74823 | 2026-09-07 01:05:00 | TERRA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 11.8 |


[Clique aqui para ver as próximas entradas](README4.md)
