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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c73251fa-ef87-3ee7-bf8d-d30e13d5b141 | -15.52119 | -50.3796 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1f0f8939-fc44-3098-90b3-bed79c94901b | -19.81752 | -53.08395 | 2025-10-22 04:57:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 29a19215-1a29-3006-a672-78d9927aab62 | -19.08542 | -44.34794 | 2025-10-22 04:57:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 841229a0-550c-3916-a516-8a7f8908971f | -18.16624 | -52.97414 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bda84b02-a286-3827-8695-d320b7ce1188 | -19.86909 | -46.33458 | 2025-10-22 04:57:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 319529c5-7434-3b4e-9c68-9e07cb786a5e | -15.78901 | -52.49147 | 2025-10-22 04:57:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 38c4e479-ecca-35a2-ba3a-f7fc94866d2c | -18.11913 | -54.522 | 2025-10-22 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 90ee2d9e-d3fa-3b1d-aa6a-0597e37ac88e | -16.0978 | -55.417 | 2025-10-22 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ca93c97d-f7df-3b66-91c7-fca701195e76 | -20.14449 | -52.83696 | 2025-10-22 04:57:00 | NPP-375D | ÁGUA CLARA | MATO GROSSO DO SUL | Brasil | 5000203 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f3de3e50-958b-3db0-80a4-f0919a6fab5e | -16.04063 | -54.26588 | 2025-10-22 04:57:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c7f6a5d9-2123-3a3a-8da1-4f9057384b7c | -12.37917 | -63.87811 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 04b95666-91ac-3e47-952f-47fc66b6b1a7 | -19.15263 | -49.12388 | 2025-10-22 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c449175-f204-3ef7-aeaa-7cae5005e794 | -18.11578 | -54.52143 | 2025-10-22 04:57:00 | NPP-375D | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 80e4a74d-6b8a-38ad-a7fc-e8fd024409d0 | -18.57753 | -44.92472 | 2025-10-22 04:57:00 | NPP-375D | FELIXLÂNDIA | MINAS GERAIS | Brasil | 3125705 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6049c6ca-fbff-3475-9429-2a22d25f4846 | -16.04397 | -54.26643 | 2025-10-22 04:57:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8bc105f-cdcc-32e7-9f99-a0b99c8f7c23 | -14.69228 | -48.78673 | 2025-10-22 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8e13d31a-ff83-3cb6-99f5-197ef16d232a | -20.42363 | -55.74387 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 8.2 |
| 4a673e48-7d44-32d7-992f-9315d094b2f9 | -14.22464 | -52.80856 | 2025-10-22 04:57:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4b5f9fe6-bd1c-30ed-b4f7-c965860b0da3 | -16.0412 | -54.26227 | 2025-10-22 04:57:00 | NPP-375D | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c6fa40db-16bf-3399-95c2-3982cbda8256 | -20.42421 | -55.74018 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 89a0dc36-3a8c-30b7-b193-7f9015b1d95b | -14.87512 | -56.2448 | 2025-10-22 04:57:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b73e2093-2eb0-300b-891d-d7e7b42229e5 | -20.98068 | -47.21167 | 2025-10-22 04:57:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 64892753-de63-3022-8e11-dc2637cbbbca | -14.6538 | -53.10419 | 2025-10-22 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c52bc70-4a5c-3105-8c1a-8b983932651d | -19.90748 | -46.11396 | 2025-10-22 04:57:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 317ac213-a7d6-33a9-979b-6daa9c562fd8 | -20.60464 | -55.90347 | 2025-10-22 04:57:00 | NPP-375D | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6df809fa-736b-31c2-a1b0-0c7a7b223eea | -13.84187 | -49.31854 | 2025-10-22 04:57:00 | NPP-375D | AMARALINA | GOIÁS | Brasil | 5200829 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e3f812cf-8c30-391b-a2fe-7cc2586e49fb | -19.90669 | -46.1115 | 2025-10-22 04:57:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9fcc5786-66fb-3a67-854e-7bb8590f0953 | -20.29752 | -46.54515 | 2025-10-22 04:57:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ce6e784f-a48e-3278-928d-420db64231a4 | -12.92698 | -56.60939 | 2025-10-22 04:57:00 | NPP-375D | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 1d162f90-b29c-363b-9cf7-631cc2a73415 | -12.12922 | -63.20904 | 2025-10-22 04:57:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0059e0b3-fc9c-36cb-bc26-857684cf1f85 | -14.78747 | -59.24024 | 2025-10-22 04:57:00 | NPP-375D | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cd7972b-a6b0-3c3c-8fe0-7d58ed4da1e4 | -17.66971 | -54.21853 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8ba0dcfb-5fa4-3539-bcd1-72b24fd39ddb | -20.97552 | -47.21154 | 2025-10-22 04:57:00 | NPP-375D | SANTO ANTÔNIO DA ALEGRIA | SÃO PAULO | Brasil | 3547908 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| acd9212e-3323-3e71-b54c-7ad710d49381 | -18.33806 | -49.50283 | 2025-10-22 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| d2433218-affc-3328-b17c-0537f67aa10a | -17.38068 | -52.0092 | 2025-10-22 04:57:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5b96831c-6ff7-3043-980b-2c61ddb2778a | -18.94964 | -55.07834 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 95edd051-fc6f-336c-a62f-2fb3f7947dd9 | -20.4203 | -55.74328 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 520e8367-4911-330a-a7c3-3661988d00a8 | -18.62734 | -51.65631 | 2025-10-22 04:57:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7fbd655-a570-3a96-b13c-ce00785ee0ea | -19.8717 | -46.33597 | 2025-10-22 04:57:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 33551996-0c2d-3c83-970d-78e6eff4593b | -19.08994 | -57.52138 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 82d4c6bd-3af9-3f50-9601-15a5902bbd19 | -20.30324 | -46.54163 | 2025-10-22 04:57:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0b5188e1-1f4c-31f9-9e85-8e2ac69c63b7 | -22.09071 | -43.27178 | 2025-10-22 04:57:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 9182ced3-6ab1-34eb-a1e2-1d81ee3dfabe | -17.34188 | -55.04049 | 2025-10-22 04:57:00 | NPP-375D | ITIQUIRA | MATO GROSSO | Brasil | 5104609 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 898cb4d7-fae4-3987-b241-362fb9e40bd5 | -17.67085 | -54.21113 | 2025-10-22 04:57:00 | NPP-375D | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 2f0cd7e9-f950-3fc0-8646-321a135341b9 | -22.0902 | -43.27835 | 2025-10-22 04:57:00 | NPP-375D | PARAÍBA DO SUL | RIO DE JANEIRO | Brasil | 3303708 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| e962c2a0-137c-3d2e-86a5-54c2a4a7524b | -18.15225 | -52.97192 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3153432a-e412-3b6a-96df-8e03957f983a | -18.14758 | -52.97942 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1c16564f-ce1d-36b2-b7da-7f0e6079488e | -15.6228 | -48.90848 | 2025-10-22 04:57:00 | NPP-375D | PIRENÓPOLIS | GOIÁS | Brasil | 5217302 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8beb5270-aacb-3942-b975-1cad5e6d9946 | -14.74901 | -54.11483 | 2025-10-22 04:57:00 | NPP-375D | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e866e0f-85a2-34f6-b0ef-7640e02489cf | -18.94573 | -55.08144 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 69bce380-b911-3c1e-8c81-874598355e83 | -14.91389 | -55.81719 | 2025-10-22 04:57:00 | NPP-375D | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4485e1e4-932b-3b94-b156-0c58188646b1 | -14.6572 | -53.10471 | 2025-10-22 04:57:00 | NPP-375D | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4f00f756-54a4-346c-b33b-68c34989d9db | -20.29783 | -46.5422 | 2025-10-22 04:57:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f9937c19-d749-3e7a-bd71-16dfb3883e8e | -15.60241 | -51.00571 | 2025-10-22 04:57:00 | NPP-375D | ITAPIRAPUÃ | GOIÁS | Brasil | 5211008 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 94522ab6-4746-3e14-adb3-e0d184a8b004 | -18.34221 | -49.4985 | 2025-10-22 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 887e5351-895f-35cc-8edb-2bb10f453e2d | -19.15705 | -49.12428 | 2025-10-22 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a668cbb0-a1db-31e0-b3d7-86e58bb84374 | -20.42479 | -55.73649 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 79fe400e-9ea0-3cfa-9710-bced8e524495 | -17.95378 | -57.63984 | 2025-10-22 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 3eae01ff-32b5-351e-b0e3-2ef16d4fafc8 | -19.15598 | -49.13329 | 2025-10-22 04:57:00 | NPP-375D | PRATA | MINAS GERAIS | Brasil | 3152808 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a8cc4a85-3804-37b1-9a28-e1665c66f3dc | -17.20876 | -47.65227 | 2025-10-22 04:57:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e2462155-85be-35cf-aaed-cf08f0db628b | -18.20341 | -52.96605 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e29fe9c-ccef-3370-a769-425ad7fcc289 | -17.62376 | -46.61342 | 2025-10-22 04:57:00 | NPP-375D | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 637ffc95-dcca-3a93-8ed2-fb43828b50c6 | -19.0562 | -57.49104 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| bdd80680-6c1f-310b-8b9a-daa1755ee86e | -18.64946 | -49.09228 | 2025-10-22 04:57:00 | NPP-375D | CENTRALINA | MINAS GERAIS | Brasil | 3115805 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 955dbc82-4d92-3d97-89dd-49402058ab9c | -17.86642 | -45.97575 | 2025-10-22 04:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 11a21808-97ae-3d16-890a-772fac3e3c78 | -16.09055 | -55.41947 | 2025-10-22 04:57:00 | NPP-375D | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 811d6625-c6cb-3951-be0e-65da567c5ed0 | -18.9463 | -55.07777 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 96ee57b8-07cc-3ef5-b138-3deb353ada8a | -20.56346 | -45.89445 | 2025-10-22 04:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9e70a9fc-5d89-3f04-b0af-ed15ddd13ccb | -17.86108 | -45.97518 | 2025-10-22 04:57:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7c496a4-fc83-369d-8cf1-d7096251c6b2 | -19.87708 | -46.33622 | 2025-10-22 04:57:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| f93fd3bc-64ff-3999-9cba-4901cb661e3d | -12.38058 | -63.87081 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1e18e22f-3fca-383d-9987-58eab8ee7ce0 | -15.48582 | -50.46416 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0c9a2018-b16a-3195-9dbf-dd92242546c0 | -19.09179 | -44.34482 | 2025-10-22 04:57:00 | NPP-375D | CORDISBURGO | MINAS GERAIS | Brasil | 3118908 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2bd13099-0ee9-30ef-868d-d3b046fc9476 | -15.52052 | -50.38444 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 960e5227-b618-341b-a378-2877198fcf58 | -18.14699 | -52.98344 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9faf8d66-69cc-3fbf-a134-1c778b52f2b0 | -18.14349 | -52.98289 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fccefa38-f13a-3f2f-ba55-400da34642ba | -18.95021 | -55.07467 | 2025-10-22 04:57:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 91546659-6699-3b03-8052-b770975b7d7e | -19.90631 | -46.11502 | 2025-10-22 04:57:00 | NPP-375D | TAPIRAÍ | MINAS GERAIS | Brasil | 3168200 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cc1f00c1-fbaf-3cf1-9ea4-faef9080b0b9 | -19.06028 | -57.48778 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 61493bff-1183-3766-bc81-39a37c2c9e29 | -19.08652 | -57.52074 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| de588038-1521-3d24-be71-93f03a76a617 | -20.42088 | -55.73959 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 9bdb2d2b-3f24-3111-93e2-5eb96ab9cd61 | -16.87144 | -49.99355 | 2025-10-22 04:57:00 | NPP-375D | PALMEIRAS DE GOIÁS | GOIÁS | Brasil | 5215702 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 146d24a8-2cd9-397c-bd93-1c5f1ccdee13 | -17.2135 | -47.65281 | 2025-10-22 04:57:00 | NPP-375D | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e3b5c63a-3ad9-3b9a-948a-c135dc86be85 | -20.42146 | -55.7359 | 2025-10-22 04:57:00 | NPP-375D | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 78d223da-946a-338a-b77c-3d4c4fbd73fc | -14.22452 | -52.80922 | 2025-10-22 04:57:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3d297df1-3954-360c-9e29-fcaff74fa30b | -20.55788 | -45.89423 | 2025-10-22 04:57:00 | NPP-375D | PIMENTA | MINAS GERAIS | Brasil | 3150505 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 137e6861-81dd-3715-926f-b03effe2776e | -19.05212 | -57.49429 | 2025-10-22 04:57:00 | NPP-375D | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| e3674d19-1bdf-31a0-a41a-4fe1af23d65d | -18.59543 | -51.72306 | 2025-10-22 04:57:00 | NPP-375D | ITARUMÃ | GOIÁS | Brasil | 5211305 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| be6d911b-eca6-34f7-9826-7078744afe72 | -18.33694 | -49.50632 | 2025-10-22 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| a5223a74-ada5-3673-853c-29b5252d8889 | -14.69204 | -48.78244 | 2025-10-22 04:57:00 | NPP-375D | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25ab15bd-76bc-3e41-9614-b99da1b5cc2d | -18.33753 | -49.50694 | 2025-10-22 04:57:00 | NPP-375D | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 3726cc16-7a68-32c7-83db-544de3aabf52 | -19.87445 | -46.33499 | 2025-10-22 04:57:00 | NPP-375D | MEDEIROS | MINAS GERAIS | Brasil | 3141306 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 15211a0d-a9b0-3c52-958c-4ec2a05cbcb1 | -15.49103 | -50.45484 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 289bbe47-6617-3ac3-a15c-a8e75252ffe8 | -15.52898 | -50.38033 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 93a7ca4f-15e5-3a19-b717-e203939ad907 | -15.49035 | -50.45979 | 2025-10-22 04:57:00 | NPP-375D | FAINA | GOIÁS | Brasil | 5207535 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0a489816-204c-35ce-a6a1-3efbafadd5bd | -12.27238 | -63.87147 | 2025-10-22 04:57:00 | NPP-375D | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d8160e57-d5af-301e-8949-c45ef36c3cdf | -18.60433 | -47.32881 | 2025-10-22 04:57:00 | NPP-375D | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e27df818-8f7b-3046-b52f-5e42f3ac079f | -16.62427 | -43.48595 | 2025-10-22 04:57:00 | NPP-375D | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 10a48c27-bde6-31fe-9b9e-197188ecbe88 | -17.95445 | -57.63586 | 2025-10-22 04:57:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 4222651f-fbff-3acc-91b0-92f9e02e9083 | -18.15166 | -52.97594 | 2025-10-22 04:57:00 | NPP-375D | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README16.md)
