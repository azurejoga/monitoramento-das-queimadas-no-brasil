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

## Dados Diários - Página 59

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c16e6b2b-9390-31a0-a8d9-215a356e51b4 | -9.73412 | -48.97116 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f91dc69e-6fb6-34f7-9cb6-0df0b98f15fd | -11.08996 | -44.63783 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| a4b3a73a-3aa7-3945-aadb-b4459109d6e8 | -11.63675 | -52.04756 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18c0ac77-b0b0-3fda-8136-251f6821ee93 | -9.92831 | -51.62747 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 796024a1-ae85-3b84-8081-d9eef64114e8 | -9.3421 | -55.21935 | 2025-09-02 05:06:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 740d195a-8cc8-39e3-bbe3-758572833e6e | -14.78271 | -48.17911 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 22c3d5dc-72c4-3719-821e-859033373af2 | -11.66999 | -52.2219 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 170bf5cc-1d73-33e5-a749-55dbae342442 | -12.78912 | -48.07416 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8176806d-d47d-36ab-ba02-4729618ac894 | -11.0602 | -45.39001 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| e25cd887-5a0c-3fe9-a45d-32c46a121026 | -11.66396 | -52.20679 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 83042e32-989f-3901-b5a7-7f6a72fd8c82 | -13.3062 | -46.83818 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 67eb05f7-3015-3a34-8f86-757cdf530329 | -13.5298 | -46.99713 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2af6c37c-24e4-331c-81ab-3b310b818750 | -8.72607 | -62.41465 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c8a53a96-0c29-3589-8a33-92a5777d7cdc | -9.16228 | -58.89873 | 2025-09-02 05:06:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 221058e4-1644-3ba6-b60a-21d99b8b2cb2 | -10.28044 | -54.26654 | 2025-09-02 05:06:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99022850-b57a-38c1-b681-7e7296808ba2 | -12.92958 | -56.96038 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cfbc2c95-8c33-3bfb-af18-03d99d861b1c | -13.89334 | -48.10624 | 2025-09-02 05:06:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9bbc6cd0-0469-3578-91f3-933f54f23501 | -8.64293 | -63.27043 | 2025-09-02 05:06:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| efc80332-a449-3330-95c4-56f8f7937ac1 | -12.98163 | -54.76579 | 2025-09-02 05:06:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 51bc2cbb-c9d1-38ca-b5ef-38c1a94cc091 | -7.5404 | -61.32737 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 00f5b47a-bb6e-3a28-843b-50a724b77c70 | -12.99193 | -48.11678 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| befbb386-2f3a-341c-9c4d-771902d3a4dc | -11.57638 | -50.64236 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d55d43e8-b29b-3387-a456-297e03928507 | -10.29033 | -47.51265 | 2025-09-02 05:06:00 | NOAA-21 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a7f2afe-20c0-3282-9f2d-26209682cee9 | -11.66444 | -52.20332 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 3ae613ad-ca31-3105-a41a-b8671946d1d5 | -9.92067 | -51.62315 | 2025-09-02 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2f176e2-ff7e-3ea0-a150-79b714ba7838 | -9.74844 | -46.92508 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 129085bd-de57-38d3-9634-b951b0ea828a | -9.44053 | -48.86701 | 2025-09-02 05:06:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19c30527-0658-332b-b26c-bb04ad1bf508 | -13.32965 | -46.84035 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a72ff90e-cb63-3c6c-a129-90eb747bcf44 | -12.98925 | -48.09442 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 691d2703-accb-3837-ac55-022c7abf5259 | -11.01581 | -46.83138 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 9bfcf075-6286-33c8-881b-8ec22793dcad | -11.00761 | -46.82827 | 2025-09-02 05:06:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| f44446c9-39a3-31a6-8e05-4b7ab457a8fa | -12.93511 | -56.96851 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc1712aa-fbab-360c-b1ec-f3e4c28ae085 | -14.80063 | -48.21741 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3848c889-8b5b-335f-9ab9-b9d4e150888e | -10.79347 | -48.45322 | 2025-09-02 05:06:00 | NOAA-21 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2473a3f9-1d31-3b85-975f-317d7edf8b06 | -12.92624 | -56.93808 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7e6381a0-711f-30e9-b9b3-340579ed9d92 | -13.33019 | -46.83571 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1612937-625d-35fe-b9db-aa3d7e356652 | -12.9362 | -56.96144 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3091744b-ca1e-3240-a46b-dd146b48282f | -15.11692 | -48.18556 | 2025-09-02 05:06:00 | NOAA-21 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 53a4a03b-b174-3e03-8955-6b9962ed06ec | -12.85486 | -48.05423 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6db63d69-bcc7-329e-b641-2164691ad6e7 | -11.67991 | -52.20913 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| dadac46b-bae9-3e5d-8c34-89766163075c | -11.09521 | -44.64984 | 2025-09-02 05:06:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 0b151484-732a-3917-8c7b-515c4f9e2142 | -9.52094 | -46.50953 | 2025-09-02 05:06:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b825fa07-d973-35b8-af85-7c6a993889cb | -13.69023 | -46.93513 | 2025-09-02 05:06:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 066f5a37-c84f-3f98-a200-357d25907179 | -11.05949 | -52.06655 | 2025-09-02 05:06:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d26ab8-dc62-3873-b2bd-dcf8051e068c | -11.05378 | -46.8983 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 64329a4f-cc88-3a70-a8cf-535789e9b77d | -7.65985 | -61.0919 | 2025-09-02 05:06:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 80a4b183-0530-3d45-819f-bb6293494078 | -12.93565 | -56.96498 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 07561643-524d-3dde-8dba-3b21c7dfa61f | -14.58336 | -48.05634 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 882cb31b-d7da-3be0-9cb2-25de098a1924 | -9.60988 | -55.38545 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 729e9e1c-4b4d-3efc-aedb-81ffe0252ae6 | -11.67349 | -52.22597 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 90.4 |
| 29fc5dfb-7592-3cf8-81d9-ff72270c4525 | -11.43256 | -55.18584 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e0d4a538-62ac-3ed2-aecf-f91a3e0363dd | -13.53561 | -46.99776 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9eb7ea43-48f1-31bc-9a5f-d9aebac78ac0 | -14.40188 | -52.0708 | 2025-09-02 05:06:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0fcff9e5-8639-3ec3-aaea-529f4c303e87 | -12.92135 | -56.99162 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a63a733-2ee8-3296-ae9a-073a8f51c5d0 | -11.37738 | -43.56785 | 2025-09-02 05:06:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 54f32648-7ec1-3f97-9137-9525bbca696d | -10.83914 | -47.27514 | 2025-09-02 05:06:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2863ae33-77c1-37d1-b429-9a86f90f99c0 | -11.67893 | -52.21613 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b13c2b18-b3f7-345d-ab0d-121cac19d8c4 | -12.93735 | -56.99781 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 24d63138-78fa-3c0b-8bdc-b20101fea4a9 | -9.73073 | -48.95971 | 2025-09-02 05:06:00 | NOAA-21 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9d45c8cd-54bc-34b1-bb15-28f480bfdcad | -14.79281 | -48.18794 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bb3c983c-7108-33c5-94d6-e212f509598a | -9.40331 | -60.54719 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a6c58214-146d-3236-a4e0-18ab6641a154 | -13.09511 | -57.12121 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b590aa4-51f0-3df1-bed2-2bbd150aa6b6 | -11.82501 | -51.54276 | 2025-09-02 05:06:00 | NOAA-21 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1684bf19-3848-3656-bd93-f93701568113 | -9.60105 | -47.15867 | 2025-09-02 05:06:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 90af73df-5974-3c84-aba2-0322a2f3ddcb | -12.92742 | -56.99622 | 2025-09-02 05:06:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 546a45d5-9d37-3f51-90c7-293b4f782f64 | -11.31211 | -55.2178 | 2025-09-02 05:06:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ec5c6e58-6b51-3105-b20d-2703cfcdb163 | -10.76272 | -59.83604 | 2025-09-02 05:06:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3ea2ae2-846c-3775-8169-14c4ce1f9ff9 | -11.05847 | -45.39031 | 2025-09-02 05:06:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fd01c135-f728-3bc0-b830-a62bc9a4609f | -11.67136 | -52.18291 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.0 |
| 694a10e6-f9e7-3626-a099-f4acc0074d65 | -12.86145 | -48.04486 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| eb283ed6-5ccb-3106-b673-f6274fbdeffa | -11.6595 | -52.20964 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 86e46fb3-b9f9-3d6e-8254-c5df1cb65b13 | -11.43534 | -46.81598 | 2025-09-02 05:06:00 | NOAA-21 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c29cfe7e-b06d-35bc-8290-e104ef5e35d7 | -7.58682 | -61.62432 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 81a5cd90-8429-39e9-afda-4115ceb1263a | -11.86168 | -46.72395 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0a98a907-9bb5-315a-9d25-57097c17bce5 | -13.52922 | -47.0063 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 006681dd-907e-32d0-808e-faa89cc56681 | -10.06552 | -48.1272 | 2025-09-02 05:06:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a9e3e34a-bc76-3201-9ec4-343d8789c2d4 | -9.83115 | -48.31834 | 2025-09-02 05:06:00 | NOAA-21 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| a40beb3f-c3ee-3bc8-816c-5815d0167cf3 | -8.70974 | -62.40779 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c9cde35-cee8-3adc-95fc-33e3cca8e7c5 | -14.76821 | -48.15054 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09bfc951-37a2-33eb-b2b7-cbbebb1fba71 | -11.64626 | -52.03806 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| dfdbe040-d8e2-3de7-a2f6-a79db02102aa | -11.67796 | -52.22309 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 79f9fbe0-2462-334c-a2a2-9b2674a3463b | -11.89101 | -46.67326 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2fb7e80-a3bc-3c71-8f0c-387aa454db21 | -9.62102 | -55.37265 | 2025-09-02 05:06:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| acf46126-8b2b-38a3-a308-48932a5fed86 | -7.062 | -62.99553 | 2025-09-02 05:06:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42786aba-5a55-3e50-8665-46da5587ec9a | -12.64896 | -48.24992 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4cc6e179-b2e3-30bb-9edc-0dc8f5512262 | -11.67047 | -52.21844 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 493.4 |
| a4384cb6-97b2-3a1a-b9f2-1bdc52b7cf6f | -8.65617 | -57.87105 | 2025-09-02 05:06:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0192f145-858a-328d-9312-58cb0ff9a04d | -10.7417 | -62.18407 | 2025-09-02 05:06:00 | NOAA-21 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ab49902d-427f-3c52-86cd-8d00168a3d0b | -7.50925 | -63.49284 | 2025-09-02 05:06:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc712732-af0f-3940-b6f8-8eea9ad6e522 | -8.69629 | -62.40952 | 2025-09-02 05:06:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 0d7a7089-815d-3d2b-9ac7-53ef7d4f680f | -11.92017 | -46.67571 | 2025-09-02 05:06:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d2eacf5f-c8fa-30bc-a61a-9472a9ba0e88 | -7.54325 | -61.33517 | 2025-09-02 05:06:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 0f23ef76-7138-3eb3-905e-ea82000fc963 | -14.58685 | -48.06906 | 2025-09-02 05:06:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41357fb4-22f4-3c32-9531-966b32e1045d | -12.92763 | -48.10893 | 2025-09-02 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6c78c2c7-7b98-3e68-a397-878c9a641a04 | -9.50022 | -57.80454 | 2025-09-02 05:06:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4543551a-86bd-3e09-88e6-44d7f5663aed | -13.33441 | -46.8467 | 2025-09-02 05:06:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2886170-5dc0-33e1-88fd-518d81de7de6 | -8.96593 | -65.97521 | 2025-09-02 05:06:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f68a684f-b3f5-37a4-9c98-2367e22be42c | -14.58415 | -54.55288 | 2025-09-02 05:06:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 15aaab0c-f931-3fad-b4a5-91fc9ade1597 | -8.86835 | -52.03293 | 2025-09-02 05:06:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7462b54a-2ffb-3c14-b470-3fcea1c8afc7 | -9.75949 | -46.92694 | 2025-09-02 05:06:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README60.md)
