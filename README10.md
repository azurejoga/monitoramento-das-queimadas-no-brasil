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

## Dados Diários - Página 10

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 72d1795a-0f77-3fd2-a09e-dec556882f7b | -22.6009 | -48.5698 | 2025-09-27 02:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.1 |
| 54b86897-860a-3157-b662-f136e71a0a90 | -9.9873 | -46.7103 | 2025-09-27 02:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| c4f72f18-6e6b-3e03-9631-3c5a04ba8fa2 | -5.5056 | -43.866 | 2025-09-27 02:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 13eeb1ea-2898-330c-bfd6-c505e3b1994c | -6.1485 | -47.2871 | 2025-09-27 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 58.1 |
| d72b11ac-7356-33e7-aab2-6c031c07413b | -10.0059 | -46.7306 | 2025-09-27 02:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 136.3 |
| a5b76c9a-75a1-35bc-a63c-01f52d47b208 | -6.1487 | -47.2651 | 2025-09-27 02:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 74.1 |
| d2d076d5-769b-3f4e-9a43-781986827c9e | -5.4748 | -43.1009 | 2025-09-27 02:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| f28df851-e23b-3219-8c1a-f5911387e67e | -22.5799 | -48.575 | 2025-09-27 02:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 54.5 |
| 70074eb5-1f84-3f80-a521-922885995029 | -5.4937 | -43.0761 | 2025-09-27 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| 64258fd2-917d-35b0-9402-1e93cf220c90 | -5.5243 | -43.8647 | 2025-09-27 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| 205ad6f2-db5f-3779-8e7c-ed9fdd8f4066 | -5.475 | -43.0774 | 2025-09-27 02:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 2ee392fe-2ac8-356e-b66a-cc349c72c57d | -22.5792 | -48.5986 | 2025-09-27 02:30:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.5 |
| c680651d-e4b5-3daa-bb7a-497551de5c31 | -5.0676 | -44.8581 | 2025-09-27 02:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 413bf90c-114b-37a6-81b9-ebd901ecfa6a | -5.5241 | -43.8878 | 2025-09-27 02:30:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 49.8 |
| f55d2edd-0af8-3e5b-b2b9-7f727648205d | -5.5056 | -43.866 | 2025-09-27 02:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 689cd29e-99b9-3c54-baf8-0b115cb1ee2a | -22.6001 | -48.5934 | 2025-09-27 02:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.9 |
| 84552711-5c54-3c88-9a00-e9af8ce660f2 | -22.6009 | -48.5698 | 2025-09-27 02:30:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| fa7a9c5d-2661-370b-8160-189e6c9ea213 | -22.6001 | -48.5934 | 2025-09-27 02:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| bbb12449-4828-306a-91b8-8a071246f1fc | -22.6009 | -48.5698 | 2025-09-27 02:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 80.4 |
| 999e60ae-f33a-38d5-84b2-3e0caad0a344 | -22.5799 | -48.575 | 2025-09-27 02:40:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.8 |
| 60b84334-9e0c-3458-9c7d-274a9a4e6702 | -5.0862 | -44.857 | 2025-09-27 02:40:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 72.1 |
| e1711271-be71-3494-be57-7ab1828c0ef8 | -5.475 | -43.0774 | 2025-09-27 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 121.5 |
| c9808d54-1e51-3842-9c60-0f22c05cec24 | -22.5792 | -48.5986 | 2025-09-27 02:40:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.7 |
| 99bd543a-148d-3811-8063-5b433501f49a | -5.4752 | -43.054 | 2025-09-27 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 1500d3a3-da26-3b3f-ba47-71352a14d995 | -5.4937 | -43.0761 | 2025-09-27 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 126.3 |
| f85fb8dc-1c99-3151-b205-eed71674b88e | -5.4935 | -43.0995 | 2025-09-27 02:40:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 46.8 |
| 775c4365-9836-3e70-832a-8343b501ee06 | -16.9193 | -45.9434 | 2025-09-27 02:40:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 48f1211c-36da-3ce1-9657-038622a0888a | -22.6009 | -48.5698 | 2025-09-27 02:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.3 |
| 7000edbe-1ea9-3924-8cca-b12d37c5451f | -5.4752 | -43.054 | 2025-09-27 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 929664e4-24a8-3b37-a6fe-36318692bf85 | -16.9193 | -45.9434 | 2025-09-27 02:50:00 | GOES-19 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 97.4 |
| 1381b1aa-3b57-3938-807c-9813f391278d | -10.1806 | -36.2962 | 2025-09-27 02:50:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 75.7 |
| d404c646-2507-3560-a9d1-dc50f4cafb50 | -5.7961 | -42.8182 | 2025-09-27 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 53.9 |
| 02d687c8-d0e6-36f7-8b9f-45ed3ba99d10 | -22.5792 | -48.5986 | 2025-09-27 02:50:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| a0988a12-0b95-3665-ad1a-5243fe390337 | -5.8149 | -42.8167 | 2025-09-27 02:50:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 36.9 |
| cf805f7b-8beb-3d44-9545-334d7448528f | -5.0862 | -44.857 | 2025-09-27 02:50:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 80.6 |
| d9b1e6a1-f5ac-3a3a-bce5-be771c21b8e8 | -5.4937 | -43.0761 | 2025-09-27 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 56.4 |
| 575c8113-1423-3abd-bb48-f86f4e640d73 | -22.6001 | -48.5934 | 2025-09-27 02:50:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 68.4 |
| 5dd11fba-bc19-3b2e-bc6b-d13728bc6413 | -5.475 | -43.0774 | 2025-09-27 02:50:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 115.6 |
| 2882aa1c-ec55-362b-b948-deccfe0b258c | -11.6062 | -45.4134 | 2025-09-27 03:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 64fae823-89f7-3cd9-a92a-14521b1c8b19 | -5.475 | -43.0774 | 2025-09-27 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| bd61f467-73ba-39b8-8c13-88db25a7d009 | -22.6001 | -48.5934 | 2025-09-27 03:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 72.2 |
| 7ef3285c-ca34-31c1-9102-422da8a82cbc | -5.4937 | -43.0761 | 2025-09-27 03:00:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 37.4 |
| 01706868-adaa-3d3f-b2c9-77c41785b2a4 | -22.6009 | -48.5698 | 2025-09-27 03:00:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 62.9 |
| 69cc0c21-b09d-3917-a6cc-08b7f727cf69 | -5.0676 | -44.8581 | 2025-09-27 03:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 50.3 |
| df031449-9ece-3a0a-99d9-603a723a864a | -5.8149 | -42.8167 | 2025-09-27 03:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| ac5eb297-608f-3363-ab36-03c47edb8b5f | -5.0862 | -44.857 | 2025-09-27 03:00:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 73.9 |
| e8a478e4-bf7a-30d2-aa96-644f9cd50f60 | -22.5792 | -48.5986 | 2025-09-27 03:00:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 77.5 |
| d892c9ff-37fa-3dcd-a7d8-6e2909abdb6b | -5.7961 | -42.8182 | 2025-09-27 03:00:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 53.3 |
| 07895a15-5ce3-34f9-a6a4-0063aaf2bde5 | -9.9328 | -59.9247 | 2025-09-27 03:00:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| 43acf1f2-632b-37a0-8f78-620e8e348cb6 | -5.14248 | -37.74702 | 2025-09-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 3b44c358-3689-3c5e-b7c6-6159ac783b59 | -5.14349 | -37.74147 | 2025-09-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 7.7 |
| ee4bdb46-3710-395c-bfc7-810de819c000 | -5.14515 | -37.74101 | 2025-09-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.3 |
| fcf1f6b8-c18c-35c1-bdc8-5845fd366c41 | -5.14417 | -37.74658 | 2025-09-27 03:02:00 | NOAA-20 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 7d7406d1-6823-3726-8d65-e9a14befadf0 | -5.47003 | -36.66933 | 2025-09-27 03:02:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 97c2b202-77b1-3ee7-a68a-643fa2ef2cda | -6.48452 | -39.4722 | 2025-09-27 03:04:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 480d337c-63cf-3553-9679-00897a75d7be | -6.49162 | -39.47346 | 2025-09-27 03:04:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 0bdc2c6d-8e96-3727-9fdb-5d9dfee48292 | -9.92349 | -37.59899 | 2025-09-27 03:04:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 4f480473-12ee-33b2-ac8d-1631d8a88700 | -6.48809 | -39.47316 | 2025-09-27 03:04:00 | NOAA-20 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| af4b8453-54eb-3a6e-bf3d-16093eec6cde | -7.1491 | -35.79683 | 2025-09-27 03:04:00 | NOAA-20 | LAGOA SECA | PARAÍBA | Brasil | 2508307 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 046cfb26-7a4e-36ab-ac29-a3acf6784c2b | -20.4299 | -43.37427 | 2025-09-27 03:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.0 |
| 4e403de2-54b0-3aef-b151-817d52a581f8 | -21.11183 | -42.92669 | 2025-09-27 03:08:00 | NOAA-20 | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| be53d7a8-ba6a-34a7-85f2-bbd2da7a0666 | -20.43692 | -43.37548 | 2025-09-27 03:08:00 | NOAA-20 | MARIANA | MINAS GERAIS | Brasil | 3140001 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 966b5413-2300-3b24-975d-d6535ed24d86 | -5.4752 | -43.054 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 94.0 |
| 1703b2bc-049e-3504-a341-d4c8857b8cb4 | -5.494 | -43.0526 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 35.2 |
| c5483054-b1ca-3a0a-9b7e-72ba822c91b6 | -22.5799 | -48.575 | 2025-09-27 03:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 56.1 |
| 9e554462-caac-3761-9263-168469805f64 | -5.4562 | -43.0788 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5abd77e9-adda-36ef-8e77-bdaf821296f8 | -5.7959 | -42.8417 | 2025-09-27 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 32.9 |
| f27a1d5a-9ef3-3024-a76d-159b6f6162ad | -5.7961 | -42.8182 | 2025-09-27 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 46.6 |
| c498608f-790a-34a5-9de7-9ac2b3915e5a | -5.0676 | -44.8581 | 2025-09-27 03:10:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 52.9 |
| c267b49b-4a00-3dd2-93da-eb38aca023ea | -5.475 | -43.0774 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 203.9 |
| 3b938991-d1af-3155-a2d8-46f0050e83da | -5.8149 | -42.8167 | 2025-09-27 03:10:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 38.8 |
| 5c3d579d-dd4a-3a3c-b1f3-83603613f42d | -5.4748 | -43.1009 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 567dca31-171c-390f-b29a-3f6b78e6c2ae | -22.6009 | -48.5698 | 2025-09-27 03:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 63.8 |
| e7b9fe27-8437-3537-bce4-aab31ad4ad70 | -5.0862 | -44.857 | 2025-09-27 03:10:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 74c81596-6ccb-34f3-b75b-4227ad34d269 | -22.6001 | -48.5934 | 2025-09-27 03:10:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 58.5 |
| dd6dc1ee-9aeb-3cfd-b654-e2c49c5e24e0 | -22.5792 | -48.5986 | 2025-09-27 03:10:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 60.7 |
| befb7d1f-2bf8-3703-a124-1b5bb0542cce | -5.4937 | -43.0761 | 2025-09-27 03:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 57.1 |
| b46d206c-45d0-3232-a250-cfee89cedd66 | -10.0062 | -46.7081 | 2025-09-27 03:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 57.1 |
| a0b27606-0947-3177-a43e-8bb3ccc4ef38 | -5.5125 | -43.0747 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 2ce7f14b-1aa8-3c74-82c7-c89629338bfe | -5.5056 | -43.866 | 2025-09-27 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| f74beb72-f029-356d-a3c6-f10eacbfb3b4 | -5.5243 | -43.8647 | 2025-09-27 03:20:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 70.4 |
| 76a84d4f-955f-379e-86ca-0d228a59539a | -5.4937 | -43.0761 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 194.6 |
| b155d1bd-bbde-3d07-bf4e-128c5ed03920 | -5.4748 | -43.1009 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| d79ed2f2-ba14-3317-929b-cebbc98afe14 | -5.494 | -43.0526 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 55.6 |
| afc260f4-c5e0-3acd-9cd0-fe5bde198031 | -5.4562 | -43.0788 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 50.7 |
| 8e368b78-b898-3a37-a4d2-200cfe7361a5 | -22.6001 | -48.5934 | 2025-09-27 03:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 61.2 |
| d457122f-a973-355a-ac61-c32be45f8437 | -22.6009 | -48.5698 | 2025-09-27 03:20:00 | GOES-19 | SÃO MANUEL | SÃO PAULO | Brasil | 3550100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 55.2 |
| f85b1391-ca6f-367f-a861-28f021b3976a | -5.0862 | -44.857 | 2025-09-27 03:20:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 81.9 |
| b8ce7e7a-bfb4-324b-b4df-a959f220bf1e | -5.5241 | -43.8878 | 2025-09-27 03:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 50.0 |
| b7ecd20a-8673-322f-bb9f-4d9b218e08d7 | -5.4752 | -43.054 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 109.3 |
| 49290f38-c92c-3287-8394-c64e23c5f418 | -5.475 | -43.0774 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 305.0 |
| e2ce1e3b-acdf-3df5-ad4d-b5d2b9b92505 | -5.4935 | -43.0995 | 2025-09-27 03:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 81.8 |
| a51c7ea1-b45b-3f4e-a52c-5723538dd14e | -22.5792 | -48.5986 | 2025-09-27 03:20:00 | GOES-19 | IGARAÇU DO TIETÊ | SÃO PAULO | Brasil | 3520004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 53.9 |
| 4e8e713e-e680-3fd4-a55c-38f37e39418c | -5.0862 | -44.857 | 2025-09-27 03:30:00 | GOES-19 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 72.7 |
| 27cca7dd-e0ec-3a92-93fa-a787dbacaa7a | -5.4935 | -43.0995 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 70.1 |
| 8818b4cf-55da-38de-bc0f-15b2f3333d05 | -5.0676 | -44.8581 | 2025-09-27 03:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 63.3 |
| bd02eedc-547b-330a-8c15-e614b13297fb | -15.2134 | -49.4052 | 2025-09-27 03:30:00 | GOES-19 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 188.0 |
| 589533e3-9fab-3a13-8cfa-f72d4d28571c | -5.5243 | -43.8647 | 2025-09-27 03:30:00 | GOES-19 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 52.2 |
| bc36bf3c-0c37-3fa6-9c8e-9a6a1424a451 | -5.4937 | -43.0761 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 201.5 |
| 88fe6e8b-011a-365f-ada5-494de91162b3 | -5.4748 | -43.1009 | 2025-09-27 03:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 62.9 |


[Clique aqui para ver as próximas entradas](README11.md)
