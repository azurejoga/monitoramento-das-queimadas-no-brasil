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
| a242a234-9d63-38ed-adfe-0c1a46f8fa4a | 4.33095 | -60.76855 | 2026-09-04 05:23:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44084823-971c-378e-bc2e-7dee6394b01c | -6.68696 | -59.98601 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| ab6f0afb-6905-378c-b841-c9e1cbe68002 | -7.79677 | -62.34422 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b73e8b6-aea6-34ea-ab18-61e469dcb3d5 | -3.14614 | -61.18341 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 860248c6-4fc2-30ed-8df3-dc21ae2a43ee | -8.44354 | -54.68385 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c9fc016-531e-3495-8d67-c085be9dcd50 | -8.42917 | -54.72149 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56872418-58a3-34bb-8623-81cede81fe28 | -3.1953 | -61.19827 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b5914f7-f59b-3de0-81bb-875068c39ec5 | -6.68457 | -59.93553 | 2026-09-04 05:23:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| db15fdd5-87df-3190-be6a-42e326e9cbd9 | 0.97385 | -59.38532 | 2026-09-04 05:23:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 52a71fc6-55b0-3b31-8773-75db0cd9e770 | -4.37057 | -47.77542 | 2026-09-04 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| ce111c1c-4003-37bb-8378-ec742b2fc32b | -7.59467 | -61.18839 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 557236aa-a592-3d09-86fe-1a14ae95bb96 | -9.39948 | -62.08519 | 2026-09-04 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f93e724-dd23-376d-8e4c-3eb8385dad24 | -6.67637 | -59.96649 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 7a2baadf-114c-37f8-b52f-41a6c6d9f4dc | -3.01934 | -61.49271 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7e3c9786-3bd3-3a1f-93d4-2ea0c8911ef4 | -7.2474 | -59.52205 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbc392a2-e4f2-3b96-8d38-eb8dcf4561d6 | -6.6763 | -59.945 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1edf9073-6160-3ce5-9400-5d00bc81cdce | -10.83975 | -51.78754 | 2026-09-04 05:23:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0bd22e0a-277d-3cc6-84d2-9be625040c89 | -8.27481 | -64.05976 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6de5c330-71ec-35b5-aec8-b355b2e0c58b | -6.03358 | -60.16594 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7801f2fd-ac36-3832-84a1-82e23e62b32c | -8.57034 | -63.19395 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e2e8483f-0942-37e3-bc31-5e85a89a1442 | -3.1629 | -61.12082 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ec08b87e-797a-3167-aba8-8315887b7db9 | -8.00296 | -61.40622 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d67d152f-1e8e-3f9c-8ac0-48b304e5c706 | -8.56751 | -63.18964 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e9ec7c31-46e1-3fe9-80f1-c01a70ad72d9 | -7.26105 | -61.10353 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 756e1f94-acb2-3641-99cd-a522e881796c | -3.09856 | -61.18639 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84b2df49-2cb7-34af-8fe0-98437672facb | -7.55868 | -61.35333 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| c909dea2-7784-302e-a489-71a80255d324 | -4.36979 | -47.78118 | 2026-09-04 05:23:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d24bf479-658e-3338-a41a-3b06f9ea3c89 | -3.47572 | -58.43272 | 2026-09-04 05:23:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2b859120-54a0-3adc-9928-5838e2484cf2 | -1.24865 | -54.5313 | 2026-09-04 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f5cd1efa-58a9-3c9f-8c26-2911f8cc8af2 | -7.01614 | -62.98618 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d19aa96a-be6f-35eb-ade5-964428be91d6 | -3.67626 | -53.75264 | 2026-09-04 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| cbcafc4f-ee80-3bc8-8816-44fc62973a77 | -8.91964 | -62.36648 | 2026-09-04 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a964d93-f582-38ef-adea-a96c815357a1 | -8.10983 | -54.78649 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 7414d5a7-101f-38b0-a97c-8622368c62e3 | -7.3298 | -59.58212 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 545c8f5e-c25f-33df-af89-67ebfb3f6fc2 | -7.08041 | -56.5117 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4e454633-6464-3ca1-bdc2-8c35df9f7047 | -7.56826 | -61.20556 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3be2d2bf-700f-3c5d-bcac-202a045f9040 | -8.44255 | -54.68655 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f28a644-c37e-39e6-b09d-e0087b721908 | -6.78363 | -58.95292 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 14213d4c-913c-369e-9a13-b83b7dc41e0b | -6.67746 | -59.9595 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 9c8dab95-5b0e-3b11-beab-202b66e609ca | -8.10665 | -54.78047 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 4e211140-2ca0-35f0-bd2a-ca9c79b1c700 | -8.42475 | -54.72083 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 60b787b2-28c4-30e2-aef2-8e00ce7191df | -8.20473 | -62.79998 | 2026-09-04 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a536f3ec-f1f6-3bd0-9bf0-e3fec891aa0c | -6.68248 | -59.97101 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 245821cd-0ab0-3270-873b-0a1435accf98 | -7.59047 | -57.68848 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5582392f-c00d-39c7-a8e1-c7c7575511a4 | -3.05945 | -61.17307 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fbcfedc6-6288-34f1-8729-ecf5a0865f04 | -7.56254 | -61.35037 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 6718f499-e17d-3064-b6c4-19d3b0fb4301 | -10.66172 | -50.39069 | 2026-09-04 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 815a4995-fc54-39c7-a5b3-e4446f22fb48 | -3.07952 | -61.08928 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 90f7f3cb-c23b-3e0d-b78d-8d80f38cf471 | -7.42476 | -61.729 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07e07a2e-442e-392b-871c-08b1057ea90e | -8.48853 | -54.64792 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c7bcc534-3673-36ee-8c2f-ea7246d2dbde | -6.74763 | -59.43825 | 2026-09-04 05:23:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 111ac49b-9eb9-39d2-84c6-7b4fcb09f05d | -6.67916 | -59.9705 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a145b64b-d6c7-3968-a95f-e0d6994fda65 | -7.27914 | -64.55142 | 2026-09-04 05:23:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2f68597b-66db-3da4-83fc-98085ed81769 | -10.49958 | -51.3317 | 2026-09-04 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 608f8359-2451-3c30-81de-1f9ac3a69188 | -7.01553 | -62.98997 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 786ebf0a-f624-37c4-8792-29399cc69019 | -7.26436 | -61.10405 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9a65f20b-a804-3979-8471-cb04a3e35422 | -3.07338 | -61.0847 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9ed282ba-c036-3e7d-8178-d59876e975c6 | -6.94435 | -56.45961 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 983db1ea-e350-3829-a0d0-197aa8fa3c53 | -3.62857 | -54.59876 | 2026-09-04 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 96480ce5-9a8e-372c-9fb0-1c5167a1d3b9 | -3.14266 | -60.64437 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ffe043b6-6586-32b3-8a76-8673bbd2b05c | 2.45043 | -60.76015 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 843e13aa-1143-345f-932a-b16668e4fe25 | 3.96774 | -59.83441 | 2026-09-04 05:23:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 315ae6ee-4bba-3747-98d2-c5fc03f0c9f7 | -7.5688 | -61.2021 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25f968c1-c5ed-3864-b89f-2b7908137988 | -3.628 | -54.60265 | 2026-09-04 05:23:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f9ca1a63-9014-3556-8dcc-8addeb11d79a | -7.55478 | -61.33496 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e77279b6-a97f-30a0-a6f5-1768d0d60eaf | -8.69659 | -62.93172 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f8cf8342-c637-3350-863c-600fe3a423f2 | -8.11543 | -54.7786 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7ef9492a-ba8e-35b0-8e66-25e35a5956b0 | -8.56348 | -63.19284 | 2026-09-04 05:23:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 70c88800-dd88-34e6-bc0a-b31151c9753d | -6.68241 | -59.94952 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c81d3ca9-bdce-32d7-a5d7-49c1c8ec626d | -8.11541 | -54.78178 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f5393400-662f-362d-8c56-0b66337b3a3d | -7.27266 | -61.11599 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d606d1f-223f-3c5d-9952-a3b07e95beea | -7.73015 | -61.64802 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 63524802-3560-3437-a8ff-270847eb3e14 | -7.08739 | -56.51769 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dffb32c0-45b8-3047-a4ef-727aa94b8ff5 | -3.02329 | -61.48962 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f18b6109-d33e-3528-a244-d9d709d4c559 | -6.99422 | -62.99045 | 2026-09-04 05:23:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 18fa8daf-21b3-32e6-868d-b452c2e84ed6 | -6.68295 | -59.94602 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 07b514b5-0342-30d1-a127-a6e70246ac68 | -6.68967 | -59.96854 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 9a180fae-3681-3e07-bf79-9d5e297b49de | -7.58685 | -57.68792 | 2026-09-04 05:23:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 0acd1678-1486-3f3e-8077-d69ecfaa8e10 | -7.78962 | -66.95813 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9110d7d6-11c3-3af2-a50c-b780c14b7631 | -3.02272 | -61.49324 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58b70dfa-a407-32b1-baa1-c2932d95858b | -6.68736 | -59.93954 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a13949f-cdaa-307a-8949-190312ea1fc2 | -3.0171 | -61.48497 | 2026-09-04 05:23:00 | NOAA-21 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 70fc633f-c941-3dd3-8f20-3dfd49a27214 | -8.4429 | -54.68837 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbee8b49-aeb8-39a1-bc01-094a4eca9f92 | -6.69246 | -59.97255 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 537dee3a-0837-30db-9aee-ae0ba68cb98a | -3.10354 | -60.19991 | 2026-09-04 05:23:00 | NOAA-21 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d6bb7f60-29d3-32f5-b8e0-e582579c0e84 | -7.74509 | -67.06325 | 2026-09-04 05:23:00 | NOAA-21 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9c7a9917-0325-3c93-b760-b63c52181129 | -8.07465 | -55.33071 | 2026-09-04 05:23:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d0b860ee-25eb-3eca-a99e-130da2cd7101 | 2.45101 | -60.76389 | 2026-09-04 05:23:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7cbe8818-8161-38df-b486-2d4d0e90e565 | -7.0797 | -56.51645 | 2026-09-04 05:23:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3d6d4b99-8752-36a2-8c0b-babe92bd3f9b | -3.43176 | -58.03243 | 2026-09-04 05:23:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 667b24fc-ba61-34e8-82af-8d09ea4090f1 | -3.2908 | -57.87781 | 2026-09-04 05:23:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3232913f-a14e-364b-b051-ad25054dfa4d | -8.49681 | -54.65369 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 75096e0a-ed8f-3757-9c01-06292248169a | -1.24464 | -54.53062 | 2026-09-04 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c047ade9-b354-3087-b001-1ebd03731d0e | -6.67467 | -59.95549 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2eaeb651-379c-3993-bafb-675f07c804cf | -6.68805 | -59.97903 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 924ca5c9-64e2-35dd-9774-db6d85bcb2fc | -7.55369 | -61.34191 | 2026-09-04 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 7133a5c2-989f-3b20-a6e3-07de5981b276 | -3.20084 | -61.14116 | 2026-09-04 05:23:00 | NOAA-21 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 10dade92-08f2-3009-a5f7-58a06aa4e886 | -8.50125 | -54.65437 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 49b1d06e-0eb3-324b-b3ec-1604f20037ec | -8.62702 | -54.84792 | 2026-09-04 05:23:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02a8ee3d-c155-3c6d-aabe-83eb15ee1d57 | -6.67576 | -59.9485 | 2026-09-04 05:23:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README23.md)
