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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 954038cf-d4f6-3f90-9cb1-6a5aeb1fb08a | -14.08238 | -44.16217 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ad5b203c-a3b8-3fc1-8f95-d4b2f5d26f72 | -6.36682 | -40.9726 | 2025-10-31 03:47:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 2bafb917-6457-3f76-9137-71c037f39eef | -7.37638 | -46.22519 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4793c72c-306f-3a31-8532-5f444e493d22 | -10.88764 | -44.31514 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 37cd15f7-831a-35cc-996f-a470670c0b31 | -10.94709 | -44.63161 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e480d16d-acba-32ca-85b7-8794d732170d | -5.31512 | -44.83762 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c9728b5-07be-35aa-a3eb-baebbc1679bc | -8.51382 | -39.64326 | 2025-10-31 03:47:00 | NPP-375D | SANTA MARIA DA BOA VISTA | PERNAMBUCO | Brasil | 2612604 | 26 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 016b73fb-e787-3a0b-8c2c-f8ee8c325cee | -10.8842 | -44.36094 | 2025-10-31 03:47:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d1027c81-0d84-3bac-b729-f68eea152ab9 | -5.71226 | -44.53543 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05a5f4cd-8968-338a-9b9b-2076d1f92672 | -8.16615 | -45.50906 | 2025-10-31 03:47:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| cfc4979a-3a40-3418-90e6-a04cbed29951 | -6.21903 | -43.94021 | 2025-10-31 03:47:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 4704fd36-ca3a-3487-a3da-103462c709f5 | -5.46344 | -40.87369 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| af6d7924-ad25-3eb8-919c-3d0fba6bafa0 | -5.79305 | -43.73486 | 2025-10-31 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3774920f-554d-3a0c-8b25-b655ee5b55b1 | -9.51979 | -47.27031 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e7dec649-8fc2-36ec-9c7c-55b36464bc30 | -13.88931 | -47.34161 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 12fbf65f-adf6-37e5-a07c-53a15e533eab | -3.93647 | -46.97343 | 2025-10-31 03:47:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7d21c671-d87b-372a-aaf2-865353c74d04 | -5.36678 | -45.5257 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ebb0062b-c638-3aac-b573-55bb6a24f619 | -10.84385 | -44.92707 | 2025-10-31 03:47:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 046f0942-d608-370b-96c0-fd0264ccb66a | -6.22953 | -37.4221 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOSÉ DO BREJO DO CRUZ | PARAÍBA | Brasil | 2514651 | 25 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 8379078d-5bfd-3250-b98a-3936ce953508 | -7.74816 | -34.91409 | 2025-10-31 03:47:00 | NPP-375D | ITAPISSUMA | PERNAMBUCO | Brasil | 2607752 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 2e638b04-b02c-3e25-8992-b154e93fe18f | -6.01534 | -41.9651 | 2025-10-31 03:47:00 | NPP-375D | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 5fa94bf4-cce9-3aa0-999a-3fd024fc3097 | -14.07869 | -44.15644 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 15d73e0b-479d-3789-8b29-32e1d7d73b57 | -16.36488 | -45.25177 | 2025-10-31 03:47:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 31846fb4-b31f-33b0-ba3b-5103c8ca2dcd | -13.68324 | -44.71327 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 414c2517-5eb3-350d-8c70-278b45f42cd9 | -12.93327 | -47.92871 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 87ccfb0a-10fc-338d-a721-a73dc77c4abf | -7.08232 | -44.93385 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 7.4 |
| 0d20090a-76eb-3ef9-a4f8-fc9c23936faa | -3.98712 | -43.42591 | 2025-10-31 03:47:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bb0986a3-b072-39c9-a5dc-72ffb1537bd8 | -14.16593 | -44.34336 | 2025-10-31 03:47:00 | NPP-375D | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 774ef25d-8380-3771-9b29-956a57b96e71 | -4.90741 | -45.72523 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 17899bfb-a5d2-3ddb-9a88-d9bbf48f4403 | -4.56072 | -45.64967 | 2025-10-31 03:47:00 | NPP-375D | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b9dc7a35-7f09-38a0-8fbc-19d3e92b89ec | -5.03343 | -43.618 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| d6e53f9a-980d-3d35-95b3-c90ee5400d23 | -13.53583 | -47.42902 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbf3ca0c-8b72-370c-98a0-27e0fc7672b2 | -5.02012 | -45.57215 | 2025-10-31 03:47:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5e2172e-e1fc-3e36-83fa-d184c7551ecc | -6.92731 | -42.25076 | 2025-10-31 03:47:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 55b0bd03-e982-308a-95dc-69225e12475c | -8.85883 | -41.44422 | 2025-10-31 03:47:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3ead3427-da66-3a5e-8dce-b90fe7a5fb15 | -8.09519 | -45.14925 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 0b33bad3-9759-35f5-a20d-323fa516278a | -12.94033 | -47.93144 | 2025-10-31 03:47:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 7fcb3ca5-141e-328e-8652-8173afa108eb | -9.93557 | -44.90614 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2c5d4cf9-8fa6-30ff-a3c0-2df954a6f86f | -10.27729 | -44.55512 | 2025-10-31 03:47:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2a0954d9-79ca-3e43-a7d4-4384ff717b43 | -4.79701 | -46.4632 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2a28e1ef-7f43-323c-8eb0-924180044d83 | -5.23318 | -45.47263 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 695f4626-0741-385c-a6dc-7f004347d7ef | -6.53171 | -43.71535 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 37809575-fa23-3876-be84-83e8b82e399c | -3.82026 | -45.05459 | 2025-10-31 03:47:00 | NPP-375D | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6ea7154-65b4-3994-a16f-4d2409c02aba | -5.13316 | -40.62776 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 52fcc717-df92-3b85-bc83-e07fef3d493d | -5.2834 | -45.42591 | 2025-10-31 03:47:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7022e4c5-1be8-3c35-ad35-1216286754f6 | -4.67461 | -46.42463 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e743e2b9-e32c-30df-9fb7-656b11e4a118 | -9.92916 | -44.91166 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95baa649-dd39-3643-bd97-c4b441f1016c | -13.68331 | -44.73296 | 2025-10-31 03:47:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 22.1 |
| bc98dcd4-1aa9-3674-a905-0b9335b86328 | -7.34673 | -45.00366 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 257f94d9-e081-316d-9aff-afd73f54a78a | -11.36244 | -42.292 | 2025-10-31 03:47:00 | NPP-375D | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| b219ba96-9664-3ccb-97c9-b2478c578fdc | -13.80804 | -47.0645 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 57f2f555-c848-3625-aa08-228de34968e5 | -13.89977 | -47.34833 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4b93666-d5d8-3b0e-ad74-fd81796d0954 | -4.8002 | -46.46516 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 01814fcf-ce1c-36f7-a274-9d7933aedf51 | -3.48114 | -46.02276 | 2025-10-31 03:47:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf49ea49-6fdd-3cf3-8004-94ff2fa2948d | -4.57215 | -38.28391 | 2025-10-31 03:47:00 | NPP-375D | MORADA NOVA | CEARÁ | Brasil | 2308708 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c3bc3007-7e69-3b9c-b60e-a569f3491fdb | -8.10045 | -45.18191 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ce8c3dc-1f9e-333e-ab7d-a463b4d4ae14 | -5.40521 | -43.11768 | 2025-10-31 03:47:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7ea84f50-fb87-3984-bfbe-77460addcaaa | -15.40249 | -41.81945 | 2025-10-31 03:47:00 | NPP-375D | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f063f8cf-5e7a-3659-9211-80e52cca4975 | -5.41529 | -41.23977 | 2025-10-31 03:47:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 16fdc222-217d-3979-85ef-019e453fb8c1 | -6.81156 | -44.45239 | 2025-10-31 03:47:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d6c69ecf-1897-3653-b2d2-b785c2465b1e | -9.93437 | -44.91257 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 645db74c-6cf1-3bcf-af1c-8d9945626f61 | -5.03917 | -43.61567 | 2025-10-31 03:47:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 24.6 |
| ecafd472-7421-331f-b20c-e85cd78d7919 | -9.85911 | -44.85429 | 2025-10-31 03:47:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 63c0f788-d43d-3fa2-acca-38304c796474 | -5.45494 | -40.87194 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| a3b7771a-37c9-320d-9590-9629cc7dce23 | -14.0016 | -44.01422 | 2025-10-31 03:47:00 | NPP-375D | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 012cb7bc-2183-38fd-bc05-9ed14f7eeb95 | -4.79932 | -46.47008 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d04fdee8-2d32-36a8-88b6-dba39ae5791d | -7.93517 | -42.23259 | 2025-10-31 03:47:00 | NPP-375D | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 730729d3-d174-312e-b1b9-34b8dbb41a7f | -7.08189 | -44.93805 | 2025-10-31 03:47:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 88e57f63-ed27-30e8-8f33-af08ea669667 | -8.10172 | -45.17513 | 2025-10-31 03:47:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 11503933-e9fd-33d7-a1e1-6c500a757d46 | -8.925 | -37.28454 | 2025-10-31 03:47:00 | NPP-375D | ITAÍBA | PERNAMBUCO | Brasil | 2607505 | 26 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 2b12a7c8-ea14-3520-9b64-8588acd91405 | -5.80343 | -40.83258 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 9fe62806-a545-312e-b6f5-d65ffea63e8a | -5.61484 | -45.97979 | 2025-10-31 03:47:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4e55fbb9-ef27-3372-9128-f76996840eea | -4.05283 | -47.50147 | 2025-10-31 03:47:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 4cf277f2-6fc3-393d-8108-23531257e11e | -13.82567 | -47.06346 | 2025-10-31 03:47:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa99045d-af77-3cc3-8bb8-2aa25c78df68 | -5.4109 | -41.23904 | 2025-10-31 03:47:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| e2e820f8-b664-32bd-8ab2-b7b77f178e73 | -4.90666 | -45.72943 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f092ca81-d065-3f96-a08a-e077a6d867dc | -13.38601 | -47.34373 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| db36aac1-a12a-3071-b42e-d570512b1366 | -8.89875 | -37.9653 | 2025-10-31 03:47:00 | NPP-375D | INAJÁ | PERNAMBUCO | Brasil | 2607000 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d3d05c78-006a-3679-8ed3-a7555338d9e3 | -13.7007 | -44.19617 | 2025-10-31 03:47:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5bd5119f-5c82-3c07-8abc-5c1278319849 | -4.47544 | -46.56264 | 2025-10-31 03:47:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 98f50c28-0743-3080-9752-454d2768c916 | -4.90607 | -42.97895 | 2025-10-31 03:47:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 20e1b9a3-7ab9-3242-8fc3-2a667bbf119f | -13.42449 | -47.35955 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 323df398-6a6b-3507-a439-948a770bb541 | -5.31374 | -44.84544 | 2025-10-31 03:47:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 338191f0-19fe-3a07-88f4-eaa2c244298f | -5.21886 | -40.76765 | 2025-10-31 03:47:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 01a44bfd-6973-3880-b9ad-b32b516b8472 | -9.88719 | -47.45768 | 2025-10-31 03:47:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fc01bcee-7259-39ab-8877-01eab9cf8e88 | -4.96044 | -45.88029 | 2025-10-31 03:47:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| c2e8ba54-88b9-35f0-9193-ed0ff144ee2f | -9.38579 | -37.92998 | 2025-10-31 03:47:00 | NPP-375D | DELMIRO GOUVEIA | ALAGOAS | Brasil | 2702405 | 27 | 33 | nan | nan | nan | Caatinga | 0.7 |
| eafc9399-fef3-3c8e-bb56-7ce5853e397c | -4.66832 | -46.42367 | 2025-10-31 03:47:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e727e66-117b-34a4-a12a-d3960894aba7 | -10.28234 | -44.55608 | 2025-10-31 03:47:00 | NPP-375D | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 89431afc-f5cc-35ef-b459-b1e23c8e3ce1 | -7.60905 | -46.47497 | 2025-10-31 03:47:00 | NPP-375D | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 76d2d153-f6a8-31b2-9921-2b60dfdbe61f | -13.70249 | -44.1981 | 2025-10-31 03:47:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| bbe931d2-4d82-31c5-8da4-a8ec68b44ad8 | -5.78732 | -43.73712 | 2025-10-31 03:47:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 05549b3f-5156-3a6e-92ec-af7f6e45fa06 | -6.3672 | -35.19611 | 2025-10-31 03:47:00 | NPP-375D | CANGUARETAMA | RIO GRANDE DO NORTE | Brasil | 2402204 | 24 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f4bcb021-2385-3204-a21a-b91fd8456404 | -3.52777 | -47.5527 | 2025-10-31 03:47:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3fb237b8-9567-31f6-abdd-09b881e793b6 | -6.68885 | -38.19248 | 2025-10-31 03:47:00 | NPP-375D | SOUSA | PARAÍBA | Brasil | 2516201 | 25 | 33 | nan | nan | nan | Caatinga | 5.6 |
| c85f9063-de69-3bce-b8e6-d8c44f80bccc | -7.36078 | -44.63535 | 2025-10-31 03:47:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7e995684-9ddd-32c5-9377-10833b87912d | -5.80403 | -40.82899 | 2025-10-31 03:47:00 | NPP-375D | QUITERIANÓPOLIS | CEARÁ | Brasil | 2311264 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6512251c-e71c-319a-ac6e-44c45ce56dfc | -7.32255 | -42.48587 | 2025-10-31 03:47:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 123e9c7d-0965-3211-80aa-137eab830b71 | -9.73614 | -48.02303 | 2025-10-31 03:47:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d5cd7060-6490-3ecd-a928-c98a7b52849a | -13.62386 | -47.58684 | 2025-10-31 03:47:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README9.md)
