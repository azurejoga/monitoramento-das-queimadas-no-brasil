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

## Dados Diários - Página 25

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1df2145c-33b9-3da8-a5a2-3eb9a0a19334 | -8.27491 | -47.53897 | 2025-08-22 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae189e06-fc6a-3c80-ad5b-d543206ec15c | -6.29191 | -43.89285 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4962ac2f-1adc-3b17-a27b-012de1019205 | -6.43529 | -44.51698 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4f9135c1-82cb-3a4c-87d2-b904d757f67b | -6.3443 | -43.42258 | 2025-08-22 04:19:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 907720b0-57fb-3d10-a5e4-c2115d3b7723 | -6.03019 | -44.37165 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cf63116d-5aeb-3c54-8306-e3ba193154ac | -6.0335 | -44.37217 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 63652baf-32f5-3e07-91cc-edfe81dca26b | -6.28368 | -43.72613 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a66d3050-d029-394a-9dfc-8c7b58adcf0d | -6.57608 | -44.72369 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0ab974ee-265d-3a0f-9cbc-67a54afd8469 | -5.86202 | -45.66872 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fd4fb004-2988-3dc7-b256-cd6493b49ef5 | -6.26179 | -53.69025 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 08907f38-b970-361f-b2f9-0d1ae2a6e288 | -7.29629 | -46.031 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ec3e3e36-f0c7-35c0-8522-8189340892b3 | -9.83237 | -45.95654 | 2025-08-22 04:19:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b5dc5f6-044b-3f2a-9cb4-3a8f0fd1be48 | -7.4715 | -44.4491 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 18bae7fa-65a3-3849-8cab-01ed0e2ba83f | -7.62103 | -46.2472 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 66f2bb6b-dff4-39b0-ad65-179d9aa7c55b | -12.58728 | -47.0884 | 2025-08-22 04:19:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4381656e-312c-3228-8556-b0d5d8183e01 | -11.43228 | -47.31629 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f615379c-a92e-38b4-9c74-f07e7b940439 | -6.98658 | -44.14069 | 2025-08-22 04:19:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13cd660b-f4c0-3b16-b9b9-83de351ec9d7 | -6.45743 | -44.57008 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7a0ec0bb-52c3-3225-91f6-445326a101e0 | -9.58768 | -55.35252 | 2025-08-22 04:19:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2738a9a1-24df-3413-a007-17877e37a91e | -6.02303 | -44.37407 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 59dad096-5321-3297-bd62-62771bf5bc2a | -6.26825 | -53.68437 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7932558-52ca-331f-be4e-a6e9cdb3f5b7 | -7.87117 | -46.99657 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 488e24d4-a6a8-3320-83b9-f6520256cae4 | -10.43943 | -47.6398 | 2025-08-22 04:19:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4eab71ea-b019-3171-b345-98357890bd06 | -5.66009 | -43.44141 | 2025-08-22 04:19:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 998a9dd8-f491-3c38-95cb-bd06fd34cb76 | -8.50238 | -44.74076 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 20598ba4-ba87-33fe-96ee-035c21ff61cf | -6.03899 | -44.35885 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0b92aca6-6895-3446-b644-5527c6853dde | -7.46764 | -44.45208 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65ee6328-2c5b-3c27-b42d-724cce901ad6 | -11.13075 | -44.70696 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 75282f51-1fe9-34c5-b801-1b5d0e532350 | -8.90029 | -47.33379 | 2025-08-22 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ada9ac9f-13f2-3228-86be-bfc8f98ee677 | -8.90372 | -47.33435 | 2025-08-22 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1214ed39-b10f-3089-9fcd-eef4ba2f0eef | -6.00642 | -44.13371 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7325e67d-e0f5-33b1-9831-a1e38ec4d182 | -6.01508 | -42.85278 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dfca4470-4f56-3f8c-ba21-f7febf0db40a | -10.73555 | -48.23216 | 2025-08-22 04:19:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ef2c3a86-3619-3da3-9090-595b473e1709 | -4.5525 | -55.96867 | 2025-08-22 04:19:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 45ae0cbf-e46b-3aa1-9dd1-2e22091d949f | -6.50953 | -44.58571 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7c4f87e6-92e7-32c8-ad4e-b3e3c3bdba1b | -7.6215 | -46.26558 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d0a32619-7a47-3b56-a0ff-4d30a178529b | -7.04015 | -44.62322 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f883fa07-0c53-348f-a9b7-77ef83915000 | -11.30086 | -44.92445 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9a15eb56-3793-3df3-85b0-a68a137845b4 | -7.27354 | -43.66756 | 2025-08-22 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57ea7b54-9fdd-338c-951a-70742caa6175 | -7.60499 | -44.37741 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a6ff9766-8b05-3b3c-b3fb-0a12013e2ff4 | -7.2523 | -44.69964 | 2025-08-22 04:19:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f69e60aa-5d53-3da9-9d08-8565e934e416 | -9.20374 | -59.46598 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1fff91b0-889c-33ba-83c1-cd448d51073e | -7.22443 | -45.17775 | 2025-08-22 04:19:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1c408a29-dd06-37c1-ae69-2694eaf35f80 | -6.43929 | -53.38895 | 2025-08-22 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3da88223-1de3-331e-b298-f4771ff03d99 | -11.28113 | -44.94716 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f7a6be63-84c7-3d16-9262-a644137200c6 | -7.86555 | -46.98798 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 803e0030-d59d-3fc2-b0a8-a58c41e3c762 | -6.10039 | -44.35817 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e62870c2-29e6-3695-9475-8d969f9631e2 | -6.29911 | -43.89042 | 2025-08-22 04:19:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 95041fff-acd2-3db4-a4a9-98f4aaab2d69 | -6.06159 | -44.10676 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f5e1fe61-c58c-39c3-a694-28b3797d1ef2 | -6.02195 | -44.38099 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cdab5dec-487c-3b66-8fca-764588913b30 | -6.58611 | -46.89629 | 2025-08-22 04:19:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51804591-0ffd-330c-b6b9-3ca242a01e22 | -5.52723 | -46.41668 | 2025-08-22 04:19:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5f35331c-11a0-3d5b-88e8-7b2450a3016b | -9.26968 | -50.25309 | 2025-08-22 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2ec4fc37-94fe-3b2c-a10a-cd5cbd2bfd71 | -7.62265 | -46.25848 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 915aba55-5462-3874-9e73-63376f7f30d2 | -11.2828 | -44.95838 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| f09a5640-70a1-3238-8d52-f72d4b847468 | -6.01148 | -44.38287 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e9cf9eed-6ed9-3fa4-9b6e-0120f167c15c | -6.28423 | -43.7226 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2512dd43-7a19-3cbe-a4a6-110ddedbe925 | -9.15493 | -59.59794 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 57c63277-05bc-3455-b7a5-cc059b96c45a | -6.03552 | -42.83343 | 2025-08-22 04:19:00 | NOAA-20 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f51a3289-c56e-3eb3-9789-b8ba5c224168 | -6.01027 | -44.13075 | 2025-08-22 04:19:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 043efa4e-585f-3dda-a2fe-530401b22042 | -6.86288 | -44.41088 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eb77818a-6de9-3aa6-91a8-4a2a10c6c227 | -10.98502 | -45.60427 | 2025-08-22 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 75c78f93-8d44-31b7-a8c2-0a04ec610512 | -6.25391 | -43.72516 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0badaf5a-ae0c-3d65-9745-f71971ddbdba | -11.30702 | -44.9511 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 01ed7a29-168f-3b90-9891-190e715760b4 | -6.29247 | -43.69145 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8174a326-ab96-3f08-ba70-4da8fe520d0a | -7.86714 | -46.99977 | 2025-08-22 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1fdc78cc-341c-35f9-95fc-8b0d55eea89e | -12.09386 | -43.3405 | 2025-08-22 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ec48bd6e-92a7-3a8d-80d8-203e94c1b624 | -6.41745 | -44.6735 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| da66daf9-558c-3c9c-bd82-9e4bd7e28dc2 | -12.52697 | -45.59955 | 2025-08-22 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a71db229-9652-3456-a20d-ef7f07be75f9 | -10.73515 | -48.25639 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5cda16bf-88a6-31d5-bc9f-cd85a3949e7a | -6.04121 | -44.36629 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ccb0ec85-b04a-315f-a1cd-dd297125c2e9 | -6.03793 | -46.12027 | 2025-08-22 04:19:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| eaa15729-08d5-3835-a46b-745b5a2375c1 | -6.37088 | -43.25006 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc9d77d2-3a12-3703-8321-f12842e6299d | -6.84854 | -44.41575 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2d5ed6ab-15a0-3848-a807-6a9eab3a1cf8 | -7.03516 | -44.61177 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cdfebe36-1f08-3205-92c7-14a6601015ff | -11.31424 | -44.94858 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a3def182-1a22-3f36-aab9-1a4b675f1550 | -9.47399 | -57.82924 | 2025-08-22 04:19:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 281d6e53-89c9-3591-994b-5f01976f8f73 | -6.73533 | -43.13379 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7f9ef378-2e5f-31b8-b536-abff6072bba7 | -7.03906 | -44.63017 | 2025-08-22 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f8f33450-87fe-3f23-8f11-cb0356e827fa | -6.50679 | -45.52638 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7bf47616-c9c8-391f-b45a-daea7544bf04 | -7.26963 | -43.67062 | 2025-08-22 04:19:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9b9a26d5-d260-33ff-9a32-83feb3b5f891 | -6.11259 | -44.38846 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| baad2cf0-84be-35a3-9ba6-c3e8d5571b2b | -7.65185 | -46.22659 | 2025-08-22 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f619c8a6-fb36-32de-b1a7-e0fba2b7aa4d | -10.71175 | -48.22416 | 2025-08-22 04:19:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0e9dea02-1f62-3282-83c7-2847bba0c82b | -7.45997 | -44.4586 | 2025-08-22 04:19:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1e02f971-2728-3c67-893c-4eeba0c5af88 | -5.77637 | -43.71577 | 2025-08-22 04:19:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 737430d7-1550-3060-b907-0b4e9b082bd8 | -8.90434 | -47.33059 | 2025-08-22 04:19:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5dc1e0c7-ccb8-33c6-a388-4f14f02e08aa | -6.56786 | -42.99264 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cf668c85-f5f0-37ba-bccf-e00b9370497f | -9.06413 | -48.56627 | 2025-08-22 04:19:00 | NOAA-20 | FORTALEZA DO TABOCÃO | TOCANTINS | Brasil | 1708254 | 17 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23be26e5-b2c6-3f9b-856f-fee3296e7ca2 | -11.1341 | -44.7075 | 2025-08-22 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 305a940f-9997-301b-a5ed-9af892145589 | -7.65518 | -45.24627 | 2025-08-22 04:19:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 572a5db7-0651-3b63-b8a9-9364f37ab1ce | -11.44414 | -47.30709 | 2025-08-22 04:19:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b6994315-7371-30ec-8212-db3398afcb0e | -9.15263 | -59.59859 | 2025-08-22 04:19:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2b4dd63f-5673-3e81-b2b5-af308f107a3a | -7.14079 | -44.17558 | 2025-08-22 04:19:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6aa611f5-e312-3eb4-833e-1e6c454ecd0a | -6.42738 | -44.67506 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 469833b3-e36b-3df3-952a-188083eb9af6 | -5.79612 | -44.7594 | 2025-08-22 04:19:00 | NOAA-20 | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f1527224-64bc-3cae-ac29-565ab227bdd3 | -6.49852 | -42.96687 | 2025-08-22 04:19:00 | NOAA-20 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7062799f-d07b-381e-a02e-0178d0d61657 | -6.21072 | -43.5627 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 49d740ca-aafa-3308-9026-f80bfe8a811e | -6.4342 | -44.52389 | 2025-08-22 04:19:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d2497765-1157-39f2-b5d3-9a99b59feb96 | -6.29192 | -43.69498 | 2025-08-22 04:19:00 | NOAA-20 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README26.md)
