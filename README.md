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
| a4bc1288-91ac-3b2a-a053-d9a71dd59314 | -19.3292 | -40.8947 | 2025-12-29 00:00:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 76.5 |
| c91f1d24-26ed-3b44-abca-7cfed03bccff | -19.3497 | -40.8888 | 2025-12-29 00:00:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 5a7147cb-12de-38e1-ba4e-3fa12efc2d60 | -6.7797 | -35.186199 | 2025-12-29 00:09:00 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54b99d12-f183-323c-a1c7-01e9837b31c1 | -13.6975 | -45.510399 | 2025-12-29 00:09:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bc7b0b35-03cd-3141-a49a-9648a8e4ed07 | -13.6563 | -43.723701 | 2025-12-29 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d5f46271-9605-399b-bf71-bfd6e37f1083 | -9.7741 | -37.733601 | 2025-12-29 00:09:00 | METOP-C | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| e710f8c5-2ffb-371f-a713-395a340715da | -10.1782 | -39.0494 | 2025-12-29 00:09:00 | METOP-C | CANUDOS | BAHIA | Brasil | 2906824 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| af67a003-be67-3ef9-b135-a26026450d2b | -8.5306 | -40.791199 | 2025-12-29 00:09:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 1dd2d9d3-e611-31f9-8e4d-bc1b9f6aa134 | -13.6587 | -43.735298 | 2025-12-29 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f5ae98d7-042c-33e5-b19b-b47b53a2e59f | -13.5219 | -43.5135 | 2025-12-29 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 257d989a-c899-3871-a6b6-2688c1f8ae20 | -3.2112 | -43.452999 | 2025-12-29 00:09:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29a60937-41fc-3aac-93de-a78d47128dad | -13.4697 | -44.008801 | 2025-12-29 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e6e1bf6e-9c10-3e48-9d42-011932ca7126 | -13.4721 | -44.020901 | 2025-12-29 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 1fb00506-d561-3b13-a935-d039419831d1 | -11.7532 | -44.578899 | 2025-12-29 00:09:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a439b17-4cd2-39e4-a0e7-640c5d561a62 | -7.6107 | -39.9991 | 2025-12-29 00:09:00 | METOP-C | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 2d612074-e858-325d-9a8e-090b1a1647bd | -6.0782 | -40.4217 | 2025-12-29 00:09:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 11a89452-d833-39cd-a09e-257b4cd7f8f8 | -3.2131 | -43.461201 | 2025-12-29 00:09:00 | METOP-C | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c4211275-806a-3016-b1f7-88215db7ad05 | -20.931601 | -43.317799 | 2025-12-29 00:09:00 | METOP-C | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| c8885dcc-30e6-3d8a-95a6-0db8dd54b3c1 | -3.8454 | -41.934502 | 2025-12-29 00:09:00 | METOP-C | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b6f97d50-e9dc-33f2-9397-bbaa114e018c | -13.7073 | -45.508499 | 2025-12-29 00:09:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2fb738b6-9dcf-31c4-a036-755f25d1c522 | -6.7774 | -35.176498 | 2025-12-29 00:09:00 | METOP-C | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 40bfa499-3c06-3726-b9b7-5af82bbe9130 | -5.2808 | -45.826302 | 2025-12-29 00:09:00 | METOP-C | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 123bb7ea-ebef-37f0-bad0-1e1506bad91e | -6.0797 | -40.4286 | 2025-12-29 00:09:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fb519e02-5ed1-3a25-b242-1537f5e3dd70 | -5.9832 | -44.596199 | 2025-12-29 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5d545d20-bed3-30a6-b1bb-2b3f06ab751b | -4.422 | -43.119202 | 2025-12-29 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 7106b3f2-6c16-3ac1-a085-7c485dae697c | -4.43 | -43.109001 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4368ecd6-6988-3743-8963-29738452af95 | -4.4318 | -43.117001 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fbc842c9-39cc-3a55-a691-d083bf9f803a | -3.8558 | -42.2528 | 2025-12-29 00:09:00 | METOP-C | ESPERANTINA | PIAUÍ | Brasil | 2203701 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e641518f-6d19-3465-9385-ded05db8ac59 | -22.5235 | -44.313599 | 2025-12-29 00:09:00 | METOP-C | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8775f247-2f74-336f-b57d-cf960bfe655a | -6.0766 | -40.414902 | 2025-12-29 00:09:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 720e983d-5d5b-3e99-ab17-e6d9a7722fd2 | -5.8538 | -40.341702 | 2025-12-29 00:09:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 61640971-9679-3bca-9834-860e0389c29c | -4.6045 | -43.336399 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c154a359-5b70-30cd-ba1a-47e9a5c1a296 | -20.929001 | -43.3036 | 2025-12-29 00:09:00 | METOP-C | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 54a16517-d9de-35b0-828f-085f4ed03dac | -4.5928 | -43.330299 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3c086af4-5425-38c7-a191-cdae9db86cd4 | -5.981 | -44.585999 | 2025-12-29 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3938c571-07a4-3de7-8ce2-567f5091f59d | -5.9951 | -43.443001 | 2025-12-29 00:09:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d3d4388d-bf12-359a-9e81-a8d92883145a | -13.7103 | -45.5238 | 2025-12-29 00:09:00 | METOP-C | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8666b2c3-8537-3e4d-98ef-22671bb16dd8 | -7.6122 | -40.006001 | 2025-12-29 00:09:00 | METOP-C | BODOCÓ | PERNAMBUCO | Brasil | 2602001 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 8a125030-5670-39f5-ad79-43fe16c6da05 | -13.5196 | -43.5023 | 2025-12-29 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0171cde3-14b5-38d0-962e-4e005454e517 | -11.7459 | -44.5933 | 2025-12-29 00:09:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 90a65a25-1d28-3cda-9fb8-f6b0591ac017 | -4.5947 | -43.3386 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33e5b516-c774-340b-8223-e7af2a2ff4be | -9.7725 | -37.726501 | 2025-12-29 00:09:00 | METOP-C | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | nan |
| 4d21351d-de7c-3dda-9e2b-d56bba4fd52d | -8.5322 | -40.798401 | 2025-12-29 00:09:00 | METOP-C | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 6b53113c-e5eb-3964-972f-e12b1d85e56a | -2.8708 | -45.497799 | 2025-12-29 00:09:00 | METOP-C | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 175fc124-47ad-3eed-b69d-d0f62a3d5e66 | -6.6338 | -39.106998 | 2025-12-29 00:09:00 | METOP-C | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7a8bd605-a61b-3011-927c-f5b07d589f08 | -4.6026 | -43.328098 | 2025-12-29 00:09:00 | METOP-C | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9e9ea430-f286-3896-89df-7d633507517b | -5.8554 | -40.348598 | 2025-12-29 00:09:00 | METOP-C | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 1e528ded-490f-32d3-a110-49dbf7ef92e0 | -11.9623 | -44.209 | 2025-12-29 00:09:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 5be27276-e7b4-3d19-bd7a-99892843b32c | -5.997 | -43.451801 | 2025-12-29 00:09:00 | METOP-C | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5445b68c-54b0-3dfe-b330-5628f61ec576 | -5.5257 | -40.530499 | 2025-12-29 00:09:00 | METOP-C | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 6004dc82-bbed-33e8-8bdc-f35bb84a5a51 | -5.9712 | -44.5881 | 2025-12-29 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 01c0af7c-e387-3884-8029-f387aa0fc41b | -11.7557 | -44.591301 | 2025-12-29 00:09:00 | METOP-C | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ab477f46-e6af-3e28-8d61-8048976d9073 | -19.3497 | -40.8888 | 2025-12-29 00:10:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 79.4 |
| d0e50f48-2d9f-3d62-b2b3-b1d50c23dc91 | -19.3292 | -40.8947 | 2025-12-29 00:10:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 89.2 |
| 92c5f4bd-f1fa-3faf-af4f-22460d4c0603 | -19.3497 | -40.8888 | 2025-12-29 00:20:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 5843c74a-c805-3eea-9b6a-81bb39475478 | -19.3292 | -40.8947 | 2025-12-29 00:20:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 100.6 |
| 8cabfd64-44e8-325c-981d-98694be218f5 | -22.52249 | -44.31605 | 2025-12-29 00:26:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| ebe85506-c658-3e58-8a9e-00e2bafa62db | -19.32868 | -40.88847 | 2025-12-29 00:26:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 59.5 |
| 0c9df4bd-f8f5-32fc-93ed-6c29834af9d5 | -19.33871 | -40.88023 | 2025-12-29 00:26:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 56.1 |
| f4ff6387-a20c-32b5-baab-4ab53e769cb2 | -19.33231 | -40.90921 | 2025-12-29 00:26:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 34.7 |
| d64ad41c-9023-3a27-a6ca-7ea082192ce2 | -20.92428 | -43.30632 | 2025-12-29 00:26:00 | TERRA_M-M | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.0 |
| 8b243718-4c6e-348c-ad7f-2557f56af3e8 | -19.34229 | -40.9 | 2025-12-29 00:26:00 | TERRA_M-M | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 90.2 |
| f049c163-a803-3f7d-9e9b-37d6c096d24a | -20.93111 | -43.31275 | 2025-12-29 00:26:00 | TERRA_M-M | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.1 |
| 14b3aa7f-4730-3a20-b6dd-50ed084e7c61 | -20.92881 | -43.29907 | 2025-12-29 00:26:00 | TERRA_M-M | CIPOTÂNEA | MINAS GERAIS | Brasil | 3116308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 2ee55b23-9ebd-3e7a-b931-d2afdcc1a855 | -22.52067 | -44.30451 | 2025-12-29 00:26:00 | TERRA_M-M | BARRA MANSA | RIO DE JANEIRO | Brasil | 3300407 | 33 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| eb262e12-ff79-302d-b613-166fb2f25b9e | -13.52673 | -43.5125 | 2025-12-29 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 0f76482a-186f-38d8-9aaa-6253565600a9 | -18.73545 | -48.03499 | 2025-12-29 00:28:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9cccd6ee-6069-3a31-b218-1d6f1c307413 | -13.46779 | -44.00683 | 2025-12-29 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 23.8 |
| 4c8cfa9f-6809-397d-b24c-9a753b0acf6f | -13.65416 | -43.72773 | 2025-12-29 00:28:00 | TERRA_M-M | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 14.8 |
| db6076d0-4acb-36f4-8130-6cd0e7973302 | -14.03641 | -46.64812 | 2025-12-29 00:28:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 19fc3ea6-4d8e-3144-8d14-f496ffe6411d | -15.13425 | -45.29501 | 2025-12-29 00:28:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ab7dbb14-35ea-3934-b21b-73eeda1710f2 | -19.77645 | -46.22577 | 2025-12-29 00:28:00 | TERRA_M-M | PRATINHA | MINAS GERAIS | Brasil | 3153004 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3ed96cdf-bac7-383a-a429-2fc971c2f5a0 | -13.7131 | -45.51722 | 2025-12-29 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 6d88d86f-e26b-334d-a70a-a46cf8c45248 | -15.13237 | -45.28277 | 2025-12-29 00:28:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.8 |
| f92c8cf1-ad0d-3b59-8a83-f3d58cd8dd6e | -17.6171 | -46.65991 | 2025-12-29 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8928b510-b680-31d6-9fad-a80c315e9d14 | -13.71124 | -45.50485 | 2025-12-29 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 414d6e0b-5eb9-3491-a5e7-9997fb3389ca | -13.47308 | -44.02888 | 2025-12-29 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 4be65460-073c-3a26-bf26-ac9128633cf3 | -13.7029 | -45.51892 | 2025-12-29 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 1d371cde-4748-3c64-b8d8-638b84bb968a | -18.73417 | -48.02573 | 2025-12-29 00:28:00 | TERRA_M-M | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 10.8 |
| 6c985c9a-2015-3a9d-9321-f56a38d5a36a | -13.48191 | -44.02106 | 2025-12-29 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 437e1a4e-1e0b-38f3-95c1-2e3cbda5b06b | -17.60799 | -46.6614 | 2025-12-29 00:28:00 | TERRA_M-M | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 273d6c0e-936f-3f07-840f-3538a4e14fba | -17.28993 | -41.82792 | 2025-12-29 00:28:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 109.4 |
| dfbeded4-49a2-30e0-9f4d-6a6bc31d7c0e | -13.47043 | -44.02279 | 2025-12-29 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 33.1 |
| 7e7e8a13-1249-384e-91a3-53b7f1eb55f4 | -13.71049 | -45.51145 | 2025-12-29 00:28:00 | TERRA_M-M | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 3f3a29fc-b23e-3f0e-b2f1-4533d44cfbbd | -13.47056 | -44.0129 | 2025-12-29 00:28:00 | TERRA_M-M | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 5d65ae21-f735-33eb-ac08-1c58c98d85f6 | -14.03486 | -46.63766 | 2025-12-29 00:28:00 | TERRA_M-M | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| e5f357a5-e57e-3db8-9ab7-54d60b166289 | -19.3292 | -40.8947 | 2025-12-29 00:30:00 | GOES-19 | BAIXO GUANDU | ESPÍRITO SANTO | Brasil | 3200805 | 32 | 33 | nan | nan | nan | Mata Atlântica | 86.7 |
| 79718663-b23a-314d-882c-c3c03dddf79d | -6.5227 | -35.1118 | 2025-12-29 00:30:00 | GOES-19 | MATARACA | PARAÍBA | Brasil | 2509305 | 25 | 33 | nan | nan | nan | Mata Atlântica | 74.5 |
| fa7e3e7f-361d-34c2-9fe5-e53355480e68 | -10.0448 | -36.3475 | 2025-12-29 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Caatinga | 72.0 |
| 2390c85f-cd83-3909-ae8f-4b1724e07f13 | -12.66969 | -46.76172 | 2025-12-29 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.1 |
| d486a840-01ba-3c1f-a552-2121655a140c | -12.67128 | -46.77245 | 2025-12-29 00:30:00 | TERRA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 92e2ca51-cacd-3478-b226-02c3b7b91d26 | -11.75247 | -44.5952 | 2025-12-29 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 6c69384e-7f6f-34e0-a3e4-0a0a224fecb9 | -5.28452 | -45.8228 | 2025-12-29 00:32:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 099403cc-1a04-3be0-a63b-2e47e2038d09 | -3.94915 | -50.73404 | 2025-12-29 00:32:00 | TERRA_M-M | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 355cd1b5-b94a-35c9-a3a8-5f6f217da386 | -5.9896 | -44.60029 | 2025-12-29 00:32:00 | TERRA_M-M | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| f3bccb6c-e788-3e3e-82bf-dcdb117a240c | -7.70322 | -55.20901 | 2025-12-29 00:32:00 | TERRA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| a1531386-8f8f-3b8e-9326-dc18345770e7 | -3.59416 | -53.23997 | 2025-12-29 00:32:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 3300fd6b-a297-3ab7-8e19-5f4d3606730d | -3.94872 | -50.4563 | 2025-12-29 00:32:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2e69a6f2-3591-3eb8-a2a1-fb9a76517d0d | -3.74255 | -49.7099 | 2025-12-29 00:32:00 | TERRA_M-M | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 43a5dcd1-5eef-3155-9aba-f2976e0eb293 | -5.28693 | -45.83871 | 2025-12-29 00:32:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |


[Clique aqui para ver as próximas entradas](README2.md)
