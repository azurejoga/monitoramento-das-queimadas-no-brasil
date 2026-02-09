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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25bfcc49-b15e-3c1b-a6cb-79a7001d152b | -30.6934 | -54.59937 | 2026-02-09 05:12:00 | NOAA-21 | LAVRAS DO SUL | RIO GRANDE DO SUL | Brasil | 4311502 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| 082a8b16-4b20-30d1-8b67-b3f641643afc | -28.4855 | -55.54424 | 2026-02-09 05:12:00 | NOAA-21 | SANTO ANTÔNIO DAS MISSÕES | RIO GRANDE DO SUL | Brasil | 4317707 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| ea123aa2-01bb-324b-9c3f-d3f1c2e60f4a | -30.30256 | -50.92496 | 2026-02-09 05:12:00 | NOAA-21 | VIAMÃO | RIO GRANDE DO SUL | Brasil | 4323002 | 43 | 33 | nan | nan | nan | Pampa | 3.5 |
| 0ee3d414-2a94-36ad-b3ce-1cdad234faf9 | 4.32354 | -61.16375 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| af0ebcfc-70e7-3ef3-8a87-3821fc99dc57 | 4.42921 | -60.66502 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5e34e179-f71f-37fc-ba9b-4cafec417091 | 4.43425 | -60.6535 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0f52223e-0cbc-3cfa-b04d-ed81f14d62a6 | 4.32409 | -61.16731 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dfc2a2ab-3196-3a84-9071-2f44847e497e | 4.41796 | -60.7024 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86be4b4c-4ddd-378d-9e88-3be5c4d29d63 | 3.64791 | -60.77589 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 30d95ad8-93fe-3d45-bb7c-556269b27fd4 | 4.42129 | -60.70179 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 248968bf-d3a6-3960-bb29-97ed66e4ee2d | 4.42463 | -60.70126 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5bdcd079-3d5c-3cc2-a2c0-2c9507ad55c3 | 3.75312 | -59.85426 | 2026-02-09 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 17cceb6d-2686-32cd-9b0e-2a2486b1d199 | 4.32802 | -61.17032 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46ec81bd-144b-3709-865c-4232f04709da | 4.01869 | -59.6318 | 2026-02-09 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ac78fd3-c35f-3786-9b1b-611a780e3cb9 | 4.32747 | -61.16676 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b81a5226-1a32-3a96-ae18-de82b1e327bf | 4.42408 | -60.69775 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f07d8392-5846-38fe-9043-be1f796ad31b | 4.19319 | -60.41207 | 2026-02-09 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 95fadbf7-4960-37c4-b4fe-389f570e29b5 | 4.01814 | -59.62835 | 2026-02-09 05:31:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fcb8d374-553f-365b-9813-884a190edc51 | 4.40129 | -60.7053 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 47d4b2af-9caf-3a71-88f3-bd9bac46e87b | 4.30884 | -61.166 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bab333d6-096c-3ab4-930b-6e29cc77c429 | 4.30828 | -61.16245 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f7f173a-97c4-3cbe-a2f4-1e6fc6b4d862 | 4.3049 | -61.16297 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ccf2ac0-0bdd-36f6-8c59-a1d260b475f0 | 4.45693 | -60.67445 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6db08d8d-73be-3bdd-9bb6-16681e0c17c7 | 4.42142 | -60.65906 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 98d576c1-922f-33aa-8e35-378b68db9f69 | 4.43582 | -60.6853 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1271a381-f878-3373-953e-2bc1c5f29588 | 4.42477 | -60.65855 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2261ec67-0c12-34b5-85f6-55a196ea30b6 | 4.43637 | -60.68876 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| df00cf13-5e7d-33cb-b5ee-188b4b99b9b1 | 4.45748 | -60.67796 | 2026-02-09 05:31:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e5e4fcb7-19b4-3af5-824f-d812e1df756a | 1.3466 | -60.024 | 2026-02-09 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b275acc2-f98d-3a84-92e7-444a185df182 | 2.19497 | -61.90808 | 2026-02-09 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b17487fa-80b4-3d95-9ef0-b788234493f7 | 2.19213 | -61.91223 | 2026-02-09 05:33:00 | NPP-375D | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8ae2593-caf0-3014-b0b4-7d190f8490a0 | 1.34715 | -60.02747 | 2026-02-09 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0f738aaf-35ea-3c0c-993a-65fcaae0bbfb | 4.43311 | -60.65327 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4b91cc6e-f8eb-3da3-83fc-37b1cd739749 | 4.45778 | -60.67346 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c94dd090-5823-3393-acee-3ed923cba4fb | 4.4204 | -60.70434 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d4492aa1-03f1-3022-9b14-9e1feec093af | 2.19418 | -61.91342 | 2026-02-09 05:54:00 | NOAA-20 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6a629c88-aad2-3289-af8a-37d76277f9a8 | 4.42395 | -60.70018 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 92e7838e-26d9-3bbe-976e-b844a71c8828 | 3.75319 | -59.85653 | 2026-02-09 05:54:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6a63de19-578f-32c6-b29d-002cf894ac65 | 4.42131 | -60.65923 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55933591-0d6d-3df4-aed5-8643617b13ca | 4.32204 | -61.16515 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f453266f-9b5f-3262-832a-d0ba3528ed69 | 4.45299 | -60.67024 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e37769d-3b72-304d-acec-06074d3b88bb | 4.45234 | -60.66636 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c797f0c0-eae8-3899-ab6b-8558d5ca2447 | 4.42545 | -60.65848 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eae433a4-3b73-3023-a3c8-332b89525551 | 4.45841 | -60.67725 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| cc53366c-e99f-3da9-bb8c-fa4f64222380 | 4.32667 | -61.1682 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 92eb9029-537b-3a3d-a371-85d375e298b2 | 4.45903 | -60.68101 | 2026-02-09 05:54:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8b660ea2-21f0-3be7-a3d7-deca19e526ef | 4.42709 | -60.70194 | 2026-02-09 07:16:00 | AQUA_M-M | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d11dd1c3-4c1a-39af-b1da-926f5ebf2362 | -6.54574 | -49.85203 | 2026-02-09 12:31:00 | TERRA_M-T | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 576ffbb2-f083-3545-8cbf-c8e68dd19f99 | -19.95327 | -54.39446 | 2026-02-09 12:36:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 6.7 |
| dd629b89-7593-3939-b4df-a11940df527b | -19.95189 | -54.40478 | 2026-02-09 12:36:00 | TERRA_M-T | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 023de5d3-08d4-3dc2-8159-8d6ee0723cf8 | -27.40935 | -52.54829 | 2026-02-09 12:38:00 | TERRA_M-T | ERVAL GRANDE | RIO GRANDE DO SUL | Brasil | 4307203 | 43 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 88418311-d590-3eea-9a0c-316b0cff713a | -26.95471 | -53.27274 | 2026-02-09 12:38:00 | TERRA_M-T | CAIBI | SANTA CATARINA | Brasil | 4203105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| 3154319e-f80a-3afb-9aac-6464d1fdbd6f | -25.65001 | -53.2141 | 2026-02-09 12:38:00 | TERRA_M-T | BOA ESPERANÇA DO IGUAÇU | PARANÁ | Brasil | 4103024 | 41 | 33 | nan | nan | nan | Mata Atlântica | 8.4 |
| eabc9dc8-01c5-32d5-ae93-c8d14bfeda7e | -26.95677 | -53.27959 | 2026-02-09 12:38:00 | TERRA_M-T | CAIBI | SANTA CATARINA | Brasil | 4203105 | 42 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 3697a918-7bd4-3502-a6e9-b31deca6711e | -29.23012 | -51.32804 | 2026-02-09 12:38:00 | TERRA_M-T | FARROUPILHA | RIO GRANDE DO SUL | Brasil | 4307906 | 43 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b2767d32-e444-34d4-a293-1815c1925983 | -27.61161 | -52.2403 | 2026-02-09 12:38:00 | TERRA_M-T | ERECHIM | RIO GRANDE DO SUL | Brasil | 4307005 | 43 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 7f9011ba-32de-39fb-a6de-749f9924d4dc | -28.85545 | -51.89857 | 2026-02-09 12:38:00 | TERRA_M-T | GUAPORÉ | RIO GRANDE DO SUL | Brasil | 4309407 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.9 |
| 985e2cf5-63c7-347b-8036-8e7b6689bcf8 | -21.67609 | -53.54642 | 2026-02-09 12:38:00 | TERRA_M-T | NOVA ANDRADINA | MATO GROSSO DO SUL | Brasil | 5006200 | 50 | 33 | nan | nan | nan | Cerrado | 7.6 |
| cb863be8-443c-346a-b10b-92de048c3336 | -29.71307 | -52.43939 | 2026-02-09 12:40:00 | TERRA_M-T | SANTA CRUZ DO SUL | RIO GRANDE DO SUL | Brasil | 4316808 | 43 | 33 | nan | nan | nan | Mata Atlântica | 12.8 |
| 6355df36-046e-3153-a705-07454978421b | 3.7123 | -60.8109 | 2026-02-09 14:40:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 70.2 |


