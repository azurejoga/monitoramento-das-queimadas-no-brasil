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
| 6cc8784a-e96b-3b78-a2a1-5298205c6eec | -4.42711 | -43.40717 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 001e27da-8e45-3c4c-968c-2991e5b44612 | -4.4323 | -43.40798 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e83883ef-84d5-3e2f-9a7b-2f0e50020e15 | -9.50426 | -47.27319 | 2025-11-16 03:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3189bcc3-cedd-3895-84ed-c5a2b140e433 | -8.57805 | -46.05257 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 165bd920-3e6e-39b9-8b06-cd509a5cf03f | -6.81212 | -48.7874 | 2025-11-16 03:46:00 | NPP-375D | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8817e744-aad3-34fc-a487-8eb998f68759 | -6.55308 | -43.2397 | 2025-11-16 03:46:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8bbb97dd-590d-3fe2-9990-65d675a3d119 | -6.30625 | -43.79223 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 21.7 |
| 9c87764e-43be-3beb-80d0-0270a2ec571f | -6.68765 | -40.80744 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 5169968e-357c-3a62-a430-4f6d38b83e18 | -7.15355 | -41.75308 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| cfebb08a-1003-31bd-9dca-c4d414ab16ef | -5.41852 | -43.25619 | 2025-11-16 03:46:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79a0220c-9d31-388d-9cbe-5b829c75ea8a | -6.00147 | -41.90654 | 2025-11-16 03:46:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 7cde55b2-aa9d-3965-8f62-056ab009e1b5 | -6.08846 | -41.61596 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ebb3cba1-5b7b-3826-9a76-aa4a3e774bdc | -6.36352 | -39.6225 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a5be3974-e425-3c8b-b422-96c542d8bba2 | -4.70056 | -46.31841 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 62673974-6eb6-3cfe-96bc-88dc00acf84d | -6.36063 | -46.16225 | 2025-11-16 03:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 997c77e5-0b4b-3640-b645-c59fbf85c349 | -10.00683 | -44.76625 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 367463ed-1c12-300b-a8de-2e7161ae700a | -10.12054 | -43.90493 | 2025-11-16 03:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ca9df48d-d274-3407-a8de-e56d6955a775 | -7.26447 | -48.03587 | 2025-11-16 03:46:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 43c73264-a2e9-3114-b779-44fe8647d9e3 | -5.68819 | -45.98843 | 2025-11-16 03:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b4ed015-9035-3e57-9813-536d27e11a09 | -6.51595 | -39.52742 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| a4675e06-ac4a-37c6-b959-9033a563feac | -4.84359 | -47.55426 | 2025-11-16 03:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e3e5fe60-0c13-3063-b121-f11d92206f99 | -9.1132 | -40.45638 | 2025-11-16 03:46:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bb6f0a77-17f5-38dc-934c-258d361665ed | -4.6868 | -46.52539 | 2025-11-16 03:46:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 2049d700-1d93-3c4b-86d8-64d2d1bad1e8 | -5.48459 | -40.97799 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d4b55b3-21ad-361e-96cd-05f6364d6fbc | -8.31639 | -45.40371 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5dff3a9e-3ced-3d38-a954-591dea655feb | -7.04958 | -45.94007 | 2025-11-16 03:46:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6d42b711-c737-31c8-a76b-77a8a8452478 | -6.71792 | -42.94249 | 2025-11-16 03:46:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e33fd3ae-53c6-312f-80e6-ed66eaa684e9 | -3.85645 | -39.83068 | 2025-11-16 03:46:00 | NPP-375D | IRAUÇUBA | CEARÁ | Brasil | 2306108 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| ab5152e1-7f7b-3c27-ac6b-6aba654fe359 | -4.43147 | -43.40697 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2c3032dc-e97c-3ffc-a6ee-04d90664bb7d | -9.69486 | -37.77852 | 2025-11-16 03:46:00 | NPP-375D | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 72ae66db-530e-36f0-9f26-11d19061ce43 | -6.0678 | -41.54928 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 896ea54d-9458-3242-8525-9a2dd6cb9a23 | -4.74466 | -46.38092 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 55a5ba00-e310-32ac-a4bb-2749a6992b49 | -8.61929 | -40.69359 | 2025-11-16 03:46:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 615d45d2-287a-36d1-b186-782dbccb19ee | -11.71229 | -37.64721 | 2025-11-16 03:46:00 | NPP-375D | CONDE | BAHIA | Brasil | 2908606 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e77c424-718b-318d-8b30-dbbf91844436 | -7.28118 | -38.90653 | 2025-11-16 03:46:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 66e26e61-614d-3cdf-812e-71ff581dc6bc | -7.22097 | -38.77767 | 2025-11-16 03:46:00 | NPP-375D | BARRO | CEARÁ | Brasil | 2302008 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| e7fa2c45-4f3a-3f27-a416-d9b471f3d291 | -10.32615 | -44.60844 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93ab1dca-8c9d-39d5-a219-e93e22a3b6f3 | -4.84075 | -45.42638 | 2025-11-16 03:46:00 | NPP-375D | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| efbf6ee6-3898-3be0-9d6c-8b7b2cba6225 | -10.00849 | -44.7858 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 39f7988e-038f-33ba-aa22-6bb9e3e8b732 | -2.52096 | -47.81191 | 2025-11-16 03:46:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| c6c837cd-7da4-3dba-86dc-ed5014c5895a | -6.31876 | -43.8116 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec6038db-0b41-3268-bba9-de5930307e11 | -5.48765 | -44.83966 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef5f2fd1-5aa9-389a-ac44-3302855ebd71 | -5.09303 | -41.4772 | 2025-11-16 03:46:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5d3728bd-97ac-3f48-bb2b-c6691260e93f | -10.248 | -45.06178 | 2025-11-16 03:46:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b4beb785-7285-3139-9468-2b4ea0ccf6ae | -4.84262 | -47.55965 | 2025-11-16 03:46:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| d0df885f-bd46-3b29-8bc9-ea7efee480e0 | -6.67641 | -40.7975 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c57aa5c1-e411-3314-80c7-938c3f2f4789 | -9.7328 | -43.95114 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 7a87ab4c-b07d-3c26-854e-f626b5f8b62a | -3.95918 | -44.84969 | 2025-11-16 03:46:00 | NPP-375D | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 152da760-5336-379a-b84e-38f4b88c5bba | -8.57832 | -46.05095 | 2025-11-16 03:46:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 471863c7-435c-3d65-8b8a-0f4689aee2d7 | -6.95387 | -38.40374 | 2025-11-16 03:46:00 | NPP-375D | NAZAREZINHO | PARAÍBA | Brasil | 2510006 | 25 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7731c74c-72d7-31bb-9ab0-13b31f3810f9 | -8.33697 | -41.25386 | 2025-11-16 03:46:00 | NPP-375D | PAULISTANA | PIAUÍ | Brasil | 2207801 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 533bf409-f4f5-3f3f-ace1-4ad725c0af66 | -7.11683 | -46.15674 | 2025-11-16 03:46:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b2cbe35-a656-3e14-a339-b23a9b79d28e | -7.28487 | -38.90715 | 2025-11-16 03:46:00 | NPP-375D | MILAGRES | CEARÁ | Brasil | 2308302 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e13fd5d-ef3d-332d-8b43-381d7010b7a8 | -8.31558 | -45.40813 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1eaba034-3cc4-38d5-9758-6a7936d9f394 | -10.12442 | -43.91123 | 2025-11-16 03:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f45bb771-416c-3554-858c-c6fd2c13b54c | -10.16083 | -44.50532 | 2025-11-16 03:46:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 87b6f3d4-f335-3391-a4ad-f45558a77d87 | -7.05454 | -42.24716 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| fda4048e-a2b9-37a3-badc-b8ca1892e648 | -7.05372 | -42.25192 | 2025-11-16 03:46:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| d604140c-f748-3909-a768-57e528f36544 | -8.32041 | -45.41306 | 2025-11-16 03:46:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e26cd1c3-bc19-335b-bf28-2a58a30878f7 | -5.48701 | -44.8434 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| db6ad375-1e98-3b47-bd8e-89cf92486bf1 | -6.06909 | -42.87133 | 2025-11-16 03:46:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 8925ee1d-5934-3510-83a2-161199c536fe | -6.29987 | -43.79812 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 28b09b7c-926b-33f9-9a96-255862414949 | -9.67671 | -37.09214 | 2025-11-16 03:46:00 | NPP-375D | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 6d44cb2e-fc5b-345c-9691-82b218521604 | -3.86852 | -40.6427 | 2025-11-16 03:46:00 | NPP-375D | CARIRÉ | CEARÁ | Brasil | 2303105 | 23 | 33 | nan | nan | nan | Caatinga | 1.7 |
| ee7bf91a-df5c-3786-baa2-738e9850424b | -5.63916 | -47.74344 | 2025-11-16 03:46:00 | NPP-375D | AXIXÁ DO TOCANTINS | TOCANTINS | Brasil | 1702901 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 33804ab7-2c39-3060-b612-ceff1899773c | -4.73139 | -46.38304 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7a1541d6-45ba-315f-9463-3d1add23dfcb | -10.00507 | -44.7756 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1225119-e271-30b2-97b4-82d831378287 | -3.79828 | -43.37569 | 2025-11-16 03:46:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 59e781f1-3e51-365e-92f4-a8b41b7884e9 | -10.00357 | -44.77781 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 593eda88-c662-37d7-9cb9-0bc0e957fddc | -5.48139 | -44.8425 | 2025-11-16 03:46:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30cd6786-8b0e-3c81-b11e-17664aa15e9e | -9.73072 | -43.96235 | 2025-11-16 03:46:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 550d57ae-d798-3f36-ab36-70bd7f786cd2 | -4.61145 | -43.29939 | 2025-11-16 03:46:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f13691e2-a3ba-320b-b5a6-877d201bd5a9 | -3.99953 | -44.2681 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f7c71dad-20dc-3131-925e-faa4fe0fbffb | -8.90345 | -44.43633 | 2025-11-16 03:46:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5e0142c7-6408-3516-9932-67f90155c425 | -4.42372 | -45.55864 | 2025-11-16 03:46:00 | NPP-375D | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 68921c3e-d7f9-35e2-b010-97dc43ae807a | -6.98299 | -39.16505 | 2025-11-16 03:46:00 | NPP-375D | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ca00d4d1-9d70-3ed3-a7cb-305d2eab8d0f | -6.50087 | -39.51797 | 2025-11-16 03:46:00 | NPP-375D | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e4b3c9d-a52a-35ff-bd98-9cb8d42d6936 | -6.30388 | -43.7978 | 2025-11-16 03:46:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 15.2 |
| 1771bdbb-9bf8-333b-a003-8eda888d4edd | -7.01552 | -45.16593 | 2025-11-16 03:46:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9ef779f0-e52c-32fa-8f1b-f0927d9a3050 | -5.46815 | -40.99692 | 2025-11-16 03:46:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fd98cfd3-a991-36a9-9b64-be3fde3d04c7 | -3.99891 | -44.27175 | 2025-11-16 03:46:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 08594475-468b-33d5-9396-3c72e6a3a8b0 | -5.3417 | -43.04327 | 2025-11-16 03:46:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 870d8374-c228-3a34-959a-e85bc5dd4617 | -7.35218 | -43.33806 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| df361ff8-042d-3790-98e0-9794b5e15398 | -6.70213 | -40.79792 | 2025-11-16 03:46:00 | NPP-375D | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| c948520a-2523-3df6-80a2-902e5e856dfa | -7.71925 | -47.30283 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4ab6314c-177b-351c-86f2-2ee2a95bf7e4 | -6.93929 | -41.53172 | 2025-11-16 03:46:00 | NPP-375D | SANTANA DO PIAUÍ | PIAUÍ | Brasil | 2209351 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 27485176-5c9f-3080-b2e1-92c9cd2ffc75 | -7.71294 | -42.94076 | 2025-11-16 03:46:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| ac5d81d3-709d-3fd8-a719-2ac62b139517 | -6.57462 | -47.90186 | 2025-11-16 03:46:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ede8e40a-4452-343b-bb64-a3234a4d4698 | -9.51054 | -47.27185 | 2025-11-16 03:46:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 60fcc9b0-22ad-37cf-8764-126a315f4ce9 | -6.25649 | -41.42079 | 2025-11-16 03:46:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 62aacc70-be61-3be3-844b-7d6cfefe570a | -7.36297 | -43.32752 | 2025-11-16 03:46:00 | NPP-375D | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1f74b3c4-ae35-3d54-9101-ae893fe55640 | -4.69513 | -46.31264 | 2025-11-16 03:46:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1828670-15f7-3035-ba66-8abaeaf1b12e | -7.11579 | -42.73866 | 2025-11-16 03:46:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 3867e73a-23cc-3788-9bc7-52abb66d1485 | -4.62201 | -47.41127 | 2025-11-16 03:46:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 46e63e32-03b5-301b-9159-3d6c1cc2ea9e | -10.12153 | -43.89949 | 2025-11-16 03:46:00 | NPP-375D | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f403d44-ea9e-3179-a71e-0e881c114928 | -10.00053 | -44.77134 | 2025-11-16 03:46:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9fa0f38e-9803-30a9-8334-fbfb0218d6c2 | -7.84277 | -47.1753 | 2025-11-16 03:46:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a1915cca-a378-39e5-b5ac-27acc9ad3579 | -4.94139 | -44.53425 | 2025-11-16 03:46:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 53a450cb-378d-36bf-b37e-b1433ad2a1c5 | -4.09672 | -40.51511 | 2025-11-16 03:46:00 | NPP-375D | VARJOTA | CEARÁ | Brasil | 2313955 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 68d6b87d-c087-39bd-b2a1-00fa5962ee73 | -7.38725 | -45.52023 | 2025-11-16 03:46:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README21.md)
