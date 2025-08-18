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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1a3d211d-0a3d-3c8a-acb3-ce180d4ec7b2 | -6.32907 | -44.71021 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c04ba461-75ed-358a-bca5-f0d7270b8e2f | -8.03556 | -47.67819 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cdcf25f8-1b7b-3222-8125-1c5a06f9770e | -6.88034 | -44.65484 | 2025-08-18 03:53:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 638eb8bd-9dd4-3a98-a30c-3edfc68ca56d | -8.04076 | -47.67912 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2b34f2e5-ca4c-3f15-820b-392eeebfd82e | -6.11218 | -46.66758 | 2025-08-18 03:53:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 87c5a3a1-c148-3795-9783-24bd2c62f97a | -4.78424 | -45.32422 | 2025-08-18 03:53:00 | NOAA-20 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 1cdd6db5-80fa-371b-803f-a378afd75acd | -8.50203 | -44.73783 | 2025-08-18 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d1abf1e9-d32b-34b1-87be-794fe67c3ff2 | -3.78882 | -41.00528 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 84c9fc18-ad86-3083-a031-4d1459866c45 | -6.42443 | -44.78631 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f970403f-9024-3ca3-8366-6fb4191c3100 | -7.29001 | -41.59708 | 2025-08-18 03:53:00 | NOAA-20 | AROEIRAS DO ITAIM | PIAUÍ | Brasil | 2200954 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| bdcc9b16-1250-31d3-a771-7484a3e18660 | -9.48852 | -40.36569 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 27.0 |
| 3040ca68-56ce-3cf8-964c-634878437836 | -5.98888 | -44.13073 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 74a320a0-1a56-347c-84b2-e68f87a7964c | -6.9802 | -41.63221 | 2025-08-18 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| f0766480-1469-3106-908c-5e31550987af | -6.76312 | -41.54003 | 2025-08-18 03:53:00 | NOAA-20 | SÃO JOSÉ DO PIAUÍ | PIAUÍ | Brasil | 2210201 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d1040f43-20c2-3609-b4f3-b9f582fe8b6f | -9.49267 | -40.37349 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |
| d88bbd0b-6662-37dc-a055-7cd9699c56eb | -3.38427 | -47.60793 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6864794b-d605-30f5-853a-bf02ae56ed58 | -5.75676 | -46.67001 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d1e7896d-a578-38cd-84c1-c46d44013d13 | -5.99727 | -44.13262 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28eb63ba-8b06-37f4-bb5a-2a75bc70bb80 | -6.07965 | -44.60748 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 39560812-fd77-3edc-a50d-b29d9e63efe7 | -5.98306 | -44.11361 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7637d33d-117a-3caa-959d-cd16dfe8a80c | -3.04697 | -47.39024 | 2025-08-18 03:53:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e634bd22-c572-35a5-b90b-2a4a01d9e914 | -5.99307 | -44.13169 | 2025-08-18 03:53:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9e293253-920f-312d-babb-4eb6e32150a8 | -6.98155 | -41.62387 | 2025-08-18 03:53:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 811e14b0-9a19-311f-8fa7-65f62854316f | -6.55351 | -43.0157 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0f7a6560-337f-3984-a538-14f24be24af4 | -5.75171 | -46.66912 | 2025-08-18 03:53:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 349cf0b7-2302-3bf0-84a1-2ab23332fabb | -8.10174 | -42.35586 | 2025-08-18 03:53:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 10c07047-56ea-3bfe-9d6f-0b61c5b6f06c | -6.98087 | -41.62803 | 2025-08-18 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 9.1 |
| eadf154e-fd90-3a4c-830f-ae07c90cc910 | -6.14578 | -42.70584 | 2025-08-18 03:53:00 | NOAA-20 | ANGICAL DO PIAUÍ | PIAUÍ | Brasil | 2200608 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f9c50b94-9171-3065-84d9-d9e239c30506 | -6.78397 | -44.35312 | 2025-08-18 03:53:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 43ecd5f8-536f-30ca-894a-941853011eea | -5.36107 | -41.22554 | 2025-08-18 03:53:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 4429a1d0-1271-32e3-bc2e-761ed39f9b8a | -8.49711 | -44.74108 | 2025-08-18 03:53:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3af25d6d-79ff-3231-a3b8-f206f0e50f9b | -7.55101 | -45.44815 | 2025-08-18 03:53:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5f3fa9f8-c2cd-3a5c-a6cc-01ab130e59e7 | -9.48737 | -40.37287 | 2025-08-18 03:53:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 106.5 |
| 87f61e7b-ef3f-38b7-a50d-18294d5f3ebf | -8.09734 | -42.35956 | 2025-08-18 03:53:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 69ec3c41-7006-3f8b-9950-613bba73811a | -8.03614 | -47.67498 | 2025-08-18 03:53:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 748f8da8-0a54-3170-bf0b-0617c63177ef | -3.79016 | -40.99697 | 2025-08-18 03:53:00 | NOAA-20 | TIANGUÁ | CEARÁ | Brasil | 2313401 | 23 | 33 | nan | nan | nan | Caatinga | 8.1 |
| f4ddee24-9387-3f58-8535-8fd7cb049850 | -6.93667 | -41.74043 | 2025-08-18 03:53:00 | NOAA-20 | DOM EXPEDITO LOPES | PIAUÍ | Brasil | 2203404 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| f4e36cad-c337-36f9-9002-bfdd8fb13832 | -6.36839 | -43.30766 | 2025-08-18 03:53:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ba2b19d-bbf9-3aac-a387-bfa5c40c0c46 | -6.03048 | -44.34357 | 2025-08-18 03:53:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7ca9cdd-5d86-3874-8d31-571427508f5d | -11.18617 | -45.06052 | 2025-08-18 03:55:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cb38a23-8e12-39b3-8cdd-43ea26a1fe5f | -14.18151 | -45.31118 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 309761d7-c02a-38db-b688-ce994ec3bfcd | -14.17815 | -45.30685 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d73e4490-7cae-3548-b44b-d09348faefb1 | -12.42275 | -43.764 | 2025-08-18 03:55:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 68.4 |
| 3f7b4264-96f8-31b1-8516-d9f0810d77ce | -13.22365 | -50.76683 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f83376f3-8c29-3b56-80e6-06339c5b7349 | -14.62203 | -54.91092 | 2025-08-18 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 80919e10-bcb3-3302-b1de-0349b45728e1 | -13.57593 | -46.9934 | 2025-08-18 03:55:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a32fe924-49fb-3e23-bdad-0318da17544c | -13.24255 | -50.79283 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 314243c4-51bb-38a0-90ba-b3bb865caaff | -13.22449 | -50.76265 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a2d6d98e-4094-3a6d-ab77-328224b4ed9c | -15.96528 | -43.90382 | 2025-08-18 03:55:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 16e7ee44-3b35-3ab0-b790-668d8438bc87 | -8.77955 | -49.99411 | 2025-08-18 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 3806b1b8-6452-3eb5-a6f2-20de25f412bd | -13.23363 | -50.74716 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 719973d6-e206-3f2d-ba13-9d82eecc04ae | -11.568 | -47.27311 | 2025-08-18 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9bfe5140-0d70-3e20-bedc-dee51b599f12 | -16.01265 | -48.08516 | 2025-08-18 03:55:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7143958b-a993-311f-9d45-c84fdfa9ba30 | -12.13037 | -47.90308 | 2025-08-18 03:55:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 58f9d26e-0e28-32d0-9518-075613028cee | -12.63116 | -46.89549 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2d5723d2-ca8b-3463-b9d9-eea7df30743a | -16.21664 | -43.14585 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 9f8035f6-5e47-3192-a345-913b80b6afa3 | -14.17541 | -45.299 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b832e28-216d-397c-86eb-6f08985b8092 | -8.78245 | -49.9935 | 2025-08-18 03:55:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 171ee02e-acff-3a06-abe0-330fc903905f | -12.52924 | -48.50029 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1be00d76-9116-35f5-9b97-8fade55d1480 | -13.21787 | -50.76558 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 357cfc5d-8c29-39ea-819e-068bb1d37d58 | -15.25002 | -49.52724 | 2025-08-18 03:55:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5dc8b598-b464-3fff-bc5e-b2a73ea4c2a0 | -13.43241 | -45.90363 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3d230438-2b75-3d2f-be90-b07fe02e3a28 | -13.9628 | -54.09249 | 2025-08-18 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e71f42bd-3b8a-3e6c-b484-6716a0f64a61 | -13.21294 | -50.76014 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 97f20add-acbe-337f-a62a-c7434b0d546f | -11.8443 | -51.58906 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cfc126d5-eb3e-39da-9322-d16ea0c5db7c | -13.21463 | -50.75177 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 09e02b6c-5c13-3036-ade0-c9bbd94d10a8 | -14.63583 | -54.90577 | 2025-08-18 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 928e28d4-04ab-375e-b8de-fbc6d31cc425 | -13.22111 | -50.7794 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c08ce373-dcca-3327-b0e4-a788f9d2425a | -12.53746 | -48.50204 | 2025-08-18 03:55:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99bf510a-d000-3a57-8b46-24eb51632ca4 | -13.96357 | -54.08355 | 2025-08-18 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b3675e0-d8e8-3bc7-9b30-b8d30bca6aeb | -9.18032 | -49.67112 | 2025-08-18 03:55:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2733d1ed-86a0-31b2-a921-7c12021abac2 | -14.63421 | -54.91299 | 2025-08-18 03:55:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 97a56889-4ade-3ea7-b972-991beeed1cc6 | -11.13629 | -47.28647 | 2025-08-18 03:55:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15982296-8bb7-3fb4-a685-a3328b391435 | -12.62116 | -46.89683 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 51820c0a-cffc-31f3-9abc-48b0eb39200e | -16.2181 | -43.14501 | 2025-08-18 03:55:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1354592-8f75-3764-ba57-3ee828220e9c | -13.22196 | -50.7752 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 21f11196-1a6b-39d7-8d20-62db0561b074 | -17.62411 | -39.92873 | 2025-08-18 03:55:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 4aad1735-3e04-3b63-bd6a-ca170d529074 | -15.25068 | -49.52403 | 2025-08-18 03:55:00 | NOAA-20 | RIALMA | GOIÁS | Brasil | 5218607 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e7d10095-9f26-3b8a-baf9-2360e5bb93c0 | -8.71518 | -47.86148 | 2025-08-18 03:55:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 733a6f4a-d556-3c73-93bc-6ad7f957e383 | -14.18024 | -45.31834 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 60b5b0a3-eccc-3f2e-a526-7689510cea6b | -12.61114 | -46.9002 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6521f354-884b-3729-a765-c5b6f515f398 | -13.44548 | -45.88107 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f50c2fbe-b787-39bc-aa0a-1ae5e570a146 | -14.17142 | -45.29822 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4c5b0497-08dd-3985-a320-a71a07aa7dcf | -15.49119 | -48.52752 | 2025-08-18 03:55:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7fe5d7c7-2a76-303b-9b68-8ac8daa7b22f | -13.44503 | -45.88148 | 2025-08-18 03:55:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a3b044bc-48f0-3ee3-aa41-46772eb5c14d | -13.2228 | -50.77101 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b6d832a7-0f06-31d0-ba9f-85736bbfe5d7 | -13.59715 | -47.74187 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c5f58ee6-cac4-35a1-aa4e-360ac14930a7 | -11.84946 | -51.59564 | 2025-08-18 03:55:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f54a898b-b087-3db1-afd2-1a19bb924703 | -12.73038 | -45.052 | 2025-08-18 03:55:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ce746537-7156-3933-943b-c234266c0d85 | -14.63612 | -54.9151 | 2025-08-18 03:55:00 | NOAA-20 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2a32a555-c5b6-3466-9757-7c8012491a18 | -13.58929 | -47.75749 | 2025-08-18 03:55:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4feee589-61c3-35e8-861f-6489a5f700eb | -13.2204 | -50.75302 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 760dbb03-7dda-304e-b588-fb7ebfb43324 | -12.30892 | -44.75751 | 2025-08-18 03:55:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fea519ce-2714-350d-a873-cf8b311498c0 | -12.63211 | -46.91566 | 2025-08-18 03:55:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8a8d3288-62dd-3dc7-b2ed-d3291f9ea8fe | -9.46211 | -44.42507 | 2025-08-18 03:55:00 | NOAA-20 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cde199d7-f07d-32f7-9251-9e63865bc05d | -13.22533 | -50.75846 | 2025-08-18 03:55:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e1ed82de-5c6d-3c6a-bec4-bc08aab30210 | -14.17878 | -45.3033 | 2025-08-18 03:55:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dd862ed-cecf-3a18-945e-791c9daf615e | -13.96202 | -54.0905 | 2025-08-18 03:55:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5a1230fb-4df5-3f43-b259-632838710452 | -14.63081 | -54.90547 | 2025-08-18 03:55:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1c3b5df3-bb7e-3c21-addb-ef5e716a3b9e | -14.1909 | -42.81013 | 2025-08-18 03:55:00 | NOAA-20 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |


[Clique aqui para ver as próximas entradas](README13.md)
