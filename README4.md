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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e12396d-74ef-33e1-b75f-29508665977b | -17.95898 | -42.50636 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 24c4edfa-b9e5-37d6-bd00-db1037615ac0 | -17.84756 | -42.30294 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| ce880897-cdf7-3cf8-9077-48d563c6f7a3 | -17.83246 | -42.32421 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 21.2 |
| af786898-1917-3462-b0ce-23657f99896c | -17.83117 | -42.31496 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| bcbcbb19-3224-3c99-9b87-2b813a33e04a | -17.82363 | -42.32563 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 40.9 |
| 5bcdf5c8-4858-3338-8cb9-ec3d5653ba11 | -17.73541 | -45.55403 | 2024-10-18 00:39:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b177f5d5-b90d-3c76-a5df-c625a4700b7e | -17.6336 | -42.34866 | 2024-10-18 00:39:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4bc3e81b-4f78-3719-a631-fccc666e223c | -17.63231 | -42.33944 | 2024-10-18 00:39:00 | TERRA_M-M | CAPELINHA | MINAS GERAIS | Brasil | 3112307 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 8885dc2b-d7cd-3f61-8492-2414228bdf75 | -17.58119 | -41.97844 | 2024-10-18 00:39:00 | TERRA_M-M | NOVO CRUZEIRO | MINAS GERAIS | Brasil | 3145307 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 773c8516-8415-3ebf-b8bb-0c9856d6a534 | -17.56116 | -41.91196 | 2024-10-18 00:39:00 | TERRA_M-M | LADAINHA | MINAS GERAIS | Brasil | 3137007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 3c472c75-9b56-3d16-9b3c-29378bfeadd0 | -17.46009 | -42.89369 | 2024-10-18 00:39:00 | TERRA_M-M | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 9.5 |
| a325cdea-545c-341b-9030-0739999690d5 | -17.19564 | -45.48049 | 2024-10-18 00:39:00 | TERRA_M-M | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 63373c36-90d0-3af8-87cc-1c2072ea0139 | -17.19421 | -45.46925 | 2024-10-18 00:39:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 77.9 |
| af61954e-a1d8-3beb-a574-d4a9ca1daca3 | -17.19277 | -45.45797 | 2024-10-18 00:39:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 7a2c12f5-d40d-388a-8af9-d17e56a38c8a | -17.18448 | -45.47058 | 2024-10-18 00:39:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 7d96d0d7-1605-387c-b7da-699d5cf2631b | -17.18306 | -45.45932 | 2024-10-18 00:39:00 | TERRA_M-M | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| c23a6aa4-e780-3d2b-a3b6-2a1e58dad6bd | -15.58706 | -42.94154 | 2024-10-18 00:39:00 | TERRA_M-M | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 763acd19-6ca3-35f2-bcc1-95bf01495b37 | -15.20025 | -44.00592 | 2024-10-18 00:39:00 | TERRA_M-M | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 0557f2e4-a439-3fd9-bd9f-909622665d07 | -14.98484 | -44.45932 | 2024-10-18 00:39:00 | TERRA_M-M | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 806a769b-a138-3b6b-bc23-e348a52af28d | -23.13583 | -45.54842 | 2024-10-18 00:39:00 | TERRA_M-M | TAUBATÉ | SÃO PAULO | Brasil | 3554102 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.2 |
| 4305efa0-1a2d-3735-9b4a-150851b0e39d | -5.87181 | -40.17645 | 2024-10-18 00:41:00 | TERRA_M-M | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 13.3 |
| 098ff36a-8119-3e9f-abc5-1ebdbe8589ac | -9.42481 | -35.80156 | 2024-10-18 00:41:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.3 |
| 49ee10cc-ab07-3045-ba16-128b8efd2edf | -9.42311 | -35.79533 | 2024-10-18 00:41:00 | TERRA_M-M | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 52.5 |
| 62ea2c74-4e94-3386-9512-3490f943e206 | -7.77652 | -35.08018 | 2024-10-18 00:41:00 | TERRA_M-M | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 43.4 |
| 648defdc-40be-3add-a6bc-b09dd7fcedea | -7.77003 | -35.08649 | 2024-10-18 00:41:00 | TERRA_M-M | ARAÇOIABA | PERNAMBUCO | Brasil | 2601052 | 26 | 33 | nan | nan | nan | Mata Atlântica | 65.2 |
| 905c2a91-9aef-372c-8a14-d30efb18612f | -6.7486 | -39.2612 | 2024-10-18 00:41:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 5a9969f7-fc89-3009-a883-4d1326e1317f | -6.54192 | -43.04391 | 2024-10-18 00:41:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 59f4f72a-3bb1-3705-bda6-936815a4f3ca | -6.54053 | -43.03417 | 2024-10-18 00:41:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 1b319f7c-0e9b-3c7d-be6c-016ed2a9d8fa | -5.94706 | -39.6797 | 2024-10-18 00:41:00 | TERRA_M-M | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 24.3 |
| 641ee743-3576-3177-8731-eb18c6d0cf6c | -5.94583 | -43.38972 | 2024-10-18 00:41:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Caatinga | 4.4 |
| 62905cd6-ec0c-33b9-aac8-b5892c7c8294 | -5.51099 | -43.70373 | 2024-10-18 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 3bfc00ef-0e7c-30d5-90f5-efa7bab1e4c8 | -5.50193 | -43.70504 | 2024-10-18 00:41:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 46ddbe85-a778-3c00-85f2-e10c95b9b7db | -5.30195 | -43.08525 | 2024-10-18 00:41:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8f8fbe9f-d392-30a9-a5ff-916aaea66f36 | -5.30052 | -43.07533 | 2024-10-18 00:41:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 9cbd7fa7-6a34-3f13-928b-94f5340c534a | -5.29263 | -43.08657 | 2024-10-18 00:41:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 674519b1-b64a-3452-9b8d-d2014cbfa953 | -5.29119 | -43.07666 | 2024-10-18 00:41:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 587ad911-b261-365c-bf23-6466a4323f26 | -5.21602 | -43.19393 | 2024-10-18 00:41:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.6 |
| f4c692e0-bfcb-32c3-881e-4fba88528dda | -5.2146 | -43.18414 | 2024-10-18 00:41:00 | TERRA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 3e74598c-5951-3d67-b334-a470d1b8ce01 | -5.21287 | -43.81269 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 16.4 |
| 73d22375-aadb-3065-9475-9623621c9160 | -5.21155 | -43.80342 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 481db414-e0b6-3fd5-a0da-0a726f785363 | -5.04356 | -43.65871 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1ba58c93-8cb3-3a3b-8463-da7bf5a1ee06 | -5.03446 | -43.66005 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d661abf7-d2b4-3266-a01d-e5d32c087f2b | -5.02535 | -43.66137 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| fa03f85c-a80a-358c-90aa-fc1fc4d57b4f | -5.00406 | -43.96477 | 2024-10-18 00:41:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| c52123f7-ab24-33f4-af99-91637446f8e2 | -4.94126 | -43.00905 | 2024-10-18 00:41:00 | TERRA_M-M | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b785006e-bef0-3de2-94e7-83e998a08099 | -4.48239 | -42.88787 | 2024-10-18 00:41:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.3 |
| 1d9dfc11-d9bd-3da6-92ed-6585906fb203 | -4.48091 | -42.8775 | 2024-10-18 00:41:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| ec771f4d-a255-37dd-ba05-ad5fbf3c1c6f | -4.24218 | -41.92845 | 2024-10-18 00:41:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 054282ef-3ebb-3478-9594-67fa2132d501 | -4.24046 | -41.91656 | 2024-10-18 00:41:00 | TERRA_M-M | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| a23418e1-614b-3438-8437-03ba78f3b381 | -4.17898 | -42.97155 | 2024-10-18 00:41:00 | TERRA_M-M | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 7677304d-1999-33c6-ac15-78d5c5a9f3ca | -5.76168 | -45.55591 | 2024-10-18 00:41:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 43508617-1562-3aa2-add8-d35c4838e027 | -5.63029 | -44.95047 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6bfc7a40-10a1-33aa-b6b7-2bd8659f9df0 | -5.57753 | -44.89502 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fd207e58-6406-379e-bbc7-f01784b0062e | -5.57629 | -44.8862 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 47.1 |
| b32281d3-24cd-30fd-b1c9-68b0dee68a76 | -5.57506 | -44.87738 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a64ef61c-c4b4-350d-b899-dd27944eee69 | -5.43066 | -44.63317 | 2024-10-18 00:41:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 745b48bb-c4bd-3a07-93e3-a901db51638d | -5.42181 | -44.63444 | 2024-10-18 00:41:00 | TERRA_M-M | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 5bf29c88-6f5d-3a6f-8fec-d57e4fd82f2f | -5.31199 | -45.16669 | 2024-10-18 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 969fdb92-7607-3336-bda3-41804d28c852 | -5.24594 | -44.17854 | 2024-10-18 00:41:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 150a89ff-7675-384c-a4a1-482e08c20a4c | -5.24466 | -44.16946 | 2024-10-18 00:41:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| d597ff5c-51c4-3627-afa0-5dd78cc9418c | -5.22975 | -45.5773 | 2024-10-18 00:41:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 41.2 |
| f765a8b4-9a04-3645-ac53-253584cd8267 | -5.22852 | -45.56845 | 2024-10-18 00:41:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| ac477be3-c875-35b9-afaa-127a212d81c2 | -5.22409 | -45.06869 | 2024-10-18 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2043e316-3533-3df3-b1e2-f5b14d4a82e1 | -5.21527 | -45.06995 | 2024-10-18 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 85bccad7-8ceb-383e-9013-dbf0cb0fd8b6 | -5.20991 | -50.07735 | 2024-10-18 00:41:00 | TERRA_M-M | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| e81b5701-8c89-3daa-81b2-ed9b1fc7f5ec | -5.20862 | -44.76473 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 149f8358-9fed-310a-a751-f0014dce3b99 | -5.1922 | -45.50152 | 2024-10-18 00:41:00 | TERRA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a3663dbb-d88c-3405-a72f-bdbf46f6496e | -5.17601 | -44.66091 | 2024-10-18 00:41:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e26ad2d3-15bb-358d-b2d2-a1b8c67cf5a6 | -5.15752 | -44.33571 | 2024-10-18 00:41:00 | TERRA_M-M | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 8fb6ba8c-3c74-34e9-944a-2a8ac7cec4ed | -5.14409 | -46.09246 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 9.4 |
| b9ac3bec-6a71-3218-b267-69f3daeb4b6e | -5.14284 | -46.08347 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8dbaf789-4977-3651-8bd6-981a52255571 | -5.09126 | -44.25319 | 2024-10-18 00:41:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 950e34a2-7711-366f-b220-27927f046f43 | -5.08343 | -44.93006 | 2024-10-18 00:41:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fe2a6a75-dbc1-30fe-9dc2-8f7c5203618e | -5.08091 | -44.25134 | 2024-10-18 00:41:00 | TERRA_M-M | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 50eb05f7-7d59-3af1-a2b9-a4242bac292b | -5.07271 | -45.11142 | 2024-10-18 00:41:00 | TERRA_M-M | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| a0324846-3311-3bbf-9a59-984346b15b87 | -5.04197 | -45.87858 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 671e5f47-f6f4-3d87-ab6f-e754812e49a4 | -5.02071 | -45.52896 | 2024-10-18 00:41:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3efe7273-8e95-3bd9-8a47-e7f1a90a77e5 | -4.99448 | -45.4697 | 2024-10-18 00:41:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 542bebfa-3c18-3728-b31a-7e14ff3960de | -4.98718 | -46.48844 | 2024-10-18 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f14d56d3-378e-35f1-a091-0afeabb6adf0 | -4.97944 | -46.49896 | 2024-10-18 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 5bf4662c-709a-3aee-9617-0f87308526e3 | -4.97816 | -46.48965 | 2024-10-18 00:41:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| bdc82a4c-6f67-3360-a3e4-d7deb2c5ca88 | -4.95946 | -47.02556 | 2024-10-18 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 13974481-c487-3da0-b932-5b6cf474569e | -4.95715 | -45.67054 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cd0c2785-2ab4-3059-8811-bfb6bcb51ea0 | -4.95593 | -45.66171 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 32.1 |
| 7441abc5-f650-3470-89de-797c5c3f83c6 | -4.95025 | -47.02681 | 2024-10-18 00:41:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 31.0 |
| 493913b8-0665-3e09-b873-1b7dffbb6c12 | -4.94708 | -45.66296 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 22503259-4d07-3a05-84a9-7b26c9b0eb14 | -4.90476 | -45.8918 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9c9c3253-8055-3d7f-8fcb-ebfeafb11d80 | -4.90353 | -45.88294 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1bbfb1a5-c1c2-3a7e-9502-9ef69d8bf04d | -4.89959 | -45.91981 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.8 |
| d31e1ea8-1fa6-3b61-abc1-d67f10e58209 | -4.89194 | -45.93 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0adfd7dd-a233-3a9c-8f5f-4877e7556c81 | -4.89071 | -45.92105 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.7 |
| d726996f-4747-3943-808e-bf580cd6e109 | -4.88506 | -45.74969 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d2f26247-aa01-32fc-9645-4a5335ef27b5 | -4.81224 | -46.0206 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3a5aa429-eff9-3b9f-aa73-eb5fd7fbcde8 | -4.811 | -46.01159 | 2024-10-18 00:41:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ef852949-fb8d-37b4-8eb7-4762750684d1 | -4.78565 | -45.69788 | 2024-10-18 00:41:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 375a7e83-e3c2-3081-82af-0a6d295ae66a | -4.70659 | -44.93618 | 2024-10-18 00:41:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c4a15134-f938-3509-937e-f308ade88ec8 | -4.70536 | -44.92735 | 2024-10-18 00:41:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 1a9059b1-3a4e-398a-bb8f-ff3126b5dd4b | -4.69489 | -44.12724 | 2024-10-18 00:41:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e9e02c73-a5a3-380b-b1f6-64db62a8f837 | -4.6859 | -44.12851 | 2024-10-18 00:41:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| d3e73443-1247-3d34-852a-4bd5c1885445 | -4.66389 | -46.34725 | 2024-10-18 00:41:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 14.6 |


[Clique aqui para ver as próximas entradas](README5.md)
