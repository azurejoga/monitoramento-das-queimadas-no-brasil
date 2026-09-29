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

## Dados Diários - Página 24

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 263ad1c4-cfa9-387a-9065-f87cf277d504 | -10.81894 | -48.74359 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2fadd120-eaa9-3f39-9831-a52c402e08ed | -11.1802 | -44.79815 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cb4aebd4-1bc2-3cf5-bb48-376f76ec1884 | -12.02917 | -50.96872 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| c32961de-b600-3173-bc2f-0abae80028d0 | -11.36635 | -54.04867 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ab20ac00-9449-349c-8c19-59ef68670394 | -14.77153 | -47.15443 | 2026-09-29 04:17:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ae0385a1-fc43-30f8-8b3a-02b0f90a8396 | -11.37652 | -54.05418 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4384afda-25af-3805-bb4f-5887fcf937fb | -21.06503 | -48.84208 | 2026-09-29 04:17:00 | NOAA-21 | PALMARES PAULISTA | SÃO PAULO | Brasil | 3535101 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 50a923a7-dfa6-3ffe-b820-6ce1d6a28a91 | -11.97798 | -50.9284 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 264e819c-cbde-34a5-99be-4acc6c7d745e | -13.37326 | -44.01098 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4e70d4c6-c634-3b0e-b70c-ad3399824415 | -14.51972 | -48.29586 | 2026-09-29 04:17:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6d2cdcd9-23db-3420-8691-8b8d64633c88 | -11.37846 | -43.38615 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f922ab1-296e-354e-bb9f-8f0cc7dfb05f | -13.54146 | -49.17736 | 2026-09-29 04:17:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 5f7d2656-9a19-3583-aa2a-177644794092 | -13.43887 | -43.82652 | 2026-09-29 04:17:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| da7ffec5-66d5-3fcd-99df-499c79c1393d | -10.80118 | -48.75481 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 5462bc73-7719-3a85-93a0-4348d2adee0a | -11.71706 | -43.46117 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 95cd1024-9054-3a27-9aa7-e1fc5c895a8c | -10.41493 | -53.77632 | 2026-09-29 04:17:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3a48ebc6-fa9b-32c5-a9a0-7c2d7575c3d3 | -9.85982 | -44.94787 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5fd1a72e-c64c-329f-b05c-9d37f52d06d1 | -10.82688 | -48.71976 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4a689e11-32bd-3fb6-94a0-3de4519052e9 | -12.00765 | -50.93822 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 559e0722-9328-32ed-b8c9-98c664a74036 | -20.43884 | -46.34331 | 2026-09-29 04:17:00 | NOAA-21 | VARGEM BONITA | MINAS GERAIS | Brasil | 3170602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4a110269-842e-312c-921b-fdc632ed08be | -15.21993 | -46.16914 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b95e5985-e150-39d3-a953-e48e044859cd | -15.45893 | -46.14343 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 1bb78a34-0b1a-3ae8-9fe0-46e10f124551 | -13.69324 | -49.22053 | 2026-09-29 04:17:00 | NOAA-21 | MUTUNÓPOLIS | GOIÁS | Brasil | 5214101 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a8e9c2e-742f-3b8d-bbf7-f7efb315713e | -8.88186 | -46.19847 | 2026-09-29 04:17:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ebc3fd7-8db2-3397-88be-79e7b9cd9874 | -11.80547 | -50.6057 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 653331af-67f5-3b68-8e54-c113ce18c1a2 | -10.25761 | -44.60548 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3e3a17c8-e4e7-3a43-b681-73ec2d82ca2e | -9.81994 | -44.94152 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b96f3d6c-fb73-3cf3-8ce4-49851e80b755 | -9.83115 | -45.27843 | 2026-09-29 04:17:00 | NOAA-21 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 34cbc27d-0176-315e-ac52-fd3600ce874b | -11.39324 | -47.44193 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0b6160d8-8188-385d-bfc2-8bdd37d3f3f7 | -11.18206 | -45.13014 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 05d507b8-416c-3b20-8390-28ff5532f78b | -11.42532 | -43.45931 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f844fce3-38c9-35a1-876b-a228bc0f33ef | -11.18482 | -45.1342 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 035e4387-f78e-3f8d-89a2-0635ec6e337f | -12.04528 | -50.95396 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 5cdc6d3c-7b9e-3f73-b001-ebb4e10b1c42 | -11.42472 | -43.44094 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6390420d-17f7-3ab4-a0ac-e89c8a75d327 | -12.72141 | -46.98727 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b34c677-093c-3ba7-8f48-a76fe2105596 | -11.41248 | -43.43173 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3e1a6c88-bce3-3f9a-ad89-e4d36642dba0 | -12.03505 | -50.96093 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6fd0f6be-8f49-3458-b144-f0f70701a461 | -10.26367 | -44.63155 | 2026-09-29 04:17:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4b18e77c-d6fa-34c6-8a55-27f531998601 | -10.8141 | -48.73556 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee5b90c5-3bae-3cee-a1b2-77c3dc767989 | -12.4798 | -47.485 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| c491b87d-5d08-3264-88de-18c33fcc861f | -10.21365 | -50.00946 | 2026-09-29 04:17:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f60b283-2646-3de6-818d-a323304735f2 | -11.99383 | -50.94011 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7355c1ae-2036-38ca-aa26-948d2951e59b | -12.31638 | -50.15216 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 65fd3eaf-d0f0-3a05-84b6-f5fc390b3da0 | -9.74827 | -48.9488 | 2026-09-29 04:17:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 108ac780-6f5f-3d41-85b3-acd1ef4c17db | -10.29972 | -48.15277 | 2026-09-29 04:17:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9795edf7-8b1d-330c-abf0-04a1034a1d2e | -10.71963 | -44.43651 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5d6ed88d-4ff4-335e-9e0b-f36b0a387a6b | -9.14038 | -49.97726 | 2026-09-29 04:17:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad4139b1-4c99-3008-b5e6-ddf30e200ba1 | -12.74105 | -47.31284 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e51a4602-49bd-3142-8972-f1016d3f2d90 | -10.01349 | -45.17937 | 2026-09-29 04:17:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7b3280d-3507-30d8-a540-ef8325f06f54 | -12.32879 | -46.95511 | 2026-09-29 04:17:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dbe59490-a4f8-3cab-a7a0-a742406eb41a | -11.35555 | -54.0465 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee24a605-ea01-3d8d-8583-1adbf8ed2e9e | -15.39938 | -47.92954 | 2026-09-29 04:17:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d2724798-0080-31d3-a406-d92c5cae3ce8 | -12.15997 | -50.82043 | 2026-09-29 04:17:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f97860db-0542-3f65-9336-2cbef0b54a52 | -13.02009 | -41.05038 | 2026-09-29 04:17:00 | NOAA-21 | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ef455ac2-10a8-3b0e-aa76-06a4f7ced199 | -14.79206 | -45.94979 | 2026-09-29 04:17:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2e6e6d7e-1d5a-3fd1-b911-ddf6d77f782a | -11.17579 | -44.80462 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 39f3d5ac-7738-3783-87c2-06a40f210109 | -20.21439 | -48.5652 | 2026-09-29 04:17:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1b12138f-6460-3c89-b91d-154e6e9e1de0 | -13.1133 | -47.40754 | 2026-09-29 04:17:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 07d1258d-baae-3112-8271-617b7f294910 | -11.93482 | -50.91317 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f7160ec-c551-3ce6-aff6-2127dd0171ff | -12.27815 | -41.82923 | 2026-09-29 04:17:00 | NOAA-21 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f561c6a6-2a90-3f73-9427-30edcce0995e | -11.36134 | -43.40909 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cd10cbbd-d1ea-33e7-a59c-40a71b72f0f6 | -20.70052 | -57.96187 | 2026-09-29 04:17:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 18f39325-29bc-3172-afab-df82e57ed7be | -10.71467 | -44.42499 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70dae783-afde-33be-b4af-52181a5ae184 | -21.06031 | -48.86977 | 2026-09-29 04:17:00 | NOAA-21 | CATANDUVA | SÃO PAULO | Brasil | 3511102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| c7bba68c-e589-3730-b6eb-c2d9a47902d7 | -13.17855 | -48.52888 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 64db00bd-3b76-3aa6-ba5f-7ad3ead49dc0 | -12.00119 | -50.99917 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7cfed4d1-2092-3ce3-a30a-cdbe4817765e | -10.81666 | -48.72091 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6b880a7c-1fa6-3aa9-9b62-1092795c6617 | -15.12821 | -43.61932 | 2026-09-29 04:17:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 349963f0-ccca-3288-b1c9-47696d22dc73 | -12.06818 | -46.46602 | 2026-09-29 04:17:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d7ac02a5-9d0d-3e35-9b40-27743be9e0d4 | -10.9721 | -49.67013 | 2026-09-29 04:17:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 29063432-3130-3411-94ab-d3ae33854fcd | -12.75831 | -47.29533 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| f923e797-153a-3a17-9a4c-96e39a783d3b | -11.38966 | -47.44142 | 2026-09-29 04:17:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 72a0a2f0-2ace-382b-9af4-896f7cc6f990 | -12.72011 | -46.99526 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 504b37c3-cdfe-3f99-99c8-a0d45ac2d6fb | -13.56305 | -48.93946 | 2026-09-29 04:17:00 | NOAA-21 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4361f1ce-38aa-329e-8f2c-bce3fcc32e97 | -13.17532 | -48.54763 | 2026-09-29 04:17:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c5954bb4-2422-3b26-8580-065a4c404e22 | -11.65224 | -43.50912 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0067008b-2795-33f3-84d6-df88c134af30 | -16.34572 | -42.57351 | 2026-09-29 04:17:00 | NOAA-21 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 00c31f41-e41c-3091-bb15-64d1086b61af | -11.37901 | -43.38258 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 639fa3da-526d-3f96-8bed-418107c8424e | -14.1216 | -46.28871 | 2026-09-29 04:17:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 336a357a-c698-3de8-a037-8b8955ec8590 | -21.32859 | -49.50691 | 2026-09-29 04:17:00 | NOAA-21 | SALES | SÃO PAULO | Brasil | 3544806 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| aa0bf96f-c2e3-3aa8-9f2d-38e8e470f351 | -11.38459 | -54.04097 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0cc3d478-51f7-3a9e-9016-c604888aa16b | -9.79807 | -44.82186 | 2026-09-29 04:17:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 223b9b50-a872-35a8-87d6-8e28036ecaa3 | -10.79336 | -48.7541 | 2026-09-29 04:17:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 609a997d-fdc2-3053-a1fe-cecd3dde1255 | -11.86574 | -47.11663 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8acf585c-15aa-3c19-bb75-def00d034878 | -11.40031 | -43.44444 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bf60d1c-a0e1-3e69-aeb9-97a4ffa83807 | -11.37242 | -54.04613 | 2026-09-29 04:17:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 45ca9676-a78c-3d86-9bb2-44e8aa31555e | -11.36391 | -47.4419 | 2026-09-29 04:17:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f220e2fc-2b9b-34c3-84e8-369deb698c40 | -11.86821 | -47.08044 | 2026-09-29 04:17:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9af3a5e1-adfb-337a-9797-be5a965fdf33 | -12.93958 | -46.66415 | 2026-09-29 04:17:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0b14d28b-807b-3a96-85bf-eb39b1e7ecdc | -10.82086 | -48.74226 | 2026-09-29 04:17:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6fe554a4-6d62-3b90-b683-d023f68b95d2 | -12.31908 | -50.29504 | 2026-09-29 04:17:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| d3d4b167-54b2-3250-b123-457f4df4957b | -15.24993 | -43.27277 | 2026-09-29 04:17:00 | NOAA-21 | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 169.3 |
| 2e5b6743-80f9-3794-af84-2fdde9c21d7c | -11.43477 | -43.46444 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 66b50e0e-b52d-30d4-a3e2-de86f5891f8a | -11.42696 | -43.44861 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4427a69-bea7-3af4-b44a-6abbc7f4017c | -15.46167 | -46.14761 | 2026-09-29 04:17:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 27de516a-8c1b-36db-b08c-7bf563b75bdb | -15.26882 | -46.54273 | 2026-09-29 04:17:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f251d509-8844-3798-920f-acbd157161d0 | -11.42811 | -43.4634 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| a6358242-1016-33a9-90d2-0c8b8c824ff0 | -14.18559 | -43.89902 | 2026-09-29 04:17:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5fccbe44-388f-3396-a195-b71dd54e279b | -11.63499 | -43.48813 | 2026-09-29 04:17:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5c732462-8d7b-365c-bc84-522027bf9734 | -12.012 | -50.93903 | 2026-09-29 04:17:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README25.md)
