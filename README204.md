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

## Dados Diários - Página 204

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5b7bf405-af35-31e5-9f2d-5c2723cf17e3 | -7.67666 | -36.84904 | 2024-10-02 12:14:00 | TERRA_M-T | SUMÉ | PARAÍBA | Brasil | 2516300 | 25 | 33 | nan | nan | nan | Caatinga | 14.9 |
| c56dab52-1953-329e-87e6-38677b3bedc1 | -4.52682 | -38.17234 | 2024-10-02 12:14:00 | TERRA_M-T | BEBERIBE | CEARÁ | Brasil | 2302206 | 23 | 33 | nan | nan | nan | Caatinga | 20.4 |
| f4106200-1fba-3cfc-9c95-33bfa3ff5524 | -6.41831 | -38.21679 | 2024-10-02 12:14:00 | TERRA_M-T | TENENTE ANANIAS | RIO GRANDE DO NORTE | Brasil | 2414100 | 24 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 816a8cdd-ecfe-3e85-8abd-870f96eb7004 | -6.38959 | -37.64071 | 2024-10-02 12:14:00 | TERRA_M-T | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 18.9 |
| 86b8b011-8dca-36c6-83a6-f0db46710616 | -6.37115 | -37.96729 | 2024-10-02 12:14:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 23.1 |
| c90a95b9-62f5-3cca-8e56-fe63b6f64255 | -6.36982 | -37.97662 | 2024-10-02 12:14:00 | TERRA_M-T | ALEXANDRIA | RIO GRANDE DO NORTE | Brasil | 2400505 | 24 | 33 | nan | nan | nan | Caatinga | 20.3 |
| 44dda704-07c3-3e4f-800e-f2f121121a30 | -6.33143 | -37.72076 | 2024-10-02 12:14:00 | TERRA_M-T | CATOLÉ DO ROCHA | PARAÍBA | Brasil | 2504306 | 25 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 0fd3cf06-cb01-32c5-b0df-3b03489b5f25 | -5.14092 | -37.42047 | 2024-10-02 12:14:00 | TERRA_M-T | MOSSORÓ | RIO GRANDE DO NORTE | Brasil | 2408003 | 24 | 33 | nan | nan | nan | Caatinga | 8.6 |
| b2f778e2-a18e-3046-99a3-7745f0bb5c13 | -7.91496 | -38.44555 | 2024-10-02 12:14:00 | TERRA_M-T | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 9.1 |
| fa10595d-8d3e-3ea1-8fc4-44b21544b604 | -7.75635 | -37.67389 | 2024-10-02 12:14:00 | TERRA_M-T | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 36fd6977-3b98-3ec2-9610-b1b1d3b0ca67 | -7.4714 | -38.39072 | 2024-10-02 12:14:00 | TERRA_M-T | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 2fdbaa2b-ab39-31d8-aa4f-04a5aaadfb85 | -7.46367 | -38.38015 | 2024-10-02 12:14:00 | TERRA_M-T | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 28.1 |
| 0e01aa3c-b33a-3b73-ba58-7ee7c01686c3 | -7.46236 | -38.38943 | 2024-10-02 12:14:00 | TERRA_M-T | IBIARA | PARAÍBA | Brasil | 2506608 | 25 | 33 | nan | nan | nan | Caatinga | 43.4 |
| 5ad9c78a-fbbe-3b63-af10-375ccb48e796 | -7.31702 | -37.86013 | 2024-10-02 12:14:00 | TERRA_M-T | OLHO D'ÁGUA | PARAÍBA | Brasil | 2510402 | 25 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 63a86101-aac1-348b-a1a8-8959590137cd | -6.94436 | -37.94595 | 2024-10-02 12:14:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5c06445b-4846-3c6b-9be5-564ef059f0e0 | -6.94303 | -37.95544 | 2024-10-02 12:14:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 8.8 |
| e9d80b0c-f22f-3b4a-8d28-9d7f3d823b6f | -6.936 | -37.94808 | 2024-10-02 12:14:00 | TERRA_M-T | POMBAL | PARAÍBA | Brasil | 2512101 | 25 | 33 | nan | nan | nan | Caatinga | 33.7 |
| f8be4a1a-8983-3fe3-85a0-469a2e5e3a57 | -8.18198 | -42.5487 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 0467d905-7e92-38f5-a7b2-981340b678fb | -8.19171 | -42.55015 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 16.5 |
| ee4ed43e-4eb8-340f-be0a-78f6b9a82dee | -8.21294 | -42.55945 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 7b5c74f7-000b-3809-a2df-12015d5929b6 | -8.2146 | -42.5486 | 2024-10-02 12:14:00 | TERRA_M-T | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| d53f96b4-879e-35a0-83ba-fae75f10dcfd | -8.17274 | -43.68781 | 2024-10-02 12:14:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 30.9 |
| 3664e0ec-97c3-3321-8b9c-6a5532cdc2d4 | -8.1747 | -43.67508 | 2024-10-02 12:14:00 | TERRA_M-T | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Cerrado | 22.5 |
| 0b07966c-2b9e-3497-a012-07302c9f5c66 | -6.50443 | -43.14835 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 22.1 |
| ca76bbe2-84d5-3592-a880-5652f262482d | -6.59893 | -42.99392 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 6653a06c-7ef7-3333-93a0-011d00fbf977 | -6.60918 | -42.99544 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 9b65d132-e01e-3d75-a470-ea2dd2e252d1 | -6.611 | -42.98347 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 0e21697f-2329-3096-8f71-5ddac33858bb | -6.65917 | -43.13355 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 7f38953c-64e1-3b88-a40e-18c5befc2d7e | -6.66016 | -43.05877 | 2024-10-02 12:14:00 | TERRA_M-T | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 891a0328-ab58-33bb-b86c-c8841c430f42 | -7.63352 | -42.45144 | 2024-10-02 12:14:00 | TERRA_M-T | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 2bc15411-c4d3-3dd9-b341-674b261e9078 | -7.70558 | -42.99147 | 2024-10-02 12:14:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 21.9 |
| 50bdb580-bdc0-38df-a523-fcbd899d30c0 | -7.85469 | -43.08667 | 2024-10-02 12:14:00 | TERRA_M-T | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | 14.8 |
| fe0f3f51-d6f3-35d4-8106-fa4d6350a7e9 | -7.73994 | -43.79034 | 2024-10-02 12:14:00 | TERRA_M-T | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| b186be04-a9d0-35dc-bc2c-65475d126e53 | -5.81746 | -42.54292 | 2024-10-02 12:14:00 | TERRA_M-T | BARRO DURO | PIAUÍ | Brasil | 2201408 | 22 | 33 | nan | nan | nan | Caatinga | 12.9 |
| 1691e5ff-0b25-3a91-a4bd-64fea780ba89 | -5.92831 | -42.83122 | 2024-10-02 12:14:00 | TERRA_M-T | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 52.5 |
| 7d3e52c3-bd84-3b15-9faa-490acf9eb17f | -5.93419 | -41.97115 | 2024-10-02 12:14:00 | TERRA_M-T | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f81c24de-eca9-3e4a-830c-26884b4c3bca | -6.15973 | -42.9216 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 98.5 |
| 51015bb0-7ee8-3031-94f1-e3b1f7081f9f | -6.16169 | -42.90866 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 590.7 |
| b152e607-61d8-3787-8b1e-c03de129aa3b | -6.16348 | -42.89688 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 83.3 |
| b4c17344-264d-327f-8847-d95ff2da304f | -6.17005 | -42.92279 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.2 |
| 13330f61-a2b8-3e02-8326-392e664e48e5 | -6.17189 | -42.91059 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 264.8 |
| 9a86de78-450c-308b-9433-9eda365865cd | -6.17368 | -42.89872 | 2024-10-02 12:14:00 | TERRA_M-T | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 33.6 |
| 007c88da-0d78-3349-badd-2fb18fd2aa29 | -6.32896 | -43.48155 | 2024-10-02 12:14:00 | TERRA_M-T | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| cfc15330-f271-3194-8f64-9105c9e2efa0 | -19.99792 | -44.52187 | 2024-10-02 12:17:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| 1dbfb970-5692-3013-a1ce-544fd0e54dc6 | -20.00728 | -44.52335 | 2024-10-02 12:17:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.3 |
| 3d3f4d11-dc71-36b0-a2e2-bff68c5a9fea | -20.00892 | -44.513 | 2024-10-02 12:17:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 19.7 |
| 6a27f95b-8202-3b5c-8005-94cd879c2804 | -20.01822 | -44.51487 | 2024-10-02 12:17:00 | TERRA_M-T | ITAÚNA | MINAS GERAIS | Brasil | 3133808 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.8 |
| df79f8be-fd68-359a-88c5-5a06f201dfbb | -19.74735 | -44.25155 | 2024-10-02 12:17:00 | TERRA_M-T | ESMERALDAS | MINAS GERAIS | Brasil | 3124104 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| aaf4f2d8-d53d-3781-bed6-75a9fa3998ad | -18.32159 | -43.2537 | 2024-10-02 12:17:00 | TERRA_M-T | SERRA AZUL DE MINAS | MINAS GERAIS | Brasil | 3166501 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| 9bb1952d-2562-3d17-b1cc-b3c1dc6c7ebd | -18.32304 | -43.24403 | 2024-10-02 12:17:00 | TERRA_M-T | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 57.8 |
| 39de59e2-eb56-3dd9-a5eb-490c30c96853 | -18.11921 | -43.91537 | 2024-10-02 12:17:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 6504b612-703a-39d6-b0f0-d2355caff0fa | -18.35023 | -44.02732 | 2024-10-02 12:17:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 8.9 |
| d3906a8e-7165-3047-b8f8-be5f06f5f3b2 | -18.37821 | -44.03163 | 2024-10-02 12:17:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 65c359e8-5aca-3eaf-8179-b753ca05e04e | -18.37978 | -44.02149 | 2024-10-02 12:17:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 30.4 |
| 4322859a-4d26-324a-a555-103b3733bddd | -18.38911 | -44.02287 | 2024-10-02 12:17:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| b34b5a59-fb47-3d21-a6b4-c0924238f99c | -18.3907 | -44.01254 | 2024-10-02 12:17:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4bda77a9-842f-35c9-be95-e780fffb800a | -18.58004 | -43.91923 | 2024-10-02 12:17:00 | TERRA_M-T | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 6c4a2e5a-dc8e-349f-883f-bc1a71b1d7ed | -18.90775 | -44.65374 | 2024-10-02 12:17:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 464d2389-2753-33ef-89ef-ccb1734df62a | -18.91729 | -44.65539 | 2024-10-02 12:17:00 | TERRA_M-T | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| d85029e6-c1d3-304d-a25c-fac72e7d44e9 | -17.26183 | -43.18283 | 2024-10-02 12:17:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 27dd0889-6a53-3e57-beff-5db44aef2123 | -17.62887 | -43.25691 | 2024-10-02 12:17:00 | TERRA_M-T | DIAMANTINA | MINAS GERAIS | Brasil | 3121605 | 31 | 33 | nan | nan | nan | Cerrado | 15.5 |
| f9893572-0209-3b4f-b20f-20c7a9c07be8 | -17.63037 | -43.24706 | 2024-10-02 12:17:00 | TERRA_M-T | SENADOR MODESTINO GONÇALVES | MINAS GERAIS | Brasil | 3165909 | 31 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 79fc49fa-4733-3048-bb95-5c917f11304e | -17.959 | -44.35447 | 2024-10-02 12:17:00 | TERRA_M-T | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 14.2 |
| 264c868d-fb3e-33a8-a9b0-252958fc682b | -16.42158 | -44.08994 | 2024-10-02 12:17:00 | TERRA_M-T | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d9c1f791-6618-3f9b-a18c-fdcccc21132b | -14.22287 | -42.17225 | 2024-10-02 12:17:00 | TERRA_M-T | RIO DO ANTÔNIO | BAHIA | Brasil | 2926806 | 29 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 59ba3af7-afaa-3867-bf67-eea3e9a7ca20 | -12.95556 | -43.3626 | 2024-10-02 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| efeebd24-ea7f-32a9-ae9a-c619d57ee952 | -12.96352 | -43.37479 | 2024-10-02 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 90f4022e-7e74-3da2-927c-58d870781d84 | -12.96515 | -43.36411 | 2024-10-02 12:17:00 | TERRA_M-T | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e2c2c790-9513-36fd-bca4-cf9afd8920e6 | -12.64776 | -42.22137 | 2024-10-02 12:17:00 | TERRA_M-T | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 5fcfb8dd-810b-321f-856d-0ec7f7392b08 | -12.94024 | -42.47994 | 2024-10-02 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 89834f50-7574-3e67-962c-d2d14aef81ba | -12.94943 | -42.48136 | 2024-10-02 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 57.2 |
| 31c401fe-13e5-3178-a476-c573e4b07f2e | -12.9509 | -42.47162 | 2024-10-02 12:17:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| e04be720-cd8f-351b-9e65-d1069e7eb4f4 | -19.67783 | -42.94226 | 2024-10-02 12:17:00 | TERRA_M-T | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 8a953a7e-39ae-3fe2-b945-1d6adedf071b | -19.67925 | -42.93272 | 2024-10-02 12:17:00 | TERRA_M-T | ANTÔNIO DIAS | MINAS GERAIS | Brasil | 3103009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| 3a81d5cf-0dc2-3a88-98ad-b5afe3d6a290 | -19.89462 | -43.15525 | 2024-10-02 12:17:00 | TERRA_M-T | RIO PIRACICABA | MINAS GERAIS | Brasil | 3155702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.1 |
| e6e2212d-9d79-3680-bba0-5056ad5b3614 | -20.04807 | -42.04087 | 2024-10-02 12:17:00 | TERRA_M-T | SIMONÉSIA | MINAS GERAIS | Brasil | 3167608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.3 |
| 054c2c86-a892-3068-930f-99758d01b041 | -18.0663 | -42.61942 | 2024-10-02 12:17:00 | TERRA_M-T | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 5a35a8bf-c1db-3c50-95c3-e1abde980949 | -18.06769 | -42.61008 | 2024-10-02 12:17:00 | TERRA_M-T | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.1 |
| 5cc6ec8a-8ae9-3c06-b80b-e9e4c787105b | -18.06907 | -42.60076 | 2024-10-02 12:17:00 | TERRA_M-T | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 11db495a-f72c-306c-a791-4c1925e722bc | -18.20626 | -42.16378 | 2024-10-02 12:17:00 | TERRA_M-T | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 16.4 |
| 36b3ae1b-308e-31d6-81de-051d5ed579ef | -18.34278 | -43.05092 | 2024-10-02 12:17:00 | TERRA_M-T | RIO VERMELHO | MINAS GERAIS | Brasil | 3156007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.5 |
| 031b3d1c-6504-3085-867d-fcd04fbb1d4c | -16.10619 | -41.33347 | 2024-10-02 12:17:00 | TERRA_M-T | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 416a7cb9-c32b-3bce-89dd-62bba8623369 | -16.25599 | -41.76906 | 2024-10-02 12:17:00 | TERRA_M-T | COMERCINHO | MINAS GERAIS | Brasil | 3117009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 45108e00-b554-3113-a710-c4b84ae28bbe | -16.29139 | -41.32685 | 2024-10-02 12:17:00 | TERRA_M-T | MEDINA | MINAS GERAIS | Brasil | 3141405 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.6 |
| a6e80086-882f-32cf-b53c-af311071175d | -15.76538 | -42.40219 | 2024-10-02 12:17:00 | TERRA_M-T | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 76d12939-c616-3f67-b182-c854adc0b834 | -15.01121 | -41.19732 | 2024-10-02 12:17:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| ec48a28b-b7d1-3653-b4df-ff020100a837 | -14.77893 | -41.21542 | 2024-10-02 12:17:00 | TERRA_M-T | BELO CAMPO | BAHIA | Brasil | 2903508 | 29 | 33 | nan | nan | nan | Caatinga | 7.1 |
| bda17457-ff6a-30ca-9c8b-5b79879a7db6 | -14.86981 | -41.41224 | 2024-10-02 12:17:00 | TERRA_M-T | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| d0c2192a-9a79-3034-8a2a-2a73bb5c7833 | -13.50133 | -40.93176 | 2024-10-02 12:17:00 | TERRA_M-T | IRAMAIA | BAHIA | Brasil | 2914307 | 29 | 33 | nan | nan | nan | Caatinga | 7.5 |
| d8e077dd-4da3-3a87-9501-b3fa5fae6c3d | -19.43633 | -41.35423 | 2024-10-02 12:17:00 | TERRA_M-T | SANTA RITA DO ITUETO | MINAS GERAIS | Brasil | 3159506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.8 |
| b2bc8ac7-123a-3106-a886-8a68ec16ea2b | -17.90486 | -40.1198 | 2024-10-02 12:17:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.3 |
| 1c30bcf9-2bdd-311f-b4d5-cfe9a313e413 | -17.94087 | -40.39446 | 2024-10-02 12:17:00 | TERRA_M-T | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| 3fc91c6b-bf70-3093-a241-fa564d9f0c57 | -17.94221 | -40.38462 | 2024-10-02 12:17:00 | TERRA_M-T | MUCURICI | ESPÍRITO SANTO | Brasil | 3203601 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| cc77e3cc-d26c-30b4-be2c-9b170388ad15 | -13.18531 | -45.4495 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 361.7 |
| 5ed893fc-10c1-3359-ad5b-93558d3038fa | -13.18295 | -45.46369 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 659.0 |
| 17b62b75-d617-35c2-ae48-e2ea48bad4eb | -13.18227 | -45.45681 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1276.3 |
| 8f03498e-fc3c-3949-abbe-c244802cf865 | -13.17999 | -45.47111 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 185.7 |
| 331c4b16-6410-3d2a-b750-e8eebe4e6d02 | -13.17129 | -45.45491 | 2024-10-02 12:17:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| d8c8d8a8-e073-34bb-acec-bb942b665c01 | -14.56884 | -46.42678 | 2024-10-02 12:17:00 | TERRA_M-T | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 25a4cc32-126d-322b-97f5-7702123d8aa2 | -15.33578 | -46.73447 | 2024-10-02 12:17:00 | TERRA_M-T | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 66.9 |


[Clique aqui para ver as próximas entradas](README205.md)
