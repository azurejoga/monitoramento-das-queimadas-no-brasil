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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7117c365-1bec-3983-8c8d-c32baafd085b | -10.8569 | -48.64611 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f3f0f1d5-01f9-3c72-92af-b2f66247bb3c | -10.52549 | -47.74822 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b5b2e180-332b-32ee-92d9-23590fa27e93 | -13.57756 | -49.59909 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 43f14d66-9c5a-3ccd-bf97-b841d7161316 | -10.86319 | -50.1016 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5060ca81-f032-3118-bd5a-3811c870a331 | -13.78858 | -52.78801 | 2025-10-29 04:46:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f297d86f-43c6-3698-834f-d373aba18848 | -10.85522 | -47.89795 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 639b2738-3094-32dc-a07c-2996b749d206 | -13.69995 | -47.67516 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dd6e5514-0e79-3af1-9ec8-aeebb9cb53d7 | -14.54734 | -49.26491 | 2025-10-29 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3907d35-3593-33bd-90fb-1c75381e40e3 | -14.26 | -48.1116 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 21.5 |
| f1b1a838-9f16-3052-ad0e-b28a93cb3e3d | -11.41043 | -51.38669 | 2025-10-29 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a20e2018-4657-3b5f-a425-c6cb2918debd | -13.67048 | -47.18223 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d8c89af6-614a-3bad-abd3-093e18dc0cba | -13.61484 | -47.59815 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7923a903-cfa6-38d4-b9fa-700d4ec880cf | -10.50788 | -47.73592 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b750adbd-a74a-3bca-9141-d6bc4bd8d30c | -12.41328 | -44.70779 | 2025-10-29 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 96ef48d5-7c0b-38d6-a57d-a24d9d7ffee5 | -12.08052 | -47.9964 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 86054e35-ec7d-381b-a6ce-d12e556138f0 | -11.036 | -47.85056 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 942a9fe5-b1b5-3e02-b7ca-356eb30a9e76 | -10.42665 | -45.05132 | 2025-10-29 04:46:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a66e13d8-5ea5-33d2-8e00-fb5b17c96858 | -13.66138 | -48.443 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 3d1c027b-5b03-3834-a068-3f5dfb2d8d91 | -15.18235 | -47.23996 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 991ad221-d9e4-3d04-bdc4-aaafecfd7c06 | -13.60669 | -46.49636 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a3dce25-e5f3-3253-b750-3b91f2fec5d4 | -13.24788 | -44.11372 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0a230a13-8f30-339d-8d2a-1c63027b3d8c | -8.72003 | -50.01327 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbd65db9-ddd2-3d46-b664-a839966375de | -13.24711 | -48.00858 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c3988b25-e642-3922-a27b-7b8d74c22001 | -10.86869 | -46.04569 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 653c0c76-784b-344c-88fc-f97be6cbf07f | -12.70279 | -46.30743 | 2025-10-29 04:46:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| d15ac514-f101-3457-9aba-37fa5c63f627 | -13.5406 | -47.13776 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| bdf25dbc-d3a0-34a0-af1b-5e0c320292a9 | -13.23134 | -47.06495 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3a1628cd-6fa9-30b8-930c-90e1feec6f47 | -9.57069 | -44.71285 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2206605 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e5637ec-0893-3b23-8dfe-8f4a143bea2d | -13.53592 | -47.35161 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| f1d1f1dc-679d-36f6-9643-9f47a02ce44a | -9.80537 | -47.75992 | 2025-10-29 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6bffa5ad-dea1-3454-93c9-6125206fbf72 | -13.53706 | -47.13304 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 6283f744-f784-3f2f-87c3-de6d77aa9974 | -13.8633 | -48.48848 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f11c1c98-99ab-3880-825c-7e3699c87e80 | -13.43368 | -47.37303 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5adc98d8-a5f9-3b7e-a5b4-e1b21ce7d679 | -14.26976 | -47.32109 | 2025-10-29 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4e89f394-e118-31f0-9fce-97615d5eb6b5 | -10.976 | -50.11853 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d3659b30-9b8d-3dbe-93db-95edf41c18a7 | -10.65768 | -47.90248 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9e1c7005-5dec-3b19-ae9d-0c9bd42b2066 | -12.15826 | -47.69925 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3babbec-d104-30a4-8a13-007c0283ac31 | -13.0439 | -48.46743 | 2025-10-29 04:46:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fdd4cdce-3bee-396b-bec5-afc60110e093 | -10.52807 | -50.00209 | 2025-10-29 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ec039b31-f94f-3ac3-bbbc-60f01e25c21b | -10.57296 | -49.75435 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 46fc101a-6699-33ad-a5da-b48448dec19b | -10.88355 | -47.99645 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 284be87f-6252-38e5-a6be-b87d0f146ecf | -11.33949 | -41.67558 | 2025-10-29 04:46:00 | NOAA-20 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| bd71a1ce-5900-3122-853f-50131b9ec524 | -13.60888 | -46.48005 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae06a573-9023-35f7-9d7a-f856010005b4 | -13.57022 | -47.15702 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 14336a6c-219b-340f-bd65-aa710a0928df | -14.00353 | -50.90606 | 2025-10-29 04:46:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d56e8e4c-7c5b-3d1e-a7ac-e84e82ccb477 | -10.52171 | -47.74757 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d9034e82-50c5-3ea7-bd9e-b607514f8cfd | -9.22805 | -46.34983 | 2025-10-29 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1a37ffe-e114-309f-8cf5-bc442e86730e | -10.64755 | -48.00032 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 065ae006-535f-3ea4-9d95-0d2528944062 | -8.85978 | -49.06659 | 2025-10-29 04:46:00 | NOAA-20 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 630c8952-871b-3bcc-abc0-531de8a4da4a | -10.77337 | -45.11182 | 2025-10-29 04:46:00 | NOAA-20 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bcb9b72-c7d1-358f-8c53-739796ecf16f | -13.66727 | -47.17493 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d2b054ea-4b75-3e86-b506-36c296c37453 | -13.93846 | -48.44649 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e73660ca-5a47-368a-97b8-a29adf37b749 | -14.76052 | -49.67671 | 2025-10-29 04:46:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e8228451-060b-3891-873e-49064138b1f6 | -10.60601 | -49.6209 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e5f7a43-da2c-348a-adde-29276ca491ec | -13.24826 | -44.11071 | 2025-10-29 04:46:00 | NOAA-20 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7bcada48-8be7-338c-8419-943f551acbd1 | -14.23189 | -48.1133 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7014c58e-483b-3d15-ad28-da46c007c480 | -14.61782 | -48.41611 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3cda0c2-f951-3329-a84e-78a189c86660 | -13.64253 | -46.52225 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 56063761-c42b-30d4-b99a-f9ab91b61bdc | -13.30243 | -47.69421 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68def934-d37a-3b14-a70c-9f4ea8faccf2 | -15.21091 | -47.21706 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 463a7d1a-7956-3a6a-9a77-dc9a4d1a3083 | -13.57098 | -49.59421 | 2025-10-29 04:46:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1560a954-3ba0-3518-895c-63bc3bc27f6d | -13.86257 | -48.49368 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02e8a3cc-8775-3814-8e2f-e1652e28bb74 | -12.36906 | -50.15997 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d69de31c-854e-30cd-b804-a06bc1c0e751 | -13.59915 | -48.42136 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ea86b80c-a82f-39e8-b982-8e5dd11a881e | -11.25914 | -45.52486 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 80c1be12-83cc-377f-888a-ad02d9605a8a | -13.37282 | -47.39036 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 51ace229-90d7-30ce-8f47-9ea2d3a5caec | -15.31687 | -47.85495 | 2025-10-29 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0d571a9-647f-3a0e-8677-29740f26b7b6 | -10.8666 | -50.10213 | 2025-10-29 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b46dcbe6-3733-3f83-90f7-79a3fef4253a | -11.41486 | -51.40189 | 2025-10-29 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd40ac34-3950-30bb-a585-8311e6b989d0 | -11.268 | -45.52614 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8f8e6905-f1f7-38cb-bdb9-94616a56179f | -13.69181 | -47.68844 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 36db2cdf-97f5-3738-b146-764d016143f2 | -14.64822 | -48.39542 | 2025-10-29 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb42c78e-907a-30b8-9fff-45a9e35fc89e | -10.94355 | -48.03272 | 2025-10-29 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 614bc420-9d28-30eb-a815-b7fb305da354 | -10.86015 | -48.64367 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 540f417f-7d89-3bba-8078-77e4615b62de | -13.55147 | -47.17206 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 44c9a0cd-6ba6-3f4f-a641-e628fc2e332d | -14.48527 | -43.94405 | 2025-10-29 04:46:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d24a9a2f-d935-3831-bc3b-60440afcdbdd | -11.73504 | -49.33522 | 2025-10-29 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a3f79d29-d9c2-3d36-b1de-7f5495ea40cc | -10.32774 | -47.09937 | 2025-10-29 04:46:00 | NOAA-20 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f04e075-340d-37e8-a48a-27c2ec421b7a | -13.57515 | -49.59055 | 2025-10-29 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 12.5 |
| f6318c6b-2485-3730-ad7e-85a2b07ea100 | -13.56013 | -47.32545 | 2025-10-29 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 54c3cddc-e710-3dd7-92e8-83e074cf4944 | -13.26892 | -47.73311 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77db3dbd-f072-348d-9f70-a03abab63622 | -10.86794 | -44.41229 | 2025-10-29 04:46:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4a65421-7a3a-3bca-8dfd-0507dd7a6b48 | -13.91222 | -48.46776 | 2025-10-29 04:46:00 | NOAA-20 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| da99511f-d996-35b4-8754-6b74996eaa8a | -12.04749 | -47.82726 | 2025-10-29 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4a991656-2f00-39d7-946b-b7e6d0bb49c2 | -12.009 | -46.78278 | 2025-10-29 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| ba6712f1-5418-3379-88bb-f4830a60e4f8 | -13.6455 | -47.03546 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a6196065-851d-348c-bf25-37b62e327c21 | -10.85591 | -48.64719 | 2025-10-29 04:46:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f7e536b5-7f93-3c5a-ae63-f46699cdb8b5 | -11.27487 | -45.50907 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 04df0c2b-8c22-3384-a2bd-567006298470 | -15.63842 | -46.97039 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f05308c9-cab7-3806-9965-3e3aacfb8595 | -11.02901 | -47.84515 | 2025-10-29 04:46:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| fe5414ff-3812-3de3-aee5-111926068876 | -13.60943 | -46.47596 | 2025-10-29 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c2663c54-ad7e-3d9c-976a-a899876cba45 | -13.53241 | -47.13639 | 2025-10-29 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ac6e3f7c-9076-3b2d-9014-129b2c5b835d | -13.22108 | -47.07847 | 2025-10-29 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b77c6f0e-89d0-399e-b00d-176967fa517d | -12.61572 | -48.44344 | 2025-10-29 04:46:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f86910dc-447c-3757-a842-ba6fe67764ec | -12.53042 | -47.5533 | 2025-10-29 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b31d07ec-8fde-39da-ab31-1b5d8d8e31c9 | -10.51684 | -47.72768 | 2025-10-29 04:46:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d208b822-db2c-3bfc-a153-132f88ce9153 | -15.1633 | -47.22272 | 2025-10-29 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7064d879-806b-3f39-bcb5-7c57c1a726d0 | -14.76111 | -49.67263 | 2025-10-29 04:46:00 | NOAA-20 | GUARINOS | GOIÁS | Brasil | 5209457 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| e8a60c59-184d-3956-95f5-abe07f6a3b29 | -13.54737 | -47.17147 | 2025-10-29 04:46:00 | NOAA-20 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a15e8495-0375-35d1-8a1b-2f8cac365a28 | -13.65245 | -48.45131 | 2025-10-29 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README76.md)
