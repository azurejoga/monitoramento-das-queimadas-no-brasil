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
| 2e40297c-25cc-3e4d-8703-1ac7adb97399 | 2.67485 | -60.24624 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e6f86da9-e033-3484-830d-d7de2f13c550 | 1.92582 | -60.27587 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 55d38f2f-3b69-3d18-aed6-9c7456cd9cfd | 2.72295 | -61.35065 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6d597a65-d270-3cb9-84c6-2950148c5639 | 2.67864 | -60.2411 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b07d9c94-0b2f-3b53-ae50-5f56c337f0d9 | 3.85075 | -61.27045 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e1bde199-a6ba-35a0-9763-0b61b2b6268d | 2.68243 | -60.23598 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d5e4f3df-01c9-3371-b32f-9a200696b931 | 1.92207 | -60.28102 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ea3b6ac5-8fd9-323c-8b3f-891e6d3fa9a8 | 2.70763 | -61.34769 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5f141aae-05fd-3634-b917-c08a13253ccb | 1.91696 | -60.27737 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 66278937-a1ae-3667-8555-582fb7a5e6e5 | 1.90875 | -60.28308 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3efcf80a-f53b-35e8-a155-389c2849a813 | 2.67933 | -60.24555 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 51686f32-4fb5-384b-964f-f14cc6e97254 | 2.11662 | -59.85274 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 158ac367-922b-31c9-8a84-e81a1735bf3e | 1.94629 | -60.9106 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 50e3bc62-22aa-36ad-a8d5-0d9689a36f41 | 2.71892 | -61.35669 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ac0feaf1-62eb-3024-b6f6-b68ff4be21af | 2.7278 | -61.3499 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| da2184b4-fcee-3a68-abae-672545e3a3f9 | 3.92437 | -61.29272 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9878dae4-f795-3eca-a8d8-1749ff77f3a3 | 2.71972 | -61.36195 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 10a91da0-4505-30e1-8c58-3f686ea49708 | 1.94856 | -60.90846 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 1103da8d-4d06-3f63-808f-92e2ce49357b | 1.76288 | -60.57992 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1b0f6bb8-e395-3ec1-91ae-10a0c3675fce | 1.94391 | -60.90914 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b055239c-fbb9-32a3-b9fe-f22614c7e623 | 2.70441 | -61.35913 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b6a30ecb-9015-3c5c-8ecb-b30ed94bbf6e | 2.71811 | -61.35141 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 8c071332-4f5a-3253-9e35-77da3926e9e4 | 2.70359 | -61.35377 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1be3de6e-d31d-3d67-a867-500c5e939fe2 | 2.7286 | -61.35517 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6c5ad3fa-e786-3a93-82ea-5042ae2440c6 | 3.92929 | -61.29199 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f53836f4-ccfd-3cc6-8461-4ad148670e9e | 1.94929 | -60.91329 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 524d9e89-b879-31b1-926d-ab1ce4164340 | 1.91319 | -60.28239 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ccad3ba8-9a8e-3042-bab0-396294b94219 | 2.67416 | -60.2418 | 2026-03-25 05:08:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd3cb912-1f1e-3be5-bcf6-fc6a9552dfcf | 1.92139 | -60.27663 | 2026-03-25 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5c0bc11a-308e-3f88-a84e-3cfdf64e6dad | 1.83269 | -60.85023 | 2026-03-25 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 86d8c449-5eef-366e-a6e5-b1e55e7ade09 | 3.93421 | -61.29126 | 2026-03-25 05:08:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4c4995f7-d153-37f0-afd3-0672d13d7ed2 | 2.72942 | -61.36045 | 2026-03-25 05:08:00 | NPP-375D | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| adcf16c7-369d-3627-951f-d2f76691b826 | 3.71228 | -60.36639 | 2026-03-25 05:08:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5ce93421-5ab1-3d26-ba6c-0ed561456666 | 0.82868 | -59.36041 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| abd68100-ffe9-38e4-a6bb-67ab46238d73 | 0.81348 | -59.34413 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 266c1214-0bb2-3bcd-9480-bbf753e90ad0 | 0.81752 | -59.36956 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| e54fd682-3726-3ae7-a004-f0729378621a | 0.82516 | -59.36468 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a0729262-1afe-3af1-807e-c0f27dd9d920 | -1.77176 | -54.02598 | 2026-03-25 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d939611-3d8c-32c1-a80e-25200cbb4faa | 0.81054 | -59.35204 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 311d8df3-d076-35a0-a48f-403519763c90 | 0.81873 | -59.35075 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3d2144d7-de0c-3636-b142-de66e5e3602c | -3.48873 | -52.5741 | 2026-03-25 05:10:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 627cb8be-eb3a-3073-ac15-295219c76f9c | 0.74374 | -59.61242 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| df5003bd-eaa4-32f1-b1f7-ac2073e32f11 | -5.97822 | -50.60593 | 2026-03-25 05:10:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| b8d518b1-bdc4-315f-8e1f-2ac0fa720ea5 | 0.82163 | -59.36894 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5273f514-10b9-377a-bdd1-95d4de66e92e | 0.98469 | -59.38173 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9e901f3d-7014-379b-8f7e-2e17d14f8a91 | 0.80932 | -59.37085 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f85b7879-3b0b-316d-ad8e-0198745271be | 0.81464 | -59.35139 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| 02f904ef-c6b4-3ef6-bc44-8045e686b0a9 | 0.81112 | -59.35567 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 6e2c4c83-f2e8-3d4f-95fa-84dfe31ba1f0 | -1.76843 | -54.02546 | 2026-03-25 05:10:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5d988fdb-bf84-35db-81d3-b6ce040dc73f | 0.80817 | -59.36359 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 28369fdf-c524-3652-869c-0f9817954f75 | 0.81637 | -59.36229 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 392677ec-2208-3f5f-a53a-b0eebcd2ade7 | 0.82105 | -59.36529 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 8f27e84e-0dbd-3c3b-92db-21c52cd2aafa | -2.82955 | -57.69551 | 2026-03-25 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 788fd22b-bf5a-38c3-b583-f5ba85f4c9d4 | 0.81816 | -59.34711 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 109c173a-13a1-3f52-915b-6ef369ffb498 | -3.6634 | -48.40426 | 2026-03-25 05:10:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 08633fa6-720b-3831-b510-f5563d8a5d8d | 0.82926 | -59.36406 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 96c6be11-0e65-32d1-b0ca-f06fd9f994b0 | 0.81521 | -59.35502 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| ae46b2c1-9b3e-3bbd-8870-510b91e6cc45 | 0.98057 | -59.38237 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 409781f0-9086-366f-a5f2-18775a6fc267 | 0.81989 | -59.35801 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 9419d687-7dae-3434-8559-17a98c5dd499 | -1.48512 | -55.28257 | 2026-03-25 05:10:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| edb76040-7a0c-35e5-b42b-3b39f9b58102 | 0.82283 | -59.35011 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 9b40653d-0598-3645-a372-44d6f4381b10 | 0.81284 | -59.36657 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 9f857c6b-bf84-34e8-9345-1c0c7a06e4ff | -2.8331 | -57.69608 | 2026-03-25 05:10:00 | NPP-375D | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5573f5ec-5c2e-387a-9885-0e8069e91842 | 0.814 | -59.37383 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3f4ae967-95af-331d-ac99-9d2a9dd514b2 | 0.67449 | -59.52349 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5ddec103-ecd0-330d-95b9-44c4de0a71e4 | 1.08799 | -59.24615 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb1c227c-ead2-38af-86ce-3a898a65c0ab | 0.81695 | -59.36593 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 03bdd850-b821-3e35-a7a4-5e4a076995d9 | 0.82574 | -59.36832 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47b5afc5-aff2-3432-978a-7b1936dd52c5 | 0.82047 | -59.36164 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 6c16f5c2-a127-3aff-9640-02ea66f29e25 | 0.98526 | -59.3854 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1960220c-98ab-3608-a653-e7dd30de94ef | -3.18433 | -52.88286 | 2026-03-25 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b5bf8ea7-3ce7-3ca0-9148-a04e7e9182b9 | 0.80996 | -59.34841 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 21.3 |
| eb8ce279-e999-3089-b754-26c2aa08c8d7 | -3.1409 | -49.21815 | 2026-03-25 05:10:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 13607eba-2b33-35c4-85a2-eb188f320418 | 0.80874 | -59.36722 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4ec9187e-4fd5-35b9-8e7b-f418507c07aa | -3.18779 | -52.8834 | 2026-03-25 05:10:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5685aea6-d4cd-373e-9ba3-b6e11d4934d4 | 0.80939 | -59.34478 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 6.9 |
| ce0e9516-c677-346a-a1ff-840845b91885 | 0.81169 | -59.3593 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 5ca998af-4959-3616-856e-44443f901a2a | 0.83279 | -59.35979 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0d7a9691-b275-36c5-afaf-47e6c63079bf | 0.81342 | -59.3702 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 5825907c-748e-326a-8e14-4e8629202e2f | -2.25959 | -47.8605 | 2026-03-25 05:10:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ab796f5-e89a-3d22-bc89-b0f8b768aab1 | 0.82457 | -59.36102 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9406978b-ff8c-3a47-9658-93149c8beb26 | 0.81227 | -59.36294 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 45cf1a6d-da63-3baa-8266-9ad193045ab2 | -1.48567 | -55.27911 | 2026-03-25 05:10:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c223ec9c-b69a-335d-9a65-6e83dadf837b | 0.81758 | -59.34349 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2a3375ca-de3e-3851-8e74-46cd19a15c80 | 0.81931 | -59.35437 | 2026-03-25 05:10:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 9.1 |
| bdd4e3e9-eee9-3398-b61a-eb15f79ab262 | -12.71175 | -47.69426 | 2026-03-25 05:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9001b237-b80f-32f4-b7fc-9648b508b120 | -13.46522 | -54.34471 | 2026-03-25 05:12:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| f69dde86-ffe7-3e8f-bcb6-b2f8442a4391 | -13.11384 | -57.74052 | 2026-03-25 05:12:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.1 |
| f59cafe4-2c73-353b-81c3-2449559871f5 | -11.34687 | -61.94919 | 2026-03-25 05:12:00 | NPP-375D | CASTANHEIRAS | RONDÔNIA | Brasil | 1100908 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 51c92f1e-6dde-369a-8818-33adc89626de | -10.91814 | -57.92008 | 2026-03-25 05:12:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ccc2a2d9-6f30-302c-9dda-d8734397dccc | -17.69359 | -48.844 | 2026-03-25 05:14:00 | NPP-375D | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b9563640-d0bc-35a3-b6f2-ca24ed4c8a93 | -17.10599 | -48.56726 | 2026-03-25 05:14:00 | NPP-375D | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4d1b029a-f843-391e-b14b-fbc31bcd21e3 | -17.50032 | -45.57401 | 2026-03-25 05:14:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a69a58e-e712-30fa-83a4-e0318ae48365 | -14.2102 | -53.81667 | 2026-03-25 05:14:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad3eda1a-f56e-31e0-bdd2-217b3f8078ea | -14.9566 | -49.76842 | 2026-03-25 05:14:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| c6b55fb7-bdbe-3ba4-bbeb-367663d5d145 | -15.75637 | -48.48077 | 2026-03-25 05:14:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a1e593a-1e35-3ce1-af99-26b30cc33db5 | -17.4653 | -55.20171 | 2026-03-25 05:14:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 30dc46e3-7e8e-3315-aa3e-f69f12fd11c5 | -18.67801 | -49.2241 | 2026-03-25 05:14:00 | NPP-375D | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| fb45f105-178b-3cee-855e-3a2736788fe4 | -20.34849 | -46.77197 | 2026-03-25 05:14:00 | NPP-375D | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08ffbcbd-3a4a-3542-ba1c-bfe953182aa5 | -22.06625 | -46.85196 | 2026-03-25 05:14:00 | NPP-375D | SÃO JOÃO DA BOA VISTA | SÃO PAULO | Brasil | 3549102 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
