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

## Dados Diários - Página 98

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8fd3b15b-d26f-3584-bd13-fc6367fcd112 | -13.85701 | -48.57874 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5b2d6e2f-1dd9-3a57-a263-b963e78d968e | -14.2966 | -43.19296 | 2026-09-23 05:06:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 435af6d0-cb84-3975-a8a5-272435525474 | -14.65878 | -45.59011 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43bd4b7f-cf9f-3745-b0a8-567535f92430 | -14.6204 | -45.64548 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c8a46361-5a60-3aab-b71a-91ed8e01977a | -12.31998 | -50.15244 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2838d922-84e0-3cbf-86ec-9ba6d53d8576 | -12.53942 | -50.06712 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0cf504be-6bb1-39a9-8ce8-703e2b527484 | -13.92074 | -47.83224 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 4df6313d-4df0-3a36-9493-7da1e82273e4 | -14.63059 | -45.64987 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f1210156-bc72-339a-818b-ce6cc35ab9f5 | -13.2965 | -47.8913 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 86f9b1d1-0e1b-36f3-bed8-664802db097e | -14.62846 | -45.6231 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8cdd09fd-f757-33fa-88c6-72ef24483ba8 | -12.80656 | -50.8564 | 2026-09-23 05:06:00 | NPP-375D | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dfe64756-157b-3e2f-96bf-9b625f1730eb | -12.51031 | -49.97991 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ca0ffe89-c79a-3b43-9b35-66e687d32e1d | -14.62984 | -45.65633 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cdb6358a-90dd-3f2f-b336-9afe24271f7e | -14.65838 | -45.59342 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6b1a1051-7016-3ac7-ab7a-a1c9cb677f38 | -14.96879 | -47.53495 | 2026-09-23 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0ac8befa-7cdd-3e7c-a240-347be5311998 | -13.45317 | -46.25946 | 2026-09-23 05:06:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| aee5acf9-01d6-39bc-8203-cfb1943fb20e | -14.69535 | -45.59481 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.3 |
| be9a6c7b-c86a-31e2-ae3a-458a95319683 | -13.92311 | -47.83454 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 21416d5b-7928-30bf-a811-929fa88867b5 | -13.02446 | -48.64391 | 2026-09-23 05:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6d52bb82-c90a-3b64-8f45-54da4b3f129e | -14.62946 | -45.65954 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5ae8dfdb-3a7c-36dd-a5d1-b17f0de08907 | -12.45412 | -48.23819 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6a56871c-6651-384e-906b-e1effd258983 | -9.33393 | -65.72744 | 2026-09-23 05:06:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9c7d898d-0f1f-3a47-bf30-77652cd3826c | -12.10662 | -50.0337 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 722ed9b0-1236-38db-b446-9224bc148115 | -10.86439 | -57.16879 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a254a49c-2e75-390d-9695-fb77b62dde60 | -14.61038 | -45.64098 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c083b020-64a5-3b31-96c2-2043c24f9d7d | -13.30091 | -47.89174 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e2bfe778-3db2-38e2-ab6f-c2c4a7d92e09 | -15.62835 | -43.52462 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 19.6 |
| 6b1b2c42-24f7-3c86-968e-8b4f170d7383 | -11.98848 | -52.45882 | 2026-09-23 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 75c81148-a538-3efa-9052-7c150d48f063 | -14.71174 | -45.59093 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5bee459b-71b9-3356-a035-c13176db2421 | -15.62975 | -43.52627 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 45e10781-999d-3f6f-9a28-dd339adafab7 | -10.6553 | -58.76033 | 2026-09-23 05:06:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed94291e-f588-302e-aaaf-077813d0d5cf | -12.70505 | -47.01345 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 723f6be3-7e9b-3dfd-abb9-e63aab534431 | -14.75489 | -47.15746 | 2026-09-23 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 874b779f-f831-3864-82b4-166ead37a4e1 | -13.70879 | -48.79248 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea434b46-7bbd-37f9-a595-20c97ba2b80d | -10.87176 | -57.1701 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 077ed96d-5080-33d9-b31d-26af6b50a0e8 | -15.63627 | -43.52247 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 125469c4-871b-37ab-9fd4-6990c393bd1f | -14.60197 | -45.62333 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 793c3e43-a21b-3be9-8178-6ff8ea45ef7d | -13.92812 | -47.83075 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ae88373a-6184-33b6-9fea-503e9c4ed65a | -15.63531 | -43.53155 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 52424f26-6903-3cd1-9309-ce13488d38b4 | -13.18821 | -51.56178 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0cd6eb6-eaf5-316c-a90d-95eb8b934337 | -14.59074 | -45.62872 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 8dabbb3d-9d0f-326a-9bd9-0d2c8f59cdb0 | -14.59555 | -45.63259 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 61ecb588-43d2-36d6-a178-4fb1aa4e7ddf | -13.92368 | -47.83006 | 2026-09-23 05:06:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 78c986f1-6484-326d-aab0-9c036865c74a | -12.07225 | -50.08475 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4500da7d-ce84-3a66-983e-08c3ebb0f7a2 | -14.29677 | -43.19404 | 2026-09-23 05:06:00 | NPP-375D | PALMAS DE MONTE ALTO | BAHIA | Brasil | 2923407 | 29 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 552abec2-f072-363b-be67-4a7282053793 | -14.62 | -45.6487 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4ddea239-cf80-333f-9927-9827aea927e7 | -13.30147 | -47.8875 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 205dec21-e3a1-3562-a70f-fd1495591b6c | -14.96417 | -47.53449 | 2026-09-23 05:06:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e15005c5-24c4-3919-b931-efa97c7dccdd | -13.21853 | -47.02433 | 2026-09-23 05:06:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a98ba776-dca2-39ee-9d00-15bfbe7d53e9 | -13.85229 | -48.58189 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 67d18b9a-7202-3565-9d7b-924a77ffe664 | -14.62641 | -45.63964 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b2f80d04-01b0-3e67-bfc1-bd01fc078d9a | -14.62441 | -45.65576 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 44a805c6-b661-3737-9d91-93b1b6423fad | -14.16715 | -47.84517 | 2026-09-23 05:06:00 | NPP-375D | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b8d9b5ed-8613-333c-9e4a-cc4460ed8312 | -14.62909 | -45.66275 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2a42e47-c0f5-37ee-9460-6bbdce19255f | -15.6237 | -43.52552 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 86a0804e-f79a-38d9-8fba-d3e2622fecbd | -14.62652 | -45.6395 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 38943302-9c99-3208-82ba-0e26b3486105 | -14.61519 | -45.64483 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 65999b1f-8761-33ca-a93c-87dc4830c8c8 | -10.85481 | -57.15802 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ad3ec469-c6af-336a-be11-93fb4a948964 | -14.63521 | -45.65386 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 52b3a0ff-4b28-3229-9971-1e9591bc464e | -14.62576 | -45.646 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcf8a008-b4ea-3a40-9a24-3fac96777332 | -14.74494 | -48.44031 | 2026-09-23 05:06:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 272cf484-4f26-3c79-8828-054e8799fde5 | -12.41851 | -46.96605 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 18.0 |
| e8e244a8-25b0-341f-8bff-07fc39ed9362 | -13.22051 | -49.92072 | 2026-09-23 05:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 446cb3a8-4ef1-303b-b4c1-24a0a5a80653 | -14.634 | -45.66348 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b30d6602-812a-39fa-abec-c52426e17567 | -10.86807 | -57.16945 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 462744e6-0f8c-372c-b79c-f817b21f2be9 | -13.21513 | -49.92244 | 2026-09-23 05:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bc5169f-1ede-3604-8390-7e77e690e7f8 | -12.70965 | -47.01421 | 2026-09-23 05:06:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 93a91168-1ca3-3d3b-a948-9e80d5298d39 | -13.21666 | -49.92015 | 2026-09-23 05:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 168f9a7f-cb19-340e-bc19-72f14de26530 | -14.69458 | -45.60119 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6aa34127-cd04-301f-8a49-b7b1b14f86f7 | -14.63021 | -45.65311 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3da9106-8afb-315b-a015-dc05eb817d86 | -14.75551 | -47.15242 | 2026-09-23 05:06:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e6b740ae-75dc-3300-9b93-c5611d7d5bfc | -14.41375 | -42.1091 | 2026-09-23 05:06:00 | NPP-375D | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| d3b929e1-bb2a-3d9d-852a-24415958a120 | -14.62079 | -45.64228 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b322457f-66ec-3cb4-b9df-a5bbfac668cb | -15.63023 | -43.52173 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 80369e40-c1a2-3940-849d-3fe87bed4b44 | -14.60678 | -45.62727 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a916d089-d90a-394c-a6da-34c9824eaa8c | -14.61078 | -45.63776 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89c5ee31-ed43-3ce1-a2f6-afdc4554550f | -13.85756 | -48.57459 | 2026-09-23 05:06:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9bc054e-4d8f-3e8d-a7f0-d3c5f746262b | -14.62131 | -45.63891 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1cdf4588-6f20-355b-b31e-a8408544e1a6 | -14.69052 | -45.59085 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| e7fb5662-ab5d-3402-bb95-ee3779098561 | -14.62019 | -45.64856 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 732c0c7b-0720-3607-aa83-8d8a101592ac | -14.63097 | -45.64661 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4561b15c-9885-38c7-b9ec-c91e60639917 | -11.03247 | -57.2304 | 2026-09-23 05:06:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf8a57e-eb9a-362f-8abc-0a0c720deb5c | -14.60156 | -45.62666 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1e805dbf-7489-39a4-9456-c4b21f7c1009 | -13.29595 | -47.89553 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f5e7f112-48c4-394a-bff0-a8f153f4ba7e | -12.35389 | -50.23648 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 403b9a7e-e2f6-3816-92af-6ec843cae1e2 | -14.96462 | -46.41872 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 763431f0-bbcc-3094-a562-508369a08dca | -13.70927 | -48.78888 | 2026-09-23 05:06:00 | NPP-375D | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b7485bc-d7fe-3c52-8055-4a9134870ac8 | -13.21898 | -49.923 | 2026-09-23 05:06:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6723a364-0b17-38c0-8116-fe1a66631bbb | -14.59516 | -45.63581 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a2f6fe35-a1e0-316a-8cc2-cc15b344f162 | -14.62614 | -45.64276 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 4d631207-cc60-394a-af2c-36e844666ebf | -15.62886 | -43.52008 | 2026-09-23 05:06:00 | NPP-375D | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| b9c83ef9-09ce-31e0-994c-45dc8ae889bd | -14.6296 | -45.65642 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4499de97-990d-3b81-bdb4-94bee422d4d2 | -12.10594 | -50.0383 | 2026-09-23 05:06:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 391f5c4f-8e8d-3201-ac3f-6b3684b7132d | -11.99187 | -52.45936 | 2026-09-23 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d3e6a84e-6d43-31a6-9b0b-237b8838ae8a | -9.33899 | -65.72978 | 2026-09-23 05:06:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bb1e8a60-ed45-30bf-b4de-563e697e21dc | -13.30036 | -47.89594 | 2026-09-23 05:06:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 29d8631b-6a18-33c1-9cbf-7966dd07f55b | -13.18715 | -51.56424 | 2026-09-23 05:06:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 805348ad-fbfe-3892-853d-0d385d950cd8 | -13.05429 | -48.73317 | 2026-09-23 05:06:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 32793efe-58fe-3f5f-8c5b-025da4216ab3 | -14.63162 | -45.64018 | 2026-09-23 05:06:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0dabf825-9eef-3d81-9d71-1381678ad2b4 | -11.99132 | -52.46303 | 2026-09-23 05:06:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README99.md)
