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

## Dados Diários - Página 13

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f6565f60-7295-31ec-9a50-ba071279ba81 | -5.60518 | -46.24604 | 2025-10-15 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea1fbea8-6954-35cf-91b6-6735329b7c15 | -5.40196 | -41.15016 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 528b67c1-9772-36ec-bda5-ffb5de8d8ed8 | -7.25862 | -44.91293 | 2025-10-15 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| be890085-fc4b-32b6-bcb7-7734f4ced4db | -6.17188 | -42.6169 | 2025-10-15 03:47:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 296abd68-3090-3306-b50d-601cf6f07c53 | -5.87091 | -43.85354 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9a531661-95a7-3096-bd96-c0a58e6ba97a | -5.39362 | -44.03879 | 2025-10-15 03:47:00 | NPP-375D | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 3d70081e-ce94-34a3-9298-e0b7a294e917 | -5.42568 | -40.98274 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 9b74cab8-46c6-3b4c-9cc8-048107fcfa68 | -6.45215 | -44.58547 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 484e9727-844b-305c-ac66-6111341dbaf6 | -6.45866 | -41.89109 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 12a9709c-db34-3c40-ac78-c35dc50dcb65 | -5.56669 | -42.9849 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b15cd0ef-0b4b-3c8f-9184-b56094d7d841 | -5.34696 | -43.7453 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ba427275-e2bc-3d7d-aa8a-ec0c93642d93 | -7.01468 | -41.95532 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9487c5f3-1630-3238-80e0-90140a498399 | -5.87387 | -43.86713 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 191542aa-40c7-3738-be25-7331be240f18 | -6.38895 | -41.48204 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 27512f52-7f8d-3e7b-978e-32893156267c | -6.89281 | -43.96925 | 2025-10-15 03:47:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5df48e63-3899-3528-983b-92b4e4417b60 | -5.26766 | -41.01739 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 746d146a-c4bf-381a-a078-acf7bf736ace | -5.5379 | -41.32831 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| faa232d1-c04c-30ca-9501-4f810b3674a2 | -7.92853 | -44.13492 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ce1ffab7-5405-3791-8882-fc0dc2fbeae7 | -5.83334 | -42.33485 | 2025-10-15 03:47:00 | NPP-375D | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| c0591876-0701-342d-a217-b934ba959824 | -5.40568 | -40.89231 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 82642611-3d09-3d77-b6eb-f3cbb0d673d2 | -6.74168 | -42.15345 | 2025-10-15 03:47:00 | NPP-375D | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6f26cca9-7038-37c4-b123-f6eef528ec50 | -6.14204 | -41.76727 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d6cefd49-a748-3fec-ae97-a4f7599aba08 | -7.50853 | -46.64185 | 2025-10-15 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 74decdc6-7771-3093-ac65-2e007f83b6ce | -10.04845 | -48.71257 | 2025-10-15 03:47:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| cdbd5a8d-c98d-30f3-9f81-e4efea898336 | -7.94845 | -44.14172 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8ef4be8c-2486-39f8-95a9-282b75ea3062 | -5.31575 | -42.92661 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ee6b0f90-d36c-3082-96bc-5b11b35b6a44 | -5.33782 | -42.56635 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| b71664a4-d2b7-3ef5-b556-93837823ea65 | -5.42771 | -40.66503 | 2025-10-15 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b593c2bd-2ba8-3f55-8865-873783084f57 | -10.15536 | -44.91842 | 2025-10-15 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c8557f7e-0b9a-3b4f-8a59-f9463e888b2b | -5.42929 | -40.98764 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 5cb13103-c71e-373d-8469-cdfb4065b4f8 | -8.19223 | -43.97973 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3f9fc23a-5025-3c7e-ad84-665cb70d3d05 | -5.39474 | -41.16641 | 2025-10-15 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b4f032b4-a0a8-3138-a49d-8caae3a20c9a | -6.41005 | -45.36493 | 2025-10-15 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a52d0f63-696b-3671-91bf-c5f1fe1ca518 | -5.86191 | -43.87405 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efa8760b-0477-3111-bad9-9cacb81c8462 | -5.86434 | -43.85782 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a1850b73-0ca6-3855-83c6-551fe792e217 | -8.21844 | -44.08618 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 12a8fc6b-6cb7-3132-bef3-436bc54279fc | -7.4897 | -42.14347 | 2025-10-15 03:47:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 75f9330c-9aa3-34f8-9b7e-1f6eb8584334 | -5.98183 | -42.86697 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| c0438f1d-d460-331c-83cd-9efc8d8e85e6 | -5.34227 | -43.74112 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27f53838-a31a-3afa-a440-a90e3c11eb17 | -8.1952 | -43.98443 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83f636a6-2ce9-3cc3-96a4-24417777e147 | -5.16031 | -45.16405 | 2025-10-15 03:47:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7377631c-f89f-3e81-ba3b-fa7e0fe81c80 | -4.9186 | -41.54171 | 2025-10-15 03:47:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| c72b06f9-4195-307b-8211-9e8ea50eee92 | -7.56377 | -43.89947 | 2025-10-15 03:47:00 | NPP-375D | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 57e19de5-215c-3cc4-98bb-2fe24b807653 | -10.33342 | -40.62042 | 2025-10-15 03:47:00 | NPP-375D | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 81544335-2d25-3952-851e-dd53a62a730e | -7.08212 | -41.95066 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b93a34fb-522f-3106-a8f0-20e400474fc3 | -8.21744 | -44.03398 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ab41c8c3-6d0c-32df-b6e8-1482e299e4e4 | -5.91875 | -42.82753 | 2025-10-15 03:47:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6c2ba86c-cc50-34ff-8883-7d2eb05bab81 | -8.21453 | -44.02129 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 39952a44-dda0-30af-9b2d-f25b6c23fe54 | -7.74865 | -42.45823 | 2025-10-15 03:47:00 | NPP-375D | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 9b545016-9b82-36f5-b012-24cf4722baf5 | -6.05499 | -41.89186 | 2025-10-15 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fd88f753-8d34-3ac4-9789-8e3b4879710a | -5.87247 | -44.21623 | 2025-10-15 03:47:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0496db3c-4702-3406-b55e-1529c1fec420 | -6.3462 | -42.65715 | 2025-10-15 03:47:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 4f294304-2de3-3cff-bb83-f03d1fb72bdb | -4.87625 | -45.77921 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 989fb345-8b8a-3027-8c67-53c232396970 | -6.45756 | -44.58639 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bc29c84a-fdf9-3f3d-ae10-4e621c2182ef | -5.84135 | -43.95938 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32676f38-17a7-3717-a423-696f1bec9975 | -4.65104 | -43.13257 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 583ef31a-9ccb-3656-a6ab-0b36a1f8ab4f | -6.76994 | -42.81292 | 2025-10-15 03:47:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| eb4c897b-c78b-3f8a-b7d0-7eb26346d172 | -5.43148 | -41.34699 | 2025-10-15 03:47:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| e454898f-1a43-3984-a7d0-a7965ce8d6d5 | -6.25534 | -44.021 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 90a4affa-6c6e-31f1-8f59-55c632ac14a7 | -4.82894 | -42.77785 | 2025-10-15 03:47:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 60af66a7-e9aa-3d00-8251-90c13dce1630 | -4.90722 | -43.46092 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| aed03294-7610-3c2c-b581-933d2c5c74c1 | -4.90207 | -43.46004 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 39.4 |
| 274c2724-b2cf-3c7c-a144-eb27ebe8671d | -5.88428 | -43.74801 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6b2d7ec9-66d7-3d3a-811a-d79bf69fbde0 | -7.93983 | -44.13074 | 2025-10-15 03:47:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| f55a11bd-02aa-31e8-8374-219bc4048b5b | -7.08582 | -41.95591 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 64ba060e-3ea5-3698-b10c-afa35e7926f0 | -7.07316 | -41.94916 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 20eaa109-47a6-3509-94c4-d64fd6e7d4bb | -15.11378 | -42.47454 | 2025-10-15 03:47:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 22b2b25b-9cfa-3029-9d1a-c1d604672865 | -5.34692 | -43.74516 | 2025-10-15 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 13780fbb-b611-374c-bb17-f18f5ad7be7f | -4.20421 | -44.70573 | 2025-10-15 03:47:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f295ee97-b53a-3786-9cf8-0bc9af8bb4f6 | -6.37968 | -41.48685 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 18cf1f9c-c13b-39f2-8a7b-650a012c9588 | -5.45597 | -42.36748 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bb21c9ba-5d75-309f-84b5-3b6f987f2315 | -6.40935 | -45.36882 | 2025-10-15 03:47:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 05bd15f2-a182-3448-8d00-9a56a46226e6 | -6.23545 | -44.16197 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 674f468f-3550-30ef-8ccb-ee0e0fbc9c71 | -5.63058 | -42.68562 | 2025-10-15 03:47:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a6fadf57-d0a6-38b7-a8f7-7e3997496ab3 | -15.10975 | -42.47372 | 2025-10-15 03:47:00 | NPP-375D | MONTEZUMA | MINAS GERAIS | Brasil | 3143450 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| ce4bcca4-5c2d-3244-b298-2e2943e54900 | -7.07609 | -41.9588 | 2025-10-15 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7f0529b3-12b2-3f2b-99b7-82979127359a | -10.16694 | -36.18125 | 2025-10-15 03:47:00 | NPP-375D | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 5b3d522f-76be-3308-8d42-4ff9bd5b0f18 | -5.86247 | -43.87087 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 101df680-f52a-3ae7-937a-a609ee89e764 | -5.31269 | -42.91489 | 2025-10-15 03:47:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 442ff01a-9d3c-3870-a70d-bd7dbd2c58fb | -5.56951 | -41.32882 | 2025-10-15 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 24feda6b-9fab-333b-9a47-ff2eab669c60 | -6.23491 | -44.17128 | 2025-10-15 03:47:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dfbd00a9-dc08-306c-a47c-dc88b52bfbb3 | -5.72896 | -43.83502 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7e2ba53-9a7c-37e7-90e1-89b71da766fc | -5.44037 | -46.29178 | 2025-10-15 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d3c61ee1-c894-36ba-b162-30b1bf353a86 | -6.45944 | -41.88654 | 2025-10-15 03:47:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3932e248-8f0c-3fba-a776-f3f6474f5e33 | -6.99022 | -38.44593 | 2025-10-15 03:47:00 | NPP-375D | SÃO JOSÉ DE PIRANHAS | PARAÍBA | Brasil | 2514503 | 25 | 33 | nan | nan | nan | Caatinga | 1.2 |
| f35690e6-5290-3202-a132-ddff16757210 | -6.14278 | -41.76297 | 2025-10-15 03:47:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 45235b3d-9b6b-35b6-90c7-b1bcd8bdaf41 | -4.7717 | -45.74144 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 8b6c490e-3d18-3208-b27a-09b2fdadc54c | -5.72951 | -43.83182 | 2025-10-15 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9ddf8678-59fd-35e9-992d-790aaf378076 | -5.33482 | -42.56348 | 2025-10-15 03:47:00 | NPP-375D | BENEDITINOS | PIAUÍ | Brasil | 2201606 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 96621928-f9b6-3a5e-8b88-ec8415809270 | -6.45277 | -44.58194 | 2025-10-15 03:47:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8b97ec86-5fd6-3305-9239-bbc08d2f868b | -4.65708 | -43.12757 | 2025-10-15 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 621c15d4-565b-3ef3-a457-f946b460ea6a | -4.25308 | -45.58545 | 2025-10-15 03:47:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a905bb45-c848-3338-86c6-65ad76b57201 | -8.22459 | -44.08113 | 2025-10-15 03:47:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 10ba9ef8-2568-33b3-9a92-66e3e55003ec | -4.42762 | -47.75761 | 2025-10-15 03:47:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 367da4a7-ce2f-33d0-b2ac-4d9c391203d3 | -6.05486 | -43.39164 | 2025-10-15 03:47:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 30a48d07-14ea-3e90-b283-7e9fc501af63 | -4.77247 | -45.73714 | 2025-10-15 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 040a7ba4-f58e-3ca4-bfef-887858ce5074 | -8.73003 | -43.86641 | 2025-10-15 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| a30fe65e-f769-3ed8-b715-0ee992c2a486 | -8.72608 | -43.85989 | 2025-10-15 03:47:00 | NPP-375D | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 88babca4-ff6c-329e-bbed-bd81dc829737 | -5.03129 | -44.7397 | 2025-10-15 03:47:00 | NPP-375D | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c70b536a-ddd9-3bec-bb8b-0ce1b765916a | -5.87783 | -44.21701 | 2025-10-15 03:47:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |


[Clique aqui para ver as próximas entradas](README14.md)
