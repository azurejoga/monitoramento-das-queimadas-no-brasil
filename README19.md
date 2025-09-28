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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 31669974-d8b9-3304-a49e-9cf07bd7048f | -14.7652 | -45.68877 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01b01038-7880-3c1f-ab9b-4a4513a7c802 | -12.88902 | -47.09917 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3c4e4ef-bb1f-32eb-b9ad-00cef977d57d | -13.59916 | -47.32513 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 7d505c4a-efa5-39ff-987b-613064d4c6c5 | -11.7217 | -44.4169 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 18b00073-bb2c-38dd-b92b-3b77bda7cb9c | -9.29011 | -45.71593 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 02151823-5b96-36b5-84db-f13703e4d3fd | -12.68593 | -46.87835 | 2025-09-28 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0684541a-43ee-3cc4-b27c-67ad0e60992e | -15.97427 | -42.0147 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 941d275e-80c5-3617-896f-f6733d074692 | -13.77549 | -47.87422 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 154ef439-ce4a-361a-8201-2f410ce1a688 | -9.44813 | -47.61886 | 2025-09-28 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eea9ecbd-54ef-3aa3-9bfd-3a05499e5ea0 | -13.60557 | -47.29411 | 2025-09-28 03:38:00 | NOAA-21 | TERESINA DE GOIÁS | GOIÁS | Brasil | 5221080 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| dad383bf-65cc-36be-a0e3-a92efb5fc638 | -14.77072 | -45.68987 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 019f3ac4-fa1c-3f14-89ba-56207abaa1df | -15.33213 | -47.88237 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1cc16ff-c724-3b3b-be43-691cf951596d | -11.00089 | -45.60372 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bdaa47d-435e-3034-ac18-ecc7735fdd84 | -11.70492 | -44.41729 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6147c567-72de-3196-afe0-d1dc3f0f8938 | -11.40214 | -44.91132 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 11e1dfa5-55a8-37f1-b911-ed9dfb2db58c | -11.71497 | -44.42282 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 80dca072-6d05-3c8f-876e-1de9fbd0f678 | -12.94372 | -45.11262 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 048df4e3-8d9c-3947-9b45-b08952a48017 | -12.90602 | -45.15884 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7923a3b3-e97f-3640-b2f0-cf05b4700991 | -12.92878 | -45.15952 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 064007eb-ab6b-316b-ab64-fad8ae6e03f9 | -15.90169 | -46.20193 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0522bc96-4f0b-3bfa-8690-def8b2941429 | -11.40861 | -44.90781 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 30cbf12d-7551-3a77-b934-f01b5dadaa4d | -9.67661 | -44.52395 | 2025-09-28 03:38:00 | NOAA-21 | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dfe9833f-ba97-3fc6-915b-e51a5c860395 | -13.58838 | -47.31465 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6d922b49-aa3a-3074-b6c0-5aadd4c7cc92 | -11.43003 | -44.91648 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2963ef14-c3cb-36ee-80ae-08c8cb7be437 | -15.62598 | -46.259 | 2025-09-28 03:38:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2cb35da9-6075-3ea7-912d-9e6992f862e3 | -10.91514 | -45.72868 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 18708f9e-f34d-3168-a513-15d777dd5225 | -15.03192 | -46.96331 | 2025-09-28 03:38:00 | NOAA-21 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06f2f1d8-9a64-3937-afb4-3fe767be0f0a | -11.13833 | -43.37094 | 2025-09-28 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a036e22-13b0-3a40-88ff-334b50f70805 | -15.19384 | -50.09907 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 414d72b5-f6c7-3f74-b53e-8f318992f6b0 | -13.29899 | -44.15651 | 2025-09-28 03:38:00 | NOAA-21 | SANTA MARIA DA VITÓRIA | BAHIA | Brasil | 2928109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ee802023-ed95-394a-9777-dc09206f00bd | -11.65087 | -48.26967 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56d4111b-0503-3122-9858-f9482047cf25 | -11.58787 | -45.49012 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b9309a22-3db5-3e09-baad-2ab056b89856 | -12.92511 | -45.17819 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5828189f-87e3-3cc9-a147-a23cfadd0124 | -12.92658 | -45.17072 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f5459f9f-c095-33cb-bb59-e6fb7e17c838 | -13.26521 | -48.4562 | 2025-09-28 03:38:00 | NOAA-21 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8798bcdc-0505-3ea0-9529-78174084f697 | -9.44238 | -43.69925 | 2025-09-28 03:38:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| be303cc5-8a44-3841-8487-f36d7efc7a26 | -11.60534 | -45.43075 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 865216d4-d65b-3840-b305-b068b4601cb6 | -15.52356 | -42.20074 | 2025-09-28 03:38:00 | NOAA-21 | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 766e9231-ee7b-3204-b887-3bfc0b330d06 | -15.62655 | -48.35398 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b866ab5f-750d-3458-8b59-84ff376ae706 | -15.89931 | -46.21355 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8da7572f-4b55-3c36-8280-f2546f64a7dc | -11.41355 | -46.95695 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 157476f9-a10b-330e-b586-23791e6e6ae0 | -13.62349 | -47.3231 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ed92da7e-0b79-38f1-ba6c-5c37349737c5 | -11.50445 | -43.53826 | 2025-09-28 03:38:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2973baa9-0c17-3100-a3c8-79b4372bafe6 | -14.58756 | -48.24788 | 2025-09-28 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c7a6f202-e9ba-3853-8b52-a71ebbf192b8 | -11.42396 | -44.91797 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b4e4786c-4727-3721-9ea2-b8a79dbfbc0b | -12.82732 | -44.68308 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00f1b20a-0f68-3182-9ac1-bca1cf08a6ef | -11.97767 | -47.88609 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6218615f-cddd-3b82-ad65-f13ac94d3be2 | -13.62463 | -47.32731 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f0f9bb09-ffee-3a9c-a2f4-aaa22f8334c5 | -15.33404 | -47.88407 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42dfaf37-3061-33ed-8942-0ab3ce792317 | -12.92584 | -45.17445 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9143f58f-fbc5-3f03-a5cf-79f373c6fe80 | -15.58478 | -42.40594 | 2025-09-28 03:38:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 59d5ccfd-5c5a-30a6-b7dd-ed74d4b2dc14 | -10.92092 | -45.7305 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 981e0064-2a35-301e-969d-ad3ba82408ba | -15.81783 | -41.89091 | 2025-09-28 03:38:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Cerrado | 8.0 |
| e90edbfa-c366-308f-9516-7baef225cb8b | -13.6462 | -48.0709 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8eac2ae6-1777-3891-a529-f4051f1ad95d | -12.02315 | -47.93196 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 69a07296-0481-354c-a202-e46647f68993 | -13.58535 | -47.29804 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8c0c94fd-498f-32dc-9cdd-da6caf9bb14b | -13.79255 | -47.9201 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| afa352c5-8bd7-3407-adf5-10d064a9fde7 | -10.91242 | -45.74235 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c19dbc0b-9f70-3793-b4b9-4e6c558b9de2 | -9.07044 | -45.53896 | 2025-09-28 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 551a3dd8-832d-31aa-80cb-c2ea0bceb204 | -15.33711 | -47.88937 | 2025-09-28 03:38:00 | NOAA-21 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 277dbb35-99a6-38e4-a2a5-885a93203c3a | -11.99797 | -47.88775 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 86020cc6-6383-39dd-94f8-e361e5e9ddcb | -11.40728 | -46.95546 | 2025-09-28 03:38:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a4eff37d-08db-3120-b6c5-321cf2a58894 | -11.44571 | -44.98488 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4e33c077-becc-3208-b1e1-ea229b7690d9 | -12.82664 | -44.68657 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 96987f43-0e69-3b94-b03c-9ee048b99b11 | -12.89129 | -45.17528 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 28a35dc3-0001-3c03-a905-a851436f537b | -12.95685 | -46.38318 | 2025-09-28 03:38:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ef101d33-7d66-3ce8-9075-45b1dd08f3ee | -11.98988 | -47.89349 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| e7114ebb-d25b-3f94-9d31-69929bee7582 | -11.98642 | -47.9907 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cf268bff-dd13-3df0-aacb-2198a41fe756 | -13.60436 | -47.32157 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 89e3d7f0-eac3-3987-a92a-d6268d55c24d | -15.44053 | -48.24358 | 2025-09-28 03:38:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| fb56a865-815b-35b3-a7cd-865c90496e7c | -13.78361 | -47.89903 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| fab5675b-73ce-3cc7-8623-c579855dcc88 | -15.87875 | -46.22869 | 2025-09-28 03:38:00 | NOAA-21 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 9ffc2d74-940a-37cb-82e1-649228290759 | -11.9544 | -47.91098 | 2025-09-28 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b09d235e-674e-3531-8314-cc7a30d12e98 | -10.90571 | -45.74513 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ebccc302-376c-3597-a6c3-231afefdcd26 | -13.29157 | -46.44114 | 2025-09-28 03:38:00 | NOAA-21 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 58dee2d0-d5d8-37e2-8823-97e43a071348 | -11.99732 | -47.04424 | 2025-09-28 03:38:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a21cc356-a7ac-3835-be67-2b174c1fafe8 | -11.45063 | -44.98942 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2ad118c9-e134-3a36-84d9-755c2b86a073 | -12.29622 | -45.64884 | 2025-09-28 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 96d710b6-af07-3dc6-b774-60a48bcd3240 | -15.53547 | -47.92437 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 68d92653-aca2-3ccc-88eb-d5b17b55873f | -13.77711 | -47.89815 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 266b412e-5223-3f7e-8eaa-1b42e9a6a151 | -13.52089 | -47.40097 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 24924820-e264-3092-aa3e-ca7dc052c87e | -11.42333 | -45.04034 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d5372397-c347-3e87-aedc-fc828b818b27 | -13.7849 | -47.8929 | 2025-09-28 03:38:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c3c3e660-f063-3a10-aee9-2daaced927f6 | -13.64914 | -42.38445 | 2025-09-28 03:38:00 | NOAA-21 | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| ec9d127e-a53f-32d6-a37f-fa472cc061d3 | -11.4463 | -44.9818 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f98a95a-2aeb-3893-9a5b-f238a42411f6 | -10.53796 | -43.63004 | 2025-09-28 03:38:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b70b7232-8dc1-3ce1-bedf-7391a150abb0 | -12.25679 | -44.09343 | 2025-09-28 03:38:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fa3aa81b-cc51-3d4a-8e89-ba459988c44a | -12.98569 | -49.44034 | 2025-09-28 03:38:00 | NOAA-21 | ARAGUAÇU | TOCANTINS | Brasil | 1702000 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 27f47f38-68e2-39b9-9dff-661960cadf08 | -11.36827 | -44.94481 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 38a3ea8c-e03a-33c1-ba6c-94fae1cf59ff | -15.53425 | -47.92068 | 2025-09-28 03:38:00 | NOAA-21 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 7.7 |
| e4a9932b-0182-3e08-9920-cf6eae3072b2 | -12.90528 | -45.16257 | 2025-09-28 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 78f3e4a0-f515-3af3-b232-d0d6464a3546 | -14.89361 | -45.56314 | 2025-09-28 03:38:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ebf4ca3c-f6dd-3ced-af0e-6999eb4f51c6 | -11.65243 | -45.34015 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 545325ea-7dfe-3c82-b07c-9c46a2422ded | -9.04521 | -46.72233 | 2025-09-28 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| b84ffe23-6ff3-327d-a3ab-598891ae312c | -11.42688 | -44.96236 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1a6fa84-d3d4-34ae-be50-860a26afe855 | -11.43645 | -44.97275 | 2025-09-28 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a806ef8-3165-37bf-a789-4aa4e652559b | -13.76221 | -48.31544 | 2025-09-28 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d960650d-1465-3783-a077-1f50cb761a93 | -9.28527 | -45.71269 | 2025-09-28 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 90eea96b-c455-3cd1-8658-93c07e22228e | -10.90295 | -45.75894 | 2025-09-28 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| aa2e600e-e902-36d4-bbd0-489a5d2f2932 | -11.72034 | -44.42387 | 2025-09-28 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 6.7 |


[Clique aqui para ver as próximas entradas](README20.md)
