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

## Dados Diários - Página 90

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a07b37ec-384c-3777-8516-a86daf94d6e4 | -10.60978 | -48.72892 | 2025-10-04 04:14:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 106499b1-b25b-3777-b769-d7b43c4e0480 | -8.38917 | -47.99058 | 2025-10-04 04:14:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| df405d74-27cf-3a8d-96da-427131b233b6 | -13.33062 | -48.07915 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 92c4b2f0-fb37-332a-802d-99e6944109bc | -12.64435 | -46.98473 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1e48285a-79de-3341-b822-58072a910ac2 | -14.21354 | -46.06309 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8bba9053-d136-3bd4-9bd6-78609281259a | -14.93922 | -46.85981 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 5e79dbb2-ab05-341c-b76a-83e8dec0b6f0 | -12.95093 | -42.42016 | 2025-10-04 04:14:00 | NOAA-20 | IBIPITANGA | BAHIA | Brasil | 2912509 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| d5cb720d-faf0-302b-8ff1-783542f09c7d | -14.63231 | -48.25845 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4dca9341-4c54-39ca-a866-a2974224be71 | -13.70487 | -47.34412 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5778bdd8-2a99-3169-837f-e4de0f99a411 | -12.86718 | -46.9964 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9b427ed-1b02-3122-90f4-2f7ea7a95bbc | -8.06135 | -44.80347 | 2025-10-04 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7439dcde-838f-36d6-9e45-c91d8d4ceb84 | -9.93023 | -50.89821 | 2025-10-04 04:14:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7a7620e3-9ed6-3afb-b8ec-01516fd70f89 | -8.05798 | -44.80292 | 2025-10-04 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 441fa54f-b598-3ff0-94ce-a41981218d3f | -13.23383 | -46.43277 | 2025-10-04 04:14:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 290e9aca-2101-3375-b940-337b6b06a52c | -12.91839 | -54.73226 | 2025-10-04 04:14:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8fee454-8a7f-31dc-9240-56b1a017f458 | -14.88122 | -48.2949 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c81df506-d93f-39c6-8969-56c648e5ec99 | -13.98261 | -48.19461 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 17d56cda-f16e-3a07-ab52-53c0630c7ffc | -12.94682 | -50.98769 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 083bfebd-ac29-37b2-a3b5-a5313fddbca2 | -7.77257 | -46.23852 | 2025-10-04 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 747fa6ee-40d2-316a-bb51-c7a55ba48e80 | -10.63884 | -49.07106 | 2025-10-04 04:14:00 | NOAA-20 | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| add947f9-1c28-3211-87e3-9ba0285d1b7c | -13.75592 | -48.04957 | 2025-10-04 04:14:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0e4e5077-49e7-3d44-93fd-c35a94cd9221 | -12.72446 | -48.55673 | 2025-10-04 04:14:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| db6761a5-a04b-360f-a06f-0a9756bc9466 | -13.05506 | -48.70916 | 2025-10-04 04:14:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d0ab695f-2648-3de0-b22c-d8ae92b5b072 | -15.3328 | -46.38942 | 2025-10-04 04:14:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2c9fad7-84ae-3a51-a910-0ff6b26e9be9 | -11.91462 | -46.38552 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 681c6860-30e8-387c-895b-ca5ce46ffc7d | -13.26009 | -47.27193 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 24b63d8b-4026-32df-b53f-86841d0672c8 | -11.07529 | -47.79557 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc0bff1d-51ad-35bb-b3cb-d4f0488d9061 | -14.19396 | -46.67652 | 2025-10-04 04:14:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 499b5e20-4e7c-3f0e-8dd6-22ed70c88a51 | -12.02134 | -45.20038 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7325c418-9f6b-3e68-a4a1-08466aaf6e22 | -14.42478 | -47.14291 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e0d14b-92e8-332c-bf00-71c3c6c35349 | -9.6326 | -54.31702 | 2025-10-04 04:14:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 96436c98-9f3d-3e11-93cb-12be9bc5896c | -13.66217 | -47.8735 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ae47f7f0-f94a-3e95-964c-af651c2760d1 | -14.65696 | -48.28885 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b6312cea-fbb8-390c-9689-8588283957ec | -11.7211 | -44.44376 | 2025-10-04 04:14:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a3c772ae-d6f8-31a5-bbb7-f20603d360ec | -10.59626 | -54.35646 | 2025-10-04 04:14:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 46cc8e8a-968d-362f-a355-468dd61a2bb3 | -11.0763 | -47.72234 | 2025-10-04 04:14:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 77e721e5-bbf2-3646-845a-df65ba706e32 | -11.91435 | -46.36598 | 2025-10-04 04:14:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8bc9620f-3d7b-3952-bc18-bafe32fce8be | -14.64276 | -48.30577 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 74956b40-9cde-355e-9ad8-f0265f958aba | -9.94512 | -50.2401 | 2025-10-04 04:14:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 31b9c5bf-e0bc-30ff-b6a2-6b16de8d5850 | -11.13312 | -47.19003 | 2025-10-04 04:14:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e501cf10-c6cb-3cac-a059-d70a2bab8e26 | -13.38525 | -47.2832 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 35e99e90-321a-377a-b48a-1b68f01b19fb | -13.12324 | -47.82121 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 18.4 |
| f8ff455b-14df-3a98-a5bd-f07192bd0a7e | -12.68686 | -47.56689 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4a5e5b62-fddc-3b1b-81c0-b5403210e559 | -12.28456 | -55.14016 | 2025-10-04 04:14:00 | NOAA-20 | VERA | MATO GROSSO | Brasil | 5108501 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b38bcbe4-77bb-3b82-834a-0af63c0f67f1 | -14.84495 | -48.28857 | 2025-10-04 04:14:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ea9b17de-3236-3d37-9306-e1b500ce3c24 | -12.65751 | -46.97053 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0b8cc590-59c2-39d0-83f0-0e0349386a78 | -12.59831 | -47.00132 | 2025-10-04 04:14:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b0ace637-d5aa-3e4b-a8f3-2de85e511c5e | -12.07867 | -45.18425 | 2025-10-04 04:14:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0a497fcf-a9a4-3686-ac3e-c75173a2621b | -13.32166 | -47.57543 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6f2211a8-8058-33e8-b714-ad954607f62b | -13.34677 | -47.23043 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 68a46ad4-3bbf-3bcd-b9ae-160e101ca61c | -14.60217 | -46.73377 | 2025-10-04 04:14:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3387668-29d1-35b0-b2cd-0640e6b078a1 | -14.92439 | -46.88573 | 2025-10-04 04:14:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 448a1531-41f9-3103-a95b-72cfcee0caf3 | -13.12475 | -47.83422 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 676a37de-e46d-341d-8764-a97e2d5101fe | -9.32514 | -45.74619 | 2025-10-04 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9e9e77a1-eecf-3f40-b4b0-4f4adb70667a | -13.32018 | -47.25943 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 48a4e004-9955-35d7-8918-d0bee282606d | -9.94989 | -43.76575 | 2025-10-04 04:14:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cc2ace7b-dee4-329c-933d-5cca56af1c97 | -10.75983 | -49.72171 | 2025-10-04 04:14:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f88616fc-e674-306e-99a3-0b39a584cf5b | -13.74171 | -47.95823 | 2025-10-04 04:14:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ecbb2f18-fd7c-37e5-9897-9e15c643552e | -13.58355 | -48.17756 | 2025-10-04 04:14:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| ba995efb-695c-3171-846d-a1bf3c24c2d1 | -13.72527 | -51.3127 | 2025-10-04 04:14:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b28f9c23-7532-36f0-8ca8-926a1dd846bb | -11.45286 | -49.71628 | 2025-10-04 04:14:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f8d5ef4f-d113-37c6-a9f9-972a42dc5be7 | -11.69493 | -47.50317 | 2025-10-04 04:14:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a9ccc8bb-1622-3cf5-8569-44495134efdb | -13.29056 | -47.8329 | 2025-10-04 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b46882f6-e487-3a3f-b3d9-4506cb11aa23 | -13.55866 | -44.09525 | 2025-10-04 04:14:00 | NOAA-20 | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a2d28385-cb74-3c1d-990b-daa43c457275 | -13.25726 | -47.26713 | 2025-10-04 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 35716985-ec37-3238-b80e-91b698b8b03d | -10.82885 | -46.58495 | 2025-10-04 04:14:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3deb4b9d-0dfb-3237-8735-ceb62d81bfbc | -11.82499 | -45.04788 | 2025-10-04 04:14:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e592f09c-94ec-3694-be6d-6d854fc92ea5 | -15.53093 | -46.82863 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1f90300c-7e40-3d51-b325-6ad285f04ea7 | -22.28154 | -46.73235 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c15319fb-8a75-3a44-bc27-4674bcd1dc4b | -16.01106 | -50.85328 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b0caab0-bf2e-324d-b201-560c0579b6f1 | -20.71881 | -49.60789 | 2025-10-04 04:17:00 | NOAA-20 | BÁLSAMO | SÃO PAULO | Brasil | 3504800 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4c68d415-a31b-313f-8a21-901d710636cd | -18.42068 | -43.48923 | 2025-10-04 04:17:00 | NOAA-20 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 4d49db4a-261c-3e33-b0ca-df9eda560ef9 | -19.6007 | -44.86491 | 2025-10-04 04:17:00 | NOAA-20 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 79049ae2-88e4-3328-acd3-c5171e373783 | -14.98974 | -49.95444 | 2025-10-04 04:17:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2328ec8-5054-3859-8fbd-24f19a6789e0 | -15.37522 | -47.95676 | 2025-10-04 04:17:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7d8f8f4b-8cc0-3963-85e0-862e8738dc09 | -21.19588 | -45.14513 | 2025-10-04 04:17:00 | NOAA-20 | LAVRAS | MINAS GERAIS | Brasil | 3138203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| 89cf2aab-bdff-3de8-ae71-9e1e8dbda1a9 | -15.33965 | -47.32577 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 513d3211-b541-30f5-b3cc-6a01c7c04b34 | -15.74272 | -46.27011 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dce2158-90e3-3b12-8e79-05c5f6ff47d9 | -22.20438 | -46.76799 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 81aab257-f875-3d01-b877-89f1640cad33 | -15.85737 | -44.45936 | 2025-10-04 04:17:00 | NOAA-20 | SÃO FRANCISCO | MINAS GERAIS | Brasil | 3161106 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 68376a29-25e0-3361-bf7d-50f0fd7fd231 | -16.02068 | -50.84738 | 2025-10-04 04:17:00 | NOAA-20 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6f5a5515-0f49-3c50-a001-2259b977a706 | -16.0171 | -50.94624 | 2025-10-04 04:17:00 | NOAA-20 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| be9d34dc-fc25-3d6e-b088-7657dc87defe | -15.60569 | -52.48196 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 042c1cd3-8206-3b61-abb4-775c3587ee4f | -19.97099 | -43.70361 | 2025-10-04 04:17:00 | NOAA-20 | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b1cd3e34-6313-3985-adb2-3e55e632bd0c | -22.28191 | -46.75154 | 2025-10-04 04:17:00 | NOAA-20 | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 1f6e5285-86d2-315a-ac23-0251b02fbe67 | -15.52359 | -46.82818 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ceb6506-ab25-346f-be39-934744773bde | -21.68345 | -50.0658 | 2025-10-04 04:17:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 16e354c1-1541-3282-b4d3-1560b2da3534 | -15.79312 | -46.25623 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 57b6d01e-5979-3d57-a281-09283bafb1fb | -18.66598 | -43.86309 | 2025-10-04 04:17:00 | NOAA-20 | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c6a1d744-ff47-30d3-be6c-caa13ec64977 | -15.72021 | -46.28916 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1da643e3-c390-33f7-b422-bb10bd51879d | -17.15956 | -47.02135 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1262522a-4c36-3c03-96c4-dad679acae93 | -15.73997 | -46.26584 | 2025-10-04 04:17:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| eaf84d5f-8a12-39ff-82cf-1c2e3106ea0d | -15.60294 | -52.47115 | 2025-10-04 04:17:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 23d88a47-eba3-3485-8c12-f423f7179a58 | -18.17208 | -53.34204 | 2025-10-04 04:17:00 | NOAA-20 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 16b95060-70ba-3e09-b6bf-c376ed6bde14 | -15.62155 | -46.938 | 2025-10-04 04:17:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4ec56beb-3288-305d-8ee0-31f9af9c47a7 | -19.57422 | -48.01653 | 2025-10-04 04:17:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 5b1cc424-ca48-3efb-8dde-98553e7cc8c7 | -21.09356 | -46.66246 | 2025-10-04 04:17:00 | NOAA-20 | JACUÍ | MINAS GERAIS | Brasil | 3134806 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8b60d608-4c02-372c-a0bd-1d8954aa6ec3 | -20.47432 | -44.82508 | 2025-10-04 04:17:00 | NOAA-20 | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 707753b2-9749-34b1-8db5-fa321c113b87 | -17.1543 | -47.03207 | 2025-10-04 04:17:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42c28983-5f38-35cc-9a27-42b1463bec04 | -15.02785 | -49.45342 | 2025-10-04 04:17:00 | NOAA-20 | NOVA GLÓRIA | GOIÁS | Brasil | 5214861 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README91.md)
