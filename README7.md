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
| 1fc1d88e-0333-3ebf-a841-eb3cfa310e23 | -22.48084 | -49.1319 | 2025-11-26 03:34:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e02c5d5e-66bb-351c-b3a1-11041784ca5e | -20.57908 | -45.86761 | 2025-11-26 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aaddb3df-a35e-31c4-abab-83581aae07e0 | -20.5814 | -45.8835 | 2025-11-26 03:34:00 | NOAA-21 | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 801a56a1-71f0-37f4-9ba4-5844bec3162a | -22.47387 | -49.13211 | 2025-11-26 03:34:00 | NOAA-21 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 39538eda-51ee-3a13-992d-eff77fc3a637 | -18.94472 | -49.30079 | 2025-11-26 03:34:00 | NOAA-21 | ITUIUTABA | MINAS GERAIS | Brasil | 3134202 | 31 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2b80520-5176-32b0-bdb1-bdf78219abf3 | -4.65293 | -43.96715 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1c98c2dd-1ea1-36f6-bce1-cbaca9ce2c40 | -4.14467 | -43.64842 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3707f38a-2dcf-3c2c-9b99-fe8855506c6b | -6.59437 | -44.32228 | 2025-11-26 03:57:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0ea6b4f6-69c8-3c63-8208-e08a0c90450e | -4.52788 | -46.42981 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 825e88e4-c44e-34a0-88ad-375d990bb23f | -6.16648 | -39.51445 | 2025-11-26 03:57:00 | NPP-375D | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 91711d8b-06a5-3bd0-918a-24eebd9084e8 | -4.17312 | -43.71447 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4e92772b-682e-37fc-8f1c-ef02663575b3 | -4.25099 | -48.56887 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dd7b9b28-896f-3d49-94a3-690f113f986d | -4.70701 | -43.98873 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5c500433-7eda-33ee-b5ae-ce0fcaa3cb2a | -5.32416 | -44.82734 | 2025-11-26 03:57:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| da234615-fad3-36fa-9fe2-6ddc9590e2e3 | -5.64506 | -47.8616 | 2025-11-26 03:57:00 | NPP-375D | AUGUSTINÓPOLIS | TOCANTINS | Brasil | 1702554 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57f10b06-dae2-35cd-b712-11002e97c61c | -4.72711 | -46.46092 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9e09703a-2117-3172-8bed-b874fe033a14 | -4.54121 | -45.56557 | 2025-11-26 03:57:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 04875f7e-addc-39a0-8712-451201fbf97a | -4.70635 | -43.99277 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 669b5693-a62f-369a-b2db-1b3803737556 | -4.6559 | -43.97595 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 6cd98188-b77a-3aca-b631-126c7ef4969e | -6.50323 | -38.84681 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 3757851c-1079-3897-a71b-b57e35236b69 | -6.76833 | -46.51468 | 2025-11-26 03:57:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 543496e5-dc53-3ac3-a0db-a30958c168d9 | -4.16553 | -43.73384 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 285e5bb3-6591-3bf7-8902-3622deb7ac2d | -4.2574 | -45.12415 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b745d1bc-8ede-3945-9013-519206a21acb | -3.46028 | -50.5468 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 547affa6-5417-3b37-807e-58cdebd02420 | -4.57011 | -38.29141 | 2025-11-26 03:57:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5b9ad86b-6928-3cb9-ab5d-3dc45e36928c | -5.17699 | -35.70803 | 2025-11-26 03:57:00 | NPP-375D | SÃO MIGUEL DO GOSTOSO | RIO GRANDE DO NORTE | Brasil | 2412559 | 24 | 33 | nan | nan | nan | Caatinga | 3.6 |
| daaae18a-7046-3abb-8f00-4991da78e1a5 | -4.16486 | -43.73787 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| d5e0368c-866c-3d89-8007-eb27ba4b1c4f | -6.0607 | -43.25622 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 77dc1f7d-d594-3df1-b4f5-70319c932a23 | -2.49877 | -47.83125 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a4cca1e4-d0e9-3c3b-b19b-7de18497bb3e | -3.39616 | -47.18998 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c23166eb-c10f-39b3-95c5-c866c51fc4ea | -7.05656 | -38.857 | 2025-11-26 03:57:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 47f9af8e-a379-3145-b3b5-37e112c126da | -3.60643 | -40.44036 | 2025-11-26 03:57:00 | NPP-375D | MERUOCA | CEARÁ | Brasil | 2308203 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f315f8dd-17e6-3beb-939e-6d23f5b36708 | -4.65225 | -43.97123 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f07c73ae-ff88-3dce-b090-4b69287f000c | -4.10287 | -49.06824 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2bcd982c-7190-3076-be68-4ec7c98e1f01 | -3.18153 | -48.62027 | 2025-11-26 03:57:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ef37bc4-76cd-361d-a000-320286539bd3 | -5.27359 | -43.64148 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 177d4aaf-c7b3-37d9-af21-e58bbe178ca2 | -3.67258 | -38.80811 | 2025-11-26 03:57:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81fb2033-589b-3a76-ab78-7970702bef31 | -4.70137 | -43.99607 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ca5ec5d2-b28d-3941-a805-9c8824e7de16 | -6.04646 | -45.83465 | 2025-11-26 03:57:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f24018dc-a11a-305a-a8c2-5da202826c07 | -3.47372 | -43.42316 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e1ebc9b-833f-30dd-9cd8-ae9b513803d1 | -4.09672 | -49.06736 | 2025-11-26 03:57:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99f9c685-cd22-36be-957e-84bf63f6f1d1 | -6.30383 | -43.78859 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 3e5f9127-1041-3588-94f3-d82ea81a2730 | -5.98621 | -44.60025 | 2025-11-26 03:57:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 64174806-0017-3a90-b9a4-3b2cd7a4ec41 | -4.14168 | -40.45447 | 2025-11-26 03:57:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8d46fdf2-bb88-3ffa-bb9d-f63345b69a0f | -6.06531 | -43.25336 | 2025-11-26 03:57:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07878489-be32-3f33-bd03-c49682ad58f9 | -7.17998 | -44.98311 | 2025-11-26 03:57:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5ccc3f15-eccb-3273-83f8-4d23127f83da | -3.92531 | -49.21629 | 2025-11-26 03:57:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e4cf3235-c6b0-3df7-baea-74452225707c | -2.48785 | -47.82524 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7091dc4-163b-3002-9c2f-78670eac1f62 | -4.16619 | -43.72982 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| fec9c151-c663-3b9e-92e9-6a9771ba396a | -3.45925 | -50.55276 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4d155cbf-b33c-3045-bdf4-b1be8d5a1c78 | -5.2351 | -45.42678 | 2025-11-26 03:57:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bf35c4fa-8917-34f9-80e9-6370d52cb7cc | -4.28376 | -47.31009 | 2025-11-26 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d61cbf57-b63b-38a9-bfaa-a633df7a0e23 | -7.05601 | -38.86047 | 2025-11-26 03:57:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b11bdc8f-107d-3d09-86c3-fb5ada736ecd | -3.13376 | -49.39959 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b086e56a-b7fc-3ed8-9453-d212ff01e727 | -4.65954 | -43.9807 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 396a94f3-bcdc-3324-98f5-e801a22517c1 | -2.48067 | -47.83236 | 2025-11-26 03:57:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b8d1868c-a978-3d3f-8051-ab6b3d7922e6 | -5.90388 | -44.00983 | 2025-11-26 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f49c5ab-12a7-375d-a167-ea10415f6d89 | -4.71066 | -43.99353 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 31296657-f349-3519-b968-f993080879ab | -5.21223 | -42.90308 | 2025-11-26 03:57:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 6b58bbcd-ae41-3668-9827-3ca5011c7a69 | -4.14231 | -40.45055 | 2025-11-26 03:57:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 55d1432f-ba50-3805-99af-417b69ece13a | -4.14533 | -43.64451 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 08b9e619-ceaf-35a0-a30a-0bf6b5db0e2d | -4.19282 | -43.70136 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 703eed8d-056c-3dba-ba40-19cbc082ad32 | -4.26293 | -45.11998 | 2025-11-26 03:57:00 | NPP-375D | OLHO D'ÁGUA DAS CUNHÃS | MARANHÃO | Brasil | 2107407 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 49ea92aa-2a16-3331-b93c-1f0770a2091d | -5.3719 | -43.72408 | 2025-11-26 03:57:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 201e9ed9-09c7-390d-ace5-522e019e0721 | -6.50376 | -38.82205 | 2025-11-26 03:57:00 | NPP-375D | ICÓ | CEARÁ | Brasil | 2305407 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| acb40f2d-3820-3102-9e1a-05e0809eaeb8 | -6.88094 | -47.23882 | 2025-11-26 03:57:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e79aef2-0ff8-3704-9532-80bfc94a524e | -6.52252 | -37.80071 | 2025-11-26 03:57:00 | NPP-375D | JERICÓ | PARAÍBA | Brasil | 2507408 | 25 | 33 | nan | nan | nan | Caatinga | 0.9 |
| ec9b3760-17be-3bf6-8489-ce35f87c4961 | -3.13027 | -49.40807 | 2025-11-26 03:57:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 705a35de-63ae-3e09-9a9a-9bf1e44362df | -5.90228 | -44.01231 | 2025-11-26 03:57:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b219a12c-0ca9-3d85-94d7-979dee6bca72 | -3.33326 | -50.2676 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| a486c7da-e6cc-3041-9217-3c76a5137fcd | -2.74553 | -47.13555 | 2025-11-26 03:57:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 35e378b5-f7f7-3a18-bb20-dcfeace36878 | -3.74508 | -44.54343 | 2025-11-26 03:57:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f1fd9b5c-f9d3-3326-915e-67c0014e6deb | -3.4356 | -50.19043 | 2025-11-26 03:57:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 00870d9c-68f9-36a2-bd0d-7a0bbe67e2d2 | -4.16981 | -43.7345 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 89fde4d8-a8a1-369f-ab76-13aa76b93e17 | -5.50272 | -42.37226 | 2025-11-26 03:57:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| e93a4c89-a601-37c9-a99f-95cac58276fa | -3.33018 | -49.71871 | 2025-11-26 03:57:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 93024ffa-fc7e-301d-be02-dec15ff0e7ea | -4.22443 | -48.37093 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a05b03d7-b9f6-37d3-b7ca-1670eab8e733 | -3.22238 | -50.57432 | 2025-11-26 03:57:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b30fbc15-e8de-3573-8567-5e230cdd5922 | -4.2849 | -47.30354 | 2025-11-26 03:57:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 11cd8fa7-6ae4-3f12-8be1-3afef3bd8c5c | -4.56435 | -43.80005 | 2025-11-26 03:57:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6342e618-f2f2-3ad9-9cb3-8ec482cf7488 | -3.58922 | -40.9833 | 2025-11-26 03:57:00 | NPP-375D | VIÇOSA DO CEARÁ | CEARÁ | Brasil | 2314102 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 0e1f53d1-220f-3723-a1d8-642bd22f2a7a | -5.03767 | -43.25915 | 2025-11-26 03:57:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 938249f3-35bd-3dc7-bc19-3412f7dd9f62 | -6.80295 | -41.71836 | 2025-11-26 03:57:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2a050939-d6dd-31c8-948f-fb5904abb8ee | -4.37755 | -49.77253 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 60f4dc1d-3ddc-32d4-ad62-b46c6d4c3dac | -6.5811 | -43.86293 | 2025-11-26 03:57:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0fbc3a6b-a7ba-308c-808b-d107b170b245 | -4.72256 | -46.45684 | 2025-11-26 03:57:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e80b883c-980a-33b2-80b4-5281defbd1a8 | -4.17476 | -43.73117 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fdbbaa01-34e0-3e50-b9ba-043aa167d04f | -4.37122 | -49.77119 | 2025-11-26 03:57:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| eeeff14c-3d78-39e7-b969-051446ad979d | -5.60308 | -35.63483 | 2025-11-26 03:57:00 | NPP-375D | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e4bddbaf-a02c-3d84-b521-a05d5cbaa49a | -4.55767 | -43.29378 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 545ca449-0bec-37a6-a0e9-52f820562e1f | -6.30861 | -43.78555 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4ce45bc9-8c64-39f2-8453-b2f8c3d37c31 | -7.49741 | -42.88124 | 2025-11-26 03:57:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 827df1fc-5a87-351c-bf1b-21b62732e1e5 | -2.42092 | -48.59339 | 2025-11-26 03:57:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8ebf0ddd-bb7a-3ba1-b1d9-f9bfd70bd1fb | -4.81074 | -43.82772 | 2025-11-26 03:57:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e689c722-697a-3eea-aff2-8922c2a18592 | -3.59639 | -38.77759 | 2025-11-26 03:57:00 | NPP-375D | CAUCAIA | CEARÁ | Brasil | 2303709 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ad4fd5a8-cc20-3398-a40c-ad0ad132d0c6 | -4.17903 | -43.7319 | 2025-11-26 03:57:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 723ee80a-452e-3229-8214-f40cd79d6cc1 | -4.56058 | -43.30183 | 2025-11-26 03:57:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a47cc3a7-5eda-3a83-ad49-089b9c58bb05 | -3.6748 | -43.56752 | 2025-11-26 03:57:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 17f72c11-f706-3184-bb4b-23166fb7f23a | -2.54972 | -45.38554 | 2025-11-26 03:57:00 | NPP-375D | PRESIDENTE SARNEY | MARANHÃO | Brasil | 2109270 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d9a9822e-3941-37a1-8c1e-d0178f84f499 | -4.24776 | -48.56966 | 2025-11-26 03:57:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README8.md)
