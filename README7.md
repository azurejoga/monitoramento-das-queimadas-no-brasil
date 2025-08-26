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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bf341a06-21e2-3212-b981-e0637fe7b14c | -4.95474 | -55.7981 | 2025-08-26 00:33:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 28.2 |
| 05c97460-81ed-3e32-97dc-23222e3ff97a | -3.43028 | -49.05046 | 2025-08-26 00:33:00 | TERRA_M-M | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 7a8c3c9d-9a82-35de-b033-f559b3266411 | -3.06807 | -40.07025 | 2025-08-26 00:33:00 | TERRA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 26.3 |
| 7cb0621c-8952-319e-b8ba-5cf986f0e69a | -3.25381 | -46.91629 | 2025-08-26 00:33:00 | TERRA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| 7d1597ed-5027-3cb4-8301-bb34c77ebd54 | -2.92381 | -53.69956 | 2025-08-26 00:33:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| d79e8f64-18cf-3bea-92d8-c05d0b46bf5b | -4.95803 | -55.82336 | 2025-08-26 00:33:00 | TERRA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 137.3 |
| a9d9ee09-5541-30eb-8814-62d102d06664 | -3.84135 | -47.49176 | 2025-08-26 00:33:00 | TERRA_M-M | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 25ffec45-7698-30ae-9900-c09c0ebf7eab | -15.1116 | -48.6436 | 2025-08-26 00:39:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 94d4c402-94af-3983-9e16-2a22401d735c | -11.5494 | -52.1455 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7d23a17d-f586-3880-83ab-d2056f87e1f5 | -13.5811 | -48.1884 | 2025-08-26 00:39:00 | METOP-B | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| d3f2745d-d83c-3731-86c2-4774d8b04a97 | -11.6263 | -46.383099 | 2025-08-26 00:39:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d4861ce-34e7-3a18-8c6a-45fe13098a9e | -17.384899 | -48.123501 | 2025-08-26 00:39:00 | METOP-B | URUTAÍ | GOIÁS | Brasil | 5221809 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 40023c0f-7155-3ae8-a044-1208822c7886 | -11.6214 | -46.404301 | 2025-08-26 00:39:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 987e2bfb-dd45-3c74-9458-191994965c7f | -11.5319 | -52.114799 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d93ad56f-ff6f-3891-ac6f-79b0cff40726 | -14.333 | -48.6334 | 2025-08-26 00:39:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 83800ad8-d4ee-3eb1-8f3a-688d8dd19116 | -11.5494 | -52.101799 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bca40388-bc1d-34dc-846e-5c6b5c40f843 | -11.1535 | -44.760201 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7101cce7-3cfd-33e5-b958-19999b4b64bf | -13.1638 | -45.271099 | 2025-08-26 00:39:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 64b966df-d89b-3990-8bc1-e61bc84b6f2b | -12.9422 | -46.323002 | 2025-08-26 00:39:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dee6c54e-af75-39bb-8076-2b27aa72a427 | -11.571 | -52.1054 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fab1c938-1362-3815-9c92-134271f25edc | -11.5533 | -52.118401 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 09d2add7-8761-339b-84a0-43135a7fd91d | -15.6543 | -52.716301 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 6f7ad68c-fa9d-341d-8a0e-a8e9c5865ea3 | -12.9279 | -46.307701 | 2025-08-26 00:39:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| b9370026-e9f4-360a-9430-05caa1bfc46b | -15.633 | -52.7136 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 610835da-0acc-394f-9270-4f3ec5182122 | -10.7316 | -47.040401 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3571e02e-8d84-3782-b785-976399a4f168 | -14.7744 | -49.165199 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 9c849e27-2864-32b4-b94e-6da098c1bf2e | -15.6313 | -52.7062 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb406a4-25b2-37c9-bb4c-869dcafe1802 | -12.4911 | -53.8195 | 2025-08-26 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9ed27bf9-f102-31f5-8e52-b75455b0bdc6 | -11.5377 | -52.139599 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 980e131e-4a5d-3243-9bb0-e17372f6d3b2 | -10.7509 | -47.0354 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 468bcfd3-6971-36a3-929d-c8d8dfe8da7b | -11.5357 | -52.131302 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4fa2abd0-2b19-3e76-b1e7-2fa1de04f02d | -11.5573 | -52.091099 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6ce8dfd2-6f5c-3c5c-9384-70fc9004829f | -10.8115 | -48.307098 | 2025-08-26 00:39:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 42cb88f3-a8b3-3aba-9830-5e17f56470b7 | -14.1227 | -53.971199 | 2025-08-26 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7493e156-1dc4-36d1-8cf1-731788db68d4 | -10.75 | -47.072498 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a8665d5a-9851-3f18-a5a6-138e35b4ff37 | -12.7476 | -48.120499 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 78455df1-bc02-3241-91f5-ccc8c3c78647 | -11.6166 | -46.3857 | 2025-08-26 00:39:00 | METOP-B | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| fc4eaab5-3d40-367e-83b8-a572cb71c84e | -11.5612 | -52.1077 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 3a642fea-932c-3dc0-a44e-cc5ad14dd4a3 | -11.3151 | -55.0979 | 2025-08-26 00:39:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ba3bd05a-5c26-355f-8b48-872469f7301c | -15.059 | -48.682201 | 2025-08-26 00:39:00 | METOP-B | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| f7839093-bd46-3178-b290-10330c3fa175 | -12.6679 | -47.8433 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6ebd15c0-e695-3991-9e15-0d0d11d93132 | -10.6167 | -54.876301 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 77543f68-98c3-3095-a388-360fb5a70f9b | -14.6375 | -49.071301 | 2025-08-26 00:39:00 | METOP-B | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 76913db0-ad32-328d-82a2-161a509483fc | -11.5475 | -52.093498 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f827c0cc-3d22-360f-95c7-99963799f62d | -14.4243 | -56.439301 | 2025-08-26 00:39:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8e6079b2-b9f3-3871-b5ec-0c7f9516dcba | -11.1278 | -44.741001 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f096bc74-6823-3d9d-beed-323d854ee898 | -10.6955 | -55.136398 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9a702c4e-867f-3b48-b2e4-df7d682e06a8 | -14.2939 | -60.347099 | 2025-08-26 00:39:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c81c10f9-f507-3873-9405-706d2aa265d1 | -13.4129 | -46.868198 | 2025-08-26 00:39:00 | METOP-B | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ab8a20a3-b8a1-3080-9735-ad359949aafb | -12.7219 | -48.141701 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6fadcd22-4f67-3f35-93e6-72013d6ab253 | -15.6462 | -52.726101 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 17642f15-ef5f-3046-9597-fa753b949278 | -11.5572 | -52.134899 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54634e1c-e5c3-3f54-bc03-a45d080c08c9 | -11.569 | -52.097099 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| db432198-dfa8-330f-887f-6259317d9cbf | -11.1309 | -44.713799 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| c2f5149a-2ec6-363a-b1fa-241ee0a8c232 | -11.5397 | -52.104099 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9151260a-e181-3e68-887a-bf284f21fd8c | -14.3037 | -60.3451 | 2025-08-26 00:39:00 | METOP-B | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 4361c380-871f-3251-b5c2-f80cb904cf95 | -12.7316 | -48.139099 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| d1fd0385-8b70-30d4-8f51-033dab10913f | -11.5631 | -52.116001 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 17bad2ae-462c-3583-b07d-32023f03cb63 | -14.7771 | -49.176201 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ade38484-93e8-3341-a0a5-d4493fc31295 | -15.6347 | -52.721001 | 2025-08-26 00:39:00 | METOP-B | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1b76e77c-ee2c-355f-a323-bcaf183f98ba | -10.8212 | -48.3046 | 2025-08-26 00:39:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| dd509099-3e35-36f7-8083-115d0b85f554 | -14.4487 | -56.4576 | 2025-08-26 00:39:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| aff2ad64-dff3-3269-adfa-e4414a3afc3d | -11.5475 | -52.137199 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 963d5569-20c0-34cb-8c0f-da6a64c5b416 | -11.4336 | -47.287899 | 2025-08-26 00:39:00 | METOP-B | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35469220-79e2-34e8-a2f2-5d59787ae468 | -11.0528 | -52.008099 | 2025-08-26 00:39:00 | METOP-B | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c50ff363-e01e-31ba-b818-7c499b8d6250 | -9.5547 | -48.773201 | 2025-08-26 00:39:00 | METOP-B | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6f9872dc-86ca-3f7e-a245-8685c56c380b | -13.4001 | -51.759499 | 2025-08-26 00:39:00 | METOP-B | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 866c33fd-3ffc-38e6-9517-a15f0447350a | -10.6069 | -54.878502 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| d2e60098-3252-3820-bd3c-ede0208157b3 | -12.735 | -48.152802 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d142073-646c-3ae0-a4f1-17b482c8228f | -10.8247 | -48.318802 | 2025-08-26 00:39:00 | METOP-B | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 35bc2cdb-6344-3de5-9717-c4d94835b896 | -11.5338 | -52.1231 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ce368ca1-783a-30f3-bdd1-811315360e7a | -10.7022 | -55.1203 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 18f0fa7b-5875-3181-9eda-9ad5538fa6b3 | -13.0112 | -56.886101 | 2025-08-26 00:39:00 | METOP-B | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| ab6da1c4-9492-337c-ac6b-0d79b0fd66e6 | -15.0201 | -48.151299 | 2025-08-26 00:39:00 | METOP-B | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 118d8834-aeb8-39c3-ae31-3175da624f2f | -10.6183 | -54.883301 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 572e7f42-695b-3dcf-91b0-5ae3c8eb45a6 | -12.7635 | -48.1017 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 83040a18-d23a-324d-bd7a-a45cb4090fb1 | -10.6223 | -54.580399 | 2025-08-26 00:39:00 | METOP-B | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6c1ec3d4-fdc2-35c1-a7d9-d34ca12f71e5 | -14.3233 | -48.636002 | 2025-08-26 00:39:00 | METOP-B | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| b043ca30-3684-3116-b3e9-494ead91a825 | -10.736 | -47.057701 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 26f10c5d-a1f4-30da-9609-c37c9862d9fd | -12.9375 | -46.305099 | 2025-08-26 00:39:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 03fb38e2-c8dc-348c-af04-996ee5ab6ecc | -13.4316 | -51.1465 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 1e01d8b9-ec9d-36db-830c-8b472a598b20 | -12.751 | -48.134102 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 074fda6a-1494-392d-9a79-8bc00f435fbf | -13.1597 | -45.294601 | 2025-08-26 00:39:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 505bd278-5a8e-317a-9dcb-761a458e62fc | -10.6971 | -55.143398 | 2025-08-26 00:39:00 | METOP-B | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| eb54006e-de6c-32a6-a8c9-b2f8cf257ec6 | -11.1438 | -44.762798 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 44abc743-5e38-336c-8914-63023cb7e82f | -14.7868 | -49.173599 | 2025-08-26 00:39:00 | METOP-B | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd0a0f52-c00a-3322-b141-4b82a4813de6 | -14.4471 | -56.4501 | 2025-08-26 00:39:00 | METOP-B | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7e87d842-b478-31db-968a-171aa33f13a9 | -12.7504 | -48.0905 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c6fb3e92-cb23-3c7e-b0d0-626f94b17b5b | -13.1487 | -45.252998 | 2025-08-26 00:39:00 | METOP-B | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2b670abc-66e7-3f4a-b9aa-e1ad9125e229 | -13.4413 | -51.144001 | 2025-08-26 00:39:00 | METOP-B | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a0720762-7eb0-3c2b-8081-915d1ff14117 | -11.5396 | -52.1479 | 2025-08-26 00:39:00 | METOP-B | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 0b4b786f-21fe-3748-be14-076ff74bdbeb | -12.4348 | -48.691799 | 2025-08-26 00:39:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 08da9f06-b960-3b1f-84e8-0d7df035e0ba | -12.7447 | -48.150299 | 2025-08-26 00:39:00 | METOP-B | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e87d6c69-5cfa-3f7d-8b74-00edf84db0aa | -10.7457 | -47.055199 | 2025-08-26 00:39:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| efa3bddd-6219-379b-a9d2-60d81309f58d | -14.1242 | -53.978298 | 2025-08-26 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 8143085e-3a55-3bba-8a43-3a94df9d0371 | -12.9325 | -46.3256 | 2025-08-26 00:39:00 | METOP-B | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 27dcb40c-3f51-3970-ad6b-ffdd148cff57 | -11.3069 | -55.107101 | 2025-08-26 00:39:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a6740386-2aa1-3ca9-b379-3a9866adb4cd | -14.1129 | -53.973499 | 2025-08-26 00:39:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 40e4371c-15fd-3cc5-a0d3-347e74e10e3f | -11.3084 | -55.114101 | 2025-08-26 00:39:00 | METOP-B | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| bee50a8f-5b56-36dd-936d-12ae8a6317d2 | -12.438 | -48.704498 | 2025-08-26 00:39:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README8.md)
