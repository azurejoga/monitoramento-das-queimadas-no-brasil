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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dcdfea18-e62d-3eda-87a4-a9087282492e | -11.22702 | -45.29655 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.8 |
| fdfc5fe4-2652-31e8-9eab-d77134378d28 | -14.90699 | -48.08685 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8de132b0-9dff-3b96-861e-bdf5ad99b922 | -11.43976 | -45.5757 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 24ed084e-d5ed-3eb1-8138-5778b0be929e | -14.20307 | -39.38638 | 2026-10-07 16:35:00 | NPP-375 | MARAÚ | BAHIA | Brasil | 2920700 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 7cab4507-e301-3274-9af3-4170f20fb1ee | -14.73482 | -52.2059 | 2026-10-07 16:35:00 | NPP-375 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f16035f6-0839-38bf-81e5-ad181c24d2c3 | -12.22379 | -44.71685 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 25.8 |
| e0e591c8-ea32-342b-9f88-a092a4a4acb4 | -12.04157 | -43.44045 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 647abeee-0cce-38bb-91ca-fbd6fa399f8b | -18.36834 | -42.07382 | 2026-10-07 16:35:00 | NPP-375 | SÃO JOSÉ DA SAFIRA | MINAS GERAIS | Brasil | 3163003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 256dbdeb-124e-3f84-8dae-5a3bbd2f3e77 | -12.99415 | -47.06499 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 6578c76a-b386-3e40-950e-b00cb94a5562 | -12.20267 | -48.41932 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 4446f808-b8d1-3196-8c78-cb8f144bcfed | -11.3749 | -43.2543 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f70928a2-e0a0-38be-8425-5079c0e350e1 | -10.94624 | -39.2789 | 2026-10-07 16:35:00 | NPP-375 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 64932942-dfa5-3dbf-a4be-a9d7de4457a7 | -12.44446 | -47.80503 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 94762100-fa7b-3121-998e-7c5122500e52 | -11.84581 | -47.37265 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 3201da0f-ba69-3c26-ab62-82bc0e0c7171 | -11.23154 | -44.02245 | 2026-10-07 16:35:00 | NPP-375 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 8fce9619-7f73-3a23-890b-8c72657dbc16 | -13.80687 | -39.90086 | 2026-10-07 16:35:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| d64c1104-a72b-3a81-9793-c6cee1bafd76 | -13.69286 | -49.10226 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 35.9 |
| a48e77ec-930e-3e29-9866-6c6a4f918fbc | -11.83855 | -47.37703 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 18.6 |
| 733afbef-b65d-38d6-8e74-b848f9aea9a6 | -13.21236 | -40.08603 | 2026-10-07 16:35:00 | NPP-375 | IRAJUBA | BAHIA | Brasil | 2914208 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| 73f05b8a-662f-37ae-ad76-4428d06448e3 | -13.44863 | -43.45497 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 15caafb8-91ae-3738-9ad2-d97fd600b594 | -11.61939 | -43.6358 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 6dd12983-c68e-3f89-9ad1-aaff2beaf06b | -13.69721 | -49.08886 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 6a18e275-6e9b-3ab7-9409-8de99bb750dc | -20.14526 | -42.43363 | 2026-10-07 16:35:00 | NPP-375 | RAUL SOARES | MINAS GERAIS | Brasil | 3154002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| ef79b8cb-9aff-3a85-951e-da051537848e | -12.14277 | -44.94862 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| a4e0109b-3b17-3913-8e55-974c69ed836d | -12.16921 | -44.75221 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 9b96bde1-d4e8-3566-8828-6d31251f9fcb | -12.18409 | -44.75774 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 490cf585-888a-3dd4-9550-335622ef6fd2 | -12.63036 | -40.7033 | 2026-10-07 16:35:00 | NPP-375 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 29ccebba-4403-3108-b5b8-c74fda68d6ab | -10.6825 | -41.21246 | 2026-10-07 16:35:00 | NPP-375 | OUROLÂNDIA | BAHIA | Brasil | 2923357 | 29 | 33 | nan | nan | nan | Caatinga | 8.7 |
| 8197b858-5167-37b9-b2be-c055bd1d5e76 | -11.7268 | -43.65484 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| b7b63c73-29c5-3b1e-b3f0-ba8796d46a51 | -14.22504 | -41.21897 | 2026-10-07 16:35:00 | NPP-375 | TANHAÇU | BAHIA | Brasil | 2931004 | 29 | 33 | nan | nan | nan | Caatinga | 3.8 |
| fb1609aa-1a63-3ea0-ab3a-d40ebbed6abf | -13.69165 | -49.09306 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| f6951303-847f-3fa6-890d-19694ab402cd | -11.72346 | -43.65536 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 2b98839c-d706-38e1-b4f2-8b222ba6bd3f | -12.31954 | -47.951 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 7075f798-fd10-37eb-a6ab-bcd78e142c19 | -11.8561 | -46.79443 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 68.4 |
| cf52dc24-68ac-34f4-8193-be10d9a5c9c9 | -12.38677 | -38.7841 | 2026-10-07 16:35:00 | NPP-375 | AMÉLIA RODRIGUES | BAHIA | Brasil | 2901106 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 139a705f-08a4-3a30-a6b2-db8da8f8542a | -11.62247 | -43.67884 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| c92710a5-e3d4-37f1-bfc4-9020bd1de501 | -11.83665 | -47.30791 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 4a699bf8-0f37-38cb-930a-ab7c0e523b1f | -14.41403 | -41.34069 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 52.4 |
| 55b9b891-5810-3b72-93b8-ad5ebc0549f9 | -10.65356 | -40.28676 | 2026-10-07 16:35:00 | NPP-375 | PINDOBAÇU | BAHIA | Brasil | 2924603 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 8dd067c0-7370-3d02-b110-2a2486caeea9 | -10.16733 | -36.3947 | 2026-10-07 16:35:00 | NPP-375 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| df2cb0c5-8ff0-301f-bbf6-4edb858d9562 | -19.01696 | -39.88092 | 2026-10-07 16:35:00 | NPP-375 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| eb3417ee-4e40-3779-bf14-5e9b10bb886d | -13.69559 | -49.11255 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 02fa1ea2-ff70-305b-be40-69f76140fef4 | -13.68488 | -49.09998 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 32.7 |
| 382f75a8-2b38-3b89-9237-56659ebdbd2c | -11.77982 | -46.77215 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 3b8f35d6-262b-3e5b-b8a2-200419cf1827 | -11.2312 | -45.27611 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 7bd06e41-9cbb-3cdc-a186-dbd491bfbe88 | -19.26335 | -40.22066 | 2026-10-07 16:35:00 | NPP-375 | RIO BANANAL | ESPÍRITO SANTO | Brasil | 3204351 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| a401988a-bd9b-34b0-82c8-950339e0a337 | -11.14993 | -40.30191 | 2026-10-07 16:35:00 | NPP-375 | CAÉM | BAHIA | Brasil | 2905107 | 29 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a34909e3-0386-374b-b4da-80a74b2fbcd1 | -12.22052 | -44.67841 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9558f998-36ea-3b72-ad58-fcb577d2d8b2 | -12.22547 | -44.72825 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 23.4 |
| df1ff0aa-db5a-3b5c-822f-97dab892b70b | -17.49741 | -39.88196 | 2026-10-07 16:35:00 | NPP-375 | TEIXEIRA DE FREITAS | BAHIA | Brasil | 2931350 | 29 | 33 | nan | nan | nan | Mata Atlântica | 29.4 |
| 3ccf01a0-0cb0-3232-a805-2d4a1fc98a68 | -19.13966 | -43.1151 | 2026-10-07 16:35:00 | NPP-375 | FERROS | MINAS GERAIS | Brasil | 3125903 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 6de73198-ba02-3778-8883-67b9040b6e40 | -18.38518 | -40.31817 | 2026-10-07 16:35:00 | NPP-375 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.8 |
| 02a82f43-3d44-3b2c-8f63-3d2df2ecc3c3 | -12.21249 | -44.66432 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 30.8 |
| a15e4783-ab6a-3d37-ad51-7070e572a79b | -13.70732 | -40.46933 | 2026-10-07 16:35:00 | NPP-375 | JEQUIÉ | BAHIA | Brasil | 2918001 | 29 | 33 | nan | nan | nan | Caatinga | 19.1 |
| 0cb32656-ea63-3533-a4c7-6899bd68c438 | -11.73456 | -43.66093 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 29.8 |
| 16b75f54-217b-3514-9079-60c5dde54c59 | -12.22146 | -44.70928 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 16.2 |
| 4b66d6ae-c976-3a4d-959f-7d85ea81e3c7 | -11.84716 | -43.56271 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 011e812c-879f-33f0-9861-f4f96b672f81 | -13.27089 | -44.00226 | 2026-10-07 16:35:00 | NPP-375 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 72d89a82-c8cc-3237-b92d-5c4517d28b64 | -11.83516 | -43.52828 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 132.4 |
| 285d14d8-6d03-3ed6-a2f1-32dcb2b5e2c3 | -12.2181 | -44.70218 | 2026-10-07 16:35:00 | NPP-375 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 2a6b249b-a01c-3b27-b9ec-538ce3d2cd4d | -11.44329 | -45.57516 | 2026-10-07 16:35:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| d183d5cc-a39a-38c4-b21c-e77d298eb333 | -11.85987 | -46.79385 | 2026-10-07 16:35:00 | NPP-375 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 21512f36-bf32-388f-a3b6-d8415639c7aa | -14.44549 | -47.05633 | 2026-10-07 16:35:00 | NPP-375 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 940d7a6c-5f73-32d9-83b6-25746317e8c1 | -11.84477 | -47.30501 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 3f28f83d-d11b-3790-a12c-dc7d7bd15f7d | -11.62273 | -43.63528 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 19.0 |
| b988b56b-f25c-311b-a63a-17817b92e577 | -17.32892 | -40.77859 | 2026-10-07 16:35:00 | NPP-375 | CRISÓLITA | MINAS GERAIS | Brasil | 3120151 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 83ae2d3e-7724-394b-8cc7-1d13fe978198 | -11.76279 | -44.92643 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 4faf8aa2-20ac-3a6e-9a64-2d349a361f8a | -14.38876 | -41.26698 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| 79756663-b9d6-3258-8574-d2adee255456 | -11.71117 | -43.66455 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 363eb7ee-f7af-34ba-89cf-dc854132c443 | -11.85115 | -43.54378 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 63.2 |
| 67abba2b-c67f-315a-9d49-62b462765a26 | -12.61395 | -38.91245 | 2026-10-07 16:35:00 | NPP-375 | CACHOEIRA | BAHIA | Brasil | 2904902 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| e43b1f95-7401-3327-984e-ff422b3da450 | -11.7679 | -45.50877 | 2026-10-07 16:35:00 | NPP-375 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 60.8 |
| 49aacbc7-b35d-3dec-b2a3-c29f84a8768d | -11.86024 | -48.03813 | 2026-10-07 16:35:00 | NPP-375 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 58298e98-6d40-310c-a357-642f05c0ec91 | -15.10843 | -48.50607 | 2026-10-07 16:35:00 | NPP-375 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 363bdeaf-69c4-3465-b5bb-16ef66d482c3 | -10.70104 | -40.91588 | 2026-10-07 16:35:00 | NPP-375 | MIRANGABA | BAHIA | Brasil | 2921401 | 29 | 33 | nan | nan | nan | Caatinga | 8.0 |
| a0370a6d-473d-3a2a-a8d0-d00070981bfd | -12.87121 | -47.66365 | 2026-10-07 16:35:00 | NPP-375 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| aab23ccb-91f3-3da3-ba59-c7d9c933e337 | -14.21518 | -42.75436 | 2026-10-07 16:35:00 | NPP-375 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 246a79e3-d7cd-3a60-adde-4ce2bfe89d3b | -12.18622 | -44.79639 | 2026-10-07 16:35:00 | NPP-375 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 5960897f-34af-3028-aa7a-deba1def158e | -14.35583 | -41.27604 | 2026-10-07 16:35:00 | NPP-375 | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 97.0 |
| aa173320-80bc-3117-a38e-8af598624747 | -11.83642 | -47.33147 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| dae275c3-1e30-329e-81d3-8607f2831287 | -13.68327 | -49.0989 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bf66af52-b4ae-3f4c-8a8c-be3cb736c24c | -11.81937 | -43.52779 | 2026-10-07 16:35:00 | NPP-375 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 75b86c0c-0071-379e-9a89-1e6f76b61831 | -11.84706 | -47.38099 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d4401be6-d828-361d-bc75-7eedb7ebcbe1 | -11.84544 | -47.31 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| dcd06294-1562-3a6f-8803-f124752ebc12 | -12.04022 | -43.38616 | 2026-10-07 16:35:00 | NPP-375 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 26.4 |
| 750a421a-9ac1-371c-80d4-e56169705847 | -11.83843 | -47.34647 | 2026-10-07 16:35:00 | NPP-375 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0ad082ff-bb4d-319c-ae31-5fc201dcd588 | -11.82583 | -44.69225 | 2026-10-07 16:35:00 | NPP-375 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a69c8204-060f-3069-92fa-9df23b7fa5b5 | -13.39198 | -43.4789 | 2026-10-07 16:35:00 | NPP-375 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 26.3 |
| b2da4166-be86-3f54-9ef6-4936d4dacb69 | -12.82792 | -45.55846 | 2026-10-07 16:35:00 | NPP-375 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| d38eae67-60a9-3929-962a-580c7eff9557 | -18.76129 | -39.76706 | 2026-10-07 16:35:00 | NPP-375 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.4 |
| 5dc39e60-5ba1-3d6c-9e01-aaacc6b31bb2 | -12.9937 | -47.06234 | 2026-10-07 16:35:00 | NPP-375 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 508b180b-c2e9-3e7b-89ad-bbfefb031fd7 | -11.80464 | -46.70208 | 2026-10-07 16:35:00 | NPP-375 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6943f634-1359-3fb0-9e59-8127526aea9c | -13.60068 | -39.78797 | 2026-10-07 16:35:00 | NPP-375 | JAGUAQUARA | BAHIA | Brasil | 2917607 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f4f2db7a-f135-3d7b-849a-9d48c23bce0f | -11.76533 | -47.7361 | 2026-10-07 16:35:00 | NPP-375 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 468b8d3f-09cf-31fb-bd85-17c3229dcbfb | -14.68609 | -42.80655 | 2026-10-07 16:35:00 | NPP-375 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Caatinga | 3.2 |
| c26a2343-0485-31aa-9663-c9a33b64508d | -18.03395 | -44.56924 | 2026-10-07 16:35:00 | NPP-375 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6214ce70-2d78-37e7-843e-e268d1821078 | -11.817 | -40.62642 | 2026-10-07 16:35:00 | NPP-375 | PIRITIBA | BAHIA | Brasil | 2924801 | 29 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 4c729343-f18a-3547-9907-72707531e93f | -12.20418 | -48.42739 | 2026-10-07 16:35:00 | NPP-375 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 3b8b0937-3d57-3b27-9556-e13a5dd2670a | -14.07992 | -43.77087 | 2026-10-07 16:35:00 | NPP-375 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 49.9 |
| e7ecbdb0-8a27-3007-8258-9cfcaa48273d | -13.68995 | -49.10395 | 2026-10-07 16:35:00 | NPP-375 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |


[Clique aqui para ver as próximas entradas](README182.md)
