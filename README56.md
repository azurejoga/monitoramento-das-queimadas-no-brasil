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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d63cad49-8aa6-3d2a-94f1-056747d513da | -9.30491 | -46.7704 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 497b0fde-8dcd-341d-9809-3ea1c24ec60f | -11.14609 | -48.46218 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e639327-8c12-3ce7-ab24-22644adf6d83 | -9.08309 | -49.8102 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b59a3b61-4e8d-3ee1-92a3-e5262c1c0691 | -11.78849 | -50.57864 | 2025-09-11 04:23:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e92c9fc3-dc86-398e-9ffd-360c6517b485 | -13.59138 | -47.67347 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3dc2237-684f-3748-90d9-d0a28bdbfb22 | -13.64697 | -45.70096 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e9a710db-2b76-37e9-9e2e-b3ea6d0225fc | -15.22224 | -44.05232 | 2025-09-11 04:23:00 | NPP-375D | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 709c9564-47ef-3abe-92d4-89adab47786d | -12.52969 | -45.3357 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3922eeb-7f39-3583-b1af-025f687a0007 | -9.02555 | -49.76945 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 90f59c1b-7d3f-33c5-a091-2b7900cbc6d6 | -12.0736 | -50.99234 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52d4baa5-33d5-36c2-8ebc-faeed7687642 | -12.88799 | -47.97666 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 62809f0a-e6ed-3955-b064-9b1882908160 | -10.00349 | -51.71215 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cb22d5d1-767b-3ed5-8555-0a0f7cc77c6f | -9.12333 | -46.98261 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f294fe36-688a-3511-b13b-3494784fd9f4 | -14.57799 | -48.76208 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a767357-0718-3049-8ad3-1c1b47f1fd4e | -9.51974 | -54.63601 | 2025-09-11 04:23:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be1376d7-0937-3e89-aff6-0c617e6f9c27 | -12.00155 | -47.58891 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 49d3bca6-79f3-33e4-9c38-6cfa0251fdb7 | -13.8621 | -47.36205 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 2100ec7b-0d6c-3c6f-b605-86609d72eab0 | -13.03726 | -48.00723 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4549119d-d409-3e01-88ed-8f4e7fefb76a | -10.40685 | -50.52337 | 2025-09-11 04:23:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f120b3d6-718d-38c6-a5e8-162daf9cdc24 | -11.47786 | -49.24935 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7846b3a4-8adc-3de1-aed6-2af1bc43dfa3 | -13.26567 | -43.74329 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1a8179e9-6462-3731-9f66-fe8f318a4415 | -11.36063 | -46.54765 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 4469eaec-dfe0-3450-9f96-3ece9bb3f51a | -14.37105 | -47.29986 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 06318c01-a841-3009-b726-63eb8b405e35 | -11.36456 | -46.54461 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 18.3 |
| 7c47a444-7814-3384-a912-c8c515720cb8 | -9.0789 | -49.80622 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ef0777b-bd4b-386f-bc71-d4be5d398218 | -11.35515 | -46.50682 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 75b0b744-03b7-379f-9b77-b15e965c2cdf | -11.82585 | -46.77468 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c72a9347-80f6-3e18-a426-e85a9cdf0076 | -10.30968 | -48.80378 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| eee465e8-0987-3d66-bc46-6240ae7f5fc9 | -12.47555 | -47.48903 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 146655f5-399e-3c87-9f51-b0274c08e1c6 | -12.52914 | -45.33928 | 2025-09-11 04:23:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 792a8f94-68e7-3503-ae32-96dea94f84ca | -10.56886 | -52.02761 | 2025-09-11 04:23:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c91624ae-23e4-3b47-9a4f-a9af2abcb848 | -11.46183 | -43.60499 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| cef5989d-0c68-30c8-a3dd-6de519e8d180 | -12.56069 | -49.14691 | 2025-09-11 04:23:00 | NPP-375D | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c1e1551d-6466-390c-aaaf-b19ab0f61630 | -10.89965 | -47.76814 | 2025-09-11 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f397979b-ffa1-33b5-b566-a94bb645bbac | -11.64756 | -46.91086 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6ec7a447-7af7-3ae7-b321-29e6bf45caf3 | -12.9524 | -54.74226 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e49a7a4f-ee59-31b1-b3bf-02cc17d511ec | -8.07956 | -54.75095 | 2025-09-11 04:23:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| afe8923c-6b0c-314a-a4b6-851bbd2a6b45 | -11.1924 | -48.39824 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2c02155-0693-3c47-9eec-34acdfa20c28 | -13.26094 | -43.7751 | 2025-09-11 04:23:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f0d78670-525b-3843-9ccf-7587030ef243 | -14.81208 | -48.28416 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| cad92bcd-b28a-31fd-8ecb-7bd2c2db5349 | -10.65214 | -48.62995 | 2025-09-11 04:23:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 02dc8b49-9caf-30f8-ab6a-923eb6e21c3a | -9.07278 | -47.08178 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fd6bb503-f31c-31d6-b0a4-95ad7aa94445 | -11.96062 | -46.65378 | 2025-09-11 04:23:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 058bd753-494c-3fab-8830-8dc484e4b3f1 | -11.35843 | -46.52927 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b0f36b8a-54de-3ed9-bee2-0278372d86f7 | -12.60531 | -56.96917 | 2025-09-11 04:23:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b853a4ae-5c8c-3e90-87e5-9b707443b280 | -11.36121 | -46.54408 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 90f33a6c-127b-379e-b7c6-8e092153d92c | -10.55135 | -51.52008 | 2025-09-11 04:23:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9b1a0fdb-37d8-3c7c-9b4a-c41b734ce1d6 | -10.89557 | -47.77137 | 2025-09-11 04:23:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59611a5c-6d6b-30ec-8259-af66fb9d82c3 | -12.92751 | -54.7905 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 246c2b68-3c46-3e2f-a87a-bc151d987bbf | -10.30669 | -48.7993 | 2025-09-11 04:23:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 8bd144be-7ec8-32f3-9ba4-36ea54e62663 | -11.9901 | -47.59461 | 2025-09-11 04:23:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f6322ca-470f-3697-9527-69ce2c7512f3 | -14.56044 | -48.75169 | 2025-09-11 04:23:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8ea58c29-4b4a-394b-b299-c106ffaa83fd | -14.36597 | -47.31001 | 2025-09-11 04:23:00 | NPP-375D | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cb516a8a-7053-38d2-866a-21911c4424aa | -11.4852 | -49.25056 | 2025-09-11 04:23:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 354ebcc8-34cf-3b80-b958-e454ccc72aab | -9.98322 | -51.6996 | 2025-09-11 04:23:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e3dd6587-cdc4-32c1-8ec0-da7eb15dcdce | -11.47682 | -43.64666 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| df06ac67-c61c-3aac-835f-bdf7b587ab15 | -9.90116 | -49.92442 | 2025-09-11 04:23:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 28c17e36-5311-38dc-ab93-7fd345217854 | -11.48845 | -43.65149 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 58ac2294-db1f-3d8c-9d7b-58bd2c00b680 | -11.08619 | -51.33458 | 2025-09-11 04:23:00 | NPP-375D | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1a3d21bb-bbaf-3fd9-b3b3-b17153f89d2a | -13.65822 | -45.72811 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e17ec62-2afe-3913-8387-96c7fd41ce7b | -11.15347 | -52.03387 | 2025-09-11 04:23:00 | NPP-375D | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be7c326e-1c5e-3fd7-bcd3-ea41b2fc3c85 | -14.30094 | -45.03635 | 2025-09-11 04:23:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fbf0b956-f09a-33b9-99b7-38f9ec5a4247 | -12.55284 | -44.65773 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58573dae-7106-3bb3-8177-b26960811b5c | -9.6577 | -47.52439 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e560ccb4-b862-327c-aa8a-cfbce488925b | -9.10628 | -46.9615 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4f7cd478-b710-3134-a766-8969952a6f1d | -11.35565 | -46.5252 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b4da580f-df96-3186-80aa-69f1ade63a7c | -9.84273 | -47.78391 | 2025-09-11 04:23:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 1101bae5-5234-3c47-883e-e55afb22d25b | -14.91498 | -47.30604 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f8d130be-177b-388e-9f91-ba9625954a65 | -12.41385 | -44.72585 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 062eba67-fbbd-36fc-9c2b-7edf46c82103 | -9.08083 | -47.07548 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70f51cf8-2967-32ec-8347-3b02aa05518d | -11.10329 | -48.41261 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00fd00f4-682c-37ce-98f3-4f30701bdf47 | -11.03778 | -46.05201 | 2025-09-11 04:23:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 441d5dfe-c98a-3c23-9b4d-c2e2325a09ed | -12.974 | -48.02748 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b24380d-3c41-38e6-8aa9-0849f0dab55e | -13.5926 | -47.66606 | 2025-09-11 04:23:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fa5d7cb3-b081-3f45-bdfb-bf172c8fe898 | -12.84794 | -52.93652 | 2025-09-11 04:23:00 | NPP-375D | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2ff75659-d9e6-3aef-bcbc-2bd568e4f50f | -13.98443 | -48.23929 | 2025-09-11 04:23:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b6516580-6402-3746-9d6f-f2dbef083a0e | -10.1469 | -46.16429 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2d634a5-5a37-3d46-83d6-6df694f239d0 | -9.08528 | -47.09152 | 2025-09-11 04:23:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6dc08db1-767e-3e19-9b8d-06653a458c04 | -11.48088 | -43.64335 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 77f373eb-689c-3032-930b-edeb80cc9b4d | -12.95489 | -54.74333 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebc0957a-9e3c-3bfb-a409-cce138b4b77d | -11.77185 | -46.48012 | 2025-09-11 04:23:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a042ef4f-5302-39c2-a57c-1df52a9abaf0 | -10.74395 | -49.28327 | 2025-09-11 04:23:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 22d39d05-bef1-3404-9537-ef905b739319 | -9.71957 | -43.53304 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 71f38e33-400c-3e13-b909-64f9b61bbf16 | -10.13615 | -47.88702 | 2025-09-11 04:23:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 45e3092b-2af9-3c5d-9fe0-f9b686d65843 | -12.95804 | -46.73692 | 2025-09-11 04:23:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 1e9d6c84-abbf-3e24-8ed5-a8f186c3e8ea | -9.06019 | -46.96473 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| e6c1bd91-9bd5-3fe7-b1e4-31e1a1d73ef5 | -12.5534 | -44.65406 | 2025-09-11 04:23:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e538d593-f4fa-3adb-a852-f7d728de624f | -9.71842 | -43.51751 | 2025-09-11 04:23:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e7c1f1f-235c-393d-9006-d252e8fc6404 | -11.46241 | -43.60114 | 2025-09-11 04:23:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e12e91d3-2a8d-3ebf-b28e-f4dd24ea6745 | -11.79011 | -47.32281 | 2025-09-11 04:23:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 689645b5-15ff-35bc-8a6e-23554373f098 | -9.02249 | -49.76382 | 2025-09-11 04:23:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| b93fbf23-4728-3114-93d2-279c14294e50 | -9.94033 | -46.05877 | 2025-09-11 04:23:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c08e4a55-2b70-381f-b8e2-d58ca75d05ef | -11.09905 | -48.4162 | 2025-09-11 04:23:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9fbc953b-5e66-3edb-8d76-77c4c86c0f3d | -9.07725 | -46.96755 | 2025-09-11 04:23:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e4616c01-05db-3520-a159-d41f5e6d5e98 | -13.13592 | -54.91359 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 348b2bdb-bb1d-3ea6-9427-cd01b7841a82 | -12.94696 | -54.81089 | 2025-09-11 04:23:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b61ece93-f149-3d4c-83ca-523479bc1c4f | -12.86986 | -47.95856 | 2025-09-11 04:23:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| dc0b7f8d-e367-333d-8d94-b52f680b3032 | -11.63096 | -46.76804 | 2025-09-11 04:23:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1ef8f660-4671-3a08-8e5c-4ec712d78ca2 | -13.15351 | -45.28399 | 2025-09-11 04:23:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ed4d5f5-7d06-35c4-9c5c-b83c449d7636 | -13.34915 | -44.00083 | 2025-09-11 04:23:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README57.md)
