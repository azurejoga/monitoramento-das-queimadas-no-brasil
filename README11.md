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

## Dados Diários - Página 11

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95251fc8-63f2-3768-b3ee-606aefdf13cf | -17.37916 | -42.48363 | 2025-05-23 04:06:00 | NPP-375D | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c41d1ad8-bb7d-3dc3-bb50-cedcfa5bb5dd | -17.67353 | -47.5302 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a65e33b7-fb45-30c7-87a8-3b4662898ff8 | -15.26418 | -51.47883 | 2025-05-23 04:06:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70fd82e7-7497-3ea4-bc4d-54913f51776d | -17.7765 | -42.80656 | 2025-05-23 04:06:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| be99b95f-7ba5-3baf-9424-b4cdc6ff403c | -21.52338 | -49.5159 | 2025-05-23 04:06:00 | NPP-375D | SABINO | SÃO PAULO | Brasil | 3544608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 45d3a1f7-4ff9-321a-b86f-1344dc8dee2f | -17.57861 | -47.48927 | 2025-05-23 04:06:00 | NPP-375D | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8eabace4-77e9-3498-a083-72dd98ff8f35 | -20.10054 | -43.17187 | 2025-05-23 04:06:00 | NPP-375D | ALVINÓPOLIS | MINAS GERAIS | Brasil | 3102308 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 0eaef707-50dc-335d-993c-6d93e43b0c7e | -20.57832 | -44.57452 | 2025-05-23 04:06:00 | NPP-375D | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f59785b0-76a1-336f-8ad8-c90e3a75677e | -19.05795 | -53.458 | 2025-05-23 04:06:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b2ceb46b-337e-308b-9ffb-99da88e45d85 | -20.41336 | -43.55235 | 2025-05-23 04:06:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0e99a738-62e1-37b7-9317-a7c648ac758c | -17.67862 | -46.82379 | 2025-05-23 04:06:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 54aa3bda-b652-326d-8442-e23f6d83b386 | -19.9581 | -45.82767 | 2025-05-23 04:06:00 | NPP-375D | BAMBUÍ | MINAS GERAIS | Brasil | 3105103 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 75694c01-804d-34d1-9f4f-7158483f4f18 | -21.63462 | -49.842 | 2025-05-23 04:06:00 | NPP-375D | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1344ab12-ce69-304e-b398-e4540ceb7d06 | -19.79631 | -53.83898 | 2025-05-23 04:06:00 | NPP-375D | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 09f4cd7a-2e44-3b75-8146-c1df43859e01 | -17.3346 | -51.90018 | 2025-05-23 04:06:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 40de98c8-3b5d-3294-ad2b-d98986d2e0f4 | -21.71602 | -55.36606 | 2025-05-23 04:08:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| ffc56fe2-b430-385a-9f43-58b01b8aff2c | -22.53966 | -48.81564 | 2025-05-23 04:08:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7ad34d76-78ef-3ca3-b9ae-1ee266f54a2a | -21.71497 | -55.37064 | 2025-05-23 04:08:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 11ac133a-b32f-3903-8e41-a084f12af3d1 | -21.71896 | -55.36813 | 2025-05-23 04:08:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| fda0be4b-20e4-3c40-a9d9-233c24c64ba0 | -21.71788 | -55.3727 | 2025-05-23 04:08:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 146e1b9a-333e-3531-97b8-edbd8df5bcc9 | -22.54203 | -48.81498 | 2025-05-23 04:08:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c9243628-f8c7-3108-ac31-cc5bb25bed73 | -21.72379 | -55.37429 | 2025-05-23 04:08:00 | NPP-375D | MARACAJU | MATO GROSSO DO SUL | Brasil | 5005400 | 50 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a43e3129-a8e0-33f0-9efc-5db88bb15f8f | -6.2224 | -43.3693 | 2025-05-23 04:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 63.9 |
| e6157de6-d2b2-317c-a7c1-20785a15e628 | -7.0695 | -44.9335 | 2025-05-23 04:10:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 66.2 |
| baaacc92-4153-3a7f-a7e6-8381cacd6c8b | -13.9818 | -56.0151 | 2025-05-23 04:10:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 6b5c677e-e676-3c16-ac9a-4a7a6512a5ed | -29.77657 | -51.17834 | 2025-05-23 04:10:00 | NPP-375D | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 3.1 |
| ad602eb7-765f-34f4-8a91-f1f15ed26ac4 | -13.9818 | -56.0151 | 2025-05-23 04:20:00 | GOES-19 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 58.0 |
| f014e134-1b4e-3aab-8870-ca129758227b | -7.0695 | -44.9335 | 2025-05-23 04:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 59.4 |
| 9667f81a-872c-38e5-8afb-7d6c149c5917 | -6.2224 | -43.3693 | 2025-05-23 04:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| dc52557b-4a2b-3056-949d-475afe7d3bec | -7.06754 | -44.94033 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aaed7bb8-dd2e-3de6-a85b-dcedc5c48854 | -7.0692 | -44.92959 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32f9af32-eeaf-30fb-95f3-024dd79530a1 | -6.03175 | -44.05028 | 2025-05-23 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d706e9e1-9331-3d7e-b23d-7d66175add3f | -5.76402 | -43.48749 | 2025-05-23 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5faf6c6a-ced6-3993-aebb-3d7f8c475021 | -6.22703 | -43.36686 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 29.5 |
| 02eacc6b-2899-301b-b80a-5968c7f7f67a | -7.06473 | -44.93618 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 7d471724-e482-32b1-9296-cf14318a9287 | -7.35993 | -43.42162 | 2025-05-23 04:23:00 | NOAA-20 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 259347b2-f8bf-3e97-9422-64b266f30930 | -7.19892 | -43.09575 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 097aeff3-c056-3690-b2cd-0622e0c72860 | -5.57866 | -45.19475 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 1991f64c-1fc2-386e-9401-aa9ec59d1bc6 | -6.38748 | -43.66647 | 2025-05-23 04:23:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d1dad3b0-f35e-3299-98e8-2ce9bf67e1b8 | -7.07202 | -44.93373 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8a5bc17a-63d0-30d8-acd3-82d023a42d70 | -5.78342 | -43.61845 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9399eaf3-e73e-32cc-a56d-8d573ce75b79 | -5.76111 | -43.483 | 2025-05-23 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 48ff4a89-ccf0-3a7f-84af-3c1c20959721 | -5.57479 | -45.19773 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 64da05d3-7086-32d3-b474-a6d3bb17f1cc | -6.94125 | -42.79353 | 2025-05-23 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| ad27078a-e127-373f-8d86-36115bb7c439 | -6.22764 | -43.36283 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 453d29c1-922d-3348-b321-0e0d043e82dc | -6.03519 | -44.05081 | 2025-05-23 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4447b51-9cb3-3491-a7c4-5afec7531c8e | -7.65324 | -45.23258 | 2025-05-23 04:23:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 411e3fb9-2525-3614-be7f-ba97e54ba067 | -6.23181 | -43.35931 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| cd2cd1ed-4e2d-3454-a75e-9f677ce8b02f | -6.94864 | -42.79457 | 2025-05-23 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| beef2be5-c8fd-36fe-9bda-78a0200378c2 | -5.76051 | -43.48693 | 2025-05-23 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a4ac2ccc-dcc3-35ae-b4ad-0b2c8a79a07c | -6.22887 | -43.35475 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b15d9ae-8a17-33d5-97ec-f9003549f385 | -7.06246 | -44.92849 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9a5b61f2-6050-3d46-8550-f81125c749dc | -7.20683 | -43.09261 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3ac62abd-a854-3b1a-9c04-5646a92337ba | -5.58145 | -45.19877 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 85f70a3c-dd68-3d36-aa43-65763a8df22b | -6.60406 | -44.785 | 2025-05-23 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ab8b60b-8d0b-3664-9984-a0aa4edeb519 | -4.17356 | -42.03008 | 2025-05-23 04:23:00 | NOAA-20 | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 32a60370-578c-345a-ab45-922188302845 | -6.69435 | -44.15973 | 2025-05-23 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cb0f0d8f-e8a7-311c-8574-f20f0c115522 | -7.20844 | -43.13193 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fdf9e0a8-2375-3d4c-9bbc-aae1a5a5a4ea | -6.22225 | -43.37435 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc098eda-a979-3ccd-bc67-8c33bb14ec6f | -7.06638 | -44.92544 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f510afdf-8529-3cdb-8ae9-a4998265bb49 | -6.2312 | -43.36335 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 3f312c21-01d1-3a0a-9b51-0c04496e5e7b | -7.23843 | -44.71714 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8207ec3-7ed7-35ed-be00-81a467278fbd | -5.57424 | -45.20124 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 7ebc2ee3-92bf-3308-b874-fb75ed905e6b | -5.58199 | -45.19527 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 496308db-a604-3c1d-b1c9-2929960dfcdb | -7.06865 | -44.93318 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 69c24995-9cd2-3066-bffc-28c5daea1fb6 | -6.23476 | -43.36386 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb136a1f-173f-3285-bca6-3f90b3b5f5f7 | -7.06809 | -44.93676 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| db6c7a92-da2e-3ee0-b88d-752537d9e329 | -7.2377 | -43.11037 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 82d50264-5d7e-3b56-9e15-73121cf782ea | -7.57908 | -45.86505 | 2025-05-23 04:23:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e34b0ed3-d559-3ed7-97a4-e1edf12cd421 | -5.75991 | -43.49086 | 2025-05-23 04:23:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9abc8a4d-8972-3f4d-a5e3-fc4fe503c642 | -5.78402 | -43.61456 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c1884347-9e8f-3244-8e70-161fca024c40 | -5.57812 | -45.19825 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| b260ca43-5c63-3e48-9f5a-d24fc80e2120 | -6.60533 | -44.78494 | 2025-05-23 04:23:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c3b43729-e8a0-3ca0-a4c3-d65c2d369236 | -7.21634 | -43.12882 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 79861763-8b56-3f66-b792-835708ef7432 | -6.06902 | -44.23874 | 2025-05-23 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fd777da1-b6d9-39f7-ab23-768068b59733 | -6.22826 | -43.35879 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1641690d-fbda-3bd4-b771-1ba516048925 | -5.9766 | -43.74977 | 2025-05-23 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 4317ba49-f0f8-323a-8ba9-d870a9792f00 | -7.2048 | -43.13138 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1829dba6-ea2a-373f-8549-11479b817efe | -5.78052 | -43.61404 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7dedd6f4-9a7c-3561-af51-b9f6cea69982 | -6.03864 | -44.05134 | 2025-05-23 04:23:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b64e503c-2456-326b-8d2d-6556a2cc500c | -6.9406 | -42.79792 | 2025-05-23 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 7ee92218-6038-3788-8106-85c5cb1f2942 | -7.23559 | -44.71294 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ad04050a-a690-3514-8528-ab469846787b | -6.22423 | -43.33736 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7e8d61e8-f157-3720-8e44-875cce4f3d48 | -7.07146 | -44.93733 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bfd067d9-0a51-3f76-930f-c0b9523bb767 | -7.20746 | -43.08836 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dc8bc44d-30f9-3897-aa1a-5a05186477ac | -7.06528 | -44.93262 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 6a9f7ab0-992c-3ef2-a83b-ce2c25adf7e1 | -6.9456 | -42.78965 | 2025-05-23 04:23:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 42873ad9-49b6-352e-bcdf-0976be083760 | -7.24182 | -44.71767 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8c8547f-55fb-37b8-b840-c204319ea774 | -5.57757 | -45.20176 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1893094e-cb73-38c6-bf6f-cce011b84111 | -7.2127 | -43.12826 | 2025-05-23 04:23:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 9ebd67cd-4683-3e56-93bf-e870c2cd6097 | -7.07428 | -44.94146 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9a5c842c-8e81-33a0-9a1e-dd4c9844be9a | -7.22879 | -44.7119 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e81a11f4-f00d-30a2-86f4-c3e63ae289d4 | -7.22936 | -44.7082 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6d9b83d2-6188-3cde-b017-24669a4469ca | -5.97601 | -43.75363 | 2025-05-23 04:23:00 | NOAA-20 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 9c7cd660-5c37-3d72-8ea6-c33a20a5d272 | -7.06583 | -44.92904 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1525866c-3e93-3da7-bfc8-14e6d177dd07 | -6.22593 | -43.35012 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 94f189c2-cd52-3043-8704-91800915c3e4 | -5.16485 | -45.10559 | 2025-05-23 04:23:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ba4bb5c-5715-3ea2-b899-a5dea849228b | -7.07091 | -44.94091 | 2025-05-23 04:23:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0820eec3-ebbf-3daf-967e-95c839e2701c | -6.22581 | -43.37488 | 2025-05-23 04:23:00 | NOAA-20 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| 2ecc44dd-5b0b-3358-832d-6facfad92ea7 | -6.54286 | -44.02412 | 2025-05-23 04:23:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |


[Clique aqui para ver as próximas entradas](README12.md)
