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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a63b5b8c-aac0-3e68-85fc-8730cc96cacb | -15.15225 | -47.95624 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41d22318-8149-39b0-bb29-b461bac4a39a | -15.58946 | -50.31199 | 2025-08-22 04:21:00 | NOAA-20 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee29f16a-b375-3055-923c-b32434159857 | -15.03161 | -54.86755 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1e2e5349-5b30-3413-b7d4-972ec32e2d1f | -13.65028 | -45.71028 | 2025-08-22 04:21:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 26a40059-d46a-3192-ae17-fe3e8319e893 | -12.98957 | -56.88456 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e391d30a-1c89-3aa0-a221-8956ce3c3713 | -13.03299 | -45.17825 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23601134-3e3a-3162-a61c-da799213c876 | -12.66183 | -47.80292 | 2025-08-22 04:21:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5eea23ef-250c-3563-b9ec-1bc91e4bf1d1 | -13.6298 | -46.87714 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c1a2e11-d455-34a3-91fc-684af17f05bd | -14.97051 | -47.14087 | 2025-08-22 04:21:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0ba41ebf-76be-33d4-abe6-7f4d214e1a58 | -12.50015 | -53.81656 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c42b60df-c467-364e-915a-9946992899b2 | -12.98226 | -56.88734 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| deeb93a3-3d9f-3aaa-b69f-d5afac7d623f | -13.03409 | -45.17104 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b58a65cf-69ee-3aaa-b948-739cdfb4b6fb | -17.91742 | -44.48255 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8eabc569-57fc-38c9-a78d-967f64aa37f4 | -12.93868 | -46.17992 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 006f5cc4-58a5-3bab-b915-a1de5f9d69a0 | -12.50118 | -53.81388 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fd2f8f4d-02ab-3b51-94a8-a5420edf343c | -16.28647 | -48.72644 | 2025-08-22 04:21:00 | NOAA-20 | GAMELEIRA DE GOIÁS | GOIÁS | Brasil | 5208152 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 36d8e871-a498-3e78-a34e-f21c2c2a374c | -15.02298 | -54.8599 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e1ef906f-4263-314f-9eca-80e12df0ad02 | -18.28473 | -45.51828 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a8368020-38bb-3aee-89d0-4b8686f3f90f | -15.83049 | -48.27552 | 2025-08-22 04:21:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 06d24994-c470-3c3b-b172-cc336c81867f | -13.16529 | -46.91325 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 842c5bd6-8303-3cba-b830-ce168150eeca | -12.94582 | -46.28621 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| dc1c2c7e-811a-3e7a-abc3-8049f4049a3e | -14.89021 | -47.97562 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3b06874c-0eb4-37f7-aeea-51550ed03f64 | -14.59806 | -54.78455 | 2025-08-22 04:21:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b65dfa42-76ea-3af9-87a6-ecda811d5ca0 | -18.93752 | -41.50127 | 2025-08-22 04:21:00 | NOAA-20 | GALILÉIA | MINAS GERAIS | Brasil | 3127305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6c1b97e2-45c4-341b-b697-6480c29d4c8b | -16.67719 | -49.16351 | 2025-08-22 04:21:00 | NOAA-20 | SENADOR CANEDO | GOIÁS | Brasil | 5220454 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e44170d1-6926-3995-ad7a-79d08e8988cc | -15.19633 | -48.69574 | 2025-08-22 04:21:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e592fa6-a86a-33d6-be5c-0e8f6af5ebc9 | -13.03023 | -45.19631 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5b6bc4ca-cbfe-3f50-93d5-92bd1c7e0222 | -17.83159 | -44.42863 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebfbff50-dca5-3945-b160-b1b7dfcd3774 | -13.03354 | -45.17464 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dac4f596-6d8d-3e89-a3b1-ff2da1bed904 | -16.55882 | -49.26261 | 2025-08-22 04:21:00 | NOAA-20 | GOIÂNIA | GOIÁS | Brasil | 5208707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f9ce2967-5036-3d3d-9c57-2607ce557ab2 | -16.1896 | -47.99035 | 2025-08-22 04:21:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75d4d7d5-175e-3c95-bb50-dee18121c83f | -14.70109 | -45.11608 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7946b44a-d8dc-3f02-a1ec-9e5168b01d8a | -13.38224 | -47.49019 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44c5953d-c521-3fe0-a00c-1ed03c7d31f3 | -14.46105 | -48.47246 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 040ee91f-a593-3745-8cf0-e282ee93ec6f | -13.36355 | -46.26364 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0051e754-fcfc-3bf8-abff-3b059e8bf754 | -14.7549 | -45.40784 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b75e1e82-1e0c-3473-95b1-977d0e55234f | -12.99527 | -56.88192 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ef75210-4826-31e7-8e95-c3178977500c | -20.242 | -46.60498 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e545662b-8bf5-3d5d-8cce-d9e6dc73245e | -19.67158 | -48.98848 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 7ab9f51f-5ed2-3382-be85-c731fb6aed6e | -13.0357 | -46.31899 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 10.5 |
| aa2c3fa6-0ceb-30bd-86c5-ab793095f167 | -13.64195 | -46.88631 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 585ebb57-a581-31cd-a363-6a88bc4a2e73 | -13.64526 | -46.88687 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a523fd7b-0c7d-36e9-a306-4c4bbb0fdc32 | -14.33252 | -53.0976 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bd857e42-e763-3154-9b54-1fd68552fd41 | -14.89779 | -48.05612 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9bf95b0c-c7fd-3015-96e9-2537f4b7c7f8 | -12.9508 | -46.27617 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 007cd6b3-8bd4-3d14-b402-6f5056aab240 | -17.8072 | -44.31701 | 2025-08-22 04:21:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9ae018d-dc5e-34ab-8e3f-a19a4f839516 | -13.00241 | -45.22142 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b64522f4-ae3e-3663-8cad-4691d417719d | -13.35804 | -46.25549 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 22512023-9e5c-3244-a0a8-3de1b262d415 | -14.88654 | -47.95588 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 00d6c006-1782-38a1-bd6d-35da777ef6ae | -12.94749 | -46.27563 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc21f809-c3cb-39ce-af5e-fba2b1486904 | -14.01355 | -49.17158 | 2025-08-22 04:21:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dd588c64-288a-34bd-9202-1784a0d77c31 | -13.02295 | -45.17667 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7fc6638a-33a9-343d-8214-7b568537f365 | -16.78856 | -47.66804 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3732eb09-6f10-3cea-b4fc-f32a49aac372 | -14.75993 | -45.3974 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 90534f54-8d5a-39a1-8fbb-d562efbc0da0 | -13.50042 | -47.04928 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| d4c462ae-4d46-389f-a533-b76dc92d8b4c | -20.30188 | -46.63026 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 5.0 |
| a7dcf627-b036-378a-aa17-e672fdf13d28 | -13.42323 | -43.67867 | 2025-08-22 04:21:00 | NOAA-20 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bf668fa6-e733-3198-8fff-88637fc64599 | -12.4878 | -53.80355 | 2025-08-22 04:21:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3d9f3871-4ff4-3589-a097-89eccef08009 | -14.864 | -47.96727 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80a3fe40-3c2a-359f-8473-f87c1fea1745 | -20.24579 | -46.69438 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4b052adc-764a-35e1-9558-48a4ca563299 | -13.03133 | -45.18908 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e3710e58-1baa-32b5-a812-b9b9136ba453 | -14.74399 | -56.05024 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6a667bc-5c48-3f72-bc9c-bce90c2c8f79 | -14.54767 | -53.15934 | 2025-08-22 04:21:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a6d8ff1d-3a48-38fa-b6b5-3046bdba706c | -15.13452 | -48.10808 | 2025-08-22 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ebb0e130-968f-3202-b6dc-563f7cef6da7 | -20.4292 | -46.50233 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 251f5024-8642-3a77-ad85-bed17b99c370 | -19.67097 | -48.99221 | 2025-08-22 04:21:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| e5cc7236-5df9-363f-b1e2-b51267158b95 | -16.7864 | -47.66024 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44538718-a7ae-30b9-883e-5643acd8666d | -14.75435 | -45.4115 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 16fb4ac4-5ca9-390b-af9c-36b406240c37 | -12.96185 | -46.27074 | 2025-08-22 04:21:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c53cb85b-4974-3a4b-9864-556418981d3e | -14.83053 | -47.92745 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d4e5d2f6-b81e-3b70-bcd0-e2ebc2d908b8 | -13.02854 | -45.18494 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80061cf9-cac1-3140-a405-70d51348e090 | -18.27619 | -45.55276 | 2025-08-22 04:21:00 | NOAA-20 | SÃO GONÇALO DO ABAETÉ | MINAS GERAIS | Brasil | 3161700 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| aa5a1f65-e2b2-39c6-a48e-56f568fad1d1 | -13.18014 | -54.95642 | 2025-08-22 04:21:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69cd890b-6e0b-384c-9e80-cf7f63c0bd52 | -13.49435 | -47.04459 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6eacc9c7-ef75-3396-9e3d-725a0ac12a6c | -13.38959 | -46.24997 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fd2b7cbe-0546-3aa0-b789-a28a7b591f55 | -14.88435 | -48.05382 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 01c82181-328e-345c-8c9d-e60cd0eed15f | -16.29438 | -43.80542 | 2025-08-22 04:21:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a6088847-f707-3dd3-9ba3-e08a8713865f | -14.88498 | -47.94431 | 2025-08-22 04:21:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 87162b24-29d5-3d4f-b886-21721fa9636d | -20.30244 | -46.6265 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaa45e15-c7d7-31fd-9a7e-03ad6da4ef57 | -13.37101 | -47.49594 | 2025-08-22 04:21:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2bc99413-7eb6-3c45-bc4d-09abd922f4a4 | -13.14083 | -46.8982 | 2025-08-22 04:21:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4d724494-9f3c-3c67-bd4c-bbe3957c92d0 | -14.44963 | -48.47792 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0506f654-44f3-3347-bf2e-96d63000bf87 | -12.97493 | -56.89421 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 06f2db96-395d-3e1c-b30a-da2018e8fe6c | -14.75914 | -56.02915 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 25c871b7-127c-349f-8d9b-7c2c6ff099f2 | -13.03184 | -46.32198 | 2025-08-22 04:21:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e637bad5-daa2-38e7-b2e4-294449405831 | -14.86427 | -48.32492 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d7a27723-0c54-38a2-b62f-974bc7ab6875 | -14.77037 | -56.00005 | 2025-08-22 04:21:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e1a68f16-9fae-3e75-a47e-dc255c0ea2c6 | -12.98065 | -56.89553 | 2025-08-22 04:21:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8de9d2d5-5b2f-312f-b06d-83b04e224ef6 | -13.02299 | -45.19885 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9bc4d15-02cb-3c9d-9f87-e1eff5cbfb58 | -16.78367 | -47.65605 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 36d31f5b-b49a-377c-a568-4e96fe4c4e44 | -15.00229 | -54.86259 | 2025-08-22 04:21:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ef5d7e77-e25a-3a22-ad0f-d9b12c07f451 | -20.43543 | -46.50704 | 2025-08-22 04:21:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dd2e7b0d-8b96-360a-a2a9-d9b577820cec | -16.78582 | -47.66385 | 2025-08-22 04:21:00 | NOAA-20 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a98310d4-a632-373e-b5e5-18672c38b810 | -13.58254 | -47.04453 | 2025-08-22 04:21:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 968a2656-f300-3025-97e6-c40e7a411db1 | -14.76275 | -45.42411 | 2025-08-22 04:21:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bb910767-af29-35ff-86a8-97dc832561f3 | -13.02523 | -45.20659 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be95fe5f-374c-3890-950b-f00d06267780 | -15.14897 | -48.11397 | 2025-08-22 04:21:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7d9f109-589b-3be8-aeb9-e40820a21a9d | -14.49544 | -48.83356 | 2025-08-22 04:21:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d2d252a4-72b8-3817-9d39-c85a2186954e | -20.3617 | -46.50734 | 2025-08-22 04:21:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed37806d-c52d-310f-abfa-63c12dafb3b1 | -13.02464 | -45.18803 | 2025-08-22 04:21:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README39.md)
