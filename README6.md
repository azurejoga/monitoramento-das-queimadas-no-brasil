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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3699cf4-a1bc-3386-89d7-a716da550c45 | 3.48954 | -61.93566 | 2026-02-25 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c858964f-29aa-37d3-aa4f-dfc116289c56 | 1.42046 | -60.75748 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6888046-b929-38e4-a703-d8622000ecb7 | 1.93628 | -60.35889 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48d3f304-dd4d-3e3b-a491-856b63182c7e | 1.51741 | -59.93658 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2dfd4d75-d533-384d-814a-37f16001807e | 1.36406 | -60.29317 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 43cbb772-9c07-376f-b998-19e65ee339bc | 3.24786 | -59.92254 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 846e7352-eabd-3c73-a373-a0d5474f0a93 | 1.94069 | -60.36526 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e84227e-4873-375c-909d-6ccf0d990de4 | 1.50909 | -59.94852 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d9c4df0c-56a5-3460-b15a-5dc606871d7e | 1.47425 | -59.94046 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| db971247-c04c-30b3-bd43-5e000655f44b | 2.22752 | -60.70184 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8057d7a5-4525-37c8-b986-e6fc590c55c6 | 3.51401 | -60.38342 | 2026-02-25 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23f71e3d-ac42-350a-a9b3-03a5deb347fa | 3.44939 | -59.89062 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6bcbe2f6-d481-366c-aff3-69b043dc41f6 | 1.83072 | -60.84563 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8181dd09-fd6a-33e4-a9e9-f716a5a9cc26 | 2.7137 | -60.22525 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2167e9c7-c82e-3bba-9693-89463671e955 | 3.45102 | -59.90095 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d33dfa43-a84a-3090-9968-f63666572b4d | 2.93611 | -60.30689 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 0f234ff5-b9b4-33ab-b280-2142d0e88231 | 1.82794 | -60.84962 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d60e26cf-d66a-39ba-be66-fe85b2d6c083 | 1.50581 | -59.94614 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c12bb713-49c7-3601-beea-1d2e7a78fcf1 | 2.23362 | -60.69734 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 535f824f-53ae-3157-be8e-10f50d6d34ca | 2.87427 | -60.26001 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 023e51ea-b5c8-3c20-b6e8-b066765b852f | 1.51187 | -59.94454 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 47ee0b8c-6eb6-396e-9371-bf8195047b99 | 1.50194 | -59.94321 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 4bd5d22b-58d2-37c7-b9b7-761d7f7db179 | 3.44884 | -59.88717 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76cd96c7-3965-30b4-b597-fc17e9b445ee | 1.50139 | -59.93975 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 77e7a7bb-26ab-3435-826e-fc584edb033b | 1.93763 | -60.85736 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3928d0df-26cf-381c-8cb8-dfe71d433104 | 1.51132 | -59.94109 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 109f0d38-ec0b-3aaa-bcee-15ec92796e8d | -4.07385 | -54.70311 | 2026-02-25 05:33:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3e5a60f1-fbed-37d3-9112-a831ecc5431e | 1.49807 | -59.94028 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| 7e2dfd70-b9e8-37c4-bbef-623a468fda73 | 3.44913 | -59.90897 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff59c453-08a8-3e40-b30a-002c1c8b4ba4 | 1.93709 | -60.85389 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef6e2eeb-a80e-351e-942e-2e7d00314f60 | 1.5003 | -59.93285 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 81141b76-acf4-3bdd-8697-fed5b2da1c57 | 1.29004 | -60.4248 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90375336-6a87-377b-85cc-b5726bb23d34 | 1.51077 | -59.93763 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 7762f08c-8d69-3dde-9456-cea944f0c23d | 3.44993 | -59.89406 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a39f2a5-6b30-3f65-b711-a230c17ce17a | 1.49474 | -59.9408 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 51.1 |
| cf1ed7bd-5a84-38b5-837c-4e62404dbbab | 2.87482 | -60.26345 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 733014ae-ff4d-34e2-867d-cad3d0ab9f61 | 1.31055 | -60.40395 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cccbbffc-cc9e-3f2d-88c8-3fd983735280 | 1.36788 | -60.31728 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 854c21dd-94ed-3452-b092-3b598a6bf1e8 | 2.71034 | -60.24697 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b6f3d79f-744f-392b-ad10-bbb39e1e49a0 | 3.44309 | -59.89225 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a3394889-04cb-39db-93f4-c23483407328 | 1.51574 | -59.94748 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 176ae89a-e702-3ca8-afcc-74d0277b2dff | 1.49638 | -59.95116 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9f087b0f-2eed-35f6-86d2-b2ba958daecb | 1.49197 | -59.94477 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e55d5094-6bb8-34d7-9ed2-0ddc90aefebd | 1.48254 | -59.94979 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 594bc4e1-88de-3718-9218-95185284b508 | 1.47589 | -59.95084 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| afd07331-4c7b-3335-8578-8b1b294e9b81 | 3.49205 | -60.28765 | 2026-02-25 05:33:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d0cd4e49-2085-3802-847c-dc420dabe913 | 3.44527 | -59.90604 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f0bda757-78b8-31cc-ae83-e6dede2f660a | 1.48864 | -59.94529 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| 81d9f7b8-072f-3017-97b0-5b478a6455df | 1.20614 | -60.62129 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e58ef9c3-8122-3567-b8ee-d84fbb2f1f98 | 1.51946 | -60.03249 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fb6f9bde-0275-3967-9495-cb3a98fbf67b | 2.11359 | -60.19654 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 72a70c33-9f25-3027-bf8a-0b051400fa3c | 1.51464 | -59.94057 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 611dd196-e047-34f9-853d-f39b74730cb1 | 1.48586 | -59.94927 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 430fa2c3-62cd-3711-834c-d48243bde334 | 1.47922 | -59.95032 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c5d067a2-e80f-35ec-bfdb-5b0d1f333561 | 2.72252 | -60.238 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7520299c-040d-3b23-8e73-ed1746901333 | 3.44804 | -59.90207 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| e1972309-6912-3867-908f-90baef19948e | 1.88536 | -60.91529 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3794b680-10f5-38eb-b22c-a66d229b600f | 1.92464 | -60.37129 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 448c948e-2544-3bb7-9d6a-f57999b77813 | 1.88149 | -60.91233 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c478c516-bfe2-3620-8817-8346ba2db295 | 3.49013 | -61.9394 | 2026-02-25 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 91c7f104-ab52-3d49-9198-02364cadf26a | 1.51409 | -59.93711 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 98efd8f9-c41a-332c-a3e1-d173f94a21e7 | 1.51354 | -59.93365 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 40f2ec9e-ba8c-3fcc-be7c-cd23065f7d0d | 1.50472 | -59.93923 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 14.6 |
| 2137535d-bf96-331b-8c72-d72d08af3265 | 3.265 | -59.92339 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da5ed83a-2c53-3e47-9d4e-643eee0abb0d | 1.50744 | -59.93816 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 52349cd7-b194-33b6-8ac9-688f0c2b2729 | 1.47644 | -59.95429 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| c6f66b02-8e7c-301e-9474-87af2cd1599a | 1.88203 | -60.91581 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 78813735-0e43-3a55-925f-73860471dc5f | 1.49306 | -59.95168 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 22.8 |
| ca51c931-d4ee-3062-89c0-58e2561c8771 | 2.71366 | -60.24645 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7bf2da6-db2b-3045-8342-4135575f69e8 | 1.51241 | -59.948 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b8c0caf6-dde6-33e3-b636-0892918e400e | 1.94014 | -60.36182 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca86b159-07b0-389e-a54d-e197f873b604 | 1.50635 | -59.9496 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7fd97f80-0a72-35d1-9dc6-5adf25aeedc1 | 1.47812 | -59.94341 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5330736-3ce2-32c5-b5d6-ad9156667916 | 1.2056 | -60.61785 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3f223425-d99b-3120-ab06-b6429f23b89f | 1.93682 | -60.36234 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e22ba5ab-53b0-3b93-9e70-42dc288e7fd4 | 1.28727 | -60.42877 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7901f59-b466-313d-a810-f3ebbdc5f67a | 3.04823 | -60.88657 | 2026-02-25 05:33:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b8373af-6afd-39ed-9522-92775275c08d | 1.49529 | -59.94425 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 3fc3b592-845f-3042-8284-15149930aa60 | 3.13624 | -59.9857 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8705119e-2a4c-3c64-bd24-40209c701788 | 1.48641 | -59.95273 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 19.9 |
| 3bf93b5b-35ca-362e-80e4-c4a93ca67184 | 2.23084 | -60.70132 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 77013b24-41e0-3e34-9bae-202be8f617a5 | 3.25118 | -59.92202 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e128664d-0d0b-34e7-997c-09c71c5df1d6 | 1.8787 | -60.91632 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ace58ffb-95a4-3b15-b552-2d2cf045157a | 3.16124 | -59.95382 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 11bbafa2-a3f8-3c4e-b4df-e7ed57b369d9 | 1.94624 | -60.35734 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f4fbdac4-d772-3d9f-af28-ac3f7ff90cf5 | 3.48552 | -61.93243 | 2026-02-25 05:33:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| eb4ef759-584b-321f-94b9-fdc122715ecb | 3.44582 | -59.90949 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 56f46147-414b-30c2-88de-bf6b2ec61737 | 2.92849 | -61.40482 | 2026-02-25 05:33:00 | NPP-375D | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31598cfa-6a70-38c1-ae0d-dd52d6501441 | 1.51851 | -59.9435 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d56e81ed-5091-3d97-bfeb-be153fe82ee8 | 1.51796 | -59.94004 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1c2eb308-31a5-39c7-8c30-472cd99f4660 | 1.49251 | -59.94823 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 30.9 |
| e59111a6-ce5c-3426-bed8-4139e7e180ae | 1.51629 | -59.95094 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0b3a3dd5-652d-359a-a479-89f62dfb2436 | 1.49916 | -59.94719 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.4 |
| 6826f595-6e1b-3966-9ce8-b2cc619dba48 | 3.26223 | -59.92736 | 2026-02-25 05:33:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 0fa56cc0-195a-3eed-84a8-29f6983ed887 | 1.94346 | -60.3613 | 2026-02-25 05:33:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 111a23fe-ddc7-3b0d-8558-09b226e7f92b | 1.93987 | -60.8499 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cbf351bb-9469-36b9-8598-d642de9fa308 | 1.93599 | -60.84696 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0e68490a-8172-3ccd-a333-360e4f353913 | 1.93654 | -60.85042 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 909ee433-de61-3b1f-94f6-95132dda7597 | 1.48199 | -59.94634 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| daf31791-b55c-360e-9e3f-5e12ab2acd59 | 1.50526 | -59.94269 | 2026-02-25 05:33:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.4 |


[Clique aqui para ver as próximas entradas](README7.md)
