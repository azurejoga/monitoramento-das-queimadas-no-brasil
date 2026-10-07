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

## Dados Diários - Página 197

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d9b6e8ae-cdc3-3f3b-87f6-214aa1981cbf | -8.75793 | -44.15464 | 2026-10-07 16:37:00 | NPP-375 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 20.8 |
| eff24169-bdaa-34b9-b8c3-aa2b15aafa95 | -7.18455 | -44.31797 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 8183f5d7-c2cc-3a13-9da8-2890e73d7ff8 | -6.13889 | -51.93451 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 77.7 |
| 8eafa3b6-1887-3ea2-99c8-903238fe3e1c | -3.70391 | -40.83923 | 2026-10-07 16:37:00 | NPP-375 | FRECHEIRINHA | CEARÁ | Brasil | 2304509 | 23 | 33 | nan | nan | nan | Caatinga | 69.6 |
| ccf08bdd-9cbd-3d16-a0c5-524ee71a6917 | -9.53047 | -46.85503 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.2 |
| c24b3a50-dd3e-31b3-ae84-6519e805e8a3 | -5.60605 | -45.58826 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 88daa8ab-a850-3273-96f1-b8fa07a4c57e | -5.7563 | -42.03764 | 2026-10-07 16:37:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 2705eb9c-c05d-3617-b20f-06adbdb01d78 | -3.91849 | -44.14025 | 2026-10-07 16:37:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 89ec1fcf-b616-3d35-98b8-cea232a1969a | -6.32649 | -43.75 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| dd1be3c8-5c31-3291-a17c-5ad1f84be930 | -4.31639 | -43.00106 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 3f2279e5-93c1-3a6f-b42b-12ac53c2bdda | -5.31229 | -48.00906 | 2026-10-07 16:37:00 | NPP-375 | CARRASCO BONITO | TOCANTINS | Brasil | 1703891 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 650611a2-7450-3e31-9209-3142ac8137d9 | -5.38051 | -45.92202 | 2026-10-07 16:37:00 | NPP-375 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 82a409c2-ee80-36ad-a1a9-b95472e844c5 | -11.10605 | -45.68139 | 2026-10-07 16:37:00 | NPP-375 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 5266609b-da28-3032-a915-f5d6e978a5cb | -5.50072 | -42.82938 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| a7c75da3-ea1b-3c4c-9adf-7898d08af919 | -8.07185 | -55.29789 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 37.6 |
| edd616e1-9b2e-36ba-8644-438d45311661 | -6.14444 | -52.64779 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 347b419c-9035-372d-bd13-99aeae159b9d | -7.4451 | -55.56897 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6001156a-fd4b-3af5-98f0-571f175aa72c | -10.49296 | -49.27652 | 2026-10-07 16:37:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 60f5d91e-a252-3301-8529-ca3d3e48e433 | -3.73455 | -39.53022 | 2026-10-07 16:37:00 | NPP-375 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 11.3 |
| ca0b94ab-2118-3224-81e0-8763a61bac37 | -5.2306 | -40.57978 | 2026-10-07 16:37:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 2ac06379-af7d-32de-b97d-78bdfb71da59 | -6.68961 | -44.95787 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 96f4eaf3-8ea8-33e1-bff1-c3d3d2280a82 | -15.36773 | -41.23136 | 2026-10-07 16:37:00 | NPP-375 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.5 |
| bd64b8d8-fa18-38aa-862d-00a44204072b | -9.38352 | -49.36226 | 2026-10-07 16:37:00 | NPP-375 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| e8179eed-493d-33fe-bb6b-e0f3739fc2f7 | -6.17448 | -52.92945 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| c370aa4c-b3e9-3c9c-ad0b-379387f60d36 | -3.9495 | -41.55164 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| 1562f0ab-4254-371b-b6fd-d61ed317f2d6 | -6.44142 | -45.21086 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| fce1da75-94b3-39bf-9c82-f96cc8de3e25 | -4.14791 | -43.19809 | 2026-10-07 16:37:00 | NPP-375 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 49.4 |
| 2c4a4974-a921-3842-b899-a15fda078b1f | -5.75977 | -42.0371 | 2026-10-07 16:37:00 | NPP-375 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 12.5 |
| 8bbfca67-e6de-3cdf-a8c7-c4588309790f | -5.85507 | -42.66182 | 2026-10-07 16:37:00 | NPP-375 | LAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2205540 | 22 | 33 | nan | nan | nan | Caatinga | 32.5 |
| 61d1dbc2-02ef-3ed9-a338-45f266b6870b | -6.44088 | -45.20733 | 2026-10-07 16:37:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 14070951-c293-37f6-b902-f617ef8c3252 | -9.24063 | -45.66051 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 3716e9e2-2a8b-37c1-a09b-220cfa2c9924 | -4.513 | -42.896 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| cd6889cc-2c87-3135-b94d-1966d46f0192 | -7.77194 | -48.23782 | 2026-10-07 16:37:00 | NPP-375 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 0667647a-e35a-361e-8cab-b719dc9f097f | -7.10851 | -55.72722 | 2026-10-07 16:37:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a7fcb458-574a-3c14-823b-e7dc4682e234 | -5.46978 | -45.70106 | 2026-10-07 16:37:00 | NPP-375 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 46158f46-102f-307a-a436-db0962afefe9 | -15.10774 | -44.08426 | 2026-10-07 16:37:00 | NPP-375 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Caatinga | 10.0 |
| a0461550-a451-3734-88fe-d2df220558c3 | -9.53783 | -46.85389 | 2026-10-07 16:37:00 | NPP-375 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| de8068d1-43c5-3349-a8f3-a2a53deed0f5 | -11.11128 | -47.58578 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| f25863a7-b0c9-3c83-b595-9dc83110dbd3 | -4.91601 | -43.22285 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 1d10c075-7c94-38db-bbca-1282c9b920c4 | -8.3904 | -48.07318 | 2026-10-07 16:37:00 | NPP-375 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| ac95c3d4-05b7-365f-8fcd-936e8d26a462 | -6.83404 | -48.84103 | 2026-10-07 16:37:00 | NPP-375 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 65c6dd46-0a0b-35e4-81c1-8c8cf9ca6be2 | -6.65359 | -43.78689 | 2026-10-07 16:37:00 | NPP-375 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| baf484e5-bcf9-346a-857e-2364ddf91b5a | -5.95696 | -46.36699 | 2026-10-07 16:37:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 189.1 |
| 17620843-7434-32ab-bfc5-cf793b471a38 | -4.30639 | -40.69411 | 2026-10-07 16:37:00 | NPP-375 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 8a2eb533-8cfd-3408-8759-c7becaac30c0 | -10.36464 | -56.43873 | 2026-10-07 16:37:00 | NPP-375 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.6 |
| d49de213-65b1-373a-9f91-d4dc3c4acf72 | -11.10056 | -47.62335 | 2026-10-07 16:37:00 | NPP-375 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 31.5 |
| 5e6cc7a0-5273-39b7-8e69-6436a147e455 | -4.0238 | -43.34175 | 2026-10-07 16:37:00 | NPP-375 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a233c8fa-c359-32c1-bd3e-6576fab1d088 | -15.64374 | -43.29529 | 2026-10-07 16:37:00 | NPP-375 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Caatinga | 5.5 |
| e9d7673f-e464-3bcf-8f01-d8d1d57e5051 | -15.66774 | -39.70438 | 2026-10-07 16:37:00 | NPP-375 | POTIRAGUÁ | BAHIA | Brasil | 2925402 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 652f1238-e91f-3e9a-aafa-71a92b17ae4d | -8.99037 | -45.94651 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 11.2 |
| a1291c45-66ac-3e37-b4ba-07803fef76a5 | -4.51583 | -42.89182 | 2026-10-07 16:37:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 2d103ff7-8ab6-37bb-b26b-cf000e35acb9 | -9.1901 | -45.6907 | 2026-10-07 16:37:00 | NPP-375 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 31df9112-5842-3403-93f9-4aa423dbb73a | -6.68259 | -41.76756 | 2026-10-07 16:37:00 | NPP-375 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 6a9283d5-e86e-3139-a5d9-f7384cafa8b9 | -3.31533 | -43.27721 | 2026-10-07 16:37:00 | NPP-375 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 81ce0e93-6f2b-3e8a-8c2c-8319f5417ff4 | -7.20441 | -55.11649 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 32.8 |
| 9ad89de5-60a5-3581-9f68-4b982b6d8bcd | -7.59162 | -47.01772 | 2026-10-07 16:37:00 | NPP-375 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| ed6a0e4a-b6f3-3f1f-851f-f49b2f4cedb1 | -6.93605 | -45.27304 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 0fa8dfd9-5e2e-3bf7-8080-d489aafa71b7 | -6.01107 | -42.27179 | 2026-10-07 16:37:00 | NPP-375 | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 60605ba3-4eed-3f37-a9f4-6de127e0c057 | -14.77587 | -41.60073 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 86.0 |
| 41cd3198-8cba-3280-96a5-3566c23c9db7 | -10.24035 | -49.65405 | 2026-10-07 16:37:00 | NPP-375 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| e280aa8d-970e-322b-9ccf-8aba7955c43e | -3.77486 | -44.35417 | 2026-10-07 16:37:00 | NPP-375 | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 59285957-3d96-30b7-9075-5449cbd414db | -7.21746 | -44.29424 | 2026-10-07 16:37:00 | NPP-375 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9ac74661-7587-35d9-89aa-724490015e29 | -3.50127 | -41.94447 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 11.7 |
| 3f12bd54-b7a5-3d05-97fd-18e8480724cf | -6.23732 | -43.73958 | 2026-10-07 16:37:00 | NPP-375 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b00a487e-33c0-3be2-afed-c922a255e2d8 | -17.022 | -45.92577 | 2026-10-07 16:37:00 | NPP-375 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 7035c457-70b0-381f-8f7f-19023bccd4a4 | -3.77216 | -41.77919 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 17.8 |
| a3ecf08f-0b68-384e-bce6-6b0a8265759a | -5.10078 | -42.92958 | 2026-10-07 16:37:00 | NPP-375 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 14e4cf23-86d9-3b76-a720-321e75234755 | -3.30585 | -42.47177 | 2026-10-07 16:37:00 | NPP-375 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 24ad0954-95dd-3282-9dc9-3b31ea1aa397 | -3.94886 | -41.54749 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 85.8 |
| a7fc6889-a918-39d6-9e1e-d8c9f1b81b40 | -6.94066 | -45.2578 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| a7c50a31-ef86-333d-a03a-d7c42050af33 | -11.3857 | -46.67652 | 2026-10-07 16:37:00 | NPP-375 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 1c5c1044-d339-3b81-a7ab-4586ae8e5401 | -3.56995 | -43.09602 | 2026-10-07 16:37:00 | NPP-375 | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 45.0 |
| 750251a8-abe9-317e-bb69-8cb5df99fddf | -8.46772 | -48.69073 | 2026-10-07 16:37:00 | NPP-375 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7b7586e9-f4f2-3d0c-a3e0-1c79b5af6378 | -3.50319 | -41.9566 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 133.0 |
| 88e664e2-59c9-35f6-a6cc-096e92eb50c8 | -8.20024 | -35.39019 | 2026-10-07 16:37:00 | NPP-375 | POMBOS | PERNAMBUCO | Brasil | 2611309 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| d2e6a241-d593-3b61-8864-b917cc772e5a | -15.07224 | -39.62362 | 2026-10-07 16:37:00 | NPP-375 | ITAJU DO COLÔNIA | BAHIA | Brasil | 2915403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| 9f5ab468-9740-39fe-be33-132355bbf5a7 | -6.93943 | -45.27256 | 2026-10-07 16:37:00 | NPP-375 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 846cb7fd-6533-3847-90c0-5df28fea12bd | -15.08645 | -41.40789 | 2026-10-07 16:37:00 | NPP-375 | TREMEDAL | BAHIA | Brasil | 2931806 | 29 | 33 | nan | nan | nan | Mata Atlântica | 26.2 |
| cd6a9dd6-973d-3790-9357-b608c745c25b | -6.95618 | -44.4178 | 2026-10-07 16:37:00 | NPP-375 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5f7cda08-dd0f-31bb-8abb-a3f958781c4b | -8.25861 | -54.7043 | 2026-10-07 16:37:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 83752eda-5557-3d1e-8337-9cf8d6446e7d | -5.49563 | -42.84123 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 37.2 |
| 8e89af3e-1b10-3cbf-88ba-8bc30bab59b1 | -10.78982 | -46.53969 | 2026-10-07 16:37:00 | NPP-375 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 23eb6420-dc9e-32cc-8c98-d72611fa8933 | -5.99572 | -44.12889 | 2026-10-07 16:37:00 | NPP-375 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 10610f6e-cd8c-34ea-8233-53fa30eab2a3 | -3.95183 | -41.54279 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 3100c1f3-9b18-3016-a069-49b210dcd9a9 | -6.41139 | -52.71385 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 888ad37a-b5ab-311c-b258-9eada5a89a29 | -3.77059 | -41.71307 | 2026-10-07 16:37:00 | NPP-375 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 2da69147-6ef9-3cf2-9183-8a790198d857 | -6.58338 | -53.03325 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 11.0 |
| 29752835-1cee-35e5-8b8d-d1023c9e44f1 | -8.90353 | -48.17839 | 2026-10-07 16:37:00 | NPP-375 | TUPIRAMA | TOCANTINS | Brasil | 1721257 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b5ec561d-bf7a-379f-8d40-bcd481d1e425 | -14.87401 | -41.71316 | 2026-10-07 16:37:00 | NPP-375 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1d81ff5a-a6ae-359f-9daa-35667f19e6b1 | -4.50577 | -45.99603 | 2026-10-07 16:37:00 | NPP-375 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d86de6fd-1870-3abc-a89b-3e7d71e62edd | -3.50776 | -41.93936 | 2026-10-07 16:37:00 | NPP-375 | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 1d1f4a21-aaa6-3f18-be57-7f9097eacd13 | -8.46255 | -36.82541 | 2026-10-07 16:37:00 | NPP-375 | VENTUROSA | PERNAMBUCO | Brasil | 2616001 | 26 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b311ab42-efe6-3292-a9d4-77cf9cb2e9ab | -15.56564 | -44.5193 | 2026-10-07 16:37:00 | NPP-375 | JANUÁRIA | MINAS GERAIS | Brasil | 3135209 | 31 | 33 | nan | nan | nan | Cerrado | 8.6 |
| fc7fd36d-da7d-36d8-b70f-cddf7354a4b8 | -5.49337 | -42.84895 | 2026-10-07 16:37:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 39.8 |
| 0df22afe-27f3-398b-bf70-65e657d1c7cb | -6.48401 | -52.81559 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| aa7c4901-f3cd-3124-9527-593c4464f66c | -6.21037 | -53.22158 | 2026-10-07 16:37:00 | NPP-375 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| f2cb6d6f-6419-3b5b-a512-e2e7e1828c08 | -11.01298 | -47.97276 | 2026-10-07 16:37:00 | NPP-375 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 33.5 |
| f6e083d5-5886-320a-b8ec-30395839fa4e | -3.76891 | -41.77162 | 2026-10-07 16:37:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| d01d04d3-6d99-3ce2-a908-3cc96653d39c | -5.23434 | -40.57918 | 2026-10-07 16:37:00 | NPP-375 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.7 |
| 5e7aada4-3007-3fce-b013-8f1c954fb519 | -3.28768 | -42.58401 | 2026-10-07 16:37:00 | NPP-375 | SANTANA DO MARANHÃO | MARANHÃO | Brasil | 2110237 | 21 | 33 | nan | nan | nan | Cerrado | 8.8 |


[Clique aqui para ver as próximas entradas](README198.md)
