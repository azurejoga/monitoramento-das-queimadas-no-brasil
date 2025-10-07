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
| 1b1377b9-81a5-3316-a1a9-7f2736401298 | -14.47113 | -44.75777 | 2025-10-07 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 558f88c8-f771-35e5-9d69-5916d47062d7 | -16.05752 | -50.99116 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b3568da-df50-3529-a6f3-67ef35c75203 | -16.05308 | -50.98966 | 2025-10-07 04:10:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a71f9264-2a52-30b5-83d8-73b11acf7767 | -18.57171 | -49.25996 | 2025-10-07 04:10:00 | NOAA-21 | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b0e223ec-044d-31e2-8494-0feb0a21e606 | -15.20883 | -48.24654 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7a4703b4-c6c2-380a-9152-4fd20491804b | -15.8883 | -46.25306 | 2025-10-07 04:10:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5881b3a0-6b7b-3aae-b4c8-547c5facf59c | -15.50366 | -46.82579 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| db736121-c576-3f45-a040-c4392e61d048 | -15.22429 | -49.31031 | 2025-10-07 04:10:00 | NOAA-21 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a6b2214f-4f51-3603-a9b0-05aac620ee2a | -12.24409 | -47.85735 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c732e12b-f37c-39b0-a5bf-e7fc5533f96b | -12.1847 | -47.78395 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77fee19c-d8c4-32b4-b993-33da120decbe | -13.86218 | -43.98902 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 10dc5642-b0d4-34df-ac16-daa8f6908d77 | -15.72208 | -46.86714 | 2025-10-07 04:10:00 | NOAA-21 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbcc7b0c-cb66-30ef-a209-a9826af0599e | -14.76868 | -46.03228 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 3b6a18c1-dbf1-3386-bd27-477cfa287507 | -15.38804 | -48.00923 | 2025-10-07 04:10:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4447b540-ac7d-366b-a6f8-7e126b3519af | -13.34216 | -47.56548 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29172fee-0676-382e-9c6c-497c1f3b33af | -15.5947 | -42.36104 | 2025-10-07 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d1c251a3-6047-3173-9642-162807b0d94f | -13.22962 | -47.80953 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| f027fc3e-7e3c-34d8-8764-0c6f405ef09c | -16.34073 | -47.05566 | 2025-10-07 04:10:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a9bae3-e6cb-3617-b3dd-002435ddb0b6 | -13.07446 | -47.81858 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 5875a1c2-28a2-378a-aacf-902da1cad097 | -20.09915 | -44.20293 | 2025-10-07 04:10:00 | NOAA-21 | BRUMADINHO | MINAS GERAIS | Brasil | 3109006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6f31c46b-4798-3728-9860-26e0dccad5f0 | -17.34588 | -46.8344 | 2025-10-07 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 755ee63e-6f12-3d91-ab0c-c5377e6c708c | -13.28652 | -47.17136 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3056ec59-b1bb-36f5-a923-ed72507f452c | -16.34539 | -48.12775 | 2025-10-07 04:10:00 | NOAA-21 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2cf50df8-864e-33c0-9ab4-b268f82b5f4b | -18.10694 | -53.36452 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a237f02-388a-3cb0-a004-0b41d50ce5e5 | -17.95836 | -44.40881 | 2025-10-07 04:10:00 | NOAA-21 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7a02ea4-9b1c-3f64-9d9b-ff10d241033d | -13.77789 | -43.94152 | 2025-10-07 04:10:00 | NOAA-21 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ceca1654-2951-3769-b702-e0d25e897369 | -13.05354 | -47.89299 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c28b38f1-a20a-3dc5-ab82-9c689cddafe8 | -13.26478 | -47.16281 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1e20cb4f-09cd-3e51-8fc9-8134a65e3b6e | -13.26964 | -47.58207 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e25a7b5b-d58c-34b0-82e5-fb3c7eb987f4 | -14.64173 | -48.31937 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e914ef7d-c192-3b03-b0bc-ff243e458522 | -14.75554 | -46.04646 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| de3b5376-c77b-36df-be8b-2ac3d5489a7c | -14.28554 | -45.85278 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 851c8a30-125b-35e8-b759-09241b548da8 | -12.90928 | -54.73023 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 90e7ca38-ea03-32c1-84eb-174ba9f6ad7a | -15.27134 | -46.35086 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ac638dec-040d-3eff-bd77-33dfd18b469d | -14.93407 | -51.42599 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0f9a134b-2aec-382d-a2b2-f1d226c0f780 | -14.76816 | -46.05683 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8ff11556-fdbc-3148-8923-a47a2ca1cf2a | -14.99091 | -42.0172 | 2025-10-07 04:10:00 | NOAA-21 | CONDEÚBA | BAHIA | Brasil | 2908705 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 42a3255b-bcb4-3cf5-b1ab-064b7fb65467 | -14.91812 | -51.40608 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7907b1f4-867c-35aa-87b4-5b379b95a0a4 | -14.65008 | -48.36334 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0da11df0-4a26-3340-a5c8-c8dc2217bdb0 | -13.96933 | -53.89931 | 2025-10-07 04:10:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c58ef170-2328-3adb-98c6-a46f7e440d39 | -19.35425 | -45.15763 | 2025-10-07 04:10:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d765dfd-24fa-3289-ba99-39ef5b62f95a | -13.07215 | -47.94593 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e5a841b3-2665-3af8-b9c2-b20389c375f6 | -14.96633 | -49.95471 | 2025-10-07 04:10:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 16adf7f9-cda2-33ed-8071-fe7250476879 | -12.97968 | -46.78416 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9be7b277-aae8-3d6e-bd86-652d47000326 | -13.71488 | -48.19435 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0aea2a52-284c-3f08-b769-714309230e46 | -13.03917 | -43.55712 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2dd8d4fc-5aae-3783-9e00-dbcf919e4dec | -15.49701 | -47.92167 | 2025-10-07 04:10:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b4c5554b-b8e4-3829-8cce-f3c3434e18ea | -14.73945 | -46.03551 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 17b900ad-1360-3db3-b0ad-6fedac84fd6f | -14.76734 | -46.04026 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6ebb42e1-045f-33fb-8008-256bdb1a5dbf | -14.73935 | -46.01479 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 23.3 |
| 8d515099-d8b5-3313-900b-d7a327f816e9 | -15.79687 | -49.39582 | 2025-10-07 04:10:00 | NOAA-21 | JARAGUÁ | GOIÁS | Brasil | 5211800 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c79b7405-2385-36d1-ac51-d52036d9e4a8 | -14.64589 | -48.3414 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 93b4b9f6-727c-3a56-a1ff-63b940404441 | -13.29007 | -47.80852 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8196959b-ec47-3e2f-b2f2-e8d73ffc121a | -13.2666 | -48.0622 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| b622c3fd-2184-356f-afd2-2382b4da0c35 | -19.04371 | -48.13579 | 2025-10-07 04:10:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 069fec4c-97a4-32a8-ac8c-a24acb2505b6 | -14.72892 | -46.0129 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f9a0c39e-1b51-372a-8bc3-abd265592e20 | -13.03528 | -47.90477 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2a62da0c-2d0d-3d0f-a4b1-921454254795 | -13.33321 | -47.55794 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 503d8414-e282-395f-a0fe-8794dc4e837e | -12.90829 | -54.73503 | 2025-10-07 04:10:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 926b33bb-80b6-3587-be77-18c06f77354b | -13.57388 | -48.14413 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ecd74db-867e-3f4f-9f0d-90a1e9731dbd | -12.15828 | -50.888 | 2025-10-07 04:10:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bcb5d95-0e00-36e9-beb0-575a7a66cfde | -15.58235 | -47.26536 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fcfcb3d-377b-33b8-9a4b-b8c5e5a5bcef | -13.07847 | -47.84227 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 5a52005e-8720-331e-9326-e8f0000effc5 | -18.11747 | -53.36511 | 2025-10-07 04:10:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75fa6d90-aebb-31b5-8287-aa62895c5e48 | -14.7026 | -48.38867 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f182f49e-1c34-360f-99f8-a4ea4726dbd7 | -15.58294 | -52.57256 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2406f3b4-61d4-305f-a4b8-331181d11e4f | -14.31719 | -45.8457 | 2025-10-07 04:10:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7f61eed-1ec7-3883-aa52-03ff595d355f | -13.3794 | -47.53354 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 17ded2fa-3893-3fa2-8bff-e8579cd8a8fc | -13.65746 | -48.72849 | 2025-10-07 04:10:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 30f202f3-c323-3feb-82cd-537463992bbe | -14.93569 | -51.44308 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| dcdc76e0-4588-3abd-8379-a4a6a54fd3e2 | -12.06276 | -51.20711 | 2025-10-07 04:10:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6377809b-0967-36ec-837c-c373ec9919fd | -13.3125 | -47.77135 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 74fe4487-a2ce-30f8-b7a4-8fb77ce36a00 | -15.11732 | -43.86613 | 2025-10-07 04:10:00 | NOAA-21 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e86010b-7328-37a2-8e46-8fa5504a1165 | -14.5491 | -46.64431 | 2025-10-07 04:10:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9deceb5d-70bd-308f-b64a-40c14f7cf6da | -17.32865 | -40.25803 | 2025-10-07 04:10:00 | NOAA-21 | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d9242d6c-26ba-3aa6-8d55-3d76225add10 | -13.26099 | -47.16236 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 46608396-54c0-39f2-a37b-311168811d10 | -13.34426 | -47.17696 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 80d00ad4-1c04-3b24-b8c6-09e249c80dfa | -14.56023 | -48.95259 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6e717a66-eacf-38d8-80fe-b55001ee77f5 | -13.8583 | -43.99203 | 2025-10-07 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| f0aa0de1-49ae-3535-b69c-52eb24e74478 | -19.89038 | -42.62482 | 2025-10-07 04:10:00 | NOAA-21 | DIONÍSIO | MINAS GERAIS | Brasil | 3121803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 8e17b4b0-1796-3d7d-afb3-a018bfbf5838 | -14.63699 | -48.32715 | 2025-10-07 04:10:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f72b8781-e01c-3b92-b826-ea5bd800a647 | -13.05901 | -47.92846 | 2025-10-07 04:10:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b714bda9-8d85-365d-ab25-d8e69be5cbe4 | -13.34801 | -47.17765 | 2025-10-07 04:10:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0a312e64-1708-3633-917a-9eeea0d60d96 | -14.94828 | -46.8186 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8b24351-cd18-353f-91d5-5e821ffd606f | -14.91998 | -46.81038 | 2025-10-07 04:10:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 53ab298c-ae77-38c6-9f44-52a3b491e5e8 | -15.4979 | -46.83796 | 2025-10-07 04:10:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ab60d32-7a96-3f68-b678-7a43f5c909e3 | -15.76164 | -47.76941 | 2025-10-07 04:10:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2852d950-9bd9-383c-8602-600a300044ca | -19.81315 | -45.33236 | 2025-10-07 04:10:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f13b9cae-53f3-3941-9eff-a648239d853c | -16.28217 | -50.98132 | 2025-10-07 04:10:00 | NOAA-21 | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 94a8df18-65b5-329f-bfc7-8dfb1d3fb171 | -13.72288 | -48.19536 | 2025-10-07 04:10:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15e53048-699b-37cd-8e1c-baee2fc3cc63 | -13.32687 | -48.03779 | 2025-10-07 04:10:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7eec3c1f-0982-3b71-94e9-341714fc31b6 | -12.95564 | -43.54707 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 60c4af7a-05c2-3a5e-a7f6-2edf66d1e413 | -15.55797 | -52.4434 | 2025-10-07 04:10:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e0807ce7-0a68-3745-8ccb-a67c751e0635 | -19.81374 | -45.32868 | 2025-10-07 04:10:00 | NOAA-21 | BOM DESPACHO | MINAS GERAIS | Brasil | 3107406 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 0e4a9b5f-b426-3972-b45c-3f3e9a2213dd | -19.02725 | -44.72986 | 2025-10-07 04:10:00 | NOAA-21 | POMPÉU | MINAS GERAIS | Brasil | 3152006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba798018-d105-37c3-97d3-00113d9fa74e | -17.16223 | -43.44785 | 2025-10-07 04:10:00 | NOAA-21 | ITACAMBIRA | MINAS GERAIS | Brasil | 3132008 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a70fb11e-eb53-3ff2-b194-aeb89f68d8cb | -14.77031 | -46.06546 | 2025-10-07 04:10:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 92d6f1ae-5b33-3dde-b5bc-cd80cc21b5ac | -13.02891 | -51.03622 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f059c28-c5ca-38a0-abb2-c3928e770b09 | -13.02996 | -51.03078 | 2025-10-07 04:10:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| e13517c5-7f85-34f1-b118-a70dc6dfb432 | -12.93853 | -46.78795 | 2025-10-07 04:10:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README36.md)
