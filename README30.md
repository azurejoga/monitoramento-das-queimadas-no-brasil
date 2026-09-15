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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ab06289e-1d72-3d0b-9a7a-4cb99daca0ed | -6.95928 | -44.54504 | 2026-09-15 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 7936c53a-9126-341e-bc77-78a09fcb4052 | -9.88088 | -47.77401 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f5131e28-fd94-3eeb-8bd0-ca3e339103d0 | -8.63632 | -44.4528 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2411c0f6-5e12-3d76-8bef-803c96d7296f | -12.4832 | -41.39737 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5ddce08c-2552-3e74-a454-e1cdf01406f5 | -13.4367 | -43.82444 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22ee01b2-2542-3b4a-ac70-8eb57db5ea87 | -6.73716 | -43.0913 | 2026-09-15 04:14:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1a869646-b8b0-3d97-9a37-afd04382e780 | -10.97601 | -48.32888 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| cb0d93f9-3a6b-38f7-8e39-96748d150faf | -8.65828 | -49.13319 | 2026-09-15 04:14:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 16edba17-3597-3cee-a6fb-cc83a572ff5b | -10.98072 | -48.32955 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a3059a38-5be6-3dbb-b082-c9aca124086e | -6.94681 | -42.56276 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1dc3bc1a-4894-3eaf-b74d-71d0b68cda44 | -7.4585 | -46.14877 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f71ab329-d4ff-3dfe-afd3-95812a5793c2 | -9.36105 | -50.10139 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 43df3cb9-a2c5-3ce4-ba2d-c5ddcbb6ec1f | -9.35906 | -50.11184 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5816e1ee-2ab9-3e3a-8f8d-322f65fec97f | -6.32616 | -44.11787 | 2026-09-15 04:14:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6f0b7725-c4d0-347d-85d9-3e42841d48cb | -7.02422 | -44.63354 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 697857ca-d63b-3e25-8880-129c17ff52c9 | -13.55597 | -43.52854 | 2026-09-15 04:14:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36a562b2-00eb-3c86-92ed-fdcf76a419cd | -7.02114 | -44.6279 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| baf92cba-148f-3d93-b3f5-6d541a8dc557 | -6.95861 | -42.55676 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7848131b-31a1-34bd-9871-c59ae8937b27 | -9.28294 | -49.78354 | 2026-09-15 04:14:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aee9d55b-977b-3f01-8617-5b58be346552 | -12.97997 | -41.07148 | 2026-09-15 04:14:00 | NPP-375D | ITAETÉ | BAHIA | Brasil | 2915007 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 221d16bf-a799-34bd-b69c-fbf43acc64f6 | -11.88958 | -43.82765 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e7aad448-1e5b-3f78-b6f5-26107b0ca210 | -10.898 | -51.54522 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9461fdf6-e34d-3722-879f-1e4da7b97fad | -8.09411 | -43.7811 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 9d0feb55-25ce-3615-8aea-676cc05f5a3c | -8.39383 | -42.21793 | 2026-09-15 04:14:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 3a5e902c-b14e-3fd7-aec1-a1c438259402 | -7.08776 | -41.82687 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 5ed65228-8fcc-3f91-8315-992c0c804295 | -7.2179 | -46.13696 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 074c0ce3-a26f-37fa-8145-fc0e8f6714fa | -12.50727 | -44.62998 | 2026-09-15 04:14:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c5e03724-8571-3932-a81f-15a77ceea716 | -8.28967 | -41.35669 | 2026-09-15 04:14:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| cf17d4cb-284a-3dc4-9c1a-ff4be73c1391 | -5.87176 | -43.50875 | 2026-09-15 04:14:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ced34e67-ad49-3fa2-be6a-e52d919ad665 | -7.17045 | -43.60385 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72b997e9-1a3f-33eb-a323-5ee61d4cfae0 | -7.16567 | -42.10315 | 2026-09-15 04:14:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a7df8602-e7c0-3a19-a0c8-23e57209c622 | -12.47542 | -41.40333 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ee903129-7f17-3e06-95de-5fa4209dba5a | -11.13575 | -47.72034 | 2026-09-15 04:14:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2901fc59-eb14-36d5-8dd3-0958af45bde3 | -6.15798 | -52.73503 | 2026-09-15 04:14:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 21be42b6-dcca-352e-8f94-b0b794c75800 | -6.43066 | -43.06913 | 2026-09-15 04:14:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dafb8d5c-5c39-3c10-9b66-4582b86be80f | -10.88439 | -51.55767 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 74b6c7fe-0aad-3474-bfff-12b74fc2508c | -7.09578 | -41.82061 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8b706e8c-567e-364b-b18e-9ceb064c9b2a | -9.15924 | -49.99154 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 408764c9-54a6-38a1-8575-9d74caa24a8a | -6.95032 | -42.56335 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| ca294e7d-02a3-36b6-8f74-d06d7865dfd0 | -12.47875 | -41.40388 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| deef1363-7dbe-3be5-afdf-b3c50a500446 | -9.3607 | -50.19213 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8bd3492d-dea1-3743-a00f-82a911570bbb | -10.68052 | -54.1765 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faf94c69-d11c-3695-a701-1cf46b273468 | -10.58084 | -47.74558 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eca511be-7bc2-3d7a-9230-2f9639f07762 | -7.24751 | -46.17149 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| a70c6bd8-e622-37bd-84da-5c3f0083565d | -11.23189 | -43.46468 | 2026-09-15 04:14:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a61f05d7-02f6-331b-a0ef-a5baf1ca73a5 | -12.02995 | -47.81436 | 2026-09-15 04:14:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 494678d9-3bd2-30c8-8232-dbc6b9708ec2 | -11.17184 | -46.38455 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| db81c32c-818c-388a-8d16-24ed82335dd5 | -6.78927 | -46.4567 | 2026-09-15 04:14:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 753f9c67-e6b2-3ef6-86ed-a9296bc8d806 | -9.45815 | -48.90707 | 2026-09-15 04:14:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| e96b2c40-d235-3209-aa6a-61cc519d9e44 | -7.2432 | -46.17069 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 7bafcca3-b1b0-369a-bc0f-4fffb73195ba | -7.56546 | -46.31365 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 90ba5061-2bc5-3e3d-9329-4efbcf41f40c | -9.41596 | -47.85355 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2cd3b3b3-cd66-387d-9f62-36594ecd5a9a | -6.26027 | -41.95186 | 2026-09-15 04:14:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 404887c9-14c1-3e1e-b7c2-ed2057dadbee | -7.1038 | -47.48029 | 2026-09-15 04:14:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d8043dc4-1376-3815-93ba-3e15bc6ad8d2 | -6.9562 | -44.53954 | 2026-09-15 04:14:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| f0e77200-454a-3dd1-ba00-a4681fc239b8 | -11.13654 | -47.71598 | 2026-09-15 04:14:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6590dcbc-3a5c-3b6b-9e0a-3a31bdccfa4a | -11.80107 | -46.59467 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40516041-5b8b-3299-9119-da5d5ae42f34 | -11.89094 | -43.81965 | 2026-09-15 04:14:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 37.3 |
| b8bdfd03-eb10-34d5-a350-61fa0be43dc6 | -11.8119 | -46.58138 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db56e4e7-33f7-3957-975a-6bfd7864e5af | -7.29118 | -46.75199 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 47da94d1-7264-3f4c-a9d2-9902f61405a9 | -13.80658 | -39.01068 | 2026-09-15 04:14:00 | NPP-375D | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 88826a9b-8b99-321e-a02a-82d9edc928e3 | -10.24427 | -50.90933 | 2026-09-15 04:14:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3e10e8d7-b3ab-3958-b7d6-3c8cd9e5b2f6 | -10.6953 | -54.17332 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f9b826bc-d94b-3920-a8e4-1ceb4a00e31d | -8.304 | -39.52237 | 2026-09-15 04:14:00 | NPP-375D | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| c340199b-4b67-303b-8635-96b3b8362f94 | -7.25025 | -46.15525 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 316c6840-9cf0-3a4b-bba2-8830f9f81f3b | -7.11058 | -42.09408 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ac0f0712-c704-375a-9ae1-3e75a11d040b | -12.12457 | -44.21714 | 2026-09-15 04:14:00 | NPP-375D | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9aa8642b-3546-3240-9d07-511b6c332d12 | -7.13246 | -42.08995 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| e03f4d8f-da33-31c6-aa48-190148738817 | -11.17678 | -42.80802 | 2026-09-15 04:14:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 8a39f5eb-2261-3dca-be3d-8587e03ecbbe | -9.36449 | -50.10612 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8fbe538-2555-3ee8-8623-f1764e3c2482 | -10.67928 | -54.18259 | 2026-09-15 04:14:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5b0d54bd-8332-3397-bc1a-b46a221a242d | -10.70079 | -47.50529 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9d88bf58-253c-3f2b-80a6-7ea4e52fd9a2 | -11.49542 | -45.75152 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a379a973-e952-319a-b2d2-299ff863646a | -7.02031 | -44.63285 | 2026-09-15 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 440ee986-e58f-3b38-95a7-a48973740b1a | -12.49036 | -41.41666 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c6d601e7-ad50-3ead-aad7-afb66af99c60 | -9.35574 | -50.12927 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9ede68a8-9ef0-3f7e-bdd4-385b7b71f804 | -9.45549 | -40.39285 | 2026-09-15 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 32.2 |
| 33abde85-ffdc-3f67-affb-81fd4b2db095 | -5.35715 | -47.70738 | 2026-09-15 04:14:00 | NPP-375D | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd4875ed-58f3-324b-855d-5c3e87a926a0 | -10.42174 | -48.63939 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d54300e-734a-3d22-a846-a57e3886ee66 | -7.09434 | -43.54862 | 2026-09-15 04:14:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3e2095f7-5ced-3c82-aa86-b80bb7b436fa | -8.81314 | -50.48825 | 2026-09-15 04:14:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41423117-1414-3e67-b757-341ed6cc2149 | -7.08338 | -42.10894 | 2026-09-15 04:14:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| be9bcb61-e613-3b3a-a0c6-2d46389b4d44 | -7.1152 | -41.80878 | 2026-09-15 04:14:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4311686-0586-3feb-aa82-473874e494b1 | -10.89911 | -51.54356 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a72ce05a-bcb6-3941-966e-f791c4e80c54 | -10.42576 | -48.64461 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c076854b-a054-3d5a-9d0a-82f49012deb1 | -10.57798 | -47.73562 | 2026-09-15 04:14:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 162f3e83-d8fe-3752-aebe-908bf40a28d9 | -8.80314 | -46.91005 | 2026-09-15 04:14:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b7386a4d-8a2b-3f4e-be50-27d9da87eda8 | -9.36646 | -50.10245 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 0ccf97af-5dce-30e1-89b3-5123dada5cbd | -12.47931 | -41.40035 | 2026-09-15 04:14:00 | NPP-375D | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 94f864b8-d918-371e-8648-3e7754902f76 | -6.52613 | -42.24598 | 2026-09-15 04:14:00 | NPP-375D | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| b63a937a-07af-38f5-9684-a2a5306aec97 | -10.98175 | -48.32405 | 2026-09-15 04:14:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4d8b1c1f-9043-3de7-a686-157c7c305de6 | -9.3563 | -50.09687 | 2026-09-15 04:14:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 701ddcce-a332-3e86-9554-5165ea731304 | -6.75276 | -39.81633 | 2026-09-15 04:14:00 | NPP-375D | TARRAFAS | CEARÁ | Brasil | 2313252 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77d6a77e-5964-3f1d-8912-e68492090b77 | -7.23376 | -46.14792 | 2026-09-15 04:14:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4c62c0b4-0a4c-3540-81ca-81495d933a87 | -7.55586 | -46.87082 | 2026-09-15 04:14:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f594095-14ad-38f8-8106-257e83ff57d7 | -9.88923 | -47.78042 | 2026-09-15 04:14:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3ab5d33a-f87c-3c47-b756-b1b4050ba1f8 | -12.72553 | -40.2777 | 2026-09-15 04:14:00 | NPP-375D | ITABERABA | BAHIA | Brasil | 2914703 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a4580708-d0d4-3cd4-95a1-3c827340bd4e | -11.79977 | -46.60207 | 2026-09-15 04:14:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3947dd11-f193-3381-a0b6-df76807a1844 | -10.88938 | -51.56295 | 2026-09-15 04:14:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c1dce6f0-e3bf-3ee4-b860-0cc898386c60 | -8.59751 | -44.4753 | 2026-09-15 04:14:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |


[Clique aqui para ver as próximas entradas](README31.md)
