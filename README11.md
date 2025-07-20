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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 943a80b4-3e78-31b6-b4f7-09e88c9cb7db | -15.7366 | -46.28383 | 2025-07-20 04:17:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 06a5ed65-e9f6-3a33-b49e-4365003de1f6 | -15.25078 | -46.96194 | 2025-07-20 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6d5a9eb-9a23-3b3f-a9fa-07636eecd62e | -18.89542 | -43.34131 | 2025-07-20 04:17:00 | NPP-375D | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| df9a7677-4b68-323c-a25a-2491671eac44 | -16.05398 | -48.11079 | 2025-07-20 04:17:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fe5f7903-c370-3f18-8a1a-f2d11c05984d | -15.99455 | -46.90626 | 2025-07-20 04:17:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 069f2d80-8b4a-3430-a35b-6365ba180618 | -15.92482 | -43.51409 | 2025-07-20 04:17:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ef2c933c-b7dc-3cd4-94fa-1883c2ebb942 | -16.70327 | -49.12705 | 2025-07-20 04:17:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ee0d849-24fe-30cc-af5d-2d0cb46d2374 | -18.89895 | -43.34186 | 2025-07-20 04:17:00 | NPP-375D | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 76cc3de0-1057-337d-bdde-bf0d51e5ce55 | -16.70537 | -49.12488 | 2025-07-20 04:17:00 | NPP-375D | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 81c706a8-dc3c-3510-87a7-dec78f0e1ce8 | -19.39765 | -43.24382 | 2025-07-20 04:17:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 822db398-6c6f-3989-b47f-55bec3da3d01 | -16.05468 | -48.10671 | 2025-07-20 04:17:00 | NPP-375D | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 36fa711a-ee5a-35bf-8855-aa1e6f135ccd | -14.20582 | -54.65703 | 2025-07-20 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ce82f416-416b-30c2-8092-28f7a0c0c435 | -18.02156 | -44.47483 | 2025-07-20 04:17:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33280840-2eb1-3423-a40c-5e0c79da4260 | -17.88439 | -51.68069 | 2025-07-20 04:17:00 | NPP-375D | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3c848d4d-8650-3e31-bb3e-dece7b5e8caa | -15.25015 | -46.96573 | 2025-07-20 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| bdb3908c-db0e-375c-b96c-37abdf2f8990 | -19.39707 | -43.24799 | 2025-07-20 04:17:00 | NPP-375D | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 422fd812-15f7-348b-8cd7-85c0be4b1c43 | -15.25355 | -46.96642 | 2025-07-20 04:17:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f051b52f-f7d1-3f72-a76b-b8800f5cb862 | -18.40607 | -44.18663 | 2025-07-20 04:17:00 | NPP-375D | SANTO HIPÓLITO | MINAS GERAIS | Brasil | 3160603 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 69cd4332-453c-3d61-9cbe-ce833bc4322c | -17.59674 | -43.19907 | 2025-07-20 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bae13699-a5e6-3f0b-b375-938e785eb2d4 | -17.17958 | -47.76742 | 2025-07-20 04:17:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 558edf0e-4d8f-35e6-ae63-ccb0ee6deff5 | -16.08983 | -45.17289 | 2025-07-20 04:17:00 | NPP-375D | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 78f11a1e-950d-3aac-933f-427b28f0d4c4 | -12.36166 | -50.32269 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf607848-ceb1-3522-abb0-b73a90ea0db7 | -12.3786 | -50.32588 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4cfdea46-6f26-3fd0-b741-f2777508980d | -12.35319 | -50.32108 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6625ff80-f1b1-383b-acdc-f60a300e15ee | -12.28875 | -48.78448 | 2025-07-20 04:19:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c574e68c-028b-37c7-803b-108e2b0f8b13 | -12.68053 | -46.83216 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 50359133-b0b2-3da1-b550-4e1a2f8516de | -12.36661 | -50.31947 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f5665544-14e0-3d51-9a5e-5c22c5eb343a | -12.51332 | -57.24257 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa11b60c-aa12-30b3-a6ce-79df17db3bdb | -14.75337 | -48.25436 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b317fea-2e8f-3cb3-af3f-fb570ebc52d7 | -12.51987 | -57.24401 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 79b48ea2-0df5-333a-9434-4efe8f6e1bb2 | -13.90135 | -43.87125 | 2025-07-20 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91d2d87a-490d-3eee-94af-fe977672aa3e | -13.45772 | -48.02461 | 2025-07-20 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae959b8c-57eb-3d4f-93fd-9b852b28a4d2 | -12.37364 | -50.32381 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5615f74f-cb8b-39f6-8b14-d8f11f65a361 | -12.3799 | -50.33742 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6ee7d27e-1a23-3597-bcaf-86c294aa0410 | -12.37567 | -50.33663 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a02819-2500-3722-808c-353153e4ffaa | -12.66546 | -47.09385 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5824ca0b-1e02-36b9-bddb-d81c713e88d1 | -12.52108 | -57.23815 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 269a1fde-7ed9-301a-8ed6-8b6eabb0b6ac | -13.71298 | -42.50741 | 2025-07-20 04:19:00 | NPP-375D | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ae3fdcf1-9bd4-3aaa-bddc-b6ff219daa0d | -12.66127 | -47.09723 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d926bb8d-f9fa-326f-ac67-9722eacfdc70 | -12.37437 | -50.32508 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f579f0d-8b8c-3eb6-99b0-3fd9c09a6049 | -14.74526 | -48.27989 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d64da13f-2531-3747-93a5-3c8194a1e7fd | -10.8101 | -56.95839 | 2025-07-20 04:19:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8fe18839-74d9-366b-ad50-2ba57dc8344f | -14.75701 | -48.25487 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ecdc0ae9-32ec-3b38-949b-a1db3dfe4a19 | -14.48369 | -46.3575 | 2025-07-20 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 61028c78-31da-3d2f-a10f-5d3bd29c268c | -12.51696 | -57.24815 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d88b94c-4d3e-3448-8bd4-ccdf87dccd0b | -12.34824 | -50.3243 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3624fbae-b35a-301b-bedd-0995972941ca | -12.52477 | -57.24369 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aabb1813-305c-3b07-8b6d-f37397a2de38 | -13.898 | -43.87071 | 2025-07-20 04:19:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c65757f2-b087-33c2-8f93-15897e0f224f | -14.75626 | -48.25926 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cff0c07b-2d87-363f-95c8-f47c73a39d0e | -14.70012 | -45.05985 | 2025-07-20 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99f550fd-e951-3a17-9fc5-7b2389f7b00e | -13.45331 | -48.02842 | 2025-07-20 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0efa311f-27ca-3b06-9c2b-02c296e9ae6b | -12.3694 | -50.32302 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 031e7be0-4329-3a1a-a025-825deb9a6b91 | -14.74816 | -48.28477 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e509219a-68f0-3033-a61b-54859be16719 | -14.69956 | -45.06341 | 2025-07-20 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c77667ba-6447-32ab-a526-951b6ccd9ff7 | -12.34753 | -50.32831 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea4379fc-b260-33b7-a910-d67693e1f54a | -12.28959 | -48.77961 | 2025-07-20 04:19:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 317aa61b-7cd8-3e42-a4e7-7e3ae843edd3 | -14.79098 | -48.29645 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7ef6231-ff41-31ec-9d0e-61e563caffef | -12.37787 | -50.3246 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80469758-d6ea-326b-9299-ecf8e6dac2ee | -12.98178 | -46.91274 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1d9e34f-70da-33b2-89a2-47830ba403a1 | -12.58166 | -56.97709 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5a7d2790-bfaa-376e-b7da-f6e5d6dca465 | -12.98114 | -46.91653 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24e8ea7c-7318-344c-85a2-3dec74a9ee4f | -12.34401 | -50.3235 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 6966bdd3-df7c-354c-9713-695bd851c395 | -13.54503 | -47.49338 | 2025-07-20 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70e316e6-7a75-31e8-83d4-5ec800f1e5f9 | -12.97984 | -46.92428 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7be1d314-5b85-36e6-b780-2a8e30f4f756 | -12.58057 | -56.98159 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f650f4ef-37fb-304b-a81d-3af808e86926 | -12.34896 | -50.32029 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7b3864b-6358-3490-91d3-351e9c7a79dd | -13.45409 | -48.02391 | 2025-07-20 04:19:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1d15efc-17eb-315c-9d68-b87315bef145 | -12.35743 | -50.32189 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1e8c36c5-ccf4-3259-93d5-bffc6cb498c0 | -12.5182 | -57.24232 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 87ff8e5f-d06c-3cfe-b610-241802e3a3a7 | -14.70344 | -45.06041 | 2025-07-20 04:19:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4d62937c-79d8-31b9-92e4-552f1ef9c07c | -14.74741 | -48.2891 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 899a81f0-5bb3-35fe-9c86-9e0bbe5bb384 | -13.00201 | -46.92012 | 2025-07-20 04:19:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ccd0f822-b18a-3162-a65c-568cfebd0f52 | -13.8951 | -50.66108 | 2025-07-20 04:19:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5e98be45-cffc-3025-94ad-ab5a75d3d178 | -12.34329 | -50.32751 | 2025-07-20 04:19:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d5b65d8d-b678-3ba6-bdf7-bd5cb1f32a34 | -14.71145 | -48.23793 | 2025-07-20 04:19:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4caf9d5e-cc9f-3eba-8eff-4da60f90de12 | -12.526 | -57.23792 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4801d013-30c9-3a4e-8ab8-6ca8eb15ffea | -13.54197 | -43.70729 | 2025-07-20 04:19:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5f2901eb-1e09-3776-b563-1f260154d2df | -14.48032 | -46.35692 | 2025-07-20 04:19:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 451d64ad-39b4-3599-a051-b2be47e9304b | -12.58055 | -56.98249 | 2025-07-20 04:19:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 73199194-e0c6-3664-b5c9-8541bb49893c | -23.10022 | -50.10579 | 2025-07-20 04:19:00 | NPP-375D | BARRA DO JACARÉ | PARANÁ | Brasil | 4102703 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 8724b5a2-437d-3c73-9c05-01db76a7e2aa | -20.10079 | -44.0773 | 2025-07-20 04:19:00 | NPP-375D | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 2dee715a-3b56-3df9-a4d4-b7863e871ca2 | -20.05726 | -47.59288 | 2025-07-20 04:19:00 | NPP-375D | IGARAPAVA | SÃO PAULO | Brasil | 3520103 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5eee64e0-343a-3a35-9054-d11dae41d682 | -20.09694 | -43.90823 | 2025-07-20 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6677b166-0fed-398b-ae95-0a221a8dafd2 | -20.13041 | -44.86652 | 2025-07-20 04:19:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f441b3f-f4b5-3d91-b981-b9efbae137e9 | -23.15307 | -49.9732 | 2025-07-20 04:19:00 | NPP-375D | JACAREZINHO | PARANÁ | Brasil | 4111803 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 7e964ec0-8cd8-341e-9a74-2e17efa69cdc | -22.9263 | -43.19131 | 2025-07-20 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| f1b97bc8-4cec-3ed6-8037-9c491912489b | -22.43301 | -48.98981 | 2025-07-20 04:19:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 559043d6-74aa-315a-a9a8-bd18293db718 | -22.96298 | -43.59887 | 2025-07-20 04:19:00 | NPP-375D | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7dc2b4a3-7b17-34b8-ad75-d5859ad11790 | -22.71365 | -43.84562 | 2025-07-20 04:19:00 | NPP-375D | PIRAÍ | RIO DE JANEIRO | Brasil | 3304003 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2d9feba9-b27c-3154-85b1-fb3de0aaa7ff | -23.25299 | -47.11366 | 2025-07-20 04:19:00 | NPP-375D | CABREÚVA | SÃO PAULO | Brasil | 3508405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9b4a64d1-5937-3dbc-a03d-2e46b1b5b3f4 | -23.10178 | -48.97034 | 2025-07-20 04:19:00 | NPP-375D | AVARÉ | SÃO PAULO | Brasil | 3504503 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7f67da1f-4bb3-3334-a2bd-aa02a7ed3a4f | -22.43645 | -48.99049 | 2025-07-20 04:19:00 | NPP-375D | AGUDOS | SÃO PAULO | Brasil | 3500709 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12bf87fc-87ab-38bd-b5c8-a1c70f75f962 | -19.90337 | -47.37883 | 2025-07-20 04:19:00 | NPP-375D | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 081da654-4feb-3d12-8a54-68dec8c939e4 | -20.12703 | -44.86594 | 2025-07-20 04:19:00 | NPP-375D | DIVINÓPOLIS | MINAS GERAIS | Brasil | 3122306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 92793f16-1f22-30ee-872b-a161eca7697a | -20.10386 | -43.90965 | 2025-07-20 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 0b77d532-1a56-35e5-a892-8a1264ae60a6 | -20.09636 | -43.91229 | 2025-07-20 04:19:00 | NPP-375D | NOVA LIMA | MINAS GERAIS | Brasil | 3144805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| db860c2c-2e1d-33df-b2e2-5317ec5b4822 | -19.02141 | -54.66177 | 2025-07-20 04:19:00 | NPP-375D | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c35ec6f1-a80d-3cb7-91ed-ecf2c8b2c8bc | -19.45354 | -45.30556 | 2025-07-20 04:19:00 | NPP-375D | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4d9c80b0-bf4c-3c63-92c1-b1223533b3ad | -23.14009 | -48.49392 | 2025-07-20 04:19:00 | NPP-375D | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 85c485c6-71e9-3236-904c-a3e65701d67e | -19.73775 | -43.91039 | 2025-07-20 04:19:00 | NPP-375D | VESPASIANO | MINAS GERAIS | Brasil | 3171204 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README12.md)
