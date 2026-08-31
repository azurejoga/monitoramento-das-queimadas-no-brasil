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

## Dados Diários - Página 33

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 277586b7-4f74-31c6-863c-cf0fc7e2ee52 | -14.38884 | -52.55579 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 745bb4a5-1eb4-37a3-9ed2-594280ec7409 | -15.66636 | -45.93013 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 988c9c95-ebe4-35b0-811f-dbb18a413405 | -16.99158 | -40.93785 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 549e00b6-7219-32f9-aa04-c265dd2a695a | -14.45658 | -42.64999 | 2026-08-31 04:17:00 | NOAA-20 | PINDAÍ | BAHIA | Brasil | 2924504 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| a95ff48d-52ce-3ffa-891f-6e14fc3ad277 | -13.36465 | -46.9202 | 2026-08-31 04:17:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3e1519d-71f3-31ab-91bc-4bff4fbac042 | -13.6344 | -51.84381 | 2026-08-31 04:17:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5b20c16-55c8-31d3-a461-6c4936ab003b | -14.19439 | -52.8757 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0c44340-e6e5-3199-97f0-13b65f72b813 | -14.23185 | -52.85306 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 634bdc1a-35ab-375f-8bac-eb7ac2bc59aa | -12.95161 | -45.94355 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ea811243-567c-37a5-9fe8-e121883eb197 | -14.07576 | -42.4522 | 2026-08-31 04:17:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0d6ea6aa-bc02-31f8-9fc5-dde4d486bfed | -13.3844 | -41.33124 | 2026-08-31 04:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 436a333f-947e-3c4c-bc7d-8879bd3858c6 | -13.05925 | -45.18387 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7f5dbbcd-f558-3cbf-a593-810b0672cc67 | -15.67925 | -41.70229 | 2026-08-31 04:17:00 | NOAA-20 | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 881bb792-52fa-3af4-84f6-bc506f2e1179 | -18.28594 | -52.67551 | 2026-08-31 04:17:00 | NOAA-20 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 544c88f5-4fdc-3536-bc44-ce6721cb151c | -14.44466 | -52.54421 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 12fe590d-b4c4-329a-a858-c942922c485a | -14.1937 | -52.87912 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 219bddf1-544b-36d3-9611-3d52605e6717 | -14.17367 | -52.87694 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e187d9b0-7371-3346-9764-60459cd9d686 | -13.9603 | -54.4029 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8dde7da7-8df2-3815-90d9-2a96fdaec2de | -14.5772 | -54.08793 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ed500102-2d6d-3fc7-a644-6678b7785068 | -14.42764 | -56.27397 | 2026-08-31 04:17:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dadde557-0f47-369a-9211-cf009dee61b9 | -15.19089 | -46.24219 | 2026-08-31 04:17:00 | NOAA-20 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 78bab09e-8b43-305b-acf2-0596050a6968 | -14.90151 | -44.80576 | 2026-08-31 04:17:00 | NOAA-20 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a7962146-0472-3ad1-b5cf-3b95225c6c0c | -17.79235 | -39.70807 | 2026-08-31 04:17:00 | NOAA-20 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| e29a6fb0-7eb9-3b0b-99e5-51d65e19e4da | -14.43629 | -52.53231 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4427b51f-a7a1-347a-9a00-f7c215680e66 | -12.92545 | -45.86096 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 044d0745-7221-34c9-b4f9-b35612d549c4 | -22.01849 | -56.03863 | 2026-08-31 04:17:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 63a63fea-046a-3911-97e8-f69d4c5a4c82 | -14.23141 | -43.8227 | 2026-08-31 04:17:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 116833fc-6196-3b20-9d71-b73c39979a61 | -14.39468 | -52.55337 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| edb9c8b2-364e-36f3-bb7d-ec4748486ae8 | -16.98856 | -40.93308 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS FORMOSAS | MINAS GERAIS | Brasil | 3100906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 14e4cdd5-d812-3c1c-a360-e2d0b43db7da | -15.55019 | -56.29012 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e1a6ef79-8a43-3b77-a7e7-5e66b0d8191d | -14.39221 | -52.5658 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 687f8188-9a74-3d38-b2f0-a69403a6c0d7 | -13.84914 | -54.09383 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d9fc41b0-ddc8-3b81-8ccf-c6e1a18d328c | -13.19934 | -44.07069 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c99351b2-7336-386b-93f3-5c11ec32fc83 | -13.24315 | -43.58578 | 2026-08-31 04:17:00 | NOAA-20 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7a1f57e9-f488-3cae-ba44-358a5ca0e5bf | -16.28255 | -42.57261 | 2026-08-31 04:17:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aec95f35-b5a1-3ab8-9102-6b5039dc13db | -13.19269 | -44.06954 | 2026-08-31 04:17:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d08e56db-25d7-3193-a6d4-03882743de72 | -14.15857 | -52.78648 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ab44381-dd4f-371d-bf37-9238aa919efd | -17.50587 | -44.2255 | 2026-08-31 04:17:00 | NOAA-20 | FRANCISCO DUMONT | MINAS GERAIS | Brasil | 3126604 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 05cac217-585c-3326-bfc5-0a66c2bef7ee | -13.83938 | -54.01957 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 06c8074b-a20e-3ada-85d0-38b5b80e4b90 | -17.28304 | -46.00177 | 2026-08-31 04:17:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 13472ade-fec8-308f-83a5-2b3f2f4ee579 | -14.18245 | -52.88037 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 631b0690-0ee5-3ee5-a8df-2ccacf37aa4f | -13.08503 | -45.17644 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f66aac16-4332-3ebe-8569-97c76dc41126 | -14.6781 | -54.90938 | 2026-08-31 04:17:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46bcbc56-e6f3-3645-b060-a1771fe153d4 | -14.5932 | -54.10588 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e2c78c8-a986-3d5d-9d5f-c370e6580ea6 | -15.71291 | -48.25585 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUAS LINDAS DE GOIÁS | GOIÁS | Brasil | 5200258 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aa11e646-789b-319d-a30f-4e3ce33963fe | -15.88803 | -46.02773 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d6e5613a-c4a3-3e0a-adb5-297fa28411b2 | -15.1237 | -53.58622 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d92a70e9-e8ac-3070-bdf3-59f4d6ee682c | -13.88477 | -41.63393 | 2026-08-31 04:17:00 | NOAA-20 | DOM BASÍLIO | BAHIA | Brasil | 2910107 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| cac51138-5f0b-3761-8a4c-e6fc588649c4 | -12.89522 | -45.84738 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aaafd219-533a-30a7-a439-d3a0c0dca41c | -14.90321 | -46.90265 | 2026-08-31 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b810a059-5a8d-3785-87e5-e54c938e34fa | -15.09184 | -48.10791 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| e4bf08f5-c4ee-3318-928b-eda8b0ae4178 | -15.63239 | -50.08763 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76b4c7af-beaf-34bf-9c2c-9c6428858969 | -14.60525 | -54.10475 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a6399743-9cc8-38d3-b383-24fa96848762 | -15.70018 | -39.89529 | 2026-08-31 04:17:00 | NOAA-20 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 87717eb0-ab90-3d3c-87c7-c5e15428fcaa | -14.42779 | -56.27393 | 2026-08-31 04:17:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 335326f3-1963-3bfa-84e6-bc3bae27782e | -14.58132 | -53.08216 | 2026-08-31 04:17:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd3d7ae9-67f6-3122-8fe3-e1bccdaff9d9 | -14.90755 | -46.89901 | 2026-08-31 04:17:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b8023391-b0ae-318f-b4ef-64443425ddd3 | -14.29796 | -52.90093 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c064da89-be6f-3d74-b5dc-43992093cbac | -12.78374 | -46.45813 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 8415d6e2-c277-3f90-8c1e-a9483d701768 | -15.77426 | -48.52974 | 2026-08-31 04:17:00 | NOAA-20 | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c9ec42b-30ac-3e79-a43b-750326515733 | -13.38782 | -41.33179 | 2026-08-31 04:17:00 | NOAA-20 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 4d626e06-41af-389e-bf94-e3f4cb627597 | -12.95017 | -45.93084 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86b1c803-ec72-3790-afba-e9d3874969b5 | -13.08781 | -45.18082 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1e3dd16b-07c3-30f5-ac07-9a288f351e67 | -15.40645 | -52.70073 | 2026-08-31 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ad1d1d1-742c-340a-8691-82088f3bd352 | -14.60112 | -54.12464 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4aee12e3-2f01-36fb-ac96-0656abe6e285 | -14.20172 | -46.57212 | 2026-08-31 04:17:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 99c74520-9e02-3e2e-bd69-cc8063183d69 | -15.12445 | -53.5826 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ff571c81-b163-3836-b22c-55480119886c | -20.46371 | -44.41322 | 2026-08-31 04:17:00 | NOAA-20 | PIRACEMA | MINAS GERAIS | Brasil | 3150604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| eb25eaff-81eb-35d1-8c5c-14dca1a9c511 | -14.59755 | -54.10401 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc4aed7c-729e-39ce-a724-53bf9f1bc4bf | -18.22414 | -51.65662 | 2026-08-31 04:17:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e33724fd-455c-3607-a463-2c081b67234d | -12.77576 | -46.46118 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b5064fcc-0197-30df-8dcf-bf934ea8b55a | -13.84257 | -54.09667 | 2026-08-31 04:17:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1165f34d-4584-31e1-9c6a-7387d0a5cebf | -15.12351 | -53.58294 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e2f7984-1265-37ea-a356-dc9bee255113 | -15.63084 | -50.09586 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d0aeca48-fbd2-39c2-aecd-7932a0df2356 | -13.05646 | -45.17952 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b286a3bb-fc66-30a3-943c-9a24e35e14ae | -15.67194 | -45.93909 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c2856ef8-a6f5-3b36-a356-1cb22fb5b04a | -15.23987 | -53.88232 | 2026-08-31 04:17:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b462c7b0-965b-3cbd-80b7-8522559a75f8 | -13.4184 | -51.38365 | 2026-08-31 04:17:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 70dfad73-6a67-33c8-9bdb-0507c2d9ab70 | -15.66422 | -45.92174 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 814e2783-1c31-3c73-b584-7b5cce427cf7 | -14.46464 | -52.19947 | 2026-08-31 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9c90a78a-5c3b-3f61-b8ec-7360f3f13e49 | -17.58962 | -39.49519 | 2026-08-31 04:17:00 | NOAA-20 | CARAVELAS | BAHIA | Brasil | 2906907 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f83c37dd-f8b8-3ab4-aea6-eec0c610f0fa | -15.02818 | -48.16571 | 2026-08-31 04:17:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e0304a0c-36b4-3d95-a433-a6951dc42311 | -12.9191 | -45.85574 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ca73de22-2374-3b88-a9e2-39dc33495ad8 | -12.9523 | -45.93953 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f944afb0-9a66-3dff-949c-372df2f0c4ef | -15.63945 | -50.09738 | 2026-08-31 04:17:00 | NOAA-20 | GUARAÍTA | GOIÁS | Brasil | 5209291 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3359d05d-6d09-3c9b-aedc-a80221d01eff | -12.93913 | -45.90894 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1f904150-febb-3e72-a116-19c994ee03de | -12.90006 | -45.84008 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9c2ffd3e-b77a-3991-8943-ae757cdd9f4d | -15.66145 | -45.91709 | 2026-08-31 04:17:00 | NOAA-20 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6aed67de-6d1c-3fb7-a36e-04ac92a3b364 | -15.67637 | -56.27681 | 2026-08-31 04:17:00 | NOAA-20 | VÁRZEA GRANDE | MATO GROSSO | Brasil | 5108402 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d78cc471-1a95-3b2f-866a-db0fdaff6d19 | -14.40364 | -52.53513 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e7d3f2ee-ac51-35ad-a02a-a12705debf33 | -14.38586 | -52.57076 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8cfa5f91-3f91-3931-ba42-4d24c25932ec | -14.46523 | -52.1965 | 2026-08-31 04:17:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 117d0238-46f0-3a33-9dd2-b13713854009 | -15.87195 | -56.49232 | 2026-08-31 04:17:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 64eee914-3ced-3d56-8fa8-e91a869f1a6e | -14.13817 | -52.80666 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1fac7cc1-7136-33b4-aaf8-2b8f41aef5f7 | -12.95135 | -45.9443 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7b4031f7-1e22-3c32-9be1-34352a2ce374 | -14.13951 | -52.79995 | 2026-08-31 04:17:00 | NOAA-20 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6c44a77a-8cc4-36b0-bcc4-4123e1792274 | -12.91871 | -45.90113 | 2026-08-31 04:17:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46cb44d1-4a56-31b5-be63-7d93e3253279 | -12.77653 | -46.45671 | 2026-08-31 04:17:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 505f7be3-3abf-38c2-977c-595fef223237 | -14.29407 | -52.89302 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8791178-089d-3fa2-b0c8-03bbcb0358b6 | -14.38644 | -52.5678 | 2026-08-31 04:17:00 | NOAA-20 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |


[Clique aqui para ver as próximas entradas](README34.md)
