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

## Dados Diários - Página 63

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1416e0df-5bdc-31e2-aa3b-dd2df96d6859 | -11.21231 | -55.9171 | 2025-08-15 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 76dfc886-f316-3aeb-b160-e9007280e9b3 | -7.9606 | -63.46881 | 2025-08-15 05:44:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d0debe9-981b-3a21-ab9e-a6f93d400af3 | -11.40592 | -58.53553 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b994a781-2d48-36b9-9ed8-8417301a3604 | -10.32096 | -63.62642 | 2025-08-15 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e684c389-a2ec-3dcc-bbf9-01e8fa1616dd | -8.69973 | -62.43463 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fcacf101-06e2-368b-8659-55416f253bf5 | -7.87281 | -61.81917 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 49683418-c801-3656-ba96-69441cfb5a4f | -9.1475 | -59.41681 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ced504c4-418f-3b9b-a1c8-b82621d4666a | -10.46963 | -61.32882 | 2025-08-15 05:44:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 268855c6-2660-3e17-b10f-93f517a8cce2 | -8.55371 | -63.8604 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d9fab05-5c5d-37a4-83dc-51e75b336778 | -7.53231 | -61.33879 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 9add7664-0b24-31df-bb80-6a8604a73da1 | -10.16326 | -59.66307 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80e86fc0-4e23-3523-9979-b6a86957f9a2 | -9.93924 | -60.48178 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d00cf2e-c6d7-3cd8-82d8-221043fd2316 | -13.11761 | -57.15989 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0e1e7233-d65e-33b0-95a6-68ee313f61a9 | -9.39534 | -60.54434 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 77decbaf-e4bb-3aeb-ad71-96cd8e265695 | -8.91575 | -60.73449 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70ad4988-ea9a-3a96-ab7f-d23c7b6543ea | -8.67572 | -62.44438 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2141b609-c460-304b-b962-9d5b7413b6ed | -11.3494 | -55.41002 | 2025-08-15 05:44:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 218a3a66-7c64-3d5a-886b-f369f0120e3e | -7.28709 | -64.69241 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 32443d5e-8013-3e58-9192-c198570e9af0 | -10.32639 | -64.44666 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c8c3fe5a-0a13-30cb-8069-c6ef6921118e | -9.20389 | -59.65531 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| f1a610ab-5d50-3aaf-b5b0-d3c05506936a | -7.81888 | -61.32744 | 2025-08-15 05:44:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ea43e1b1-c3c9-3283-9c23-a46635b20736 | -7.95861 | -61.76109 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44f2dc22-dd36-32d5-88b9-f3189d0e7044 | -7.95619 | -61.75119 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 52583328-78ae-3e99-8597-1cf3fe7a0d73 | -13.48572 | -56.66139 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 17.5 |
| b0277a11-8df1-3f92-81ba-8f67c209ad2f | -7.56422 | -61.41744 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a4ac477-a0c1-363c-8d2e-a1ab36acb8d2 | -10.32508 | -63.62294 | 2025-08-15 05:44:00 | NOAA-21 | CAMPO NOVO DE RONDÔNIA | RONDÔNIA | Brasil | 1100700 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b789e0a9-72ef-31ae-98ea-b744549d9d31 | -10.86301 | -62.00335 | 2025-08-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 9a97ecbb-636b-330f-82f3-12a2111365bf | -7.27988 | -64.6949 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a932b80b-4962-3f02-af7a-5da3a4c41174 | -7.45747 | -60.40915 | 2025-08-15 05:44:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7c4cca2b-062d-3f24-9646-b461b7739cee | -9.50609 | -60.52375 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 27f654ac-2b03-34ee-837f-0a7150fa3c03 | -8.67508 | -62.44876 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b7d4b6ed-a045-365a-b317-d1dea664de80 | -7.52844 | -61.33819 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38263069-96fd-31a1-9512-bef3ff7e6065 | -7.59855 | -63.52975 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d5c804a6-f689-3a4c-a66c-47771f99b49f | -9.18555 | -59.65734 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| eb3eadaf-b61b-38a4-bc80-61a2b7013719 | -7.94481 | -61.74947 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 874c2da5-1d77-3ff7-b7cb-a0887a64f341 | -7.94724 | -61.75936 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce55ce78-6083-387b-8a10-040cbd28f587 | -7.93829 | -61.76752 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2fd59376-c329-3d09-840f-17b78ca19dcf | -9.17172 | -59.65955 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 22.1 |
| ae87f742-ba44-3400-b3bf-ba388b1ff5f0 | -9.92335 | -63.18756 | 2025-08-15 05:44:00 | NOAA-21 | ARIQUEMES | RONDÔNIA | Brasil | 1100023 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a570e09b-c0bf-36f2-84f7-8982f61a6b60 | -9.50813 | -60.53981 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4f5f50b6-25a1-34a2-a485-22467ea7c85a | -9.51178 | -60.54426 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| df0a3b50-f167-314c-a01e-07632f7601e7 | -9.15136 | -59.42199 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c6805724-016c-3391-aa60-c49be719fa52 | -8.60136 | -63.89478 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d473d3b2-5704-30f6-8c4d-2323b806a389 | -8.72528 | -63.14272 | 2025-08-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 34c9906f-d921-3163-940d-1936f704682d | -8.56413 | -63.90839 | 2025-08-15 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c1c4ed0-56b8-325e-8ab7-2aaf07745bd0 | -9.21215 | -59.66085 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 29867ddb-f95b-3b69-8a00-1d6338a9dd0b | -9.15727 | -59.66632 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 97aa75b3-b7f4-396a-9301-66952b5db157 | -7.60971 | -63.51944 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e5cf7ec-9f2e-3ef9-8a34-2faed9cc7fe9 | -9.50759 | -60.54368 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ecc562b0-f4ff-389f-a514-c21c2ed47d0e | -7.28267 | -64.69894 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| f9f6279d-dfea-312d-80db-b5212ff6e3fa | -9.61446 | -67.29077 | 2025-08-15 05:44:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e34f99f8-b870-3bd9-96ca-51aff524ffc5 | -7.58825 | -63.45781 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dd2af0ab-9c0f-3a4a-b6bc-b41ad72c136c | -9.05252 | -60.64834 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7726deee-ed33-3bee-bd20-f4cbc2d58fc9 | -7.8697 | -61.81396 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6494e0cb-713e-321b-88a0-e072d1c987c9 | -10.32924 | -64.45096 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 15748e28-2e06-3e2b-8a77-dafc0ba961d1 | -10.04864 | -64.89462 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5847e28-2c61-3299-b4aa-25687a593180 | -9.15227 | -59.67001 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 28d14bb7-a942-31c6-88dd-2e2e42d593a9 | -7.6126 | -63.52379 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb1dd4c3-e2dd-3df1-93b2-79c5a60d4414 | -10.72778 | -64.85247 | 2025-08-15 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 68123b48-4cd0-345a-824d-760ea20f9a64 | -7.87592 | -61.82436 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3858802b-6ec5-3690-a5b6-a3a6e373b661 | -13.47516 | -56.66354 | 2025-08-15 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 85914121-2bbc-3223-855a-0ee64092cc87 | -7.60322 | -63.49923 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 11aabed3-513d-3cd6-8b57-8d0d0c24fb2a | -9.17112 | -59.66395 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 0d3593e4-ce51-309a-a371-f4ac8a478ee7 | -8.10975 | -61.19691 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| b465a54d-a075-3150-a853-4a4d0b3ca9c9 | -10.34976 | -64.45414 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3955d821-641c-30aa-85ce-b402420ff6ee | -11.40449 | -58.54661 | 2025-08-15 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da89781f-067d-3cfc-8ad1-b7ad00104d92 | -9.71105 | -66.83164 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 508766fe-1744-3d74-9460-90b0c6996477 | -10.86454 | -62.00089 | 2025-08-15 05:44:00 | NOAA-21 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5bd6cd04-799e-3ce9-bb53-9448764fe157 | -7.94276 | -61.76344 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1a73b335-4fc6-305f-a485-af527f0a616b | -7.62009 | -63.52103 | 2025-08-15 05:44:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 86c48582-c718-3d8a-9d9d-17383a218c90 | -13.11636 | -57.17083 | 2025-08-15 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2f50c82e-3054-39f9-8c8d-b14fa67be346 | -9.20832 | -59.65591 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7faf5963-87a9-3b39-a75e-b34946527dfe | -7.87414 | -61.8099 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| df4d032d-3bd2-3f5e-ade5-af109afad385 | -9.02437 | -61.22115 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d5329d5a-e145-3c33-a44d-be404e5d7111 | -7.97264 | -71.37579 | 2025-08-15 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 562cfd87-88c5-370c-a9c6-492c5539f71d | -9.17553 | -59.66467 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 4e147364-4f6c-3a19-9580-f49858ed8435 | -9.01642 | -61.21996 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e716c022-ba9d-3fb3-917c-8637704acce4 | -9.0204 | -61.22057 | 2025-08-15 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 83044ce3-f0b0-3fba-9365-464cd7626f1f | -9.5034 | -60.5431 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f8efc2e9-6028-3d1f-8cfe-18ad3b14c77e | -8.7961 | -63.46638 | 2025-08-15 05:44:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7cd218b9-c0f7-3377-8387-760cd8264fa3 | -7.28655 | -64.69594 | 2025-08-15 05:44:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 27b486db-db1a-3e3c-b4a8-763c39bd45a3 | -9.93869 | -60.48576 | 2025-08-15 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cc885a55-cc9b-3ab1-8663-0c2de9fe43b6 | -8.11368 | -61.19751 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3316fffd-910c-3ef2-99fe-ec3f21d29c2a | -7.87526 | -61.82894 | 2025-08-15 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 184a4a24-e88f-3beb-b3d2-83fb062b0cab | -15.38548 | -59.82093 | 2025-08-15 05:46:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 9.3 |
| be045e51-9993-36dd-bbbb-7dd9589be838 | -15.67256 | -56.38273 | 2025-08-15 05:46:00 | NOAA-21 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 436bf586-a821-3f8e-8a2d-7c67ed64aeb1 | -6.0806 | -59.9657 | 2025-08-15 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 60.6 |
| c69d48d1-617f-3602-b2c8-cf87571ba52c | -6.0991 | -59.9459 | 2025-08-15 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.3 |
| 43bd6631-7183-355c-9607-c49f781e4486 | -6.9303 | -59.5305 | 2025-08-15 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.4 |
| 236800c1-0509-3023-bfb7-613d9ff0ed79 | -6.0807 | -59.9465 | 2025-08-15 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 87.5 |
| 7f9c59f6-978c-3307-bab4-f4da07f430bf | -5.455 | -60.1391 | 2025-08-15 05:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 67.0 |
| b3c0ee0f-6d45-3295-b585-e596bf5e4357 | -9.1706 | -59.6762 | 2025-08-15 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.7 |
| 0e850846-d349-3837-908a-e5229a9dede2 | -9.1708 | -59.6568 | 2025-08-15 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 4d52edb1-d772-3c35-8ace-acc6761fd998 | -6.9302 | -59.5497 | 2025-08-15 05:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 87.2 |
| 4e0ffef9-4390-3dc0-8aad-c67bc4a4c0a3 | -9.1892 | -59.6752 | 2025-08-15 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.9 |
| 26c1ecb2-2359-3b87-9c96-b1ab75249fd5 | -9.4994 | -60.5278 | 2025-08-15 05:50:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 54.0 |
| 341f3964-444c-338b-bcad-783220e936d4 | -9.1894 | -59.6558 | 2025-08-15 05:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 9d853714-6bda-39eb-b4bf-bde943101f04 | -13.4757 | -56.6739 | 2025-08-15 05:50:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 771857aa-9937-3405-99e0-f0b5542c84be | -7.5292 | -61.3254 | 2025-08-15 06:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 48.5 |
| b61765f0-c815-3bbf-9ad8-503916d22612 | -13.4757 | -56.6739 | 2025-08-15 06:00:00 | GOES-19 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 133.4 |


[Clique aqui para ver as próximas entradas](README64.md)
