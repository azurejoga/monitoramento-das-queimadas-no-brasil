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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f83834cf-3cd7-3a29-8bcb-90a0f5a1bd8f | -6.29747 | -42.54221 | 2025-11-13 12:16:00 | TERRA_M-T | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 34.9 |
| b194ab1b-8afd-3902-bc03-e44f87ced5c0 | -5.77637 | -42.8307 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 22cd7a5c-14cb-351b-8230-49b6ef0e1219 | -4.72071 | -41.89875 | 2025-11-13 12:16:00 | TERRA_M-T | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 30.2 |
| c9aca510-26ed-3218-b6ca-0e486291f089 | -6.88575 | -42.85824 | 2025-11-13 12:16:00 | TERRA_M-T | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 56.2 |
| 08dd91c3-567b-3cfa-a755-24d6f77707a1 | -0.78298 | -47.99739 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO JOÃO DA PONTA | PARÁ | Brasil | 1507466 | 15 | 33 | nan | nan | nan | Amazônia | 53.0 |
| 5bf517da-7240-351d-835a-ac83818fd0ad | -7.73024 | -47.18295 | 2025-11-13 12:16:00 | TERRA_M-T | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| d8eb40de-1311-3903-8637-087256f71464 | -4.78547 | -44.40377 | 2025-11-13 12:16:00 | TERRA_M-T | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a78a053e-b182-3796-8abe-ddd25c06fd7d | -2.50815 | -47.16916 | 2025-11-13 12:16:00 | TERRA_M-T | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 3feec308-1868-3511-9fd4-44e8f2a64767 | -7.22642 | -44.72753 | 2025-11-13 12:16:00 | TERRA_M-T | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 9f2c2982-9172-3508-b848-57bc5d2b98b3 | -7.49019 | -46.06848 | 2025-11-13 12:16:00 | TERRA_M-T | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 9104436b-8f43-3dba-a3ba-aad0ab3627dd | -3.44562 | -45.57991 | 2025-11-13 12:16:00 | TERRA_M-T | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 955b9a91-606a-317e-93f1-761922d508cd | -3.43443 | -44.6911 | 2025-11-13 12:16:00 | TERRA_M-T | ARARI | MARANHÃO | Brasil | 2101004 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 55a4920b-74da-3729-91a2-1cd0094ba9ae | -4.25689 | -43.78905 | 2025-11-13 12:16:00 | TERRA_M-T | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| f279a874-4272-36f6-b165-f0b06a449865 | -10.2755 | -46.83777 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 15.7 |
| efec2f7a-8d6f-3d43-a5fd-3b040b022e9d | -16.1375 | -48.22438 | 2025-11-13 12:18:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 8.5 |
| d9bcbec8-00eb-302d-921e-7e5c805fce8d | -15.16742 | -51.26933 | 2025-11-13 12:18:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| c3b61e67-6296-3f29-ab55-badeebb2c6db | -15.89117 | -52.818 | 2025-11-13 12:18:00 | TERRA_M-T | PONTAL DO ARAGUAIA | MATO GROSSO | Brasil | 5106653 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b23a457d-a262-35e4-8c97-3f6f3c308d32 | -10.26627 | -46.83647 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 5dc26c84-8be4-33a1-ac94-9fc801f15ec1 | -9.64859 | -44.54948 | 2025-11-13 12:18:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 11.8 |
| cf7bd8c2-3c00-360e-958a-631f34d450a2 | -10.6167 | -42.3205 | 2025-11-13 12:18:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 122.0 |
| 6df0dbf1-5dc4-33e4-a107-de40ddd5adac | -9.48525 | -47.88334 | 2025-11-13 12:18:00 | TERRA_M-T | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 65d71128-2c82-3d04-9755-5490a503f3c1 | -9.01952 | -45.45303 | 2025-11-13 12:18:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 8be72576-ba4e-32e8-aa1b-d7a4cb8a7de8 | -9.35228 | -46.59372 | 2025-11-13 12:18:00 | TERRA_M-T | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 44.6 |
| d1b961b8-17f5-3507-90cb-b52448c9ccd8 | -16.45364 | -44.99384 | 2025-11-13 12:18:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 4b078b4e-577e-3a46-8692-d53b860edc81 | -10.60628 | -42.2987 | 2025-11-13 12:18:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 67.4 |
| 40569cd3-233c-3a58-82aa-a7791beec0b5 | -15.8053 | -47.95993 | 2025-11-13 12:18:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 847a8283-5e3d-3c11-98c2-b9fab08bbc9e | -10.26761 | -46.82664 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 6b976010-d1bb-348c-bb89-4bdd44bfdd6a | -12.06694 | -48.20801 | 2025-11-13 12:18:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 21.6 |
| fe5d9d78-c015-3fb3-a4da-7736cd51180a | -14.59273 | -46.71608 | 2025-11-13 12:18:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 498c80d1-0663-3e43-8703-61092efc93d8 | -8.56129 | -46.04232 | 2025-11-13 12:18:00 | TERRA_M-T | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 4e1f527f-d90e-3db5-bd21-6a5da71d1f86 | -15.5467 | -43.18056 | 2025-11-13 12:18:00 | TERRA_M-T | PAI PEDRO | MINAS GERAIS | Brasil | 3146552 | 31 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 2129ae32-99c7-39d6-b73e-c3123e6a27df | -18.09205 | -48.80542 | 2025-11-13 12:18:00 | TERRA_M-T | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 8.9 |
| 3150e9a9-131e-31a7-a225-e32a803a6ae2 | -14.41683 | -43.26299 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 22.8 |
| 80a06c6b-b264-3e5b-b0c4-42092c7c71a1 | -9.64395 | -44.54245 | 2025-11-13 12:18:00 | TERRA_M-T | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ed15bb9c-bdf4-357a-834e-aa711db10e81 | -9.02937 | -45.45426 | 2025-11-13 12:18:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.4 |
| e3a54d99-f31f-3cb6-8c7c-9e6c7d643d2a | -12.44106 | -47.90756 | 2025-11-13 12:18:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 7ff84cdb-334c-30c7-8e54-b73133fc1ffe | -10.63135 | -45.00753 | 2025-11-13 12:18:00 | TERRA_M-T | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 18.2 |
| a57a5016-1e54-3807-99bd-29c06070bd96 | -14.71829 | -43.59675 | 2025-11-13 12:18:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 41.2 |
| 2cec2a82-986f-363d-8dfe-1bc1c257d190 | -14.48261 | -47.10267 | 2025-11-13 12:18:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 33.5 |
| 93544b7c-92c2-30f9-b4a7-704e8f4dd4f8 | -10.5276 | -46.18914 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 488cfca5-07d7-30f0-91b5-5205b1fb5d22 | -12.41785 | -45.78597 | 2025-11-13 12:18:00 | TERRA_M-T | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 33076263-9d30-3315-8b09-f603551639dd | -14.48402 | -47.09197 | 2025-11-13 12:18:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 38bba064-1cc7-3297-b0ca-cfbe26e3a112 | -9.02104 | -45.44181 | 2025-11-13 12:18:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 17.7 |
| b3c3f2df-af60-3fc2-8c9d-0205cc042339 | -10.27684 | -46.82797 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a8f2da04-529d-3cae-af3b-a78248b46da4 | -14.7158 | -43.59 | 2025-11-13 12:18:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 6f872955-e553-3bcd-8655-40b7a55dde8d | -12.06823 | -48.19886 | 2025-11-13 12:18:00 | TERRA_M-T | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 8a6d287d-9274-34ac-a1ac-37675a302f59 | -14.09258 | -43.45393 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 25.1 |
| 24aaf9fa-5b84-3626-9833-addd036b7839 | -10.31738 | -44.59809 | 2025-11-13 12:18:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 36.0 |
| 2cee9f12-0540-3307-92aa-6055a02df9fd | -14.40044 | -43.18074 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 36.9 |
| 954dce2a-6402-3e5e-86f5-1168fd459fa6 | -8.9442 | -49.96032 | 2025-11-13 12:18:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2f577e7b-5a7b-3206-af07-1344c2f69434 | -10.80038 | -47.9057 | 2025-11-13 12:18:00 | TERRA_M-T | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| f3ce10bc-6a12-3993-87d2-01e0ba12a302 | -15.35511 | -51.3111 | 2025-11-13 12:18:00 | TERRA_M-T | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 164a2efe-af49-36df-a1ec-cb4ac8b46d11 | -16.45219 | -44.9994 | 2025-11-13 12:18:00 | TERRA_M-T | UBAÍ | MINAS GERAIS | Brasil | 3170008 | 31 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 8d4cd664-ba8a-3d5c-ad83-f5c7af6b74da | -15.56233 | -46.48773 | 2025-11-13 12:18:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 16.2 |
| bd412df8-82dd-38dd-be09-3bdc89534dd7 | -10.61918 | -42.30028 | 2025-11-13 12:18:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 84.2 |
| 0ce8a2ea-4815-32ba-94d3-c9767298e87c | -8.94281 | -49.96971 | 2025-11-13 12:18:00 | TERRA_M-T | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.4 |
| a7c2b0aa-7601-3cd2-a8a6-9a51c9a7fdf7 | -10.31564 | -44.6115 | 2025-11-13 12:18:00 | TERRA_M-T | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 46.2 |
| 198a806e-9e2f-39c8-ba47-7114f2a9b9ee | -8.51134 | -44.7408 | 2025-11-13 12:18:00 | TERRA_M-T | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 3e0ca2dc-5bf9-36b9-ac78-9a6c4351ba66 | -14.71353 | -43.60877 | 2025-11-13 12:18:00 | TERRA_M-T | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 18.1 |
| e5b24355-c2b4-3d85-988f-a3e0a50f6e50 | -15.42462 | -52.18938 | 2025-11-13 12:18:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9efe8ff9-7785-3536-b7b0-d50cd9b0b495 | -8.50975 | -44.753 | 2025-11-13 12:18:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| cc751de0-73ad-3f5a-bc74-6295d5082286 | -12.36455 | -47.65899 | 2025-11-13 12:18:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 82556ce3-764b-3f6c-a714-95b33de7cc64 | -9.03091 | -45.44294 | 2025-11-13 12:18:00 | TERRA_M-T | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 21.2 |
| 8d0fc826-5763-36cc-a606-67f73eb8f05c | -8.51263 | -44.74686 | 2025-11-13 12:18:00 | TERRA_M-T | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 28.2 |
| b4c5b287-b516-34ac-8fdd-995d00eaa077 | -11.00592 | -45.27222 | 2025-11-13 12:18:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| c9fdde59-2e8b-31bd-a80b-2c84f63704a8 | -9.38066 | -40.23591 | 2025-11-13 12:18:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 64.0 |
| 429b60e1-a145-3d8c-a1b1-b735d005efdc | -15.17645 | -51.27073 | 2025-11-13 12:18:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 28410c9c-ae4f-3ff7-976b-dc5e083a77eb | -14.40064 | -43.17419 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 37.2 |
| e39fe4a6-6a1a-3fd3-b798-c87e2bdda806 | -13.63759 | -43.01466 | 2025-11-13 12:18:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 25.2 |
| d46ee578-d9dc-39d1-be23-78b11275cb2d | -14.47448 | -47.09066 | 2025-11-13 12:18:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 10173036-f98f-3150-afbb-c51ef6f55f88 | -11.59595 | -45.11179 | 2025-11-13 12:18:00 | TERRA_M-T | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| f759e475-7161-3b99-8358-57e7b28923ae | -13.63979 | -42.9959 | 2025-11-13 12:18:00 | TERRA_M-T | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 12.8 |
| c4a1f011-a36f-361e-9f5f-c3bcfaf34533 | -14.47308 | -47.10135 | 2025-11-13 12:18:00 | TERRA_M-T | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 18.1 |
| 99c103d7-479f-32ca-9373-65d8bcec8a86 | -13.13108 | -43.79176 | 2025-11-13 12:18:00 | TERRA_M-T | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| fc841e34-1753-359e-8a6a-1bc1abe71100 | -11.00754 | -45.26008 | 2025-11-13 12:18:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f0309b5d-208c-3fd4-8c77-193261897192 | -14.09523 | -43.45998 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 037f5029-c5b6-3b25-93eb-f7acc3321ecb | -15.35655 | -51.30151 | 2025-11-13 12:18:00 | TERRA_M-T | BRITÂNIA | GOIÁS | Brasil | 5203807 | 52 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 8bb29f3b-2a02-3f97-9be5-1bf336f3a710 | -9.94822 | -44.93339 | 2025-11-13 12:18:00 | TERRA_M-T | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d857c1cf-a693-33dd-8ace-b089349abba6 | -10.529 | -46.17855 | 2025-11-13 12:18:00 | TERRA_M-T | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 5b27510b-2514-3d5b-a839-bf3601b742fb | -10.60382 | -42.31894 | 2025-11-13 12:18:00 | TERRA_M-T | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 155.7 |
| 151dd6e8-bf49-30cf-8ec6-a24dadeea8a0 | -11.05024 | -45.39598 | 2025-11-13 12:18:00 | TERRA_M-T | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.7 |
| a20682ca-b57c-3fd2-97db-5cfbd170c1b0 | -16.13615 | -48.23426 | 2025-11-13 12:18:00 | TERRA_M-T | SANTO ANTÔNIO DO DESCOBERTO | GOIÁS | Brasil | 5219753 | 52 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 2c84cb6e-6af5-327f-90fc-b5e2e12ddce3 | -10.33433 | -48.06834 | 2025-11-13 12:18:00 | TERRA_M-T | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 198742fa-44c9-3a35-8f99-234b4324fba3 | -18.23969 | -44.13335 | 2025-11-13 12:18:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 47.6 |
| 097180c8-e08e-324f-8908-b41243c97976 | -18.08338 | -48.80772 | 2025-11-13 12:18:00 | TERRA_M-T | ÁGUA LIMPA | GOIÁS | Brasil | 5200209 | 52 | 33 | nan | nan | nan | Mata Atlântica | 19.4 |
| 7018d8cd-844e-3469-9cdb-028082d664b8 | -9.44401 | -44.8743 | 2025-11-13 12:18:00 | TERRA_M-T | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| eba1b57d-2f58-3580-89fd-b838f3551cf9 | -9.38115 | -40.2308 | 2025-11-13 12:18:00 | TERRA_M-T | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 54.6 |
| 2fea01cc-e65b-316c-8d58-0ded9526598b | -22.67892 | -46.57904 | 2025-11-13 12:21:00 | TERRA_M-T | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| cb420b5e-6786-35e4-9d0c-0f97c4eb89e7 | -19.64279 | -40.27664 | 2025-11-13 12:21:00 | TERRA_M-T | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 58.2 |
| 4c1befbe-ab5d-35dd-aacd-b855eb6d22b2 | -21.12691 | -44.24421 | 2025-11-13 12:21:00 | TERRA_M-T | SÃO JOÃO DEL REI | MINAS GERAIS | Brasil | 3162500 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| 101d9696-e8c0-3284-9195-0aae6a01deb4 | -19.85515 | -44.5909 | 2025-11-13 12:21:00 | TERRA_M-T | PARÁ DE MINAS | MINAS GERAIS | Brasil | 3147105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 0153f3d1-2ee1-39a5-91ac-2ef557030ebd | -22.46769 | -44.1874 | 2025-11-13 12:21:00 | TERRA_M-T | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 1ed1a474-04a4-35a5-9eb8-806c04976298 | -22.6798 | -46.58507 | 2025-11-13 12:21:00 | TERRA_M-T | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| cb33282a-f201-3bc4-87c0-05921bc6e839 | -22.46926 | -44.20347 | 2025-11-13 12:21:00 | TERRA_M-T | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 3a29c543-6542-3787-8d15-64fb0289309e | -31.21749 | -53.1382 | 2025-11-13 12:23:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 24.0 |
| b79cfead-61e8-3a89-a27f-d2c321cfc1cb | -29.82654 | -51.99682 | 2025-11-13 12:23:00 | TERRA_M-T | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 8.7 |
| f025cf10-87f2-3eef-8ac0-4fc333434748 | -31.21605 | -53.14849 | 2025-11-13 12:23:00 | TERRA_M-T | PIRATINI | RIO GRANDE DO SUL | Brasil | 4314605 | 43 | 33 | nan | nan | nan | Pampa | 26.7 |
| b17e8d1b-ab23-3b4b-9a9b-f1bb9f6f01d7 | -29.82514 | -52.00731 | 2025-11-13 12:23:00 | TERRA_M-T | GENERAL CÂMARA | RIO GRANDE DO SUL | Brasil | 4308805 | 43 | 33 | nan | nan | nan | Pampa | 24.9 |


