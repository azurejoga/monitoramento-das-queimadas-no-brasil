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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 49e3a5ec-857c-327e-acfe-10fa2f62d8d0 | -9.51346 | -65.57715 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ea26a8-1858-3caf-9ccb-61d451df334f | -9.04545 | -65.44553 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3234c512-2c07-3dca-989c-076b1f962f1c | -11.9549 | -63.28833 | 2026-08-31 05:36:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 336164ba-6dbe-3d51-8e09-6db350fb8303 | -8.87185 | -66.78355 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| df572501-52b6-3c05-8ec9-59833d8c1995 | -9.2202 | -59.76442 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7097dec0-1a36-3d9f-9429-48ed671ebf6d | -10.77896 | -50.85766 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7a99539b-725b-3f93-90da-691fcab7ecf7 | -9.8904 | -60.27857 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 83373509-a60f-3aa9-b688-865fe6419910 | -9.12308 | -60.38961 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2c091f3a-4781-3563-ac37-6a0ce765f271 | -10.31495 | -58.08885 | 2026-08-31 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9d6d081d-bc58-3142-b7f9-ca620aaeebe5 | -11.03512 | -57.24964 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4982a801-cfb5-3d09-83ae-d7f282b8a77b | -10.48122 | -59.60841 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08a18235-6b6e-3172-89d4-05637c2e3a8c | -13.63224 | -51.84359 | 2026-08-31 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d37c88c5-7585-3036-b5a7-590bef184b14 | -8.70522 | -63.96918 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 18930026-8826-3c21-ba72-6c7495dc7a0f | -9.05412 | -65.4177 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddd44100-91ef-3ea5-a811-360fdbcb6f9d | -10.17896 | -69.06532 | 2026-08-31 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 06fff25a-6387-372a-8b1a-dddc40c977da | -9.92889 | -60.48279 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 42a829ff-33e5-399a-8b91-2cd1836b54c7 | -8.80516 | -62.49744 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dae95d83-f7e2-3261-8c2d-4952479ce301 | -11.03729 | -57.23487 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5e3bac83-2c8e-3a80-97ee-92fa0a0a7298 | -8.94162 | -62.06862 | 2026-08-31 05:36:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c0c3f690-bc48-33cb-a80f-cac63e16cbbb | -8.87211 | -66.77965 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67a32f72-eebd-3d7d-ad0c-f77841a1d32d | -11.07892 | -51.52167 | 2026-08-31 05:36:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7fbce576-3eaa-3761-85f7-7a6475e77c34 | -10.75452 | -53.99969 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| cc3befb2-4f96-3c67-a62d-aeb09f8f1246 | -9.70745 | -60.75624 | 2026-08-31 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4f51bddc-7207-3712-bc25-e08df61f6754 | -9.89152 | -60.27138 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 358eeeb7-2cc9-3e09-97bf-75ccf6169cad | -8.79958 | -62.48911 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38314c05-42f4-3071-8ba1-e82838b01594 | -11.49363 | -60.58039 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52a37a37-9c45-3a4f-b1c7-9d9636bf3b03 | -9.92778 | -60.48993 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f84bc370-deba-3ef0-a08e-e5c164de3444 | -9.87305 | -60.30157 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4c3d819f-4b73-3e77-b37a-2765258d8535 | -10.84224 | -48.35231 | 2026-08-31 05:36:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9afc868e-e613-308d-9e69-6b8b14824c51 | -9.90996 | -60.15237 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 57d366e8-f659-3704-ac80-4f709a88912f | -9.40208 | -60.59223 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bd42ef1e-13cb-3747-a432-057a8e54bc31 | -9.79903 | -60.1908 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95beca5f-cbf4-3757-bdcd-71ea81006a4c | -11.48298 | -58.51864 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cae8075a-d23b-35a8-8a09-426feeef6601 | -13.6444 | -51.84007 | 2026-08-31 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9d026bf2-5aa9-3205-82a9-65f93b5948b9 | -9.14743 | -61.099 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9ca3e532-2b9e-373f-a169-f6148059d084 | -10.75024 | -54.03558 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 1160da17-ffcb-3bce-8290-da79007ab814 | -9.93731 | -60.51699 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dc163d62-d1e6-36a4-96d2-87ca835d78dd | -9.00173 | -65.43575 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91101a4f-6ee3-37dc-bc39-9c2ac8c3409c | -9.93169 | -60.48689 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 263c7a19-c36a-3129-a47d-9e7a3fd9bf3a | -10.74952 | -54.04082 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| ef1a4409-2f2f-310b-aed1-9fd5f193f0af | -10.48179 | -59.60466 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d2061ba0-c84d-314b-9c1e-77c4a20da6e5 | -11.47697 | -58.50896 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3e3ade1-2268-3c86-b3fb-86fb48d3de53 | -9.70237 | -65.06032 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5ea30953-b8e4-3b2b-8a89-64e3c967488e | -8.57979 | -66.97142 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 88760664-e251-34a3-8978-fcd945b6e20c | -9.51674 | -58.38515 | 2026-08-31 05:36:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 26bd0576-bb81-3937-94ff-5602fa0e8a84 | -9.88815 | -60.27085 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e30494ea-520e-3f48-8611-61ff793f4e74 | -9.71842 | -64.99789 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc4d53c9-2b80-3236-8ef3-e373957c9ed7 | -9.79566 | -60.19026 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0688ebfa-839f-35b8-9f0f-75cd2b241fe6 | -8.63292 | -66.54001 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2b3e73d4-9c0e-39cf-9b34-ac615e438b3a | -9.13934 | -60.52627 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ad6a048-4f70-3233-a560-0a5f4b49c58c | -8.96932 | -62.39433 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bb7bba09-cd34-3814-bbf4-5c3029404a93 | -9.15131 | -61.09604 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f2acf28f-3f5c-3d5d-a14b-9b5fd4ab6490 | -9.00094 | -65.44051 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 103c1196-2ac8-30a0-8b7f-274c1a2e2b30 | -10.74353 | -54.04634 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| a889874c-70c8-3e71-8c47-9ed3a6a9de31 | -9.85936 | -64.98388 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4ea2e0fa-278f-325f-85f9-b346f83a704c | -10.744 | -54.04535 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3508b0dd-f855-316c-bb15-9db6cfc5297e | -9.94122 | -60.51395 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f7c542a1-947a-3cd5-a0ce-d0230deea422 | -8.95164 | -62.36988 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da22f560-d3cc-30c3-a084-ea584221dc74 | -11.49251 | -60.58762 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 42ba4970-e102-3122-9b8c-dbe7ba0a68ff | -10.7795 | -50.85331 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c8b19e6-b5e8-3d79-905c-eaf0f4efcb95 | -10.47781 | -59.61646 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7f082b60-57a8-3dca-aa50-b570f64faae5 | -8.80237 | -62.49327 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 66ab31de-49b2-332b-9d47-f352597065d1 | -8.86879 | -66.89861 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 265d2e94-8979-3fc7-ab03-d1070f337b4d | -9.19882 | -64.44859 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 97a53420-4be9-3670-b3c4-3f650c37e3c9 | -8.59748 | -70.21398 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00fbce9c-6115-3777-914e-f9333e803f75 | -8.9404 | -62.3754 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a54d0e1d-3226-3002-a8b5-df8533f575cb | -8.80574 | -62.49383 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f3f29a0c-b665-35a8-b92a-1345e8dbd503 | -10.49211 | -59.60628 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 82056272-a3de-3ab8-9b6e-0f6cd13e260b | -8.80897 | -70.7795 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8a4c5ea0-8a2c-3883-962e-c320d90fc330 | -10.17802 | -69.07059 | 2026-08-31 05:36:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 053e1226-0dcc-3a91-b2ba-a7f4cf9bdbbc | -8.80854 | -62.49799 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c76697c7-5526-359a-a1e1-8fe084ce7862 | -10.90941 | -61.67642 | 2026-08-31 05:36:00 | NPP-375D | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a0847bae-7ff0-3df2-b7af-c39e4714bc5a | -9.14799 | -61.09551 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89a404df-e484-34ae-a4a7-cbff16af8f39 | -9.79397 | -60.17892 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f74c2a3-fd3c-384c-a88b-1da0128195a7 | -8.95221 | -62.3663 | 2026-08-31 05:36:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 40b0751e-a5c9-3010-b037-96e3111a88fc | -8.67863 | -66.52123 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f314ca49-ddbb-33c9-9787-256e3d0070e6 | -11.47634 | -58.5132 | 2026-08-31 05:36:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9df2ae0e-9d15-37c9-922e-dd8f24015443 | -9.21152 | -60.87945 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac671a01-c693-3c5c-9f2d-3f4631d1d44c | -10.80419 | -50.6543 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95f30c24-aa32-3c91-8a31-241849731318 | -10.7504 | -54.03123 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8cdd14bb-36ac-3f29-b4b5-2cb6b79c920f | -10.81567 | -50.66039 | 2026-08-31 05:36:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 92a138d7-a541-32f1-be8b-dc2461701ce4 | -8.3949 | -70.08797 | 2026-08-31 05:36:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1f183785-e2d2-3a76-8362-9ed98c211d77 | -10.73993 | -54.0394 | 2026-08-31 05:36:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| aef4e18e-21d5-383a-98f7-a7c101c440a3 | -10.57361 | -57.49927 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cda0c440-528c-322e-a1a7-d8798f950a6e | -10.31128 | -58.08829 | 2026-08-31 05:36:00 | NPP-375D | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e763b0e1-8643-3a61-a7b4-33d635740312 | -11.49587 | -60.5882 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8718b86a-0590-3111-89f2-edcd6e4f735f | -9.93897 | -60.5063 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 31f9a0e5-a93a-386e-b5d4-a58fe90c03be | -9.22416 | -59.76129 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 233f7fe6-7e83-38f9-812e-ab4c01a6ab87 | -9.7979 | -60.17585 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 98a90069-be8e-3ff2-b3c9-bb58270be16e | -10.57828 | -50.36617 | 2026-08-31 05:36:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2ba0fbd7-f543-32c3-84e2-21b72d0b70c3 | -9.01288 | -65.40565 | 2026-08-31 05:36:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fc99bf5d-025c-3d69-af3d-6b1e6112acc8 | -13.63279 | -51.83888 | 2026-08-31 05:36:00 | NPP-375D | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f78b05f0-cb87-3961-a3f5-e56d7b35ca53 | -9.71133 | -60.75325 | 2026-08-31 05:36:00 | NPP-375D | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9a33e2a-ab78-3105-a862-f582060da303 | -10.49555 | -59.60682 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7c1f8b76-3f65-3838-a6fb-23f28372efdb | -11.03411 | -57.22939 | 2026-08-31 05:36:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46e47211-f3c3-3f3c-b930-725c726d934e | -11.49419 | -60.57676 | 2026-08-31 05:36:00 | NPP-375D | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 03b60e56-6e8c-3436-ab3d-80559ab64708 | -9.14356 | -61.10196 | 2026-08-31 05:36:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7fd00bad-dd46-3913-a075-dbd361c5e675 | -9.89432 | -60.27551 | 2026-08-31 05:36:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 799373cf-aca3-38e3-b512-4f06dac96ea2 | -9.72086 | -64.99493 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e4d5d4a-56c1-3a4b-b51d-34248ffa635e | -9.85567 | -64.98325 | 2026-08-31 05:36:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README63.md)
