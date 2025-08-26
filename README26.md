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
| 3e134f64-7a07-331e-a879-19597500394d | -4.82817 | -47.31458 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d073e56f-8009-34b2-bc4c-677d62287b58 | -6.10079 | -43.16123 | 2025-08-26 03:55:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 64ee0f4b-ff99-3962-abaa-484e346da1e4 | -7.85385 | -46.73925 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7185ae6c-3e17-38f8-9b91-daead46bd456 | -7.9029 | -38.72287 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 8fd819a9-ab5f-356b-9134-4646d546b9a0 | -11.14837 | -44.75237 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cec16a31-7c3a-3688-85ce-ff23bf272bd7 | -6.13947 | -44.40237 | 2025-08-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| e42d1358-3e36-3823-91d8-da787d8bd402 | -9.32322 | -40.22149 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 900c2cb2-4ff3-3b70-b363-e488e87062b3 | -7.22048 | -44.40738 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 007f3c8e-8bc1-37da-8868-d4d25862ccbf | -11.62805 | -46.39546 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a2d525e1-0614-3c6f-9e23-b959a8452cb0 | -11.15267 | -44.77512 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 133c8edd-96fc-3e32-ac84-ee53e09b5797 | -7.08005 | -41.50099 | 2025-08-26 03:55:00 | NOAA-21 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| aab076a9-b32c-3e73-8e5d-c85025649cf9 | -10.87499 | -45.23426 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cea674f4-e2e2-3a51-9e23-ecc326c65e12 | -6.56673 | -44.21453 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 928cd2dd-0a19-3229-a3cc-7a7111e68517 | -9.57511 | -48.63269 | 2025-08-26 03:55:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a130f8ab-7083-319e-aa60-aa8c8415eefc | -6.78729 | -44.34786 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3a14fe4d-2b7b-3f27-aa27-1ce9909f896c | -11.15454 | -44.76447 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 771ca70c-e06b-39df-8c5d-6b9edc865740 | -11.63869 | -44.86685 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 91a998e6-3a3a-3ed5-8bdd-1f9e9dc0c825 | -6.89417 | -45.65349 | 2025-08-26 03:55:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d1275fbf-28da-3a22-8e50-dd936fc2a432 | -12.4424 | -43.56314 | 2025-08-26 03:55:00 | NOAA-21 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ded8d066-834d-359d-b862-18cf38d9c8dd | -8.23778 | -45.12418 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 01c80bf5-b07d-35b3-a545-905d8b7e4dfe | -11.14122 | -46.33538 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 814f3bc3-e006-3fd9-a2f7-3ca4d5890be7 | -6.27174 | -43.68701 | 2025-08-26 03:55:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0b072a53-4222-354d-ab3f-02c40b892502 | -4.82626 | -47.31662 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 66f38d42-79d0-32f2-9207-5417af0df9be | -8.24898 | -45.09558 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3231ea2-0087-36cc-8cc1-aa06e2b3348c | -10.8078 | -48.31214 | 2025-08-26 03:55:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 994b7de9-61df-3f46-9927-06f87b8dbd1f | -11.91676 | -46.72881 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 46d19f26-2a08-359c-ba18-0d600384ac0c | -6.4994 | -44.68499 | 2025-08-26 03:55:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7b0b1c19-9a65-350e-b32e-388d65750617 | -7.2159 | -45.31245 | 2025-08-26 03:55:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ba3b8f10-fff6-3388-8bc3-980b3fd0c42f | -8.07376 | -47.30973 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| eb3738ba-8ace-36c0-acf6-12c517747504 | -8.29438 | -47.23092 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f504b27d-ea79-339f-afcf-b7e32fc0bf20 | -11.28576 | -44.99514 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| be8bf959-2526-3ea0-9667-821a98301eaf | -11.14522 | -44.77016 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f7155713-d2c4-38b1-8881-7f29eb56dfe9 | -10.75857 | -47.0646 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| af7e8c59-310c-3fc4-897f-59d856813176 | -11.15795 | -44.76873 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e8e4edbd-cdd5-35ae-861b-28886acdf062 | -11.06222 | -52.00808 | 2025-08-26 03:55:00 | NOAA-21 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0360cf47-9bb7-3164-99de-0087e746513d | -5.41348 | -49.20296 | 2025-08-26 03:55:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 382cf8de-05b1-326b-9510-d5ef3a4d6e7f | -9.66951 | -47.10907 | 2025-08-26 03:55:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37348bf9-e9bb-3adb-bc1a-849a0f9605e1 | -11.34139 | -47.85015 | 2025-08-26 03:55:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 5dc4e4dd-de4b-34d5-b72e-127b41c69514 | -8.33022 | -50.57907 | 2025-08-26 03:55:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 47b05648-3273-3129-a159-9ed15e9903e3 | -8.07723 | -45.01235 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9319ca93-8b6a-3a5f-9eec-8090baab5c2a | -8.23979 | -47.45226 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 028f4f74-5003-3609-8fe3-a3a8c37c0bbe | -7.64887 | -39.01976 | 2025-08-26 03:55:00 | NOAA-21 | JATI | CEARÁ | Brasil | 2307205 | 23 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 590d1406-9993-3686-8e6c-39c45a2c58aa | -11.9241 | -46.73994 | 2025-08-26 03:55:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 74fa1db8-f678-311e-a4b5-11af348a64af | -9.26274 | -43.4072 | 2025-08-26 03:55:00 | NOAA-21 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 376cbe89-d7f4-34e5-b952-07fbfc103d59 | -7.58381 | -47.49038 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 90079a3e-7c12-3700-b3bc-fafe9702f364 | -10.60779 | -44.77681 | 2025-08-26 03:55:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f40c4009-e21d-3cf5-b93a-4b958f82e695 | -12.64371 | -38.48072 | 2025-08-26 03:55:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 058c1643-4e59-316f-9cf8-38b18e5a3b2c | -9.64553 | -40.59302 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 8a9e53de-7d98-3ad5-afb3-4de87bc9b70d | -7.74922 | -43.92636 | 2025-08-26 03:55:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 10d38094-384d-31a4-9889-738e95ab5185 | -7.65091 | -42.6745 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 6deba18f-66fa-3814-b03a-445e056772de | -7.15651 | -44.16915 | 2025-08-26 03:55:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3bebcb30-a16c-356b-874a-c66edaf40244 | -8.37533 | -48.02664 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c07bf33b-45c4-381b-86dc-2877b09d7044 | -8.12838 | -47.29482 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 944c5b7e-5186-3961-ab95-12565281806b | -6.1854 | -44.15436 | 2025-08-26 03:55:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f31c2065-840f-3bee-8d92-813de054727c | -9.7499 | -37.91713 | 2025-08-26 03:55:00 | NOAA-21 | CANINDÉ DE SÃO FRANCISCO | SERGIPE | Brasil | 2801207 | 28 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59068f9b-0b23-3d51-b246-6af4dd2eeb19 | -7.90236 | -38.72633 | 2025-08-26 03:55:00 | NOAA-21 | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 848aa6f1-d6f4-3ccc-829e-155703dcc113 | -6.69924 | -48.37958 | 2025-08-26 03:55:00 | NOAA-21 | PIRAQUÊ | TOCANTINS | Brasil | 1717206 | 17 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 88ada86c-7ab9-3b9b-9e04-0efcad879018 | -8.2844 | -47.22913 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 97a79eb6-24eb-3135-80a8-aecf0faef077 | -9.32379 | -40.21793 | 2025-08-26 03:55:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| a84a64de-8d22-3725-8770-cd8ec9b427c8 | -8.32676 | -47.25307 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ce917172-0285-340b-b913-36d149f0854d | -12.37169 | -46.57085 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 50a023f3-8d7e-3696-be43-eaebc032784b | -8.90817 | -45.72138 | 2025-08-26 03:55:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f2166d4d-0f97-3942-a219-3155522264ec | -11.1626 | -44.76593 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 20.7 |
| abdbfba2-207b-3fc1-9a64-8b538147b49c | -11.63528 | -44.86258 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 725ee44c-e09b-3460-b2df-fd625996166b | -11.14774 | -44.75593 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| da4570a1-b2b9-30ac-9453-f85c78e321bf | -7.69227 | -37.55706 | 2025-08-26 03:55:00 | NOAA-21 | AFOGADOS DA INGAZEIRA | PERNAMBUCO | Brasil | 2600104 | 26 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 68eee58f-024a-314e-a543-f0945b4740c7 | -7.30485 | -44.52513 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d7f42e37-cf6e-3cc4-980f-ac54b955e572 | -5.55248 | -45.19928 | 2025-08-26 03:55:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 103e8928-7c3a-313c-a129-89ee0dbb6e9a | -11.14963 | -44.74525 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8e522445-4e07-32a1-97da-5038833b5307 | -8.12331 | -47.29412 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c73c5a37-268f-312c-9e92-c0a36c0e960f | -8.11168 | -47.1299 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3556e7fc-5be9-30fe-a53b-bf01f5e054e9 | -6.31032 | -47.41773 | 2025-08-26 03:55:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8aae8b46-875e-39de-a73e-73bd67eaa4d6 | -6.89227 | -44.42108 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1fd73b6-e284-3979-9971-a361772d9721 | -7.44616 | -42.04326 | 2025-08-26 03:55:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 182d52ef-9051-3a0e-a66e-abff46dadc6b | -11.30574 | -43.28767 | 2025-08-26 03:55:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6b78cd3d-9267-31e0-a1cc-3998477ab656 | -8.38125 | -48.02551 | 2025-08-26 03:55:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1277b76e-1afe-353b-8c66-2fe476aad04a | -7.66587 | -42.67703 | 2025-08-26 03:55:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| edc7aeb6-c154-3556-bc25-e33bed1644b1 | -12.37416 | -46.55736 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64d02c6e-712e-33cf-b3df-a660e181aa19 | -8.70672 | -47.86908 | 2025-08-26 03:55:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c99a1fd5-f6b0-39c9-92ae-e4fddbd969f6 | -11.2544 | -44.9819 | 2025-08-26 03:55:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 268776c4-5e5c-3446-9692-8316a16ebcf3 | -8.07469 | -47.30859 | 2025-08-26 03:55:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6426f73b-425d-3e95-9f85-8e4ca8524fdc | -7.21593 | -44.43419 | 2025-08-26 03:55:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 62c1a370-d6d4-3169-85f7-a1749765d99c | -10.53634 | -46.78642 | 2025-08-26 03:55:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 86babbbc-7761-3f7c-9baa-c265be1ab698 | -11.63466 | -44.86616 | 2025-08-26 03:55:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5dcdb24c-7661-3fb7-a919-6545b8280770 | -10.43689 | -47.17659 | 2025-08-26 03:55:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f682cd66-4913-359e-bdeb-a9accebb7a08 | -6.89646 | -44.42201 | 2025-08-26 03:55:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f146a3a-8625-327e-bc2e-10b384e1d008 | -8.24824 | -45.09977 | 2025-08-26 03:55:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09c5d657-03cd-3f3c-87f4-d5e916a27ce1 | -11.16198 | -44.76947 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6cf9e057-e42b-3ea9-a581-5135cd317ac2 | -11.149 | -44.74881 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6af94d0-1c61-341c-968a-8d7d64482743 | -11.14648 | -44.76304 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 6d2456fe-86d9-32e4-aeb6-71ade79bb736 | -11.15768 | -44.74669 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8adb06a-0af1-388e-b08d-b5fbb987ce41 | -6.78957 | -44.30898 | 2025-08-26 03:55:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 492171e1-df49-33ea-986a-2cc4a536919e | -9.17124 | -40.59792 | 2025-08-26 03:55:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 3fce6a89-8cb9-3f02-9066-9212db779d0e | -11.61014 | -46.40228 | 2025-08-26 03:55:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 1984ee4a-e71a-3e12-a037-d4de348ab590 | -5.8638 | -46.4128 | 2025-08-26 03:55:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a15b0ad8-e91c-3b2a-82e7-d3ca2d536137 | -11.14606 | -44.78893 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaac5968-e21e-358d-9fd1-2047199483cb | -6.76613 | -43.83052 | 2025-08-26 03:55:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 922ee570-7b88-3e10-ae30-9fb16be40eec | -11.15705 | -44.75024 | 2025-08-26 03:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2c586a6-eab6-3054-9025-007cd39f2258 | -12.42156 | -46.81491 | 2025-08-26 03:55:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 07103a1e-4f54-3c5b-9baf-4854f12b7d4d | -4.82281 | -47.31388 | 2025-08-26 03:55:00 | NOAA-21 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README27.md)
