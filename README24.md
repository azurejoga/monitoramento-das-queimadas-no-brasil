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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 745afb28-d85e-33bd-9bad-bd8772b81a50 | -5.29167 | -43.21803 | 2024-10-28 03:40:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8a23270b-2d43-36c1-9178-9770a648abf5 | -3.07497 | -44.33521 | 2024-10-28 03:40:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fbd5af97-0677-3c28-88b5-25cd0fbbbc63 | -3.0693 | -44.33421 | 2024-10-28 03:40:00 | NPP-375D | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d6c2a28-d0ae-3b89-9244-42bb2c5628c8 | -4.65244 | -44.66809 | 2024-10-28 03:40:00 | NPP-375D | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e44d2c5-58e9-3c50-a3a4-02aaa8ebaea0 | -4.1728 | -44.10774 | 2024-10-28 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e5994e3c-3764-3cbf-8860-04827a71881f | -4.17218 | -44.11139 | 2024-10-28 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5836df9a-4be6-35f5-8e5d-b839e1c41e04 | -4.17156 | -44.115 | 2024-10-28 03:40:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6cef5f06-e2c2-3de2-99dc-2e8471fa0baa | -3.89098 | -44.17417 | 2024-10-28 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0eac95ba-0291-30d7-91a8-90d80eca41f8 | -3.88544 | -44.17315 | 2024-10-28 03:40:00 | NPP-375D | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efd565b5-8823-3c41-a635-2351ff7d97d6 | -4.98084 | -43.71159 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| df4fe405-f6f6-39c1-aa29-8c2ce9224cc7 | -4.98027 | -43.71484 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2c7e7109-e1f5-3a03-84fc-2143471479b1 | -4.97971 | -43.71808 | 2024-10-28 03:40:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 76c851b0-2b3f-3229-9d0a-731ef46b46ee | -4.74278 | -43.25539 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 57212ffc-362f-36aa-8073-b43a51006e20 | -4.73814 | -43.25159 | 2024-10-28 03:40:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4324fa1c-5bfe-342c-b20c-4b13a86d1767 | -3.8833 | -43.19279 | 2024-10-28 03:40:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0d3bcb60-cbab-3af7-a3e6-12afe36e723b | -3.8781 | -43.19196 | 2024-10-28 03:40:00 | NPP-375D | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 83633f8f-3059-3817-953c-e3d6964c65f8 | -3.66644 | -43.62756 | 2024-10-28 03:40:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fc3daeb4-9689-33c1-96b6-750de3e5a03d | -5.65588 | -43.41764 | 2024-10-28 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 034ca03a-0159-3167-96ab-ea4251eb79dd | -5.65641 | -43.41463 | 2024-10-28 03:40:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f268bf0d-94a7-3e32-83b1-deebab61a335 | -5.26511 | -43.99406 | 2024-10-28 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f330dce9-f1a5-3a8e-9cfa-cd6619bca0a6 | -5.26454 | -43.99737 | 2024-10-28 03:40:00 | NPP-375D | SENADOR ALEXANDRE COSTA | MARANHÃO | Brasil | 2111748 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4a218c9a-daeb-310a-a546-36a633187b6a | -5.06737 | -44.2207 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0f421a6c-3427-346b-ab29-3137e72df4a6 | -5.06253 | -44.21614 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc958a04-4b83-397c-b343-cf33f382f3d2 | -5.06193 | -44.21965 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ff519f70-3830-320b-96c4-41b90bea3707 | -5.0565 | -44.21858 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 0093b097-10be-3ee9-b8e9-69e4238bdd76 | -5.05591 | -44.22203 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| a59c6d47-58cc-34e8-ac69-5c63938cf358 | -5.05532 | -44.2255 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ed307f2a-ae89-3529-8538-9220f9d45c0a | -3.50508 | -45.80336 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 35fbaeb9-f4df-3549-9bb6-7457270715cd | -3.50377 | -45.79916 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 99940b7d-6cb7-3165-9d56-6841c7094c9a | -3.50293 | -45.80397 | 2024-10-28 03:40:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 9.6 |
| beed9dab-1ba7-3d14-ab35-31feccb37d29 | -3.45146 | -45.89326 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdb8f020-1237-331f-96a4-05efdb4c1431 | -3.44524 | -45.89214 | 2024-10-28 03:40:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 11f78efb-d4d9-341b-8a3f-7ef5cf917ac6 | -2.90556 | -45.26846 | 2024-10-28 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7d1c52a7-fa62-3553-bb93-aceab120bc88 | -2.79727 | -45.34993 | 2024-10-28 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47aa68b7-1b26-38ae-b963-281b58ddf474 | -2.79651 | -45.3545 | 2024-10-28 03:40:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4044b7e5-65cc-39ab-ab84-7263e5d4aea6 | -4.89589 | -45.95647 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d0e8e531-44c6-3ab2-8a4c-37881bba031e | -4.89509 | -45.96097 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4266ebda-1787-3fb6-a1bf-0311899767de | -4.8023 | -45.73698 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c0b0f5d-3a9c-37d6-9901-e56dba271c50 | -4.79706 | -45.73516 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 101bf974-43b9-306d-aa6d-3ab0b54e1e09 | -4.79623 | -45.73604 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce4448ac-04a6-3b20-8044-4ce721ca61f9 | -4.7111 | -45.79057 | 2024-10-28 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b2805c83-4a20-385a-af35-12319ad3ccec | -4.70496 | -45.78989 | 2024-10-28 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a549af8c-2b91-3295-839c-6502f342b4a9 | -4.70191 | -45.88176 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b1af7da8-3ad8-3b69-ab81-05db96fba468 | -4.70138 | -45.88456 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8b4ef189-c337-39ef-a9af-ac97972fca09 | -4.70102 | -45.88682 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c3bb321a-e3fb-3309-aba1-5d9c58bc2333 | -4.70054 | -45.88953 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bcf35dd6-fd25-3cd1-969a-26c38bd2ab06 | -4.69532 | -45.88323 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9adb823c-636b-3a60-89b9-0f47f7d727f6 | -4.69498 | -45.88537 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| fa4770ce-5d70-3dc5-98ac-f154414185b4 | -4.69451 | -45.88795 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 924a84f8-c49c-31d7-8acc-6e8c764fa76b | -4.69414 | -45.89011 | 2024-10-28 03:40:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 38a1d27a-a8b6-3269-a41d-4037f957c176 | -4.59213 | -45.60933 | 2024-10-28 03:40:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 89117c3f-e495-3f67-ae76-0e5b5ef7fd6b | -4.56502 | -45.8027 | 2024-10-28 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| af0b5862-8d35-3eed-80e5-ed822ec1994d | -4.56424 | -45.80724 | 2024-10-28 03:40:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 9049fb91-e748-3195-9303-fa314841e222 | -4.559 | -45.8012 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 091c1391-b0c7-3aff-a78a-7bc8931da697 | -4.55823 | -45.8057 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 415acc7e-dd38-3056-8e6f-ae39d18c69f3 | -4.55299 | -45.79973 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c720ce49-747c-3eeb-b92a-30e6ece462dc | -4.5469 | -45.79865 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d10c255-c259-35df-a44f-58a861c68b75 | -4.47979 | -45.67609 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| cad67d27-37ad-3c17-ae05-f563a03cb4cf | -4.479 | -45.68067 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 22be73fc-f674-3383-affe-d6478cc340eb | -4.47376 | -45.6749 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24f46823-7f24-3f26-a8c4-0c0d5bc65d6b | -4.47295 | -45.67961 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 456e75e0-9dc7-3874-9670-91e24ff4b9af | -4.42396 | -45.96356 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7ffc7ee6-fdbb-35ad-82b0-05c6336baa71 | -4.42316 | -45.96819 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7921871a-53c0-3a2b-b73c-a992c0245294 | -4.42175 | -45.65165 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 13c20b8b-8e13-37e8-976d-c3cf5939be32 | -4.42143 | -45.65021 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1a98d615-0a82-3a26-b82f-15e2db25a6ee | -4.41652 | -45.646 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| 7331434a-cd43-38ca-b3ac-6973980265fe | -4.41615 | -45.64463 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 0cacf89e-fdd6-33c0-9526-52ccd8dc2639 | -4.41569 | -45.6507 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| 468e6ed4-2f4c-392b-9892-8b095dd833c7 | -4.41536 | -45.64931 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 1327c7cb-f91b-3f1f-ad21-d948eed00456 | -4.41486 | -45.6554 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 17.6 |
| bdde360d-f5e4-35e6-8f42-c8a99e6ec33c | -4.41456 | -45.65401 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 31168411-2ab0-3ce1-a6ba-6b409149c1b2 | -4.39447 | -45.3395 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4091aeb1-ad86-3ed5-8190-2531c7cccd82 | -4.39378 | -45.34351 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fdf111d3-20d1-3642-97a9-7a24a8ece0a6 | -4.39305 | -45.34771 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4506d07b-c210-3040-a494-df0b8c34602c | -4.38854 | -45.33849 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 1d42e8f8-f998-3b2f-b4ef-757b94d4595a | -4.38781 | -45.34272 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 68504aa5-7e7c-38aa-84bf-f640d4ea652f | -4.38707 | -45.34694 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 98e22684-6d66-3c00-bbce-4d3132bf8ae5 | -4.38635 | -45.35106 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 7142c24f-da4b-3a76-8180-59f781727820 | -4.38186 | -45.34181 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| cc08fbe4-ad52-3d56-baae-4cff6fe9f605 | -4.38112 | -45.34603 | 2024-10-28 03:40:00 | NPP-375D | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9a4ae236-c9a1-332a-8480-d594fe2fd26b | -4.3649 | -45.8358 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a29e642f-db62-3c45-9b77-f334aac63676 | -4.36409 | -45.84058 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a39a7aea-818b-310d-910e-d6bc84980162 | -4.3639 | -45.8369 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6afdf49f-8e7d-3687-ae41-1c5f4cd51da0 | -4.36307 | -45.84158 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 214be508-3b12-396d-97f4-2c3737e5beb4 | -4.32474 | -45.77664 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 801680fe-d8a7-39fc-b0bc-bc5a49e31e61 | -4.32392 | -45.78135 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d426e0ba-0ebc-3446-8245-feee19e1d2e7 | -4.32309 | -45.78614 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 140afdca-9865-33b8-a552-5d17d199831a | -4.32228 | -45.79081 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 963dfab0-7c80-3179-827c-0e3496ad21fc | -4.32148 | -45.79539 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a5d3a187-c862-3030-acb6-dcee05b2892c | -4.31484 | -45.86996 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c0015671-76ea-323b-bbff-e27dbc0105eb | -4.28419 | -45.53594 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7fc0994a-65d3-3c89-b6fe-c5abb908bdb6 | -4.28343 | -45.54032 | 2024-10-28 03:40:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| d68d7661-4a6f-3df5-9b7b-bf3df1798951 | -4.28268 | -45.54469 | 2024-10-28 03:40:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| aafff1b0-78f5-3e1f-ab72-7203142f0f6c | -4.27892 | -45.53055 | 2024-10-28 03:40:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| e8fce330-79db-3ae6-a660-4160c4f51a1a | -4.27816 | -45.53498 | 2024-10-28 03:40:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 729824d3-fb93-397b-8321-f3b87ead923d | -4.27741 | -45.53935 | 2024-10-28 03:40:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3d080d2f-c191-36d7-8fb3-5bc7035dc49c | -4.27666 | -45.54372 | 2024-10-28 03:40:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 59480c33-c18e-3843-aa1c-095a9ab54100 | -4.08031 | -44.61271 | 2024-10-28 03:40:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51220352-b135-3b84-9f73-6ab944bcd1d4 | -4.07964 | -44.61659 | 2024-10-28 03:40:00 | NPP-375D | SÃO MATEUS DO MARANHÃO | MARANHÃO | Brasil | 2111508 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4478243c-5412-3a0e-a280-9e84360fe386 | -3.85 | -45.7271 | 2024-10-28 03:40:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README25.md)
