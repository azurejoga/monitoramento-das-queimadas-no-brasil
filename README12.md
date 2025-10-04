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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 719eb1c5-b402-3935-907f-0680147ce182 | -6.0773 | -42.51093 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 315088af-b0c4-3c9c-8441-a53c4a11e350 | -9.12112 | -40.13538 | 2025-10-04 03:23:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d340531c-d091-3d0e-b3b5-b755ba1d7d30 | -6.69326 | -42.84131 | 2025-10-04 03:23:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2bfdf9b0-b653-3b6f-84f6-46f312cd07f5 | -7.04893 | -42.766 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 87314e4b-4fb2-310e-b767-1e619743a030 | -6.26905 | -42.45629 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 73d02687-6e65-37a7-bd3b-0840c6a38e37 | -7.74829 | -42.52763 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.0 |
| 04548ba3-b0ea-3cb8-b736-4c9948860152 | -6.2736 | -42.45539 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| 8d20f3d5-7acd-398e-a95d-3340b511ceba | -5.73994 | -42.92941 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| c0d2e8db-d0c8-3ed6-a7ab-1b1b8f573a5e | -7.75649 | -42.51855 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 14.5 |
| e30c9367-1140-3d05-b858-058a36add015 | -7.55772 | -42.39799 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 45bdf4db-58f9-31f0-a16d-2de031434ba5 | -7.79268 | -42.566 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 7a6960ff-b06e-378e-99c1-547ed199586e | -7.5463 | -42.39836 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| fdd6116f-fa59-3a27-b752-7e580ede477d | -6.07405 | -42.52025 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 31.0 |
| a9c46664-6e42-3467-88d4-442dcecdd859 | -6.28325 | -44.04508 | 2025-10-04 03:23:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3f588424-e41a-3331-8d00-a25cf14fe40c | -6.67422 | -44.20846 | 2025-10-04 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e243d171-7782-311b-bf32-3f0d18bc7fa7 | -8.05595 | -44.80561 | 2025-10-04 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4cfe3b40-1151-38c3-a458-258b040880e9 | -7.53917 | -42.4022 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 88a400cd-b23e-33b8-b560-1594d5bb3a67 | -7.53824 | -42.40721 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 5.9 |
| 2800f7e0-074b-361a-9e96-81446e6641c5 | -6.71716 | -42.16096 | 2025-10-04 03:23:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 376bcbf9-ffc0-37da-a206-1a404763b40b | -6.26634 | -42.45923 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 14.4 |
| a07b584e-2276-3c03-9111-9a50279e05b3 | -6.67029 | -42.82108 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| ea915228-3ff3-3fda-a8aa-5881833e9026 | -7.15689 | -44.21403 | 2025-10-04 03:23:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 750a1e89-e670-3178-9d99-9c157b51adc1 | -7.5534 | -42.39466 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 4fb740db-90b7-340f-87a5-eafd7835ca9c | -9.90708 | -43.79935 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84fc09dc-e5b6-3062-8923-af0b95cbdf9e | -9.94429 | -43.74651 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 92e78ac3-6030-3d08-b55b-f4472ef7b7b7 | -5.73957 | -42.92136 | 2025-10-04 03:23:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 7.0 |
| de1e31ff-47c3-38fc-812f-beeb05ba8f7c | -7.54539 | -42.4033 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 98267d23-8691-3200-a49b-73a1b0e2264c | -6.66146 | -42.83258 | 2025-10-04 03:23:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 23.8 |
| c3362fcf-f178-3042-97a7-5ac8f461e69e | -9.10572 | -44.39759 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 2fbf003a-04f8-3372-a1ba-91fa72642f1d | -7.75074 | -42.54853 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 6f21a2c0-e92a-392b-b101-fcd3ad7cb8a1 | -7.7583 | -42.51944 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 092f0887-4ab9-34b5-be85-44ba23962f94 | -6.66126 | -42.83141 | 2025-10-04 03:23:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 15.0 |
| 09e96ea9-fdcc-31cf-a2f2-b8e08fa7f7f2 | -6.98974 | -42.79914 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6d7486d4-d514-31d8-8759-d8670f8e92ed | -6.06994 | -42.51498 | 2025-10-04 03:23:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 47.5 |
| 272bd88b-5be0-3864-b886-94ce9988f1d3 | -6.65262 | -42.80839 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 5c4c700a-6e15-3a93-b131-21cb1e0a2260 | -9.94967 | -43.7533 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 13ec5918-f773-356a-90c7-5e4d1b7fec92 | -7.72127 | -42.57978 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6ce01548-953a-3db9-81c7-cc0d0900e4da | -6.31187 | -44.27732 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| b3a624d8-6b7f-342e-a82c-0ba9968e4fc2 | -7.04813 | -37.96787 | 2025-10-04 03:23:00 | NOAA-21 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 1d14f2a3-6cdb-3e0b-9613-f5e6078c95d4 | -7.34519 | -39.17233 | 2025-10-04 03:23:00 | NOAA-21 | MISSÃO VELHA | CEARÁ | Brasil | 2308401 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 2c8ec2d2-77ca-3809-8021-e4362aa9bf85 | -7.75205 | -42.51832 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.7 |
| f2d098e9-b529-33aa-bbad-7159c51379cd | -5.73843 | -42.92743 | 2025-10-04 03:23:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 99128d7b-4ddb-304b-aa3e-fff4d274f182 | -8.05726 | -44.79884 | 2025-10-04 03:23:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e8d45b0e-0a7a-3f43-909b-32cd2faf0585 | -5.8348 | -42.88425 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 26246229-7213-39c7-9422-ef4960edf72f | -6.87707 | -44.50085 | 2025-10-04 03:23:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 21.4 |
| c0a1e2ad-29ca-3991-8876-468b0c479bca | -6.6755 | -44.20161 | 2025-10-04 03:23:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 415a6f21-a323-3e4b-80ef-48e81cad78b4 | -7.79173 | -42.57105 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 5c617a13-01f2-3380-b464-e62c6d1f5fa1 | -7.77877 | -42.60535 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 95cf91a2-262f-335e-a838-50391b0af83a | -5.73441 | -42.92229 | 2025-10-04 03:23:00 | NOAA-21 | SÃO PEDRO DO PIAUÍ | PIAUÍ | Brasil | 2210508 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 2e53c7a3-79b0-3de5-a56c-7a01e31dad09 | -7.70246 | -42.57645 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| bbff54c3-6aa6-36ff-9507-9afffa4df710 | -11.42888 | -43.49018 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 46906680-3954-3c04-a687-3995fc659a23 | -11.4351 | -43.49138 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e3158caa-95ca-3796-b537-61bc33886498 | -5.48217 | -44.11112 | 2025-10-04 03:23:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 552db3be-9760-358c-96ea-5d15c10c4e4d | -7.71777 | -42.56384 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 831bc4bd-f1f5-322b-9671-6340bf135019 | -6.26991 | -42.45164 | 2025-10-04 03:23:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 22.3 |
| 5593a13f-6310-3cbe-ac2a-433d9e5e5d93 | -7.32719 | -41.44195 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e1ddae0d-b1e3-337e-a0ac-d4c832a50e3e | -6.34335 | -43.4619 | 2025-10-04 03:23:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 59815719-b349-31be-a7c3-feae56758f65 | -6.66352 | -42.82152 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 07ae52c5-247c-3241-8432-ae216397a9f8 | -6.98261 | -42.79585 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6f42f5c3-595b-3573-9116-71639cb115ec | -8.17597 | -44.14658 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 70458fba-014a-310f-b012-bfa62338735f | -7.78981 | -42.58123 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 2f2f1789-a771-3459-ab97-8ee28415737b | -7.0123 | -42.31026 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 6cb2869e-bc8c-3c5d-8004-cb0881f07fd5 | -11.41645 | -43.4877 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8e0315a9-e324-3efb-a216-8f08cd18eb15 | -7.80459 | -42.53715 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 41657ef9-7e51-35d7-8d49-686a4e177a1c | -9.11716 | -44.38253 | 2025-10-04 03:23:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2bcf852a-a3ed-369e-b476-f4eb3dc16090 | -9.90007 | -43.7324 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 28b1f9f9-e2d0-3be3-a943-1d18dee8f0ed | -6.65326 | -42.80168 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 47ca7bf9-bcc1-3cb8-aa70-b3e3721a2d10 | -7.74389 | -42.52757 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 58b390bf-6818-3483-bc08-37ff1385ce47 | -6.65771 | -42.81405 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 3e9a0c41-b815-39a6-8b5f-a4c7ee53f785 | -7.33378 | -41.43898 | 2025-10-04 03:23:00 | NOAA-21 | ITAINÓPOLIS | PIAUÍ | Brasil | 2205003 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 04e10020-d4c0-39b0-8849-96bab1cc2688 | -9.38643 | -40.45823 | 2025-10-04 03:23:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 949fc984-d0a7-369e-aa34-36e9c067fa5b | -7.78495 | -44.13765 | 2025-10-04 03:23:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 91c2ea15-d54e-382a-a5e3-c878804f20b3 | -8.62826 | -43.98895 | 2025-10-04 03:23:00 | NOAA-21 | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 8e328a76-3425-37ac-9881-1324b1a94420 | -5.48347 | -44.10408 | 2025-10-04 03:23:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 11.3 |
| befe0778-cec7-3e04-a52b-675c158dc717 | -11.15128 | -43.38909 | 2025-10-04 03:23:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 099da5e4-899a-3682-926d-cceb40c20ef2 | -7.57285 | -42.39361 | 2025-10-04 03:23:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 1d172ee4-b817-34ec-b15a-07fabb5437b3 | -9.90816 | -43.79376 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 93d75503-8330-356b-b159-63ffca17e7b1 | -7.78166 | -42.59007 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 02cf9d9c-4f9c-3746-904a-47591395f562 | -6.17678 | -44.28988 | 2025-10-04 03:23:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 1518cd7c-029d-35fe-b45b-9a9423234df4 | -6.71184 | -42.81293 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| faa434ce-861a-38f8-9021-8dd982c7f9c3 | -6.65228 | -42.80715 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 393c9fb2-d59f-3361-b340-299339e6d300 | -5.98048 | -43.49023 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 11.2 |
| 3d818e2f-363a-314f-a554-6a079ace51ef | -5.93561 | -42.88126 | 2025-10-04 03:23:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 5.0 |
| 9e5d1d5e-f45f-36d5-8acf-8618de1820b5 | -9.90713 | -43.79789 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4694f81b-b43b-3caa-8418-b129d809d7fe | -9.90657 | -43.7335 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 66d77d82-3ba5-328d-b7d3-ac9ced42b9b2 | -7.78604 | -42.49881 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 4d6d0c68-5da6-3feb-95b1-f37d38be004a | -7.77145 | -42.60974 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 7b6642d9-6868-389a-9a1b-2a77182b57e2 | -6.70297 | -42.78869 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9a168b13-fb2b-342a-9181-599aacfcf16a | -9.90945 | -43.71754 | 2025-10-04 03:23:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8393d1c4-5e8b-347d-9689-ed1defc37ebb | -6.09472 | -43.48729 | 2025-10-04 03:23:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bbe2a4a1-e521-3baf-ace8-45eb32e06329 | -7.04796 | -42.77123 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| a9308478-f62a-3ecd-9a06-1b0a0b7da7e7 | -7.8055 | -42.53228 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 01811a8c-cc65-3bc1-98b0-bd07343c22cc | -6.6462 | -42.80703 | 2025-10-04 03:23:00 | NOAA-21 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| bf7c3d42-2210-326b-96bd-b22368e85958 | -7.77576 | -42.60044 | 2025-10-04 03:23:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 4c1a973c-d200-3746-92b1-dca7f7a0369e | -7.04501 | -42.78728 | 2025-10-04 03:23:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| 92f46f85-44fc-36df-b511-70b785962cd9 | -7.69523 | -42.58046 | 2025-10-04 03:23:00 | NOAA-21 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 185686eb-8ae7-31e7-8b19-81be47a0bf7d | -6.64662 | -41.9585 | 2025-10-04 03:23:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| a63ef530-d50c-38c4-83e1-2deaf3678050 | -7.74488 | -42.52227 | 2025-10-04 03:23:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 10a43cd6-c1b4-3b8a-b773-db9a89f5457f | -6.22799 | -42.92899 | 2025-10-04 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| ed8d42de-33b0-35d4-9b4a-40c7ead80557 | -6.36344 | -42.8851 | 2025-10-04 03:23:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README13.md)
