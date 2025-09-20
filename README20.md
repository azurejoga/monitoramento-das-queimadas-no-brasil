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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6d11f9a5-3b95-38fc-83b9-2b148153fe52 | -5.94102 | -45.07537 | 2025-09-20 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6b72cbab-2c48-3ef1-b89a-15daa9abfdec | -6.24012 | -47.31577 | 2025-09-20 04:53:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9794c74f-0c2f-3d0c-80d2-868518af117d | -5.71422 | -47.43131 | 2025-09-20 04:53:00 | NPP-375D | GOVERNADOR EDISON LOBÃO | MARANHÃO | Brasil | 2104552 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f27359f-9ad3-3302-83af-f0da7981c9fd | -4.258 | -54.84739 | 2025-09-20 04:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 22d39abb-3fac-32d3-ab77-be3f058f7812 | -5.8143 | -49.85022 | 2025-09-20 04:53:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| a10beea4-3c20-330e-980f-ab1cebf7ae4b | -5.4832 | -51.53756 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 95abe6bc-67e4-31da-aa90-a50cc2f03944 | -5.69771 | -51.74755 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3af17517-a574-3106-bc6f-69701162babf | -7.4065 | -50.01072 | 2025-09-20 04:53:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2543726f-e41d-33eb-899f-d07e4f02eef3 | -5.95894 | -42.91502 | 2025-09-20 04:53:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b09fa65f-8668-3174-af30-4713ca949ab8 | -4.94545 | -49.92423 | 2025-09-20 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bd4dacb-d79f-382b-ab1f-78ffe552fcf7 | -5.10895 | -43.2031 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 15a3e1e1-7d39-3976-8ca4-9a672aebae5d | -6.23837 | -53.46809 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 65b71ac5-1483-3bd0-8f91-773d9f9f44d6 | -6.01745 | -49.86399 | 2025-09-20 04:53:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f2af928f-9196-3646-89a8-3539a34d8a4b | -4.29449 | -48.27397 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 22b81d88-94ff-3b7a-a4e5-d8805b091773 | -7.11276 | -47.85482 | 2025-09-20 04:53:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 873a7d17-d898-3392-ad65-b8ad2c28050b | -5.30453 | -45.57906 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 53ba85e5-44d0-387e-a42d-2b46fb29805a | -5.84214 | -46.28653 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2c4ba21a-ec07-3085-8f78-3ec8ad5347e8 | -5.06067 | -49.94891 | 2025-09-20 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8efbbb39-5bf7-31f5-9dbb-d0fa3477aad2 | -2.79315 | -47.15053 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 294c651b-d39f-365a-9645-90c7c7d0cc93 | -3.45846 | -51.21642 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| c6a0f5ed-9bae-3797-bf6d-9749b9e90878 | -9.17095 | -44.64243 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 879089f4-501a-3da5-a21e-99031ec590fe | -3.32132 | -54.92287 | 2025-09-20 04:53:00 | NPP-375D | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d2c73d0e-3314-33f3-b4da-728e6dd11678 | -5.86768 | -45.90594 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1fd9da4a-b190-3c24-ae7c-97286976a8ec | -3.45901 | -51.21292 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| d143dbf5-a09b-3877-92ec-c18022835593 | -3.80661 | -52.35386 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff196316-9f46-306a-9185-dcda1f1da6b1 | -4.37087 | -54.97611 | 2025-09-20 04:53:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 583def98-619b-3a86-b564-deb280bad2db | -2.79628 | -47.14765 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 689b0156-23ce-3224-8100-2fbd06e3d883 | -6.59964 | -43.58421 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 19e7373d-a79f-3a05-9799-f57ee85f2514 | -6.34988 | -49.85792 | 2025-09-20 04:53:00 | NPP-375D | CANAÃ DOS CARAJÁS | PARÁ | Brasil | 1502152 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 592d8527-fbe9-3464-abb0-b03bad840a06 | -9.01902 | -46.32721 | 2025-09-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 48b94dd8-6d2c-3495-8b22-954ca7f70dd4 | -3.80606 | -52.35732 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bc633d2a-88b5-3977-8320-41637837351e | -3.35081 | -48.3932 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 44ce462a-59e6-31f6-a73f-71799454a68c | -3.29304 | -52.58247 | 2025-09-20 04:53:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ddc455cf-17fd-32bd-8b03-ab2a5d390989 | -5.83796 | -46.28786 | 2025-09-20 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| df18cfd3-daab-36dc-804b-c47c4c5955ca | -5.30516 | -45.57765 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f1b12b42-8402-3066-8b0b-1d24bd209923 | -6.11099 | -47.8514 | 2025-09-20 04:53:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d685f8fb-916d-3750-b3e6-0aa5aa4569c4 | -2.7971 | -47.15118 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 07dda2b8-ff14-39a1-8a0d-abbeec848a7d | -2.94626 | -51.76162 | 2025-09-20 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 037c8bce-9231-3837-8561-c0ccbd9be00f | -4.4772 | -54.85244 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 11aae456-6ef9-3a40-867b-52d94004449d | -5.197 | -45.48571 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9e137710-8e1e-313c-a02a-f8feaacf9886 | -6.81141 | -47.85402 | 2025-09-20 04:53:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e23b4e1f-3ff8-3fe1-bff1-35e164541772 | -4.29826 | -48.27454 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3629f15-a3f4-34a9-ae2f-98f46fbc02ea | -7.70855 | -55.1931 | 2025-09-20 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5b08bab9-1ab5-3337-a339-699e97c490c0 | -3.45424 | -47.628 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fed51737-3980-3d99-b6c9-2f52e26783c4 | -5.10796 | -43.20981 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| a4a7033d-4a8e-3a34-b6c7-7872567b6085 | -9.12162 | -44.65734 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3f69d9f7-b98c-3f64-98ff-74bf09b27683 | -3.35886 | -52.9992 | 2025-09-20 04:53:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| fd344df7-c5c6-3d00-b46c-6501ba2b8bd0 | -3.3434 | -48.39205 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d61ac6e3-f263-34ae-89e3-7c425678f483 | -5.78943 | -43.65401 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f6409d43-0eee-3c6e-a31f-d8216c5b2c21 | -7.43992 | -42.6258 | 2025-09-20 04:53:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0217596c-974a-365e-9df7-7dd13cf72ff7 | -6.80993 | -47.86423 | 2025-09-20 04:53:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 325a5080-bd27-3a9b-a028-490af8694b2b | -2.98383 | -51.24249 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f91b6719-48d1-32e4-a792-5469b3673013 | -3.44311 | -56.93437 | 2025-09-20 04:53:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 46cfb822-3c92-31fd-b4a2-77ec760814dc | -5.19767 | -45.48093 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1164a43d-15a8-3af5-8539-3b9bdcf9dc10 | -5.74407 | -42.58805 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 92f34f8c-d533-35c8-aa68-b06d6b840d2d | -4.08611 | -47.9565 | 2025-09-20 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7d2be097-b3ba-3cfd-85d7-9d7d747cde5d | -9.17139 | -44.63925 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c01f7aee-0867-3e42-9daa-21c2695ef529 | -9.12204 | -44.65421 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e6db251-15a5-34c0-b67a-e2e740c2738b | -5.60379 | -52.15059 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 35ad63c0-7b37-367d-8837-9ca4e185ee67 | -8.45903 | -49.52193 | 2025-09-20 04:53:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 82b86e0d-336f-3df1-b024-b8e864130f9f | -7.52989 | -47.28297 | 2025-09-20 04:53:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ae227079-fcfb-355f-ada4-3805009185ad | -2.98639 | -49.29332 | 2025-09-20 04:53:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 785a0cfd-699b-35fc-a3fc-af3ddc439757 | -5.16409 | -45.42437 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9455c73b-fe19-3c84-a53a-3b040dd0fd7d | -9.17242 | -44.64453 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 7d2c93b4-3a08-318d-a8ca-bbf252fd3778 | -2.82854 | -48.66009 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ccfd68d4-ca2c-307a-9985-1f74c1501c51 | -5.30449 | -45.58214 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 79a50949-3eff-3188-bbd1-93c013d63d96 | -4.48074 | -54.85299 | 2025-09-20 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c62ba091-4298-35ad-a208-dcddc03bdd85 | -6.02452 | -49.8652 | 2025-09-20 04:53:00 | NPP-375D | PARAUAPEBAS | PARÁ | Brasil | 1505536 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b2ad2978-2b29-3fae-9c06-d51afbf0d986 | -9.16852 | -44.63403 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c33d3c8b-565d-35c8-b4a2-4c09e08361fa | -7.11281 | -47.85777 | 2025-09-20 04:53:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 758cf550-ebfb-3b4a-a2d5-dfab27805e03 | -5.73855 | -42.58643 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 94989d0d-fa7b-39d2-876a-2d7575813c67 | -4.27306 | -48.63795 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9e23e8e4-9fd4-3297-955e-b9c8ab069a68 | -4.63532 | -50.99731 | 2025-09-20 04:53:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59520695-7709-38a2-9cf2-55cecfb95f1b | -3.98642 | -51.06121 | 2025-09-20 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 261749c9-7274-358d-b727-d2dcb8557e20 | -7.18118 | -44.41024 | 2025-09-20 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aacde6be-e778-3b77-a33f-994e2944ae31 | -5.55276 | -42.15678 | 2025-09-20 04:53:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 3aa78e25-f855-3335-a6fb-08aaaa5b7a6a | -5.55795 | -42.1618 | 2025-09-20 04:53:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a5892565-a60c-33f1-a994-d44a9936b4ad | -3.98698 | -51.05766 | 2025-09-20 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ca626f71-cb2c-3512-a19e-bcb958be74c9 | -3.63763 | -52.09655 | 2025-09-20 04:53:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| aef33404-89cf-37f9-b420-a805fc562da6 | -3.98362 | -51.05716 | 2025-09-20 04:53:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 784d5827-dc25-33ce-9465-4e08f25c3a39 | -9.02292 | -46.3327 | 2025-09-20 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33e56276-28dd-3710-8832-0e671c6657d6 | -2.96091 | -48.59712 | 2025-09-20 04:53:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3cea6161-4c27-3ca3-980a-339f945f5865 | -2.55424 | -51.04696 | 2025-09-20 04:53:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 9ccfbf02-087e-33d7-8d58-bb5caa33e6bf | -7.83123 | -45.63894 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4f8a8750-0b8c-3988-86e7-cf2a58f12a52 | -5.44877 | -49.46568 | 2025-09-20 04:53:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b3694b9-e978-3102-83c2-64a224598b18 | -5.8266 | -43.88119 | 2025-09-20 04:53:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0261f450-7932-30af-8740-c3c72d0b683e | -5.52069 | -43.85693 | 2025-09-20 04:53:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9926eb42-9974-3baf-8656-b8e04117e78d | -4.35226 | -48.7286 | 2025-09-20 04:53:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 59a47562-6616-3809-ba3f-b9891c6d23f5 | -8.90074 | -40.43916 | 2025-09-20 04:53:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6c0944fd-f40c-3974-9607-69bfeb70668b | -5.73295 | -42.58536 | 2025-09-20 04:53:00 | NPP-375D | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 1a6c4a7d-0b2c-35c8-a2b2-c85e0105503a | -4.15747 | -47.83378 | 2025-09-20 04:53:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 37874401-9b43-34ea-bddc-c6df40a748e2 | -5.79032 | -43.64759 | 2025-09-20 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 24b59f91-c832-3f53-9d17-07c63a94fe67 | -7.8359 | -45.64001 | 2025-09-20 04:53:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 505e91d8-2df7-392f-9b84-07a4d307b4ec | -5.11175 | -43.20464 | 2025-09-20 04:53:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| cf56ecff-e72a-3a24-8f9e-d0b7c756f90c | -5.29994 | -45.58131 | 2025-09-20 04:53:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 743248f6-a338-3ebb-ac70-92f4d38761b1 | -5.69158 | -51.74301 | 2025-09-20 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 210321db-2eaa-3a06-9a64-3cef2f8ba7db | -2.79947 | -47.15339 | 2025-09-20 04:53:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 60f18683-d287-33b0-8328-8fec8d884248 | -8.14469 | -43.63454 | 2025-09-20 04:53:00 | NPP-375D | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 556e4a3a-2019-34db-9e2f-6e8cc4a08ae5 | -9.11563 | -44.66291 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8349d68e-20b7-39d5-8bfd-83ccdd304096 | -8.96745 | -47.68104 | 2025-09-20 04:53:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
