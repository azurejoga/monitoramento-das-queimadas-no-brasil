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
| 27fa8985-8152-32b7-be6e-7ce3c83117fb | -14.8558 | -47.131901 | 2026-09-19 00:19:00 | METOP-B | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 37e6fefa-fe3e-367d-a117-b4ee1fee8d56 | -4.2155 | -56.321999 | 2026-09-19 00:19:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 16a656e8-f40c-3f63-adc0-e67f8c942fde | -14.8008 | -48.539001 | 2026-09-19 00:19:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 681e1c46-0cd4-330b-960d-d6c1c06d6f46 | -6.6761 | -50.899502 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c11252d-c826-32a8-9353-6e5d3e5f6c6a | -5.8489 | -52.069302 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 973c4696-5ff7-3b95-b9ae-9d737cffc631 | -11.3212 | -47.346901 | 2026-09-19 00:19:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0bf80165-b05b-3773-ba53-e597366ef912 | -11.2754 | -54.108299 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7455040c-45a9-38d5-bb03-1ab785857098 | -14.1592 | -47.027302 | 2026-09-19 00:19:00 | METOP-B | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| edd8af7b-a88d-37ed-8bfd-78cd86ad0fe0 | -5.6188 | -45.236401 | 2026-09-19 00:19:00 | METOP-B | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bc3c5af9-309b-3491-ad28-08191491912e | -10.9164 | -53.9636 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25834fc9-2cda-324b-a80c-54db6c06cf72 | -5.9923 | -51.792 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a05d3ec-47e9-334e-a4f3-56e55331c0c3 | -1.8386 | -54.8461 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 617b0fb1-84e4-3bfe-b649-b1b05cf36367 | -5.8989 | -53.530899 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cdce11d-f816-3ca4-bf64-d1062cdb722f | -12.1248 | -46.989399 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f96ae17-fd8a-34a1-97f2-08b7af12139e | -12.9678 | -46.971401 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ea2f531c-51bf-3bb2-9b32-a0bf0a784998 | -10.8547 | -50.1875 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 595b6072-f9a8-31ce-9bab-28ad80b5f7fe | -11.8282 | -46.829102 | 2026-09-19 00:19:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 88bdac1a-ac62-3b4c-a523-3666b650989b | -10.5248 | -46.734798 | 2026-09-19 00:19:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b6c71264-460d-3e67-bed1-3bb6abfe00af | -5.1919 | -49.330101 | 2026-09-19 00:19:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44daf6eb-dc42-3fd3-abcf-f432e998eff1 | -3.1569 | -53.930599 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d2ea3c9e-5255-3f14-bf80-66e959b04d0e | -5.8705 | -52.0284 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9d2af1c-4725-3522-8c3e-a9c64d3a975a | -11.4397 | -51.462601 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9e7ad531-faef-3a56-bc4b-8b241f2f1bc0 | -18.8293 | -47.921001 | 2026-09-19 00:19:00 | METOP-B | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| a7d2c82d-78c2-380d-a607-a877bd69ae10 | -12.3904 | -48.471401 | 2026-09-19 00:19:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9af65dfa-17b6-3d02-991c-00d2bfacf41f | -10.1994 | -46.583302 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d86cfa10-9093-3004-a225-605e9617102d | -11.6834 | -54.437 | 2026-09-19 00:19:00 | METOP-B | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7cee0e3c-93ed-3d8c-b56f-53ec42e01384 | -1.5921 | -54.438202 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0fb9fb08-0230-3a53-8968-16f1a7c4e435 | -11.9346 | -50.130501 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ebe42d1b-9f19-3fb5-9bc0-230603107399 | -7.5695 | -57.663502 | 2026-09-19 00:19:00 | METOP-B | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 690ea87b-52aa-3ca6-ac54-6b9cf29ae92d | -8.6298 | -47.534901 | 2026-09-19 00:19:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dcf9eb4e-d6b6-3d57-973b-d81466929a16 | -1.1893 | -54.2057 | 2026-09-19 00:19:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1766d6a0-5c20-3758-94e6-409426f8ff71 | -6.1317 | -59.918201 | 2026-09-19 00:19:00 | METOP-B | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ab69ed4a-32d5-3571-a96e-ff92f5ee3133 | -11.05 | -48.3018 | 2026-09-19 00:19:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ceb6d332-35fe-3dce-ac2a-026aa608ede7 | -10.862 | -56.178799 | 2026-09-19 00:19:00 | METOP-B | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 76d93574-2b2c-3173-aafd-466446716395 | -8.168 | -54.730099 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6e1cabec-a7d5-377b-880e-34aed57dfc81 | -9.9557 | -46.556999 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 48254485-c32a-3ebb-989c-22721494ec2c | -4.5431 | -54.926601 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e800f0cc-9230-311d-ab0f-417b18e523be | -12.8462 | -44.3894 | 2026-09-19 00:19:00 | METOP-B | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 12ee59bf-3f9a-30ac-9bb6-2568f41bbfb7 | -14.6833 | -46.665798 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0ceb776a-b134-3356-8be1-5ac7aff709a5 | -0.5146 | -49.1418 | 2026-09-19 00:19:00 | METOP-B | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a935baa-dc6d-399c-88fa-3db9f2bcbac2 | -10.9326 | -53.943199 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cefd4b60-45c1-3ec9-9ebf-ec72c8f4a22e | -11.4252 | -51.443901 | 2026-09-19 00:19:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ec355375-1220-3b2c-9a35-d5aa33fe08bc | -13.7347 | -48.7952 | 2026-09-19 00:19:00 | METOP-B | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 89623051-9aeb-3c4c-91a9-a5e092a68094 | -13.0123 | -46.941601 | 2026-09-19 00:19:00 | METOP-B | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f8f32306-3915-32e6-8ac3-fd69f2c24d28 | -10.8986 | -50.883999 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a26b1df5-a935-38e5-9fce-49991c48045e | -10.8287 | -50.163799 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7e421a90-ddda-3cbe-9478-cd5c41ecbf05 | -11.0659 | -49.755901 | 2026-09-19 00:19:00 | METOP-B | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| aa22696a-9d5f-3861-b33e-446b17fa086d | -3.7384 | -54.6409 | 2026-09-19 00:19:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6ba90fd1-39db-300e-8438-510d4eaac9df | -14.1748 | -47.841499 | 2026-09-19 00:19:00 | METOP-B | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1cbd8a-e0b6-38e3-8820-ea1d57ed9b96 | -3.0196 | -51.184601 | 2026-09-19 00:19:00 | METOP-B | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6401eada-c46f-394a-987d-3a63a730343b | -12.9874 | -44.833801 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5675c2a6-7929-39be-8230-79bbec078bf6 | -2.6594 | -49.4748 | 2026-09-19 00:19:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e91aa52-85ef-3fce-a8f7-28f54e8db302 | -6.3616 | -58.272202 | 2026-09-19 00:19:00 | METOP-B | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 73f90750-8794-3e9f-bc60-154f71805871 | -9.0258 | -48.738899 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| 6318676e-76dd-3653-9253-5f14653621fd | -9.0337 | -48.7286 | 2026-09-19 00:19:00 | METOP-B | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| d7b8195e-f26e-3a6c-92cc-1b130d21779e | -15.6676 | -52.731201 | 2026-09-19 00:19:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f02c3a64-d926-3081-9822-1c31c19df4c3 | -3.2122 | -53.947701 | 2026-09-19 00:19:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 77bb63db-c8a9-38fb-85db-c24bfb16d7d3 | -12.3341 | -50.716099 | 2026-09-19 00:19:00 | METOP-B | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 3c8669cb-2f7a-3060-b17a-20a75d08e22b | -11.3114 | -51.719601 | 2026-09-19 00:19:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 93997ba0-8588-35e3-8b14-166e63966b34 | -12.6878 | -45.933998 | 2026-09-19 00:19:00 | METOP-B | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6f0b5029-fc94-3c99-896f-8bc03d14457f | -10.6961 | -60.697399 | 2026-09-19 00:19:00 | METOP-B | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fe45c021-e68f-344c-a7c2-6a78b99d6847 | -11.3352 | -44.1315 | 2026-09-19 00:19:00 | METOP-B | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a285f3d5-5015-30ab-9e4d-5cf9a04dc90f | -3.2271 | -46.946701 | 2026-09-19 00:19:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9f7c43f1-2a5c-3f21-9544-7883d7eddd36 | -5.8974 | -53.5238 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3110f70-0ae7-357f-b680-065409d9d5d7 | -8.6083 | -54.5835 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a0d7d24-6b8b-39b8-ad0a-362110a5f711 | -8.7726 | -48.670799 | 2026-09-19 00:19:00 | METOP-B | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | nan |
| ffdc03af-f43e-3a3c-be95-477cbaa8baa1 | -1.7127 | -54.8815 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7d530cee-076b-3cb0-955e-6ab5ac997e4b | -10.9088 | -50.837799 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 23cdc444-17db-3ff5-a5c4-32cd9966b651 | -8.8404 | -50.4431 | 2026-09-19 00:19:00 | METOP-B | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2a1c559b-c2a0-30d7-97dd-f60df016cdd3 | -12.0023 | -49.928699 | 2026-09-19 00:19:00 | METOP-B | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8a3a3e14-91af-3e35-b347-7b226db145a2 | -8.3647 | -45.649502 | 2026-09-19 00:19:00 | METOP-B | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 63ca82f4-98ff-3723-9a6c-f8e43673f7ef | -1.6586 | -54.9161 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a85493a3-3981-3f6a-82ef-801297fa4788 | -7.0099 | -44.651001 | 2026-09-19 00:19:00 | METOP-B | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d073f270-6490-30fa-9705-1ebdc48b2eba | -9.8443 | -49.243099 | 2026-09-19 00:19:00 | METOP-B | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 983eda8c-5070-3662-96da-5d9aa31f8ea3 | 1.2643 | -50.962601 | 2026-09-19 00:19:00 | METOP-B | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| 9774d932-0a1c-3661-a302-1b9db393e3b5 | -11.0715 | -48.305099 | 2026-09-19 00:19:00 | METOP-B | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 5271f1b8-6b03-33bd-963c-95db90ed8805 | -8.656 | -45.447201 | 2026-09-19 00:19:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e5412dc9-8119-3658-b9ee-babcb0786743 | -5.8675 | -46.7108 | 2026-09-19 00:19:00 | METOP-B | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 21665175-3ac2-3055-ac80-207a87eedaf7 | -11.0766 | -50.667599 | 2026-09-19 00:19:00 | METOP-B | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a6e27f1b-370e-3e64-b7ff-cb397b82c6f2 | -14.6638 | -46.6707 | 2026-09-19 00:19:00 | METOP-B | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 7faff1cf-f1e4-3a92-b0cd-d344afa0a34d | -1.657 | -54.908901 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 98a08731-63f9-38fe-a2b7-0f909d53952b | -4.491 | -55.479301 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 73498d08-2cbf-3596-880d-225c94305040 | -15.0798 | -49.587898 | 2026-09-19 00:19:00 | METOP-B | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 431637cd-f874-3a79-b913-ed5ca38a19eb | -6.6614 | -50.925098 | 2026-09-19 00:19:00 | METOP-B | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cfdbd1fa-97c4-343f-a1f0-ec78496fb56b | -8.1662 | -54.8162 | 2026-09-19 00:19:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1fc3ecca-c640-334b-bdcb-309b4013a64c | -11.1278 | -49.0369 | 2026-09-19 00:19:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| ab5d1053-8fe8-3e95-b573-e5c2d3781671 | -10.8303 | -50.170898 | 2026-09-19 00:19:00 | METOP-B | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e4a79dcd-f3c8-38f6-8530-5a3478c6a7a8 | -1.4105 | -49.415798 | 2026-09-19 00:19:00 | METOP-B | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c6ba4d2a-c21e-38af-aeef-ed62538aa1d2 | -2.3897 | -48.525501 | 2026-09-19 00:19:00 | METOP-B | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a14acd2f-aa26-309c-a18f-fd3409e99bad | -10.9262 | -53.961498 | 2026-09-19 00:19:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2e9ac001-1bb4-3250-bab6-940ac8f7458c | -11.3016 | -51.721802 | 2026-09-19 00:19:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 63e3201b-3dc4-378a-a898-5b636a25f81e | -14.1339 | -45.1632 | 2026-09-19 00:19:00 | METOP-B | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fa34cec0-5e5f-3086-82bb-2a82ff9efaad | -4.4928 | -55.487301 | 2026-09-19 00:19:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9e8ed96-d1f7-3846-9ae7-4aa91246a8f7 | -1.711 | -54.874298 | 2026-09-19 00:19:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3616e76b-946c-3545-bc68-da4c7294718e | -14.9597 | -47.530701 | 2026-09-19 00:19:00 | METOP-B | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| a64ce145-a543-31e5-9fa7-27116510383b | -11.1142 | -45.2855 | 2026-09-19 00:19:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b16ef28d-811f-35cb-b1e6-45964c0aefcf | -12.1519 | -46.973099 | 2026-09-19 00:19:00 | METOP-B | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0e8dd5af-e0f1-3d95-a975-5a1f327beaa6 | -8.4506 | -45.705898 | 2026-09-19 00:19:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 61e1a63e-5631-3adb-9697-fdc370ea4dbb | -7.2331 | -46.951199 | 2026-09-19 00:19:00 | METOP-B | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 97bf2e78-8740-3a48-add4-93d1ec41a5af | -3.334 | -59.804001 | 2026-09-19 00:19:00 | METOP-B | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README7.md)
