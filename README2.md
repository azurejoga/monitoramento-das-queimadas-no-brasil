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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d345c3da-7414-34b0-ae61-1ce91228b04f | -7.56974 | -45.84098 | 2025-04-16 03:55:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 963a8201-86d6-37c6-a852-d74ab991c1d3 | -5.15876 | -45.10889 | 2025-04-16 03:55:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| aea7c4b3-b07b-35f4-99ab-a897afe71bbc | -6.34703 | -43.65872 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 7161ba15-61fd-3cd3-917a-ddb010585ea6 | -6.34826 | -43.65154 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3b9aa642-70ca-3064-8b38-c343c723a402 | -6.341 | -43.65855 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 00653f0c-acde-3b85-b481-87c304016c94 | -6.34453 | -43.66287 | 2025-04-16 03:55:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 41ebe1bf-cd94-38a4-8d39-450e4d1f7a90 | -19.4388 | -44.33953 | 2025-04-16 03:57:00 | NPP-375D | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 25f773a4-2c5d-3b71-a2af-3643e9f38f7c | -29.77817 | -51.17675 | 2025-04-16 04:02:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| d6934433-b375-36be-9b83-b7c94b19b97c | -8.31398 | -48.0549 | 2025-04-16 04:17:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87e08fe6-e3f4-3933-888b-cb4e23098188 | -9.67693 | -37.07347 | 2025-04-16 04:17:00 | NOAA-20 | BATALHA | ALAGOAS | Brasil | 2700706 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 9368b177-d508-3f59-9865-099bfe4cf056 | -6.66207 | -47.58923 | 2025-04-16 04:17:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f619a1ea-2bf8-36f1-a22a-5939461b714f | -6.65716 | -47.59687 | 2025-04-16 04:17:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 14624114-2529-363e-ba48-372ee6ed462e | -10.32314 | -39.51477 | 2025-04-16 04:17:00 | NOAA-20 | MONTE SANTO | BAHIA | Brasil | 2921500 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eb7eaf1d-3ee0-3709-bfad-cb58064e6bc8 | -9.61572 | -37.03566 | 2025-04-16 04:17:00 | NOAA-20 | MAJOR ISIDORO | ALAGOAS | Brasil | 2704401 | 27 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 1d68aa1d-13f6-3639-8421-b308d88a6050 | -7.57176 | -45.84666 | 2025-04-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d86d31c1-5b75-3732-bc81-59dc27b6bde4 | -9.81357 | -38.45241 | 2025-04-16 04:17:00 | NOAA-20 | JEREMOABO | BAHIA | Brasil | 2918100 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 91c7a618-fe99-3866-977c-f62c12e52f6c | -3.12743 | -42.13956 | 2025-04-16 04:17:00 | NOAA-20 | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 35ec17f9-5a66-3099-b375-645f7e6b8a65 | -1.33439 | -48.36973 | 2025-04-16 04:17:00 | NOAA-20 | ANANINDEUA | PARÁ | Brasil | 1500800 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b0239745-fb07-3913-9604-0494933f9ea6 | -3.4826 | -51.19186 | 2025-04-16 04:17:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9d732c5c-dcf7-3b25-a746-2ff94034d479 | -8.30611 | -48.05788 | 2025-04-16 04:17:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2788b21c-a805-304e-94b4-e696abe1f72b | -6.66141 | -47.59333 | 2025-04-16 04:17:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02620ea7-1471-32fb-bee7-d808cc196897 | -4.2119 | -41.36481 | 2025-04-16 04:17:00 | NOAA-20 | DOMINGOS MOURÃO | PIAUÍ | Brasil | 2203420 | 22 | 33 | nan | nan | nan | Caatinga | 0.1 |
| b214fd09-dad8-3a20-acfc-558e14b0366f | -7.24415 | -44.7858 | 2025-04-16 04:17:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64812f76-2495-3658-baf8-d4803d4f1f7a | -8.3196 | -46.77694 | 2025-04-16 04:17:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 48d7e9b9-656e-3f34-bc14-deb919ca125a | -6.71442 | -47.59681 | 2025-04-16 04:17:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b6d3d95a-d88e-3ad2-a0cf-c451b94790a4 | -0.15869 | -53.32357 | 2025-04-16 04:17:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.1 |
| b7a07acc-a734-3bfd-babd-3492cf594882 | 0.32187 | -54.68384 | 2025-04-16 04:17:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c9dd856c-4f0a-3c70-8eff-388dc31bb0b3 | -2.00259 | -46.1795 | 2025-04-16 04:17:00 | NOAA-20 | JUNCO DO MARANHÃO | MARANHÃO | Brasil | 2105658 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 581265e3-5b14-3bc7-9d5d-c4cb7fdec9ce | -7.26368 | -54.24221 | 2025-04-16 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2a1f8de-915b-3413-ac46-ad6287bfbdc8 | -7.57232 | -45.84313 | 2025-04-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f047e9f9-97a7-39ab-b6ae-a3681eaa6fc6 | -7.56955 | -45.83907 | 2025-04-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98d3f243-c6f9-3260-ac6b-4a4bc82fe9b7 | -6.66074 | -47.59745 | 2025-04-16 04:17:00 | NOAA-20 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 6d268954-77fa-38fa-b48c-277b0cae4b33 | -9.86964 | -37.58518 | 2025-04-16 04:17:00 | NOAA-20 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 95f9d56d-479e-302e-826d-943fe4eba49d | -7.54622 | -43.5288 | 2025-04-16 04:17:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8fa5151a-7eb9-3778-84cc-4cb35e7be5cd | -0.3402 | -56.86007 | 2025-04-16 04:17:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4685fd17-d715-3f01-9ee2-987afdf6598f | -6.60316 | -54.22466 | 2025-04-16 04:17:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| beffc6c2-7734-3ff8-85a5-534acdd33008 | -1.0556 | -53.82084 | 2025-04-16 04:17:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.2 |
| 9f92210d-998c-381c-b592-a7b33038d5bc | -8.10987 | -43.12341 | 2025-04-16 04:17:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f47673d2-670c-30f0-a38d-3777a5a5880e | -7.56898 | -45.8426 | 2025-04-16 04:17:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 43ba6b21-22f0-37aa-a714-9e6ecf8deba6 | -3.127 | -40.98871 | 2025-04-16 04:17:00 | NOAA-20 | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 136cabb8-65eb-32b1-8566-edcf41aaa3dc | -8.31107 | -48.05017 | 2025-04-16 04:17:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9c0db1e-33e7-3c6a-92d6-e90a70b569df | -10.2302 | -40.19156 | 2025-04-16 04:17:00 | NOAA-20 | JAGUARARI | BAHIA | Brasil | 2917706 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f20b7e7b-473d-3cbd-bc63-3ffbdfe113df | -10.93198 | -37.9543 | 2025-04-16 04:17:00 | NOAA-20 | RIACHÃO DO DANTAS | SERGIPE | Brasil | 2805802 | 28 | 33 | nan | nan | nan | Caatinga | 0.4 |
| cf964b37-cbcf-363c-ba15-55dc07976882 | 0.82421 | -53.03279 | 2025-04-16 04:17:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57bfbac5-cd5c-34a0-adc2-db4092e9ba53 | -3.69392 | -53.75731 | 2025-04-16 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 44da0620-65e2-3fc6-8360-d815f52e8c54 | -6.34452 | -43.65854 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 95d4c3b4-8034-30ab-882e-3c6108e129cf | -11.50262 | -53.55423 | 2025-04-16 04:19:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| ccb9f7e5-d006-37cf-9eb9-04d02f61f395 | -6.36128 | -43.65779 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd757d16-0991-3b55-8396-9cf6d7ce3e72 | -13.72913 | -55.76303 | 2025-04-16 04:19:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 307ae711-0dd2-31e8-9ffe-1ae7c448ab61 | -5.16514 | -45.10621 | 2025-04-16 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e7fbb144-e632-34b9-b555-02d4ea0e47af | -14.0321 | -42.60194 | 2025-04-16 04:19:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 882c627e-af4b-3b9b-86ef-1c0080698b33 | -5.16458 | -45.10971 | 2025-04-16 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6652284f-18f6-3d72-b1e2-df4f803a837f | -6.33786 | -43.65749 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| cfefdac2-fc18-39d3-8abd-d7401c95884b | -5.16181 | -45.10568 | 2025-04-16 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5112e9cc-1832-323c-9b02-520df3cc9cfe | -6.34895 | -43.65201 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0f2e9e1b-0a0b-366b-aabe-8bcb8d21a5ac | -5.64416 | -43.70653 | 2025-04-16 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b25d28e0-0029-3fd4-b8c7-13c71b21d468 | -4.91463 | -51.62069 | 2025-04-16 04:19:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73d12541-195f-3ee5-9f4b-6dcdb04b4895 | -12.21401 | -56.67145 | 2025-04-16 04:19:00 | NOAA-20 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e0cb154-fa13-3f7e-814b-d56b582ba64e | -5.4694 | -39.52124 | 2025-04-16 04:19:00 | NOAA-20 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e220c48a-789d-392e-a57d-49ac78f31e75 | -6.34785 | -43.65906 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 94ad725b-2381-3dfc-998e-abce6a399238 | -5.64084 | -43.70601 | 2025-04-16 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 46a346e1-cc32-361b-ad05-c3450b1ec3d2 | -16.82989 | -54.32747 | 2025-04-16 04:19:00 | NOAA-20 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3c1a58c3-5e75-3e04-9399-186ce4efda46 | -14.17341 | -56.99303 | 2025-04-16 04:19:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| 0ab02ecc-599f-353f-b236-7bf4a2462e8e | -4.50366 | -46.08033 | 2025-04-16 04:19:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d5b573ca-21f8-37f8-afd8-13a5c9c47ac2 | -15.70083 | -52.80135 | 2025-04-16 04:19:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9244485f-7e67-3e25-b50e-9a57b3a83e87 | -6.34064 | -43.66154 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3d60e9a2-3198-3cc9-bacc-8ca8951f2897 | -6.34507 | -43.65501 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 2a0642b7-a2cd-3624-a718-7cca857bedb2 | -6.35173 | -43.65606 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ba50a57b-a8bb-38bc-8ebb-d2044cde8713 | -11.97407 | -40.28896 | 2025-04-16 04:19:00 | NOAA-20 | BAIXA GRANDE | BAHIA | Brasil | 2902609 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f2187a08-044d-3f19-871a-2abf8bcccd11 | -5.94711 | -44.45959 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dd580830-020d-3b99-9f6d-dd15f2ca43a1 | -14.46391 | -44.06414 | 2025-04-16 04:19:00 | NOAA-20 | MANGA | MINAS GERAIS | Brasil | 3139300 | 31 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 2d2dc13b-4222-3745-8f2c-1068ae46e588 | -9.62036 | -54.13834 | 2025-04-16 04:19:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.1 |
| aa4aed77-6a34-36c0-8265-99391ddd2c2e | -6.3585 | -43.65375 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ca724548-00e1-37a3-b774-2236e649a1bd | -12.36778 | -41.81786 | 2025-04-16 04:19:00 | NOAA-20 | SEABRA | BAHIA | Brasil | 2929909 | 29 | 33 | nan | nan | nan | Caatinga | 0.2 |
| 11999235-0650-34fb-be32-a6c967ae3cb3 | -12.83061 | -40.60575 | 2025-04-16 04:19:00 | NOAA-20 | BOA VISTA DO TUPIM | BAHIA | Brasil | 2903805 | 29 | 33 | nan | nan | nan | Caatinga | 0.1 |
| 715dc20e-e244-3624-bdf1-693b639ef23d | -9.88394 | -56.45647 | 2025-04-16 04:19:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 027c6e1a-ab6c-3766-9ba4-0ab0f6976b87 | -5.93941 | -44.46545 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 7c51e83a-b1da-32cf-b092-829f1f20dd1b | -3.71182 | -53.75314 | 2025-04-16 04:19:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| e1c2e8e8-174b-356b-a78a-3748b534b495 | -14.55923 | -58.9298 | 2025-04-16 04:19:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 99e3b23c-e15f-3b25-be9b-f39078c37fa4 | -14.01314 | -40.52829 | 2025-04-16 04:19:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.3 |
| 3fb5e276-c0b3-355d-94cd-0dd545325bdb | -16.71468 | -39.92249 | 2025-04-16 04:19:00 | NOAA-20 | GUARATINGA | BAHIA | Brasil | 2911808 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.2 |
| ba403cd7-632e-3f8f-9918-47831c2efea1 | -13.68359 | -50.09884 | 2025-04-16 04:19:00 | NOAA-20 | MUNDO NOVO | GOIÁS | Brasil | 5214051 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| ea699885-e368-3040-a91c-d4c47df0a14b | -12.06498 | -44.67214 | 2025-04-16 04:19:00 | NOAA-20 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6288b71c-e168-3c5e-97bd-78e3aa8d6f81 | -6.34119 | -43.65801 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 289dd9ae-1453-3ba8-af7b-4de5e0c1b8ad | -5.54816 | -45.1998 | 2025-04-16 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dfb7960d-b065-356c-9cd6-2c4fb4ee3a7b | -6.09374 | -46.67813 | 2025-04-16 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 040c528c-60f2-326a-90d0-ad8ea29ea1ec | -5.16126 | -45.10918 | 2025-04-16 04:19:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 8.2 |
| abb48cd1-ff42-3005-9f88-3ff3db83be19 | -6.09129 | -46.67803 | 2025-04-16 04:19:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6e16bccf-0c9e-3a9f-8bf6-a732e5214761 | -9.95794 | -58.25604 | 2025-04-16 04:19:00 | NOAA-20 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fa66f4c7-0604-3585-b9ad-18aac75adeb3 | -11.23984 | -51.51647 | 2025-04-16 04:19:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3df41e67-7088-316e-a6f8-e50efb7047a2 | -11.83911 | -44.88614 | 2025-04-16 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 802407fa-7420-3d8e-a4ba-1bea08278b9a | -6.3484 | -43.65554 | 2025-04-16 04:19:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 1b4b34ab-af90-3a0a-a57b-a2199a68429d | -12.0667 | -40.01868 | 2025-04-16 04:19:00 | NOAA-20 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a56261d1-03c5-3658-82ad-e6043c1bfb63 | -5.94326 | -44.46252 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ac1d6d06-711e-30c1-bebb-c0ea62c06faa | -15.794 | -57.45224 | 2025-04-16 04:19:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2a00f770-2a48-35ee-9197-735a754c21f8 | -16.56857 | -54.97368 | 2025-04-16 04:19:00 | NOAA-20 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 9cdf62b2-3e5c-34ab-81a9-425e0c515d6b | -9.78561 | -54.47105 | 2025-04-16 04:19:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5cec6e51-de84-30b3-a519-54010c4ad546 | -12.07338 | -55.02097 | 2025-04-16 04:19:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da94e5c4-79ff-3a89-8df6-1dd908c4eb85 | -9.37045 | -55.29808 | 2025-04-16 04:19:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6d326b71-f072-3215-890d-20a9377c4b55 | -5.94272 | -44.46597 | 2025-04-16 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README3.md)
