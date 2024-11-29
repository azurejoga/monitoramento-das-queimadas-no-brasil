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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| da4de354-d432-3352-b074-cc04cbc4a0b9 | -4.78713 | -46.11483 | 2024-11-29 03:42:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a067b859-2415-3270-abe4-c81fa29d0b80 | -7.06286 | -38.9704 | 2024-11-29 03:42:00 | NPP-375D | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 40340798-0622-3b20-9d4a-4c3e51589ab5 | -5.71683 | -43.83737 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4c1207f1-afea-37d1-928f-ff1e3b3b5277 | -11.1054 | -37.71385 | 2024-11-29 03:42:00 | NPP-375D | RIACHÃO DO DANTAS | SERGIPE | Brasil | 2805802 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c5970696-bcb6-3476-9c15-90eb349323ec | -5.8638 | -42.75977 | 2024-11-29 03:42:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 5037c298-92ec-3d66-8888-f2cc9019dfbc | -8.37776 | -44.47638 | 2024-11-29 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94fecd02-0582-3853-9394-258cfdb8b5ef | -6.14194 | -44.73016 | 2024-11-29 03:42:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3fd34a80-caa6-3602-b314-214a934cd824 | -4.92306 | -44.53235 | 2024-11-29 03:42:00 | NPP-375D | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aae865c4-35e9-35ee-a1b0-67e8bc90395f | -5.56026 | -42.87768 | 2024-11-29 03:42:00 | NPP-375D | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 928544cc-630c-3c18-b4a8-3f0b2d0af8b7 | -6.74991 | -46.52256 | 2024-11-29 03:42:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2ff696a0-c67d-3079-b4f9-1c8d3a0d773c | -6.09701 | -43.96585 | 2024-11-29 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b594fe72-37a4-3d2d-ae2e-5341bcd4977f | -5.72208 | -43.83826 | 2024-11-29 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 36a7280b-0c02-3f81-821c-730ddbc9c85a | -9.44734 | -35.91383 | 2024-11-29 03:42:00 | NPP-375D | RIO LARGO | ALAGOAS | Brasil | 2707701 | 27 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| 983abc55-eb7a-378a-9e50-4376e63cf311 | -17.09437 | -43.80449 | 2024-11-29 03:44:00 | NPP-375D | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3b9647d-4abd-3f2c-b4c5-b046a1d8b1de | -16.68246 | -43.88329 | 2024-11-29 03:44:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 12cb2241-bb46-352d-9cbe-315be0535a26 | -15.96528 | -38.9234 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b596a6e6-9ead-3cab-9b9b-a521c4501769 | -19.17713 | -40.13496 | 2024-11-29 03:44:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 10f3efc5-d6c9-3680-9f42-ae7ab657c9ea | -18.92612 | -39.91666 | 2024-11-29 03:44:00 | NPP-375D | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ec785cfa-7e4f-3ea5-9a13-56eb170e893c | -17.76287 | -42.22403 | 2024-11-29 03:44:00 | NPP-375D | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 958e957b-9723-3cad-ace7-abff7fc67430 | -17.62378 | -42.74776 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9b1d6841-8bd9-3ea7-a420-fcf59cfef14d | -13.39572 | -43.52556 | 2024-11-29 03:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 423018ca-2093-3243-9efe-429f131ab288 | -12.16638 | -39.85693 | 2024-11-29 03:44:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| f17494cc-3aa0-3815-b708-2dcfc78a93dc | -19.17779 | -40.13102 | 2024-11-29 03:44:00 | NPP-375D | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| f9bc0130-1194-3d3d-9d78-11c255f2bdbc | -17.60187 | -42.73239 | 2024-11-29 03:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f7c4710a-6937-3659-99e8-fcb987834129 | -13.88255 | -43.07731 | 2024-11-29 03:44:00 | NPP-375D | MATINA | BAHIA | Brasil | 2921054 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 515b704b-d103-3a29-8679-8f96fc56ecd2 | -17.16703 | -40.6791 | 2024-11-29 03:44:00 | NPP-375D | MACHACALIS | MINAS GERAIS | Brasil | 3138906 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 5db1fb24-a778-32b5-8016-86fc421347cd | -15.96188 | -38.9228 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 92cafe60-6a46-34a7-8e04-d1db543d5e5c | -17.58002 | -42.76144 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| 59fcfc29-c50e-3285-bcae-80f63618a984 | -17.57703 | -42.7553 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| c241ddb3-f407-331e-a38c-aa0f53d1446e | -17.60583 | -42.73321 | 2024-11-29 03:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7abcd836-9480-3e34-b6a5-de684d824de2 | -15.96931 | -38.92024 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| f83e622f-1710-3ebf-9787-cae1bd8bff6a | -15.96251 | -38.91904 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3d067b8b-7ea7-3922-a066-749527cba425 | -19.26496 | -40.70541 | 2024-11-29 03:44:00 | NPP-375D | COLATINA | ESPÍRITO SANTO | Brasil | 3201506 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 35bc82cc-af7d-3ce2-a20c-c91682807e66 | -17.58401 | -42.76222 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 22.0 |
| a6851658-1c10-3922-91c0-5d4436589aff | -15.95973 | -38.91467 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7e41790-bef8-34d9-bdcf-b1b4c67dbb4f | -15.96591 | -38.91964 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 2d6c16d7-ee85-3f7e-a146-7a33f444ec6e | -12.6733 | -42.33447 | 2024-11-29 03:44:00 | NPP-375D | IBITIARA | BAHIA | Brasil | 2913002 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| ee42612e-b08b-3380-bcc7-34cae37cacaa | -17.58101 | -42.75608 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 24.8 |
| b915118a-4cfa-3911-8524-5684f005e972 | -17.57603 | -42.76068 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 25.3 |
| f89c518f-0057-3947-ba0f-ba9cd1e29d0c | -17.585 | -42.75684 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 35.5 |
| b794eef7-a162-3f85-95bb-a635822e973a | -15.96313 | -38.91527 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| aa3c9110-aba8-35bf-8f4b-f415767ba0c4 | -15.95294 | -38.91347 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 20f12c7d-7b09-30f1-8444-a0f9a37a94d5 | -17.75156 | -42.89606 | 2024-11-29 03:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d3c95931-fa38-3a4b-a517-19eaba81ce65 | -12.16712 | -39.85257 | 2024-11-29 03:44:00 | NPP-375D | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| f2c9eb83-e573-317b-9c83-e249e063216f | -16.68156 | -43.88474 | 2024-11-29 03:44:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e6bdc9c9-525e-3254-84c9-045a75a08ee2 | -17.7512 | -44.96069 | 2024-11-29 03:44:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e1fb7d54-9139-3542-b02e-d959f5f4ee4d | -17.62281 | -42.75312 | 2024-11-29 03:44:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6d9e008-4f0f-3048-9531-9465a877f223 | -17.60283 | -42.72713 | 2024-11-29 03:44:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecec81db-7d50-34bf-9442-637a8bdf56a7 | -18.04051 | -39.92574 | 2024-11-29 03:44:00 | NPP-375D | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| ecd571d4-d59c-3558-852d-c1ba8edf251e | -15.95911 | -38.91843 | 2024-11-29 03:44:00 | NPP-375D | BELMONTE | BAHIA | Brasil | 2903409 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0c64f641-bce5-34e9-9164-74fbf759a919 | -15.49942 | -42.00822 | 2024-11-29 03:44:00 | NPP-375D | INDAIABIRA | MINAS GERAIS | Brasil | 3130655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 4a6f07b2-25fb-3689-9eb9-8c59bfdf33b4 | -13.39643 | -43.52733 | 2024-11-29 03:44:00 | NPP-375D | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2beac22f-71ae-3cd4-8424-18be17be86c4 | -20.90046 | -43.81982 | 2024-11-29 03:46:00 | NPP-375D | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 764a749f-e96c-3205-907d-d34a2fd0bb18 | -22.19111 | -42.86247 | 2024-11-29 03:46:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5399c8cb-5956-3a34-ac58-870049e6b9e9 | -22.19084 | -42.86437 | 2024-11-29 03:46:00 | NPP-375D | TERESÓPOLIS | RIO DE JANEIRO | Brasil | 3305802 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 1e4b200f-319d-3a43-8f4d-171637c58b67 | -19.66699 | -45.88524 | 2024-11-29 03:46:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 55422960-c4c7-3b87-bf1c-397174cf9d03 | -20.20504 | -41.43573 | 2024-11-29 03:46:00 | NPP-375D | LAJINHA | MINAS GERAIS | Brasil | 3137700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| f26f63b7-84f1-36b6-8781-0fde3e1c4f2d | -20.93641 | -41.66003 | 2024-11-29 03:46:00 | NPP-375D | SÃO JOSÉ DO CALÇADO | ESPÍRITO SANTO | Brasil | 3204807 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| ea9603fd-ffbd-3bf4-ba96-efd6be5e0d70 | -19.54608 | -41.13097 | 2024-11-29 03:46:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 169b5278-af3f-3cb5-a926-8ab12c80b78c | -19.48133 | -41.61112 | 2024-11-29 03:46:00 | NPP-375D | POCRANE | MINAS GERAIS | Brasil | 3151909 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 8091fd22-ddd2-3841-a061-6161c782dbd4 | -19.66601 | -45.88397 | 2024-11-29 03:46:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 041ab0c7-6e14-344c-9f13-dcf411b9058f | -20.69902 | -40.88686 | 2024-11-29 03:46:00 | NPP-375D | ICONHA | ESPÍRITO SANTO | Brasil | 3202603 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 02c8bf3b-50e3-3e4e-ba35-3bc829dbfca3 | -19.67061 | -45.89138 | 2024-11-29 03:46:00 | NPP-375D | ESTRELA DO INDAIÁ | MINAS GERAIS | Brasil | 3124708 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6b2da964-a733-315f-ba85-fdeb612c0349 | -19.33243 | -46.3198 | 2024-11-29 03:46:00 | NPP-375D | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99b220ca-8e15-3ff5-a604-c6ce9afd62ff | -20.69803 | -40.88789 | 2024-11-29 03:46:00 | NPP-375D | ICONHA | ESPÍRITO SANTO | Brasil | 3202603 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 8c1b0f81-7444-37d3-a1a9-9b3d6afa20cc | -21.1792 | -43.98146 | 2024-11-29 03:46:00 | NPP-375D | BARROSO | MINAS GERAIS | Brasil | 3105905 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 76e2c5d8-6d2f-3ed6-b5ec-77a51d84262d | -19.54963 | -41.13166 | 2024-11-29 03:46:00 | NPP-375D | AIMORÉS | MINAS GERAIS | Brasil | 3101102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b33876fb-f22d-3a7e-b638-e6ac68032764 | -3.259 | -53.6388 | 2024-11-29 03:50:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 62.4 |
| 2ec4dd03-a62e-3b4d-9166-02a31f39402b | -1.5869 | -53.8336 | 2024-11-29 03:50:00 | GOES-16 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 51.1 |
| d74616a8-c307-3b56-bccf-81de62befb59 | -2.966 | -53.3027 | 2024-11-29 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 755d657d-6c20-392c-9d8d-a1b465070dfe | -2.6499 | -48.7772 | 2024-11-29 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 961303ec-e1d0-37cd-ac9c-da2373b3a25c | -1.5897 | -52.2915 | 2024-11-29 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 579b37cf-f7cd-3c5d-b958-05ef9d08f435 | -2.6684 | -48.7767 | 2024-11-29 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 153.9 |
| 578c3db2-38b1-311d-b6b8-09b10efd040e | -2.3233 | -46.8786 | 2024-11-29 03:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 87.8 |
| af0db33d-7f1a-3185-9640-0156905af164 | -2.6683 | -48.7981 | 2024-11-29 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 189.9 |
| a5ad1b03-3cfd-366e-97ba-89b47f03efc7 | -2.9844 | -53.2819 | 2024-11-29 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 228.7 |
| 49502082-6671-31a3-b747-25f31f181bcb | -1.6997 | -52.4535 | 2024-11-29 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 106.8 |
| e2a99721-efae-33fc-b457-54c7fe84201b | -4.4404 | -46.5975 | 2024-11-29 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 160.0 |
| 636e265e-a87b-35c9-b955-ab6133f9650d | -1.092 | -53.3954 | 2024-11-29 03:50:00 | GOES-16 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ba471e6e-1f67-3008-8cf4-07821fd235a1 | -2.3419 | -46.8781 | 2024-11-29 03:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 163.2 |
| ef914033-c20d-399f-8e1c-5579313d26ea | -1.6997 | -52.433 | 2024-11-29 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 94125e65-6206-3aea-bc7c-d6733528b64c | -2.3419 | -46.8562 | 2024-11-29 03:50:00 | GOES-16 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 36c03d2f-9d2c-3f38-87c3-a449103f1d9a | -2.9844 | -53.3022 | 2024-11-29 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 151.0 |
| 2618527f-1777-3563-a3ce-dcf2b9b83624 | -4.4405 | -46.5754 | 2024-11-29 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 238.1 |
| 3f927681-f4b0-3282-9d49-8884c054156f | -17.5805 | -42.7483 | 2024-11-29 03:50:00 | GOES-16 | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 99.3 |
| da60519f-1a3c-38b1-9399-53606d26f799 | -2.6498 | -48.7986 | 2024-11-29 03:50:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 143.8 |
| 86de5471-0553-34ad-9dde-7b66ba2ec066 | -4.4218 | -46.5985 | 2024-11-29 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 102.1 |
| 3f7367cb-a240-33c4-b112-35886e7813a3 | -1.6081 | -52.2912 | 2024-11-29 03:50:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 85.3 |
| 7a1e6a52-e24f-3b59-a429-412cb36dc7c7 | -2.966 | -53.2824 | 2024-11-29 03:50:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.6 |
| 0715ad52-e8b6-3088-819b-e883e12adb6e | -4.4219 | -46.5764 | 2024-11-29 03:50:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 144.4 |
| af2dc7da-2db1-3426-a39b-ba4640936a06 | -2.966 | -53.3027 | 2024-11-29 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 3161ec3c-f483-3868-a9b2-5c68bbf02b9d | -3.2406 | -53.6393 | 2024-11-29 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.6 |
| e02a5b3b-8914-3630-893e-1fea2b2bf659 | -4.4405 | -46.5754 | 2024-11-29 04:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 33e1bd05-c3fc-39dd-8b26-8311d4d7a88f | -2.6683 | -48.7981 | 2024-11-29 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 201.8 |
| 3b7bbc31-3c75-308e-a524-b42967d11843 | -1.5897 | -52.271 | 2024-11-29 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 54.4 |
| c9efb972-50ef-342e-b258-a031e2c07183 | -3.259 | -53.6388 | 2024-11-29 04:00:00 | GOES-16 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c20049b1-51f5-33fa-bdf7-2b96ff242296 | -4.4219 | -46.5764 | 2024-11-29 04:00:00 | GOES-16 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 81.0 |
| da8d884d-d29a-3cba-9afc-c1be5481e6f2 | -2.966 | -53.2824 | 2024-11-29 04:00:00 | GOES-16 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 79.0 |
| 9be8ae85-e1fd-3c99-adc2-30f7990f1cf6 | -2.6499 | -48.7772 | 2024-11-29 04:00:00 | GOES-16 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 110.6 |
| 62b238e1-3090-38a8-9392-1e22d9b540bd | -1.6997 | -52.4535 | 2024-11-29 04:00:00 | GOES-16 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 97.3 |


[Clique aqui para ver as próximas entradas](README22.md)
