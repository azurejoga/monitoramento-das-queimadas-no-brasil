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

## Dados Diários - Página 47

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 955fb9d1-6148-311b-8939-26cc6cda2aa2 | -9.63431 | -59.63816 | 2025-08-27 04:27:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 529bb117-e93b-3ade-b0f9-377eba430e82 | -12.90176 | -44.65942 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b07547d8-1acc-3736-a756-be58cb9892a7 | -13.62086 | -48.20466 | 2025-08-27 04:27:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| dfc519af-e60e-3b6f-8fde-b19b84ae3ad4 | -18.93549 | -46.9646 | 2025-08-27 04:27:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 17ffbe82-2523-3136-99db-6c68567226f8 | -14.40733 | -51.94123 | 2025-08-27 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4ec0d40e-7a58-3e78-b42b-69671196b525 | -19.08091 | -48.14314 | 2025-08-27 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6905efee-b5b1-3744-953d-d8aa9498c8f6 | -12.42146 | -46.488 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 26c6c895-5190-397f-b966-2d1e464335e9 | -17.80826 | -44.51511 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3a208f9-182e-3fff-80ef-be1c9fe1baaf | -13.50286 | -46.87241 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 79eb86ad-bee9-3a81-8cdd-abd3653d6ab9 | -16.37048 | -43.03959 | 2025-08-27 04:27:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f70a8a03-e41b-3578-8474-42ff5f32f090 | -13.82267 | -45.89286 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8acbd8ec-1418-3bda-b5e5-6a0d8485bfa7 | -12.79974 | -48.11316 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9429a716-60ca-3d41-9b5c-35d55db698fb | -12.68046 | -47.88005 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 46adc3d7-67ea-37e1-b81c-e0adfdd978f2 | -9.40034 | -60.51337 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.0 |
| 03506c02-fb43-3011-be3e-0b62a22fd407 | -12.71362 | -48.14264 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 754a0c4b-ad03-37f7-bdb3-9ff2ee88cea2 | -11.92231 | -47.10754 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0dec1c69-2926-3c33-b0db-f280844ec661 | -15.09154 | -48.39682 | 2025-08-27 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f1dd9aa-fb13-31cd-9fe6-de5cd14083c3 | -14.2464 | -48.02784 | 2025-08-27 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 35b811a0-8868-3eb7-80ee-d4490a267099 | -17.9729 | -48.04623 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e8c18be-5fe6-34e2-aacc-23580ff50c3e | -10.40581 | -57.70826 | 2025-08-27 04:27:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9d62351f-9eff-36d3-9f70-8f6c1a7bbe29 | -12.71806 | -48.13611 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a1a5048d-1ecb-3833-9faa-3a92e23f2ae2 | -11.80994 | -46.80325 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 84baabc0-7136-378f-9602-c086e2049dc3 | -12.74608 | -48.19515 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 301ead4e-daa7-3ae1-ba9c-6944ef66d9a8 | -15.18417 | -52.3268 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7d732375-8dec-397a-b56e-067bd8759285 | -11.91864 | -46.74028 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e897da3b-a5ba-3a09-9bfb-bf1bc07f97e7 | -12.7644 | -48.16544 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 50fafff0-d9ac-3e25-af28-082bec3110e4 | -13.44054 | -46.98833 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4813e508-d2ad-3968-be02-401db81a7949 | -9.4154 | -60.50965 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 51f1f8d8-6177-3342-ab97-3ce66a82ec1d | -12.93442 | -46.33223 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 46fd5daa-32b3-3823-a1cc-d4c6de7d5686 | -11.52242 | -52.13099 | 2025-08-27 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fabd4a38-1b89-3eae-9399-bf3c74c5fad6 | -11.92306 | -46.71181 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7041b768-40f1-3808-9afd-aeaa46ce6406 | -17.77141 | -44.48407 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3ab1f235-71c0-3a24-8574-c11276aa245d | -13.41312 | -46.86216 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| abfcb585-dbf7-3d74-9253-3a77db864b7f | -13.63867 | -45.69558 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ce9af108-15b3-300c-82d6-829c7917c67c | -12.78746 | -48.14748 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1adc3c46-4a18-394d-86b7-765f85ac6bbe | -15.61713 | -52.7145 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e60b4059-c3e8-3f2a-8259-ccf837701cf1 | -12.75271 | -48.19624 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e702d683-5e4c-3de2-9db0-8f76cc88e17a | -13.6381 | -45.69948 | 2025-08-27 04:27:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6f22145-9cc0-3a65-91a3-833bbd9150fe | -15.61466 | -52.7114 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 52467a31-9b8c-3388-ba3f-08fb6d08b9a7 | -12.94904 | -46.32711 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4648b366-01d3-31e1-8d0f-f5678ab142c7 | -14.12891 | -45.40515 | 2025-08-27 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 84d6fa04-658d-3767-b844-0c26388e140d | -13.39581 | -46.88549 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3922d5f6-8e55-3d59-85be-e1b2ebd76ef3 | -12.79367 | -48.10855 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1297372c-3b42-3024-9c03-95a484c1e20b | -9.40201 | -60.5408 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 1c861d4e-ef84-316f-922e-fc644c8c23fa | -16.74288 | -48.53938 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 054721c7-bb3d-3d94-9305-ac340b341d72 | -17.80508 | -44.50947 | 2025-08-27 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a37c7609-0884-3f79-b712-64122615d8c8 | -11.81773 | -46.81903 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 60ce6c3b-1de4-3340-a1c5-0d4d69714144 | -13.17457 | -50.5931 | 2025-08-27 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20c06342-0c8f-3f79-bed2-4b516582d1ad | -15.65925 | -52.74256 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0aff053b-f74a-3ccd-89e6-1a8843be31d2 | -13.42198 | -46.86332 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 0c1e31d1-dd89-3159-b443-ae2db7f71a1e | -16.74345 | -48.53579 | 2025-08-27 04:27:00 | NOAA-20 | VIANÓPOLIS | GOIÁS | Brasil | 5222005 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a0c8e99b-5159-39a2-8763-be7f9f9f0d70 | -12.74747 | -48.07937 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ed75a01a-c304-31c1-9bee-1fb9e4a9a66d | -13.98201 | -46.34847 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fef064ba-1499-3786-93ae-459d4bcda97c | -12.79643 | -48.11261 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a6b62e7d-2c04-3f69-a8bf-1ec83623a84a | -9.39085 | -60.52495 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 948109fd-d1ab-3abf-87c8-4121eb65d3dd | -11.81049 | -46.79969 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3d6db89a-cc06-3c54-a933-32e7913eecff | -17.36893 | -49.17716 | 2025-08-27 04:27:00 | NOAA-20 | PIRACANJUBA | GOIÁS | Brasil | 5217104 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fcf042a-99ad-34c4-9bf6-ca8d11587e08 | -17.17489 | -48.68537 | 2025-08-27 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d0893683-d536-3a08-815f-d1535e4d7ffb | -13.00527 | -56.89963 | 2025-08-27 04:27:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f8aebab1-1d29-34ae-8e74-d8b2329d7650 | -12.77117 | -48.10132 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ef0bfcc3-b77f-365b-b820-411d9ade3438 | -9.41707 | -60.53718 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 81617821-0fe0-3b94-8257-52e1ee789036 | -15.65838 | -52.74746 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bcb4a5a1-b04d-3e14-a96a-110beb7337e3 | -13.06414 | -46.32999 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5ae7b6af-3041-3d1d-ae46-dcff8c74c25f | -13.42533 | -46.86386 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 22.0 |
| d405a362-7cf5-3aa2-9ad5-a74ac1d7b386 | -15.623 | -52.72555 | 2025-08-27 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 520cc6ae-1e9e-33dc-b7a5-b9f849239d75 | -17.84023 | -47.74057 | 2025-08-27 04:27:00 | NOAA-20 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f7e8a493-1316-38df-875f-b3200069950e | -13.18189 | -44.03928 | 2025-08-27 04:27:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f08beff8-9c66-340d-b06c-1547bbf57b0a | -12.40474 | -46.50751 | 2025-08-27 04:27:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c68ad60-15b6-33e1-a5eb-bed9e7416795 | -13.3666 | -51.77723 | 2025-08-27 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dd5ec1a3-0cd1-350e-859b-048ceb39f064 | -13.06807 | -46.32687 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 00fb8011-c501-3592-b026-83d90eef1b40 | -13.06639 | -46.33789 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a8f88d8d-8fe4-38ab-aac8-0ccfb600219a | -11.82157 | -46.79416 | 2025-08-27 04:27:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e3721eac-da1b-3b8a-a2f7-0bcbec27f414 | -11.91809 | -46.74383 | 2025-08-27 04:27:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a8b30c0a-bd22-313a-a03a-99f15c420351 | -12.66942 | -47.88548 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b93279cc-41fe-3935-92a9-0b8329135a08 | -13.35709 | -54.39216 | 2025-08-27 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5972f6a8-09b8-3e65-b19b-4a37bae00a6c | -11.74672 | -49.08757 | 2025-08-27 04:27:00 | NOAA-20 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 82c5d07f-421a-39b1-a546-0feab0d2842c | -13.98485 | -46.35276 | 2025-08-27 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5bc216ba-d1b9-31cc-9368-80599361c776 | -9.4033 | -60.53437 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| d6669465-953c-326f-9714-f45e5e27a67e | -12.87319 | -48.09996 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b46617a3-20ac-3f97-bf39-381931837647 | -12.78717 | -48.10756 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9f883983-b625-3983-9180-6fcae8aaa30a | -12.93387 | -46.33586 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 19388a09-d7c7-3303-900d-ad5882bc882e | -12.93043 | -46.31298 | 2025-08-27 04:27:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| af73ae8c-c2e9-3352-8301-bdb2e4d009d5 | -13.44776 | -46.98586 | 2025-08-27 04:27:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| adcae1b3-9cca-3795-8c3e-87ffda7aa8c1 | -12.7125 | -48.1497 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cd17549-1326-3fdd-9f97-08a382027395 | -13.05058 | -46.30537 | 2025-08-27 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c412767e-d25f-329e-9fa7-5f7f895df673 | -12.75685 | -48.08452 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d84d66ec-424c-314c-b322-b651ca8d17b7 | -14.29596 | -60.36262 | 2025-08-27 04:27:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 737db2b7-b111-37c3-b9d2-bcc79c3852fa | -20.05525 | -42.6037 | 2025-08-27 04:27:00 | NOAA-20 | SÃO PEDRO DOS FERROS | MINAS GERAIS | Brasil | 3164001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4cd30694-b4c6-3031-b185-06ab7bd45130 | -18.0323 | -45.57337 | 2025-08-27 04:27:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 14255c98-a404-3ce7-a4a7-58b52ea3c8ec | -14.84572 | -49.2118 | 2025-08-27 04:27:00 | NOAA-20 | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e2600981-ecf6-39d7-af71-b0f05e3b0253 | -16.78256 | -47.56063 | 2025-08-27 04:27:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a7243697-934f-3b5a-a75f-5b18ab0fd4f8 | -14.32814 | -53.25895 | 2025-08-27 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b3c86a3c-aca8-3b07-ab71-6412ee492220 | -12.73698 | -48.08127 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5d326402-52d6-3c42-8308-fa00dbfbe5ad | -15.12186 | -48.67609 | 2025-08-27 04:27:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 68a5005d-f33e-3f4b-9d90-fa90e3fc37b8 | -11.919 | -47.10701 | 2025-08-27 04:27:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8063e0a-baf7-3f56-92dd-3200a88642ae | -19.05801 | -41.91003 | 2025-08-27 04:27:00 | NOAA-20 | CAPITÃO ANDRADE | MINAS GERAIS | Brasil | 3112653 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 123acf52-972e-3fe1-9206-ee683ea7df34 | -12.78489 | -48.14351 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 003bd329-0a48-346a-879a-2a4787c15cb6 | -9.41279 | -60.52272 | 2025-08-27 04:27:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 0ca1f60d-1748-3cd0-9040-db30d1a12064 | -12.8787 | -48.1081 | 2025-08-27 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 33875945-4d15-3786-a4c2-b86b6c7f3c30 | -12.89758 | -44.63714 | 2025-08-27 04:27:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README48.md)
