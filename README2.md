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
| ee047aa2-64f8-3075-a737-0c012ed94ae7 | -10.28902 | -36.36369 | 2025-11-06 00:11:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 42.5 |
| 717f5531-beb9-3047-a44b-dccac3b2b330 | -11.88001 | -40.94635 | 2025-11-06 00:11:00 | TERRA_M-M | TAPIRAMUTÁ | BAHIA | Brasil | 2931301 | 29 | 33 | nan | nan | nan | Caatinga | 10.6 |
| 101429dc-d653-386b-a97d-ac4789a9ea2b | -10.28681 | -36.37046 | 2025-11-06 00:11:00 | TERRA_M-M | FELIZ DESERTO | ALAGOAS | Brasil | 2702702 | 27 | 33 | nan | nan | nan | Mata Atlântica | 32.3 |
| 7323c553-26b1-37ce-ba74-ad8504d6214d | -12.36386 | -41.36399 | 2025-11-06 00:11:00 | TERRA_M-M | LENÇÓIS | BAHIA | Brasil | 2919306 | 29 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 9498aa88-1d0c-39c4-a9a9-f8ffca0d62c0 | -5.59919 | -42.80861 | 2025-11-06 00:13:00 | TERRA_M-M | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 18.9 |
| ec0a2a64-9644-3993-b0db-3fe4215dd94c | -8.49715 | -44.73264 | 2025-11-06 00:13:00 | TERRA_M-M | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 776d2023-d8c2-3d01-b49d-2e7c160fab02 | -4.72224 | -46.42297 | 2025-11-06 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 16.0 |
| c1d5afe1-ee17-3ca4-bdf5-63595e18a264 | -4.98259 | -48.48373 | 2025-11-06 00:13:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 0d66f7cb-b1a3-34b8-a187-767b27d4d8c7 | -5.3104 | -41.04002 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 13.0 |
| d7376233-65b6-3988-82ec-00ef6e65ecff | -7.49255 | -44.53605 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 307.7 |
| 2fd65798-eafd-3006-a1d8-97bd91c247ee | -7.4837 | -44.53732 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 378.1 |
| f0bff543-076f-3754-aa03-51496aacd32b | -5.29842 | -47.13332 | 2025-11-06 00:13:00 | TERRA_M-M | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 44005f8f-40da-3c25-ad71-bba6e4943279 | -4.60742 | -43.33924 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| c1e57950-48cf-3c45-b342-5b6179840d9d | -6.13894 | -42.64994 | 2025-11-06 00:13:00 | TERRA_M-M | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2e67ba41-6ea9-37e2-ba22-0f5a276de43a | -7.09212 | -45.5065 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 43f0afd6-3f70-3112-84b8-e3f37c446047 | -5.77036 | -40.81292 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 18.6 |
| f01bc518-3cf2-3c2e-87d4-01878d409643 | -5.35339 | -44.92426 | 2025-11-06 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0dddbd10-6848-39a1-a7a3-1e57cdce3739 | -6.28737 | -44.74258 | 2025-11-06 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 7b3f6203-17fe-317d-810f-6c555d9e1074 | -5.7902 | -40.79545 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.5 |
| fe6969ab-4216-380e-9da7-f6734483e0c6 | -10.06769 | -42.74344 | 2025-11-06 00:13:00 | TERRA_M-M | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 8.4 |
| b0a9dfc8-7798-31c6-8748-687442cfb34e | -7.92505 | -44.33462 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 22.6 |
| d98547e3-2b50-3752-96f4-8bca6139b641 | -7.26962 | -46.0633 | 2025-11-06 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| a4439d5a-ccbe-3b07-b643-68747dab4185 | -4.57783 | -43.33324 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 33.8 |
| 228746af-84da-3f3b-9c1f-739e0badaa0a | -5.93273 | -41.36608 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.8 |
| 00ab1f2d-a2ad-34bf-a400-1ab1e405d427 | -4.85954 | -40.63934 | 2025-11-06 00:13:00 | TERRA_M-M | IPAPORANGA | CEARÁ | Brasil | 2305654 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| eeab5a25-3290-3230-9e07-6c478caf0324 | -4.72176 | -45.88093 | 2025-11-06 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 0a289233-91c5-3568-b804-bb23780b4b72 | -4.46035 | -43.2223 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 113.3 |
| 30489163-72f2-3196-8541-dabda8922d56 | -6.96978 | -46.22546 | 2025-11-06 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 37c25856-ed57-31c8-85a4-39f934461abc | -4.78555 | -45.14072 | 2025-11-06 00:13:00 | TERRA_M-M | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | 40.8 |
| e20c8176-56e5-38f2-bc13-446866ae8e83 | -6.99623 | -38.06247 | 2025-11-06 00:13:00 | TERRA_M-M | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 5ce41729-829f-3eb5-bfd9-51ee2d9793c3 | -4.64808 | -45.7537 | 2025-11-06 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 10.7 |
| f3dbfbc3-01d8-3bfe-9a68-bda897bc1ce4 | -5.7923 | -40.80989 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 16.6 |
| fcf02720-2a8a-376f-8add-ceee391ead28 | -4.9811 | -48.47256 | 2025-11-06 00:13:00 | TERRA_M-M | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 32fe6228-6ab5-3080-b902-e3094d786f60 | -5.07119 | -41.21616 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| f204c038-4367-3b41-9725-1e54518a64e6 | -7.5554 | -45.85973 | 2025-11-06 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 4df3c421-a0b4-37d6-b88e-7190382d9f00 | -4.69484 | -46.55586 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 28674ff9-737a-3ffa-aca7-9d1e9273b7af | -4.70904 | -46.52621 | 2025-11-06 00:13:00 | TERRA_M-M | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 119.4 |
| 37f399e7-1696-35f0-9c44-0cb60d626ba2 | -5.86001 | -43.99957 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 15.0 |
| e169caf2-8e9a-3e2c-8a6b-2e4688b5a63f | -7.93267 | -44.32442 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 9102932d-5253-31a6-990a-d8c6a97695cf | -5.17951 | -44.93401 | 2025-11-06 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ecaf86aa-6e83-31db-a0f3-701342d9e090 | -5.89817 | -46.40156 | 2025-11-06 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 5fccf02a-646b-320a-8d7a-dfdaa9887a9c | -7.18805 | -38.37075 | 2025-11-06 00:13:00 | TERRA_M-M | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 13.7 |
| 8547d8f0-aa9d-3c99-9111-1d7d7aa70d21 | -5.14499 | -41.24028 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 35.1 |
| a40ee6b2-8d42-3ccc-98e2-ff73e406cb1e | -7.18708 | -38.35493 | 2025-11-06 00:13:00 | TERRA_M-M | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 9a2373c1-3384-3d65-8ad4-59c4df152a94 | -4.81648 | -45.57405 | 2025-11-06 00:13:00 | TERRA_M-M | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 37f2c4c8-61aa-364d-827f-bda93f256e56 | -5.37374 | -44.73407 | 2025-11-06 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d5a678bf-524e-366a-8337-4666cc694e38 | -4.42797 | -43.77791 | 2025-11-06 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| cde72908-43eb-3c56-aa1b-2806c63a84b0 | -4.98253 | -45.03742 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 3b677ccf-a70a-3b68-8547-d1858bc66423 | -7.72429 | -45.8145 | 2025-11-06 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 5ecd2bed-de26-362a-b0cb-b68ee105679d | -4.64332 | -46.3208 | 2025-11-06 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 9b4993be-2b7a-3da7-8a1b-650df7f94db2 | -5.09303 | -45.42982 | 2025-11-06 00:13:00 | TERRA_M-M | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 917c660c-1095-30ec-beb4-b5a11582a9af | -5.15772 | -41.25233 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 11.8 |
| 079e8410-c2f1-33d6-8f73-06e716b8d79c | -6.5123 | -42.88595 | 2025-11-06 00:13:00 | TERRA_M-M | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 76a680d5-4aee-32cc-89f8-bf710d4833aa | -6.18918 | -41.64507 | 2025-11-06 00:13:00 | TERRA_M-M | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 7636fce1-d640-391c-a0c5-cf0164421257 | -4.46981 | -43.22093 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| cd4dbc95-1c4c-361c-9384-f7914c1f4288 | -5.14896 | -41.26692 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 87.4 |
| edcdc074-1c95-3efc-9396-220dc467383d | -4.67808 | -42.09377 | 2025-11-06 00:13:00 | TERRA_M-M | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1abfa3c8-a7e3-318a-844d-91e4251a84fa | -9.45128 | -40.65458 | 2025-11-06 00:13:00 | TERRA_M-M | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 8d7ff932-b1df-3464-93b6-aed47fb99261 | -6.19888 | -43.27104 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 1b96a718-d058-3fa2-a505-24301c064428 | -5.77446 | -40.84083 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 4ae2b70a-0dc2-3181-9e4b-8ab0b4be7877 | -7.47733 | -44.55636 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 50.4 |
| 96c2346c-63de-3f55-a56f-ddef9fe58566 | -4.65195 | -44.51908 | 2025-11-06 00:13:00 | TERRA_M-M | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ffbf3221-bc59-3fb1-938d-0e5a189055e3 | -4.58865 | -43.34197 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 188.8 |
| 9fd3447b-b299-3c09-995f-464daef4e566 | -5.42658 | -40.66814 | 2025-11-06 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 44.4 |
| 597bc453-3c08-3cfd-b504-a096e7e17aa1 | -8.24226 | -44.49755 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 4ea002ef-84f6-3d35-b60d-a47c246d8665 | -4.59522 | -43.32051 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95d64a15-d38a-3ebf-8a44-f17103f9c3c1 | -5.76134 | -40.82767 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 27.4 |
| afe12182-8626-3ae7-b409-de252b037cb2 | -5.53601 | -46.51374 | 2025-11-06 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 866511b9-214f-3193-8989-2e94cf1629f7 | -5.3181 | -44.33819 | 2025-11-06 00:13:00 | TERRA_M-M | GRAÇA ARANHA | MARANHÃO | Brasil | 2104701 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 88fbdeec-207e-3e3c-a265-e25f2f47bb75 | -5.48345 | -45.4582 | 2025-11-06 00:13:00 | TERRA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 640ada5d-7d25-329c-928b-05a1a189fe58 | -4.60223 | -43.37061 | 2025-11-06 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 7bf9e429-89f8-3a84-897f-494488d62ae9 | -5.93068 | -43.52625 | 2025-11-06 00:13:00 | TERRA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| d511f13c-7ad7-318c-95c8-5293420724f9 | -5.47185 | -47.72857 | 2025-11-06 00:13:00 | TERRA_M-M | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 30.5 |
| 814e1532-3503-3998-bba7-29f3a08afdd2 | -5.77245 | -40.82716 | 2025-11-06 00:13:00 | TERRA_M-M | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 18.7 |
| 383e2fd3-3be6-3270-993c-c1f5bb9a0005 | -4.81948 | -43.53871 | 2025-11-06 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 90fba124-b5e9-38d6-9b0f-5ebc892c7635 | -7.12788 | -45.35966 | 2025-11-06 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| d77425d9-ecb4-3707-8220-3651e8eb0634 | -7.28643 | -45.44868 | 2025-11-06 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 81c38d45-4f81-3a73-bf41-f3cc7cd9cec7 | -6.01406 | -46.17582 | 2025-11-06 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 15.4 |
| ba23b6ff-dbda-389f-95c1-7d68f0241080 | -4.9855 | -45.52901 | 2025-11-06 00:13:00 | TERRA_M-M | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| bde03c00-cf6a-3a6a-856b-5b0289f314e8 | -7.91619 | -44.3359 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.5 |
| cdfd4547-a9e9-3670-a2e4-510d9438fd96 | -8.2689 | -44.35157 | 2025-11-06 00:13:00 | TERRA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| bf5fd3e6-b55e-3829-826e-fd7176a75649 | -4.92558 | -43.18644 | 2025-11-06 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2d9f7634-99c4-3337-a06e-d760a5f32af0 | -4.92702 | -43.1966 | 2025-11-06 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 39c4a741-2b7b-3aa3-8384-894543504e19 | -4.80306 | -45.7376 | 2025-11-06 00:13:00 | TERRA_M-M | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fb619594-40da-3396-8d63-e25dc1a536a6 | -6.47498 | -39.11829 | 2025-11-06 00:13:00 | TERRA_M-M | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 21.8 |
| 35ec0e87-04e0-3d7a-9bb3-0257932d7bde | -7.9263 | -44.34354 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 7585ffdb-e6bc-3d41-9bc2-bc6ed8ef854f | -7.18467 | -38.34949 | 2025-11-06 00:13:00 | TERRA_M-M | SERRA GRANDE | PARAÍBA | Brasil | 2515708 | 25 | 33 | nan | nan | nan | Caatinga | 34.2 |
| ef6ed42c-98cd-3012-9707-18bb18682b25 | -7.49379 | -44.54493 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 87f72fa5-72e9-33da-a510-59a4833dac0b | -4.96905 | -44.34744 | 2025-11-06 00:13:00 | TERRA_M-M | DOM PEDRO | MARANHÃO | Brasil | 2103802 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 6d2ae973-ae23-3beb-99ba-aaa68b3e1fc2 | -7.31087 | -45.28533 | 2025-11-06 00:13:00 | TERRA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 737e3bc8-8721-36e5-b667-8328b841ca64 | -6.1336 | -42.18076 | 2025-11-06 00:13:00 | TERRA_M-M | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 3ee8845e-2d76-34be-aac1-67f586eaac6f | -5.27335 | -44.41518 | 2025-11-06 00:13:00 | TERRA_M-M | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 572e0ad3-cc89-3feb-8dfd-903884dc0394 | -6.07606 | -43.25554 | 2025-11-06 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7339d604-9198-31ba-9769-b98344994ae4 | -4.72348 | -46.43201 | 2025-11-06 00:13:00 | TERRA_M-M | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7f98ca2b-bf8e-37ca-8814-9622aa4f8a56 | -6.0128 | -46.16674 | 2025-11-06 00:13:00 | TERRA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 523f8ab8-2d50-3ceb-9ce6-ce66fba54598 | -7.91744 | -44.34481 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 57cefb6e-05c1-3b68-9b01-b743d1e9d7a6 | -6.96854 | -46.21633 | 2025-11-06 00:13:00 | TERRA_M-M | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 008d8a42-73da-3bb4-a267-4c91979895ff | -7.91869 | -44.35373 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1ea06369-d774-3467-8fb2-cd83c25705e2 | -5.14146 | -41.24744 | 2025-11-06 00:13:00 | TERRA_M-M | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 20.2 |
| f15f3d58-13ad-3046-9795-9cd4a5292bed | -7.48494 | -44.5462 | 2025-11-06 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 14.2 |


[Clique aqui para ver as próximas entradas](README3.md)
