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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bb9e3558-ce1d-3965-92d8-1d64c6116d2c | -10.59111 | -36.6863 | 2026-10-09 03:45:00 | NOAA-20 | PACATUBA | SERGIPE | Brasil | 2804904 | 28 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 306e59af-7499-306f-a866-5d1f97f8999a | -8.9137 | -45.22254 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 806dc7d2-2a86-3344-b9d1-3e6cf1436a73 | -11.61893 | -43.60483 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f2e32dd0-ee2d-3662-a295-43af1a0c3e37 | -14.44632 | -43.92669 | 2026-10-09 03:45:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 93f6e351-acf7-3948-bbe4-c86a84a0a0bb | -9.36338 | -36.96397 | 2026-10-09 03:45:00 | NOAA-20 | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 06574708-14b5-3c7a-aa2a-52079605210c | -8.73125 | -45.14568 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 469db21a-11c2-3ad4-b67a-9d8ff1d0800c | -11.61213 | -43.61291 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f67e0e35-078f-3250-8991-34da60982763 | -12.00966 | -43.47857 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ac8cac4d-cf92-305f-9945-b43bfa9dee46 | -12.01279 | -43.46193 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ea8f90a-98fc-369c-8b9b-235638825fdc | -10.1899 | -36.32965 | 2026-10-09 03:45:00 | NOAA-20 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 4176de95-9e4a-3784-be6f-e08c9c7ea013 | -9.93821 | -43.55716 | 2026-10-09 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0962195b-148b-345d-b161-4b89e7be72f4 | -11.07148 | -44.08729 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08f2cda5-aca9-30f6-b476-0b224ab8b917 | -12.46595 | -41.32215 | 2026-10-09 03:45:00 | NOAA-20 | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 934805db-e119-3355-9060-8227a922ee10 | -10.8974 | -45.53406 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b09219d-8817-3ea4-8c25-0bedac1864ef | -7.24932 | -48.06481 | 2026-10-09 03:45:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0c0d994f-bb2b-3ce4-ad9d-8d4f442e0919 | -8.96464 | -45.9124 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 124e0f5e-a8f5-39b9-a46a-f982167a7eec | -12.01127 | -43.49765 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 09d02db5-0779-33b8-b1e1-e24caa85b3bd | -11.06056 | -44.06503 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f63da7ef-3576-3f40-86e3-90e88755d030 | -13.40861 | -43.72897 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 9856f905-2b9c-3d69-b8a2-1d55a581d938 | -8.7212 | -45.16636 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b344d9c9-a8fa-37b6-b70a-f8b379714a43 | -12.00616 | -43.46964 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86e0849a-0c2f-3857-96cf-7aa1d01e8957 | -11.99902 | -43.48006 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 85bcfe8b-9c28-37fd-a5ce-fc4eaca016e4 | -7.40919 | -44.76494 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| aa247c31-07b9-3084-8e10-9b2ce1151a3f | -13.49821 | -44.36939 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3d1115e3-67b0-370d-85f2-33bb1d8dff1f | -11.75872 | -45.48044 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77262d4f-5e66-36bb-9b1f-ef924f1d89e5 | -13.50372 | -44.37459 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5d93062d-df5e-3813-a583-08ccc046da67 | -13.38198 | -41.33609 | 2026-10-09 03:45:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 865c69a4-4fc3-331c-8020-8c2026222cf2 | -11.77193 | -43.53478 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 275bdcbb-0291-3a00-934c-ebfe75136554 | -14.05149 | -43.82769 | 2026-10-09 03:45:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2914d7dc-9e6a-366f-aacb-e4fe3d23dc95 | -11.65609 | -43.68737 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 62a5c5f8-b3ec-3459-a525-a290e3f3d148 | -7.40252 | -44.7681 | 2026-10-09 03:45:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 552535b6-0b9d-31d2-a6c9-c8e85424da37 | -11.83859 | -43.59004 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8e1197e5-627b-3976-abe2-d94dabad5aab | -6.95937 | -45.28331 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 473078ba-11a9-3390-a93c-3153980d82c1 | -11.5757 | -43.69265 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ffb4f4b5-d699-335c-8b1d-53f8fda960cf | -11.27538 | -45.1987 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bfdfc8c7-7ea9-3aca-bc9f-f0f66d2e3b0f | -11.76882 | -44.9514 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 939d14bf-615e-39c6-ab8f-711ed335450b | -11.3098 | -44.82558 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| e585e8b1-edff-3a50-9c8e-fe981d733295 | -12.00526 | -43.44688 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e44ea36-1910-3cfc-bbc1-e9b395d69e7b | -8.91203 | -45.23124 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 02477527-71d9-317f-8026-6967be470921 | -8.90749 | -45.23577 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 69599406-9ce5-3e58-a853-75dbefeef5ac | -11.76281 | -44.95679 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8f1f03b6-13e0-3c90-ba14-a12a831cd3bd | -12.01502 | -43.45004 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3676a695-ed50-3267-8396-c2fcfd4bc26b | -11.65551 | -43.69047 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3988a2d3-bb9b-3138-8dbf-763c37db8295 | -11.41516 | -47.5955 | 2026-10-09 03:45:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1d709ff7-f338-303e-a5fe-cc736b1d9340 | -8.32442 | -45.45454 | 2026-10-09 03:45:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 59f2b788-cf20-3513-afcb-e4c41c8c6d0c | -11.58365 | -43.65137 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 937a45b6-bb7c-3d2d-9a24-fd89509488a3 | -7.37474 | -44.03442 | 2026-10-09 03:45:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 349b0a59-ebf6-35a3-8ca6-fe34939bf9d6 | -13.50206 | -44.3773 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 37def197-4f35-330b-8fca-b5c142f8f5f6 | -11.61798 | -43.72103 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 80df83de-257a-3034-9850-ea76d3e31c34 | -8.89653 | -44.93727 | 2026-10-09 03:45:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab65303b-f142-38c4-b43b-161bb6eb3388 | -13.24821 | -42.25451 | 2026-10-09 03:45:00 | NOAA-20 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 45.5 |
| 89345fb8-52f7-37f6-8d37-75ae67a402dc | -11.7848 | -45.59418 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b997b3f-9d9b-3092-936a-06b06db1326a | -11.3146 | -44.83041 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 6441093e-eb82-341e-b3e0-5793cae16cbd | -11.46401 | -43.3886 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 20c414c9-ccad-3223-bad8-3e5f444ac49f | -11.20836 | -45.25909 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 34d85c4d-d8db-3e5e-a9d8-7d8ea754923b | -11.67554 | -46.77553 | 2026-10-09 03:45:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 65901720-844a-33e4-ae94-325b98cc847a | -13.50438 | -44.3713 | 2026-10-09 03:45:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9a83957b-b2f5-3898-941c-4972ca580db9 | -9.16444 | -37.35568 | 2026-10-09 03:45:00 | NOAA-20 | OURO BRANCO | ALAGOAS | Brasil | 2706109 | 27 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 6fa80f36-edde-3772-bf9b-4dcdad0a86ca | -9.2966 | -47.42426 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 773753a9-6df9-3c75-8826-45acd2e8766d | -10.41658 | -47.28713 | 2026-10-09 03:45:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 48ff6091-cb46-30d1-9c27-72a15b65a19a | -11.99196 | -43.48998 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 31440835-1a54-3956-bfd6-c756ad55cf6a | -11.06273 | -44.08276 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c947b5ed-1ca6-3a72-8ccc-a01cc496613b | -11.74648 | -43.64194 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 580a6a77-0459-35ff-b08b-145336538428 | -10.42315 | -47.28819 | 2026-10-09 03:45:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb2ca6ab-9b06-3a26-8f50-a1942d1c8d3f | -12.00726 | -43.46381 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 67c9dd26-ba39-31fa-8584-7f93594201f2 | -13.26183 | -44.00409 | 2026-10-09 03:45:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2f1f826a-61a8-3ce0-a844-46c63100e962 | -9.29493 | -47.46817 | 2026-10-09 03:45:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5fc7d4e1-b368-3785-bb2a-fbc285a55bc0 | -12.02525 | -43.4783 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c78662a1-708d-3c3d-85a6-b5ead448b9f9 | -9.9388 | -43.55397 | 2026-10-09 03:45:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3baaec25-440c-3424-826e-ee785928472e | -9.92307 | -44.79729 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7e14b75b-f873-3398-a35c-571394503ddf | -11.99348 | -43.48192 | 2026-10-09 03:45:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b5a7ae34-3620-3cda-9ec1-1ec35c019952 | -11.21479 | -45.2564 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f0e2178a-2f38-3cda-8829-48003c9cc20c | -11.06748 | -44.07957 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10c18be3-c05f-3aed-8846-1d20a5505812 | -8.98475 | -45.90732 | 2026-10-09 03:45:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 9b83a4b9-0329-3909-a83d-92cf245d2fac | -7.48041 | -42.8377 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a4b9622a-41db-3487-8391-4143424a8c90 | -10.89823 | -45.52971 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 786afe59-9585-3e3d-9175-cfeeedd081f1 | -11.63852 | -43.69643 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 210348c6-549f-3991-b69e-195b1292ab37 | -11.26321 | -46.26747 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bbcef4aa-02c8-39ac-a928-4ea8f465a42a | -9.89248 | -44.80409 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4fb41a8f-65d0-339a-8a62-96888e0b4f44 | -11.76199 | -44.9569 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 256a8b73-c0e7-3d79-8532-4b00ffb30031 | -11.74955 | -44.93291 | 2026-10-09 03:45:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 998bd3a5-c35e-3fcf-aef1-bb613704e08c | -7.47654 | -42.8596 | 2026-10-09 03:45:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 22ebdc80-d0e1-3015-8b67-f8909470d230 | -11.24546 | -46.2937 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72f502e6-7bf9-35b4-a356-7f9c732c14e5 | -10.90433 | -45.5245 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 895a6cd6-9c70-330e-a237-d336c50c9f60 | -11.00779 | -45.42573 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 17.9 |
| 5b83f21f-ff9c-3e1e-bcc2-2425f491b09b | -7.51054 | -47.3323 | 2026-10-09 03:45:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6d06ab86-7633-3add-8c3d-8bbb123c5c13 | -11.25439 | -46.28035 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e56428be-028e-3074-93ee-b1580b7e389f | -11.3077 | -44.8365 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 142.3 |
| 91e2bfe5-f7d0-340f-b97a-22cea18d0ad6 | -11.11835 | -44.01402 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4dc4706-4bb8-391d-be62-6fad081c5f61 | -7.50841 | -45.7668 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 019b1342-84db-3084-ae94-44b31ce72bce | -11.87284 | -43.60276 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 13364132-5cec-3daa-bc20-7a53a076db30 | -13.36761 | -43.88916 | 2026-10-09 03:45:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5f713911-4501-3b07-8e33-3e42e95540e6 | -9.46875 | -40.34365 | 2026-10-09 03:45:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ff17dce6-93af-3bd8-9563-7b9bac009d2e | -6.95944 | -45.28184 | 2026-10-09 03:45:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1b3fab35-b9f4-3dcc-a481-93186ba0d97d | -8.72624 | -45.17205 | 2026-10-09 03:45:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cb0f638e-fd97-3e95-b6f9-cac325245ef5 | -11.85489 | -43.5319 | 2026-10-09 03:45:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8523a35-5152-34c2-a875-8041f62ddb85 | -11.3091 | -44.82921 | 2026-10-09 03:45:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.8 |
| 0f2eafb4-53d2-3ec2-b782-626086f0c33e | -11.26232 | -46.272 | 2026-10-09 03:45:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7c801dd5-6170-3e9c-bc67-fb3fc166ceb9 | -11.08716 | -44.06281 | 2026-10-09 03:45:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2bda7331-ea8e-3c6f-9468-844005fcb6b5 | -9.90049 | -44.79279 | 2026-10-09 03:45:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README63.md)
