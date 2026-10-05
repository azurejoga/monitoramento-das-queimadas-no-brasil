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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 07fcf95c-db92-38ba-9c5f-75baf6cfe0ad | -12.86779 | -39.92966 | 2026-10-05 15:33:00 | NPP-375 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 19.4 |
| 1250af80-ee12-316a-af53-5e82300a744b | -6.61928 | -37.88901 | 2026-10-05 15:33:00 | NPP-375 | LAGOA | PARAÍBA | Brasil | 2508109 | 25 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 522d036c-219d-3d1d-ae47-fff0e546b36d | -6.22536 | -38.50677 | 2026-10-05 15:33:00 | NPP-375 | SÃO MIGUEL | RIO GRANDE DO NORTE | Brasil | 2412500 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 9e95377d-d179-3436-8226-570ab10d029f | -8.00177 | -35.0899 | 2026-10-05 15:33:00 | NPP-375 | SÃO LOURENÇO DA MATA | PERNAMBUCO | Brasil | 2613701 | 26 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| b8685cb1-916b-3048-8e30-9b94bb5f8ae6 | -6.85678 | -38.67945 | 2026-10-05 15:33:00 | NPP-375 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 23.8 |
| b797c35f-a0e2-3b62-bb53-c494a4ded820 | -10.1341 | -39.19328 | 2026-10-05 15:33:00 | NPP-375 | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a46ac209-ba4a-3aa2-9d0c-1d37b71fba75 | -3.17095 | -41.40841 | 2026-10-05 15:35:00 | NPP-375 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e5f8cedb-e59b-3a45-85eb-5f2b6189bc44 | -3.57616 | -41.24197 | 2026-10-05 15:35:00 | NPP-375 | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| da8272ff-ff00-3556-8bba-8f89ebc3d14b | -5.9086 | -38.05133 | 2026-10-05 15:35:00 | NPP-375 | TABOLEIRO GRANDE | RIO GRANDE DO NORTE | Brasil | 2413805 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 3fb4fd36-fca7-3198-a350-a9548c6740e5 | -5.98945 | -40.91072 | 2026-10-05 15:35:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 3ce51056-9076-3f5a-89e7-9b1c28222c85 | -3.28608 | -42.25992 | 2026-10-05 15:35:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 98b1beac-649d-3fed-8e03-f56d5aa95be7 | -5.95701 | -41.3423 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| c1afb320-af4a-31db-be76-ecce7cf458f9 | -5.71639 | -40.12653 | 2026-10-05 15:35:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 83f2858b-df97-3ff7-b22f-4936bc5838ad | -4.56818 | -39.5817 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 79.1 |
| e99bde63-e6b4-338a-889b-76f39dae5742 | -3.8569 | -38.52071 | 2026-10-05 15:35:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 37d3dbae-c4c2-3fe2-9770-76da5381b938 | -4.84389 | -41.81788 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 5561ca48-eb59-3fb2-91b2-ad672bca24c2 | -3.10422 | -41.83211 | 2026-10-05 15:35:00 | NPP-375 | BURITI DOS LOPES | PIAUÍ | Brasil | 2202000 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 0c6129cf-994b-3d5b-a639-249e9dd28124 | -4.56682 | -39.58473 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 9bd577b2-10c4-3d0a-a73c-f0d037a30cf2 | -6.59808 | -41.57998 | 2026-10-05 15:35:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 14a4756e-0e37-3e6d-b347-4183586d7b37 | -4.35256 | -40.25621 | 2026-10-05 15:35:00 | NPP-375 | SANTA QUITÉRIA | CEARÁ | Brasil | 2312205 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e3c8c144-77a1-399e-a049-e0128f6c70c9 | -4.08296 | -39.01707 | 2026-10-05 15:35:00 | NPP-375 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 67107ece-5f4b-3ebd-ba6d-ba32e8697a12 | -4.91195 | -39.90076 | 2026-10-05 15:35:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 42.2 |
| 8822f5ed-0f1e-37c8-9c36-988098de7a90 | -4.85327 | -42.19868 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| ee5368c1-a7e9-36aa-9dde-30dff4fe0577 | -3.20974 | -42.44257 | 2026-10-05 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 38e92d0f-c6d4-3cc1-ae20-99d08a1cec6b | -5.47237 | -41.23083 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6409b31f-043d-3efc-afe2-c39001032052 | -3.89224 | -38.6447 | 2026-10-05 15:35:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 21d045b4-05f2-32de-9a9c-694baca68b9e | -4.80152 | -42.13634 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| 27f97a28-7eb7-3176-8ad9-08ff1c5bfde0 | -5.19397 | -37.36435 | 2026-10-05 15:35:00 | NPP-375 | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5191ed33-6c5c-3b98-bb6d-431931b282d2 | -3.93248 | -40.73073 | 2026-10-05 15:35:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 12.1 |
| 005ed84f-e6f7-3668-8210-45c3661c90ca | -5.95289 | -41.31048 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 24d47e76-d488-3329-8c7d-a1eaa9441de1 | -3.93968 | -40.73518 | 2026-10-05 15:35:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 7.3 |
| c0c1c4fe-c4db-3936-9e6c-edae784626fd | -6.59634 | -41.56673 | 2026-10-05 15:35:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 49.7 |
| 4bca63f2-2615-3f52-b3c1-cbf175b127f3 | -5.95046 | -41.34539 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 73ddc5d1-1365-33ae-87ec-4a6e75a374df | -4.91072 | -41.74146 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| e3e15bcd-b53f-3627-8896-42cd83c521fe | -5.68085 | -37.78599 | 2026-10-05 15:35:00 | NPP-375 | APODI | RIO GRANDE DO NORTE | Brasil | 2401008 | 24 | 33 | nan | nan | nan | Caatinga | 3.9 |
| e62a41e2-34a7-3e59-896f-3731ce7ee010 | -4.80243 | -42.14315 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| eb0122b0-e64b-317d-8b06-3c7c333fc506 | -3.93894 | -40.72997 | 2026-10-05 15:35:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| e4aff67b-41ef-33fd-96a6-58595a06678f | -5.45241 | -38.47178 | 2026-10-05 15:35:00 | NPP-375 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 82f855f4-ce38-37a5-9049-a7ab4da74615 | -4.91264 | -39.90565 | 2026-10-05 15:35:00 | NPP-375 | BOA VIAGEM | CEARÁ | Brasil | 2302404 | 23 | 33 | nan | nan | nan | Caatinga | 47.3 |
| e2138ede-3f18-38b9-893d-b57244c5783b | -5.27317 | -39.36997 | 2026-10-05 15:35:00 | NPP-375 | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2e2b0abd-2d4d-3243-9700-57fd1128bd18 | -6.60421 | -41.57244 | 2026-10-05 15:35:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 81070884-6959-3bdb-94ba-79ef0a6f4088 | -3.76901 | -39.84636 | 2026-10-05 15:35:00 | NPP-375 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 7.4 |
| a7dace8c-2286-3d9b-80b9-6916be3cc012 | -5.35443 | -38.2464 | 2026-10-05 15:35:00 | NPP-375 | SÃO JOÃO DO JAGUARIBE | CEARÁ | Brasil | 2312502 | 23 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c83d4579-bfe9-361e-9790-3cf7e0788574 | -5.47036 | -41.23302 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 917d2835-2c77-3220-b758-c49862953cf2 | -5.9828 | -40.91187 | 2026-10-05 15:35:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 0206defa-c24e-37ac-9553-1d42cbfba3c0 | -4.95899 | -40.55959 | 2026-10-05 15:35:00 | NPP-375 | TAMBORIL | CEARÁ | Brasil | 2313203 | 23 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 4ddd1125-94ee-337d-8117-3eaa3237faca | -4.84298 | -41.81129 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 26.9 |
| 367efcac-6a8a-3fc1-9429-69573a6d7d32 | -4.91016 | -41.73644 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 30.1 |
| 4908aac1-f68d-3433-8121-672ad55ed9aa | -4.56936 | -39.59034 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 58.8 |
| e302506f-756e-3945-a7e8-dd83a7d68334 | -5.71225 | -40.12402 | 2026-10-05 15:35:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 9207d663-82be-35df-b482-be5e41e4f832 | -5.44672 | -38.47262 | 2026-10-05 15:35:00 | NPP-375 | JAGUARIBARA | CEARÁ | Brasil | 2306801 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 15c5966a-7a3f-30dc-a913-967119ef0d6e | -4.90984 | -41.73505 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 6e2e7b82-6641-3bfd-b656-4e3c9b845982 | -3.55922 | -39.91309 | 2026-10-05 15:35:00 | NPP-375 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 0aa501e8-0a16-3fb8-9e4d-3f6628c76f1d | -4.14632 | -38.59243 | 2026-10-05 15:35:00 | NPP-375 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b44431fb-1e27-311f-8f69-b02c1f7ae8bb | -3.93323 | -40.73597 | 2026-10-05 15:35:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 14.6 |
| a43b5851-5dca-3d45-ae8c-fae85218e2e7 | -4.81043 | -42.14902 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| b6c27ba5-809f-3856-8401-ee48f780b404 | -4.80767 | -42.15472 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 106.7 |
| 00d5a76c-0a08-3ddb-94c3-9477b57a8af2 | -5.95131 | -41.35165 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b108597b-6485-33d2-8a63-bc41d33b0d30 | -3.93819 | -40.72472 | 2026-10-05 15:35:00 | NPP-375 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| b8ee1f3d-6d78-33a1-b422-fabc67242ef3 | -4.57291 | -39.58423 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 72.4 |
| 9dea27e6-07d7-318d-9516-6804d771bba7 | -4.56743 | -39.58899 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 57.5 |
| 182fcc62-0e86-3160-940d-3ed6cd81a9ce | -6.6061 | -42.26409 | 2026-10-05 15:35:00 | NPP-375 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 91acc3b6-8055-3855-aa4c-ea942bf9918f | -3.53695 | -39.88834 | 2026-10-05 15:35:00 | NPP-375 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 3b294f2b-4af7-3e54-9f51-b0cb27d54bf1 | -5.94362 | -41.34643 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0abc6645-2508-3902-b2a5-a57dd0abb473 | -3.20714 | -42.44746 | 2026-10-05 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| c8bbbf27-d0c4-3664-85fc-cdaa20a8da3f | -3.74155 | -39.54595 | 2026-10-05 15:35:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 0b9ae92d-c85c-3c4b-b011-db79540ef0e1 | -3.61839 | -40.44263 | 2026-10-05 15:35:00 | NPP-375 | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 5f2ce165-440e-3602-822d-6b5ebd9eaa2f | -4.56876 | -39.58598 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 79.1 |
| aad3cd64-c6a5-3b07-8cb5-bd55a0faa978 | -5.95729 | -41.34428 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 5302117a-0359-3064-bf87-f69e2f15c0a7 | -3.85745 | -38.52442 | 2026-10-05 15:35:00 | NPP-375 | FORTALEZA | CEARÁ | Brasil | 2304400 | 23 | 33 | nan | nan | nan | Caatinga | 6.0 |
| cddfecf8-e6a1-3bd1-9612-8ff838954a58 | -3.65291 | -39.43741 | 2026-10-05 15:35:00 | NPP-375 | TURURU | CEARÁ | Brasil | 2313559 | 23 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 1d7a28f7-3b3a-3bc6-9a5d-f396ac2df571 | -3.88891 | -38.4678 | 2026-10-05 15:35:00 | NPP-375 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 56e0dca7-b60c-3cae-92a3-35a24b1bcc65 | -3.90871 | -38.66098 | 2026-10-05 15:35:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 12c57e31-418b-3df9-b2d8-416a782a182f | -3.166 | -41.40576 | 2026-10-05 15:35:00 | NPP-375 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 7c20b932-1cc4-34c7-a2cf-e4360e9ea1ed | -3.53629 | -39.88384 | 2026-10-05 15:35:00 | NPP-375 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fb895a5f-8a02-39b1-a455-df0f269ae55b | -3.17014 | -41.40275 | 2026-10-05 15:35:00 | NPP-375 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 18.8 |
| 68ada64a-8f0c-3ddf-8000-108ca0fbdefb | -5.98358 | -40.91766 | 2026-10-05 15:35:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 6d2cdc56-4b95-3bb8-b83e-9c4fcedb8ee6 | -3.21074 | -42.44927 | 2026-10-05 15:35:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| b9a738f9-69bd-3b4d-95db-6ea46ffc8ca8 | -4.80575 | -42.14109 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 388.8 |
| 74513f10-9f15-34aa-8e9f-17ff0446bbb9 | -4.00058 | -38.35413 | 2026-10-05 15:35:00 | NPP-375 | AQUIRAZ | CEARÁ | Brasil | 2301000 | 23 | 33 | nan | nan | nan | Caatinga | 3.7 |
| d3bb10e9-950d-3524-a4fd-7398036f55a3 | -6.59721 | -41.57338 | 2026-10-05 15:35:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 98c62328-d028-3989-b418-97d441912f2c | -5.71853 | -40.12262 | 2026-10-05 15:35:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a306851-21a1-3313-8a65-93ce8bc9cde8 | -3.9119 | -38.66106 | 2026-10-05 15:35:00 | NPP-375 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5a56b033-779c-3263-965b-58693182cd97 | -4.80951 | -42.14219 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 88.4 |
| e961646b-10ae-3e17-b14a-8ce786ab7526 | -3.2875 | -42.26146 | 2026-10-05 15:35:00 | NPP-375 | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0ce71aa0-cc30-3d75-87b3-37446dfde6a7 | -5.95296 | -41.31245 | 2026-10-05 15:35:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 31f60488-c445-350b-b2b4-8bb023eebdfa | -4.08249 | -39.01715 | 2026-10-05 15:35:00 | NPP-375 | CARIDADE | CEARÁ | Brasil | 2303006 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 941c1c2e-fb07-3395-9b65-b1ffbb57c2dd | -4.49207 | -39.36187 | 2026-10-05 15:35:00 | NPP-375 | CANINDÉ | CEARÁ | Brasil | 2302800 | 23 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 12f5418c-d6bf-3ef7-bc80-e3c7eedc8044 | -3.17264 | -41.40487 | 2026-10-05 15:35:00 | NPP-375 | LUÍS CORREIA | PIAUÍ | Brasil | 2205706 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 9deed2e3-6f57-35f5-a3cc-94a312a6a767 | -4.14577 | -38.58861 | 2026-10-05 15:35:00 | NPP-375 | PACAJUS | CEARÁ | Brasil | 2309607 | 23 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 72b85047-06ae-3990-8ebe-cfbf568f0981 | -4.91108 | -41.74284 | 2026-10-05 15:35:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| a66895d8-a266-3bb3-bbbb-42fda89b7022 | -3.77381 | -39.84471 | 2026-10-05 15:35:00 | NPP-375 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 9a7aef4e-b6d9-3377-a846-fbb5cf811d0a | -3.56003 | -39.91187 | 2026-10-05 15:35:00 | NPP-375 | MIRAÍMA | CEARÁ | Brasil | 2308377 | 23 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7e667fab-9b92-3802-bfec-b9d7016b337c | -4.80425 | -42.15681 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| f5d57512-1e6e-3090-8323-5046ea8b3098 | -3.88715 | -38.4673 | 2026-10-05 15:35:00 | NPP-375 | EUSÉBIO | CEARÁ | Brasil | 2304285 | 23 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 01d86a6e-35ee-349e-947e-2ca3b99f1458 | -4.80334 | -42.14997 | 2026-10-05 15:35:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 96.4 |
| 821ab22b-3148-3a15-be39-2507706a8ffb | -4.57355 | -39.58865 | 2026-10-05 15:35:00 | NPP-375 | ITATIRA | CEARÁ | Brasil | 2306603 | 23 | 33 | nan | nan | nan | Caatinga | 57.5 |
| fd3610b5-2dc6-3dae-8ca9-0bcd6366bce4 | -3.76774 | -39.84558 | 2026-10-05 15:35:00 | NPP-375 | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 76fad3e3-0b12-3db9-a768-35ee9f5f612b | -9.0429 | -65.4361 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 07f8f6ad-37ea-3f10-83a0-36ec6f89bfdf | -9.1335 | -65.8813 | 2026-10-05 15:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |


[Clique aqui para ver as próximas entradas](README69.md)
