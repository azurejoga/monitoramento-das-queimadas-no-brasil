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

## Dados Diários - Página 17

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 972e572f-1560-3030-a596-bec2e0ffbccd | -11.16053 | -54.85624 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6d06d642-c85d-3694-ab5e-d2a2c898e79e | -14.27279 | -45.2962 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 1c2faa50-43c9-38c6-9030-aaf9110449a0 | -9.48904 | -57.32384 | 2026-08-07 04:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c6791a9e-0a0d-3f8e-8246-764c8bcd211f | -12.00925 | -49.282 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f5087f47-f1ac-3545-a8f8-27143da6dfc7 | -14.42982 | -45.67717 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9e9a115b-e4ca-3627-8571-ce181a027186 | -12.55527 | -46.95423 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b6568d9-d8e2-3b33-b301-7636691430b3 | -13.96192 | -47.36783 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0e4266c2-5c30-351d-8767-37de1b4b82e7 | -14.43163 | -45.67914 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2b7daf9-ba1d-343c-b81a-022ca09ce8e7 | -12.49934 | -50.53675 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5e4ed831-c0e9-3a4b-9690-f9f91690aadf | -11.18226 | -54.85609 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9f802c1d-6a3d-3eeb-b1c4-d98c15e82c97 | -14.34007 | -54.93153 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d2b601c5-3217-3961-bdd9-1398bd4166ab | -11.46685 | -44.57245 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 916463d9-2c0a-349d-9739-ea19af6bc425 | -14.93376 | -49.00537 | 2026-08-07 04:46:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63ae2a40-b846-3b69-8783-8c2e04cc2f87 | -14.15468 | -54.00042 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6cf79977-880a-39ce-840f-7e94ac8bd6de | -13.69067 | -51.98244 | 2026-08-07 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 634f6c70-3bec-3c35-a851-212b148d7159 | -12.56526 | -46.9352 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b3d2a05-d368-3158-987d-deac063933b3 | -15.08217 | -53.59373 | 2026-08-07 04:46:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 25c04aec-2a2f-39e6-a661-2e2922690a37 | -12.44127 | -50.36412 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13058c09-d371-3289-ab02-b058ebe728e1 | -10.93242 | -57.17821 | 2026-08-07 04:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 92003972-49d8-33ad-a557-90a1c5c0ce70 | -13.78413 | -49.72142 | 2026-08-07 04:46:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 76db9716-3d24-3b66-8142-9b04acacf18f | -16.18542 | -46.2259 | 2026-08-07 04:46:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0d4f0bf1-7d5a-3e57-8169-175b35cc999d | -11.32338 | -45.20794 | 2026-08-07 04:46:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e8e20174-5ca3-3fca-af01-90a55085b882 | -12.55177 | -46.95364 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e311bb43-d27a-30be-8a99-0615bd1f4b26 | -11.16475 | -54.85696 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 383ffc5e-6f43-301f-acba-36409053b460 | -12.62443 | -46.89988 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 05e26f1e-b050-3def-961d-52fd9c6afd40 | -12.30841 | -49.99409 | 2026-08-07 04:46:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c00f1e09-f2b2-3727-a865-d159c9d796a3 | -13.82768 | -53.72015 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 191c535f-dd3a-3b3f-89ab-7df42fb4e87f | -14.43364 | -45.67773 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8e864315-6e08-3e38-997d-576524167077 | -16.69243 | -51.36503 | 2026-08-07 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| a99733f1-0c07-3568-ac67-dfad25790d55 | -12.58406 | -46.9054 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dcdcb3f4-f643-33f5-b2b2-a72598a376a3 | -14.42847 | -45.67376 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 37e23cbf-83c1-3836-9163-c2fef7dd6fd5 | -11.12538 | -54.90667 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f2bab5bc-abde-326e-afe1-42dbd15b38fe | -9.48958 | -57.32079 | 2026-08-07 04:46:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bb9a2acd-6785-3f3b-ad0a-2d35135865df | -11.13032 | -54.90347 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2b58848-ad53-3de4-8773-11006653f247 | -16.29095 | -48.53851 | 2026-08-07 04:46:00 | NPP-375D | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 05500bd1-453c-3b5f-bff6-32fb17498f0a | -13.62609 | -54.67824 | 2026-08-07 04:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c9352e69-e77a-3c27-83fe-9dc6cb297c00 | -14.42738 | -45.66698 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 492660c9-31da-340e-a716-6bf71eb044c2 | -14.73414 | -47.13427 | 2026-08-07 04:46:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9573df4c-ce9b-309b-9679-54998d5b93d3 | -14.4215 | -45.6808 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a6c20c34-35ed-34f8-ab90-d1949e5204b3 | -13.68786 | -51.97791 | 2026-08-07 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a176fefd-bac4-322b-9000-8d4f6b8eeca0 | -12.32792 | -53.16878 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75228894-1160-3028-aa9c-abd04f54f46b | -14.26957 | -45.2906 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 48aa5689-5d7c-3e87-a199-394693c0bab5 | -14.424 | -45.67798 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e42500a4-2810-36c4-b665-93d80d894d1a | -18.14855 | -47.98104 | 2026-08-07 04:46:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7b7dad88-b025-3e18-9a3e-f6892b2c80b8 | -11.1373 | -54.91311 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e8eccadd-c10d-365c-8072-0535e2123104 | -16.14251 | -43.55024 | 2026-08-07 04:46:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ef7f542d-5723-3b74-83ec-65ee0df53b83 | -12.51864 | -55.78205 | 2026-08-07 04:46:00 | NPP-375D | SORRISO | MATO GROSSO | Brasil | 5107925 | 51 | 33 | nan | nan | nan | Cerrado | 9.5 |
| ce85e994-96f9-38e1-88f3-1ace079a7d78 | -10.6346 | -47.48992 | 2026-08-07 04:46:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| bdd0a698-82a1-3d6d-9eba-93214dcabc05 | -12.33242 | -53.16492 | 2026-08-07 04:46:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9a83001e-83d9-38a6-9bbc-9e7cc22f31de | -14.42913 | -45.66894 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| dc9c6f76-02a1-3635-8e06-975ef1401258 | -14.3407 | -54.92796 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d62fb2c-c9dc-34fd-9f17-9c876341c53c | -11.46617 | -44.57485 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3058e980-8aab-3971-b24e-6b3852d17542 | -11.13103 | -54.8995 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de79d95d-a321-3f94-b342-4b51f2ce22d8 | -11.14493 | -44.48441 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 44.5 |
| 9405cac8-f046-3c7f-a8af-ca8d8dcc8804 | -16.49083 | -52.72292 | 2026-08-07 04:46:00 | NPP-375D | RIBEIRÃOZINHO | MATO GROSSO | Brasil | 5107198 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c0850e88-c521-33e3-bd46-3b158db6f8e4 | -13.83601 | -53.71692 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e9b6618-57d6-3ddb-b86c-1704380d0a5b | -16.68909 | -51.36444 | 2026-08-07 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e3c9e66a-dc67-3efa-a627-b4f046e02a1c | -14.42531 | -45.66837 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4deb810c-38c6-3f32-a71a-e482e85be460 | -12.58525 | -46.89741 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e5d501a2-83fe-34f4-997c-80a47e19af28 | -11.15562 | -54.85943 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e83907b-2215-3f90-8849-761d03157fd0 | -11.13245 | -54.89163 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f2c279c4-2c8a-392a-80b7-472ed4bfb33c | -15.87653 | -43.33269 | 2026-08-07 04:46:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| da0101c5-1ba7-387d-8215-5251ec9d54ea | -11.46046 | -44.56121 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 86f96e5f-924a-36af-8143-c8dbc0d04967 | -13.69199 | -51.97466 | 2026-08-07 04:46:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 069a1383-76bb-3fcf-860f-16be531c7b2e | -12.44555 | -47.80141 | 2026-08-07 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| be5ee0d8-f11b-32ff-818d-4ac0e61fe2f9 | -14.42597 | -45.66354 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b18816e7-e1ef-3692-81e5-676c064b989d | -15.0945 | -52.76487 | 2026-08-07 04:46:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 964af477-4cf5-3b96-8919-8cb7eabc1c85 | -12.44185 | -50.36053 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c637ee8c-eeeb-3c03-91bd-9db15656545f | -11.14222 | -54.90997 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 37b7011d-4877-3340-b1a4-64ea19dd1232 | -14.426 | -45.67659 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b38c4506-ba23-3a39-ab09-233ba52096c1 | -18.42791 | -45.49134 | 2026-08-07 04:46:00 | NPP-375D | MORADA NOVA DE MINAS | MINAS GERAIS | Brasil | 3143500 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 21338b2d-57a8-3973-9b3d-cf45d97d8ee6 | -12.55006 | -46.96516 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c34dc51-d2c2-330a-b929-294eebf1ee30 | -12.57412 | -46.89973 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 595ab4f4-8591-3a16-b7bc-96ad77ca30d4 | -14.42663 | -45.65871 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 47461034-90e5-3ad5-a47b-59147a5be95e | -11.15671 | -44.48623 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08d0f348-98d9-3b8d-b264-2f5d7b94fb07 | -13.78357 | -49.72496 | 2026-08-07 04:46:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e7de26e7-2e19-3e57-8db0-9c27e401e506 | -14.27737 | -45.29174 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 44741ed1-ca22-3032-b4ef-476590a7ca75 | -11.63075 | -59.01487 | 2026-08-07 04:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0b0051e-bcd0-3c77-862e-3aa3ec2a7255 | -13.93809 | -47.36007 | 2026-08-07 04:46:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 12ab8630-d264-3332-95fa-f4359116699e | -11.13309 | -54.91226 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bf9c0b3e-c5c0-3fab-bf01-cebbf675c3b4 | -12.55765 | -46.93811 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bb52d58b-d1b0-30d0-a2c2-1826be68a3c6 | -10.6091 | -52.22328 | 2026-08-07 04:46:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a8108e37-e355-3ad6-9e41-4e0e5a04312e | -14.32439 | -54.97301 | 2026-08-07 04:46:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bda93562-f915-322d-8d3a-89b8b234d804 | -11.13874 | -54.90511 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a810854-8923-396a-97dc-8d2115c849f5 | -11.15558 | -54.90839 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c312070e-c17e-3618-a482-e815f38bf6e5 | -14.27402 | -45.28895 | 2026-08-07 04:46:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| dd83336a-8548-3302-aa6d-9f765fa7c3b9 | -12.5547 | -46.95803 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a199c7e5-dd7b-3f91-ab3f-a9dbcfbd502b | -11.141 | -44.48381 | 2026-08-07 04:46:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 304960b6-e453-3b88-8bb1-3ad790fd74b9 | -18.00724 | -47.13993 | 2026-08-07 04:46:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2817e963-8c4f-31ed-a5d1-1c4fd722065f | -11.14151 | -54.91396 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 753a61db-6086-3bb5-b427-cefc93423295 | -14.30571 | -54.73257 | 2026-08-07 04:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 663c97ea-f409-3052-aa34-25d1a9e2abcc | -12.60617 | -46.94965 | 2026-08-07 04:46:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9fba255d-f3ff-3e36-80de-614cf80ea48f | -11.15141 | -54.85873 | 2026-08-07 04:46:00 | NPP-375D | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4e7af421-9d6d-3fc5-aff7-b2f125c70b7b | -13.77378 | -47.18127 | 2026-08-07 04:46:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c4d85b6e-dbfb-3e62-b565-7565c0561980 | -11.47009 | -44.57543 | 2026-08-07 04:46:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b33317da-3011-3dd9-876b-5a0dea704212 | -12.42136 | -50.54961 | 2026-08-07 04:46:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15952d50-0861-35cc-9fdc-fdd5660e51fa | -12.34906 | -48.20638 | 2026-08-07 04:46:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d5e75555-e0bd-3c75-b961-8c1b4804d727 | -10.93333 | -50.28511 | 2026-08-07 04:46:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e8264df4-3250-3dcf-b957-2d572bb5edb2 | -14.42287 | -45.67123 | 2026-08-07 04:46:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f4a87cc9-df4f-3c68-9d72-1e6573a4a13d | -16.68849 | -51.36811 | 2026-08-07 04:46:00 | NPP-375D | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README18.md)
