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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 917d3b88-ad93-3f4c-9dd6-e2f33f8d6823 | -21.07974 | -48.66358 | 2025-04-11 00:24:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.2 |
| ba2d8a6a-cf3e-3cf9-80b6-037400bcd122 | -21.34463 | -48.59191 | 2025-04-11 00:24:00 | TERRA_M-M | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| d6fc79ff-e62e-39a0-97c6-33b9bc683d7c | -21.07637 | -48.68084 | 2025-04-11 00:24:00 | TERRA_M-M | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| bad03e3d-9863-378a-a1fe-27471dadd952 | -20.18945 | -51.16857 | 2025-04-11 00:24:00 | TERRA_M-M | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 122.7 |
| 954a1ed6-da19-3b8e-9709-7b402d7cef9c | -9.63101 | -36.82134 | 2025-04-11 00:26:00 | TERRA_M-M | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 15.6 |
| ba628e7e-a3a9-3992-b8f7-7f400f2feaac | -7.49078 | -41.32494 | 2025-04-11 00:26:00 | TERRA_M-M | JAICÓS | PIAUÍ | Brasil | 2205201 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| a97ea7ae-3e2a-3b79-ba86-1260fa941293 | -15.25033 | -47.46371 | 2025-04-11 00:26:00 | TERRA_M-M | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 39620712-0c8a-3954-b3af-3f747b7c8299 | -11.84832 | -38.20277 | 2025-04-11 00:26:00 | TERRA_M-M | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 6ab595d0-9d47-3e7c-89b8-66ca3b6b458d | -8.11097 | -43.12032 | 2025-04-11 00:26:00 | TERRA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| 1c04e7d9-684c-3842-a35f-a04321074e17 | -10.71524 | -42.32339 | 2025-04-11 00:26:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 27.2 |
| eed206a3-496d-3caa-8112-e2a0b62d449b | -10.71391 | -42.31407 | 2025-04-11 00:26:00 | TERRA_M-M | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 15.9 |
| daf6f309-a232-30ba-a8a2-685b77cbbf19 | -9.62647 | -36.81645 | 2025-04-11 00:26:00 | TERRA_M-M | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 15.6 |
| a814dcf6-8908-36f1-a6ef-3544a0e5f33c | -6.3899 | -43.667 | 2025-04-11 00:27:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4a7cde55-3d14-3501-a540-716fbaab0c72 | -8.1099 | -43.116001 | 2025-04-11 00:27:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 35dd9afc-f651-3dc6-a424-30c558d3a4f9 | -21.0793 | -48.675701 | 2025-04-11 00:27:00 | METOP-C | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| cef0c7f8-e47a-34c0-82c7-6ceb578f1eed | -5.6319 | -38.2845 | 2025-04-11 00:27:00 | METOP-C | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 696eb2d9-2ca3-3004-b295-e3d42314558a | -9.546 | -40.3088 | 2025-04-11 00:27:00 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6394877e-0180-36cd-9edf-a00aa33cbb78 | -6.6641 | -47.603699 | 2025-04-11 00:27:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| f71b658f-ab42-3b6b-95fb-fc6ae0405330 | -21.0767 | -48.661201 | 2025-04-11 00:27:00 | METOP-C | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c4ea2f8b-da75-31b5-9d42-4f6937b735a2 | -5.6285 | -38.270599 | 2025-04-11 00:27:00 | METOP-C | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 61bea5aa-590d-38a5-b44e-f83dd99868f7 | -10.7243 | -42.325802 | 2025-04-11 00:27:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b61c9b4b-74d8-3d66-8ce0-9a203c9040f6 | -20.176399 | -51.125198 | 2025-04-11 00:27:00 | METOP-C | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 10c4476b-c607-3096-a855-e614923757e1 | -10.7226 | -42.318401 | 2025-04-11 00:27:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6ae0c3ea-af37-3670-861a-4e35570b1793 | -6.6624 | -47.595798 | 2025-04-11 00:27:00 | METOP-C | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 819a285e-544e-3132-afe0-a9b36dd06410 | -6.8455 | -42.782799 | 2025-04-11 00:27:00 | METOP-C | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 61d725ec-ed53-3a95-859a-7d721c9e8e68 | -6.372 | -43.6786 | 2025-04-11 00:27:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3f42ac23-0996-3a02-8eab-6d581d9518b5 | -10.7209 | -42.3111 | 2025-04-11 00:27:00 | METOP-C | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 6e779e21-85c0-3346-b17b-bbf5fe6b074f | -6.3736 | -43.685699 | 2025-04-11 00:27:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d1874941-36c2-34ca-a1e1-f181944a83c7 | -20.179899 | -51.145599 | 2025-04-11 00:27:00 | METOP-C | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| f9b51aa2-0cf7-339f-8a9d-715be3e4dd87 | -6.3752 | -43.692699 | 2025-04-11 00:27:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e880ead1-67ee-38c5-90ab-9e548afbd000 | -8.1115 | -43.1231 | 2025-04-11 00:27:00 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9e9ff7f3-8037-3ca1-bf29-5d0b6df5ea4b | -6.3818 | -43.676399 | 2025-04-11 00:27:00 | METOP-C | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dd39efb0-4148-3e5e-b29f-c5e4459a54db | -20.1833 | -51.1661 | 2025-04-11 00:27:00 | METOP-C | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 334ab71b-bf13-35b2-8e96-cb0b77bbead4 | -20.1896 | -51.143902 | 2025-04-11 00:27:00 | METOP-C | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0c7eb2ed-7fd5-3581-871c-9efaa9554733 | -6.38221 | -43.6684 | 2025-04-11 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5e867135-b175-3353-ab91-f21c4d23c4fb | -6.37583 | -43.68768 | 2025-04-11 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| eaaba0db-fbc9-3cc4-9c43-1cb6a6a4b9ac | -5.61873 | -38.27644 | 2025-04-11 00:28:00 | TERRA_M-M | IRACEMA | CEARÁ | Brasil | 2306009 | 23 | 33 | nan | nan | nan | Caatinga | 39.9 |
| d76c0104-56b0-376e-8d52-6136b5dfa5c2 | -6.36692 | -43.68896 | 2025-04-11 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 12.2 |
| bb6cc8c2-2cb8-38ca-9e9f-03db08e086ff | -6.38347 | -43.67739 | 2025-04-11 00:28:00 | TERRA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| fd2be1f2-1864-397b-94ff-9c44cf00a4e8 | -6.83812 | -42.78561 | 2025-04-11 00:28:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.9 |
| a1d930c6-38ef-34f0-bf03-179038290547 | -17.7593 | -56.299 | 2025-04-11 01:13:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| 161c72c5-a607-33b6-a3f4-17ee154a70dc | -20.5844 | -56.0369 | 2025-04-11 01:13:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 9f92ad7d-07ff-3b5a-94e6-969c8fe1ae87 | -20.190399 | -51.141399 | 2025-04-11 01:13:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c3185658-b6ba-3cbd-bb82-00884dd2f948 | -20.1852 | -51.161201 | 2025-04-11 01:13:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 592fd3d5-c09d-3341-9968-5e1da3eca75a | -17.761499 | -56.308102 | 2025-04-11 01:13:00 | METOP-B | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | nan |
| b7fcacc5-c05e-3610-8e02-698f33fa3367 | -20.1807 | -51.144299 | 2025-04-11 01:13:00 | METOP-B | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ad71ad66-6968-36c0-b13e-4f14526abab8 | -20.582399 | -56.028198 | 2025-04-11 01:13:00 | METOP-B | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| ca6a283b-2f9a-37b2-8846-d6a0ca463c5c | -5.66027 | -35.7534 | 2025-04-11 03:21:00 | NOAA-21 | BENTO FERNANDES | RIO GRANDE DO NORTE | Brasil | 2401602 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 68be8a82-82cd-3c28-90e8-69541ae88c8c | -11.91474 | -38.13402 | 2025-04-11 03:23:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| fb263ef5-a7f0-3667-aba5-60462e7fcb1f | -10.69506 | -37.04857 | 2025-04-11 03:23:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 86311dee-8580-31ec-85eb-f7f0c284e867 | -12.86071 | -38.36618 | 2025-04-11 03:23:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0056b677-accd-3be4-9bea-9e51f487e7fb | -8.1934 | -35.94885 | 2025-04-11 03:23:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ffbe2e16-e822-343c-9119-2f52e8877514 | -11.9145 | -38.13363 | 2025-04-11 03:23:00 | NOAA-21 | ENTRE RIOS | BAHIA | Brasil | 2910503 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 33f9719b-393e-3f8a-ab68-adb80d5a8509 | -6.83884 | -42.7854 | 2025-04-11 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 87e79a47-28dd-3c57-8fdc-e16e8c47cd91 | -10.97873 | -38.27505 | 2025-04-11 03:23:00 | NOAA-21 | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 45d66a57-3524-30b1-9923-edba4ce1ae0a | -6.83876 | -42.78687 | 2025-04-11 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 01cdfda4-ef7b-37ce-bed7-fbe8ee34b49b | -10.98129 | -44.4276 | 2025-04-11 03:23:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 989948a8-efbf-3da1-aa74-2b1c48581343 | -11.84775 | -38.20293 | 2025-04-11 03:23:00 | NOAA-21 | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5def1bce-b35b-322f-baa4-8db5f496bae8 | -11.90561 | -37.64201 | 2025-04-11 03:23:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 21457c7e-73f3-3219-8173-31f5a30f3873 | -11.90487 | -37.64076 | 2025-04-11 03:23:00 | NOAA-21 | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| ccc7a07b-fde7-36e6-862d-f9206b047ff4 | -11.06259 | -38.43897 | 2025-04-11 03:23:00 | NOAA-21 | RIBEIRA DO AMPARO | BAHIA | Brasil | 2926509 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a5164006-78e6-3be7-9ad4-0f41f6f821f5 | -12.86078 | -38.3668 | 2025-04-11 03:23:00 | NOAA-21 | SALVADOR | BAHIA | Brasil | 2927408 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 757fe928-a37a-320f-8fcb-26eb65444318 | -9.62601 | -36.81842 | 2025-04-11 03:23:00 | NOAA-21 | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af6ab4e7-33ef-3730-a3e3-a32138218a6f | -15.80451 | -43.57401 | 2025-04-11 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e394a33f-dd3c-3508-bb95-a40ed4e57317 | -15.80541 | -43.56971 | 2025-04-11 03:25:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 10.7 |
| e55155f0-a59b-3844-a49f-00d425627aa9 | -22.47434 | -48.36556 | 2025-04-11 03:28:00 | NOAA-21 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 20eab197-a27b-3d17-8b69-af102c0ab8ad | -21.62926 | -43.46746 | 2025-04-11 03:28:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| e7c4f1e7-aef9-3e9a-903a-e227754aac39 | -22.85757 | -42.98121 | 2025-04-11 03:28:00 | NOAA-21 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c7f8fbba-d0b4-33bd-9935-25480fde4f5f | -22.90174 | -43.75141 | 2025-04-11 03:28:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 54ff2cea-e0b8-38d1-8e61-195c17a052a2 | -21.08242 | -48.67013 | 2025-04-11 03:28:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 0f238225-06b6-3854-bb5a-82092cc6b5d6 | -21.07826 | -48.67562 | 2025-04-11 03:28:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 5fe62b1d-6291-34b1-8228-04517c778376 | -21.07545 | -48.66825 | 2025-04-11 03:28:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| 8a24cb1c-1427-304b-bf41-b4135fb6b8ee | -21.62415 | -43.46601 | 2025-04-11 03:28:00 | NOAA-21 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67a037d7-e024-36d4-90df-dbac5b5c0f24 | -21.08006 | -48.66862 | 2025-04-11 03:28:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.0 |
| ededb928-d9d9-3d35-88a4-e55957429ec7 | -6.38114 | -43.67363 | 2025-04-11 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 929edb47-f1d9-3fe3-af38-427bfe37eb7d | -6.38732 | -43.6652 | 2025-04-11 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 18abf800-9310-3183-a980-3a1d26eab9f1 | -6.37493 | -43.6822 | 2025-04-11 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 53de0538-b947-3ff7-8013-b885c434e5ba | -6.37412 | -43.68694 | 2025-04-11 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de1a1275-7547-32af-a584-eb1f4452d283 | -6.36951 | -43.68613 | 2025-04-11 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 82107da9-2c30-345e-af40-6b608716a8f5 | -9.34307 | -36.83475 | 2025-04-11 03:49:00 | NPP-375D | MINADOR DO NEGRÃO | ALAGOAS | Brasil | 2705309 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 35eacc2c-7f96-311b-8741-04986c99c728 | -9.84126 | -37.19756 | 2025-04-11 03:49:00 | NPP-375D | BELO MONTE | ALAGOAS | Brasil | 2700904 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 9c6b740c-c207-32b7-9dae-e59289efc43d | -10.65117 | -44.40767 | 2025-04-11 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3e6ad100-13a1-3df5-8479-45cbc868bfeb | -11.35108 | -37.42743 | 2025-04-11 03:49:00 | NPP-375D | SANTA LUZIA DO ITANHY | SERGIPE | Brasil | 2806305 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a4a8e432-9de1-31a2-a4ae-206d6c4c9400 | -6.66263 | -47.60183 | 2025-04-11 03:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| db1f89d3-9777-3fd6-a9b0-ee6d983b7b3a | -11.09126 | -41.0942 | 2025-04-11 03:49:00 | NPP-375D | VÁRZEA NOVA | BAHIA | Brasil | 2933158 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| fba000ba-00b5-31b1-9934-9a8e0ec75181 | -10.25964 | -39.57483 | 2025-04-11 03:49:00 | NPP-375D | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 82940546-0429-31e2-95b1-a15c94d521d0 | -6.83857 | -42.78363 | 2025-04-11 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 2966b53f-606a-3d06-858e-a340471acd40 | -6.84287 | -42.78436 | 2025-04-11 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f7ca650b-ebe2-3791-9c57-83e16401063b | -6.83789 | -42.78761 | 2025-04-11 03:49:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3979319c-b817-3586-b190-b0113ccd7fd8 | -9.2338 | -36.88614 | 2025-04-11 03:49:00 | NPP-375D | IATI | PERNAMBUCO | Brasil | 2606507 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 810956ad-7ddf-374b-b063-911a11983c18 | -6.66422 | -47.59298 | 2025-04-11 03:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 0.2 |
| d6e7fb58-b948-36df-afe2-df6d6f28af67 | -10.65566 | -44.40854 | 2025-04-11 03:49:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 3982753d-38bb-3268-8aeb-d0e894fbb196 | -9.62612 | -36.81826 | 2025-04-11 03:49:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 60dad504-669a-30da-a682-bf3082b63e6f | -11.84827 | -38.20122 | 2025-04-11 03:49:00 | NPP-375D | APORÁ | BAHIA | Brasil | 2901908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0406d6d4-8ee5-31f9-808e-9739625ef28a | -10.19223 | -37.22473 | 2025-04-11 03:49:00 | NPP-375D | GRACHO CARDOSO | SERGIPE | Brasil | 2802601 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 0792f2a6-3088-35e4-a055-f36a0b493b82 | -6.66344 | -47.59735 | 2025-04-11 03:49:00 | NPP-375D | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ea7709db-12ea-3007-84a4-447949381013 | -10.98042 | -38.27361 | 2025-04-11 03:49:00 | NPP-375D | ITAPICURU | BAHIA | Brasil | 2916500 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b039f9a-b884-351f-956f-0195d54a0938 | -12.63465 | -38.35883 | 2025-04-11 03:49:00 | NPP-375D | DIAS D'ÁVILA | BAHIA | Brasil | 2910057 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5695b98c-4e90-358a-8416-c3594d6e7fa6 | -9.62667 | -36.81474 | 2025-04-11 03:49:00 | NPP-375D | CRAÍBAS | ALAGOAS | Brasil | 2702355 | 27 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec479056-3497-3a7e-9f3f-48e06038001e | -7.96883 | -40.10579 | 2025-04-11 03:49:00 | NPP-375D | OURICURI | PERNAMBUCO | Brasil | 2609907 | 26 | 33 | nan | nan | nan | Caatinga | 0.4 |


[Clique aqui para ver as próximas entradas](README2.md)
