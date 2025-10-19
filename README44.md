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

## Dados Diários - Página 44

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d8c8d78-32f1-3535-93ba-22b6ca7ced74 | -10.43155 | -48.05108 | 2025-10-19 04:32:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 58801c5a-859f-3808-bb82-7e4632876aff | -5.46622 | -44.89293 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bb00dd88-cb63-38f8-b476-99edcaa18983 | -7.34633 | -48.59356 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a4229ed3-c32d-3656-8448-8b6cebc00d84 | -11.63668 | -44.08806 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32fc306b-1d84-3c01-9e32-137101da9545 | -12.69361 | -46.95654 | 2025-10-19 04:32:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ec4f6b3d-8cd0-3163-9100-0835de800007 | -11.77762 | -47.55434 | 2025-10-19 04:32:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 154f719c-9151-3149-8ab9-e1e3c74a2df7 | -11.89845 | -45.43904 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0b766598-c096-3890-94dc-f5f213a3a128 | -11.97757 | -46.92874 | 2025-10-19 04:32:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ec11cfd-7e48-3215-9c0c-6fcfce39b325 | -5.19699 | -46.17381 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b9e983c-e3a6-3b89-b603-fda6931fd32f | -7.0237 | -46.80342 | 2025-10-19 04:32:00 | NOAA-20 | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ad4c78d-e2fa-3a39-8d45-f7992c9c6dc1 | -10.22811 | -44.06437 | 2025-10-19 04:32:00 | NOAA-20 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7f88b6c1-8e5f-3085-b9ad-aa1c53d8ca34 | -8.3596 | -46.20758 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d836f323-1230-3200-a026-2d60245f61cd | -10.88723 | -46.07595 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cb47904d-3b05-36e9-ad69-5dcef1c0928b | -8.24225 | -43.99278 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 507a698c-ff95-3e80-99c3-77390f89901f | -8.42903 | -44.13951 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9387fbd2-6e1c-35f2-9074-1315ee49cb79 | -9.22375 | -61.83061 | 2025-10-19 04:32:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 5cea9387-3e17-3b55-b63b-cdb0d0bb1f3e | -9.75898 | -43.95438 | 2025-10-19 04:32:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0464280a-719f-3a06-951c-8ca2c73ba61f | -4.63142 | -50.41095 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeeecb2a-1558-3bc0-8962-727575e3b31e | -8.45679 | -50.35555 | 2025-10-19 04:32:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b05bf414-de7f-3d88-825b-a6e5cd5fb2ac | -12.45818 | -45.4415 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 12052d58-2772-356c-894c-4402c119ee39 | -9.93208 | -47.66196 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 547b8970-9894-3447-b2a1-17d0331af9e0 | -5.75557 | -44.00045 | 2025-10-19 04:32:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 61d72a73-e5be-30c1-9848-d54413dde109 | -6.05682 | -49.38798 | 2025-10-19 04:32:00 | NOAA-20 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6c865c3e-62f2-37ee-904a-697ba103c990 | -8.89862 | -49.00109 | 2025-10-19 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eed47025-6aae-3724-8784-2970e314aa61 | -7.27479 | -42.30823 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 81bd3606-bb04-326a-a32f-108792a063d1 | -6.95975 | -48.65335 | 2025-10-19 04:32:00 | NOAA-20 | MURICILÂNDIA | TOCANTINS | Brasil | 1713957 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bbb658e3-13a6-35e9-b8f4-c3037ba2abdd | -5.53144 | -46.98538 | 2025-10-19 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 764648cd-fc94-3c82-8b1d-b3ef7fdb35d8 | -8.31772 | -49.48737 | 2025-10-19 04:32:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 155a88a0-5a33-3403-9061-bb3301f8b0e0 | -8.89806 | -49.0046 | 2025-10-19 04:32:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9529230b-fd27-3899-b7b4-cab82c69c3e5 | -5.67226 | -47.98732 | 2025-10-19 04:32:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 69c4ca8c-d28d-3e91-88f7-576cff3c968d | -5.49554 | -45.92902 | 2025-10-19 04:32:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6680d90a-e73c-3695-a733-5e32ceb35b53 | -12.46988 | -45.43876 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6af67306-74a8-3dda-9ccd-c305164dfe9d | -4.97037 | -56.27686 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 55bdb4c4-e338-3138-9c2f-11ad85ce460c | -10.8638 | -47.60386 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8976e8a8-f441-3d8c-984f-a5860161f8b2 | -8.613 | -40.19849 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 29.1 |
| e9fcbb3c-64be-3a1e-88e6-cf31dcbdcdfa | -5.63462 | -44.80928 | 2025-10-19 04:32:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e739b7bf-7648-363d-93d5-d31e899fe69c | -11.62555 | -44.08116 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a43738c-d6e8-3eb4-8cf7-e7c7750ac133 | -11.14664 | -47.7108 | 2025-10-19 04:32:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5d655d4-de46-3e7f-a736-b0664199cebb | -6.49806 | -54.89096 | 2025-10-19 04:32:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 154fa3bd-43f9-3840-8a14-d57fb468e497 | -9.30709 | -44.47776 | 2025-10-19 04:32:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5d8d3baa-6ba6-3fe8-89b7-15603afc51e5 | -8.41698 | -44.14266 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d183e84c-5a66-3b6d-82db-35c778672625 | -11.51991 | -49.14221 | 2025-10-19 04:32:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3e8fa7a-9a2e-325a-8069-e0e669eba5ad | -8.34821 | -46.21357 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5d549edb-6f78-36fb-823e-899158f6c49f | -10.2306 | -44.89975 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 39b63f70-d2e0-354c-9c67-cf4be7319c84 | -5.36988 | -45.95053 | 2025-10-19 04:32:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 73210f7f-6ba3-3f54-a3be-cebf207ba94d | -8.24843 | -44.00116 | 2025-10-19 04:32:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a4a61c2-e075-3650-a970-d7a6cba53389 | -9.88883 | -47.65516 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b6e93268-5979-3589-a268-17e1daf528a1 | -6.12896 | -44.22808 | 2025-10-19 04:32:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 65066178-a634-36fb-b5ac-cd1e1f578dac | -7.66648 | -46.66261 | 2025-10-19 04:32:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 739e136f-e6db-36d2-a02c-8b9f4bc21dca | -7.59813 | -45.85292 | 2025-10-19 04:32:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3eb63e20-86a1-308a-9fdd-bb1106519b52 | -10.45516 | -45.02434 | 2025-10-19 04:32:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6f1908a7-7f2b-350c-8b5d-a2d948736a66 | -5.53421 | -46.98936 | 2025-10-19 04:32:00 | NOAA-20 | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b0530fb-143c-3a6b-aa64-a357af627cfd | -6.35414 | -45.74443 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7a815e6-e5ea-3cef-b5ea-62f1d8a4ff89 | -8.58641 | -45.44096 | 2025-10-19 04:32:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7949a736-a013-37f0-a41d-ce23032a0dfe | -5.43083 | -47.53887 | 2025-10-19 04:32:00 | NOAA-20 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf77e339-53db-3602-9613-c4f057a861aa | -12.10765 | -45.87725 | 2025-10-19 04:32:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 649e6733-b048-31e9-bfc5-f9289a82dc84 | -12.00105 | -46.77217 | 2025-10-19 04:32:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64c9fdf5-905c-30d3-a446-a75826b1c59b | -6.37982 | -45.75943 | 2025-10-19 04:32:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 6898f62a-f5a0-3fa5-b730-65fb49c183be | -10.88073 | -47.44835 | 2025-10-19 04:32:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5bdff7af-c733-3ef9-a8fa-b53931e3e18a | -7.40665 | -44.80258 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c647a7a-9194-3ebe-8497-75800395656b | -9.18094 | -61.39306 | 2025-10-19 04:32:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| b72c77b5-f8a0-381f-bb0c-824214bbbfb4 | -4.74321 | -48.63533 | 2025-10-19 04:32:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 66acce5d-82f6-3d04-a62a-2dc955634189 | -9.89493 | -47.65975 | 2025-10-19 04:32:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| af2f0732-aa7f-3f29-8017-b64ea2b10a4d | -6.5609 | -45.94918 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a625ef2f-1737-3d8a-a7ff-c5244e5fca36 | -6.05706 | -44.33412 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d431a9b5-19f2-331a-84c7-c19250d2ec91 | -5.56534 | -46.37878 | 2025-10-19 04:32:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10306010-29cd-31ca-8e46-7e892ade6fc0 | -10.7233 | -44.54123 | 2025-10-19 04:32:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| bfab2690-61e7-3a46-aedc-c7595fce3fbd | -11.47599 | -42.22396 | 2025-10-19 04:32:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5ac20b52-1a69-30bf-84c1-d97abd4e4d69 | -5.4944 | -49.57069 | 2025-10-19 04:32:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b3ab4cfd-0f88-3424-86d4-48adf6e885cd | -12.45263 | -44.86349 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ddf64886-eb87-3b70-91c0-e83451812348 | -6.67692 | -46.19449 | 2025-10-19 04:32:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4592c771-454b-3c66-81bd-a3711ceed8be | -5.71193 | -43.82103 | 2025-10-19 04:32:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7df3676a-a702-355c-98d7-347570319c8c | -9.21236 | -46.05616 | 2025-10-19 04:32:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 791d7c8e-1015-3c76-837e-6b416ef094ee | -4.48396 | -50.56141 | 2025-10-19 04:32:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6a15d531-00e3-3023-8f07-b614379cd59a | -6.31191 | -43.97721 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 55be3a5e-d9dd-3044-a54a-99f0bdf20986 | -7.4156 | -40.07 | 2025-10-19 04:32:00 | NOAA-20 | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 929a6aca-abdb-39c9-af7c-295d9d5ebc7f | -7.65642 | -44.63111 | 2025-10-19 04:32:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 97a019c8-e2f3-3d68-b91f-16636d4f32ef | -5.36841 | -45.27546 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2395cb53-f8c8-3a30-9aff-149c233bfc96 | -4.96715 | -56.26399 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 70172b3a-24bc-3a6a-aa8c-6f4a777362f4 | -10.5358 | -44.50334 | 2025-10-19 04:32:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| f01a0fb6-e909-32ac-bbcb-75c65e85115d | -5.77422 | -42.73034 | 2025-10-19 04:32:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1844ee37-5bc4-3af6-9e24-dea3831d61e1 | -6.41553 | -43.92028 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 661bdab3-6c4f-3ea5-845b-a8cff3fc5b7f | -5.59258 | -44.75393 | 2025-10-19 04:32:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5a1e6e4b-e272-318d-9573-f4f16f3629d1 | -7.30276 | -42.33014 | 2025-10-19 04:32:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 41558b19-430c-3178-a05e-fa1f6a91664c | -8.42524 | -44.13905 | 2025-10-19 04:32:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 465ae149-a5aa-3507-ad8a-fff9d365cc95 | -6.06239 | -44.51873 | 2025-10-19 04:32:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5ad99447-d918-3465-958f-8187f48c4494 | -5.17236 | -46.11172 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e51df0cd-11e5-3650-a8b1-d19ce3dfaee1 | -6.70407 | -46.63048 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aa3b81cf-b2bb-3504-b4ea-695b4b3f88fc | -12.14439 | -45.07788 | 2025-10-19 04:32:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 72a1ef24-3d68-3a58-9c88-5b9cb80afc67 | -10.64607 | -44.75631 | 2025-10-19 04:32:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 007886aa-e34c-3051-be46-86ae9aba4fc3 | -6.54942 | -47.27319 | 2025-10-19 04:32:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e3f19afe-19c0-3723-9215-8af425ced153 | -6.1876 | -46.52526 | 2025-10-19 04:32:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3fc6269e-7dde-3cbd-b4c0-57d98ea5fac1 | -4.97009 | -56.27801 | 2025-10-19 04:32:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a8b9a9f4-a18d-35b8-bf22-ad5af2e1480f | -5.30469 | -45.07584 | 2025-10-19 04:32:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| cb89e534-96d4-331e-8f00-2d646f3ec1ad | -6.41733 | -43.91852 | 2025-10-19 04:32:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cdf35cb0-abf8-3d2e-983c-1bd827a5768d | -11.62231 | -44.07543 | 2025-10-19 04:32:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c08bb73c-2e5c-393c-bbaf-8386477a1962 | -8.60882 | -40.19234 | 2025-10-19 04:32:00 | NOAA-20 | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 29.1 |
| 412856bb-0cc0-3b62-bdf3-d212d4593b86 | -5.10087 | -46.1368 | 2025-10-19 04:32:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d8644a7c-371c-326f-bd60-3987c4baa936 | -7.6174 | -60.92498 | 2025-10-19 04:32:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7aea012f-e3b1-315e-979a-bf7117d064f0 | -12.45883 | -45.43706 | 2025-10-19 04:32:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README45.md)
