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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 85788a1a-0dc0-3460-9fdf-97d90acfa3b4 | -6.74695 | -46.46329 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ec016d95-b516-3d95-94fb-4e284bacbc55 | -6.67247 | -46.16158 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 767efe79-8c53-3625-85ca-e8da947bf6fc | -7.42266 | -46.69823 | 2024-10-14 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9506768-13a8-3573-9dc3-29f766db745a | -7.41932 | -46.5564 | 2024-10-14 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4d8c7263-21d7-350e-9835-4e9db7257394 | -6.80142 | -46.47322 | 2024-10-14 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1705e3da-cb72-3575-a509-bb80e2ceb228 | -6.67797 | -45.95794 | 2024-10-14 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a64e0a29-a803-3f40-83d5-6c2b706c39a0 | -6.67169 | -46.16679 | 2024-10-14 04:44:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65292f7a-711f-3a73-bba5-865d916dda9b | -7.97196 | -45.60658 | 2024-10-14 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82bea4f1-47d1-31c2-8fd8-c6e77fdc05d5 | -7.97141 | -45.6105 | 2024-10-14 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 864c702b-f13f-3ae1-b0b2-5921aefa35c2 | -7.97124 | -45.61061 | 2024-10-14 04:44:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 16497254-fe94-30d7-a219-df980f7fddb9 | -7.91858 | -46.16217 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77fe1ce4-5d68-335e-92ac-d4c474344506 | -7.70838 | -46.60193 | 2024-10-14 04:44:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36afd55b-d59c-3c65-a4ab-6c014f0e2c08 | -9.31163 | -46.0998 | 2024-10-14 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8d30bc24-4470-3c9e-899e-07a2aeb6cce1 | -9.09892 | -46.49598 | 2024-10-14 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ef246c0-fd18-3577-b11e-3985a32cdb54 | -8.71949 | -46.63494 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 536390d0-3676-3d4d-b0e0-75b171fc6238 | -8.7115 | -46.63398 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bf8c3796-27bf-393a-8917-43d818facf8e | -8.70603 | -46.64379 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcfff882-f8ac-3e67-94c5-4beac43247f8 | -8.69681 | -46.73659 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ee05c5f5-208c-30b6-9b41-3c6f013b1ad1 | -8.21018 | -46.79321 | 2024-10-14 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 78bc024f-8cc2-3cd5-b2d1-359015e091ca | -7.99343 | -46.85959 | 2024-10-14 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93377d7e-1c06-37c3-8627-caead25f94ed | -7.99304 | -46.8576 | 2024-10-14 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a1125c14-25af-328d-9b49-b411e2854278 | -7.99232 | -46.86242 | 2024-10-14 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91241807-7bd2-3bb2-99ff-3c25d52db43b | -7.98916 | -46.85697 | 2024-10-14 04:44:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 26068107-a285-3496-accc-c6f0bd95b8a9 | -9.09488 | -46.49539 | 2024-10-14 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b340d301-8dbe-38aa-8be1-724114686928 | -9.0863 | -47.05064 | 2024-10-14 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e3fef480-53fb-3fb8-bf1c-5d588ba8ce3f | -8.72348 | -46.63548 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3499a6e7-d397-366c-81a4-4a801627bac8 | -8.7155 | -46.63444 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad788c72-ca5f-3bca-9928-66d561250abd | -8.70749 | -46.63359 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7f5388c-7875-3782-a551-659ba596b1e7 | -8.70676 | -46.6387 | 2024-10-14 04:44:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91b06ba9-60ac-312f-83b8-4ed422b8149d | -9.68015 | -46.91181 | 2024-10-14 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 32c617ce-2f15-32ed-afbf-b24f6a3a630c | -9.67692 | -46.90612 | 2024-10-14 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8346fe2d-bc12-3019-86f9-5ff07bbd0f0c | -9.78096 | -46.47166 | 2024-10-14 04:44:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a547d39-13a0-3350-8622-ae72f2e288f3 | -9.68089 | -46.90665 | 2024-10-14 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ec1f855-e56b-33ea-902a-d2184da13505 | -9.67618 | -46.91125 | 2024-10-14 04:44:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70361372-a7d2-3417-81c1-a5d789a0bec4 | -3.55894 | -46.1489 | 2024-10-14 04:44:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aacdd1b-a16f-31d9-a521-787f6a187c36 | -3.53389 | -46.31063 | 2024-10-14 04:44:00 | NPP-375D | SÃO JOÃO DO CARÚ | MARANHÃO | Brasil | 2111029 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 739c13ba-80dc-3d0e-a51f-0e8fdb6aadf2 | -3.35705 | -46.48523 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d2cf9cb2-34c9-302f-bffa-90a6c148b5b1 | -7.01994 | -48.32023 | 2024-10-14 04:44:00 | NPP-375D | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| efb3382e-fce2-3716-82fc-9004ab525701 | -3.35637 | -46.48967 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a4b59031-2dce-3cf4-a118-b4f08ddd1def | -3.35264 | -46.48903 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fbf665cd-0275-35f7-8f5c-e177c52c852c | -3.08649 | -46.54324 | 2024-10-14 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8eb7f806-6b61-3e63-9009-75e9f5473234 | -2.75021 | -46.74823 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4418fc59-6960-3243-bb30-626be2a6780c | -2.7459 | -46.75192 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a6609c13-cfb1-3049-a103-d0611338f3cd | -2.7416 | -46.75562 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2a641fa0-256f-3632-83ad-9d9cf78b26df | -2.71952 | -46.71054 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a9faacf3-48df-3d2a-a88b-295509802912 | -2.4528 | -46.01915 | 2024-10-14 04:44:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 03e15340-3c9b-37b1-8194-806417fbe9ed | -2.44892 | -46.9165 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 768f8f8e-a1ec-3979-8525-689f597829e2 | -2.4453 | -46.91597 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e2551cd1-991f-37b1-a2e8-53ee433f7727 | -2.44467 | -46.92004 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ac56cc57-a18d-3e59-ad0b-8e68dee7f86f | -2.44169 | -46.91541 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| d9043260-f85b-3168-ab91-7f6a4a0d2ea2 | -2.44106 | -46.91948 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| c0f1c5ea-1b69-3675-b00d-b7cbfd312187 | -2.43808 | -46.91484 | 2024-10-14 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 18.9 |
| 63afc782-12fc-33e0-a4e4-cb6d8d19e553 | -2.42426 | -46.15492 | 2024-10-14 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7defbd23-043e-3343-a2c1-524f7caaf5a1 | -2.4205 | -46.15434 | 2024-10-14 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 94aae37b-74e5-38a6-b471-678270dac8e3 | -2.3704 | -46.48173 | 2024-10-14 04:44:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b01ceec6-b352-3194-a7e0-fae1207e775c | -4.98914 | -46.49503 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 544b062b-10e4-331f-be5f-3536fc5e812d | -4.86649 | -47.1045 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca0a6cb8-43d6-3e7d-ac53-65b442eb5b4e | -4.86413 | -47.09513 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 501b9980-7cfe-3b8d-8a5c-269aaf46b5e7 | -4.83735 | -46.88652 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dc01c7aa-564c-3adb-a3f1-ce7ac2cf8695 | -4.71078 | -47.2994 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ce6e54c5-a78b-37bc-95ab-8433a3e00754 | -4.71017 | -47.3035 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6e2e03ef-1287-349e-a192-1ccd978ae1e9 | -4.70777 | -47.29473 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 42a2963c-c245-30ba-80ed-b92db27a2dc2 | -4.70715 | -47.29884 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5239030f-c0ca-3f05-9812-47def64dbb21 | -4.70653 | -47.30293 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9e5e715-aeed-31bc-a19a-d5c5236e7f24 | -4.70351 | -47.29829 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5883bdce-e11a-36e8-bf4e-84baee96a12a | -4.7029 | -47.30238 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 62c399aa-a7da-36b8-a223-18d132874e34 | -4.69771 | -47.28614 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 329dfd7e-8379-3787-808e-cc2df7da80c1 | -4.68131 | -46.39343 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0702eb3f-e6a3-38b1-beae-19afb8da7c6e | -4.67178 | -46.30066 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fb8c22d1-c5a8-3ab9-9dac-828d0118d415 | -4.66072 | -46.80529 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 18a77d7f-f308-35b0-8274-6b9217914fa0 | -4.65596 | -47.73542 | 2024-10-14 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 125b97ae-0692-399b-a17b-8ee179532897 | -4.65562 | -46.81352 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5620d241-010c-383f-9dac-0615671d5a58 | -4.65259 | -46.80848 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 18013a6d-6b28-351d-8701-78d80c70aec0 | -4.34925 | -47.57288 | 2024-10-14 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24e240b0-0a15-3d0a-8297-45c170eb70bf | -4.33223 | -47.31577 | 2024-10-14 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c95ab67c-58c8-3eb0-b8c0-b0ec4204a38c | -4.31418 | -47.31276 | 2024-10-14 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5b31d6aa-7680-3eea-87ee-cb01a9a283c6 | -4.28588 | -47.30413 | 2024-10-14 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e36ec1b2-fd52-32d2-8e6d-60ddc89619cc | -4.28524 | -47.30836 | 2024-10-14 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8270a492-b41a-39a1-9662-0f722ce79794 | -3.82393 | -47.50181 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 336da747-0095-3b53-9d28-484a9f60c057 | -3.82331 | -47.50583 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6432c43-ce52-3f16-819d-55e5d7f6881c | -3.82271 | -47.50983 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 673e2e24-47c4-3d74-8004-bb4a20d4cd2a | -3.82036 | -47.50127 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d969b767-7b0f-3b85-901c-d76b6381befa | -3.81975 | -47.50531 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8afbbf15-b676-3cf5-b2f6-56c4de5513f9 | -3.81914 | -47.50931 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 52410a2b-4ebe-33ee-97d0-3fb05b7379b6 | -3.80498 | -47.48241 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5fe0cbf2-e846-336e-94a6-a23ded0a449a | -3.76247 | -47.5056 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fd70018-e11e-36f6-b2f5-c24aa8e5786f | -3.76185 | -47.50963 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411fb453-a9aa-3619-a290-fe96d6d4659a | -3.75829 | -47.50908 | 2024-10-14 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 87a23656-f038-3ef3-8109-450be61ab03a | -4.91051 | -46.83716 | 2024-10-14 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3908fd81-8bc7-3d32-ba8c-1bcae516564b | -4.67249 | -46.29592 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 126021ee-2a01-39bd-9079-223e59a9f0fb | -4.66865 | -46.29528 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ea3fdbb8-f5ab-3bf0-9237-2bdfd26971f5 | -4.66111 | -46.80764 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 723158f4-66b8-3322-ab7b-324c9b5f27e0 | -4.66003 | -46.8097 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e294488-2e74-3d59-a1f1-5be8933a7d8b | -4.65631 | -46.80909 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5b775e4c-1fc0-3caf-9d25-42ec396f5cfb | -4.65326 | -46.80408 | 2024-10-14 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b71a4df6-49c0-3f86-8160-6f30e944eb54 | -4.61388 | -46.33263 | 2024-10-14 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b9622d57-fa70-3609-9ab0-c734bf189272 | -4.36116 | -46.75393 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13af557d-e0ee-3e7a-92bd-ca43687f4e4c | -4.2027 | -46.90053 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 285551bb-f4a7-324b-bd34-37d45c3c49c6 | -4.18244 | -46.7358 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 61e828b7-6268-307f-9738-7d089a002048 | -4.17872 | -46.7352 | 2024-10-14 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README77.md)
