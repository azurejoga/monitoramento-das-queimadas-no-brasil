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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2c8a6d5-c876-3aa8-9f4a-faf8f697a234 | -11.76258 | -50.5498 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e91f98dd-b0d8-34f7-a285-2b2aac699448 | -9.39395 | -60.56687 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a03c75da-7062-380a-8106-d7e60c5ee97a | -6.92418 | -59.6457 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d8a17263-d965-3cc7-8ad7-0156374de71b | -9.66473 | -46.52913 | 2026-09-02 04:57:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a39876a0-0eb9-3789-a8c9-aee5e08d2969 | -11.3046 | -45.1715 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 245466a9-0e6b-3486-b764-4528f61d9d34 | -7.31627 | -51.215 | 2026-09-02 04:57:00 | NPP-375D | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a82e085-dba5-3a77-9ac7-393e8f32b13c | -8.74888 | -62.56364 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| b58504cc-2177-3992-b0ab-895d88d2a4b6 | -11.65865 | -50.20026 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b5f517f-7a56-385b-b344-c9b3bd9cf8de | -8.4575 | -54.70182 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| de8ed1a7-2bdc-3dd3-b345-3aaab5f0785e | -9.39292 | -51.6896 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f92d39f4-c96b-35e2-8d23-4ccdee5bcc14 | -10.84908 | -54.04148 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ee1915fa-ba29-35fc-8776-326ed01e8e8b | -10.79157 | -44.75381 | 2026-09-02 04:57:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb892493-fc73-3295-a125-e2d4ac2a14c2 | -10.44322 | -46.71685 | 2026-09-02 04:57:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eca07c45-df30-33e5-a538-50d6929d2abd | -7.20448 | -60.66568 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 81c74659-ab6a-3971-a7f2-6e89349f9b6a | -14.32568 | -47.22836 | 2026-09-02 04:57:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8edea61-a8ba-3970-a18f-3d32e2119f37 | -12.14366 | -47.0736 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 99c81b35-6e01-3be0-b872-d5d6e96171a9 | -7.45562 | -46.15787 | 2026-09-02 04:57:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e519a676-0e95-3cfa-bbec-85231308e245 | -11.14502 | -51.57683 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 96fbc3fb-190c-384f-a66a-c7dc35cd0c4f | -9.22129 | -47.98218 | 2026-09-02 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 475a032d-f5aa-3d38-a2fb-cfd3a282a10f | -6.05565 | -57.73815 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a5518af0-e9b3-3080-8453-dbb0fe5e479e | -7.94282 | -52.45934 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 375f820e-d45d-38fc-a3d7-8a1fcfcba034 | -6.24777 | -55.43983 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 127d481e-8687-3352-bac2-52ae6489fa68 | -6.24733 | -55.43693 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6182b5b6-f145-34ed-b5ae-b19482650df0 | -6.42905 | -53.56392 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 52645aed-69c0-378e-846c-a631d5326e94 | -10.49256 | -59.6133 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7e22916-d9cf-3a2c-aa1c-965227525b5b | -6.87362 | -59.40276 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e26717b-b8a2-396c-9319-8c5a99b767f5 | -6.3165 | -54.75517 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9770b05a-c5e1-38e7-88f7-a0d4c6de76ec | -9.22196 | -47.97768 | 2026-09-02 04:57:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0cbe93b7-a0d4-3d33-9094-c29673ffefa4 | -8.26955 | -54.95694 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3da49714-86cf-3ea3-b1b2-66996f7481bb | -6.16671 | -52.6361 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 334c23f8-749d-3da1-b56a-61bba8f89df9 | -8.11956 | -54.95956 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 14.0 |
| f1d27811-6eb8-38a8-aa8d-4916c0c1641c | -8.48209 | -54.71024 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.3 |
| 48bf9a54-50df-3adc-83e9-a2e8b6105623 | -6.04893 | -53.83808 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c7fe64b6-19d1-3458-94fe-dc7a06f730bb | -6.9135 | -59.6469 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 70635a0c-0517-347c-a21b-0a25a7072abd | -9.40007 | -51.57972 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| afd7afd1-cfed-352e-acb8-a079d98f0973 | -11.6523 | -50.19534 | 2026-09-02 04:57:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cb3535b5-f93b-3c5a-9442-4a97a8ef1656 | -8.44957 | -54.70481 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c09ae689-c20f-35b8-8f7f-bfdfc956fd92 | -8.44393 | -54.7383 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0c2e2df2-f2a4-3d73-9c25-a7b4b1db57ac | -11.30526 | -45.1665 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d1848afb-903d-3d65-a996-e11067b91a53 | -12.09194 | -47.09644 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cb5c3f9f-52c8-37d2-ab5b-b88cba93549a | -8.43299 | -54.71496 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0c462996-34b1-377b-8374-51e9f9f398c1 | -6.94798 | -56.46035 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 37e373a2-e2b1-32aa-94ab-ed97c8749284 | -10.32248 | -49.94858 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffe0e05e-eab2-396b-8ace-00a7baf34ad3 | -10.13131 | -46.81826 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1eec2119-ba7b-30b1-b532-98c5a17c63d9 | -8.43087 | -54.72752 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 35321747-39bc-306b-8eb6-fb42d4774e49 | -8.91935 | -63.28223 | 2026-09-02 04:57:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 08e5d855-cb1e-37bf-a22e-f3f6075ca2ac | -11.12496 | -51.53 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9eed914c-9066-3b87-9b99-4d0ebc4f529e | -10.32651 | -49.94531 | 2026-09-02 04:57:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43911e9e-06b1-381a-af7d-bf0121ded1ac | -12.14415 | -47.13041 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 42f6d34d-6e53-37da-85c8-aa8cb2bc7ca1 | -11.3475 | -45.40683 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 81736be2-0372-3acf-93ca-5c3e773ebfc7 | -10.68247 | -54.0438 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| f86481a6-7fbf-364c-963a-390a685fc84c | -6.15746 | -57.72072 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d151aa9c-47b3-376f-b056-36d6cb4f0076 | -6.85518 | -59.47653 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| aa8fa70f-7b24-3c38-a86b-e34c9154d25b | -9.46525 | -50.31133 | 2026-09-02 04:57:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c5ed5db3-4281-38f3-9a95-04d84167e5f2 | -11.05553 | -51.52307 | 2026-09-02 04:57:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b90e02a7-f5e1-3213-9edd-2927754015f8 | -6.0748 | -57.95732 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 884040bf-89a3-3357-9412-071c6f30a0d3 | -6.12186 | -53.54445 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0415821b-33c7-39f8-ba6e-6070794e8489 | -8.71733 | -52.35997 | 2026-09-02 04:57:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a276abd1-1a87-3859-a571-ce92cc2761bd | -8.62285 | -54.85353 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2ff4715-202b-3480-b65b-eceadd0c1301 | -6.04407 | -53.84549 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 739e5c06-5d83-37e3-a19b-9408130469b6 | -6.15276 | -57.7759 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b1634d7-8d01-3c32-9def-a488f7d31664 | -10.78312 | -50.47697 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 207fc2fd-9909-3176-9e8a-519626e8bb6b | -6.94859 | -56.45663 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a5b7ef1-cb74-300c-b794-269bec91969b | -5.3302 | -60.14576 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1967809-92d4-3b39-bc95-201630a04ac3 | -6.15803 | -57.77222 | 2026-09-02 04:57:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42ceaf74-5cd4-326d-8306-16b7ab24278d | -10.50114 | -59.62029 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d96a8acf-a25c-3201-89f2-39c55715ccd0 | -8.75973 | -62.58685 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1d1e6b76-26f8-37e5-b062-27a70c752fe6 | -8.45117 | -54.7395 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 42111535-b843-34cf-8b99-6533999e4af6 | -12.08557 | -47.09936 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 72a583a5-5d26-370c-a9fa-ed8f142fb7e1 | -9.01918 | -65.45049 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2fa86dad-469f-3363-8fa7-dfee47138e18 | -11.36052 | -45.41376 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8eaa3638-6670-3b52-adf0-ce4344163359 | -12.87285 | -45.82298 | 2026-09-02 04:57:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c409e5bf-dee3-3263-8c04-c162902928f8 | -11.35506 | -50.62254 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9f822ddb-985d-384b-936e-6adfc8f980ed | -11.30656 | -45.15666 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 495eaae9-1986-33b5-b6ac-ad411e754003 | -12.37605 | -48.14827 | 2026-09-02 04:57:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e11a404f-5556-37fe-ad46-88a93d1175f3 | -6.25553 | -55.44106 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2baf4943-75c2-3fd5-ab9d-38c14b49ac7a | -7.21217 | -60.68486 | 2026-09-02 04:57:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5fed2c07-2598-3810-9cdb-9d76eb000ae7 | -5.97767 | -53.58945 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4cb5bb2e-9ea0-36c3-8879-595c778affce | -6.32022 | -54.7558 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee422d1c-20cf-3ce4-8a7a-a141ad61f315 | -9.87006 | -64.9738 | 2026-09-02 04:57:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 32ef42c8-42e2-3098-8fe1-10eb6337ec65 | -6.88011 | -59.39669 | 2026-09-02 04:57:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fe0d6191-aa3d-3d91-b46d-53ad83e5f247 | -5.48401 | -57.15427 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2fc369b7-4b6f-3bd1-b6b9-cfb051af08d5 | -9.02618 | -65.45197 | 2026-09-02 04:57:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| de4662c7-f6c4-3098-9da6-e38eb8a797df | -11.3562 | -50.61513 | 2026-09-02 04:57:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e617da31-967b-39df-8bfa-26227b09d343 | -11.29134 | -45.16479 | 2026-09-02 04:57:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 46930aca-5146-3992-895c-39c274b76bdd | -11.03701 | -54.10757 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 187c4f8b-3e3a-3809-ba93-33bd88b940aa | -6.38354 | -55.21866 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d00241f-4a93-37f7-80e5-58a5740f448e | -10.74645 | -54.03416 | 2026-09-02 04:57:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea88f95b-3bc2-3817-b4c0-6a63934b2d6f | -13.538 | -43.30748 | 2026-09-02 04:57:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5b59d61f-9852-3638-b6fb-9a0d37704cca | -6.27582 | -53.33368 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2e6e788-fbc6-386f-95f7-241ab1254ad5 | -6.15094 | -55.67984 | 2026-09-02 04:57:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 887afbe5-fc48-3b80-8b64-9a115f375e19 | -10.50177 | -59.62107 | 2026-09-02 04:57:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 00a3f659-bc42-3c0c-a1f9-b20eb17e4aee | -6.20166 | -53.47683 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 88fc7d9f-a0f9-34d9-9ec0-a87f86541f32 | -11.68601 | -46.73812 | 2026-09-02 04:57:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3a7c4894-e8a9-36a5-bae9-fe2973854226 | -6.07617 | -53.67046 | 2026-09-02 04:57:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f55fe20e-7344-3960-ba82-226a07d77bb4 | -11.53837 | -45.48058 | 2026-09-02 04:57:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a533a1e6-8727-3e29-bd60-e4ba9de21381 | -12.12512 | -47.05562 | 2026-09-02 04:57:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 424368dd-8c68-37b2-bca4-4f336437481b | -12.15339 | -47.12427 | 2026-09-02 04:57:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b2f81aec-384e-3935-8b10-ffa2049ed8d4 | -12.37564 | -39.56958 | 2026-09-02 04:57:00 | NPP-375D | RAFAEL JAMBEIRO | BAHIA | Brasil | 2925956 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| dcf3b084-2d1f-3616-a868-64e693f2b7b0 | -8.74803 | -62.568 | 2026-09-02 04:57:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |


[Clique aqui para ver as próximas entradas](README38.md)
