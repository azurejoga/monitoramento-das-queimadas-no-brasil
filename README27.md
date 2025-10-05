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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79ffaa93-6c7c-35e5-a8ed-b255871bb5c8 | -11.02203 | -46.7071 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 068bec7d-e94f-39ae-b5d5-e9dc06a25ba4 | -13.57989 | -48.16854 | 2025-10-05 03:34:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| eaa12cea-313c-30e7-9d97-38937e19babf | -11.7609 | -44.73908 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e0b7865-ae07-32a4-8514-1a51cecc848d | -7.77939 | -42.61102 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| f2861a62-48aa-36de-a6c9-097c83093308 | -11.92144 | -46.26075 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b5795d77-332e-3aa9-a085-b0b81fd9c0ef | -13.30191 | -47.80644 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| bb2e0d68-5219-3dae-8c4c-1c1706f58236 | -7.46008 | -43.05743 | 2025-10-05 03:34:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 7cdd0d0f-b21a-3f86-bfc8-6c7eeef20ff3 | -11.80415 | -46.85284 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 14c7f2e6-e422-3720-85ac-10ae1cdf1cc4 | -7.78162 | -42.60428 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8db0b175-a84b-327e-86e2-9ebdda008684 | -10.75819 | -46.61594 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 9672dbf5-b271-35e1-90dd-f248c7d3d80d | -7.5177 | -41.27215 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 65836bc7-00f5-3434-abe0-58b7a87ebd01 | -13.73682 | -48.07708 | 2025-10-05 03:34:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 665af6a5-3cfa-3734-beac-ab61ecd7779b | -8.58584 | -46.29808 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| bb9fe8f6-18a2-3200-8aa7-4eb0ffabf4e9 | -12.46298 | -45.52182 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 82a9a5d7-3352-38e8-b746-4b6f740e93cd | -13.07754 | -47.92304 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 67f75e4e-b71a-3ea0-af3e-61761cf413a7 | -8.6056 | -46.27128 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5eef01f6-7a89-3b9e-8655-ba5471e00e8a | -13.37959 | -47.55264 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 875b43e4-3c81-350c-8d5b-7f3a31d93343 | -9.05933 | -47.02353 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f502f8a9-b171-3579-b53a-040e4f1326e7 | -11.02185 | -46.71366 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e517b796-4046-35de-bef2-a78ea1a55c42 | -13.2616 | -47.82093 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8d2c391e-5300-3f54-858a-bd930f652d97 | -13.30721 | -48.08949 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a7b75546-8539-312e-b390-e1a2c1cf03cc | -8.53435 | -46.33694 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c704b55-fcff-37b5-8389-f12d041ddfcb | -14.01334 | -44.92927 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f9dc93a5-4d32-3401-ab6c-5fe0b4f24b31 | -11.92021 | -46.25364 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 82587634-ba5e-38d6-a0d1-5993b4b22d30 | -10.20744 | -40.54605 | 2025-10-05 03:34:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 03905227-6eaf-3e4e-842e-a693400d0778 | -8.55125 | -46.2732 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 84e6a349-aac5-3e6a-975c-67b129a5ac22 | -14.88148 | -40.83414 | 2025-10-05 03:34:00 | NPP-375D | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 64f98818-1efa-3700-8f6b-238e94f8f103 | -7.7218 | -46.27478 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 857e5c03-3830-34a2-997d-4e582dafbfec | -9.29791 | -45.99328 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| e6af7e7c-03bf-38c9-99b0-c78ee64d8980 | -11.82061 | -45.04613 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f50c6c46-d090-3148-b35c-570b403767cf | -11.75481 | -44.74142 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 493be003-706e-30b0-a397-0e0811c5316c | -7.79969 | -42.57082 | 2025-10-05 03:34:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 3eeff6ef-0e14-394d-977e-aaa86e0e9719 | -8.54406 | -46.32481 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| b451a593-8602-312c-93a7-9446c7c49910 | -7.77287 | -42.61442 | 2025-10-05 03:34:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| aeedcc45-39a3-3578-84b4-bab5c1fbd492 | -8.56977 | -46.32653 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| f037647c-f831-31c9-974a-9868ddc32fb3 | -8.58935 | -46.30191 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 969997ba-6de5-3b2a-9022-8dcf5297cb0a | -12.70187 | -45.85992 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4b5eb265-b1b4-3b00-95b6-631088b46e0b | -7.79278 | -44.54815 | 2025-10-05 03:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6d7b8a40-87c2-3407-82e6-c4707253d7a3 | -8.78737 | -40.57209 | 2025-10-05 03:34:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 3d75d247-2330-3e54-ad60-2e4236f43a1f | -11.11854 | -47.2069 | 2025-10-05 03:34:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6c5b757b-430a-3370-bda4-0267e6807b26 | -13.28288 | -47.82544 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 307f3e8c-1eea-3339-9f88-9a578523437e | -13.26834 | -47.60769 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 398e8211-36cb-304e-b09e-c632c61f8e4c | -13.31352 | -47.56804 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fee716d8-3bf7-3260-8ca5-479064ff8e3d | -11.82488 | -45.07716 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b012361-e4f9-3c09-8522-aad5d567b690 | -13.12554 | -43.84846 | 2025-10-05 03:34:00 | NPP-375D | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 78ce5cf7-19fc-3897-9a05-3ca9399f8dd0 | -12.70296 | -45.8546 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5e740491-3cd9-35a6-b082-519b43db187d | -13.26994 | -47.60034 | 2025-10-05 03:34:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0f8bfd09-a6a3-3e73-ae5d-782ef8392c8d | -14.27814 | -45.86859 | 2025-10-05 03:34:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0200d2a9-9dab-3db2-8dbd-948ed118c154 | -11.86841 | -44.95874 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bff7436f-c858-3f80-af33-aff64510fd42 | -8.59159 | -46.30614 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| ba5a131a-cd74-3cbb-98e7-1f79942ff0de | -13.31194 | -47.17492 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53bca0ee-284c-3658-ac95-61091624c9e7 | -8.55852 | -46.36343 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad92e11c-ba33-3e32-b4e9-8a4812173a67 | -10.94445 | -47.08958 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 95.1 |
| 357812c8-8604-35b7-8496-23cade63972f | -11.70398 | -47.51257 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| c275e5b3-f84d-31cb-a0b1-12f79a74e34e | -11.82786 | -45.09426 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2a153561-01b6-398b-9e56-7de11019841d | -13.29741 | -47.81465 | 2025-10-05 03:34:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7d9c9aa4-9917-3d3c-87b3-591106f3035c | -8.55709 | -46.31676 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| ce3f16e0-28e2-3160-bba9-a22090f4d034 | -11.83182 | -45.08746 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 2f49517e-1362-35d4-aaa2-631a857f7c90 | -10.8706 | -45.4157 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8030141f-c0c4-32a6-960f-08fc8ab8eff6 | -8.18479 | -44.13789 | 2025-10-05 03:34:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6a55233e-3a60-3ce6-bdc4-01749d61295b | -8.16493 | -43.34705 | 2025-10-05 03:34:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 9a49637a-3cfb-35b7-8e36-e7c58d7b701a | -9.26427 | -40.49977 | 2025-10-05 03:34:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 969351b4-d85d-32d3-b03e-236a2222b4ed | -10.94033 | -47.0738 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 47.5 |
| 893ceb83-79ca-3d1b-9e28-c72e6764c49a | -12.45775 | -45.51517 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 230b62e5-ba41-376e-a1a6-0a4736685620 | -8.55834 | -46.27428 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8f6c9125-c476-3393-815e-cb867c466928 | -7.74878 | -42.51976 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| f2816a3e-0f5e-39a1-af70-96137633dab4 | -9.05206 | -47.02208 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b900e44-528f-3bae-a709-5149da6304a8 | -9.57116 | -46.11979 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d9bfa49a-a11f-3a64-8061-e60be4ed64ba | -12.92428 | -47.31109 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3bb07028-962d-3328-b33c-0beb1d7caf7e | -11.01492 | -46.71224 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| f353cd39-37c8-3c08-9ee1-2e710118c20e | -13.2732 | -47.18875 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 60ec002c-04c2-307d-9c00-32da32620f82 | -11.00184 | -45.59301 | 2025-10-05 03:34:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2afcaadc-7d89-343d-85c1-3854e6d45f5f | -12.45849 | -44.63735 | 2025-10-05 03:34:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| eb821326-ed7c-3e8e-b721-fa28983ff073 | -11.70553 | -47.50548 | 2025-10-05 03:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| cc09c3cb-0832-334e-8e10-5eeb234cfa91 | -11.81341 | -45.08235 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c103780-d555-3b64-a69d-8a89801e00ed | -8.58325 | -46.31146 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| c0b59284-5c8e-37f1-a0b9-69b570568c23 | -13.27293 | -47.1895 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 28eff997-9437-34ae-a7f8-50c339094eaf | -12.45704 | -44.73661 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c3d6056b-4965-370c-a0fc-1fdfc990068f | -10.39161 | -45.40178 | 2025-10-05 03:34:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1224b627-6a7e-3cdf-abce-d3df3dcc1695 | -13.28147 | -47.18356 | 2025-10-05 03:34:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ae08cb1c-2801-3c1e-90d1-dac096adab79 | -12.46919 | -45.53164 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 64ae1ddf-5db5-3c77-b962-15b4be23c6fc | -13.67517 | -43.18572 | 2025-10-05 03:34:00 | NPP-375D | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 849f1ccc-e752-3bd4-ab90-58ffb24a3d36 | -12.81781 | -46.85069 | 2025-10-05 03:34:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 68b0c92c-d8e1-39eb-8c0c-12c7cfee60b9 | -12.08327 | -45.1492 | 2025-10-05 03:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3c6b543-5624-3c7e-b75b-3486d0131270 | -7.51245 | -41.27108 | 2025-10-05 03:34:00 | NPP-375D | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| f145f9d7-0eae-3aaa-a71e-9546a6aa0a0c | -11.83482 | -45.09193 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d440b423-b08c-34b9-bd68-5f596b74ba5b | -7.54214 | -42.41095 | 2025-10-05 03:34:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1c2bea2b-fa6b-3503-ab16-14ae7406b5f6 | -12.46718 | -45.53355 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ec7b7842-4a86-3cb5-972f-4c40300572eb | -11.80198 | -46.82904 | 2025-10-05 03:34:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53fa575c-c8b9-3592-a2fd-05e0b90ada65 | -11.83637 | -45.05268 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1ac5ea4b-67f8-32b5-b985-74354368be52 | -11.91 | -46.23563 | 2025-10-05 03:34:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b7bb7b80-c6bf-337d-8725-2d42e4279df8 | -7.79387 | -44.5424 | 2025-10-05 03:34:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 49f7ee8c-099b-37f2-86de-a69cbe007ce5 | -7.74233 | -42.52283 | 2025-10-05 03:34:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 699dc79e-be4c-32a6-9855-43927f8d0c87 | -9.27371 | -46.00689 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4a66a363-80a9-37e5-9c5a-83977684b7a6 | -8.57544 | -46.33482 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 5539c357-c01d-3632-8124-1eb43ca5ada2 | -12.70326 | -45.85596 | 2025-10-05 03:34:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 151b24a0-5904-3a39-972f-205e727afe8c | -10.64126 | -46.34757 | 2025-10-05 03:34:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bfa3a7fa-41cd-30ef-bdb3-a4e86ba555e6 | -9.65189 | -45.85706 | 2025-10-05 03:34:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| ef7ed916-9c82-34aa-893c-8cd8b4450bf9 | -7.80095 | -46.02198 | 2025-10-05 03:34:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| fd4db936-ef1e-3b32-9a53-16c76bd946c3 | -11.62974 | -45.02511 | 2025-10-05 03:34:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README28.md)
