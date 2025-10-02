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
| 1d7def75-e664-34f3-8217-5562d3ba875c | -12.14809 | -46.67507 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6c5de04c-a87a-3dfa-ba49-5445000510fd | -12.83968 | -46.86344 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7bc2ba0d-0047-3aba-8fef-6dc08e5fbe4e | -8.90753 | -46.06563 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7250556e-72e2-3a81-804d-892ffa96c203 | -6.412 | -43.84452 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d9c737ec-8516-3adc-af12-9674e49455b6 | -7.17 | -41.69645 | 2025-10-02 04:02:00 | NOAA-21 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| a647c100-a779-3ade-9d0e-cb184a897d1b | -10.23527 | -50.3265 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 22.2 |
| b6ee7066-67c7-3941-8258-d750cbe2dabd | -11.34624 | -44.97502 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 78051e60-5eeb-354e-8d08-f5295e944c2e | -11.44873 | -44.96831 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 840c9b56-3b30-3358-9dfa-6653c4213af4 | -11.66894 | -44.28355 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e668911-b6ae-3c94-a8a7-1dbc005e4b29 | -10.88404 | -44.28243 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bffc9cf5-9bf5-3645-8aaf-867f90f6a25f | -5.78578 | -45.74864 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2ad45f4f-43bd-3e5a-97c0-7ecac4a7dd6a | -11.01169 | -49.57722 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d6f6970-f2d4-3600-96ed-190c7b3d1745 | -6.54631 | -45.21803 | 2025-10-02 04:02:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b5e9b14c-da8f-39d5-86e5-e242bab4d4d5 | -11.46872 | -45.06268 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 49b26641-792c-360a-b802-ccb20480c3ee | -9.93761 | -43.77375 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 3cd2e6b5-67d4-310f-86f8-acdae96c8acf | -11.60562 | -45.05747 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f4f2c7fd-fdbb-372c-a2d0-499d4cbd2c93 | -12.02145 | -46.63291 | 2025-10-02 04:02:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8f1f088b-2923-3d63-91e0-f96d93b67956 | -12.95125 | -46.37177 | 2025-10-02 04:02:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6c49fbc-5c2c-38ea-9765-02e87509cc8b | -12.81666 | -47.01612 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 887ccbb9-fd1d-3e53-8b8a-c6f353b98e06 | -11.80882 | -44.9973 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5fdbcbd5-2539-349c-bcb6-bf84095d963d | -9.90977 | -43.67671 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1859213c-d548-3de9-9707-3ad5ce4f7a7e | -10.22459 | -48.22332 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 90d5a620-cb56-3ebb-b644-38638b3beae1 | -13.00911 | -45.20605 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| bc64c352-c6fd-32e0-9873-77380df0f0a5 | -11.4832 | -45.11239 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b94366dc-cbfe-3aa9-8c32-ba4428443e6a | -8.71652 | -47.14443 | 2025-10-02 04:02:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cd803a0b-3623-3f24-9b79-3e154b1bd1c6 | -7.04672 | -43.31144 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a8f414ea-e454-308d-98bf-cbb9dbe82067 | -11.62141 | -45.05481 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 89cb56c2-2cfb-32c9-b4ea-e4b17056a6ac | -7.77898 | -42.51813 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 6d52b84c-0bdf-3546-9a71-c9e187390599 | -12.51307 | -46.83744 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7c57d2f3-3d6e-3bb1-affa-19839ffbf1a3 | -12.65691 | -46.95156 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8132973b-9ef7-3ec0-a3f2-91e8f7230978 | -10.22715 | -48.20904 | 2025-10-02 04:02:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e2cfa0e-3ae2-3fcc-a193-5afc810987bc | -11.27959 | -47.82069 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| acf72965-04e8-3c95-952a-d8ddedd3fd05 | -11.81413 | -45.0243 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 61e39382-725c-35d0-b709-a7fe4a601c4d | -11.0868 | -47.81118 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39542f2a-48cd-38cc-8511-caa599cb345d | -12.22379 | -43.76105 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 052b7446-08ae-3242-be79-b7ff4b417e9d | -11.47106 | -44.99466 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7596aa2c-1eac-312c-bf41-b3ec4862c26a | -12.77235 | -44.91963 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 385ad5e7-5289-3564-94cf-af244a6807c4 | -8.41437 | -47.75024 | 2025-10-02 04:02:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9148cb58-a1c8-3f9f-9dc4-dbfc587d81b7 | -6.35926 | -42.89511 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 9112907c-c5b7-3b32-81c7-49f2775f5cb3 | -12.89842 | -46.90864 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 445e0cde-4f64-359c-9aa7-47c0f8ad9d75 | -11.68135 | -46.97693 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fc178229-c9b5-349e-8c2f-294278a01b09 | -12.12363 | -43.427 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 29b4eb85-ef33-3f20-916a-6e18cb7f6ee4 | -11.85223 | -44.98002 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 7633a169-0842-36fe-ac4f-f5231b7c012f | -12.41413 | -45.17184 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 748e3227-46da-35ca-95b6-8141523d9592 | -10.23868 | -50.33787 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 43f16465-4067-3ba1-aa91-6a7c42fcfaf1 | -11.79549 | -47.5692 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16ea98a3-77fe-32cf-aa42-c41f7907d52d | -10.29115 | -45.18554 | 2025-10-02 04:02:00 | NOAA-21 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 10c8b3e9-3215-3bc6-8d13-2bfb67a95715 | -10.82761 | -46.63313 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| d16d02d6-85d7-31fb-8f55-eafa618887f2 | -6.5419 | -43.37149 | 2025-10-02 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| beff9725-6e85-3176-9727-3b186d1c68e9 | -10.20918 | -50.2716 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 901c4516-e8d0-3fa0-9e88-35a2b39df99f | -12.42101 | -44.08987 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3767a02c-ab7e-31a7-a58b-67eaa6fa6802 | -9.93694 | -43.77787 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 0f6a4689-2a9d-3ff3-9bfc-fd0eb7f3f6c4 | -12.88705 | -46.92924 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 04f560bc-e9c0-3c12-8dd3-bd2b889e694d | -6.22539 | -45.33345 | 2025-10-02 04:02:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| d80bcfa0-0aa0-361c-bf40-0baf3c66d92f | -8.50976 | -44.70026 | 2025-10-02 04:02:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2a392321-bb87-3443-90be-40c7eb329935 | -12.77456 | -44.90654 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5355c4a7-9b10-3d73-9f1b-6fe85ad33d66 | -8.78897 | -44.8015 | 2025-10-02 04:02:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d04e60e5-95d7-3d27-9037-d57489144c62 | -11.45577 | -43.51086 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dd64b8c5-2e01-3f21-8011-da768739f7d1 | -12.81664 | -47.04008 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 70b373b9-a8e9-3ef6-87a3-87043c8fe192 | -12.47907 | -47.27004 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 44f608af-61fe-327d-87fd-774920d0e759 | -12.248 | -47.8304 | 2025-10-02 04:02:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| df027c49-c2a2-3436-8fc8-3f4ebd3bc980 | -10.89846 | -44.28489 | 2025-10-02 04:02:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 91f6af60-81ca-3e67-998c-221703d31c18 | -12.1149 | -43.43721 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52962961-2064-30ee-8801-1d426f187b9c | -7.84361 | -42.85561 | 2025-10-02 04:02:00 | NOAA-21 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a1285a20-83d3-3e59-b40d-1e46c8b08dbd | -7.01103 | -44.49887 | 2025-10-02 04:02:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 61de8d0c-238b-35af-ada8-d2473496df99 | -10.82651 | -43.66689 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 22b03f00-a496-3532-a390-fadc203ccb00 | -9.94497 | -43.72864 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 925a3bf4-8016-3b20-afb9-d78c6f8aeeae | -12.75322 | -46.90259 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38310523-0019-3a4e-bf89-0430d2354aee | -12.79905 | -46.85742 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f885dd7b-bec6-35ac-a44f-c0e4635e7302 | -12.66503 | -46.85691 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00a15ab8-d277-3931-b640-d3d27065bec9 | -11.72104 | -44.46892 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 909b621a-b766-37f7-858a-6acdf791c0f4 | -12.86465 | -46.93661 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47f2ecf4-50c7-3c1f-aea0-59ed70fad4aa | -9.94785 | -43.73333 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 28a8ba90-aefc-3e75-bddf-9844525987e7 | -11.19192 | -47.18813 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 6cc0e8a7-a46a-3e9a-a390-37ff7ce49612 | -6.3192 | -43.88744 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a332cd6-c19a-324f-9303-880039b01b23 | -11.81632 | -44.90697 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 03e16fcc-bea6-359b-8843-f39373001bdc | -6.11432 | -41.79059 | 2025-10-02 04:02:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c09bc03f-0e53-3cec-8faa-81deb708a153 | -6.72249 | -44.55731 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ac3d6093-25a9-33cc-8cda-a95516ed6c72 | -9.80526 | -47.84667 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db49e0df-8d88-3209-9fc5-b2b59cf4c160 | -12.89781 | -46.91201 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| b7e2db83-ecd5-3b97-8d85-28c19dfa5163 | -12.27609 | -44.12842 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 970f4a35-24e5-3929-8213-34c5feaa244d | -11.7998 | -47.57015 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 11e3c6e7-567a-3bf9-bc6b-979f1ad6814a | -9.44809 | -50.89964 | 2025-10-02 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 626899da-1d84-3816-9b48-e03acf39039f | -8.64286 | -43.9765 | 2025-10-02 04:02:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c9f08003-c59f-3aad-9637-a6ccf716ac50 | -11.91203 | -47.88251 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| d6924298-a9c1-3789-b267-04e705b5f185 | -11.46656 | -44.99869 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 763b9f2f-fe8d-3887-b939-4adb687db606 | -9.93145 | -43.72213 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4c5af02d-61f6-3f1d-a92f-f4dd6c941f1b | -8.20944 | -45.52449 | 2025-10-02 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab9eb5c1-f922-3412-bcdc-ea60d6941a75 | -11.44949 | -44.96382 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0d0c6905-74b2-3ca0-8ad6-092241cb62e8 | -11.4992 | -43.50628 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43b3101c-2327-3de9-be1c-30f76e233e86 | -11.56853 | -47.02564 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5e02c275-9486-3230-991b-f19826a35567 | -12.27994 | -45.36711 | 2025-10-02 04:02:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a974d2e-8cff-3365-85be-e5da16c640a7 | -5.98432 | -44.58726 | 2025-10-02 04:02:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ba669120-239a-3c8a-be20-0e5048ebaf55 | -11.92981 | -47.05358 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f9c0f92-179e-35e0-98c9-a8401643a214 | -11.51703 | -43.54106 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4f48c73b-600f-3d70-8e41-35686e9f8aee | -10.96382 | -46.64838 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 509d1485-2729-3d34-a6e4-200524342ee1 | -6.66657 | -41.39456 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 65928b4b-3f40-3da3-a56f-e26f0601de41 | -9.92875 | -43.73856 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 159.4 |
| b4deaca2-3eab-36c5-884b-2d209a6a08fa | -9.45061 | -50.90089 | 2025-10-02 04:02:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| bd89bf8e-f33c-3581-a708-9e112d73dd50 | -10.82268 | -46.61247 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README25.md)
