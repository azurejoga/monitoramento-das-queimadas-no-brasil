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

## Dados Diários - Página 128

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ed738a92-8e55-3577-9e25-e3fb7fe73b93 | -6.11913 | -55.81128 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 68dbe4c8-552a-3398-8f70-cc83b0e41c4d | -5.8522 | -57.7521 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 8dd3a846-d173-37d5-918b-0a7fedafb839 | -6.7772 | -59.4424 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c0075e07-7fe8-310a-8ed2-7c9ab5761b97 | -8.01531 | -48.01289 | 2026-08-28 17:28:00 | NPP-375 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| bbf26522-5fcc-30bc-8c59-449a1b8d069f | -6.94403 | -58.94392 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 8473c3b3-6a8f-3916-b083-be6c1615a88a | -4.30867 | -59.46759 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 3decc853-67e1-36b1-851f-bee1ecd57252 | -9.23496 | -51.53136 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a303283a-134e-3d74-b11e-e643b0fc59a4 | -6.76656 | -59.46817 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 2e38e81d-7b0e-3750-8e66-26261173d338 | -8.59087 | -55.27881 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 100463b3-5353-3d45-adae-72448be7e000 | -2.71826 | -47.03786 | 2026-08-28 17:28:00 | NPP-375 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| 5e30379d-8422-3e5b-b837-5dfda1f7d5c8 | -9.70126 | -65.07574 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3452836e-fead-3140-8304-b8577923a270 | -10.15197 | -64.44069 | 2026-08-28 17:28:00 | NPP-375 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 82ad6f35-b50e-3f21-98bc-07d0371def4b | -10.72036 | -69.65591 | 2026-08-28 17:28:00 | NPP-375 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e62e27a2-c05b-3cfc-bb50-511f68c2b87c | -6.80955 | -59.44158 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 01f8ea83-904e-36e7-b392-e91db7135be3 | -6.17945 | -55.46135 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 901d8f21-2742-34c8-a4cc-95e2506f8beb | -6.04273 | -57.79805 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| fb4508a3-c753-359d-ae94-0c879b657a4f | -6.73338 | -55.45509 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 19.4 |
| 82119c7c-0720-310b-abc3-a9c3e1cf6757 | -6.64967 | -55.87985 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9312707f-4df7-374b-90f3-c81c9f8fe9ea | -9.21237 | -65.79502 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d668ba50-5fe1-3557-b30e-3f0cf879b3ca | -9.11561 | -60.30386 | 2026-08-28 17:28:00 | NPP-375 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c30e0f4d-1720-31d9-891b-05411fa2ab9c | -4.74396 | -55.94464 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7ac8a30a-ffa9-39ce-82c6-b4ae57100748 | -4.38679 | -55.45972 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7c307b68-bbfb-34c3-b4dd-951da8936b6e | -4.30691 | -59.47939 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7abeba0-10c3-3a01-b5e5-220de464f93f | -6.81073 | -59.44947 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 359584fe-e81e-3d5b-aebb-73228353d8ed | -3.62826 | -56.81478 | 2026-08-28 17:28:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 8f0c2f89-d738-300b-b0f2-ee9429c7b43b | -4.46364 | -55.66775 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 0ba6e5f4-c532-3459-a0ee-4f27d88b2d28 | -4.91228 | -56.2654 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88432d6f-efe2-3e78-ae12-fd2345cce74f | -6.77662 | -59.43847 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ba895d60-fd75-35cf-94eb-9fa210ee2b3f | -7.09594 | -55.47875 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 28.1 |
| 0a9701ed-2b57-3043-b3b0-503f72b161c5 | -3.67664 | -57.00315 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b15149f2-6deb-3a44-a749-7727e9091e94 | -9.25747 | -57.08458 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 7d3be550-ef0e-3515-8bdd-720da446fbcf | -7.60041 | -61.34286 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0f6255e6-74b5-3017-bf81-f23bc8b8079c | -9.41836 | -50.43615 | 2026-08-28 17:28:00 | NPP-375 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 89.9 |
| ed246b66-6f94-3890-9727-43e8ded52ace | -9.50434 | -56.91153 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 10b41a4d-15e1-390d-b00f-1c84bdb9192b | -7.75714 | -61.10201 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 14268f8b-85b9-38e1-9da6-32691a48a9ec | -6.09893 | -56.09175 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 25.9 |
| 1400b0fb-2c6b-3f03-9fba-2d6e5e92c1a4 | -6.15894 | -57.79344 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| 8459cb6e-fbc1-3ccd-bcdc-3688e8ab351a | -10.75382 | -54.03724 | 2026-08-28 17:28:00 | NPP-375 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 105.7 |
| d999b431-0c7c-3fa4-9824-e917b278033f | -6.96515 | -55.64337 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 09361cdd-194c-3c03-86a2-86ff6eaa0ebd | -9.97037 | -66.79582 | 2026-08-28 17:28:00 | NPP-375 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 53933bbe-67ef-396a-b905-e8076857406c | -9.31154 | -56.79412 | 2026-08-28 17:28:00 | NPP-375 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 140f5b06-3cc0-321e-b17a-028f399fbdbd | -7.52748 | -61.36103 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 5250f2e0-4d1b-30d8-8f47-7cb17177181b | -6.16 | -57.80047 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.2 |
| cd8ceea8-3218-36d4-9ee3-279b7b28cdd6 | -8.09488 | -51.67331 | 2026-08-28 17:28:00 | NPP-375 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 27f126c2-7fca-3614-a27e-ed06806fe83d | -6.7333 | -59.65218 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c82a182f-1688-39e5-ae2f-1cc59c224e73 | -8.12075 | -48.99516 | 2026-08-28 17:28:00 | NPP-375 | JUARINA | TOCANTINS | Brasil | 1711803 | 17 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 3f75194f-57c7-32bc-880f-6639a0a89605 | -7.92154 | -61.3625 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 44a7a6ff-a5ba-33cd-a38a-476200c20b3a | -8.79786 | -50.04087 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 90a3b392-3d66-3e48-9bcf-99d95dcbf212 | -7.57562 | -61.31046 | 2026-08-28 17:28:00 | NPP-375 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 81994b3b-51bc-3fba-a518-033aa97cd248 | -9.43424 | -51.57621 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 2e4741c2-b548-37ad-8f48-197b9df27858 | -8.79086 | -62.48224 | 2026-08-28 17:28:00 | NPP-375 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ee4e1a09-5f0c-31e5-99d5-d70ecee0678a | -7.11586 | -43.17466 | 2026-08-28 17:28:00 | NPP-375 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 941dcd6a-4ac3-3e81-828c-da81ddf7886a | -8.57878 | -54.82636 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 1f763bc1-4548-3983-84a6-79f32edad2ab | -6.96908 | -55.64644 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 1dcb0313-bc7e-39a4-bc75-7c0778761d8e | -6.83159 | -59.73697 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8e2aadf1-69eb-3b11-907b-d76d319bd038 | -5.21473 | -49.17785 | 2026-08-28 17:28:00 | NPP-375 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 13.6 |
| bba9bff8-7655-3fe0-aebd-14577cc6a447 | -7.98754 | -45.5042 | 2026-08-28 17:28:00 | NPP-375 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9d365353-6df0-3e03-837d-226758bec35e | -4.45579 | -55.39134 | 2026-08-28 17:28:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a02edaba-890f-3cc6-9922-7a3aaed47e41 | -5.76714 | -57.56511 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4d341874-271c-35f2-9c6b-d35d192ae67c | -7.49787 | -55.28119 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| e99d483f-c062-3c77-97bb-32a55a326738 | -7.73503 | -64.67525 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 34.7 |
| ec128994-6a9e-3ae8-a879-c9176d3e14bc | -6.95939 | -59.04675 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 9769c0dc-19af-3e2a-b3a5-99e34beadb48 | -6.32631 | -54.74549 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 03670746-ef7d-3728-8a26-6eb6562dee6a | -6.81897 | -59.45631 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.3 |
| d133fec8-a827-3d85-bf49-db170714fc4c | -8.23794 | -54.96839 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| bfa54c6e-a60a-3376-a6be-b23ec2aa222c | -6.65121 | -58.50124 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c13e31fd-da74-3cd9-b45b-3f67866c1f97 | -9.70333 | -65.09188 | 2026-08-28 17:28:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 513c2b64-81eb-3d37-befd-b139a569ae06 | -7.7859 | -61.10791 | 2026-08-28 17:28:00 | NPP-375 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| aa339d47-1bd7-38cb-a09a-3134ba7937df | -8.1537 | -64.00294 | 2026-08-28 17:28:00 | NPP-375 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 12.9 |
| a2df47b1-030c-3126-a246-93a7f3832998 | -6.93249 | -42.71624 | 2026-08-28 17:28:00 | NPP-375 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 2c63b90a-9391-34c1-a9ae-c139fe679223 | -6.5726 | -45.32701 | 2026-08-28 17:28:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7f160a81-dcd6-3bad-908c-848d9e217400 | -4.90947 | -56.26947 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3103a931-0836-392d-8cfd-109f11204cc5 | -9.45002 | -51.57343 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8a8333f5-03e4-36d7-b48f-b6f94c501800 | -8.59456 | -54.77082 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 77ff45c2-08f0-3c76-84c6-692ff44d53fe | -7.36979 | -55.50813 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 66d2bfcc-23f3-3668-b199-c120d654f1a7 | -4.92701 | -55.77454 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 14.4 |
| 466cfaef-61a8-3b24-ae8a-3e756a072753 | -6.80424 | -59.60105 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| c815e295-5e46-3e85-acef-4e3c2a06c6f4 | -9.88122 | -60.25846 | 2026-08-28 17:28:00 | NPP-375 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 99f2757e-66b8-3713-a84f-9452f2091243 | -6.97752 | -55.63411 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 1a363cb2-3a52-3e50-aa56-8a0cc8b36eec | -6.53261 | -55.24375 | 2026-08-28 17:28:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bec4f2b4-1423-368f-b324-c4297e90753f | -8.45396 | -70.41791 | 2026-08-28 17:28:00 | NPP-375 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 5e3697b7-249f-365d-9391-f0a7604a8af5 | -9.23409 | -51.52617 | 2026-08-28 17:28:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| dac45ff7-a878-36af-885b-9303e7560513 | -5.47746 | -45.12363 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 3fd839ab-5818-384f-a66a-9e9fd3c561e3 | -6.60277 | -55.44613 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 2a3b3983-04a9-36e0-af0c-dea6aede17ed | -4.30346 | -59.47991 | 2026-08-28 17:28:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cd6ceced-26c7-3a5f-84a3-8e0820a653ba | -6.59256 | -55.42538 | 2026-08-28 17:28:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| a10043d7-15d1-3d89-9bb4-70101af5a139 | -7.36875 | -55.16703 | 2026-08-28 17:28:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e28c26d7-38e7-3826-9e96-4ebe7aeac1a9 | -5.3432 | -45.15547 | 2026-08-28 17:28:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| a1e00f28-b0eb-3bd2-bb3a-2651ae1cb109 | -6.6523 | -58.50853 | 2026-08-28 17:28:00 | NPP-375 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1b320215-011f-3b13-9075-3e7800ecb19e | -8.63242 | -66.53928 | 2026-08-28 17:28:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 89e410e3-8230-3320-b5ec-a869b60ea9bc | -3.22265 | -48.61122 | 2026-08-28 17:28:00 | NPP-375 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| a5a0451f-be41-38f7-9b2a-62198adac573 | -4.8854 | -56.26951 | 2026-08-28 17:28:00 | NPP-375 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| c948276c-dd48-3bf3-9187-5c819e9f5888 | -7.27371 | -49.8645 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 8dd38886-dfc1-324f-9834-a4e71a3887f2 | -7.27822 | -49.86331 | 2026-08-28 17:28:00 | NPP-375 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 39977ae0-2476-381e-988b-fc86a073cc97 | -4.15811 | -60.69815 | 2026-08-28 17:28:00 | NPP-375 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 29.6 |
| 485477a5-d89f-3cdc-93eb-f8ddd51869a6 | -8.04447 | -45.85814 | 2026-08-28 17:28:00 | NPP-375 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| e11f0588-32e8-365d-b869-66622fa2a868 | -6.99094 | -59.3067 | 2026-08-28 17:28:00 | NPP-375 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 6affdb3c-526b-3636-b37c-9438c0c93ca3 | -8.43612 | -70.70319 | 2026-08-28 17:28:00 | NPP-375 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 26.5 |
| bbdcf065-7ba0-3401-bbbe-6a5a80edf1f7 | -8.80037 | -50.49572 | 2026-08-28 17:28:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5655e5e0-f32e-36c4-89b8-52f7d8c1e816 | -6.14427 | -57.84664 | 2026-08-28 17:28:00 | NPP-375 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |


[Clique aqui para ver as próximas entradas](README129.md)
