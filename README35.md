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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e626cdb-1657-317d-b767-b283944960a3 | -11.74288 | -48.18906 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7ac290c4-320a-3aa6-a844-947ffd55fcc3 | -13.03437 | -46.80846 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e53c59a1-5e08-3069-a86b-3c95cb6dc1c9 | -15.38593 | -47.51639 | 2025-08-20 04:36:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 99bbb6b1-0dd4-33fe-bdcb-9e19ff3d9bbb | -12.97431 | -56.87514 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 994c6bf3-85a8-3f86-b9b1-275b410dfe50 | -15.35173 | -49.61232 | 2025-08-20 04:36:00 | NPP-375D | CERES | GOIÁS | Brasil | 5205406 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 137eabca-3a90-30c8-9710-4684c9562794 | -11.09299 | -44.81009 | 2025-08-20 04:36:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4572241-fb13-3d86-9867-44d066166969 | -11.12056 | -46.8956 | 2025-08-20 04:36:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 5cdc7f28-3749-3f70-b7bf-e62969ae3852 | -13.87275 | -45.56952 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21e504f1-b37e-368c-864d-d5318607d26d | -13.19004 | -46.87149 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 84b18c1c-3f16-3e07-a741-02bcfce07088 | -13.57666 | -47.03128 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 4d6f6f89-410d-3a80-97d6-64727d7cd9ba | -13.60871 | -46.88698 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3e2e52c-8ebc-3df1-a15e-0c216cbe145b | -13.64981 | -43.7888 | 2025-08-20 04:36:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 33edcca4-6d34-33fd-9652-e7a016633ebc | -15.71325 | -48.62873 | 2025-08-20 04:36:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| da949e00-4fdc-399c-82ff-a819ce839d84 | -13.13308 | -57.15915 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e4f42849-b256-3876-be54-f0a4f2848a2b | -8.87566 | -62.39157 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7aa098f2-adac-3a2c-8e76-ed876b1f3dcf | -13.14504 | -54.93673 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 1ccaf355-a3ec-37cf-9c62-42b896df1103 | -12.9696 | -56.87006 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 629df0fa-3c15-3e36-8166-5f0cda2bfc92 | -9.21423 | -59.68985 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3a6f0c2-2287-3091-b77e-e9901d741ae8 | -13.57376 | -47.0268 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9cd59179-7359-3332-b195-1cda3c01a23e | -14.6257 | -54.88994 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6ba6bdc2-d24d-3fd5-93e3-dda46dd4a437 | -13.73625 | -52.01228 | 2025-08-20 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a343eda1-3d60-3549-ac16-bbd39d57c66b | -15.4261 | -46.71827 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a830dfd2-9b6d-3c76-8a9d-7e447c6eedac | -14.45575 | -48.36972 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ba3cb53-2fa1-3e59-9177-3b79d0e4ec56 | -13.1924 | -46.90366 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daa4653d-6811-3f1a-b3d2-df19a30e9af8 | -13.15622 | -54.9226 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 19b90a55-2d41-330b-812c-3d8debdcf772 | -8.87994 | -62.40774 | 2025-08-20 04:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 94828b85-f967-315c-b2df-5ef25d29533a | -13.15687 | -54.94299 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cbdbea1c-dfd2-3fb7-8e41-dcf6904c515c | -13.18945 | -46.89944 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e8398831-f103-3175-a261-5ca6f2669e46 | -12.9791 | -56.87203 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd552e38-8447-3c27-8bb5-d9c17e7ff8ac | -10.12377 | -47.4341 | 2025-08-20 04:36:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c215a4e9-6f27-3bb1-b547-ea34a7b10590 | -12.96385 | -56.85155 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6f2601c4-cb90-3b11-b048-37d9e4f91e96 | -13.17712 | -46.88632 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9d68fd7d-3ddc-3e6a-84b3-acb727b9a266 | -13.02394 | -56.84342 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 47a8afba-1502-32d8-a424-82db92c7362b | -12.64096 | -46.88734 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a0997bae-dd45-32a3-bcce-258e50bceebb | -13.57899 | -47.01556 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 7fb806cd-5b79-30b3-885c-6d5c40f070ad | -15.54037 | -48.57082 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 29018c0b-6906-3938-a42e-55fdc153129e | -15.55161 | -48.56511 | 2025-08-20 04:36:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b6896d30-a98f-3f96-8611-2e360c3b9b99 | -13.19064 | -46.86744 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| e6da7e95-ec94-394f-855f-1d83962a8d43 | -12.66393 | -45.81972 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c73d518f-c514-3c97-a435-0ca190f71ff8 | -11.67159 | -60.19349 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 040408bf-44b2-33e8-8bfa-22f2d8148d07 | -14.16623 | -45.28589 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| db6dd802-3a71-37c9-841d-a0edd65cd706 | -13.58363 | -47.0083 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46e0ee11-f502-3b8b-b7b7-582afd491bae | -9.19353 | -59.63192 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4d6e3d33-f0d6-3b9d-8bb4-843db3b1842a | -13.18241 | -46.87471 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b8fc04a5-e1dc-3617-9820-a2e646067001 | -12.96683 | -56.85878 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7a61e7f9-4963-3c83-9ba5-e7482842fc4e | -13.33694 | -54.42729 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 74b44720-edca-3009-b36f-6e52e7f50610 | -13.02952 | -46.78776 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1323e3ff-0cf3-3ec9-b853-f979bb3fa3f7 | -12.59204 | -47.07258 | 2025-08-20 04:36:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de64cde8-8f37-38c3-83d2-b8c30f4dbefa | -9.19795 | -59.64191 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ffdd8b49-8131-34b4-9539-36d37814b461 | -15.54449 | -42.29013 | 2025-08-20 04:36:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ec1038ee-7e83-3cde-8ea1-abb6167e49e8 | -11.67249 | -60.18907 | 2025-08-20 04:36:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 15d433c7-8fff-325c-b2a5-58da210f3c7a | -14.89471 | -48.07177 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 01b95225-2843-37d6-a72f-b4c31648312b | -11.77196 | -47.563 | 2025-08-20 04:36:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d42d6aed-ed21-358b-b967-8c9b3ae75c49 | -13.56144 | -44.45628 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 13362b81-19ca-36f6-8865-373a14356353 | -14.88902 | -48.08691 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7cdf7270-e826-3658-b14a-865672a2aab6 | -12.66281 | -44.96128 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 760bbb5a-415b-3f63-a677-138721820579 | -9.20823 | -59.62069 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c6e64961-db25-3a90-84d2-6f95e244168d | -12.98384 | -56.87307 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fe25c3d-fa95-3bd7-bb25-06e926812006 | -9.24162 | -59.6098 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 629a5222-b6e0-3d46-a754-de438be86d19 | -13.14716 | -54.92498 | 2025-08-20 04:36:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| c9e56c4e-7ba1-3bdc-8fa0-340f8b0ed966 | -13.40399 | -46.353 | 2025-08-20 04:36:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ab2c117b-520f-3d27-ab8e-c7acb8e39b4d | -12.99309 | -45.20971 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 7b83eaeb-05bc-3a97-a33c-21549980c75b | -15.75017 | -48.29213 | 2025-08-20 04:36:00 | NPP-375D | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 72c8c4da-2dd4-3b8f-99cc-5cf5dff817a5 | -13.58711 | -47.00888 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3c50097f-845b-3e66-88da-fc6ff43cbf60 | -14.5008 | -45.96495 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4ffd59d2-96a8-3b8c-8218-afaffe48370d | -13.02867 | -56.84443 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5abd7000-e47c-3d5b-83ff-f841f996e053 | -9.22989 | -59.6058 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 18a95d38-4d59-3cd5-a73f-8c0ad5487612 | -13.44659 | -50.66636 | 2025-08-20 04:36:00 | NPP-375D | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a739483c-c470-38ed-b64b-558580e60cdb | -12.77634 | -48.26455 | 2025-08-20 04:36:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 33e553db-9870-33fb-8bdc-fe469934da22 | -15.09548 | -47.33852 | 2025-08-20 04:36:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ac3b401-8517-3d2c-8738-a11c353ee0bf | -12.96881 | -56.84843 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4f00377-8290-3a03-969c-f486bca9bb75 | -13.59762 | -46.91354 | 2025-08-20 04:36:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 944afaea-29ba-3242-97af-3cd40d6a0e94 | -12.96782 | -56.85358 | 2025-08-20 04:36:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 26050266-10ea-32d2-b2fc-6a7d51a9f31b | -13.34084 | -54.40551 | 2025-08-20 04:36:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 01dade73-cb19-397d-b0d4-a0983af69ab1 | -13.10914 | -51.91632 | 2025-08-20 04:36:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2891b46e-838f-3abf-9370-c51461b7cbd2 | -13.59237 | -47.55798 | 2025-08-20 04:36:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 4753cfff-620b-3c85-8b55-9c8c04b293d3 | -9.17868 | -59.64377 | 2025-08-20 04:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1a8dc92a-e807-3eb5-be5d-513840c5f8d0 | -12.91658 | -46.09911 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 34a774b0-d73f-3f27-b1d4-6f27b9f062ce | -13.48984 | -47.05844 | 2025-08-20 04:36:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cbc7ea0-ce6f-3a44-8da9-1f2fe654e1c1 | -12.10497 | -47.91962 | 2025-08-20 04:36:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2fced7bf-fbee-3144-bac0-a9e6f49efa7a | -13.03085 | -46.80803 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 405137dd-534c-3531-b471-d40d02d381af | -12.87405 | -46.0622 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4459ef75-75c2-3ff0-93a9-9500e781947f | -12.98997 | -45.20447 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 803cfd29-f16c-3f9d-a957-93c12d86618d | -13.73557 | -52.01626 | 2025-08-20 04:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d415139e-5283-3a1d-b23a-bebc4a0621fb | -14.62975 | -54.89081 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 652ed22c-c240-3efc-8865-c0c46bd966c3 | -14.89075 | -48.07504 | 2025-08-20 04:36:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ef8ef2e1-2263-33c4-a67a-e2b2a6a73417 | -12.67488 | -45.82129 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dff60a6f-5722-3bf9-964e-0d70c96b77c6 | -12.95146 | -46.17116 | 2025-08-20 04:36:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 29b0a0fc-2e81-3465-9584-26f2f6fce402 | -15.74782 | -46.62086 | 2025-08-20 04:36:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5a90062-4db0-3aa9-8913-7415171c675b | -11.12629 | -46.99648 | 2025-08-20 04:36:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1ff0e3e7-b873-30a2-90df-3dbd88719b92 | -12.98685 | -45.19923 | 2025-08-20 04:36:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| d141122f-a44e-3302-abd2-b1d8d215ff0a | -11.7373 | -48.18831 | 2025-08-20 04:36:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b4e24a45-684f-3477-937f-6625e22b66a6 | -14.61757 | -54.88839 | 2025-08-20 04:36:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 306a257e-03fa-3b92-8fbe-59015768c14a | -11.57015 | -50.45001 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e773a89e-970b-3f83-ac85-5a5d6b2133ee | -14.15409 | -45.28895 | 2025-08-20 04:36:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b80dc656-9b31-3e97-8ae4-9e73b351edac | -15.19301 | -48.74517 | 2025-08-20 04:36:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a61c73-88b6-3b99-bff8-909028eb6ee4 | -15.12928 | -48.71239 | 2025-08-20 04:36:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| de49a35e-f40f-3cf9-902e-e26d79a7d777 | -11.56616 | -50.45314 | 2025-08-20 04:36:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cd2bc096-5017-33ea-baf9-06586abe5f8d | -14.46136 | -48.37817 | 2025-08-20 04:36:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 416bef2e-5697-331e-86ab-61c6b9366546 | -14.88166 | -48.08955 | 2025-08-20 04:36:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |


[Clique aqui para ver as próximas entradas](README36.md)
