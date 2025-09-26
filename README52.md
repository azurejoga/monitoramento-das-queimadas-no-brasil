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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 93fb6ad7-c89e-3205-b2ce-c226c59c3c30 | -11.4221 | -45.0025 | 2025-09-26 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 245.9 |
| ff72c94f-868c-34af-b0ed-d8a413679a3f | -6.5801 | -45.1117 | 2025-09-26 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 130.5 |
| d0df0eed-396f-3a40-b66f-350c633ee875 | -11.4233 | -44.9331 | 2025-09-26 13:10:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 6929e4cb-39f7-3c9f-895e-374544845a77 | -10.0065 | -44.1533 | 2025-09-26 13:10:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3a84f162-14d7-341f-b680-7f81c4455ca5 | -6.9303 | -45.6931 | 2025-09-26 13:10:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 6b587366-aa5d-3ce9-b0d1-72d1ceb3caab | -11.6233 | -44.4398 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.5 |
| d46e956a-2f66-3445-9731-ed1dfadcc8a5 | -10.4129 | -46.142 | 2025-09-26 13:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.8 |
| d4c44d0c-5525-3557-adda-986e144b34b7 | -11.7006 | -44.4049 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.4 |
| bc30d65c-f52e-3e17-8fcc-355ce021c605 | -11.4102 | -43.5099 | 2025-09-26 13:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 57fb420d-a652-3af7-a32d-e85f9d3ab52b | -7.6775 | -45.9872 | 2025-09-26 13:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| e896325d-04b7-3c6b-9795-32b3ddfe97d1 | -11.9659 | -47.8669 | 2025-09-26 13:10:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| fd2d3fca-e460-35f1-b5d0-210d59dd0173 | -11.6814 | -44.4078 | 2025-09-26 13:10:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 7b4e25a2-200b-3ba7-b9b7-549589c487c7 | -5.475 | -43.0774 | 2025-09-26 13:10:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 1c1bff2a-2b02-316c-9b69-70ff11539363 | -9.5601 | -47.5139 | 2025-09-26 13:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| a640b938-38cf-3af6-b18d-b03dffdb775e | -11.9659 | -47.8669 | 2025-09-26 13:20:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 5d662054-efd6-3f7a-9df6-865dc9c88699 | -11.6046 | -44.4193 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 64323356-439a-319e-9e27-1f78792303d9 | -11.6041 | -44.4427 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 76.1 |
| 17c70b45-a72b-3f0f-b51b-f3c64c764f2d | -11.4233 | -44.9331 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 62433f0c-684b-38e8-9e26-8f11a3d88917 | -8.0056 | -45.2555 | 2025-09-26 13:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 89.4 |
| 183dd574-4c25-3115-b809-ff38792e9cf8 | -17.6009 | -52.4907 | 2025-09-26 13:20:00 | GOES-19 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 62.0 |
| 5a14c908-86cf-3b76-8f8b-66d6f3d66596 | -11.385 | -44.9386 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 63.0 |
| 9478274d-0e72-3120-9485-d13806128e76 | -20.7529 | -57.8684 | 2025-09-26 13:20:00 | GOES-19 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 78.6 |
| ad3d0113-7c39-3a99-8f39-01130541243f | -10.8051 | -45.3866 | 2025-09-26 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 78.7 |
| a89d6720-6381-3b0f-9c8f-744efe65921e | -5.7775 | -42.7961 | 2025-09-26 13:20:00 | GOES-19 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 94.0 |
| ef0be650-86eb-3e3d-931c-a67867ea556a | -8.8415 | -46.2095 | 2025-09-26 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 99.4 |
| d2b9b91c-e310-3da8-8de3-485ee27952a8 | -11.6425 | -44.4369 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 80.8 |
| 2b9d05b9-aeb5-3288-9038-70d00dd6a724 | -12.631 | -48.1313 | 2025-09-26 13:20:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 7d5b9c65-18cf-3e98-9bfc-44b84feb4b13 | -6.9303 | -45.6931 | 2025-09-26 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 26a1dcab-5c8d-3f3e-a576-a8b864588a9f | -11.4102 | -43.5099 | 2025-09-26 13:20:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 1dfb5487-5c6b-3837-bb62-7fe675bbb224 | -10.8055 | -45.3637 | 2025-09-26 13:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 64.7 |
| 11d01cac-dc05-3ac5-a3cf-2ca48638679c | -9.8921 | -46.7437 | 2025-09-26 13:20:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 74.3 |
| 393e8687-7071-3edc-8cab-2a51bc2d65b9 | -7.8735 | -45.2911 | 2025-09-26 13:20:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 75.4 |
| 9e712e26-3800-3ec9-bcb6-94d645491e9f | -9.5648 | -48.5877 | 2025-09-26 13:20:00 | GOES-19 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 96.9 |
| 0db1b26f-77bd-3303-83e1-64355125919a | -11.4041 | -44.9359 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 5ef7207e-1860-3af0-b797-664424e17da2 | -11.681 | -44.4312 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 117.9 |
| f1747fa5-fc0f-3025-ac01-8a3b71d63c92 | -5.9264 | -42.9253 | 2025-09-26 13:20:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 90.5 |
| b7fdba1d-e58c-3422-89b9-9352655a2c64 | -8.8409 | -46.2544 | 2025-09-26 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.1 |
| 344ad744-dd67-3e4d-8e78-63ff243ad63f | -11.6818 | -44.3844 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 92.5 |
| 756da896-fa6b-3af5-afff-1f03c631f066 | -11.4225 | -44.9794 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 246.8 |
| 14a25967-f9c6-3b5f-871e-744ade8bd447 | -5.475 | -43.0774 | 2025-09-26 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 97.9 |
| b39be5e3-cca0-3ece-ab7d-411db924052f | -10.0065 | -44.1533 | 2025-09-26 13:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 81.5 |
| a63801e3-49b5-3574-9912-08d9a3d2ee72 | -11.6814 | -44.4078 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 197.1 |
| 9252ba35-8d6a-3c5d-9de6-76e83f87b6e3 | -5.4752 | -43.054 | 2025-09-26 13:20:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 2048cf2e-da34-3df1-abce-4bfae037208e | -6.5801 | -45.1117 | 2025-09-26 13:20:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 77.1 |
| 1debcf32-ce08-3350-a2b9-d23e8205f062 | -11.5669 | -50.2279 | 2025-09-26 13:20:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 70.3 |
| 8ebe0de4-0523-37e0-b706-508a2ee2748a | -10.0062 | -44.1766 | 2025-09-26 13:20:00 | GOES-19 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 163.8 |
| 1a1ec799-aa84-3694-8d23-f17048eca705 | -11.6233 | -44.4398 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 146.7 |
| 9f3c7823-fc6c-34d7-a5bc-2abd118da59d | -13.201 | -47.4026 | 2025-09-26 13:20:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 82f4eb65-f754-364a-af68-b07ead195542 | -8.8603 | -46.2075 | 2025-09-26 13:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 122.0 |
| 8bd3d34c-beb4-3eba-be61-39df0740f384 | -14.8304 | -45.3947 | 2025-09-26 13:20:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 85.2 |
| 22e18498-8060-307a-9012-92e40938a4f3 | -10.9377 | -44.2832 | 2025-09-26 13:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 3b036a79-3042-322f-a25f-ad28bf31d9ad | -7.6775 | -45.9872 | 2025-09-26 13:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 85.5 |
| db48e4ec-c31d-3fea-94c1-30dad0b1b501 | -11.6238 | -44.4164 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 137.0 |
| 199da0e6-61c4-3eca-bd6f-7662127ea3d7 | -11.4221 | -45.0025 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 258.1 |
| f498b827-81a1-336f-8995-cb581a75fa1d | -11.4033 | -44.9822 | 2025-09-26 13:20:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 7c4069c0-fb39-3314-84f7-b19be83ab819 | -11.7006 | -44.4049 | 2025-09-26 13:20:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 131.7 |
| b1efe1ea-8ee8-37ec-ae2b-f9c97648b335 | -8.8603 | -46.2075 | 2025-09-26 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 153.6 |
| 78093a10-167e-32b7-83c8-4a01db3b905c | -7.6772 | -46.0097 | 2025-09-26 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 10b6bd29-718b-3ecb-ab8e-f7a0065ecf50 | -11.0635 | -45.8996 | 2025-09-26 13:30:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 84.4 |
| 4c6ca518-3413-3feb-ad3b-8dcc22929dde | -8.8409 | -46.2544 | 2025-09-26 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a6d28cc5-32d9-3750-9f84-dddfbd405918 | -7.6587 | -45.9889 | 2025-09-26 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 90.9 |
| 431d4d99-990c-3d4c-b4c1-a3672ec95bca | -10.9377 | -44.2832 | 2025-09-26 13:30:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.4 |
| f4c93dd2-22a1-326c-9238-a9facdd89ceb | -11.6233 | -44.4398 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 111.0 |
| ef4d922c-f1b7-3fab-a7ec-82cd4e68278c | -6.9115 | -45.6947 | 2025-09-26 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.8 |
| bbb29ee2-e3f3-3321-af7b-56ff2750874f | -12.3427 | -50.544 | 2025-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 72.5 |
| 3b85cfdc-b96e-3613-8956-43d5f5794e41 | -12.3424 | -50.5655 | 2025-09-26 13:30:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 026c8be1-09d7-3a5b-8fc1-f9cd1f750b1b | -14.8309 | -45.3714 | 2025-09-26 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| d6bc8f9f-2924-32fb-8eb4-3fcd134efdb1 | -11.9655 | -47.8891 | 2025-09-26 13:30:00 | GOES-19 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 54.7 |
| cf5d7ae0-3c46-3356-a323-865b9bd59554 | -7.5415 | -46.4025 | 2025-09-26 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 103.2 |
| fea42299-b7bc-30ec-a08b-4b472469cf98 | -14.8108 | -45.3983 | 2025-09-26 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 4aa21df6-6b35-378c-a74d-4fc5777e41b1 | -7.8735 | -45.2911 | 2025-09-26 13:30:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 172.9 |
| bbba9c4f-98eb-3b1b-aa5b-36bd0618bcf6 | -9.5601 | -47.5139 | 2025-09-26 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 1874998a-b4b5-315f-aeb8-6e2a4bea1a8d | -6.9303 | -45.6931 | 2025-09-26 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 96.8 |
| cbdf0dfa-8cc0-3284-a710-0ed3606bf469 | -8.0056 | -45.2555 | 2025-09-26 13:30:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 100.1 |
| 9423720c-6971-3e90-805e-90c84ae683ab | -12.3776 | -44.1355 | 2025-09-26 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 83.2 |
| a478585e-5c44-310f-a85e-5bd2500b60b1 | -11.7977 | -47.6449 | 2025-09-26 13:30:00 | GOES-19 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 3e070738-15b0-3a6e-aaa0-9a2d67a02d45 | -11.681 | -44.4312 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 120.7 |
| 38976bb8-98cc-3e31-bfbb-9bc6917459f8 | -7.1203 | -43.7323 | 2025-09-26 13:30:00 | GOES-19 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 7cb36dd9-e23f-3586-ad99-6805fa0c9bff | -11.6818 | -44.3844 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 96.3 |
| 20d869fa-dc0c-3662-99d8-229a7b52c6f5 | -9.5598 | -47.536 | 2025-09-26 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 2e0fc0d6-9a5c-3a00-9a24-cdd0e8786c4e | -11.701 | -44.3815 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 99.9 |
| 20087dcf-8d39-3d79-a25c-d3398c69447a | -5.3091 | -42.761 | 2025-09-26 13:30:00 | GOES-19 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 85.5 |
| 7fa7d12a-0d56-3b72-91d8-c3081a3f078d | -14.7377 | -45.1786 | 2025-09-26 13:30:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 314c86a1-7289-3780-9a81-909dff4e4182 | -13.7123 | -47.8851 | 2025-09-26 13:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 50894732-ecf5-358b-92f6-c55167c726e9 | -11.7006 | -44.4049 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 206.5 |
| 9b1fa974-7cf1-359d-9372-78607560cbcb | -5.4565 | -43.0554 | 2025-09-26 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 93.8 |
| b36b7d26-b3e4-3992-98f3-1692a9db457f | -13.201 | -47.4026 | 2025-09-26 13:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 80.7 |
| b665b55d-865f-39a8-9c69-49ceeab51d4f | -11.6814 | -44.4078 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| fd20d72f-ff0a-396a-aa1a-0053abe37c62 | -5.9452 | -42.9238 | 2025-09-26 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 256da402-380b-3d4c-aec8-3787e1da5e57 | -9.5412 | -47.5159 | 2025-09-26 13:30:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 8a857f22-6950-3701-80ae-5265b2f63cf4 | -6.5801 | -45.1117 | 2025-09-26 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 33b69ed3-3ae2-3dd9-b794-e9b5f0c7434d | -5.9264 | -42.9253 | 2025-09-26 13:30:00 | GOES-19 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 157.6 |
| 290bb2f2-6967-3540-8d82-76be47b10e01 | -12.6118 | -48.134 | 2025-09-26 13:30:00 | GOES-19 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 7ebe6de3-3423-39b7-a4a4-94e2b8f254f9 | -9.8658 | -45.9372 | 2025-09-26 13:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 16f2f51c-7ce4-301b-bf9e-84123a0d27b2 | -5.4562 | -43.0788 | 2025-09-26 13:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 85ae7952-6d1c-3bec-a26b-3b69c0d15191 | -8.7708 | -43.0417 | 2025-09-26 13:30:00 | GOES-19 | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | 104.5 |
| 92578059-5a1c-3ad1-bd87-1448fb16cf2e | -7.3371 | -46.2194 | 2025-09-26 13:30:00 | GOES-19 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 254a1d55-993c-3c71-af5d-fd9fd7265ca9 | -7.6775 | -45.9872 | 2025-09-26 13:30:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 140.3 |
| 2db2b18f-3450-32d6-a363-b6a164973fa5 | -12.3771 | -44.1591 | 2025-09-26 13:30:00 | GOES-19 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 82.9 |
| baac6c44-41fe-3294-b2ce-3153dce9f22b | -11.6238 | -44.4164 | 2025-09-26 13:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 104.8 |


[Clique aqui para ver as próximas entradas](README53.md)
