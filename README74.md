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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6aaad4b-2d8a-33a2-baa4-3e3312aff423 | -11.31445 | -54.04114 | 2026-09-22 04:49:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85fe24b9-3a3c-32f4-9168-d448f0912cec | -14.04957 | -52.05563 | 2026-09-22 04:49:00 | NOAA-21 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f09e3180-7506-3dd4-83b9-d7c7387509ae | -17.38015 | -46.76127 | 2026-09-22 04:49:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4e1fa720-7cd2-3ab8-973f-9d20c228f8ed | -11.47829 | -54.94603 | 2026-09-22 04:49:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6e4cf6e0-e1c7-36d2-a622-2a0b2c2ce78e | -13.54624 | -47.66554 | 2026-09-22 04:49:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ab148b86-7844-3a95-809b-bc100f918049 | -11.87615 | -46.84734 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7a06585a-8560-38d8-a61c-ccbbb0995c2c | -12.0272 | -47.81279 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4e72ae19-2b69-3966-a254-be0d032f45e3 | -10.4228 | -53.7933 | 2026-09-22 04:49:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 85ffdbef-2d63-3dcc-82c6-347e827f8f8d | -10.59869 | -53.98904 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ab03ee10-55c2-3df6-8343-9360d8a5de7d | -15.85932 | -49.88881 | 2026-09-22 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ed53fcb3-0b78-3e9d-bea8-d39e8e6cd4a5 | -11.84644 | -46.81553 | 2026-09-22 04:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5ce13cc-688e-33aa-b528-54ec8b963473 | -12.77057 | -52.85098 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f8d5c8e-7f64-3100-b633-dab1faf65179 | -9.28126 | -60.6243 | 2026-09-22 04:49:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 18bc9e0c-6380-3a3d-aa4e-f3df737dbfa5 | -14.31409 | -50.49406 | 2026-09-22 04:49:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 56a20e36-f776-36ed-8d6f-cb0469357635 | -12.14497 | -47.39957 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1d057000-cdb1-3f4a-908b-50975777fdb7 | -9.40127 | -65.91485 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c1957380-6cdc-3527-a1ed-c26b13aa01f3 | -12.26787 | -50.14494 | 2026-09-22 04:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 495d8960-efd4-303e-be49-79106e5c19d6 | -15.86297 | -49.88936 | 2026-09-22 04:49:00 | NOAA-21 | GOIÁS | GOIÁS | Brasil | 5208905 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 9d90e0ef-af91-3fbf-bd42-3d80e9a02162 | -9.12227 | -65.8716 | 2026-09-22 04:49:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e2f097f0-b5d8-343f-bc8d-a4859acc59a1 | -12.02793 | -47.80742 | 2026-09-22 04:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| ff56b9be-ee71-354e-b066-04335ae76838 | -12.149 | -47.40017 | 2026-09-22 04:49:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f23e5f77-67f9-3ec1-9798-bf2e553021ea | -11.94295 | -46.51472 | 2026-09-22 04:49:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f550b67a-84b2-3c17-954d-4efce2754717 | -12.31217 | -50.69637 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ad491986-706b-3d1a-bc41-63c5e7694f46 | -15.44535 | -48.48079 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb49d5c5-08e1-33fe-8e60-c22b0c62b481 | -9.56385 | -66.04359 | 2026-09-22 04:49:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0c3fd9c-ef1e-32d3-b328-c23c4b5116a3 | -12.77443 | -52.848 | 2026-09-22 04:49:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e9dbf044-8b63-3137-822b-ee41ec3aecab | -10.61349 | -53.98386 | 2026-09-22 04:49:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ba8f3e8a-2139-38ca-b583-ffa10d311b82 | -15.4477 | -48.43351 | 2026-09-22 04:49:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 032ba15a-a8ed-3c77-af8d-02420a076895 | -12.33715 | -50.66948 | 2026-09-22 04:49:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ebb477bf-382b-3277-83ad-3b2bd84cb82b | -12.93354 | -51.0385 | 2026-09-22 04:49:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a549056-ada5-325b-b6dc-62eb62e93007 | -18.03708 | -50.91929 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7530d09a-f447-3d45-b722-ae1e0720f675 | -18.03648 | -50.92356 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 712eb2ab-f56b-39ba-828a-338fb51f76c0 | -17.85322 | -52.35262 | 2026-09-22 04:51:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bdd71418-7d56-3fdb-8462-e0be62a8a722 | -18.65212 | -52.16471 | 2026-09-22 04:51:00 | NOAA-21 | APORÉ | GOIÁS | Brasil | 5201504 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 09a3f69d-1270-3809-85fd-9dc4b97a4038 | -18.37763 | -50.59581 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 712cfacf-ed38-3772-8f79-9dd356b6969c | -18.51955 | -50.32175 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 12e97f3b-02da-32f5-aa10-15c5dccb1bc5 | -18.11599 | -51.15167 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75cfcef5-d0ef-32b5-a75e-64ab275e96eb | -18.03768 | -50.91507 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 35b359d9-3bf4-3e69-bc86-ba773cc315a9 | -16.84715 | -56.7883 | 2026-09-22 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0446ebe7-ce7a-3420-a6a5-24d2159e8549 | -21.2517 | -49.17907 | 2026-09-22 04:51:00 | NOAA-21 | URUPÊS | SÃO PAULO | Brasil | 3556008 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 47bcd7f0-3d6d-3d0e-ac6a-c8d678a3ed97 | -18.80476 | -47.55576 | 2026-09-22 04:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6633788f-5d90-3149-b16f-9bc267e40dcf | -16.84789 | -56.78403 | 2026-09-22 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| e6bcba61-0df8-35e0-b8ba-aeb87c2c5aff | -18.80911 | -47.55652 | 2026-09-22 04:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 16e9b67f-7bf3-3ec4-a5a0-3019e97ed741 | -18.77175 | -45.11928 | 2026-09-22 04:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d031807-60be-3c7a-b888-d85675ebd9f6 | -19.40817 | -46.41571 | 2026-09-22 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f4971ec2-cff5-3024-8a73-8776e269e20f | -18.04003 | -50.92411 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 72e65727-76e6-3b0f-8551-69ff476fe94e | -18.51644 | -50.34471 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 94c6ebeb-2b66-3a02-85f6-ae636f36fbd3 | -16.99236 | -56.45198 | 2026-09-22 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f65b700f-b71b-3c2b-a026-46685bf1610d | -18.51582 | -50.34929 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 83a53ca8-19a5-3959-a8ee-6b8a17231a89 | -18.52199 | -50.3315 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 1cb90245-0aa6-3d7e-bd5c-97ae8a3bbec0 | -18.51831 | -50.33093 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 5b7ec61a-e89b-3820-ab3e-85cdcc7be34a | -17.55506 | -50.14557 | 2026-09-22 04:51:00 | NOAA-21 | ACREÚNA | GOIÁS | Brasil | 5200134 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0f5d9d05-4f4a-338a-afd6-a7fc951d0823 | -16.85147 | -56.78469 | 2026-09-22 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c0d49b0b-6c87-3acc-84a4-f18b21da0c0e | -18.81347 | -47.55725 | 2026-09-22 04:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9f5c454b-1ee7-3008-9c3d-248b5f80bc89 | -18.52017 | -50.31716 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 0d58b5df-3201-313e-b332-59d7d7c86aa1 | -16.99306 | -56.44787 | 2026-09-22 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 556ae5dc-46bf-3353-b748-fc97297a99ce | -17.83966 | -45.7877 | 2026-09-22 04:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 442afbc2-615b-350e-9514-210d10007b64 | -18.52136 | -50.33611 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| fecb835d-597a-3081-b63a-9f1a7eb57608 | -18.52011 | -50.34531 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| ce1f0aaf-ef5b-3618-b271-fe593bd24541 | -16.92843 | -53.58195 | 2026-09-22 04:51:00 | NOAA-21 | ALTO GARÇAS | MATO GROSSO | Brasil | 5100409 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6818cce3-8d09-36fc-9638-0f4e69e282f2 | -18.03827 | -50.91087 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff98811c-8d10-30c0-97d1-d8e85d8d4be7 | -16.84357 | -56.78764 | 2026-09-22 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| df79e647-ca86-3a7c-9813-f528471007cd | -16.84641 | -56.79256 | 2026-09-22 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7f036802-1cff-3955-bc24-a0b6b532da86 | -18.04064 | -50.91984 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0ef2fd98-eafe-35bf-adf8-9c1f72c638af | -18.03943 | -50.92839 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| ff517c93-b7db-3d39-9dd6-5de4b467c590 | -18.51893 | -50.32634 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| ed12d4e0-9b51-3c12-bb3e-d8731fa4e6e3 | -19.41295 | -46.4162 | 2026-09-22 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17330032-eed6-3ebf-a74a-fc3c0eb4392c | -19.40873 | -46.41071 | 2026-09-22 04:51:00 | NOAA-21 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 520e3622-02a3-3d49-90c8-b92ddc6f052b | -18.51949 | -50.34988 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 848f604e-6793-3f59-8127-6a034024341a | -18.04479 | -50.91621 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 455e8263-a427-3063-85df-8c58fc9dfe70 | -18.04298 | -50.92893 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 84981fb2-a3c8-3d34-8b9b-b16ff76ba66d | -18.04654 | -50.92948 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7475e28-22ab-3313-9d5a-6b8b90a6599f | -18.04123 | -50.91563 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1261c0e5-0e55-3111-af89-44e6e09cf9cc | -18.76662 | -45.1185 | 2026-09-22 04:51:00 | NOAA-21 | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9dbb12c-7fcb-3d1d-bb9a-3681aaf928ea | -18.80858 | -47.56089 | 2026-09-22 04:51:00 | NOAA-21 | MONTE CARMELO | MINAS GERAIS | Brasil | 3143104 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c65e40cc-2617-3d6c-a539-da1619afd7d6 | -18.52074 | -50.34072 | 2026-09-22 04:51:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 31.7 |
| 03378090-2612-3d7f-a694-63c9fd9c9623 | -18.03587 | -50.92785 | 2026-09-22 04:51:00 | NOAA-21 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 16.4 |
| bac3dbfc-ae8a-3f04-8154-67bf8a5eaf69 | -8.8 | -44.28 | 2026-09-22 05:15:00 | MSG-03 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1212fdea-c575-3b24-b489-5de53c729ae2 | -8.8 | -44.33 | 2026-09-22 05:15:00 | MSG-03 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2efc484a-46a9-37c5-b159-dd082874e8a5 | -8.77 | -44.28 | 2026-09-22 05:15:00 | MSG-03 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 009117bf-4e01-30f2-b2a8-f52fdea608b2 | 3.3504 | -51.60243 | 2026-09-22 05:21:00 | NPP-375D | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9f5a74b7-3b8f-38b9-bce2-05f39fb737bc | 4.25517 | -60.64471 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fef99b06-ca0d-3352-b8c8-1cada6eb895b | 1.0796 | -60.6741 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee005e2a-3c23-371b-87a6-a48a47af6193 | 1.9908 | -50.86235 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94107179-a1b1-3609-8ce6-70a1ea86f94a | 1.54711 | -55.78981 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 497174d0-e3ea-3a39-8f32-e681fab5c016 | 1.96357 | -60.56974 | 2026-09-22 05:21:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9300bf79-337e-38c8-8963-7ec7ac9ef2ed | 1.99161 | -50.86735 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3a573df0-2ed2-3956-b45a-799fb1058449 | 1.53328 | -55.78843 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 06f092ea-81a7-306a-aafd-570ce55c613a | 1.97355 | -50.88052 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2002a612-51ed-3134-b64c-b03c5fc6bc50 | 1.81342 | -56.0813 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 665f5c7b-3b10-32ed-83ed-c8e95beeec9c | 1.54701 | -55.85348 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 24441c3e-52a3-3e53-85d9-640a9f6ff863 | 1.9783 | -50.88487 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b929aac4-6461-3409-b850-6bce28ee46a5 | 1.07666 | -60.68183 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 727c4dbb-cf24-3680-a203-41a89494b048 | 4.81361 | -60.3222 | 2026-09-22 05:21:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e5405826-5d85-34d6-aa39-8bbd2c110c88 | 1.98291 | -50.86361 | 2026-09-22 05:21:00 | NPP-375D | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2330a4fe-d3a8-386c-b45e-fd188e21776d | 4.58648 | -60.72296 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce922d17-0cdd-31b5-b428-6df80cc64091 | 4.58895 | -60.7231 | 2026-09-22 05:21:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4191c31b-c1a8-3601-a0e3-51fa9eb9a3cc | 1.52941 | -55.7855 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b6ede11d-058e-3506-be36-de8b38c2978e | 1.07556 | -60.67477 | 2026-09-22 05:21:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 63a23c8c-621a-32ec-b251-df34a5521a5f | 1.54379 | -55.79033 | 2026-09-22 05:21:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README75.md)
