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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f3a74890-627f-36aa-b3a8-39a512ce9953 | -12.40462 | -46.47151 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 750a98a6-7e3e-3fc6-846c-c102068addeb | -9.45792 | -60.54961 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6652e4e6-4cbc-33cd-ac01-7c44892fac66 | -11.30558 | -43.64506 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9917814f-5246-3434-8dbf-1e594f26c731 | -9.69433 | -48.30836 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4250b794-41f8-3267-828f-ae3ab80abab3 | -11.8987 | -46.71381 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2d53cf8-1140-326a-b0b1-859c756d6696 | -11.75068 | -49.08833 | 2025-08-30 04:49:00 | NPP-375D | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 79558847-e7af-3b53-a9ea-de177efd8662 | -9.47654 | -48.8269 | 2025-08-30 04:49:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 17513fb7-0d0c-37b8-b2b0-d1e416f3fe02 | -7.09256 | -44.30798 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| a5f601c3-dd4d-3745-b7ab-c03a95458343 | -8.46002 | -43.63485 | 2025-08-30 04:49:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 086b8884-bbc8-3b7f-bf0b-67aca80cbc65 | -9.43823 | -60.53935 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 7084603f-8c1c-36cf-920d-8b7330172546 | -8.88542 | -47.16395 | 2025-08-30 04:49:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fa1d058a-a620-33cf-b78e-aea2f8a28b8e | -7.09731 | -44.5366 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 47aa6ee6-efac-355d-b64c-99c0d140174c | -7.43434 | -44.80819 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 52066c6b-2d6a-33d5-9eb9-a16ad6896cd1 | -7.39629 | -45.92963 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 280a79e1-7293-3e55-9656-8cb47db9b7ce | -11.85408 | -46.38508 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2906215-876b-3a80-ba93-928917b77b02 | -11.83735 | -46.78982 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1d90046-907c-371e-ae60-5cf4a8567c11 | -11.02012 | -52.47569 | 2025-08-30 04:49:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 073d7397-4278-3ef0-9a34-b04d3634d9f6 | -11.30907 | -43.61821 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97a110e0-325b-3d0c-8922-da289e76e391 | -8.90272 | -62.10086 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a90d2b15-34b5-3d28-8031-6474c9ff3e4f | -9.202 | -59.5455 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 35a62798-e235-3600-8b1e-5a4465efa331 | -11.84578 | -46.44686 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d1a76da1-7429-3bbd-973f-923287c78b6e | -10.02783 | -46.03313 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4beb00e-e919-3ec8-8ea8-85432a3eafcd | -8.69316 | -50.38381 | 2025-08-30 04:49:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f5466ad-4d10-3fc5-adb0-443c3093377d | -11.83165 | -46.86131 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5a347832-add8-34ee-8aa5-a924e8647a35 | -11.41523 | -46.91619 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f7da3455-02b7-3540-bd10-5d9c4c14193e | -10.37475 | -57.82462 | 2025-08-30 04:49:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ae160936-68a0-395b-b487-bbc77e5fe0c4 | -9.46019 | -62.33409 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 83912589-9bad-34fa-9e45-803bf2f6e681 | -10.49372 | -51.6333 | 2025-08-30 04:49:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2041cc1-fb0b-3a77-b28c-5819cde43c94 | -8.18217 | -61.38602 | 2025-08-30 04:49:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0d46ca14-1770-36d1-b044-8ac42ccce734 | -9.50623 | -45.38916 | 2025-08-30 04:49:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f836b75c-5b4d-38d1-9854-76818587ece1 | -9.24355 | -60.93037 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0334acf2-c0d7-30c1-8801-92e3f71533d6 | -7.7766 | -45.46484 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 184fda76-7ae9-316d-8f6e-bfe65deeb4fa | -11.83584 | -46.46174 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 38.8 |
| 0a9f3b67-8cb3-30a7-a464-a8082e0a22c7 | -9.44299 | -60.5432 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 499d5ebe-4afb-3ab5-89cb-d11bd8933315 | -9.08929 | -59.48746 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 90ae8585-e708-30b9-85e0-040addfa5665 | -9.44929 | -60.53801 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 1b94ea4f-ce49-3c89-840c-828afab1caaf | -8.87354 | -60.73486 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47a31e19-f525-39f0-a4e2-0cf4b78d5f14 | -7.09241 | -44.60303 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b7481015-1cbb-30b6-bdc3-e2e4789b8277 | -11.82737 | -46.46072 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e2aa0045-0654-3c7b-a4b8-2c3f2ec934a0 | -9.43988 | -60.55935 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 225e2cf5-0e85-398d-9b66-c53a64154548 | -7.96241 | -46.39259 | 2025-08-30 04:49:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 02b964ac-901a-38af-b51f-a31b1848c4f0 | -9.11793 | -65.77471 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1583ad45-fc7a-3221-8f85-328d8a41638b | -10.99475 | -46.84958 | 2025-08-30 04:49:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 34fd3080-b68c-366a-97de-7d861ec66761 | -7.63627 | -42.66085 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ce3cb5b0-c710-3383-8d35-fa15354ad274 | -11.84724 | -46.38095 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d824adcd-1bf5-3f3e-80db-ed8e862794c8 | -11.35874 | -43.57314 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad41dd8f-a5d2-3fd3-a361-1c462d902831 | -10.84666 | -53.76836 | 2025-08-30 04:49:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1524eaa0-b35b-37ce-bb37-ce1abe6f2f3e | -8.04846 | -46.9139 | 2025-08-30 04:49:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6713f5b5-dd75-3bc6-abd8-e9fe4a311fa5 | -7.74108 | -50.26934 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a4f227d6-f033-3925-9a33-21a913900b56 | -11.57085 | -46.35914 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e289c574-5672-320f-839d-5052944d03eb | -10.44703 | -57.96825 | 2025-08-30 04:49:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c924c8ab-cf2b-3b86-ba4d-4432f7f5a819 | -11.31492 | -43.65269 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c382057b-a34e-3c93-87d2-bf33b39575af | -7.59643 | -42.72066 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ae5ac59a-f6c0-3a91-b552-2899df433b47 | -11.31415 | -43.6586 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f147a845-6a5d-35fd-972d-64db5b33f81c | -11.35745 | -43.54177 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3d4b9d44-2264-3050-b194-99605d6e755c | -11.07162 | -52.0435 | 2025-08-30 04:49:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b08a6fd2-8f08-31c8-a4c2-3a0e8aceb4a9 | -7.78343 | -45.47202 | 2025-08-30 04:49:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 6851ed91-2506-3fba-aaab-068cb02dfd18 | -11.00015 | -46.95636 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5681bd1c-80bd-3823-82a8-340ca1918a18 | -9.45734 | -60.55273 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f7dac0be-d484-30f7-9e51-ed1b33ac875f | -11.85733 | -46.39308 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f65ceaf0-9e32-3310-b8af-b1d7d4f53ffb | -9.11058 | -65.76601 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| b2e101ee-d1e1-3f24-b06a-ba87e306a2a2 | -12.00694 | -43.98751 | 2025-08-30 04:49:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 035a58e5-557c-30e3-acb6-614396ced268 | -9.44389 | -60.56679 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 8e057a1d-6c9c-3884-8777-f8444499da90 | -11.3321 | -43.60052 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 006ca14d-d361-389b-83e1-2d38681f18f3 | -8.90116 | -62.10927 | 2025-08-30 04:49:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 53f43cf4-b230-344c-bcb2-3165dfcf502a | -7.16707 | -44.46725 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0ed815ea-7442-30b9-ac23-948764061e93 | -7.09711 | -44.30869 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 7edd94f5-e247-39e3-a469-a76522bdf48b | -9.10928 | -65.78038 | 2025-08-30 04:49:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 1f25d2f4-16c4-32f4-9956-42840e20bcc7 | -11.88722 | -46.39587 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 08d995bc-af8f-3cf9-9f82-9a6d59e83ea0 | -7.15838 | -45.13488 | 2025-08-30 04:49:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| edfbbdca-1606-3e2b-bcc0-c5d2709aaf92 | -11.8338 | -46.44566 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 5b28d2bb-6021-35cd-8aef-e2598e5995bb | -9.64849 | -48.34004 | 2025-08-30 04:49:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2c3413c4-3f55-3cb9-a3a9-1990cbf87798 | -11.32312 | -43.62954 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5c5dc568-23fd-3762-bad9-f918a5595afd | -7.09554 | -44.31594 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 4934d0d8-7dfc-37f5-b856-0dfbefa477b0 | -8.1769 | -45.0509 | 2025-08-30 04:49:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fe9482fe-dea7-390b-a7ac-92467c757324 | -9.53945 | -45.8462 | 2025-08-30 04:49:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6dccd655-a533-345c-aa02-4a6734d1d600 | -7.08075 | -44.28974 | 2025-08-30 04:49:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 62fcc1ef-38eb-3941-8228-9f4e977f784a | -9.4539 | -60.5422 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| e30dcf2d-1bdc-363f-a7ff-397a4c8dec25 | -11.9368 | -46.69509 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2854fa9b-3e43-35f8-a1d7-87f66e6728eb | -11.35707 | -43.54482 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2cfcbffc-9241-3633-8929-ff48109616a8 | -8.67804 | -62.43348 | 2025-08-30 04:49:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c46ae973-c2b3-3ffc-8c45-bb9678747f4a | -10.6437 | -48.6541 | 2025-08-30 04:49:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8a13317d-ddf6-3156-995a-e35bc90a0121 | -11.82893 | -46.47627 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 9dfecbfe-63ee-319f-bc58-2a7117e6dc02 | -12.40888 | -46.47213 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 172e2d6c-406c-34bb-8fb1-6f56fbff4347 | -8.49563 | -49.40302 | 2025-08-30 04:49:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa41d06f-954f-344b-b144-62022dbf0e15 | -6.6883 | -51.96322 | 2025-08-30 04:49:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72b108c8-a724-3b23-b281-41eebe8b7eac | -9.44512 | -60.56026 | 2025-08-30 04:49:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7e78b947-044f-342f-b1f3-ed61c08f21b2 | -12.39187 | -46.43727 | 2025-08-30 04:49:00 | NPP-375D | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 183bd160-0902-3049-9cf5-b426c3de6627 | -11.82626 | -46.46408 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 3a2e48a5-b6e5-3565-97a4-d566128ad6c7 | -10.93589 | -47.42841 | 2025-08-30 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7d78121-6a83-3a96-a69a-586d2d51046c | -7.71881 | -50.30233 | 2025-08-30 04:49:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1ba617e3-994f-3171-9c4d-277d9f69768e | -7.60325 | -42.70926 | 2025-08-30 04:49:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c5a53906-9149-3a60-8a1e-3eb97726245a | -11.31804 | -43.62884 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 73c0abf0-6f8a-3a23-a2a7-7f04cfb881b6 | -8.87417 | -60.73149 | 2025-08-30 04:49:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b11ba81a-354f-3f1b-ad3f-57f1c5860709 | -11.89452 | -46.71339 | 2025-08-30 04:49:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b37ca8cc-7b36-3d33-80dc-db1d6fa2fa2e | -11.30202 | -43.63268 | 2025-08-30 04:49:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 08ae40ad-d3fe-3b46-b809-cadc8cb62067 | -11.57509 | -46.35967 | 2025-08-30 04:49:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9b25e279-0388-3b6f-bd44-67536a58edbb | -7.43494 | -44.80408 | 2025-08-30 04:49:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28d7bbf2-aeaa-33f2-a7f0-ab3fb225d72d | -8.55292 | -63.03045 | 2025-08-30 04:49:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02dcffe9-985a-3ca2-a894-e25369282a4c | -9.58573 | -54.48712 | 2025-08-30 04:49:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
