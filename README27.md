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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b45bffb1-b96f-3b56-bbd6-fa5bd1ad623b | -8.30019 | -43.4043 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 1734b819-6caf-3d47-8020-6bdc34899994 | -4.40926 | -43.3955 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ccf18afb-8681-3a8b-b14d-4664f2aa630b | -7.95003 | -44.12444 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a9d5f73a-7d22-3aba-9009-09d102ee58f2 | -8.3971 | -46.23267 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 71b05626-409d-3222-9c2c-b354bfe3bbf7 | -3.98155 | -42.49128 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4027ce42-15d6-39de-8cc8-663b0e6dd16e | -8.30109 | -43.42413 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f2840dfb-04ac-39a5-b505-c4795cae077c | -7.97768 | -44.16452 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| be42c145-e7ff-366b-84f5-bece786ec777 | -5.28941 | -43.55401 | 2025-10-17 03:28:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 290ae0eb-b531-3d4a-82e8-ff378b6426d7 | -4.42108 | -43.40348 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| b59a62f9-0194-3d9a-a1fd-8982f9f42fad | -8.19484 | -43.31719 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.9 |
| 9854ee08-4ed5-354b-b72c-a51d5691362a | -6.7609 | -42.36848 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| c9fc193d-0a22-3961-87c6-a9ce2fc7d640 | -8.30192 | -43.41963 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| aa449919-44a6-3dfc-b4d7-5d81ee5c70f8 | -6.13779 | -41.73392 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 7f8c9848-d091-305f-a519-d7dd31edfbb1 | -8.3926 | -46.23688 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 50450dcc-4b1d-3a48-885e-ba6025a9fd1f | -8.3869 | -46.32307 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b849dbaf-9364-3ecb-bf22-e4bc5925affd | -8.73646 | -40.59708 | 2025-10-17 03:28:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| cadb1968-f033-3566-b48f-c412ff0efb17 | -7.19549 | -45.49247 | 2025-10-17 03:28:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 97ae1a5d-99b7-3f99-8395-edb0b9f42487 | -6.32159 | -44.32312 | 2025-10-17 03:28:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8e5b295f-c7e9-3575-965c-da1a626bd697 | -8.3019 | -43.42788 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 6fc70c5d-d868-3176-b61e-31a58d028de7 | -6.69284 | -40.86467 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60854027-2c6e-3e09-9997-c42f02521cc2 | -7.5626 | -41.01163 | 2025-10-17 03:28:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8e528457-c4b9-3f42-b613-b9be59f41534 | -7.46885 | -41.521 | 2025-10-17 03:28:00 | NOAA-20 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 91bf7139-d1d2-36ed-937f-dcfc2f3d3e28 | -7.27226 | -42.93909 | 2025-10-17 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 53cfc7ba-8860-33ce-866a-4a8779334042 | -6.01788 | -41.93939 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1e115a4d-4bf8-34f7-a3aa-67bba69f163d | -6.29056 | -44.01469 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| eaf63e4c-0768-37aa-9478-e5054b8c4975 | -6.7496 | -42.36475 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| c38c00cf-4e0d-3297-8be5-aa798bfd5de0 | -6.1277 | -41.75852 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| ba24ac14-9db0-3463-8811-b46a9edf81d3 | -5.29823 | -41.08446 | 2025-10-17 03:28:00 | NOAA-20 | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d727490c-396b-38a6-877b-fd60820b9836 | -7.73965 | -42.50795 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 799a9f84-5b33-3f9a-bb76-e6c98ee72f9d | -5.45991 | -44.64793 | 2025-10-17 03:28:00 | NOAA-20 | SANTA FILOMENA DO MARANHÃO | MARANHÃO | Brasil | 2109759 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d328e2b-ac98-3bdf-b2a6-0f28c9731ad8 | -6.76369 | -42.8499 | 2025-10-17 03:28:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| fd068abb-355f-3dba-9f7b-6c39d67f6cb1 | -4.47714 | -42.93491 | 2025-10-17 03:28:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e25b7a78-7165-37ca-a4a9-9015a017be44 | -7.4834 | -38.99859 | 2025-10-17 03:28:00 | NOAA-20 | BREJO SANTO | CEARÁ | Brasil | 2302503 | 23 | 33 | nan | nan | nan | Caatinga | 2.5 |
| c63f7c47-3ab1-306a-b21d-6a6c337a6f1b | -7.46428 | -42.1434 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| ad33e476-b6f9-3ad6-9d27-fe01369ff67e | -7.4835 | -42.76192 | 2025-10-17 03:28:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e5fdce8-47be-379c-a569-605692bf2d95 | -8.45544 | -46.25458 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 26cffe7c-6a0b-3457-8723-58707f620f83 | -6.15046 | -40.91293 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| c60efb1a-e914-3929-b3e3-c02f6787b375 | -6.58493 | -43.93985 | 2025-10-17 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5a790847-feb7-30c6-905f-12b37d385d2b | -7.94526 | -44.15005 | 2025-10-17 03:28:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 97c5f084-6a9a-36a9-909e-d1c2103862a7 | -7.46711 | -42.14394 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9d98aed7-0907-34a5-b7b3-ba741fc39bb3 | -7.17046 | -42.51638 | 2025-10-17 03:28:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ef4c1744-bdde-374f-be18-367accd84a8e | -7.20005 | -45.4997 | 2025-10-17 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 68c7820e-961c-38d8-935d-5eff2efef6a9 | -7.3485 | -43.86404 | 2025-10-17 03:28:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5e58a51d-1e99-3fd5-ae9a-5e9ea144b8a8 | -8.39226 | -46.25759 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 2a848180-ea04-34b1-9897-4d1d9cb766df | -3.97943 | -42.50186 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| bada3060-ab2f-3377-81a4-9c655fb3ca4f | -4.37825 | -43.38398 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 15a26c51-cb93-33c2-9407-9f227e29870c | -6.28927 | -44.02009 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a15eac48-daf7-3541-af16-6cce215abdd0 | -6.75321 | -42.37798 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 6bb34cd9-92c8-35ac-9155-7fac06dd08be | -4.3946 | -43.40368 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8dd19901-e73e-339e-b6ea-141c13569641 | -8.0833 | -45.42612 | 2025-10-17 03:28:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 13906e1e-5470-378c-ae8e-f606ff4c3d97 | -5.89236 | -43.19648 | 2025-10-17 03:28:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 80ed4847-a01b-37aa-aaa6-f1c60282f968 | -5.88119 | -43.91056 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8d4ac40f-dfe9-34df-beaf-6d7161c3c5b5 | -8.28892 | -43.38886 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2cc6ece4-f5b0-3f20-86fb-fa7e1fe2572f | -6.75537 | -42.36592 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| fe44c173-4457-3999-a8ce-020a119881eb | -6.13633 | -41.77561 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3411683d-3538-3aac-8644-f0be3c59897e | -5.84453 | -42.34651 | 2025-10-17 03:28:00 | NOAA-20 | PASSAGEM FRANCA DO PIAUÍ | PIAUÍ | Brasil | 2207751 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| f0c995bc-2533-31c2-a3d0-d00a76e2c9df | -8.39573 | -46.23973 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 7b7c9c42-9768-34cc-9623-57f4056de158 | -6.3559 | -41.48944 | 2025-10-17 03:28:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| e4c1781d-9003-3bd7-98b0-7d7d73fe3e75 | -8.44717 | -46.24043 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 8914d058-044d-3f42-b032-0122149d9666 | -8.24585 | -44.02121 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1c42afec-0a88-3296-bb96-18df24fc1f65 | -8.25019 | -44.03256 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8296c4e0-cacb-389e-9fb6-114867fb2ea1 | -8.39404 | -46.22977 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| b6c8f29d-d50e-35f1-853b-a8c1575c660d | -6.42055 | -42.57211 | 2025-10-17 03:28:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5135f37f-7294-3cd8-af16-c04a464928e7 | -6.34885 | -45.48843 | 2025-10-17 03:28:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3788c604-1eb9-3d17-a4c5-599254875c95 | -5.8535 | -43.87891 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 8cd365a2-4680-3f38-9139-4bf8a9a5ffcd | -6.60491 | -42.06946 | 2025-10-17 03:28:00 | NOAA-20 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 28b2f4dc-5f20-3b91-a5e4-0a9a5fe1ce46 | -7.18378 | -41.68116 | 2025-10-17 03:28:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f0ef3d1-582b-38de-8792-0f173ec75780 | -5.86742 | -41.236 | 2025-10-17 03:28:00 | NOAA-20 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 7863b0b7-7f1e-3b3a-9c31-9a50110789d7 | -6.01926 | -41.93143 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 30157bb4-5f52-3c97-9c05-fe96ce48789d | -5.90312 | -44.74985 | 2025-10-17 03:28:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 727646dc-ec03-39c7-957b-8d25915a3883 | -6.83003 | -42.41641 | 2025-10-17 03:28:00 | NOAA-20 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 6150bd72-91ac-3ae1-bb90-3718cefb89c9 | -7.0282 | -41.81883 | 2025-10-17 03:28:00 | NOAA-20 | SÃO JOÃO DA VARJOTA | PIAUÍ | Brasil | 2209955 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 094cd075-f289-35ba-9347-1c2355f7ceda | -8.20885 | -43.97754 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c672dffb-7c53-3189-b0fc-7d0784a5b9a4 | -8.55478 | -44.58107 | 2025-10-17 03:28:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ae6a57db-6764-3b50-b6c7-298ef09b27f8 | -4.40738 | -43.40621 | 2025-10-17 03:28:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.1 |
| f87636ec-8a33-3a6b-b551-90be1f2a072c | -6.13647 | -41.7415 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5fb454ba-a647-360c-880b-9c89b7ce8f5a | -6.5859 | -43.93454 | 2025-10-17 03:28:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1ff40c95-0d72-3837-b04b-de1d1095d51f | -7.46648 | -42.16377 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 545fa9de-0c4c-32c3-843b-ddb6229caa40 | -8.33344 | -46.23994 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| c81915dd-5c74-31c8-a30b-791b165e17e5 | -4.36392 | -44.77706 | 2025-10-17 03:28:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 90e32b74-5e81-3e50-ad5d-e8304371a0ba | -5.49544 | -42.16405 | 2025-10-17 03:28:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1cdc8b27-c04d-32af-a1c8-b51ec2d91866 | -5.5076 | -43.87073 | 2025-10-17 03:28:00 | NOAA-20 | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 2e304a55-f142-361e-9511-3e655058b8ce | -7.29799 | -41.95523 | 2025-10-17 03:28:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 60a6b5be-327a-3da7-a997-3a01192bc1cc | -8.25113 | -44.02757 | 2025-10-17 03:28:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0d216889-a2b1-3540-b869-db58151ac5b5 | -6.652 | -35.15274 | 2025-10-17 03:28:00 | NOAA-20 | JACARAÚ | PARAÍBA | Brasil | 2507309 | 25 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9be02d72-76b8-3745-b0ad-7cf34456c818 | -6.01389 | -41.9386 | 2025-10-17 03:28:00 | NOAA-20 | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| cde56fec-f39c-36e0-8aa4-b543979bba1d | -8.30535 | -43.44246 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 858d1bf6-b0ad-342a-a05b-8c6ba580bbfd | -7.45656 | -42.154 | 2025-10-17 03:28:00 | NOAA-20 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 2a5b0659-132c-3c3a-98c3-78d77e6e1d3a | -3.97332 | -42.5008 | 2025-10-17 03:28:00 | NOAA-20 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6bc22ba2-81c8-3c6f-b5a2-d240909947b1 | -6.20585 | -41.76049 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 5a7a469f-7db4-3217-b77b-c6f88a77d7b4 | -6.28956 | -44.02008 | 2025-10-17 03:28:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8c55e4ff-d158-3cad-9f1d-84198ae877f9 | -6.04416 | -39.68347 | 2025-10-17 03:28:00 | NOAA-20 | ACOPIARA | CEARÁ | Brasil | 2300309 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 60a45c2c-ffbc-338b-9d43-8649b9fd7fd0 | -6.13591 | -41.73032 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 6553b29f-755a-3733-8e53-eefd76a70c0c | -8.40453 | -46.28776 | 2025-10-17 03:28:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| eaf20f08-9afd-30a2-98d2-5937fc1d81c5 | -8.45059 | -41.26889 | 2025-10-17 03:28:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dba624e9-c79e-3500-8585-45237477b6de | -6.13128 | -41.77123 | 2025-10-17 03:28:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1d5da44f-75e0-3099-aeee-1f94605ecaf8 | -6.69165 | -40.87144 | 2025-10-17 03:28:00 | NOAA-20 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| fdfab77a-e390-3110-a6e2-7e446eacfd78 | -5.88103 | -43.91321 | 2025-10-17 03:28:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9e0c00b3-b65b-365a-af5c-c299f15c11fc | -8.30355 | -43.41082 | 2025-10-17 03:28:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c5b39ac1-4826-34e7-8fb7-abcbd4cba858 | -7.20115 | -45.5007 | 2025-10-17 03:28:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README28.md)
