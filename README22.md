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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 89eefd18-f200-3511-be50-62743d848d53 | -8.88495 | -50.15415 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 2afab58b-d3f2-384c-b0d1-e8b65f8f5e45 | -11.74007 | -48.18653 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| befeb055-a359-355e-8a39-b1c95b5ffbe9 | -7.06473 | -42.9866 | 2025-07-18 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6e6ab792-558c-3547-808f-b3bb2b6b82a4 | -7.6111 | -45.54564 | 2025-07-18 04:53:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 07c4d6a1-f357-3aad-ae57-da6410562b39 | -12.70982 | -46.81318 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ebadccc-76de-31ad-9244-db8ac41d8c6d | -11.73864 | -48.19156 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 34d6c4aa-cb5b-3640-8ffc-db4302b7e842 | -7.7113 | -47.28942 | 2025-07-18 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9b7a842b-83d0-30f5-ad89-bec46a5d65bd | -9.8502 | -48.06435 | 2025-07-18 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a14513d9-50e4-32e0-b04e-d19750dd6237 | -7.61045 | -46.32436 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9b276ddc-5de8-37c8-818a-e9de8fb0e817 | -8.06567 | -50.07889 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d40c05df-dfd4-3f89-87dc-509d4fe177d6 | -11.74446 | -48.52713 | 2025-07-18 04:53:00 | NPP-375D | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cebb9b44-077a-300d-a0ab-9533f0f77338 | -9.01556 | -59.5372 | 2025-07-18 04:53:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0e59ed7a-32e1-332a-acd2-ddb8bafdd05f | -8.10532 | -43.15251 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| c1bc575e-03c7-3a03-a572-acdd0d9a0d03 | -10.89941 | -49.2105 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 93b1af4a-cf59-3926-9a8d-5f5e822d8bab | -6.96515 | -43.7436 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a138c730-f546-3df1-b0ed-a77a585cadf5 | -10.84019 | -48.34539 | 2025-07-18 04:53:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 91b23f04-64eb-3460-8238-c3e929b1d1cc | -13.00214 | -44.85935 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d11abc55-8643-3a74-91a7-20d0a030c31a | -8.88025 | -50.14998 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 97bd664d-34fd-3a07-a5e3-97cf33e4399a | -8.87417 | -50.15253 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ab738529-4866-3c90-8d08-536a00a71952 | -10.71438 | -49.47976 | 2025-07-18 04:53:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f278688d-3b16-3325-8ab0-4732dca0d548 | -7.60716 | -46.31511 | 2025-07-18 04:53:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7296f0b4-db38-3587-b223-aae5dc2c2b7a | -7.06525 | -42.98287 | 2025-07-18 04:53:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 00963389-fa00-3b23-8d4f-560afe6442e0 | -8.11143 | -43.14956 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fca6ee7c-c094-3d4f-a4b9-11a7c7f49f77 | -6.98196 | -43.93027 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c5a9f1f9-c5bc-3d9a-9a21-e9b9d7130f22 | -11.56291 | -47.08174 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8ae569a6-c961-3657-b649-3e2f5e0c6aeb | -8.92088 | -49.83376 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df9f6e81-d45f-3444-a569-a39dd7a57d6d | -7.35046 | -44.19054 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f0a612b4-7881-3879-ae9e-955e1cde6247 | -11.74374 | -48.19107 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.7 |
| ebdddb9c-d417-3f3b-90d8-d97eeaf33286 | -10.67998 | -56.54903 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1b67ef9c-1129-34b3-953a-eed53d8094c1 | -8.09411 | -43.15095 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| c23abe81-818d-3289-8eec-ff0f8ec460cb | -7.49175 | -63.81955 | 2025-07-18 04:53:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f4fcd475-335c-3829-8345-d893a5754304 | -9.16012 | -49.66982 | 2025-07-18 04:53:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8f96a5f0-972a-3bae-a90d-46151fab974f | -12.03353 | -48.76516 | 2025-07-18 04:53:00 | NPP-375D | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c111730e-7ac8-38db-b945-b556a6cfcdb2 | -11.56165 | -47.09094 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 7371ce5e-8f72-3c2b-abaa-756754f04e01 | -8.08291 | -43.14934 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| d9898033-339d-37b4-b1cb-0ea4e424b25c | -9.49944 | -47.56026 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 8518c1d5-7f49-3392-80c3-8b6a99e35fd1 | -11.56228 | -47.08633 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 2bb8ce53-e101-3e87-a337-985b4d1f84a5 | -7.19656 | -44.0757 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5c3811f-7e71-3e96-abbd-96b55c9c1c1b | -9.46812 | -62.20089 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8c4620da-abfa-332c-a7f8-0c227ce0d0fe | -8.96914 | -61.51822 | 2025-07-18 04:53:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc1b35b3-c396-37b4-916f-b689cbc3cfc7 | -8.88929 | -44.79072 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5a843ea9-8dcc-3ea3-9bbb-81490d376552 | -6.96469 | -43.74689 | 2025-07-18 04:53:00 | NPP-375D | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c4df99a-2479-3f15-9219-fce3e3e1ed58 | -11.99883 | -45.30716 | 2025-07-18 04:53:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34b7bada-ce1c-3ed8-88dd-51de09148ce3 | -9.76839 | -48.75946 | 2025-07-18 04:53:00 | NPP-375D | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 861acacc-c38c-3cfb-963a-b380cb5cc936 | -8.11754 | -43.14659 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51dcc604-a798-3db4-8585-c93fefad9f6d | -11.46037 | -48.1571 | 2025-07-18 04:53:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a6143d54-945b-35c5-8b13-147ca4af53a8 | -9.86114 | -44.70548 | 2025-07-18 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dbd926a0-dd39-3203-b782-d02842b394e4 | -8.04015 | -50.07841 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd9cc1e3-951e-3f69-8361-78879c8e8243 | -6.95251 | -44.55843 | 2025-07-18 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 361e4c30-01a0-31ba-9b34-c8d88f7c7492 | -10.67349 | -56.5437 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5281a587-531c-3f1f-91de-8e66f061268a | -8.06275 | -50.07401 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 62f0d84b-90a0-3a4d-a875-4de9b7a4ca8f | -13.00171 | -44.86282 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b6109f80-a3e5-3f41-b2ab-87e2e575271a | -7.34485 | -44.19293 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e54971c0-ca4c-3182-892e-0acbb50dba6a | -6.616 | -47.1948 | 2025-07-18 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8b5a03d0-37b7-3727-b81f-b84d1b052f73 | -11.56434 | -47.07927 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 9318c1a9-31bb-3aa3-938a-37aaa1c40bc9 | -11.57215 | -47.08978 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c69709a-30ce-3803-a982-9ab6f2217495 | -7.39524 | -43.79506 | 2025-07-18 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7d9d9f01-ebf5-3964-89c4-346a5cfbc0a5 | -12.99677 | -44.85879 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 437ffb78-9565-3705-8e73-eea7f5364484 | -11.85809 | -46.75141 | 2025-07-18 04:53:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 590c64c8-3e51-3196-a4f1-0f8edd555525 | -8.07633 | -43.15591 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e264d038-ffd1-3551-8d04-48c7a52ab0b5 | -10.68249 | -56.54464 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9c150692-8f29-3728-9ce4-4d685826a639 | -10.68179 | -56.54873 | 2025-07-18 04:53:00 | NPP-375D | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40f291df-92f2-32f3-a579-04702dd3f990 | -8.88196 | -50.14948 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44b87268-55c0-3d9f-8477-69300cb11f7d | -7.63423 | -56.73433 | 2025-07-18 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e9148334-9b87-309d-b219-55eaf0234842 | -8.88075 | -50.15773 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4ee3486f-4604-310d-ba8b-8ea1640df78b | -11.57155 | -47.09438 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ebd688f4-3a6c-30ef-b24a-bd81a430cd58 | -10.8407 | -48.3418 | 2025-07-18 04:53:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 03e94269-b8f4-357d-85f5-3c3617591293 | -8.08192 | -43.15678 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| e0754a90-d98a-3291-9d80-4cc30a8dce72 | -10.05814 | -59.09901 | 2025-07-18 04:53:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7b6d8f8d-8c2e-318c-b503-13ffd2d14b31 | -10.82059 | -49.28592 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97ab84ca-75ca-3ad6-a681-078dea33ad2a | -12.57472 | -44.74741 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d8e1ecd6-1d4d-31e1-b75f-cd5b0d366511 | -7.70289 | -47.28827 | 2025-07-18 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 50c7b523-d4f5-3fd3-8c61-46b304d75aee | -9.86221 | -44.70906 | 2025-07-18 04:53:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 015c40c0-5616-3ea8-a4ef-c5886b143e1e | -7.28334 | -44.21883 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ac0fc74d-c542-3331-b154-f6b5f65a8acc | -9.39365 | -48.39864 | 2025-07-18 04:53:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e8257ee6-dd33-3fa7-a62c-770f71f43097 | -10.09266 | -47.24348 | 2025-07-18 04:53:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5309b16e-7731-3b2f-ac39-ac9ba0f52f35 | -7.93894 | -43.85856 | 2025-07-18 04:53:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1981dca5-5d09-3f61-b029-335d11bc2935 | -6.61484 | -47.19569 | 2025-07-18 04:53:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f5f42d46-bba8-390f-a58b-afa72a3be0a4 | -8.87603 | -50.15357 | 2025-07-18 04:53:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 7b74264e-932a-31b3-8391-f7bd24091089 | -7.35 | -44.19378 | 2025-07-18 04:53:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 70716b71-c1b9-37b7-baf4-b98cbb55cf78 | -12.99633 | -44.86232 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c221ddb8-f2e1-39ae-b4dc-0833461598bf | -12.56894 | -44.75012 | 2025-07-18 04:53:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b0e09b6e-4cdb-3ba6-b041-3e7593517152 | -9.80506 | -47.73808 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5c9eb148-7cbb-3847-b76a-bcd288820ef9 | -8.06322 | -50.09521 | 2025-07-18 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fc716edf-bc66-3672-9169-c69c4b58bb4a | -9.80032 | -47.74134 | 2025-07-18 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67ba58e8-8aa9-3e87-a601-2cb11ef5e2e7 | -11.56615 | -47.09158 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 21d5b347-5acb-309c-9478-9b8166d0ac7f | -12.65921 | -47.09663 | 2025-07-18 04:53:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 719756da-2dc8-3611-8c83-a0f4c30d51d2 | -9.24255 | -48.55923 | 2025-07-18 04:53:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 670dd1e2-c37d-305b-abad-7e4f23d67298 | -8.08851 | -43.15017 | 2025-07-18 04:53:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 435e949f-99c5-38d3-b779-71a0bb3697b5 | -11.7339 | -48.19487 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 9149afd2-cb38-3016-b47f-7e200d5ddecc | -11.56314 | -47.08848 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3eb4cbf8-b62c-372e-8e40-b148bd0e82cc | -11.56374 | -47.08387 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 58e827cc-0cc2-3730-b623-7d76b5098cde | -11.73446 | -48.19094 | 2025-07-18 04:53:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 25.5 |
| fd2724ba-0df9-37ed-9131-bee78df369b3 | -11.57129 | -47.08762 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc3c60a5-ca32-367b-87f5-6a2e28fb7f16 | -8.65078 | -47.75275 | 2025-07-18 04:53:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 00a15a95-5ee6-3b05-94a1-04bd2709cc24 | -11.56493 | -47.07468 | 2025-07-18 04:53:00 | NPP-375D | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 246868b0-1e10-39f2-b4d1-ad5b339b89fe | -8.88738 | -44.78767 | 2025-07-18 04:53:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 6.2 |
| cf795b5e-602b-3028-988b-7f98ad81e388 | -10.81603 | -49.29019 | 2025-07-18 04:53:00 | NPP-375D | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4827b750-9849-33e3-bff0-1b2fe0b8973b | -9.85431 | -48.06496 | 2025-07-18 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 755712a9-c3dc-3ebc-b44c-141072bbb064 | -7.5329 | -61.34845 | 2025-07-18 04:53:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
