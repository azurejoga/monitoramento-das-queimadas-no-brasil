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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e8b701e1-19df-3321-9e29-cb42f5f3cc1e | -9.36601 | -45.73872 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c544184d-b0db-3ee6-a935-01c21474334e | -15.64803 | -47.84824 | 2025-07-29 04:21:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13773ff2-8489-3be9-9be0-d6770c6f4f6c | -14.32051 | -48.64956 | 2025-07-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7ae7fd31-65ae-35d0-9e44-59cf6ee6f37d | -12.98901 | -44.89319 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c0cda49-84cf-341d-8e16-0cd3f80b2a94 | -8.89088 | -47.34348 | 2025-07-29 04:21:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2a56f6c8-bc03-33b5-aa32-71448b4e7f70 | -11.98317 | -46.69921 | 2025-07-29 04:21:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ac78104-f84e-324d-aa4d-8c61efcbf9a8 | -14.50149 | -46.53587 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f9c5a08-9c3c-3934-876f-d6db252af517 | -9.46128 | -57.84489 | 2025-07-29 04:21:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7e7038b7-d663-358f-ae0b-e73ee48553a5 | -14.48609 | -50.29428 | 2025-07-29 04:21:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c572c37c-5777-3283-b7c5-a5e3868d79e3 | -13.52404 | -45.62278 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| ddc22771-c880-3b64-820c-94b8f2424495 | -13.13693 | -47.35694 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a361c650-9fab-303f-a80b-a7770cc17807 | -11.27406 | -44.64743 | 2025-07-29 04:21:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e02cf4a5-8133-309c-97b6-76001585b398 | -13.08869 | -52.13614 | 2025-07-29 04:21:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4bed5a2a-2b69-3a60-b299-1968b17b6681 | -9.99899 | -48.13078 | 2025-07-29 04:21:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22bb41b3-e270-3e62-99ae-9bd960e83cb2 | -13.12407 | -47.37663 | 2025-07-29 04:21:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4cf9107a-664b-3093-b66e-c220e644ea2d | -15.12702 | -45.32901 | 2025-07-29 04:21:00 | NOAA-21 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 870300cd-ff1e-3827-a37f-b3b06b55f064 | -14.82759 | -47.23136 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ef2ca38c-e1c1-391a-b5f9-ee2ba7754402 | -9.72758 | -48.30249 | 2025-07-29 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fe3b7f8-2cfe-31d4-905b-8dfb6ae4bb44 | -12.99576 | -44.89422 | 2025-07-29 04:21:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 086374b5-5876-33bb-8c01-534a90a278eb | -9.87142 | -44.69329 | 2025-07-29 04:21:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a8fe3b6a-ad6f-3411-bdde-646251045047 | -14.50369 | -46.54352 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| af5a399d-cae0-3dad-af95-ef7eec8397d3 | -9.72824 | -48.29855 | 2025-07-29 04:21:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 79aea80c-0161-3220-94a9-34f61d3f4249 | -14.83033 | -47.23548 | 2025-07-29 04:21:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b704865d-dea0-3413-b1c2-0d8f4d11d685 | -14.46208 | -47.88226 | 2025-07-29 04:21:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f92487db-eeb2-35dd-a2c6-edd792b21e93 | -9.36656 | -45.73524 | 2025-07-29 04:21:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 0eeb23dc-f790-3d69-84cb-bc87ee4b1996 | -14.50093 | -46.53943 | 2025-07-29 04:21:00 | NOAA-21 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ae3388b2-7dad-33eb-af8e-a8470d0cd86c | -8.49396 | -47.32132 | 2025-07-29 04:21:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cbceac0f-0711-3850-be6f-2e51d757de1c | -12.57916 | -49.79682 | 2025-07-29 04:21:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4056aa6-0c15-3cfc-856b-67d8e4f5a5ad | -11.43178 | -45.13108 | 2025-07-29 04:21:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 30ba0be1-3288-3cc0-9177-d66c1a794ef2 | -13.48728 | -45.59885 | 2025-07-29 04:21:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8348c2dd-30af-31b5-b35c-c31e7bef5328 | -23.01224 | -43.50766 | 2025-07-29 04:23:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ce2a31b5-4b87-39e7-ba7f-33cc3a04a7eb | -17.6709 | -44.12311 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1320737e-f15a-3627-9bbc-5e3fdc0b0e4c | -18.44611 | -54.66476 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 579dd63d-6b82-374f-9892-adc391d7beb7 | -18.43985 | -54.67304 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 534fcedb-edcf-3c93-be3c-5221b4b35eb1 | -20.59802 | -51.61129 | 2025-07-29 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0b2a62fe-4306-3a3b-a3cb-1b66820363d3 | -15.87004 | -52.40925 | 2025-07-29 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ff655fd9-ff30-3ba1-b765-ee4a47f2c408 | -17.6002 | -48.42666 | 2025-07-29 04:23:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b150ba3e-c234-3841-81a7-63626c4dd299 | -18.43627 | -54.66758 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 18a0e978-4e72-3cb0-988d-dd26fb88fd9d | -16.66181 | -47.7206 | 2025-07-29 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c860553-2a30-346c-8646-a522a7e570da | -22.53304 | -43.55826 | 2025-07-29 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 195e6c52-38d2-3be2-92fd-dab83658053c | -18.45058 | -54.66568 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab485d71-ce46-3482-87bb-b958e916dff5 | -18.44969 | -54.67026 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f643340-b358-3783-a247-77dd82cb410f | -17.6703 | -44.12739 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63b5cf21-8d2a-37d8-8ae9-d7f048de9442 | -22.53239 | -43.56345 | 2025-07-29 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 84e58762-dc4e-3caa-9303-0eff49a40634 | -15.87071 | -52.40544 | 2025-07-29 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1a9b3c29-d29d-3030-8137-521ada90a5cd | -15.87002 | -52.40914 | 2025-07-29 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d9d9ed73-419a-33fe-9641-da92ddd6f522 | -22.52846 | -43.56259 | 2025-07-29 04:23:00 | NOAA-21 | MIGUEL PEREIRA | RIO DE JANEIRO | Brasil | 3302908 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| c4148caa-b036-3877-a6a8-c977ba13c0d1 | -18.44164 | -54.66387 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| b515c702-1145-3b54-9f48-e888d290b0c0 | -17.04682 | -43.77851 | 2025-07-29 04:23:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 10707c23-4f7c-34d3-aa2f-e8d67cf11e9e | -17.69296 | -44.20385 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad82874b-a4d0-3999-abd8-4b0c0bbfbd4d | -16.66238 | -47.71699 | 2025-07-29 04:23:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 21fec36d-6294-3800-a2c4-0fdb4b4f949b | -17.04316 | -43.77794 | 2025-07-29 04:23:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5286d7bb-ef0a-3674-8666-fe9912b427cb | -18.43448 | -54.67677 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaec4b0f-319a-3761-90b8-743dde499ec7 | -19.94989 | -54.39066 | 2025-07-29 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbeb9e6c-644e-3d9f-9f86-1a21fbc51ce9 | -17.7013 | -44.22315 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8fc363d7-09ef-3b8e-9758-63d2a62cf295 | -15.8707 | -52.40554 | 2025-07-29 04:23:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 44245363-df8c-3ca1-8cb7-3c2b69a85747 | -18.43538 | -54.67216 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f0cdbad7-55db-3819-b8af-add0584b1acb | -17.66668 | -44.12683 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9fb6890-fb86-30e4-8447-2d99e04139c4 | -16.03324 | -51.39169 | 2025-07-29 04:23:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2c203b7-07d3-3ecc-abdb-07300d6b9c90 | -18.5301 | -46.284 | 2025-07-29 04:23:00 | NOAA-21 | PRESIDENTE OLEGÁRIO | MINAS GERAIS | Brasil | 3153400 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9b39ca6-5dc9-36c0-b77d-8b087797cdc5 | -17.04744 | -43.77398 | 2025-07-29 04:23:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3212808a-3b9c-3c5e-acf4-53037c2cea46 | -20.63989 | -42.90514 | 2025-07-29 04:23:00 | NOAA-21 | TEIXEIRAS | MINAS GERAIS | Brasil | 3168507 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 2c493661-2a38-3502-88e5-ea7133cac632 | -18.44075 | -54.66845 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 2353870a-aa68-332c-bd11-3597490ba689 | -17.66727 | -44.12254 | 2025-07-29 04:23:00 | NOAA-21 | JOAQUIM FELÍCIO | MINAS GERAIS | Brasil | 3136405 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46e53baa-a802-3fa6-84f5-b3d8e3716a90 | -20.2945 | -54.074 | 2025-07-29 04:23:00 | NOAA-21 | JARAGUARI | MATO GROSSO DO SUL | Brasil | 5004908 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eb789359-7b37-3943-8661-ca25c5bef2bb | -18.13969 | -48.13758 | 2025-07-29 04:23:00 | NOAA-21 | GOIANDIRA | GOIÁS | Brasil | 5208509 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 44fcb812-c5ca-39c3-a13b-7dfebc3a687f | -18.43716 | -54.66299 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 129d1036-4cd9-36d8-bea6-7e3ab8e4265b | -21.77011 | -43.30774 | 2025-07-29 04:23:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| c394d9eb-ff24-317f-bf04-58d1d62ba534 | -18.44791 | -54.67946 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 912c3262-9767-3ef1-9823-4a6b2f100dd2 | -20.09501 | -49.95199 | 2025-07-29 04:23:00 | NOAA-21 | CARDOSO | SÃO PAULO | Brasil | 3510708 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| f243796d-429d-3d5c-9a1c-f6627dcab4d6 | -18.44523 | -54.66933 | 2025-07-29 04:23:00 | NOAA-21 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2ad0121e-429e-393a-b0de-fa5a742926b8 | -20.599 | -51.60976 | 2025-07-29 04:23:00 | NOAA-21 | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 35c13c06-a9f1-3c41-a999-b336a9d4ca0c | -23.40056 | -47.0065 | 2025-07-29 04:25:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ff5fa8a0-f3f2-3d6e-b3d5-71561e5afb9d | -27.88191 | -48.6296 | 2025-07-29 04:25:00 | NOAA-21 | PALHOÇA | SANTA CATARINA | Brasil | 4211900 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| abee8ee1-a386-3ddf-940f-aeb8a8fecb9f | -23.01217 | -46.49665 | 2025-07-29 04:25:00 | NOAA-21 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| ae1d353e-67ba-3a80-a8bf-19d183017ec6 | -22.58615 | -48.16061 | 2025-07-29 04:25:00 | NOAA-21 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| 5fc6ae37-99df-3204-9966-dfd9d71b1088 | -21.77649 | -52.75083 | 2025-07-29 04:25:00 | NOAA-21 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d023b4cc-6232-32b3-bbe3-b5986fff077e | -23.39997 | -47.01049 | 2025-07-29 04:25:00 | NOAA-21 | PIRAPORA DO BOM JESUS | SÃO PAULO | Brasil | 3539103 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 60c59618-b8c8-3f66-9c09-704ba18d41f7 | -22.58226 | -48.16376 | 2025-07-29 04:25:00 | NOAA-21 | SANTA MARIA DA SERRA | SÃO PAULO | Brasil | 3547007 | 35 | 33 | nan | nan | nan | Cerrado | 0.0 |
| dbfb322c-f9fa-3ca8-a6bb-6c0336eb6b08 | -32.04475 | -52.09256 | 2025-07-29 04:27:00 | NOAA-21 | RIO GRANDE | RIO GRANDE DO SUL | Brasil | 4315602 | 43 | 33 | nan | nan | nan | Pampa | 0.4 |
| d821de9c-9a18-3c50-9a7c-8d0559c19a1f | -18.4486 | -54.6674 | 2025-07-29 04:30:00 | GOES-19 | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 9cdf6ef7-16c7-3a8c-9131-dc42fb9e96ad | -11.4389 | -45.1385 | 2025-07-29 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 53.3 |
| 1e64a9cb-7eb1-3cd6-8f01-32bea3e3b53c | -11.4201 | -45.1181 | 2025-07-29 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.1 |
| 81721af7-f7e3-3203-87cd-b64782eb3eb5 | -11.4393 | -45.1154 | 2025-07-29 04:30:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 82.6 |
| b2afed15-13a4-3730-89d0-3764c2506bbf | -11.4393 | -45.1154 | 2025-07-29 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 93c86445-b919-3a89-99eb-2349fb0ca002 | -6.5631 | -51.1126 | 2025-07-29 04:40:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 52.4 |
| 4c262bbe-3fcf-354b-ad1c-1f547509721e | -11.4201 | -45.1181 | 2025-07-29 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| a86e18c1-198e-3565-9eab-c15188c2e8ad | -11.4389 | -45.1385 | 2025-07-29 04:40:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 4a5b2a52-6651-30d4-b1ad-9fbd1ce01c1e | -6.39996 | -53.36462 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c8fecf9d-5ddc-3940-813f-36d5e6676b8c | -2.66762 | -47.40759 | 2025-07-29 04:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d94a09b4-916b-3550-8538-3f5a250b664b | -3.21768 | -48.81525 | 2025-07-29 04:46:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 082569e8-2047-376d-ab23-313ded184188 | -3.25285 | -43.2675 | 2025-07-29 04:46:00 | NPP-375D | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5722ba61-0db5-3ef5-bc6f-ad311dc427d5 | -6.40408 | -53.31763 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 855383ea-1454-3790-8919-07540600b090 | -6.39552 | -53.34798 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 40778039-b032-399d-8700-574808031756 | -7.19574 | -44.1818 | 2025-07-29 04:46:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f55de57a-2905-3f4d-b7ec-d8b72d8e6cdf | -6.77238 | -50.48953 | 2025-07-29 04:46:00 | NPP-375D | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 82524b30-42ce-3fcc-ada2-a6aec7fd0b96 | -2.88766 | -48.28804 | 2025-07-29 04:46:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 3ea1aec9-31ce-3a58-8adb-c449c116e297 | -6.41584 | -53.35523 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 943ff6a0-1553-3456-b996-c85d6cc50404 | -3.88555 | -54.21309 | 2025-07-29 04:46:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b1b0d5-ae74-33aa-bf1d-a9a5600d1667 | -6.40536 | -53.35355 | 2025-07-29 04:46:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |


[Clique aqui para ver as próximas entradas](README15.md)
