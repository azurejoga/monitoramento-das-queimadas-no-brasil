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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56349326-84b1-362b-ad0b-1004f977ae58 | -5.20102 | -45.48378 | 2025-07-18 05:57:00 | AQUA_M-M | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 3bf157f3-3eb6-351c-b8e6-720ccc9bb8c1 | -8.08201 | -43.15639 | 2025-07-18 05:57:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 15.6 |
| ef665cdd-3708-32ac-97bd-8ee7d43ec195 | -8.08453 | -43.13831 | 2025-07-18 05:57:00 | AQUA_M-M | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| e11f0056-557f-3836-b68b-5a81bbd53cd2 | -9.80236 | -47.73142 | 2025-07-18 05:59:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e795233b-00ac-3228-aa4f-2cee543da833 | -9.50294 | -47.56136 | 2025-07-18 05:59:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 47.0 |
| 0859b97b-59b1-3bf2-b741-78e8f3c86762 | -11.56732 | -47.06753 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| df985e13-b706-3318-b498-e595b23391f5 | -11.73764 | -48.1876 | 2025-07-18 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 125.5 |
| bd6ff254-0b07-3037-81ec-f0cc68954e5a | -10.82082 | -49.28334 | 2025-07-18 05:59:00 | AQUA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| fe4aa86e-0d68-39cd-a741-f68de4d258bf | -12.65895 | -47.09316 | 2025-07-18 05:59:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 0de24774-84eb-3eda-94dc-67913c311ec4 | -10.71782 | -49.4717 | 2025-07-18 05:59:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 15162bbb-164f-3b9e-9251-294a7cdf7d7d | -11.56577 | -47.07841 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 16.3 |
| e6233602-f571-34d1-a13b-96674c447c9d | -11.55458 | -47.08792 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 03ba3850-44e8-308f-a2d2-ddee256d2745 | -9.76183 | -48.75262 | 2025-07-18 05:59:00 | AQUA_M-M | BARROLÂNDIA | TOCANTINS | Brasil | 1703107 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 5872a298-1c8a-3443-8754-83245bcf7845 | -8.64588 | -47.75102 | 2025-07-18 05:59:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| cd102030-73ad-32ec-832a-a7000f6b3083 | -8.88776 | -44.79224 | 2025-07-18 05:59:00 | AQUA_M-M | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 17.6 |
| 2323e5bd-6f14-30c9-9ff2-923d6352493f | -11.56422 | -47.08931 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1a53cb88-71aa-3f8c-8773-c3790345bd62 | -10.84003 | -48.33405 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| d3f72c12-ec71-3627-afaa-29112567d15c | -8.87791 | -50.15136 | 2025-07-18 05:59:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| f27c1b43-e9d8-3751-a511-8ff3e40915c8 | -10.71649 | -49.48061 | 2025-07-18 05:59:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 32.9 |
| 7bda8053-6578-3eae-ac10-9874f57ef752 | -9.50433 | -47.55165 | 2025-07-18 05:59:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 3f4957f5-4197-36fc-a3ea-29b6d44e2bf7 | -11.55612 | -47.07706 | 2025-07-18 05:59:00 | AQUA_M-M | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 22.9 |
| cb08d487-9eea-3e8e-bb8e-a3115ade7809 | -11.73624 | -48.19729 | 2025-07-18 05:59:00 | AQUA_M-M | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 0340722c-cc78-3a53-8282-83dbd3a56f8f | -10.71516 | -49.4895 | 2025-07-18 05:59:00 | AQUA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 6311f3aa-c261-3e68-ace3-1a14430e5d9b | -5.6567 | -43.7161 | 2025-07-18 06:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 98.4 |
| 8f282927-83ba-39e2-b0c3-16537781762e | -3.3958 | -47.4785 | 2025-07-18 06:00:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 70.0 |
| d322145f-9fef-313d-bd8b-d91159a3a92a | -11.7508 | -48.1825 | 2025-07-18 06:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 52.1 |
| 13349c6b-048a-3661-8918-faa6ea3930ca | -20.19155 | -50.5028 | 2025-07-18 06:01:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| 339e1932-65a6-39e8-be63-8ea48ece0dc5 | -20.19294 | -50.49308 | 2025-07-18 06:01:00 | AQUA_M-M | VITÓRIA BRASIL | SÃO PAULO | Brasil | 3556958 | 35 | 33 | nan | nan | nan | Mata Atlântica | 28.8 |
| bed5417d-a4f2-36d1-98a6-7856047ddced | -7.82796 | -63.29632 | 2025-07-18 06:08:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3790969d-30ce-372c-a9ea-62830371a843 | -10.02294 | -66.83168 | 2025-07-18 06:08:00 | NOAA-21 | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a6b30062-bd02-30ed-b857-01b5cc0e0696 | -7.49102 | -63.81591 | 2025-07-18 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5dd031e4-620b-3cc1-b0d2-233b4cb977a9 | -7.49063 | -63.81881 | 2025-07-18 06:08:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9e89932c-0177-374b-b4a5-3cb493e40046 | -9.88272 | -65.17173 | 2025-07-18 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 5aa8dea8-110b-3727-9ed5-fc6078583a67 | -10.1472 | -67.72128 | 2025-07-18 06:08:00 | NOAA-21 | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b09d3dcc-16bc-3bf4-81c4-629b94edf5af | -9.88812 | -65.16728 | 2025-07-18 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fd02ae6b-2e2a-3a7c-acdd-1016f3797a2e | -9.88339 | -65.16657 | 2025-07-18 06:08:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 09128010-9adc-3414-ab63-d72589a8276c | -9.87607 | -68.3356 | 2025-07-18 06:08:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 807d2441-55d8-3beb-8833-c91b522199ae | -9.0242 | -61.22498 | 2025-07-18 06:08:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 75b759fa-b744-317b-991a-40942246ec17 | -5.6567 | -43.7161 | 2025-07-18 06:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 100.2 |
| ed380e4e-458a-38a1-a0ae-bf6c764e2c68 | -3.3958 | -47.4785 | 2025-07-18 06:10:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 64.8 |
| e4c6d19e-3473-3d8b-90cc-431a81d22c0e | -11.7508 | -48.1825 | 2025-07-18 06:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.7 |
| 3dde8ed6-e6b1-3839-ad81-ae7b14c5ba6a | -5.6567 | -43.7161 | 2025-07-18 06:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 94.7 |
| 46c8c6d7-e1f5-39f2-ba7f-6b690ca45728 | -11.7508 | -48.1825 | 2025-07-18 06:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 41.9 |
| d4b87b8c-2333-32a8-aa51-c713717304c9 | -3.3958 | -47.4785 | 2025-07-18 06:20:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 4db82e4e-8e9b-3db5-9844-097d8c4c4e72 | -11.7317 | -48.1849 | 2025-07-18 06:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 673776d0-c8bd-3564-87e2-3dd5f199b45c | -11.7317 | -48.1849 | 2025-07-18 06:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.5 |
| e0337e51-6c14-3d8b-9403-aca323f84a36 | -5.6567 | -43.7161 | 2025-07-18 06:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.7 |
| 46bae900-4bd6-3758-a4b6-f834029a1b2f | -3.3958 | -47.4785 | 2025-07-18 06:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| a31099b7-e39c-3408-bbe9-d46de01c90e2 | -9.88576 | -65.16463 | 2025-07-18 06:35:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7ab564b9-0430-3b34-85d8-f8e709335a2b | -9.88494 | -65.17162 | 2025-07-18 06:35:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2de7e610-fc09-3780-ae5e-bf86a92cb36a | -9.88154 | -65.16884 | 2025-07-18 06:35:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4aedc1f3-7d57-36a7-bbfc-a0558342c0cd | -9.88859 | -65.16981 | 2025-07-18 06:35:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ae6630f6-d48f-3013-9648-6c2d33e10a88 | -11.7317 | -48.1849 | 2025-07-18 06:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 01f153c4-a957-32a9-894b-e578ac61e3dd | -5.6567 | -43.7161 | 2025-07-18 06:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 80.1 |
| 273ead86-9026-398e-9856-3070dcb44814 | -11.7317 | -48.1849 | 2025-07-18 06:50:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| 35c88a64-5275-30cf-bec5-729fd95f416d | -5.6567 | -43.7161 | 2025-07-18 06:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 96.2 |
| a9534735-907e-39b7-8c75-3000b85e0ffa | -11.7317 | -48.1849 | 2025-07-18 07:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 43.2 |
| ca34502d-4475-3a9f-bb2e-3a47fceb4148 | -11.7508 | -48.1825 | 2025-07-18 07:00:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 47.4 |
| 00a5770b-e9be-3438-8421-9afce78c20ac | -5.6567 | -43.7161 | 2025-07-18 07:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 8060140b-703c-3481-bbf4-f23a31bae754 | -5.6567 | -43.7161 | 2025-07-18 07:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.6 |
| e51332b4-9435-3c39-a9a1-5d57172ce940 | -11.7317 | -48.1849 | 2025-07-18 07:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 50.1 |
| 083d55fd-afd0-337e-805f-d2743ec2336f | -5.6567 | -43.7161 | 2025-07-18 07:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 0487e9ca-caa2-368f-8922-d0cce926cf2c | -11.7317 | -48.1849 | 2025-07-18 07:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 60abbeb3-48ef-3e76-8cb6-856cac73f0c2 | -5.6567 | -43.7161 | 2025-07-18 07:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| e0ec0b38-0779-3d23-a7b3-033e1c68dd5d | -11.7317 | -48.1849 | 2025-07-18 07:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 45.5 |
| 5b01f7cf-adc8-3b79-b3cb-b4669be22b3c | -11.7317 | -48.1849 | 2025-07-18 07:40:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 56.3 |
| 7ffcdcc0-56f2-30f0-8f53-cb3b46e8288b | -5.6567 | -43.7161 | 2025-07-18 07:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 76.0 |
| 6744c180-37f1-3acc-a41e-3579feb8a566 | -5.6567 | -43.7161 | 2025-07-18 07:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 7ed3ed9c-f30b-3d9a-9f30-4837ef243fc0 | -5.6567 | -43.7161 | 2025-07-18 08:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 68.5 |
| 92226843-0ab6-3fc3-85c2-883288b5ce08 | -5.6567 | -43.7161 | 2025-07-18 08:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a73834eb-1da9-3308-b33f-c8a7132b89af | -5.6567 | -43.7161 | 2025-07-18 08:20:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 70.3 |
| cd8f2952-5ca5-3138-b146-f085590ab0f4 | -5.6567 | -43.7161 | 2025-07-18 10:50:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 105.7 |
| 0c039a26-9b93-3c2e-a7ee-cbe096d666fb | -5.6567 | -43.7161 | 2025-07-18 11:00:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 116.1 |
| 474cd943-5117-3f01-b516-5e8601eb4c7c | -5.6567 | -43.7161 | 2025-07-18 11:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 6fc45ca9-088b-3b19-b511-5c0fb369400d | -5.6567 | -43.7161 | 2025-07-18 11:30:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 97.5 |
| 2188b5d2-923e-304c-863a-fcecb71c1bd9 | -5.6567 | -43.7161 | 2025-07-18 11:40:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 86.1 |
| b50541db-a125-3141-8248-f05e97eeb1ad | -5.62619 | -43.15253 | 2025-07-18 11:49:00 | TERRA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 14.6 |
| 6ffac7ed-15b3-3bbb-94ad-d102ce7e1072 | -6.9673 | -42.79466 | 2025-07-18 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 28.2 |
| f876256c-f00f-3a10-9db5-eead827437d4 | -3.30024 | -42.52486 | 2025-07-18 11:49:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5de16019-639d-39c5-8cf4-40d694a98297 | -6.40029 | -37.6898 | 2025-07-18 11:49:00 | TERRA_M-M | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 845108a5-7672-3907-9796-3c0c548dca92 | -4.90512 | -37.30371 | 2025-07-18 11:49:00 | TERRA_M-M | TIBAU | RIO GRANDE DO NORTE | Brasil | 2411056 | 24 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 3caf189b-f138-3908-8f68-661b47c6807a | -6.91653 | -44.12759 | 2025-07-18 11:49:00 | TERRA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 17ae1fc1-e8a4-3ef9-80d4-3524465abe64 | -7.28837 | -44.02864 | 2025-07-18 11:49:00 | TERRA_M-M | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5f52f7a7-36c2-3047-984f-41572eb78f06 | -6.96176 | -42.80056 | 2025-07-18 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 7c9afb9a-359d-3eb3-a95c-381c5861f302 | -5.78513 | -45.07235 | 2025-07-18 11:49:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 20.8 |
| 03d55cd9-5993-3c07-a9fa-70ef0793ea53 | -7.25788 | -44.50183 | 2025-07-18 11:49:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8fb6c31a-f6fe-3a72-b0aa-ccb6d3e81961 | -6.69257 | -43.17881 | 2025-07-18 11:49:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 14.1 |
| 2c15f482-e155-323a-a8ef-cf4b32034a2d | -6.87541 | -37.9217 | 2025-07-18 11:49:00 | TERRA_M-M | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| fc585bc1-9883-3762-b254-8240c6ea5b37 | -6.95533 | -44.55342 | 2025-07-18 11:49:00 | TERRA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 1bdfcda3-eaea-3f7c-9ad5-0ce600183386 | -6.97229 | -42.80206 | 2025-07-18 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 134.0 |
| 551ccc60-8630-334f-aed4-2554fd395bd0 | -3.29819 | -42.53889 | 2025-07-18 11:49:00 | TERRA_M-M | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 0410209e-91a7-31a8-9eae-da8dc3687642 | -6.95677 | -42.79316 | 2025-07-18 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 92e8373a-c0cb-3b46-aa6b-f81350c07912 | -4.80778 | -43.22863 | 2025-07-18 11:49:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 26.8 |
| 6498cfd5-c950-3074-87fe-38f1043685a4 | -5.79462 | -43.63212 | 2025-07-18 11:49:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 49f4e1db-eea3-3f52-8984-af3a209f5f44 | -4.59963 | -43.30911 | 2025-07-18 11:49:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 25.2 |
| e1f6e124-4a0e-35cf-a79f-c4cf9f4cf794 | -7.12744 | -43.80253 | 2025-07-18 11:49:00 | TERRA_M-M | MARCOS PARENTE | PIAUÍ | Brasil | 2206001 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 07a1cff5-1d4f-38ed-8bc7-8bc88e113241 | -6.96539 | -42.80751 | 2025-07-18 11:49:00 | TERRA_M-M | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 28.3 |
| d433a167-59fc-3149-bc8b-1ee835e3bd54 | -7.1869 | -44.08853 | 2025-07-18 11:49:00 | TERRA_M-M | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 133a0d3a-a357-3f38-b6ff-4f74e44d4e64 | -6.14867 | -42.57632 | 2025-07-18 11:49:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 6814be20-2535-3159-9333-102b4bdb6535 | -6.83371 | -39.29398 | 2025-07-18 11:49:00 | TERRA_M-M | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 19.4 |


[Clique aqui para ver as próximas entradas](README30.md)
