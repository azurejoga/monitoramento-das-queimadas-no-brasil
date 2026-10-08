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

## Dados Diários - Página 323

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c009b3b2-f319-3173-98a5-3d11979c40bd | -11.11091 | -41.31067 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 43adc6dd-0eb3-3130-9b8d-a895ff2f55b9 | -6.53671 | -45.37156 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 1684d190-3f09-3bb4-86b3-0fdf71f7cf3f | -11.08361 | -44.02268 | 2026-10-08 16:37:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b93d4619-fa64-39b7-b70a-20dbde516ca5 | -12.2209 | -43.93407 | 2026-10-08 16:37:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 224.7 |
| e405fff9-b0c5-3121-beec-1c6e2cf04e03 | -11.77012 | -47.74123 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8fd919b3-805e-3c97-bda0-d5b2bacb59bc | -13.70438 | -49.08324 | 2026-10-08 16:37:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5f4b99d7-24ae-39ba-bc63-19081cdfc46f | -11.7688 | -44.94604 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| 94c7aee7-61ee-3991-8753-217bee182b4a | -10.72825 | -39.12636 | 2026-10-08 16:37:00 | NOAA-20 | QUIJINGUE | BAHIA | Brasil | 2925907 | 29 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 3d65d254-461a-3b49-a2aa-7ed3deca180c | -9.89404 | -44.80188 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 58.0 |
| 31164180-8a6f-35de-b862-ee30398508a0 | -12.65018 | -47.71445 | 2026-10-08 16:37:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2aba112e-66c5-3429-ae4f-6b331ea5cb44 | -8.27525 | -46.9052 | 2026-10-08 16:37:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 7bdf1542-6b4c-3b49-a366-4659dbfb5cc9 | -18.27988 | -42.62391 | 2026-10-08 16:37:00 | NOAA-20 | SÃO PEDRO DO SUAÇUÍ | MINAS GERAIS | Brasil | 3164100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c0cea7f1-2c69-39f7-92f6-159b62185db3 | -8.10479 | -47.12448 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| f74c5f27-f91b-3315-a0a5-4a575ec0b5d7 | -11.36098 | -46.69837 | 2026-10-08 16:37:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 9363b2c1-86b2-3178-a58a-6562089c1828 | -19.06848 | -48.63872 | 2026-10-08 16:37:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 9d521765-2de9-3ceb-8ef4-4c9b0a3397e2 | -11.2116 | -44.8745 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 38429d4a-ab68-34ee-9f68-9074f09b75b9 | -7.46866 | -42.85802 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 50.1 |
| 7f6a4c43-7a0e-3b2a-83dc-668e19ff4845 | -8.20327 | -46.42385 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 172.9 |
| 7f4c6e20-6dbb-3164-ab96-960bdf2ea322 | -6.6676 | -35.1149 | 2026-10-08 16:37:00 | NOAA-20 | MAMANGUAPE | PARAÍBA | Brasil | 2508901 | 25 | 33 | nan | nan | nan | Mata Atlântica | 14.3 |
| 8b587fd7-03a6-3aac-b6a2-ec2ca8938cf8 | -11.09991 | -41.31252 | 2026-10-08 16:37:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 39d3fbf2-3313-37fb-8884-4af0f04a70df | -8.93438 | -45.16134 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 34cf3c84-dcaa-329c-96d9-9b6ca3293dff | -11.40641 | -47.57012 | 2026-10-08 16:37:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 25.7 |
| 2e089024-1c93-34be-9989-42770a0858f1 | -11.35535 | -43.1435 | 2026-10-08 16:37:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 20.4 |
| 26b701d7-7ec4-37ee-b7cb-0e093c726704 | -7.47868 | -42.8523 | 2026-10-08 16:37:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 29.7 |
| 61894ee2-eff1-35ed-a1e6-cd78581d1471 | -6.82354 | -38.54481 | 2026-10-08 16:37:00 | NOAA-20 | CAJAZEIRAS | PARAÍBA | Brasil | 2503704 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 070c882b-4c37-370d-9e23-fb233d945833 | -10.97511 | -45.39448 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 53e60a7c-ca7e-3343-b1bf-6c11181640bd | -12.03503 | -43.4366 | 2026-10-08 16:37:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 9efd20bc-64a2-37eb-987e-a30f3b843a1b | -8.19345 | -45.77432 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7aa2401e-50d8-3f63-b31c-728142181811 | -5.18088 | -38.45481 | 2026-10-08 16:37:00 | NOAA-20 | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 13.1 |
| 107bdee1-6ca2-37ed-a009-046fd545afbd | -9.02977 | -44.36932 | 2026-10-08 16:37:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 7cc7c379-06e5-3873-82c1-7383ea6ec688 | -7.83056 | -44.17427 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1116b4e1-4cf0-35c3-82db-9bbb659a6473 | -6.53158 | -45.40438 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 111.4 |
| 1c527bd3-c112-39de-aa71-222a6537f76e | -10.85302 | -42.80684 | 2026-10-08 16:37:00 | NOAA-20 | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 9a95d3df-b174-36e1-9b7e-049f879a3aa6 | -7.17066 | -47.78357 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5ff3a7e3-6fa8-3452-8d39-0017041376bb | -6.43338 | -44.81302 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 6f6fa0af-3b35-31c5-93b7-c024e22b9e2d | -11.59704 | -43.65634 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 16.7 |
| bb73e582-3f3f-359c-a3ab-fa535fb0e0c0 | -10.67359 | -47.81896 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 58c44a67-24ae-3111-a006-e501654480ac | -9.39421 | -45.88718 | 2026-10-08 16:37:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| febfecc0-69e6-3363-ad79-5e7ecf37b002 | -6.67095 | -45.36121 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 45fb91b4-1cd6-3557-915e-c45f208800aa | -8.78347 | -47.26655 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| a88b85c1-33ad-3124-a4c6-26e4d94f166f | -9.82619 | -45.69274 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 58a39ff0-f1b9-3367-9bb1-140ac058efc5 | -11.20284 | -44.86151 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 29.3 |
| a36ec2f9-4540-3fe5-b39c-3f21fc480ee0 | -9.90268 | -45.19066 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 12.3 |
| d7d592eb-23a3-3ddb-91ee-2b723879e908 | -7.76802 | -44.18146 | 2026-10-08 16:37:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e8cd8c87-08ce-3d5c-aa34-cd87baaaf93f | -7.84537 | -45.51734 | 2026-10-08 16:37:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 300c36f7-3a3b-3a9d-8c7c-0bb84c1e9a02 | -12.3132 | -47.0732 | 2026-10-08 16:37:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b4b3d11f-a666-3f06-a7e1-a510dee1ec6c | -8.9394 | -45.14988 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 5f188d2d-dd3a-3b4c-b2c1-7df8f21e9a94 | -7.33547 | -45.29044 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 20a3671b-2480-3e78-ac54-df58c0585499 | -5.86971 | -38.85948 | 2026-10-08 16:37:00 | NOAA-20 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 70f62d36-d46b-3483-bb48-2886b754fd0f | -6.68353 | -45.57583 | 2026-10-08 16:37:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| d7df3d3e-4fb5-37ee-9eb5-14b3615f99d7 | -12.22306 | -44.7434 | 2026-10-08 16:37:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 473ee29a-f59a-3dcd-b397-31983f6b8667 | -11.74178 | -44.94668 | 2026-10-08 16:37:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 560e5a0f-762d-3707-9cdd-84c70f92b319 | -11.85579 | -47.38278 | 2026-10-08 16:37:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 36430352-d352-38ae-9e8c-eef19d8a37fe | -8.79252 | -47.28048 | 2026-10-08 16:37:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 782aa2bf-ff61-3555-a2fa-3fba409c0830 | -8.29182 | -45.7301 | 2026-10-08 16:37:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 267.1 |
| 404836c3-e052-3f42-8e15-6143cde50656 | -12.23906 | -44.73728 | 2026-10-08 16:37:00 | NOAA-20 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 8.1 |
| bbc3e196-685f-3917-88d5-af24aaa4c34c | -13.11762 | -46.35201 | 2026-10-08 16:37:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 89226441-bfdd-3ace-9417-be72c7acbb3b | -11.24534 | -47.72881 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 46f306e3-8617-321d-8094-fa32b8c842bf | -9.7044 | -45.69418 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 19.7 |
| 80bfbcf8-e196-3a0f-a3df-1520e7ddd39d | -6.84567 | -41.74962 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| 9957b429-7040-3cee-97e0-6ecaf35d71d7 | -8.93373 | -45.17924 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 8b6b265f-65d7-373c-95c8-2257b5914c40 | -9.98085 | -39.53038 | 2026-10-08 16:37:00 | NOAA-20 | UAUÁ | BAHIA | Brasil | 2932002 | 29 | 33 | nan | nan | nan | Caatinga | 17.1 |
| 52ee403b-9f23-397a-b7be-379ea90284c8 | -7.10063 | -41.74355 | 2026-10-08 16:37:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 41.7 |
| 0c9fc72a-9fa9-309a-891b-f6e26f2d2e06 | -19.26076 | -40.73788 | 2026-10-08 16:37:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 6a040f84-5fbe-3782-a086-7423eeff7e05 | -5.72431 | -41.77019 | 2026-10-08 16:37:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 4f651700-b2d0-3f1d-b451-d758d022a6e1 | -6.79072 | -45.05944 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 21a41468-699b-3e6b-8945-d1ca63fb91cb | -8.10802 | -47.66296 | 2026-10-08 16:37:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 22.3 |
| bf7825ad-7f5c-32cf-8ff0-58795c054c95 | -10.93599 | -45.38256 | 2026-10-08 16:37:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 85b1f195-9ae1-3c85-baac-58d726ba53a9 | -6.88339 | -43.7051 | 2026-10-08 16:37:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 44.8 |
| 4ddba321-4fa6-367b-b59d-4622d14cfd10 | -7.28033 | -44.19583 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| eb136526-308f-32b7-a135-39a4208b06ed | -8.93586 | -45.19316 | 2026-10-08 16:37:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 29.6 |
| b3368c6e-1f6e-39eb-a0f6-1fdb4fce207d | -10.25172 | -49.6654 | 2026-10-08 16:37:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| ae2b0fef-0e31-3e48-8be7-3853bf985033 | -5.49722 | -36.50188 | 2026-10-08 16:37:00 | NOAA-20 | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8205cad5-d32a-38a1-b6ae-9d46649421ca | -9.90044 | -45.19815 | 2026-10-08 16:37:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| ba05fbc7-f3b3-3c5b-ad99-4faf007b31b8 | -11.62886 | -43.70652 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 26.2 |
| f4354a2e-8e6d-35fb-b777-95afaed0f2f5 | -8.74515 | -44.2002 | 2026-10-08 16:37:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4c0c7dd2-f57e-390b-9fcf-28dcf87e8e37 | -6.80124 | -45.06141 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| eb9f90f1-266d-3ce6-b08a-05f28e1cc390 | -11.63887 | -43.70488 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6cea57e1-6a00-3a6a-aaaf-d4adbc6f91a7 | -11.08526 | -47.61954 | 2026-10-08 16:37:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d52a82e5-aca5-38e6-bf86-638e9b53504c | -11.79904 | -46.78012 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bb396556-bb9c-377b-b8bb-4582c5f7ed4a | -7.54115 | -42.0933 | 2026-10-08 16:37:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 8bdb3032-d865-3b61-8b60-6d31145893bc | -8.25259 | -54.65147 | 2026-10-08 16:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 56f5a469-0540-3b87-8c79-13ec5dcc55fa | -11.45353 | -43.39103 | 2026-10-08 16:37:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 7b893a95-040a-3a5c-82d7-3e36578e6a24 | -9.13334 | -45.84316 | 2026-10-08 16:37:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e5d30845-31f2-3bb6-b79a-3c0217a1d159 | -11.21715 | -44.86645 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 0485db5a-3335-37c3-8748-0c075446290c | -7.27975 | -44.19219 | 2026-10-08 16:37:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5fdbe17d-d950-3a40-81e6-7d8143d3ba77 | -11.83525 | -48.09523 | 2026-10-08 16:37:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| d6abac32-a5ee-32c1-a73a-584b57ce5743 | -9.90622 | -44.79284 | 2026-10-08 16:37:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 60c0d671-6503-3d2d-b343-c94c268b7bc1 | -10.67772 | -47.82242 | 2026-10-08 16:37:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ca10c065-b11b-33a5-b71c-0a3009496326 | -6.97241 | -47.67188 | 2026-10-08 16:37:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 051904d3-963d-32fc-8e46-73c08c3b39d9 | -11.30346 | -44.83109 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 66.3 |
| a175307c-b489-3a6f-acd9-15bec00781df | -18.35702 | -42.50889 | 2026-10-08 16:37:00 | NOAA-20 | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 8193e13d-261b-312e-861c-aeb941580c66 | -6.84946 | -41.74897 | 2026-10-08 16:37:00 | NOAA-20 | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 33.5 |
| 1842627e-665e-3a26-af7f-e610b7caa0c8 | -6.16378 | -42.58595 | 2026-10-08 16:37:00 | NOAA-20 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 64.2 |
| 8fbc5320-8e22-389a-9adb-e0eacaeb5929 | -11.77317 | -46.76797 | 2026-10-08 16:37:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 9eb0fb3d-2866-3bbb-93cd-3c03ac321e50 | -7.30929 | -44.00442 | 2026-10-08 16:37:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 25.9 |
| 7e8dabbb-f493-3b36-a741-7d0de913ead5 | -9.71923 | -40.13357 | 2026-10-08 16:37:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4128c87a-ab23-3ea7-8f8f-5643e3461da7 | -6.99067 | -45.1235 | 2026-10-08 16:37:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| ee178f78-c38b-346e-ad31-b1b3c254c406 | -11.20562 | -44.85749 | 2026-10-08 16:37:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9d0d4fb8-ca10-3d2c-a67c-349eeb09f473 | -7.48712 | -42.81345 | 2026-10-08 16:37:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 32.8 |


[Clique aqui para ver as próximas entradas](README324.md)
