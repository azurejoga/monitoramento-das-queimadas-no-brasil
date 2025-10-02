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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94fe96fb-6e66-31ca-93c2-53564bdb7b99 | -11.56874 | -47.02598 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 521728ea-0c7c-3b68-a999-37559ad7773d | -6.48989 | -44.29805 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 06507301-7335-3dc7-bf8c-94af4628b159 | -11.59068 | -45.0551 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| c685a295-d011-3767-b720-57526804cf50 | -12.79934 | -46.85374 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 29eafe78-a964-35ce-8dce-2a501aa16b49 | -9.94121 | -43.70699 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77a0fa7e-196f-3cd8-aaed-dbcd86662384 | -6.1051 | -43.44625 | 2025-10-02 04:02:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| ee2af481-31ff-3c63-bee8-330daccdc9e3 | -11.82023 | -45.0111 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| eeb373aa-1008-31e8-8f85-e82105e5c429 | -12.84753 | -46.93791 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| edb1d6d6-9fd5-3961-8110-896fcdfa3d69 | -11.94828 | -43.91491 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f50a5a15-3dfb-36f9-89af-4867f6a458a5 | -10.3097 | -42.39234 | 2025-10-02 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| c2c56be9-64ba-3b39-9171-f1f9f1134c1f | -11.00338 | -46.5578 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| d93c1a5c-ab9b-3fbf-b112-b90222fd7afc | -6.69652 | -48.70501 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7c73f365-70ae-30dc-afb3-bfd7756dc4a2 | -5.79361 | -45.75411 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 747be3a8-ec5a-375a-80de-cdd59be2bb11 | -5.82665 | -42.86743 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 6.9 |
| 9a930fc9-97b0-3e38-8ed4-3b06949553cc | -11.03458 | -47.81924 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 7cbd0e55-c760-3284-a269-2e629c9502ac | -11.82159 | -45.02533 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 63a31364-225e-35bf-a178-1b658c1360f7 | -8.55865 | -48.64549 | 2025-10-02 04:02:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 40191edd-3da0-3312-b1ac-e611e5fdc13b | -11.78034 | -46.83718 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 832ac03c-729a-3ad7-8e6d-59b0c085b8bb | -10.22126 | -50.34177 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a0fbb5d1-f7e4-36c7-9836-233a2814229e | -8.90914 | -46.06636 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ebd95a7f-f1bd-3e1b-a301-107e2ffc4f2d | -11.80176 | -47.58459 | 2025-10-02 04:02:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 6e71e7fd-13f1-36b4-8375-3fbdbe787661 | -6.72784 | -44.1478 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 79a0149f-c217-3acf-b0cc-9ae31a6e7674 | -7.32425 | -45.24473 | 2025-10-02 04:02:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0084445d-2b64-3225-a1cb-45f198ab9e80 | -7.5611 | -42.64838 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 7ab3cf07-cc80-3e66-84d7-29e90414d891 | -6.53759 | -43.37503 | 2025-10-02 04:02:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 70f92369-434e-34f0-be11-98bc599dce92 | -8.3353 | -46.22241 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 957879c1-b69b-350f-92b9-a821237d721a | -12.75117 | -46.89025 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a95efd7c-ec33-3c33-9bcc-e16f06b2d3fc | -10.67181 | -48.56556 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 6290d33a-752f-3f90-9c04-1e1fbae8b8db | -6.69546 | -48.71115 | 2025-10-02 04:02:00 | NOAA-21 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 5b63a0ff-ea8a-3b6d-a069-4f9ca92a259f | -5.82796 | -42.85926 | 2025-10-02 04:02:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 925371ae-3a61-3d7e-adb0-3112d92b8250 | -10.22388 | -50.32795 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 03a9345a-b578-3a19-ab02-f2bfac7bef52 | -7.03839 | -43.33994 | 2025-10-02 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 94a5095c-8e2e-32f9-96c9-94943c9b679b | -6.3874 | -43.8776 | 2025-10-02 04:02:00 | NOAA-21 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 668d34bc-1df2-3475-b3a2-82e45776a3d8 | -9.79853 | -45.95034 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 732553d8-e3c8-3474-8c95-a1e0840ab85f | -12.82008 | -47.02078 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d9aa1d7-fdfb-3dec-b3a6-bc6f683479e0 | -5.88424 | -42.50727 | 2025-10-02 04:02:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| aa1586b0-2a97-3e14-88ba-cb70c4719a7b | -8.21288 | -45.52869 | 2025-10-02 04:02:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f5ce698a-1587-3084-9344-afb7d1ebd36b | -9.00094 | -46.70657 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 849d3b59-ab9e-3006-b01d-a21840afe453 | -9.59474 | -43.07064 | 2025-10-02 04:02:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 054fbe30-9807-3d56-9537-7bdcd195acfd | -12.70902 | -46.88993 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e5e12267-acc5-3bb3-98c4-2ef0a199e08c | -9.79577 | -45.94632 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d42ad771-ddbb-36fa-940a-cd7bf773c8cb | -11.47168 | -45.01379 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53d3582b-d6b7-3567-ad19-6f211c2a6fb8 | -7.78588 | -42.51921 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| dbfef98a-a41d-38c9-bbc7-2555a575316b | -11.87586 | -51.22943 | 2025-10-02 04:02:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1059e8bd-2f1d-314b-93da-2efcf97fc8d0 | -9.9208 | -43.72031 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 268082f4-2f1c-3ea6-95be-225df4285f05 | -11.27258 | -47.83418 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 48c56ff8-9533-3d16-91f4-300a996d8850 | -10.99735 | -46.59156 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| f137f71a-9cba-3404-96ad-622a0b9a637d | -8.89973 | -45.03936 | 2025-10-02 04:02:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bca9adfd-56db-3ab3-8057-fe7639cb9681 | -7.5657 | -42.40253 | 2025-10-02 04:02:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| afe468ac-7187-3f95-82b9-919ec74a0e62 | -11.4365 | -43.88933 | 2025-10-02 04:02:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fcac0e78-f894-3748-ae4a-441fbb8757c5 | -9.33949 | -45.9193 | 2025-10-02 04:02:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0dd91f6a-3b74-3183-9682-c45bf1d28f43 | -9.94808 | -43.68721 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f0262c2f-90b3-345d-97fc-3bbbe09e0395 | -7.30053 | -42.88851 | 2025-10-02 04:02:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 1cbf96da-6963-3355-b873-f6298a795b23 | -10.66615 | -48.56969 | 2025-10-02 04:02:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b69fe1dd-7002-3fd9-8c08-1c34823a34b5 | -11.1982 | -47.77058 | 2025-10-02 04:02:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c0818006-a552-3291-b29b-bc972286b9fd | -9.3995 | -47.33454 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b01ab44-dab3-3c07-a415-9e182a47d724 | -11.827 | -44.99395 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8bb4dc1e-90b8-3568-87ad-80fb14ba76de | -11.2731 | -47.80554 | 2025-10-02 04:02:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b8e4309f-5ffd-350d-8e04-a8e59cf96f8d | -10.25331 | -50.31916 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b14bbe26-0a8f-3aeb-ab8b-8975ff969541 | -12.26837 | -44.1313 | 2025-10-02 04:02:00 | NOAA-21 | TABOCAS DO BREJO VELHO | BAHIA | Brasil | 2930907 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 706e4300-526a-3563-8024-fb934985267c | -12.77746 | -44.91152 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 61724521-3e0d-3062-964b-421052042daa | -11.47899 | -45.00351 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c50cb1c9-6ca0-36c9-9c56-8ebeceeec671 | -11.62003 | -45.04054 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4aba43e4-5cee-3415-a5c0-75393c64baa6 | -11.77694 | -46.83226 | 2025-10-02 04:02:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a0cb27f3-5dad-3d41-8dc4-58d6e7be4317 | -10.22585 | -50.31759 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 24378e16-98c1-38d0-b386-fc7b1aa3374a | -12.81254 | -47.01541 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2199425e-37ef-328f-aa40-5db58053644a | -11.80695 | -44.9997 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0bf9b8c6-950f-37aa-aaaf-68fe33205ad0 | -11.47123 | -45.11473 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 57731f54-c7f3-3aca-a6a0-b8334ccb0112 | -12.7253 | -44.84444 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 88431cc7-9b4b-3a84-815d-d9d822b1529c | -11.86531 | -48.01344 | 2025-10-02 04:02:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 042a640f-2cc2-31c1-a97f-e8cfa662aea4 | -6.48615 | -44.28976 | 2025-10-02 04:02:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5d8a22e1-1f0a-3263-8f05-a9cd32085c88 | -10.23722 | -50.31615 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| eaa5c616-b701-38b3-92db-4bdc8cecce81 | -10.54995 | -43.65052 | 2025-10-02 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0d18fe48-f1f4-30d8-a6bc-3fc59ee00c1f | -7.7796 | -42.51433 | 2025-10-02 04:02:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 23.4 |
| 108c7b3d-2d4a-3ff7-9a2f-157179f9c4ce | -11.08965 | -47.82117 | 2025-10-02 04:02:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1d4c7eb1-7d4e-3776-90f2-f3d3889057ff | -10.22323 | -50.3314 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 97bf38f6-7e3b-383a-a949-474469e4bd06 | -9.90287 | -43.69639 | 2025-10-02 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 14910fb5-b98a-34e9-b3e2-91915f5b1416 | -12.89091 | -46.92675 | 2025-10-02 04:02:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2fc3f1f3-c631-3b7c-b948-61b09176cb33 | -8.82135 | -46.68017 | 2025-10-02 04:02:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 07b3fb72-bc8d-3bea-bdbb-1f398190235f | -12.88078 | -44.68123 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7827c111-20c8-3e44-b5c4-da5806086bf1 | -9.93586 | -43.73973 | 2025-10-02 04:02:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 37850a76-19be-319d-ac97-b1842a5b9fd7 | -11.70338 | -45.34808 | 2025-10-02 04:02:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3f1bd3b1-ccf4-30cb-8f35-85e53cc70239 | -10.83446 | -46.61842 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 372e845b-8b06-3cfc-b9e1-3a399a03a9ca | -10.82055 | -46.60024 | 2025-10-02 04:02:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4a7341a0-ad3b-3d97-83ef-64a7bec5e4c7 | -5.63672 | -45.96756 | 2025-10-02 04:02:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1f093357-c611-3723-abcc-7943c5e590b9 | -6.32134 | -43.03946 | 2025-10-02 04:02:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 83e3de78-f42c-3cf7-a181-0a276141b7cb | -7.03907 | -43.33577 | 2025-10-02 04:02:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 552e79c3-a63f-3293-82a7-acb829a3ba7a | -6.72444 | -44.14405 | 2025-10-02 04:02:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 27d4a376-6cf6-30dd-ad87-cdd2cd2c5f3a | -11.16812 | -47.27325 | 2025-10-02 04:02:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 63f47b30-98d2-3327-898e-d9ad036cdb41 | -10.22454 | -50.32449 | 2025-10-02 04:02:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6612d10e-9179-31a2-a43c-90873524316f | -11.4819 | -43.50337 | 2025-10-02 04:02:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b3e990b-655e-3811-9e38-e7f24b8cbb9b | -6.71961 | -44.62314 | 2025-10-02 04:02:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 64fd4d64-5ab1-3d59-bb10-4c722d03cd1b | -6.82091 | -47.98038 | 2025-10-02 04:02:00 | NOAA-21 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d77946ef-4723-3719-815b-5186a48b2174 | -9.92911 | -50.49566 | 2025-10-02 04:02:00 | NOAA-21 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 83d7c9ee-78f4-3064-9b2d-c52f0380c84c | -9.41126 | -47.58664 | 2025-10-02 04:02:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0f73103d-62b8-33a8-adfc-feda38c21a21 | -6.2645 | -43.89249 | 2025-10-02 04:02:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| eff32c9d-6b22-3ad3-9a27-b4024baf4e9e | -11.20248 | -41.53782 | 2025-10-02 04:02:00 | NOAA-21 | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| ebdedab4-6587-3f4e-9693-abc696e5c385 | -12.22663 | -43.76549 | 2025-10-02 04:02:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2450782b-331f-33f7-be15-46a56b0aa17f | -6.66596 | -42.79396 | 2025-10-02 04:02:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 50e72bd4-fa62-30f7-909f-d625aab17e01 | -10.30911 | -42.39598 | 2025-10-02 04:02:00 | NOAA-21 | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |


[Clique aqui para ver as próximas entradas](README27.md)
