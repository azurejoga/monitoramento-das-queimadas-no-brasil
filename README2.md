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
| e4cdf5eb-9f5f-390b-9c9e-e39db679ebb2 | -10.87844 | -49.55006 | 2025-03-13 04:08:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6de4d3cb-4709-3dff-893a-c7e3304c1d32 | -6.95838 | -43.04032 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a0ea1d98-fb88-397d-abb4-9262f8deeba7 | -7.24789 | -44.77131 | 2025-03-13 04:08:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 841db595-a6e5-3ba1-8ede-3b6b38048eb5 | -6.92798 | -35.13902 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 7dc8d49e-67ed-3d25-b60f-1a08cf25e824 | -7.86072 | -39.71205 | 2025-03-13 04:08:00 | NOAA-21 | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 8.9 |
| 10529ec8-f0da-3c44-a2d0-770ebd1b249e | -9.25971 | -40.96036 | 2025-03-13 04:08:00 | NOAA-21 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d0d2e378-afb8-324c-906b-bc2c59f50a6d | -10.83967 | -38.10714 | 2025-03-13 04:08:00 | NOAA-21 | TOBIAS BARRETO | SERGIPE | Brasil | 2807402 | 28 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 2e908e5f-2fe2-31e2-a45c-b6d3b9fd46db | -11.5836 | -44.83435 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 0d875b88-9963-3e28-8c32-e88abbf1f23e | -11.77891 | -44.71523 | 2025-03-13 04:08:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09fcf6d1-2187-3287-ae10-40c87aa4734d | -5.64805 | -43.71691 | 2025-03-13 04:08:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0c32ca01-6829-36ef-aaf7-1993d579c1af | -6.96511 | -43.04137 | 2025-03-13 04:08:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ec2749a4-60a8-3949-81f1-d987a78c3c73 | -10.35238 | -37.98022 | 2025-03-13 04:08:00 | NOAA-21 | CORONEL JOÃO SÁ | BAHIA | Brasil | 2909208 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 50de9dbc-8a21-37c6-a6ae-5bff279f1e29 | -6.9268 | -35.13747 | 2025-03-13 04:08:00 | NOAA-21 | CAPIM | PARAÍBA | Brasil | 2504033 | 25 | 33 | nan | nan | nan | Mata Atlântica | 10.3 |
| a926730d-32a0-350c-bd0c-7a42e11f1876 | -17.59508 | -43.19886 | 2025-03-13 04:10:00 | NOAA-21 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 92432de6-fd06-304a-95f9-feafa54cab53 | -15.59016 | -42.40154 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 808108ff-d1cf-38c3-a36b-2fd914a34305 | -17.24858 | -46.66155 | 2025-03-13 04:10:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8e944fd3-89ec-370c-936d-1ccc571eed17 | -14.16155 | -43.72864 | 2025-03-13 04:10:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2cce87c0-a0d8-3934-901b-f96183d9a41b | -15.08064 | -48.94419 | 2025-03-13 04:10:00 | NOAA-21 | BARRO ALTO | GOIÁS | Brasil | 5203203 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81e8e74f-1966-35ce-9eb8-1ea30b5e1ddb | -12.5082 | -45.50021 | 2025-03-13 04:10:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 21bcb46f-9b03-33be-bbc6-ac50d2aab2b4 | -12.07305 | -45.51894 | 2025-03-13 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| eb6f62d8-436b-33c4-a57a-fdaee05e345e | -16.34974 | -43.6978 | 2025-03-13 04:10:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4bba7fff-772c-3cc8-b416-fffdd6800585 | -13.19644 | -43.5506 | 2025-03-13 04:10:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 3680ee77-2f66-3c75-8f55-59458f0d45b9 | -19.92246 | -41.51802 | 2025-03-13 04:10:00 | NOAA-21 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1ef27084-b803-3a08-865c-a89a97b95705 | -15.61291 | -43.58295 | 2025-03-13 04:10:00 | NOAA-21 | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6d98a5cb-7d18-3160-97f0-51e341179abf | -12.05527 | -45.42995 | 2025-03-13 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.3 |
| f5cebf2b-3f8f-3c38-a574-45be3c78daaf | -14.42958 | -45.39746 | 2025-03-13 04:10:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3028685d-40ee-3b9c-8c91-478edba1f351 | -18.67333 | -43.13747 | 2025-03-13 04:10:00 | NOAA-21 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| d4725615-05e9-3f8d-a88b-f1ef4fe9c329 | -15.59183 | -42.3905 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e264ea1b-4ab1-35be-8c54-acd9f3efc48b | -17.67713 | -42.74218 | 2025-03-13 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 08dcc927-bff9-3a81-b431-ba9e43f7b605 | -13.33758 | -40.31076 | 2025-03-13 04:10:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 95844520-ebad-3c22-a9b9-20f5ed5bed9d | -19.18637 | -44.19162 | 2025-03-13 04:10:00 | NOAA-21 | ARAÇAÍ | MINAS GERAIS | Brasil | 3103207 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 479021d5-fb1c-3733-ab77-f347a96d0049 | -19.60902 | -44.13919 | 2025-03-13 04:10:00 | NOAA-21 | MATOZINHOS | MINAS GERAIS | Brasil | 3141108 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b4edfac1-2a8f-3b8c-98ec-48bd98f1ba0e | -17.38116 | -39.37288 | 2025-03-13 04:10:00 | NOAA-21 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| e60569cf-603e-3375-b9c9-2493c0f3f7ab | -16.20574 | -47.38216 | 2025-03-13 04:10:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 66a9e14e-f2c3-35e6-9813-dbd2b0535dff | -14.23236 | -42.77295 | 2025-03-13 04:10:00 | NOAA-21 | GUANAMBI | BAHIA | Brasil | 2911709 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d29ade46-42e8-33d9-9945-ee7d899dcbea | -16.61395 | -43.32946 | 2025-03-13 04:10:00 | NOAA-21 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dd680aa3-e305-35b2-b67d-36d64e16e326 | -17.60917 | -49.13558 | 2025-03-13 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 60809009-9b1b-3e6b-9e90-98a37ec2c73c | -18.04111 | -39.9242 | 2025-03-13 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 04a5f0e1-7909-3eb2-8f63-490ad92a6e90 | -12.06954 | -45.51834 | 2025-03-13 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d1a58165-4516-3d88-93b8-41442cb19abe | -15.59072 | -42.39786 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11e271f6-7e87-32f1-b747-a3cd66c1a5a9 | -17.09489 | -43.80324 | 2025-03-13 04:10:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 32d82c17-0b93-31aa-8bc3-3c9faa358070 | -17.6131 | -49.13641 | 2025-03-13 04:10:00 | NOAA-21 | MORRINHOS | GOIÁS | Brasil | 5213806 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 318f4921-2de8-3b63-93d5-e2fb6d69a979 | -17.75257 | -42.89518 | 2025-03-13 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 076a274c-244f-3fb5-9f47-11706c524a9f | -14.85896 | -45.19841 | 2025-03-13 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 84e394a9-9a85-3ecd-a677-8380514d849c | -15.59798 | -42.39526 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c7a7739e-7d91-3c98-8eb4-fcf1c3f98fa1 | -16.04352 | -43.80817 | 2025-03-13 04:10:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2d65d0d0-0a1d-3c9c-9d2a-9dbcf080f8ec | -15.59462 | -42.39473 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f5084f83-1362-3242-a5cd-8da39fe8d069 | -13.0542 | -39.92633 | 2025-03-13 04:10:00 | NOAA-21 | BREJÕES | BAHIA | Brasil | 2904308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6444fb4e-98c8-3550-86b3-41dccc57589b | -15.59742 | -42.39893 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| af58e72a-a5a2-342f-8a1e-d9a90be9a274 | -18.04171 | -39.92695 | 2025-03-13 04:10:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 612afa25-f53d-3a1a-8bd3-087163f7fa9d | -13.04833 | -40.33706 | 2025-03-13 04:10:00 | NOAA-21 | IAÇU | BAHIA | Brasil | 2911907 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 239c4e35-04ba-3754-940f-acfe9ab2ad93 | -14.13442 | -41.69033 | 2025-03-13 04:10:00 | NOAA-21 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 69941ee5-bf7d-3db4-a274-9899a1d3af40 | -15.59127 | -42.39418 | 2025-03-13 04:10:00 | NOAA-21 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6f9f8007-ac26-3e28-88f1-79ed955224c4 | -17.67657 | -42.74592 | 2025-03-13 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 56a79478-6c29-3636-af33-ef0937a88ca3 | -14.86007 | -45.1982 | 2025-03-13 04:10:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d403d9d9-fe27-328c-b535-793139486721 | -16.6809 | -43.88528 | 2025-03-13 04:10:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 5ca13b8c-d614-3b22-932d-6dae337b5f6f | -12.0737 | -45.51493 | 2025-03-13 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 76e1ce01-68f3-30f1-9514-91cbaf3a322a | -17.77075 | -41.31687 | 2025-03-13 04:10:00 | NOAA-21 | TEÓFILO OTONI | MINAS GERAIS | Brasil | 3168606 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f3148b3e-653a-3aca-8c11-4123e243df19 | -12.66632 | -44.50604 | 2025-03-13 04:10:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 10b24180-71b8-3737-81f5-2cd362d0ab81 | -17.78266 | -42.80861 | 2025-03-13 04:10:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f484a981-802b-302d-999d-abb4a6bf8572 | -12.0702 | -45.51434 | 2025-03-13 04:10:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 98df7cf0-86dd-38aa-b643-e83589f84c48 | -20.90043 | -43.81907 | 2025-03-13 04:12:00 | NOAA-21 | CARANAÍBA | MINAS GERAIS | Brasil | 3113107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6a65da85-4841-339c-9c0b-b22221a63292 | -20.53412 | -42.00031 | 2025-03-13 04:12:00 | NOAA-21 | CAPARAÓ | MINAS GERAIS | Brasil | 3112109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 5a6fb3e9-0fae-33fc-bafd-99d93a630de6 | -22.1245 | -41.44537 | 2025-03-13 04:12:00 | NOAA-21 | QUISSAMÃ | RIO DE JANEIRO | Brasil | 3304151 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 4dcd3225-f8b1-3440-b125-d3d37aad2625 | -21.10641 | -49.25069 | 2025-03-13 04:12:00 | NOAA-21 | IBIRÁ | SÃO PAULO | Brasil | 3519402 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 68b78790-d864-399b-90e2-93e50ac10765 | -21.00405 | -44.19273 | 2025-03-13 04:12:00 | NOAA-21 | CORONEL XAVIER CHAVES | MINAS GERAIS | Brasil | 3119708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| e0e84a49-db03-3598-bcdd-eaefb0be8adc | -20.38911 | -49.76744 | 2025-03-13 04:12:00 | NOAA-21 | COSMORAMA | SÃO PAULO | Brasil | 3512902 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 48780a3a-3258-35cf-89ac-8913c53ffa6a | -22.92265 | -45.41449 | 2025-03-13 04:12:00 | NOAA-21 | PINDAMONHANGABA | SÃO PAULO | Brasil | 3538006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 7a2f98b6-a340-33fd-9e61-1568f2a92d96 | -20.57831 | -44.57512 | 2025-03-13 04:12:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| db9686c0-9af8-3b58-88a0-ae65d158fa04 | -22.54097 | -48.81521 | 2025-03-13 04:12:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1fd35554-c92d-3344-aaab-7ee3ad8aef01 | -29.98677 | -51.13887 | 2025-03-13 04:14:00 | NOAA-21 | PORTO ALEGRE | RIO GRANDE DO SUL | Brasil | 4314902 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| e90ca86c-d1d1-3b6b-84b3-451d8aa37efd | -29.87353 | -51.15947 | 2025-03-13 04:14:00 | NOAA-21 | CANOAS | RIO GRANDE DO SUL | Brasil | 4304606 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| e677dc81-ffc1-38a7-8b3b-fa5fddfabed5 | -6.95959 | -43.04516 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4d029ba-80ff-321e-8d6d-405de3b196be | -6.96411 | -43.0423 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c1ba6f1b-a66f-378e-8971-0ef9679b4266 | -6.96009 | -43.04168 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a2dffa36-147e-37dd-b5ac-fc8fc66c5651 | -6.9606 | -43.03818 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 55d49e91-9c8d-37cf-b2a0-d2da6002a69c | -6.96512 | -43.03534 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| ef8b9f44-3b4b-3387-8ca7-2175d450c6c3 | -6.96111 | -43.03472 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 04d0466a-3e7c-3850-aa2a-3566876d3a2d | -6.96462 | -43.03881 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6cdf1daf-e138-3481-976d-8934f365de72 | -6.22549 | -48.05262 | 2025-03-13 04:32:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b13164e2-177c-382f-a80a-dbcc2e4197bf | -6.95558 | -43.04452 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2f6da540-b6cd-3b94-bfc8-161163bd982e | -6.95908 | -43.04866 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2cace75e-a295-33ab-8272-4de4801ec63c | -7.86192 | -39.71328 | 2025-03-13 04:32:00 | NPP-375D | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| df1b2e13-edbe-39a6-ae11-a446e36778fb | -6.9987 | -45.61366 | 2025-03-13 04:32:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 424c33bf-97e4-3ca2-8cb7-101006550ca1 | -6.95608 | -43.04107 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5d06834d-6a0f-3b71-ad05-7c4eb11d4e0f | -7.24387 | -44.77151 | 2025-03-13 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ab28d507-cd98-3ea5-8f4d-6655feae08ba | -7.8568 | -39.71259 | 2025-03-13 04:32:00 | NPP-375D | GRANITO | PERNAMBUCO | Brasil | 2606309 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| fcf63711-0b0b-3641-b450-5f059292e540 | -7.2426 | -44.78001 | 2025-03-13 04:32:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a6a1b9e6-9b10-340c-8707-625a88faeaac | -5.44462 | -45.42868 | 2025-03-13 04:32:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9ae61245-41a9-3b1c-aff5-3785f48071b3 | -6.95507 | -43.04802 | 2025-03-13 04:32:00 | NPP-375D | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8d46bece-688a-38d5-9443-0ee6c7b95a30 | -6.24979 | -48.02802 | 2025-03-13 04:32:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9706813f-1058-3341-ab71-7f15b0ff6050 | -10.39303 | -47.99387 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6f3ad3e9-62fb-3efe-b3b6-effc7759036a | -15.58784 | -42.39637 | 2025-03-13 04:34:00 | NPP-375D | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ec027cd8-f05d-3c53-a56e-b811a95dc1b4 | -10.66714 | -44.39909 | 2025-03-13 04:34:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 88b82a7b-664c-316d-9ec3-4c429952c892 | -8.71604 | -38.64076 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 0a6e239c-1b15-30eb-9d92-36f63c0725a7 | -11.56152 | -47.61967 | 2025-03-13 04:34:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 311b1ef7-4801-31c4-bdb7-bd61c8eeb27a | -10.39413 | -47.98682 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7288204f-8ffa-3715-ba18-252240956c1a | -11.89144 | -45.2738 | 2025-03-13 04:34:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ae0a76cf-9f37-392a-95a1-b1538a7c2f2c | -10.39358 | -47.99035 | 2025-03-13 04:34:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 2eb1670b-1986-341a-a014-cf2218485323 | -8.71095 | -38.63629 | 2025-03-13 04:34:00 | NPP-375D | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 3.3 |


[Clique aqui para ver as próximas entradas](README3.md)
