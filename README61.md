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

## Dados Diários - Página 61

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7ed19de9-b9ca-3601-9539-ae748c63a2bb | -15.2775 | -46.34576 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dfccd5ec-1dc4-3846-ba60-a0e93221c02d | -12.27951 | -45.01695 | 2025-10-07 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 715bfd6a-78eb-3520-9b83-9a75b95bbdb7 | -12.11772 | -45.13579 | 2025-10-07 04:38:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b3bbad13-bc09-3ff7-8185-ebc4ead4b935 | -16.10518 | -48.9381 | 2025-10-07 04:38:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 050521a4-54d3-3fc8-8c40-bc5bf64bc7b3 | -15.76349 | -47.77533 | 2025-10-07 04:38:00 | NPP-375D | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17f0cd8e-e1eb-32df-a539-f1472e11cf98 | -11.0267 | -51.15707 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 35c11236-7ba5-38cc-9bb6-303660e255e0 | -13.26379 | -48.48052 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 35625c4a-db3a-3824-b973-e7433d26362d | -14.68582 | -48.37358 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 130ff488-8210-38af-bd0c-d3d925c12a4f | -13.09598 | -48.00965 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a0d7ce58-2b7a-3dce-a22d-9e1d040d2d1b | -12.76538 | -50.49044 | 2025-10-07 04:38:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7283a48-3432-3d29-a779-80b2b564ac42 | -11.94525 | -46.45609 | 2025-10-07 04:38:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6b5231b4-cb56-3e7f-9649-90bfc23b61db | -15.07241 | -46.6371 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1bdfc63a-801a-3a0c-ab72-f655cfac171a | -14.28903 | -45.83593 | 2025-10-07 04:38:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06559499-e46e-353e-ab9c-0ac2bdb63e62 | -11.77954 | -45.13164 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b7cd99cf-1d27-356c-87ef-87da132406e5 | -14.94207 | -46.82046 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 747ba0a3-1131-3427-8518-6bc85db51757 | -13.58058 | -51.82481 | 2025-10-07 04:38:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9d8d00be-2566-3ae9-9245-a6a19fb4c94a | -10.41193 | -50.30909 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 16.5 |
| b76a4b10-3441-3d7b-a387-746aa8f111bd | -14.93077 | -46.79638 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 80abe0eb-f07d-3272-aefe-cba7d533f375 | -15.16911 | -52.77224 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3de71228-e645-3173-b274-0a90b56e753e | -10.79107 | -48.59455 | 2025-10-07 04:38:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a148716e-4b43-3a9b-ab4a-985ab2839d34 | -11.79181 | -45.10041 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a438845f-6cb6-309b-96be-a3836157c39f | -10.39556 | -50.3026 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 764b44ed-353a-39b3-8f7d-ba2fa341fb78 | -10.35824 | -57.83033 | 2025-10-07 04:38:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2752d1d6-6f84-3bc0-a0aa-92a45482d34c | -11.22184 | -47.77559 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 50e70620-57de-38c9-aa72-1cd8e0cdfd1b | -17.96101 | -44.40157 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1d961c2b-f341-3502-8aa2-bace51caa45b | -14.47124 | -44.75819 | 2025-10-07 04:38:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0cd28250-14a5-35c7-990c-214e18fbc0b0 | -13.25666 | -47.16884 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6806b5da-3440-3dee-84eb-25a304553c87 | -10.63061 | -57.61819 | 2025-10-07 04:38:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1abcde78-d734-391e-9def-f00d74ba5f71 | -13.23999 | -47.23369 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0451f5e-3fe8-365c-886f-34e82094349e | -12.9754 | -46.78347 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e71897c8-5596-37dd-b641-f4c3faaf755e | -11.15739 | -47.96152 | 2025-10-07 04:38:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 206cd60e-1f93-3321-ace4-8799699e4041 | -11.03164 | -50.92322 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 26.9 |
| 95b0b757-6293-3d50-8f8d-e3822e94b22c | -13.26533 | -48.48095 | 2025-10-07 04:38:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29829d1f-097e-360c-b576-bf1945e1b979 | -13.64825 | -47.28642 | 2025-10-07 04:38:00 | NPP-375D | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f186bf6c-1d5e-3924-af16-148614de680f | -11.87815 | -44.95149 | 2025-10-07 04:38:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 33532611-4641-3c74-b314-512c2394c6e5 | -15.88674 | -46.25127 | 2025-10-07 04:38:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d3e46f36-fef6-3c34-9be1-5a70f5a03e4c | -11.73964 | -43.29058 | 2025-10-07 04:38:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 281a5751-5ae9-3026-9783-2e4811e5fcb6 | -15.61283 | -52.56723 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f5c2a1d-60c3-3e51-a971-743ba9f0c91a | -16.54975 | -42.72896 | 2025-10-07 04:38:00 | NPP-375D | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a9dfcc80-681e-394a-bb8e-8d0f4591cbc8 | -14.90811 | -46.87068 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1d7137ea-c026-319f-a900-3c0c34cc604c | -13.28223 | -47.16486 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 656e98a0-12d1-3765-a131-2b93984dad18 | -14.82723 | -52.92949 | 2025-10-07 04:38:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1c46f21c-2ec1-33db-9ab8-9f98e55486e3 | -14.90523 | -46.84031 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 54124aae-bb9c-3f5e-af5c-0d2693891463 | -13.53743 | -42.99908 | 2025-10-07 04:38:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 39.3 |
| 2aa9c495-3614-38c6-b2bd-558cf93db3bf | -12.06422 | -51.2092 | 2025-10-07 04:38:00 | NPP-375D | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc167220-eb6c-3cd8-9e92-ab540a3a0244 | -13.33648 | -47.75768 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 6320e884-5f85-3b30-93cf-4a7f9e79c875 | -14.76638 | -46.05025 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0ae86d35-cd9c-3fa8-92e1-ba6077c7f42e | -16.27958 | -50.98412 | 2025-10-07 04:38:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ea4058c9-5704-3f8f-a775-e531c79f2b89 | -15.98052 | -50.84721 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5ac80efc-539b-388c-9a92-d39005bf267c | -15.39571 | -48.00259 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4c7af57-3ef0-3aa8-9031-98e0b9a57c7e | -10.39097 | -50.30937 | 2025-10-07 04:38:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 6c95dd14-c833-3826-9e3c-a36259ae5bfe | -13.24027 | -47.7966 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c072dae-7ad7-3b72-b860-8f654ae99368 | -18.29011 | -45.41321 | 2025-10-07 04:38:00 | NPP-375D | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 43466405-8526-3a47-b1c6-421276bfe2ac | -15.96438 | -50.84077 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e34b8d76-cb7d-3d73-8b3d-3f3c0f11b786 | -12.25503 | -47.85324 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 096e51a7-013a-3d79-9e13-4a61447c0d19 | -10.58018 | -51.58628 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 649758cd-edd9-33f4-ba66-99036c26668c | -10.85467 | -51.03811 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d2543448-8220-343a-8e87-7a03618d4fa7 | -13.71748 | -48.07101 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7b17ae6-f05d-3c02-8cff-98b617d5fe41 | -13.26825 | -47.7927 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a40f4bef-cbf8-3e2a-87d8-23f70c73dc92 | -17.95619 | -44.405 | 2025-10-07 04:38:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8e65835a-0039-36d7-86e0-c4a584d67207 | -15.22155 | -56.77622 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| c18f90d4-4b4b-3244-bde2-edec5665c3e7 | -14.76278 | -46.02166 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4a481c30-7af8-3953-945f-f229eacf503e | -15.17224 | -52.76133 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7372bfe9-9009-3c92-b694-896e6f0eaef9 | -13.37832 | -48.03439 | 2025-10-07 04:38:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 994a9ce1-1728-3348-81c7-bfd5b4d4e683 | -10.94269 | -49.47852 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 931630b3-2757-33f0-8e2c-321193219451 | -15.6016 | -52.56949 | 2025-10-07 04:38:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 92c0c33c-12c9-3394-8c4f-79a35de2ccf1 | -14.71988 | -48.35606 | 2025-10-07 04:38:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09508760-c4c2-3dbe-b17b-8a8f28ee324f | -15.27453 | -44.13159 | 2025-10-07 04:38:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f66147cd-9bff-39a7-9073-f7f49efb86df | -15.2702 | -48.05811 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 93407447-a048-3878-ae1e-87fc62e00d11 | -14.53728 | -46.63756 | 2025-10-07 04:38:00 | NPP-375D | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa55c896-d9f9-3efd-9022-753ebb3b9d8c | -17.54414 | -46.7626 | 2025-10-07 04:38:00 | NPP-375D | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 55e72db9-a16c-315d-8ed9-6c299e381a1d | -12.95175 | -46.82082 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd08e46f-99d1-37fe-bd0b-431fbab15700 | -10.94122 | -51.1713 | 2025-10-07 04:38:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ad4719d6-aad0-3bdc-9c4f-3bf0b0cd7697 | -13.05048 | -47.89747 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7e6dcead-6a11-34ee-850d-e314cf6522d1 | -15.38969 | -48.00656 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b2219e8c-0e44-3be3-8032-35b021671768 | -16.34464 | -48.12907 | 2025-10-07 04:38:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f140de6-4fb3-3d79-8dcd-79ab1add8629 | -15.20955 | -48.25079 | 2025-10-07 04:38:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0899560b-206f-31ab-8d54-b39a9b818587 | -13.71352 | -48.07419 | 2025-10-07 04:38:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3fd0e07f-0992-3ade-9bc2-e8e369cb8cad | -11.22522 | -47.7761 | 2025-10-07 04:38:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f62074c6-8ac3-31f7-bab0-350a7f7ec440 | -14.74281 | -46.02781 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f78a02e0-4e8d-335a-a91c-223faf5db067 | -10.3949 | -51.58944 | 2025-10-07 04:38:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c4482d0f-0544-3813-acdf-27c60b7e4092 | -15.55758 | -46.82656 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 3cc1ff1b-7f44-34bd-b48c-29a950d773e4 | -16.0009 | -50.95521 | 2025-10-07 04:38:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3cab1aec-9e96-3cac-b9e8-e69f83020587 | -13.29157 | -47.77708 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| efd9a80f-baaa-3790-896e-c4c17eb8ecf1 | -12.18349 | -47.77481 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 049e8420-dc2e-3bcd-8f5d-55c2b2cbd80a | -14.9164 | -46.81981 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 555c0110-fae4-3501-9aa4-0bfc9e9258d9 | -13.02598 | -51.03184 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb62c8b1-a184-3a57-860d-26968a8ea7af | -15.55725 | -46.82896 | 2025-10-07 04:38:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 23568c73-cb36-3f72-8fe8-11878e86d27c | -12.93826 | -46.79013 | 2025-10-07 04:38:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f96fec84-e70d-3093-81a2-d6dabd9babd1 | -14.75221 | -46.01531 | 2025-10-07 04:38:00 | NPP-375D | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 436871ab-8620-3634-bc36-408ce9a05aad | -12.61146 | -44.75005 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 094c5f48-e4e9-3bb0-8fc4-e8ddf6f3fe74 | -15.19808 | -56.82162 | 2025-10-07 04:38:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c72d23d6-92d9-3d8c-bf55-5972bcfa99f4 | -10.99752 | -49.57819 | 2025-10-07 04:38:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25b92cbf-14d4-3f3b-a47d-ca167dac68c5 | -14.91435 | -51.4066 | 2025-10-07 04:38:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 81ce7526-60be-3282-b75b-c3e5e85763f0 | -15.59351 | -47.26515 | 2025-10-07 04:38:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cc1be2c0-79f1-3ce8-a088-0049096ecd14 | -12.61759 | -44.75762 | 2025-10-07 04:38:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 50e81b04-b0fc-3eff-9bec-3ea244514b1a | -12.57798 | -52.20185 | 2025-10-07 04:38:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bebaacf-1817-3c95-9b32-9d1c2520008a | -13.26828 | -47.16265 | 2025-10-07 04:38:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2a8d26e0-8623-32b5-852c-da1d0c0093e2 | -13.0766 | -47.8858 | 2025-10-07 04:38:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c1b1aa5e-a382-3a86-b5c5-9247f5d5aebc | -14.91964 | -46.8173 | 2025-10-07 04:38:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README62.md)
