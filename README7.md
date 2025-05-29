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
| 87931a40-0eed-39d8-a318-601e1816c055 | -10.71977 | -49.54391 | 2025-05-29 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8622c7ac-7a1c-3d2b-82d8-60ba8286c6cc | -12.10031 | -44.7485 | 2025-05-29 03:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 79208117-dfc6-367b-a28e-1feb0c043eaf | -15.32502 | -43.07568 | 2025-05-29 03:51:00 | NPP-375D | CATUTI | MINAS GERAIS | Brasil | 3115474 | 31 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 3d35d1bc-ef76-3e5c-b993-c238f1401658 | -10.95004 | -48.15282 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 439587bc-f095-3c52-9b9d-7bbeee6ab4c8 | -11.81669 | -44.27143 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 27.5 |
| c6ab9a09-b662-32bb-9dd5-7e8a630f15c0 | -10.726 | -49.54511 | 2025-05-29 03:51:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c0b31cfe-82e0-302e-97a2-ac8eae69bf68 | -14.67534 | -45.09317 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 85974133-0860-36a4-b010-5b00696041be | -10.52969 | -47.58274 | 2025-05-29 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e7018369-49ce-3d55-a14b-1ae46893fb8b | -10.67233 | -44.4145 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| b65040ae-8aeb-3ce0-ba5d-303761517c88 | -11.28224 | -46.4387 | 2025-05-29 03:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 2c37126e-8ba0-3664-9ef7-7fc85b3cb498 | -11.97419 | -52.46292 | 2025-05-29 03:51:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| f57733f6-3c90-3d2f-9785-7caf0db29148 | -12.26115 | -44.60813 | 2025-05-29 03:51:00 | NPP-375D | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 24be4698-1508-348a-b24c-82c4cdaacf9e | -12.30434 | -47.27296 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9873b5c5-0f21-35eb-ae99-93fae20aebe9 | -10.95869 | -47.44658 | 2025-05-29 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5cff5cb7-4e81-3d92-9062-6a6c111f7a56 | -10.95801 | -47.45006 | 2025-05-29 03:51:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 06753930-05c9-3250-abe9-fd78e067fd3e | -12.39316 | -49.97142 | 2025-05-29 03:51:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 693c5f0f-b4d1-318e-868a-6a61355078a0 | -14.66309 | -45.08626 | 2025-05-29 03:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ddc75181-8b65-3d82-b637-60cc40e0334f | -11.81821 | -44.26301 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 82feef76-8583-3503-b666-155c272d385d | -11.91883 | -44.55517 | 2025-05-29 03:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f10e0217-03d3-380a-af25-379962f51178 | -18.18269 | -42.63972 | 2025-05-29 03:51:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 3dd22b93-f8d3-3e67-b762-fdc5d69b1bc5 | -10.73346 | -49.28839 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 6730432c-0270-37ac-8cd0-4f135f8deade | -10.67757 | -44.41108 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7f69001d-029f-3b95-b5c2-171825073d94 | -11.82255 | -44.26382 | 2025-05-29 03:51:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 194ed16c-cf78-377d-abd2-0d9a451677a7 | -18.17911 | -42.63905 | 2025-05-29 03:51:00 | NPP-375D | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 783f8b8c-8cb0-30f3-84a6-9b7a16112664 | -10.95541 | -48.16017 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c73bc962-a374-39ab-a1ac-7cc178a420e6 | -10.73708 | -49.29541 | 2025-05-29 03:51:00 | NPP-375D | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5610a7fa-6116-31f9-b57a-093f65389c8c | -13.07886 | -45.28928 | 2025-05-29 03:51:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 329aa0ce-bcb6-3782-9056-ea970e91be25 | -11.78203 | -37.86272 | 2025-05-29 03:51:00 | NPP-375D | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ad11d225-06e4-3230-8862-c1783dd5886a | -12.10477 | -44.74927 | 2025-05-29 03:51:00 | NPP-375D | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 77ec0cab-2c1b-3b20-8a9d-d53eecf8404d | -10.65577 | -44.49686 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7631d9fd-c7ca-3342-855f-4e31b07a15ce | -10.66789 | -44.41356 | 2025-05-29 03:51:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3610bcac-d768-3bea-b712-87d5d92acca1 | -12.30557 | -47.26643 | 2025-05-29 03:51:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d578c598-78ea-3357-9dd7-4640f4e5d1f7 | -10.95128 | -48.15113 | 2025-05-29 03:51:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2e02f869-f7fb-3f7c-ab86-b398ce81d256 | -15.80468 | -43.56611 | 2025-05-29 03:51:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a02ec5c-3f16-3480-b250-feff2c6cab04 | -20.98609 | -44.29277 | 2025-05-29 03:53:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 321649e7-0293-30c6-86dc-9b9bd7fc84f6 | -19.43872 | -44.33946 | 2025-05-29 03:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f428cce4-f71a-3b1c-8707-d1351904fec8 | -22.67772 | -42.85692 | 2025-05-29 03:53:00 | NPP-375D | ITABORAÍ | RIO DE JANEIRO | Brasil | 3301900 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 76b4b2e4-fe8e-33e5-b271-c7d1a76ba557 | -19.4716 | -44.29568 | 2025-05-29 03:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 944137e5-7896-386e-bbfc-d124f4af7789 | -21.59443 | -44.29778 | 2025-05-29 03:53:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b00a668c-abe0-3fd9-a91f-e8bab1a46701 | -19.46991 | -44.29868 | 2025-05-29 03:53:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| deb46b2d-2d86-3c27-9a97-a5962ba14087 | -18.38018 | -44.51822 | 2025-05-29 03:53:00 | NPP-375D | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 95cc6848-cca4-313d-ae42-e0f65644bca0 | -20.98671 | -44.29082 | 2025-05-29 03:53:00 | NPP-375D | RITÁPOLIS | MINAS GERAIS | Brasil | 3156106 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| 3105fdd6-82df-39e3-9965-5fb617bddbb9 | -20.90567 | -44.2246 | 2025-05-29 03:53:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f0b5b189-62f5-3066-a0fd-e5adca105bd6 | -20.90939 | -44.22542 | 2025-05-29 03:53:00 | NPP-375D | RESENDE COSTA | MINAS GERAIS | Brasil | 3154200 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 81d7bad3-409d-3fed-9ad3-e6e2e5c32ad4 | -20.31025 | -45.585 | 2025-05-29 03:53:00 | NPP-375D | ARCOS | MINAS GERAIS | Brasil | 3104205 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac00f498-cfcd-3ab7-91e9-846b1704ce73 | -28.58736 | -49.44307 | 2025-05-29 03:55:00 | NPP-375D | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b9b9516-50b8-3c39-9576-06300cc13908 | -3.28766 | -43.46602 | 2025-05-29 04:10:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 51372511-c726-3a25-bed7-35b658f4f06a | -2.44403 | -47.46938 | 2025-05-29 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 36168cdf-198f-34fa-ba0c-de4f60e9e456 | -3.13413 | -40.98952 | 2025-05-29 04:10:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| fc4f8abe-b94f-3c6e-8d9a-37f3fd71e64b | -3.13076 | -40.989 | 2025-05-29 04:10:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 38a97f26-0e7c-3155-b62b-e2202abb43ac | -2.44343 | -47.47306 | 2025-05-29 04:10:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd47f4f7-10a6-34b1-846d-977c25bde9ec | -8.00927 | -46.151 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 090e7efd-6af3-3fd3-810d-a93b251ee370 | -4.82114 | -44.35581 | 2025-05-29 04:12:00 | NOAA-20 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ad648e70-4104-3e38-a3fe-b9bf5993a962 | -2.65462 | -48.79548 | 2025-05-29 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 950e0293-bf25-3cba-aa98-b2c789372e0a | -8.79414 | -47.94125 | 2025-05-29 04:12:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c83b547e-dc56-3874-8397-b0c8d941161f | -8.89785 | -44.78236 | 2025-05-29 04:12:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0954340e-8c53-32c7-a615-5682fc5159df | -7.59127 | -45.95996 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 977355d8-0d16-39bd-978c-bcbea9acc685 | -8.66711 | -48.28749 | 2025-05-29 04:12:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ca194f96-16a3-381a-a055-244d81f98bf8 | -6.22536 | -43.34468 | 2025-05-29 04:12:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| be5135ec-6f09-31d6-9c5f-b2e411bc62d2 | -7.07681 | -44.92088 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 622c77d3-d96b-3777-ba19-0f306269fc1f | -6.82968 | -44.64612 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3ef3435e-d30a-3139-941b-b9bbfbef3ea9 | -9.08796 | -47.71903 | 2025-05-29 04:12:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 75414c33-506c-3dd4-b6cf-fdaab72ecc5e | -7.23863 | -43.10123 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 4efa6a1a-8f59-3b17-8bd5-4c7304a62c07 | -7.24471 | -43.10573 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 677746b2-af49-3080-8301-ec744be3b3e6 | -5.96256 | -43.75914 | 2025-05-29 04:12:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 73391835-f205-3176-a109-9adccf199172 | -7.61959 | -45.74368 | 2025-05-29 04:12:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 323d074e-9aaa-318c-ae98-e11e107c4888 | -6.82514 | -44.65277 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 022b076a-b77e-3469-b5ce-09616ec0c3d7 | -8.40295 | -47.10238 | 2025-05-29 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47e907e3-730f-3247-951f-fe7467b33841 | -7.07221 | -44.92767 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 56f4474e-9c47-3385-bcd8-1761e7f02939 | -8.62856 | -45.34258 | 2025-05-29 04:12:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a9f7b8d4-2331-385a-b02d-f35798245f81 | -7.18295 | -43.11019 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3495dff4-a846-34ac-95ff-14761e96d2a8 | -5.30731 | -43.072 | 2025-05-29 04:12:00 | NOAA-20 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 86520183-3a80-39a5-ab0d-a760e76c38e8 | -7.58642 | -45.85815 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0c4576b8-a855-385b-8347-025ff402a6ca | -2.65316 | -48.80428 | 2025-05-29 04:12:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b601051-0da9-33ea-bb16-beb6daf48459 | -7.2789 | -44.22102 | 2025-05-29 04:12:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| fe88d6be-3be2-3bf5-ad54-3ae8a5582bb9 | -7.09239 | -46.04153 | 2025-05-29 04:12:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d7babbb6-2e74-3c35-a314-80393eb1eeee | -7.94975 | -44.85098 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80d22a53-39ba-3017-9fb4-7b06dcfcb68f | -6.82853 | -44.65327 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cc1e01b5-ed6a-379b-983f-214c631f646e | -4.23061 | -48.97487 | 2025-05-29 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d78271e-8dc5-33a8-a90b-6a1e36e969e3 | -4.8088 | -43.15252 | 2025-05-29 04:12:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.3 |
| ad5ed7c3-e9b0-3801-b684-21aa331bfb88 | -6.8291 | -44.64969 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d820f5a8-6d39-3156-80ef-205cee0744f6 | -6.03137 | -44.0508 | 2025-05-29 04:12:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| f432327c-938d-352f-8109-5517b75c3d56 | -8.09178 | -46.28785 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 33441b23-97bd-3c40-876d-2c31e45d4bf9 | -6.82794 | -44.65688 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 375910fa-4adf-3ffb-a913-84c5eaf588b4 | -8.40072 | -47.09306 | 2025-05-29 04:12:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| de1881b8-c0c0-3c21-94a1-cfaa63f4804f | -7.58137 | -45.9543 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 719b78d9-5392-3c1d-95b7-c568ffdb2cc5 | -7.43728 | -45.42056 | 2025-05-29 04:12:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c5be18fd-e087-3007-96fc-0c30a8864fe5 | -7.07901 | -44.92876 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 82f0205d-e957-3225-a850-06a7226942b2 | -7.0824 | -44.92933 | 2025-05-29 04:12:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b050bc3-8bdd-3e33-9fb2-4fd56878021e | -7.5418 | -43.35524 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e22a5f0-473d-399a-b050-721ad0bf29ff | -7.55719 | -43.32217 | 2025-05-29 04:12:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 64d2cd83-dc72-396e-9347-d361f1efda84 | -3.9606 | -41.48341 | 2025-05-29 04:12:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 78162c82-c584-38c8-b9b3-a116031f0c5e | -7.95073 | -44.85489 | 2025-05-29 04:12:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7da86c37-4acd-35b1-8387-1b5b428abf47 | -7.98299 | -49.68994 | 2025-05-29 04:12:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c97efeb9-081b-39b9-bc68-30b5c3ebef63 | -8.09533 | -46.28844 | 2025-05-29 04:12:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95d6d96e-6bb3-3ed8-9909-95732ce26f3a | -6.82572 | -44.64919 | 2025-05-29 04:12:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 74b6b4e6-7b48-366b-9989-34573d083f38 | -7.18735 | -43.10379 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 4c2f562c-d36b-33bd-bb00-b549efc2ced4 | -3.58171 | -48.95028 | 2025-05-29 04:12:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d7196055-2100-3684-93e3-b979e66c0817 | -7.23918 | -43.09776 | 2025-05-29 04:12:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 7f8ab156-214c-3a28-94ef-9e4417535b22 | -6.6324 | -47.34367 | 2025-05-29 04:12:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README8.md)
