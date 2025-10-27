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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 804aaef4-276e-3b4d-aae8-a7ce84469274 | -11.61121 | -50.98354 | 2025-10-27 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 1500a973-eb4a-3df6-8c16-ed9864434870 | -13.23915 | -47.99361 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ef0ae1f0-e74f-35dc-bd0a-121e6a5e51f8 | -16.37762 | -47.419 | 2025-10-27 04:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f4bfaa4c-c7c0-3428-8a7d-c282c247c9af | -17.31914 | -43.60537 | 2025-10-27 04:34:00 | NOAA-21 | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c352b87d-330e-3058-9e83-9d4b080bd277 | -11.03254 | -47.86896 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c7c3bcca-b5b8-3989-b9b5-795ece35ff25 | -10.91403 | -48.02024 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f4606981-4cd6-3ab7-a76d-eafaad8707ea | -10.38118 | -48.03691 | 2025-10-27 04:34:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d16c82a8-b47c-330d-89a7-055837ed7bd6 | -17.41377 | -46.74283 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02dad915-1b61-34c8-a155-022e2763dfd5 | -10.91058 | -47.95465 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0dd9ba5d-b6c2-3999-8c73-b490bb191311 | -17.21475 | -47.65553 | 2025-10-27 04:34:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdbd9596-1574-30f8-89c1-cb4be112cd73 | -10.31595 | -47.17276 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10f6234f-eea2-3c0e-866c-fafea59e1d3f | -12.32366 | -47.48432 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54145b8c-635d-33b6-a58c-267e695be87e | -13.26365 | -47.96782 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| beeba08b-d85a-35fc-a276-8f489c289e88 | -11.14573 | -44.93848 | 2025-10-27 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9de2fef4-dac4-33b6-9bd3-0b407ab3c48a | -10.82573 | -47.62094 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| bd8a594e-5708-3ec3-b40c-e8d08715683f | -15.13957 | -47.93778 | 2025-10-27 04:34:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1874302f-f270-3d10-b940-b5dd1ce8fdab | -11.33414 | -53.93324 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d9fc042d-32b8-39f8-a2b5-e66b8ced3ff6 | -10.97158 | -47.86669 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2135befd-273a-3b1d-beca-030ff9d01fcc | -11.80054 | -52.49606 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8f5ce133-9e2c-3432-b168-256a3d7d7356 | -11.43095 | -46.12362 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7ea0b7b0-1ac0-3a38-b175-138932ae29f9 | -12.32595 | -47.49205 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 76168328-ecfa-3d19-94c8-63669341f362 | -12.33318 | -47.46686 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0f48c3b4-a362-302a-92d1-c8800d4f2da2 | -11.02577 | -47.82434 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 660e8991-6e3d-37e8-8774-25578ae00f62 | -11.05893 | -50.35802 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 20de36ce-f7e2-3c3d-b68a-82563a92b7fa | -11.91369 | -43.82022 | 2025-10-27 04:34:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 0e241571-5273-3a3c-9860-9ec73d877f68 | -12.35646 | -50.16354 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2a363f81-12ee-30d9-89a0-0b7e05a0933f | -13.36532 | -47.40582 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b8944989-21cf-360f-acd7-f0925a1b7809 | -10.32056 | -47.21059 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 570f22cb-2b6f-32b5-8211-de20fa82bf91 | -11.71166 | -44.43901 | 2025-10-27 04:34:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 3aad1535-ceeb-30f3-8198-1a6775bd4f66 | -10.9139 | -47.95517 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf941dd1-5dad-3b30-940b-423a8008bed0 | -13.64669 | -47.6338 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d012d479-473b-32e4-b09a-24affd9b1b8e | -14.83114 | -52.42908 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9efc4bf2-f021-3e5f-a002-5e7c6da97ab7 | -10.33963 | -47.221 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9f9cd0cd-c732-3a4b-a9fc-04debc7ba5f7 | -12.28806 | -43.75559 | 2025-10-27 04:34:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 909c5d65-746b-384f-af6e-5b4dd75a1963 | -10.04813 | -48.16689 | 2025-10-27 04:34:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f917c9ea-b730-3116-82d7-1995701a7063 | -14.5631 | -47.9988 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 60dfac01-fb13-374c-ad7b-b74fcec85235 | -11.0291 | -47.82489 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1686b44f-4b21-3acc-9cb6-82aa4b068ce1 | -12.66452 | -52.63118 | 2025-10-27 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 28a4921b-50f6-3fd4-a9eb-7f2e80fc944d | -9.59783 | -50.78876 | 2025-10-27 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0b9ce675-2b41-3085-814d-bff427de9689 | -13.00955 | -48.54213 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1ccd2c8-65db-3fb0-9182-d315d969be74 | -14.48823 | -47.8883 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b8acb2e-731d-317e-b2eb-f1d5130857e9 | -16.44054 | -51.80984 | 2025-10-27 04:34:00 | NOAA-21 | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a858f289-6df4-3ab3-ab76-e52fee048642 | -14.6323 | -48.42062 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfa8fb9e-f55e-3ae3-9233-e7d2be5b04d7 | -10.62774 | -47.89231 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 02747964-37d0-351e-89fa-a36ca35a1d29 | -16.71647 | -47.64655 | 2025-10-27 04:34:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| dc766527-4ef1-37c4-b1cc-50c02811ea24 | -17.41323 | -46.88284 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 83107bb6-8d99-3ab3-b293-f65992104486 | -12.35524 | -48.10933 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3347aa7d-9f55-3359-ac84-699f899ea194 | -15.4512 | -50.4823 | 2025-10-27 04:34:00 | NOAA-21 | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 535578bf-e982-3660-9df0-7cb021e87b6f | -13.2603 | -47.96728 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2f4d697c-21d3-33ce-8057-1663ef302a94 | -14.39512 | -51.54548 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94ff6ae0-1b4d-359b-bd3c-00d923660057 | -13.25975 | -47.97092 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53cb726d-a15a-356f-ad3f-f3eb1f580986 | -11.42506 | -46.11446 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 3f81601e-63df-31ec-9d22-1159e7b732f3 | -11.06231 | -50.35858 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf07b279-c34c-395b-95da-e49acf1d67be | -11.78018 | -45.32626 | 2025-10-27 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 99706a65-f234-3889-9718-5b2ebee9393f | -17.2755 | -45.31315 | 2025-10-27 04:34:00 | NOAA-21 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a146c644-e299-3569-9f61-543283fd2ad0 | -14.6289 | -48.37519 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f6bb61a-ddfa-3cff-a2aa-6d1d512d1f33 | -13.28529 | -54.40062 | 2025-10-27 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1d52ece4-c027-3dab-aeca-eb689dc12eed | -10.42096 | -47.64553 | 2025-10-27 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3197ea3c-10b3-3462-84a1-3b923fc26136 | -10.90686 | -48.02273 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a2033460-0c19-3bf9-9c5c-de8b3175054c | -12.90746 | -48.5877 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1f8e4101-6ab5-32c6-a405-76b4580006a0 | -11.66936 | -41.32231 | 2025-10-27 04:34:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 525068fd-d11f-32e4-80df-a1424b253158 | -11.24684 | -49.86641 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 169385dd-d057-3f71-98bb-da229370f736 | -14.63214 | -49.39704 | 2025-10-27 04:34:00 | NOAA-21 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 04f8927f-d8b5-3b42-a43c-20cb15e5fd03 | -13.55245 | -49.55671 | 2025-10-27 04:34:00 | NOAA-21 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9899fc14-f90b-3d1b-9824-f5bf7ceec8de | -12.32813 | -47.47753 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 4323afac-ae8d-34e7-8df8-81a694bc6d27 | -12.35748 | -48.117 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c81ea7cb-0f5e-32d5-b616-0c014821613c | -11.03199 | -47.87254 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a24fe59f-f373-3926-8c20-1297b468f070 | -17.64689 | -43.05335 | 2025-10-27 04:34:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aa27c4b2-3cc1-312f-9ab6-8cf850dce452 | -11.16366 | -47.79068 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 033fd9aa-b45b-3b8f-84bd-3ed1f6eece36 | -10.62645 | -48.01133 | 2025-10-27 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6bceca2d-7820-32c3-bb78-e08d6fb8c214 | -13.77859 | -44.09176 | 2025-10-27 04:34:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 68bef9f7-7098-34c0-abdc-44c2f35c82d8 | -12.30731 | -47.47786 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6be39737-c0bb-3fe2-a61d-7c5406268e2c | -11.04814 | -49.89645 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8a07b56-50f1-3de4-9797-541b860268d7 | -13.2425 | -47.99413 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 2a971fa9-0796-3c61-a3b1-69cebc0c84dd | -17.41261 | -46.88735 | 2025-10-27 04:34:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3255ac7a-c8d4-3c72-8604-bf9504d6797a | -10.32597 | -47.15211 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e08e834-c1de-3e4b-a586-5c7833f702e0 | -12.33602 | -47.471 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5bc7296a-d352-31df-a781-a3639e05f044 | -13.00657 | -48.67212 | 2025-10-27 04:34:00 | NOAA-21 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c3a39b8a-891a-3aac-a657-eb9b0e2ee53f | -10.31603 | -47.19505 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b641e541-2771-3f9c-8de9-a4f2077fcf60 | -14.62503 | -48.40079 | 2025-10-27 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 078f74a9-6037-300a-abdb-887b44d6d12f | -12.85539 | -48.6376 | 2025-10-27 04:34:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 596141d7-fa22-378a-94d4-6fc7f7b061e5 | -11.83645 | -49.86118 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8b9b60a9-1a57-30e8-a116-1b5cdb6161aa | -12.23182 | -46.52764 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 278bcd89-8f78-32cc-ab1f-73793ebef255 | -10.3586 | -47.18685 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9e88daab-50f1-3414-8d28-f5a675b27d8e | -11.43036 | -46.1277 | 2025-10-27 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6c137789-1b29-3fd7-9971-9253f5133a43 | -11.62753 | -54.57843 | 2025-10-27 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3cfcc794-8742-3c27-8472-da4638a4507f | -10.34961 | -47.17805 | 2025-10-27 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 92b870a0-0173-3497-b74f-2ec6b5c53a5c | -13.54179 | -47.16237 | 2025-10-27 04:34:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b1672b57-381d-33f9-86c6-b440153c173b | -12.22971 | -46.52618 | 2025-10-27 04:34:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 114f4010-7a87-34fa-8e4b-7c86534c532b | -12.89527 | -54.72919 | 2025-10-27 04:34:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 375c9557-a70b-3f28-813e-016db087916b | -13.23798 | -47.97857 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 618bbccf-cc43-3ed6-b5c3-3ecf88e626be | -14.8283 | -52.42451 | 2025-10-27 04:34:00 | NOAA-21 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| fa592cbc-383c-35e6-b8c1-2242a259083a | -13.2631 | -47.97146 | 2025-10-27 04:34:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d1ff3a6-efeb-3a2b-b91a-40510133bae1 | -16.30217 | -44.9633 | 2025-10-27 04:34:00 | NOAA-21 | ICARAÍ DE MINAS | MINAS GERAIS | Brasil | 3130051 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37e9dc45-0e62-3844-a8ad-1893d32f8d14 | -12.33712 | -47.46368 | 2025-10-27 04:34:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4dfec1a8-11f2-322f-9af9-084172418d19 | -11.64495 | -45.23211 | 2025-10-27 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f91f495d-1f8c-3706-be7b-d3b7288d05b8 | -11.02851 | -47.80653 | 2025-10-27 04:34:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 83f5c4fb-bd85-3ff5-af48-5e48db9e4153 | -10.91272 | -49.82626 | 2025-10-27 04:34:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1ff25ef-c30b-3a07-93e9-e8447cc61e31 | -13.60408 | -47.59317 | 2025-10-27 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a6be87b-511b-3721-8792-9ebcf788894f | -14.3694 | -51.52929 | 2025-10-27 04:34:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README51.md)
