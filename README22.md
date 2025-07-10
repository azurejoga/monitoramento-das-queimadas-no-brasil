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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d7acf39a-7ac4-382a-a076-0f979e733e4d | -11.32505 | -51.44644 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a95315f8-406f-39eb-a530-690145c6d64c | -13.34627 | -52.91048 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b79458c-efd6-34f4-bf9d-9352f277d275 | -17.78407 | -52.43378 | 2025-07-10 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 450c8e42-1008-3b8e-a054-7a03bc242f90 | -17.65353 | -46.83448 | 2025-07-10 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 79896807-3dce-3bad-b04b-17006a6143da | -13.91429 | -51.81223 | 2025-07-10 04:27:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dbd4e8e-d394-31a4-a6ae-cc0e6403259c | -13.01635 | -46.28886 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 656194b7-7eeb-3b8e-8bb5-a424931e7ea6 | -13.00677 | -46.32907 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3675a228-be52-3195-93c9-76feeba496f2 | -19.698 | -44.61452 | 2025-07-10 04:27:00 | NOAA-20 | SÃO JOSÉ DA VARGINHA | MINAS GERAIS | Brasil | 3163102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b8cc133e-5d79-3f29-a4a2-27bf8714e811 | -13.38503 | -47.87812 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2b9a4608-5ae3-314c-8370-951293414a2a | -13.00281 | -46.28669 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f31d79c6-17d2-34d8-8f0d-21a6cf9a5cf2 | -15.47676 | -45.19638 | 2025-07-10 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a0af4e45-b644-357d-830a-d55be37ba334 | -19.05694 | -48.33606 | 2025-07-10 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bd540cb5-cfb2-3c16-9c8a-8ebfd4f7f763 | -13.00674 | -46.2836 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e71f07bb-f9eb-3ccf-a682-42add24ddbaa | -16.68236 | -43.88395 | 2025-07-10 04:27:00 | NOAA-20 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 34361e08-f1e8-38e6-b91a-b8a6ee11d94a | -12.42982 | -43.72112 | 2025-07-10 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 3787f0a2-0950-3adb-9150-0d7a793c9f03 | -12.4691 | -46.91355 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9068da3d-0e22-32a1-af83-7ca1f7f5e1b5 | -11.8716 | -58.72215 | 2025-07-10 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45a8bd3a-9ee6-3baa-b2a0-4e0cf37f45ed | -12.48007 | -44.50328 | 2025-07-10 04:27:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| acb247d0-e014-3209-b292-63c6c6fc38b8 | -11.75138 | -48.34487 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d633de6-31f4-3d1e-b917-95c18b9c2aa2 | -13.9002 | -42.13348 | 2025-07-10 04:27:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| c84396ff-8d99-32b3-be82-d47aca2bd6f7 | -15.09982 | -50.61237 | 2025-07-10 04:27:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 437dcf8d-86d7-32c5-8b17-bbfd3bb877b3 | -16.58135 | -43.6481 | 2025-07-10 04:27:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3275aac6-066e-3916-9c19-a453e621f3dc | -13.01128 | -46.32217 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47e3e203-da32-3f1d-b605-583ceffd2912 | -13.34231 | -52.90977 | 2025-07-10 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| dc8fc624-dfdf-3efe-86ee-8e5ddd2c8f73 | -15.4735 | -45.19853 | 2025-07-10 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 36a090d1-44ba-3e72-b262-d52ab11793e4 | -13.89592 | -42.1329 | 2025-07-10 04:27:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 00d3d06b-25cd-3206-848c-8a130762f974 | -13.02082 | -46.28223 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c7f1567-2bc4-39c0-aa22-48ddbe4057ed | -13.90447 | -42.13405 | 2025-07-10 04:27:00 | NOAA-20 | LIVRAMENTO DE NOSSA SENHORA | BAHIA | Brasil | 2919504 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 6b5562c7-7300-37aa-b632-6d5a1aca3fc0 | -13.65125 | -46.81541 | 2025-07-10 04:27:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8e9b7900-ea3d-3d99-8f0c-133605acadea | -13.01071 | -46.32589 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73b04a61-5102-3434-a45c-28f1fe5b3826 | -13.1554 | -47.28275 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ae489c9e-4edc-3d36-a05e-b3fa117a5e86 | -10.87441 | -54.04334 | 2025-07-10 04:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a16f291b-70d9-3000-8176-55863e0dbebd | -18.0349 | -50.53691 | 2025-07-10 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6573bdb4-5564-3c6e-b81a-9da83d139e18 | -13.15981 | -47.27619 | 2025-07-10 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b4e24b21-c5a1-3c56-af81-738770affb94 | -18.79133 | -47.96125 | 2025-07-10 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| f7564215-cc48-34c0-bbe7-b74e8c6e03d2 | -16.50722 | -49.10084 | 2025-07-10 04:27:00 | NOAA-20 | TEREZÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5221197 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5c570da7-ec78-325e-9b33-d85c07c921ad | -12.98261 | -47.82344 | 2025-07-10 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fb8aafd5-55c1-3bd3-9f00-15431564a246 | -13.03609 | -46.30333 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 954c8347-1c8a-36f2-821e-50aae0ffaea3 | -16.74023 | -52.84208 | 2025-07-10 04:27:00 | NOAA-20 | PONTE BRANCA | MATO GROSSO | Brasil | 5106703 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f3284044-0196-3f50-8131-4d9f89e6598d | -11.8304 | -48.21276 | 2025-07-10 04:27:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 905f072a-a9cb-34c9-be65-8210447eaa83 | -13.67565 | -44.22124 | 2025-07-10 04:27:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 9acd528a-40fe-39e9-987d-61d710d26fd8 | -15.03219 | -57.18839 | 2025-07-10 04:27:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 21a05b0d-48f1-3a5a-a34f-838ecfd4555b | -11.32879 | -51.44711 | 2025-07-10 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 832a76c3-d05e-304d-920c-bf0996fabbd2 | -19.45311 | -45.30655 | 2025-07-10 04:27:00 | NOAA-20 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9376cb82-7c6d-3adf-9c27-19466a1a1246 | -12.43376 | -43.71913 | 2025-07-10 04:27:00 | NOAA-20 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2196ae73-f36d-38dc-8770-09dcd9ade2f7 | -13.36361 | -47.77694 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4110d065-7929-33d0-8f6e-29e11756c510 | -13.01523 | -46.31901 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 308a7b62-e173-39d3-9e67-c8853e8239dc | -15.4741 | -45.1942 | 2025-07-10 04:27:00 | NOAA-20 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cf9023ab-2e05-3ad5-964f-d1a33ce9cfc5 | -15.07784 | -48.94476 | 2025-07-10 04:27:00 | NOAA-20 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a935a908-b4b1-3942-884f-4f42abefe50a | -12.03522 | -48.75723 | 2025-07-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 29638989-db26-338c-ad09-161e9fb9199b | -13.00733 | -46.32536 | 2025-07-10 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2726a178-80de-3d67-a97e-f042aa969288 | -11.8725 | -58.71767 | 2025-07-10 04:27:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| df18dc62-613c-3021-b166-58143578ac19 | -13.38447 | -47.88165 | 2025-07-10 04:27:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a8c9b0d6-ccec-3ba3-bc61-c5b108a7bbbe | -11.32721 | -55.21154 | 2025-07-10 04:27:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e3d67bf-1b74-332b-890d-4f5469f4ab7b | -12.22286 | -44.21718 | 2025-07-10 04:27:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7fe47031-195a-31e4-aee5-094bf1eef432 | -12.22046 | -44.20785 | 2025-07-10 04:27:00 | NOAA-20 | CRISTÓPOLIS | BAHIA | Brasil | 2909703 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 615a4452-0666-3c6e-9c60-8bfdb398d367 | -12.03856 | -48.75778 | 2025-07-10 04:27:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 214225d2-757d-37fb-b558-eaa2642bdc27 | -16.84403 | -49.35356 | 2025-07-10 04:27:00 | NOAA-20 | APARECIDA DE GOIÂNIA | GOIÁS | Brasil | 5201405 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cc18a04-12d3-3a5f-a8d2-eda236958189 | -19.36921 | -51.39927 | 2025-07-10 04:29:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1b4f86c8-3989-3055-88ab-cbf4ef67c70d | -20.19195 | -49.12286 | 2025-07-10 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 4.7 |
| fbfa9688-cdf9-3837-b318-ee0d26b35035 | -18.64982 | -55.72572 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| fc650b41-36a3-3e7a-8f29-a1aca94f5258 | -22.63151 | -52.14124 | 2025-07-10 04:29:00 | NOAA-20 | PARANAPOEMA | PARANÁ | Brasil | 4118303 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| bf708ce2-d434-332b-b52b-012306afd668 | -18.64205 | -55.71954 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 2b66a525-ac8a-3688-a7bc-117e512d6284 | -21.77472 | -52.7554 | 2025-07-10 04:29:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b914172b-53e2-38d4-b21d-c1123c000fa6 | -20.76203 | -46.76799 | 2025-07-10 04:29:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 1773bd36-2c56-3512-bb98-cee16efdfc90 | -22.67417 | -42.85444 | 2025-07-10 04:29:00 | NOAA-20 | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| a4e140bb-d2df-343e-8435-a06b80d00309 | -21.63493 | -49.84074 | 2025-07-10 04:29:00 | NOAA-20 | GUAIÇARA | SÃO PAULO | Brasil | 3517208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 9cc234ba-8eac-3fe5-b2a2-71e5fa4134fb | -19.39848 | -54.46717 | 2025-07-10 04:29:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f65d9ae0-5792-3486-925c-db1fc8bcc343 | -19.44683 | -48.53717 | 2025-07-10 04:29:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 79628524-1b68-36e4-bfc2-2a1aad800bf5 | -22.24763 | -49.61145 | 2025-07-10 04:29:00 | NOAA-20 | GARÇA | SÃO PAULO | Brasil | 3516705 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| b1ebdb2c-2478-3db3-a73d-cf75fe42def9 | -19.08733 | -56.0466 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fc785697-d1f4-3102-a77f-10a350ff0427 | -19.44961 | -48.54139 | 2025-07-10 04:29:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c3b1bde9-dbc2-3276-b16f-debf357bff63 | -20.47751 | -53.67493 | 2025-07-10 04:29:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7970a7f-b865-3286-a8c6-71d866342a7c | -21.43918 | -54.57933 | 2025-07-10 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| de1e44b6-1000-3b1a-b871-3a56563c294e | -19.45017 | -48.53771 | 2025-07-10 04:29:00 | NOAA-20 | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f6420abb-f4f9-3163-9bcd-e4c8b9457118 | -20.95876 | -56.59047 | 2025-07-10 04:29:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6eab3353-9e5c-30d2-9ea8-4da0efc1a7eb | -19.86229 | -54.38868 | 2025-07-10 04:29:00 | NOAA-20 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 91b3d478-ed7d-32da-bb0c-a900edf42421 | -20.19138 | -49.12654 | 2025-07-10 04:29:00 | NOAA-20 | FRONTEIRA | MINAS GERAIS | Brasil | 3127008 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 558c9c17-938d-37c4-8d08-576c9ef72172 | -21.7642 | -48.12238 | 2025-07-10 04:29:00 | NOAA-20 | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4b4e9225-471d-33af-843d-cc9720aca55c | -20.9591 | -56.58824 | 2025-07-10 04:29:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 4afe7bf9-d9ef-3fd1-a6a1-c14ad413625c | -21.31026 | -48.56924 | 2025-07-10 04:29:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1e88ad7e-3ab8-37ef-84f7-acffbd94ffd2 | -18.64551 | -55.72479 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 0ab75e38-f40e-370e-a17a-b356563382e0 | -20.5712 | -47.86732 | 2025-07-10 04:29:00 | NOAA-20 | SÃO JOAQUIM DA BARRA | SÃO PAULO | Brasil | 3549409 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d726369e-5fcd-3b4c-b218-5d199002d086 | -19.97807 | -47.18469 | 2025-07-10 04:29:00 | NOAA-20 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b3169ed2-44b2-3651-9a23-246c8ca2e9d8 | -21.65905 | -48.71249 | 2025-07-10 04:29:00 | NOAA-20 | ITÁPOLIS | SÃO PAULO | Brasil | 3522703 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 16e38db7-06fa-3d7d-a620-02b5ad03c0cb | -21.11546 | -47.80298 | 2025-07-10 04:29:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| a1b6d03d-95a7-38fc-a896-6d40074792fc | -19.37262 | -51.3999 | 2025-07-10 04:29:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 261a6aac-ca01-3015-902f-1fa084d72b64 | -19.36986 | -51.39538 | 2025-07-10 04:29:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e545fb5-9efa-3b06-84f7-fe80a5baf676 | -21.43722 | -54.56827 | 2025-07-10 04:29:00 | NOAA-20 | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9f17aa15-c00e-3651-9d73-36006a08c2a3 | -20.28852 | -46.67117 | 2025-07-10 04:29:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b6858580-8bc7-3674-b6b1-8ba1cbf97a10 | -21.00056 | -55.60203 | 2025-07-10 04:29:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 690d0086-0a91-35a2-ad17-b862fe4ff19d | -23.84073 | -52.61726 | 2025-07-10 04:29:00 | NOAA-20 | CIANORTE | PARANÁ | Brasil | 4105508 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 736fa90a-fa20-3140-af4d-dab29a50d6f7 | -20.28499 | -46.67044 | 2025-07-10 04:29:00 | NOAA-20 | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b480ad4c-8d12-39af-9ae9-48fe2384385c | -24.24106 | -50.73954 | 2025-07-10 04:29:00 | NOAA-20 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| bdd0a2b8-0f7b-339e-a813-2361646bf8b1 | -18.6472 | -55.71614 | 2025-07-10 04:29:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7b4d11b9-994d-396e-939d-05a516d4edc6 | -19.37327 | -51.39602 | 2025-07-10 04:29:00 | NOAA-20 | PARANAÍBA | MATO GROSSO DO SUL | Brasil | 5006309 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5ceb42f8-afbb-37cf-95dd-40fc78d6c92c | -21.9616 | -56.07978 | 2025-07-10 04:29:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5b125fca-c0c0-3f70-9a16-0bfa1676a5d4 | -19.65489 | -50.88647 | 2025-07-10 04:29:00 | NOAA-20 | CARNEIRINHO | MINAS GERAIS | Brasil | 3114550 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 4e4c3526-150c-387f-9901-4dd672285a21 | -21.77049 | -52.75894 | 2025-07-10 04:29:00 | NOAA-20 | BATAGUASSU | MATO GROSSO DO SUL | Brasil | 5001904 | 50 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f32a10f4-4137-3ad8-996c-18e3f29348b5 | -22.21388 | -56.19538 | 2025-07-10 04:29:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README23.md)
