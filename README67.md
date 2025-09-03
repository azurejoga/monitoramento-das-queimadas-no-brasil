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

## Dados Diários - Página 67

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9767d9d9-a003-36d7-b9be-9e6e33236e01 | -7.25623 | -57.55031 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 734cb1c1-4050-32a1-a56f-624be03f8d9d | -8.72114 | -46.13239 | 2025-09-03 04:46:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c2f57b39-8abb-3af8-90db-61dc94701a63 | -9.05337 | -54.95228 | 2025-09-03 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0edc813d-1ae6-30e5-b1c1-d0f88be041ff | -6.23398 | -42.43154 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 4d05c60b-c359-31f2-b158-8e552b872b42 | -6.47363 | -45.41051 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 648e5154-3b26-39c7-bbee-ba0dd082329b | -5.8884 | -43.01449 | 2025-09-03 04:46:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| ddf35add-a4d3-3d3f-a172-4097d965f6ba | -6.97636 | -44.35945 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0b370d2f-54ab-355c-a87e-ad9d0f8c592f | -6.52826 | -56.19744 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90d32661-d203-3e24-a5fc-ecbebf1cdd16 | -5.38597 | -45.94609 | 2025-09-03 04:46:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 826ea8c5-95e9-302a-a6d6-d0dddbf1e5ef | -6.80236 | -52.80945 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 201da559-fd9f-360f-b5b2-1993c155d087 | -9.63419 | -46.12329 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 97cd12de-b820-3051-abca-ac82e67faa04 | -8.3548 | -52.52807 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 092d322c-5a21-3d89-a527-a85a7499eb84 | -7.7807 | -50.96137 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fcb3f44-9b9c-3fca-abd4-71b531946b39 | -7.00271 | -43.24558 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 41f0de69-991c-315c-9098-74d1af52f3c5 | -11.60611 | -52.10219 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| eee457ef-10f6-3838-9093-c64f79aca729 | -6.35131 | -51.77006 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9467cdb8-3cfb-383d-b8c0-c90f65c7b43a | -11.63194 | -52.06679 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92f48b25-9144-3be4-a8ea-af4cde603773 | -11.59125 | -52.1106 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 60ada761-8df8-357f-9a28-90e325f3d8bc | -7.48857 | -44.81067 | 2025-09-03 04:46:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 03681879-fdf6-3d55-8087-8593eb1ef7e6 | -6.75531 | -56.39598 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 539f0420-17ea-36c5-8932-56019b42294d | -8.06014 | -52.34742 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 209e3785-5961-3df6-996b-a7cd6574d88d | -8.36127 | -48.31092 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| ca0d5e00-1508-347d-9b8c-c3ef6bf82ff5 | -6.97444 | -44.33964 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 362d0f25-56f1-356b-ab62-ee15f8a31e1d | -7.00424 | -43.23438 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5046892a-31b7-3e91-ab06-9122935dbc94 | -11.58631 | -52.12059 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 14.8 |
| d1d53f18-30aa-3b54-b029-c69d9a920cfb | -6.86372 | -52.79322 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a3597c20-99da-3306-b1f2-fad2ead6b58f | -6.66575 | -45.9058 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 35a83061-38f0-3566-96c8-d9aa1a7165a9 | -11.60771 | -52.0701 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 890fad42-d8c9-3f2f-b013-7009245056e6 | -6.45989 | -43.97777 | 2025-09-03 04:46:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 639bf1e5-1ed7-3187-9e7a-0150962dceee | -7.92906 | -46.45926 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 81b69249-c54c-3b9e-b84d-4923aa1f17d3 | -11.44004 | -46.91766 | 2025-09-03 04:46:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 16788bc4-38b0-3ad7-bc3a-51fcccf2df37 | -9.63792 | -47.86222 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 45e85a82-570e-3997-98c6-c56008aaeb26 | -10.27709 | -46.49688 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c330e808-fba5-3842-8b7a-cb0e5955c0de | -6.58213 | -44.56972 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cd2e289a-4e8c-3410-ad71-7d918bd9dce8 | -6.54174 | -42.95307 | 2025-09-03 04:46:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 77f86409-34b0-39e8-bc30-87d1f3c03cab | -9.63106 | -46.11464 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e8acaba1-74dd-357e-8b7b-7567c98de0f9 | -6.22622 | -43.38837 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 28e63c47-0bc1-3681-9e80-164fb63d061c | -10.72812 | -49.59794 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e526a6db-3816-37ac-85d0-f01e354a622a | -6.45373 | -42.38574 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 68e5bbbe-837c-320a-84c5-bfa94d5f57d6 | -7.93088 | -46.54218 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 0077f151-9d11-38d3-a0fb-5c774f6ae12c | -5.72069 | -45.23717 | 2025-09-03 04:46:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1adf1dd1-f1f8-38a8-92ad-217829041ae9 | -10.92334 | -50.86021 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c8c30b88-165f-3cd9-9977-534b1e1daab8 | -6.80622 | -52.82861 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7665e61c-bb2f-30bd-901b-f13f06d96ed7 | -7.00581 | -43.21564 | 2025-09-03 04:46:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| d8fb9dd4-4e6a-3817-9ca5-77c146ae8742 | -11.2138 | -55.06517 | 2025-09-03 04:46:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2d41b17-165c-3c04-bb1c-25db2b1e9b5a | -6.66819 | -45.91793 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 89b8d1c0-d71c-34bd-8391-565c0ece7486 | -11.57007 | -49.90728 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3d2d2bd2-9daa-34d8-8688-f9e2e2e72a01 | -7.92622 | -46.4224 | 2025-09-03 04:46:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7a7a563-7974-3775-a6b9-c8b5047e7f6d | -5.90005 | -57.73806 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 73f5bbd1-0fe9-3f9a-aa8d-ec53b2d4734f | -7.72093 | -48.72648 | 2025-09-03 04:46:00 | NOAA-21 | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 1cf2ce55-eadf-3257-9960-f6ae7de66edd | -6.83149 | -52.84386 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c316526f-31e1-3807-9530-1aef658da509 | -7.12343 | -43.75771 | 2025-09-03 04:46:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 45fd4d0e-8323-3952-8802-a5501a310c19 | -6.80352 | -52.8022 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6b5683d3-a89f-31a0-9cb8-cc31ecb6985b | -5.69868 | -45.94525 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 588a1c1c-08c3-3daf-ac84-c81996519559 | -5.40514 | -42.33406 | 2025-09-03 04:46:00 | NOAA-21 | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 8cbc8a23-6c1c-3729-9e21-b12fb6385b1a | -10.95003 | -50.77515 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 53709826-6465-30b1-a1df-75106b0b14f1 | -6.27561 | -42.66249 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| dac5ac32-b0d6-31e8-980d-e2966e6dd429 | -5.91871 | -57.70914 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a82c676a-2921-3987-96bb-832e9c09f628 | -11.62696 | -52.05521 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1fc1e6d5-8ae7-3bc8-be33-cc1547a4646d | -6.48663 | -49.18218 | 2025-09-03 04:46:00 | NOAA-21 | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5787c403-51b1-3648-9de6-3b22cb8b4f16 | -10.49953 | -50.3229 | 2025-09-03 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a1ca7f7-1aa5-3acb-93c5-dc1ae3ffad29 | -11.11761 | -44.64108 | 2025-09-03 04:46:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b623afb1-a3ba-3046-8cbe-b5794b5d08b5 | -8.08539 | -47.60071 | 2025-09-03 04:46:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d0cb0918-ab1e-3eb2-8964-4fcd25c3006e | -10.60722 | -49.63286 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4dc7d947-5160-3ebd-9005-c21335e6bd65 | -8.43826 | -45.08754 | 2025-09-03 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 29759b10-00f4-3897-adf9-b3c18108a04f | -5.03447 | -49.23195 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IPIXUNA | PARÁ | Brasil | 1504976 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| de261e87-df15-3a54-9e9d-acaf9db055ae | -6.54365 | -44.56646 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3aed362-0f55-3cb4-ae24-3d56d1067524 | -6.75585 | -45.91522 | 2025-09-03 04:46:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| dc428cbf-b667-366b-929e-f1a64878a020 | -5.89912 | -43.35727 | 2025-09-03 04:46:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4a9b42c-4483-38c4-98ed-7763a72c3d40 | -8.35868 | -52.52512 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 41b3bc5b-b390-396e-a7c0-c48612b8900f | -6.53789 | -56.19932 | 2025-09-03 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| afe93b1a-096b-3c71-bfb6-43e219d17b1f | -5.80701 | -45.62904 | 2025-09-03 04:46:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 208b1c18-b373-3dba-8907-c281d077c51d | -9.13737 | -49.64002 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bdbb6961-d985-3e3c-a515-57f1503bc658 | -11.01235 | -46.82624 | 2025-09-03 04:46:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7a439f58-1ba4-397b-9817-217d66b0cafd | -8.38321 | -48.2882 | 2025-09-03 04:46:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1259b99-c20b-32ef-9554-e959650e1a21 | -6.79445 | -52.81566 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 13e19e6d-9eef-3b30-a6f4-9bed2e6b1a31 | -11.03434 | -45.06763 | 2025-09-03 04:46:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 97a04f46-0a26-35e9-b9f7-ece23e12029e | -7.10551 | -50.77691 | 2025-09-03 04:46:00 | NOAA-21 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 926ff7cd-a484-3205-a48b-289556940e49 | -7.71238 | -50.25607 | 2025-09-03 04:46:00 | NOAA-21 | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6071e90b-657f-3991-9ede-94cb2982265c | -10.91545 | -50.84414 | 2025-09-03 04:46:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c2ab9e95-ea04-3b14-a390-ad1e7dc8dd27 | -5.51017 | -42.64908 | 2025-09-03 04:46:00 | NOAA-21 | LAGOA DO PIAUÍ | PIAUÍ | Brasil | 2205581 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| f175c4ce-a381-3890-92a4-b6465d492fa6 | -10.14829 | -46.27774 | 2025-09-03 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e2bf1a03-399a-39e6-80dd-a52913518b78 | -9.70514 | -48.30172 | 2025-09-03 04:46:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 01e4724c-c931-3e27-914c-ac3b965fe487 | -5.91722 | -57.71803 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a6674b05-0596-37d8-a7d4-bb3e3ea8d324 | -6.51308 | -42.18993 | 2025-09-03 04:46:00 | NOAA-21 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 48ad1c48-aaaf-35e3-a030-0f12cccc87db | -9.63103 | -47.85636 | 2025-09-03 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8dce21c8-4581-3e54-8ebb-e200d610c0fa | -5.92172 | -57.71864 | 2025-09-03 04:46:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 4f53fc00-62b8-33f6-9c3d-1748dd7a3bf1 | -11.06546 | -52.08009 | 2025-09-03 04:46:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d917252-104e-3bb5-bf2b-2e42f25fb026 | -6.79966 | -44.08217 | 2025-09-03 04:46:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 419a3ff2-e80a-395b-b31c-30c507456465 | -7.77962 | -50.96828 | 2025-09-03 04:46:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fe365217-c03f-3d2f-8417-23f28539fd0e | -6.23951 | -42.4298 | 2025-09-03 04:46:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 6696f60b-88a5-3275-a436-4a3bd9b5488b | -11.64404 | -52.05434 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 49e9109a-6d1a-38fe-b05d-0269cff9b380 | -10.20883 | -54.30141 | 2025-09-03 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93895ea2-ebb4-3ebe-aeaa-0eabf9e2e577 | -11.60001 | -52.07605 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0e0dfc24-058e-3e7c-8df9-ec24d9717eb3 | -7.90692 | -46.44158 | 2025-09-03 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 0604bfd0-fb81-3220-b086-41ca5543afff | -5.47964 | -51.47224 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| be7941ea-34c0-35f2-9fb2-eaf0d5bf2e1d | -6.25764 | -42.60432 | 2025-09-03 04:46:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2ab7a41d-68b3-3a08-b2ef-090e4fda0217 | -6.85067 | -52.83202 | 2025-09-03 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ff720e4-a1a9-3eaf-9d99-b08725025ee2 | -6.45511 | -44.67663 | 2025-09-03 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0f818d76-f49b-3d55-b434-b19498c497fc | -9.13566 | -49.65141 | 2025-09-03 04:46:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |


[Clique aqui para ver as próximas entradas](README68.md)
