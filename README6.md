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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 369f4d1a-3b32-3202-8b50-bc7e27f6f507 | -3.4919 | -49.581799 | 2026-10-10 00:09:00 | METOP-C | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c010fdd0-0ade-3242-af17-92192c2563f7 | -12.3672 | -46.612999 | 2026-10-10 00:09:00 | METOP-C | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| a2e331a3-6977-39f9-8f87-fe48a044a129 | -11.9863 | -43.479801 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9e911a0a-f543-300b-ba1b-abcb075803a2 | -5.2273 | -45.377998 | 2026-10-10 00:09:00 | METOP-C | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bf34d657-eb58-32ed-9c7d-a106b9ff1e5b | -5.5589 | -43.9646 | 2026-10-10 00:09:00 | METOP-C | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8fa96854-a737-36e1-bb09-8a2a49913ccd | -3.6604 | -40.197399 | 2026-10-10 00:09:00 | METOP-C | SOBRAL | CEARÁ | Brasil | 2312908 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| c6d6317b-866c-3afb-9ad8-3db0177bffda | -11.0167 | -45.427399 | 2026-10-10 00:09:00 | METOP-C | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2a111c11-9395-31bc-8310-060e2199e2fd | -4.2695 | -48.582699 | 2026-10-10 00:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f972ab88-29e0-39a6-9665-b1d8916bae39 | -5.4252 | -39.2631 | 2026-10-10 00:09:00 | METOP-C | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| fce2e417-bee8-3198-aa13-5c8e44dbc471 | -11.5604 | -43.690601 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 352c2975-60a1-36ba-83af-7bb03ceea1a4 | -12.6906 | -43.084599 | 2026-10-10 00:09:00 | METOP-C | PARATINGA | BAHIA | Brasil | 2923704 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 60a9bf7c-664a-34f3-b992-1a9689b205aa | -11.8304 | -43.612701 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a37f86e1-2d3c-33f0-9f91-e030b553bd33 | -6.0904 | -43.997898 | 2026-10-10 00:09:00 | METOP-C | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 35832c3e-1ab0-3503-bc6a-d5564e09e157 | -11.0748 | -44.1012 | 2026-10-10 00:09:00 | METOP-C | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| a8e03d4a-2c30-30bb-87eb-f0ae21f87fe8 | -17.2843 | -40.343601 | 2026-10-10 00:09:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| ccbb33dd-e7fb-303e-b14c-f7d946fac79b | -7.1815 | -52.639999 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aa348b9-04d7-3c05-a691-6bbc0039a613 | -8.1867 | -45.752399 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5b045010-7f61-3230-a4d2-4270699a6dc7 | -5.6836 | -49.040798 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9adc1777-b63c-332c-ad7a-5ff9d8e7e523 | -10.6138 | -43.2869 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| bd124d6c-8a61-3ec1-b2d3-bf371367078c | -7.506 | -45.3013 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9227d522-e1fc-39b9-b011-a91216bceff4 | -3.5532 | -51.460899 | 2026-10-10 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b1c1603b-ed99-382b-a150-14d9076228be | -10.2721 | -43.936501 | 2026-10-10 00:09:00 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2cc70fc6-ec88-382b-a363-840cd3d7fa94 | -9.2798 | -47.401199 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 191c4cba-e8b9-3a63-843d-38839e3d75fc | -13.3456 | -43.919399 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| d048fdd3-add9-31d2-8b2d-0c0a5b5b3ebc | -13.3705 | -43.8922 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85dc7775-68d4-3455-a981-23b0c74c0167 | -11.9803 | -43.451401 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| efa51307-3913-393f-a203-be1435f326f1 | -13.3825 | -43.9007 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 7525a059-2873-3771-b2f6-30f4d7535c85 | -13.6241 | -44.431702 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b23af0bf-f814-370f-8b5d-dbed804af433 | -18.319 | -42.394501 | 2026-10-10 00:09:00 | METOP-C | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 17d87e58-633c-30a6-9b3c-143b6d57e5f7 | -4.1254 | -45.774101 | 2026-10-10 00:09:00 | METOP-C | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a16dcb1c-698c-3d62-8072-001c22d4ab92 | -12.8363 | -44.170502 | 2026-10-10 00:09:00 | METOP-C | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bb740df5-8f88-3bea-b164-193ed546666c | -13.388 | -43.877602 | 2026-10-10 00:09:00 | METOP-C | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 2f535f14-4994-3ed6-9237-645d9cc6647b | -6.0727 | -44.657001 | 2026-10-10 00:09:00 | METOP-C | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d358ed39-0a74-3893-a7e6-53aaea477caf | -13.6218 | -44.4203 | 2026-10-10 00:09:00 | METOP-C | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9feb1553-e556-39ab-a089-9cbcbf227ece | -9.2863 | -47.383801 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c2ae8b7c-5deb-3b06-a304-e245202c5b18 | -10.4459 | -47.841599 | 2026-10-10 00:09:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| c30c33a9-61c8-3acd-8a38-ef2a282f3738 | -11.6665 | -43.708199 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| b2b76be4-a6fd-3721-a3af-635414407156 | -16.113501 | -43.748299 | 2026-10-10 00:09:00 | METOP-C | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| ec8cef94-7f0d-39cf-b360-b9f30fb26885 | -14.4468 | -43.9683 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1938ea80-ff68-35fc-8d61-65aa5973eba7 | -13.8879 | -43.927101 | 2026-10-10 00:09:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| fd26f3d5-6027-39d7-a444-150be8177240 | -4.1112 | -46.856701 | 2026-10-10 00:09:00 | METOP-C | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 31a9d6b9-c207-3108-b1ad-2fe2bff8f847 | -7.4842 | -42.827202 | 2026-10-10 00:09:00 | METOP-C | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 07742f60-fdeb-3f93-830a-4957dc6d2cd1 | -8.9488 | -47.373901 | 2026-10-10 00:09:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 91d932e1-52bf-384c-884e-539f3d0a4312 | -4.3585 | -44.3419 | 2026-10-10 00:09:00 | METOP-C | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4f9afea7-f1a2-3d81-90f7-24e1b995e90f | -7.0756 | -41.604 | 2026-10-10 00:09:00 | METOP-C | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d91d529c-3e24-33fb-8624-844a02939c26 | -12.77 | -44.8881 | 2026-10-10 00:09:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3a80b5c6-f860-32f4-89fb-8642b2bc5564 | -5.2239 | -50.669701 | 2026-10-10 00:09:00 | METOP-C | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ca333ecf-730a-3dd2-94f8-aa45636c1799 | -4.9308 | -45.060799 | 2026-10-10 00:09:00 | METOP-C | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9ccee0ce-de7d-3d37-8b6d-cc4d784be10f | -4.3848 | -49.752998 | 2026-10-10 00:09:00 | METOP-C | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1c7b3fd7-e897-3ace-807c-32e1364b46fd | -13.351 | -43.8964 | 2026-10-10 00:09:00 | METOP-C | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4a0904d4-5d13-3901-8ad1-2e5c6ab556f4 | -7.5106 | -45.3223 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a4e3920e-2a86-3da1-954f-717e1cb976a4 | -9.6226 | -48.869598 | 2026-10-10 00:09:00 | METOP-C | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4440317a-696e-3166-a429-c38dc0387831 | -10.2762 | -43.955502 | 2026-10-10 00:09:00 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 91aaf12e-d0c5-3090-a96c-558b1cf2951e | -11.8683 | -47.361099 | 2026-10-10 00:09:00 | METOP-C | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 297ab185-a62d-3fe8-bae1-0f47b6d283ee | -15.7402 | -41.574402 | 2026-10-10 00:09:00 | METOP-C | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 87c24f83-fc3d-3986-a8de-09d91e52098a | -10.4362 | -47.843601 | 2026-10-10 00:09:00 | METOP-C | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 68302ba5-80b9-3d3c-a641-c600666daa01 | -8.3064 | -45.738899 | 2026-10-10 00:09:00 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2d18db3e-9b92-375a-9cd6-af79ab6ce03c | -11.6506 | -43.6814 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 33439e8e-3b79-3642-bfdd-3a65692e51c5 | -3.5682 | -51.4828 | 2026-10-10 00:09:00 | METOP-C | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5b461086-f8bd-3861-bf40-deeda4f35217 | -12.9155 | -47.4394 | 2026-10-10 00:09:00 | METOP-C | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7c55d1e8-e4c0-3a2c-942d-e50135767c4f | -12.0369 | -43.380299 | 2026-10-10 00:09:00 | METOP-C | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 0fe31147-8bf5-366b-bc3e-5740d68cbf4a | -5.6875 | -44.448399 | 2026-10-10 00:09:00 | METOP-C | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 477a5933-6e85-3982-8fae-0d59dbbcd1f7 | -17.1443 | -41.337399 | 2026-10-10 00:09:00 | METOP-C | CARAÍ | MINAS GERAIS | Brasil | 3113008 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 09dcaa1e-aeb7-3b5b-9a62-7429784f21f7 | -16.6306 | -40.598 | 2026-10-10 00:09:00 | METOP-C | RIO DO PRADO | MINAS GERAIS | Brasil | 3155108 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| f5eb5bcf-83fe-385d-b539-1092811f93c0 | -9.283 | -47.416599 | 2026-10-10 00:09:00 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2d8a409a-9a44-366a-b732-131756b1b146 | -6.4907 | -44.366699 | 2026-10-10 00:09:00 | METOP-C | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| d5a79cc9-fe23-305e-badb-b70719f8d5dc | -18.091499 | -42.276001 | 2026-10-10 00:09:00 | METOP-C | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 3c331986-a235-342b-882b-01a6991276b9 | -5.8866 | -43.408401 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 29466b5e-d305-3b78-beeb-5737f5c8f977 | -8.2287 | -46.424702 | 2026-10-10 00:09:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 99a650d3-fbb6-3c41-8153-2e54414eefdf | -12.7676 | -44.876202 | 2026-10-10 00:09:00 | METOP-C | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 21bc7b67-3162-3486-accd-3cc58f96affb | -5.8751 | -43.402699 | 2026-10-10 00:09:00 | METOP-C | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 613c6e75-2b8f-3e96-a070-d86df1d598fa | -4.1608 | -48.737202 | 2026-10-10 00:09:00 | METOP-C | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 44489103-5850-3807-9703-39676d07d081 | -4.428 | -47.545399 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| dc49d62f-bbb6-3646-a114-e5420af715a0 | -8.2411 | -46.435299 | 2026-10-10 00:09:00 | METOP-C | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8e50dc70-a785-3933-a2a9-8e64f9898f24 | -9.8903 | -44.782001 | 2026-10-10 00:09:00 | METOP-C | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 041dc713-75b8-3055-b498-eea13067c6bd | -5.5067 | -43.045799 | 2026-10-10 00:09:00 | METOP-C | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a59075d5-58df-3eda-8996-f039c77df2f0 | -17.2876 | -40.359299 | 2026-10-10 00:09:00 | METOP-C | MEDEIROS NETO | BAHIA | Brasil | 2921104 | 29 | 33 | nan | nan | nan | Mata Atlântica | nan |
| e35f83d6-a627-3613-8113-1b8b0e5bdf50 | -17.446501 | -45.075298 | 2026-10-10 00:09:00 | METOP-C | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 9b1ca264-c477-3452-ba36-e2aa2f6a021d | -3.7355 | -49.991001 | 2026-10-10 00:09:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d1636080-341e-3d71-96e9-def759a900d9 | -11.6618 | -46.7873 | 2026-10-10 00:09:00 | METOP-C | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 237efdda-01cc-3fb7-bb21-39254efd4d3f | -11.6526 | -43.691002 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 9d945e8d-886e-3d6e-953d-186733585425 | -4.4411 | -47.927898 | 2026-10-10 00:09:00 | METOP-C | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d50751b3-1979-3776-9458-01005a6d3dc9 | -14.009 | -48.734798 | 2026-10-10 00:09:00 | METOP-C | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| bd612c65-884d-3a59-96db-6aa27e521c68 | -11.6029 | -43.601601 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| bf9b9f4f-50c2-3f0b-bcad-5e32b272f06f | -7.0972 | -46.716702 | 2026-10-10 00:09:00 | METOP-C | FEIRA NOVA DO MARANHÃO | MARANHÃO | Brasil | 2104073 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5f7b3a5d-b146-3e1c-b9d4-0791360290e6 | -8.9391 | -47.3759 | 2026-10-10 00:09:00 | METOP-C | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 7333b199-ff19-362e-8438-5f051572edae | -6.8713 | -45.022301 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| ab363884-49bc-3423-be0d-45a2136ed11a | -5.8363 | -44.932701 | 2026-10-10 00:09:00 | METOP-C | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a13d5e03-d8f2-3ae4-92f7-abf0ea7e9bf0 | -7.7684 | -43.784599 | 2026-10-10 00:09:00 | METOP-C | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d93a0e83-7083-367c-81fd-7604a91354e8 | -4.399 | -43.109299 | 2026-10-10 00:09:00 | METOP-C | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 8607b200-8323-3b2f-a9e4-f28ed9964c9d | -11.5902 | -43.7346 | 2026-10-10 00:09:00 | METOP-C | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| e3281d40-c822-39a3-a346-10b0a7a5efb5 | -14.0507 | -43.826 | 2026-10-10 00:09:00 | METOP-C | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| ef69a096-9d72-3bdb-b089-c590765ec7b3 | -5.3355 | -42.925701 | 2026-10-10 00:09:00 | METOP-C | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5cfb4330-7b01-3fad-bdc3-3b6884cba771 | -14.4522 | -43.944199 | 2026-10-10 00:09:00 | METOP-C | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8a1abe49-cad8-3b25-bcd0-784668b155d2 | -7.5279 | -45.307598 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cdce1503-74ed-3be1-bd5d-49d813cfd7fc | -7.0033 | -47.654301 | 2026-10-10 00:09:00 | METOP-C | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 4b9441a4-b8e3-37fb-9503-1439f4150bfd | -17.949499 | -42.4837 | 2026-10-10 00:09:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 206a3be9-571c-3bf9-8e21-bed76fb8c5be | -17.9613 | -42.491798 | 2026-10-10 00:09:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 8c518d83-ddef-3c01-8874-9fc1679dade8 | -7.5083 | -45.311798 | 2026-10-10 00:09:00 | METOP-C | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| a8a18d0a-488a-39a1-920f-ec19b39c6a3a | -17.953501 | -42.504002 | 2026-10-10 00:09:00 | METOP-C | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |


[Clique aqui para ver as próximas entradas](README7.md)
