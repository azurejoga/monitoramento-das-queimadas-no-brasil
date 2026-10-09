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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d837bf2-eb23-3b8c-8119-e47226a68b0c | -3.30437 | -53.71148 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b2655d9f-b103-39e1-bd57-5933267885d8 | -2.55182 | -57.99328 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 813d00c2-128a-323d-bcd6-f4af47849acc | -8.07766 | -55.29228 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ac7d483b-ca08-3bda-b24e-d06834bd892d | -3.10114 | -54.27654 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1ec23637-61fa-3071-86a9-834ce53abe13 | -3.39867 | -54.08558 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e90edd83-e064-3a9c-bf9d-ee7eff9b6bd9 | -6.09612 | -55.69954 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0fd3d04d-99db-3406-9c45-9959e300d200 | -5.10022 | -46.21627 | 2026-10-09 05:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 84ad424a-202a-358d-a8f1-325c2e35d544 | -7.90487 | -54.72128 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 44252671-5249-336e-b7df-6b1b67c96339 | -3.56484 | -54.6833 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6a8c0986-31d6-350a-8376-45ef97b31dcd | -2.9767 | -54.04033 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 68d64aba-e641-3efe-8761-087c2940faa9 | -6.49236 | -55.96371 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4b206341-08a7-33e0-9701-8032f78d2137 | -5.71091 | -53.45473 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1c828c62-935e-3fac-9dce-e23499a6cbb5 | -2.88791 | -54.09723 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| eae69116-8163-369b-83c8-3ca2b588a69c | -10.3086 | -46.59718 | 2026-10-09 05:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 400b9b97-20a0-33c7-9399-13f5c1218382 | -6.14217 | -52.90061 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bacff2c9-d9c2-36ac-8a71-50c9256efc9e | -11.99628 | -43.48066 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c26d964a-465e-3d7b-9a8b-bfed17721c9c | -3.48944 | -54.73056 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a7a463b9-58d4-3ad4-b168-fdadec490b15 | -3.52667 | -59.57085 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 94e55249-1691-3be1-abba-dc691dfff2cc | -3.83085 | -59.41189 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb69bd7e-02a8-3167-83f3-c850746e9a37 | -8.907 | -45.20884 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 27e6c56c-c882-3396-a8a3-63e80d74502a | -3.30443 | -54.69515 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a67790c6-5a69-327e-a394-ddcbfa1c93c8 | -3.30708 | -54.04737 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7f322e81-d08f-31c0-b3a5-48389991dbdb | -3.5258 | -59.57619 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 99ff5407-ba12-3865-9e6f-de6034f480b1 | -3.54726 | -54.69025 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 7b6a0d6c-33e9-34d2-87b4-ad58604a583e | -5.99689 | -40.93779 | 2026-10-09 05:04:00 | NPP-375D | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 93fec60c-e829-3e1e-bfe5-f33311d66be6 | -3.53954 | -59.40014 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| e7945457-6c40-31f8-aae3-cf2817d597ee | -11.0031 | -45.4154 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7dc2e2de-ac2d-3d67-8ee9-e68f13f03a16 | -3.02445 | -54.05883 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa2d0938-6a85-3499-8424-c066aa76b259 | -8.498 | -54.62285 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4f3118c7-c35c-3638-91cc-7e8b9428d6af | -3.66917 | -60.60836 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 73e36eb6-2c8c-32f9-8db1-3bde0a3eb631 | -2.52297 | -56.26931 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 077bad58-63a4-3b8e-97b3-3fd0de513d49 | -5.68961 | -53.45168 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04c5c727-792b-391d-b192-d33bee6e79f9 | -5.69966 | -53.47514 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b030b1f7-2859-3584-8149-bb603706c321 | -3.91993 | -52.13515 | 2026-10-09 05:04:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57e7d956-097a-33c6-9d52-a08164f0ccff | -9.09834 | -59.39062 | 2026-10-09 05:04:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7a549b4b-0d7c-34e4-90a4-856dd4152e12 | -8.28162 | -45.7376 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 8d16bb5c-618d-3f07-9890-82d4fe8a425e | -3.04572 | -54.14907 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9d2f1d6e-6cc3-3c99-ad2c-d2f271009512 | -6.45527 | -55.49313 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4bcca100-3f22-34d6-9592-106d7f3c2145 | -3.43215 | -56.93797 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 41eb4e65-e30f-3746-9cd6-c7fb0dec9150 | -3.66916 | -60.60837 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14e01a8b-f3a2-372d-a4b9-5fe7b6ff62ef | -3.12105 | -54.17615 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 517bf87e-ce06-3416-966b-2ef17663251d | -7.61431 | -46.53037 | 2026-10-09 05:04:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 724cc1b5-4928-39ff-a77c-6a155b9f0c21 | -11.77262 | -43.52729 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0860b3a6-aa17-334e-b626-985d30ffc741 | -8.33036 | -45.45352 | 2026-10-09 05:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9e696b8-cc15-3599-8f0a-b345611db2cc | -8.96531 | -45.14956 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a1686099-7a94-345c-93dc-c3e8961e1777 | -6.50803 | -55.39714 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd709ad8-176a-32ec-a2ac-9cf1911defbf | -3.31023 | -53.6971 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb6f80f1-426f-381e-8f0b-d0adf11b942b | -11.99832 | -43.4706 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a5293210-4a27-3eae-a81a-0eb3ef202999 | -3.08867 | -54.28656 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f8e335b-662e-3a69-aad8-2fd41d8aa781 | -4.31749 | -55.62432 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5e5c6f50-07bb-3130-bc0f-80501c6e667d | -3.71615 | -59.36448 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8e57efd-3e06-3704-9d2f-c2eb5284d30c | -3.03936 | -54.25574 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1021759b-74bd-3e7d-bf7e-956cdcf41832 | -2.56853 | -56.18233 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 682ddfe4-54af-3984-a9b6-14f3d2d8d9c5 | -3.62363 | -54.23384 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e0114fb7-c206-3171-a663-17f7c6dabcae | -3.18861 | -58.65059 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7922a241-8776-30bf-addb-626839b48392 | -6.0038 | -53.49443 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4edd66ec-4979-30c3-ad34-5abfe2d3ba38 | -6.92241 | -44.55408 | 2026-10-09 05:04:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5341b0fc-7788-342e-ae63-2eccf5af1483 | -3.38827 | -56.93053 | 2026-10-09 05:04:00 | NPP-375D | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4005e7a8-281c-3425-901e-c4407e20929f | -3.5249 | -59.33929 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 5b28ab2b-fb04-3979-bff7-86bb50686884 | -4.12547 | -46.86843 | 2026-10-09 05:04:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 235b9e1a-d207-3418-9155-f437ed515eb2 | -8.96797 | -45.16667 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c42c9bf3-6c6c-3666-a5fb-c08e0bb11d93 | -6.88105 | -45.90054 | 2026-10-09 05:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e1d15a1e-f3a4-3b29-9670-cb08328ab1e6 | -3.9777 | -56.1135 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0737b4ad-8696-3138-af40-1602a99cf8fa | -7.60487 | -55.71323 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b0715218-727a-31f7-9e34-e4a937ad3f8e | -3.17794 | -58.62963 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 7a1203bb-8773-36e8-b395-3293df181a0f | -3.27713 | -53.81422 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f3dfea7b-a6ae-3413-98e7-790dd1e9c559 | -6.12624 | -52.72686 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2788546a-2f64-3b9a-b466-c29911ab4eda | -6.24372 | -52.8344 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e061e69d-a68d-3fdc-aad0-8a926ea25707 | -3.73889 | -59.46012 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 05b785bc-b65c-34cd-b203-602bf1e1e504 | -11.46249 | -43.37877 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| afa5770d-2f59-3310-9d3b-67f0f0d60172 | -3.52844 | -54.67061 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| afe1250a-6423-3caf-9bb5-a165e4d17a97 | -3.75184 | -59.47678 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c7c108e9-d750-38bf-8a74-dffea21f8648 | -3.45683 | -59.57007 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 612b6b26-ca48-3ec9-b00e-a8aecdaaaf3c | -3.91316 | -55.89959 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 35ded4ca-183a-3859-b6a8-047a7a5d8763 | -3.47099 | -60.25329 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 790a7d24-fdd7-3180-a1b7-a4be9a426a77 | -3.039 | -54.23552 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 97c44070-07d8-31cf-af5f-6be063b6c93e | -3.10451 | -54.18944 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c142df8-41e3-3f52-833d-9d80ad2eaf5b | -5.96391 | -55.37084 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b10c723e-7a10-319a-a92f-a99b119f9c1c | -8.69636 | -62.41135 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 339be0db-1662-34a5-851e-d14acfc3f669 | -3.73919 | -59.37363 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 1c504c73-39ba-3fd6-a576-16d3e6b8b564 | -8.06505 | -45.63982 | 2026-10-09 05:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e8a57df2-ce83-3c6b-9632-9fee211a44d6 | -6.48869 | -55.96309 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 339dfaf2-8492-38af-90b7-1bdf13d4df35 | -8.17978 | -49.55283 | 2026-10-09 05:04:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2962f6dc-6be6-358d-8aeb-838f78129938 | -7.25479 | -48.06027 | 2026-10-09 05:04:00 | NPP-375D | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ffc489b1-37da-39d7-b81a-71a32509741c | -3.11195 | -53.7814 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 098bfc8d-9917-38cd-b1d2-b802d55876c3 | -2.97262 | -54.11069 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 71cccc70-79a8-3da8-a28c-46edb50c8ee8 | -7.19031 | -52.6289 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b38c94b8-dd46-360e-b602-51f8afb5a5ec | -3.03219 | -54.09947 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3b1fd9c-712b-3043-bc1d-51dc5a6c5abf | -3.4466 | -60.27372 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 048493b9-ab61-3b7b-98a8-bfa065c7d459 | -4.57126 | -54.95931 | 2026-10-09 05:04:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8d79f26a-7113-37ab-a28b-6319c784cdd4 | -3.30737 | -54.69975 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0b13116-38bd-381f-ae61-2ba6f9741c6f | -2.93981 | -54.18089 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b7f7b432-29f3-37a8-9ea7-964ff05d11b5 | -4.74798 | -55.66008 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0502173b-413c-36b9-b13f-dd609e1c005a | -8.66453 | -49.13707 | 2026-10-09 05:04:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 490da862-5544-3d84-96c3-51822f190f71 | -4.74057 | -55.65897 | 2026-10-09 05:04:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f5daf067-e5be-3d45-8591-071897905181 | -9.80089 | -44.77208 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b366e0d-11c4-306c-b747-2621f050ee6a | -3.00736 | -54.07579 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 613bc6e7-35ef-34a8-8a68-342779328784 | -3.07995 | -54.25006 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 7fca8108-c4b4-35e7-a3da-9102923ededf | -3.00431 | -54.13852 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6afdf63c-50e5-3660-94a6-63bb1be18edd | -3.4725 | -60.5001 | 2026-10-09 05:04:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README151.md)
