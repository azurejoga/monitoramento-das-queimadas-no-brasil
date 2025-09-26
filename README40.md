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

## Dados Diários - Página 40

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b8ebd0e-52e3-3541-b245-491c5fcc37e3 | -6.25371 | -46.12157 | 2025-09-26 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 19d962f9-ae79-396e-bb9a-6f1b8731b266 | -2.92373 | -48.31052 | 2025-09-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8e571789-77d7-3b67-8664-2309407965a6 | -4.79293 | -42.74998 | 2025-09-26 05:01:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd7dca01-f6d4-312b-98e1-527c485b5225 | -5.73105 | -44.97315 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 6b908bda-90fc-3255-9aa1-65ecb1d6594f | -5.74989 | -44.9673 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 1f163a4f-8b56-32c3-ac5c-6c93d13f18e7 | -5.42868 | -45.14191 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a71dd247-200e-3638-8290-e64016e1b47c | -4.79634 | -42.75148 | 2025-09-26 05:01:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8df2f5ee-a5cd-3209-b0a2-805e5baa07de | -6.87828 | -44.50867 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| e938aff1-914b-3b41-aa3c-e08119f5edff | -2.95882 | -48.58947 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78ff1b92-106c-3e3a-932d-72d7aa5ae8e7 | -4.74797 | -43.61382 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 86d5c326-30af-30f8-819b-02fb782016a2 | -5.6931 | -44.44409 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cfa803b9-abcd-3c75-862b-0784183eb440 | -3.81468 | -41.5621 | 2025-09-26 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 59e87b6b-354e-3686-b3db-b1ac9605cd30 | -3.66576 | -52.15035 | 2025-09-26 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 96112a84-4880-3924-982f-fa97e0cd1a8b | -6.85597 | -43.18003 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0bd33e6f-c2df-39d9-b017-dc81bd70a2f8 | -3.05327 | -48.70712 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 730e0ea9-7abb-36d2-8502-be6d3027bf56 | -3.44732 | -44.12473 | 2025-09-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 83cadbe9-a367-3b74-b934-3d68e2e74c57 | -2.96323 | -48.59014 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ede51d6d-f1df-3397-b4c4-5cea974fa52c | 1.0061 | -59.5085 | 2025-09-26 05:01:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 02f4ff4b-bcb2-35fe-9e8e-8016e2645b79 | -2.78993 | -49.59704 | 2025-09-26 05:01:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26259e1a-635d-363e-bd7a-ea8af0ce9b94 | -5.64625 | -43.93158 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 771324b8-5ae9-3287-900e-10df5d2661a1 | -6.95901 | -43.24817 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 70ea3a4a-7ad8-380e-a2f1-afc922508256 | -5.80284 | -42.80144 | 2025-09-26 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b1b0799e-905c-3288-834a-7888bb9f87ca | -1.08897 | -54.11245 | 2025-09-26 05:01:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 93d92f22-a020-3170-b249-934bd28157b3 | -2.92307 | -48.31497 | 2025-09-26 05:01:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd611ea6-1d53-340f-8fda-1a20c2316feb | -4.74367 | -43.27246 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2f714c00-c0d0-3154-bbdc-3280a9eab660 | -5.73518 | -44.98633 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| 73f1ade1-8600-3e8b-9d81-9b79b8bcf9b1 | -3.78422 | -48.63187 | 2025-09-26 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 75c1667f-2840-364b-8dbe-807ffdf79773 | -4.75116 | -43.26957 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7d626f23-12b1-3f62-9b65-d3957ef5cb64 | -4.17184 | -44.27059 | 2025-09-26 05:01:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ae8f857-82ac-3ccb-8d1f-049b532453c8 | -6.26165 | -42.48252 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b68cc1c4-560f-3540-81d9-f8c3b4b122cb | -3.64744 | -48.3235 | 2025-09-26 05:01:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a28a660e-13a5-3783-be35-0d114d181700 | -5.75142 | -44.91452 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af496650-e293-3e31-89b8-f5a93508c6c1 | -3.81372 | -41.5689 | 2025-09-26 05:01:00 | NOAA-20 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| c8288bc8-1161-30d6-b534-899142202813 | -5.18074 | -48.0326 | 2025-09-26 05:01:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 65d38d08-1bd2-34cd-a924-a5b28cb829ea | -6.25423 | -46.11776 | 2025-09-26 05:01:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de9ff5ba-9985-3ffb-830e-d939575a75ba | -2.45114 | -49.01895 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ddee0dcb-2ee4-3987-a273-df29f8b7ee19 | -2.19512 | -54.46544 | 2025-09-26 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55cb945d-ea7c-30f0-b2ec-81ca1242e2fa | -6.25323 | -42.49289 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| f07c00eb-a610-3e6e-986b-258d48a0b526 | -7.10997 | -43.7448 | 2025-09-26 05:01:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 83089bc0-47ad-30fb-b3a3-0321649df758 | -4.48519 | -47.67755 | 2025-09-26 05:01:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e7580a6f-c7e1-30f0-a8b4-005455323001 | -5.46078 | -43.0755 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d710ae27-06a4-317a-b8fd-94e4bbb8bb7d | -3.33442 | -50.25048 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 18016b4b-dd17-36f9-8aa7-a2f8f3fb845a | -5.7496 | -44.91253 | 2025-09-26 05:01:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 11256b5a-83e9-3de7-ab8c-4e39acb5029f | -4.74168 | -43.61268 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 5bb6f2c0-8c49-3b1d-b67d-a59b05ffcfa1 | -5.73225 | -44.96473 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 9010685e-05f8-3794-b2d7-0bf5171fa7b1 | -4.79648 | -43.04124 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f1b55e77-5f78-3eba-a45f-b940a46c8eb6 | -5.74677 | -44.97783 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 42.4 |
| 068f8770-dfe9-3109-9865-0b24640260d1 | -5.7487 | -44.97563 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| c49316d1-d7ab-3d5a-afcc-53a6d787ada6 | -5.74968 | -44.92667 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 0790da77-78a7-3b15-8c1c-772efe50fb5c | -4.78762 | -42.81479 | 2025-09-26 05:01:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f11b846a-8fd2-3745-a40c-fcef3da79e46 | -4.38962 | -41.92444 | 2025-09-26 05:01:00 | NOAA-20 | PIRIPIRI | PIAUÍ | Brasil | 2208403 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| a326f746-6990-3834-a1ba-04fd4dc03616 | -6.93501 | -44.64484 | 2025-09-26 05:01:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c7a83096-1ca7-3cd2-a003-d84569b6a557 | -5.97338 | -44.13188 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 380ddeea-5ebd-3f2a-bbb4-7d3c6792a75c | -5.73056 | -47.98541 | 2025-09-26 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d7e89e4b-8d43-315f-82e6-2f08ab9189e1 | -2.45175 | -49.015 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8e00d7f-8456-3029-819c-e686ec1e0d70 | -5.73811 | -44.9657 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 39.6 |
| bbbaddc3-1e47-3950-97f1-51b250d88100 | -6.25409 | -42.48649 | 2025-09-26 05:01:00 | NOAA-20 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f5e360d-7a49-32f7-a598-cba78c0988ac | -5.73132 | -47.98024 | 2025-09-26 05:01:00 | NOAA-20 | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 363a20f3-d9ac-3538-8eb0-513f21bef365 | 0.69172 | -51.46235 | 2025-09-26 05:01:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d67594da-9b13-3962-a830-e86aca7667ec | -3.41403 | -52.82623 | 2025-09-26 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 356f2f7e-bfa4-37f4-a7f3-820f2997208f | -2.19182 | -54.46492 | 2025-09-26 05:01:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| adb64664-f41e-38c3-bcb0-937e95364589 | -3.62754 | -43.87327 | 2025-09-26 05:01:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c46cee75-efd4-3c52-a8f3-af4649195b64 | -5.64555 | -43.93661 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 44e95f71-8dd6-3dfc-9d7c-6628cae1533a | -5.46784 | -43.06109 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.7 |
| e127117f-7fe2-39a0-afc1-343b0bebc537 | -6.71125 | -42.74368 | 2025-09-26 05:01:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d9a07a61-9055-3719-98e0-882798ebc826 | -5.97429 | -44.13609 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f082c4af-3990-3c25-97dd-1967eb1118f6 | -7.27763 | -42.98351 | 2025-09-26 05:01:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 81fb2877-2c9d-3815-a730-8e7c8c05a589 | -3.33738 | -50.20478 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3f0f3377-c8e6-3175-8e0d-549bbf2b971a | -3.68357 | -52.387 | 2025-09-26 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1054a128-faac-354d-b1b2-1b388eba9914 | -6.54286 | -43.93114 | 2025-09-26 05:01:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a295a207-2044-3f8d-883f-c0a482846fbc | -5.74524 | -44.95782 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 309ff1c5-c493-3752-9ded-57b64eb628c2 | -5.97277 | -44.1364 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61c42ef0-cd72-3be9-829c-fe25746acf0d | -4.74471 | -43.26857 | 2025-09-26 05:01:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e31d67fd-d4d5-3315-95e6-f68d76633a1f | -5.74281 | -44.97484 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| ccdcc62d-f631-32b5-9c00-7fda47ac6d67 | -5.53455 | -43.8779 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| dd5b5eb5-bdba-37fd-b98e-ba02890fc832 | -5.74812 | -44.97968 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 32.3 |
| 8b1d4a08-42e4-3832-bae6-d93c7ad50ac2 | -5.74928 | -44.97156 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 39aa81f6-abf6-3758-bf74-9211b57e065f | -3.79908 | -47.58688 | 2025-09-26 05:01:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3e5bf061-d65d-3681-b095-8b8b66dd42b7 | -2.91577 | -48.63522 | 2025-09-26 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ea8a45b4-8b3e-37f2-853b-4c7c12dca1c1 | -2.71236 | -54.95535 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5a092d13-315d-31cc-88a5-dff7530b8ea0 | -5.74258 | -44.9645 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| e56a8852-d346-35a2-97a6-7bc1ddbbeb78 | -3.33394 | -50.20065 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b82b0b74-2072-3588-86df-8d9c6fb0072c | -3.8422 | -50.9709 | 2025-09-26 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 99b1818c-c76a-3251-ac87-e7b6a4d9650b | -5.2143 | -51.99913 | 2025-09-26 05:01:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fe93a95f-0e50-3360-8bf6-5aba9e71f240 | -5.62731 | -43.92979 | 2025-09-26 05:01:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| b8da26a4-52c3-3592-9994-4bbcd44e4d29 | -5.46628 | -43.07281 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 8b1a464e-2fd2-31b2-ab17-5887cbd52a13 | -5.4624 | -43.06399 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3a610639-5c8e-39d8-ac2f-9212c4620016 | -5.97492 | -44.13159 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f599b875-1d4d-37cc-82ba-c06c05b5e42d | -5.96808 | -44.13513 | 2025-09-26 05:01:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 680ef1f5-085e-334e-8eb7-650f6a182bd8 | -5.74847 | -44.96531 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 32de5044-d9c9-303b-8c77-1687bacc7eb7 | -5.74622 | -44.98188 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 14c8c8c7-9a0d-3a2b-b8ff-2d4559d1f6f7 | -5.74317 | -44.96016 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5fa83c4c-7f65-3d20-a108-e386efc6c48a | -5.46818 | -43.07076 | 2025-09-26 05:01:00 | NOAA-20 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 89f7fdbb-6152-33be-9001-e37966cc439e | -2.69692 | -54.9459 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ea0622e-17ad-3cfc-924b-b4fe749580d7 | -5.79616 | -42.80012 | 2025-09-26 05:01:00 | NOAA-20 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 8ca5816d-b059-39cf-ba63-ce9747561066 | -3.44455 | -44.1276 | 2025-09-26 05:01:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4e46943d-f09e-3537-bee7-83b8d96f5b0e | -5.74032 | -44.9812 | 2025-09-26 05:01:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.0 |
| a129a741-1674-372d-b693-f336d7ac6b64 | -2.44689 | -49.0183 | 2025-09-26 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c7ba10de-a89e-3799-b2a3-4d3297b04339 | -2.70906 | -54.95483 | 2025-09-26 05:01:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 34e009dc-8705-3cbf-8892-696fd6b5afe8 | -2.38029 | -47.71455 | 2025-09-26 05:01:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README41.md)
