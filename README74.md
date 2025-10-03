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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b375db88-ff4f-3d35-9546-627c400f55a0 | -13.74569 | -48.01931 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e4a40c-4c0f-3c71-9711-644827da2e3a | -13.13358 | -47.88748 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 11.9 |
| b88a98e4-9612-3618-a977-ec09a19e8653 | -14.41222 | -46.16151 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 368036b9-98c0-324f-9b47-b279963a8381 | -12.93243 | -45.09279 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a515e40-9101-3bfb-a52c-c546f2e37764 | -9.94137 | -43.74196 | 2025-10-03 04:12:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 902d1f6c-bf12-3ebc-8a7f-0b2157f2f040 | -12.60249 | -47.00325 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 95e1c175-211e-31b2-9856-b40567bbae07 | -9.37903 | -45.85366 | 2025-10-03 04:12:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17a4af66-aae4-3442-af60-4ad2048d0ccf | -14.43948 | -46.1228 | 2025-10-03 04:12:00 | NPP-375D | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e661790d-7a7a-3a62-afd7-333ad5a5ff53 | -11.30408 | -47.83873 | 2025-10-03 04:12:00 | NPP-375D | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 57ee7679-5846-386e-b4fc-a9cc53062fb0 | -10.93234 | -46.72931 | 2025-10-03 04:12:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 03ebc0a1-41f9-3f73-9d5c-b81e2f9ab855 | -11.21089 | -41.59618 | 2025-10-03 04:12:00 | NPP-375D | JOÃO DOURADO | BAHIA | Brasil | 2918357 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 90588714-620e-3c36-b424-da9139210f7d | -13.15063 | -47.8218 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 1467ccb6-438b-3aa6-8c27-cb16ee4e0b34 | -12.92962 | -45.08838 | 2025-10-03 04:12:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9d9e029d-e68a-3cc8-adf5-99d84db5de6d | -14.23448 | -46.11767 | 2025-10-03 04:12:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b7c890fb-d3ae-3639-b644-31b55affb303 | -12.94251 | -46.39334 | 2025-10-03 04:12:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ca3a5af-f6bd-36e9-8e11-398d9d7b0a8b | -11.06202 | -47.79392 | 2025-10-03 04:12:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 37fe630f-7881-30d5-9808-a638953c2967 | -13.73149 | -47.91547 | 2025-10-03 04:12:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 593ec001-adac-36dd-86ed-06339a55b785 | -13.14159 | -47.89732 | 2025-10-03 04:12:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 39ab910c-0e9b-3b71-adcf-7da2d4ee9758 | -11.59497 | -47.62754 | 2025-10-03 04:12:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5fd5af15-1347-3fc1-988e-575bc3a80fb3 | -10.41053 | -54.41455 | 2025-10-03 04:12:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71d77d16-6640-3444-a7ee-0e74a702358c | -13.08867 | -47.0789 | 2025-10-03 04:12:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 40cef1b9-0047-3cf8-a854-2503519d578e | -16.36544 | -47.01146 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 36e2651a-6917-374e-8e94-80ccea80b612 | -14.94768 | -47.51923 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4f4338a5-e0c9-3f9c-bcf5-51e666f99c45 | -14.93886 | -46.88943 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 581300be-00d5-3bff-a8d9-64e2aec50609 | -19.23171 | -43.71912 | 2025-10-03 04:14:00 | NPP-375D | SANTANA DO RIACHO | MINAS GERAIS | Brasil | 3159001 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 02d74cd6-2520-3b87-bf82-24c9f700a4d2 | -14.63214 | -48.13398 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 7c66bb5c-b38e-3e06-886f-253b5fa45ea4 | -14.73146 | -48.11582 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e932fa3e-fb5e-34c3-8ce2-b21926f88baa | -17.86253 | -57.62362 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 9990a5a1-9773-3a56-b7c0-7ed343ed64b7 | -15.46313 | -51.56193 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2497bdbe-0bad-3421-a380-aa276093b02d | -14.87924 | -47.44436 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f8f8dec-942f-358c-b310-a1d70a9d3a28 | -19.4641 | -43.65822 | 2025-10-03 04:14:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 631291d8-6403-3748-abee-10a019a83476 | -15.60849 | -47.03828 | 2025-10-03 04:14:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b3a19d79-8705-37f6-8cc2-245f248a2643 | -16.43065 | -42.41061 | 2025-10-03 04:14:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 764ebf1e-37bf-3554-ab3b-ee8389ec44d3 | -15.20353 | -47.99242 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f2d379ee-df15-3269-892b-869d20db43fe | -14.60088 | -48.23916 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7cb46bc4-da4d-3146-a6d6-fd7af0c7d660 | -14.66791 | -48.09243 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| de89f509-45f4-3311-8541-cc7dec18b992 | -14.93418 | -46.89996 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 11.1 |
| c1f7afef-6503-3e02-8af9-55a0c92c9ba6 | -17.85575 | -57.62267 | 2025-10-03 04:14:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| a04ed3b2-a185-305f-ac46-549f8f6a6d61 | -16.04858 | -50.91558 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2ed332f6-8fe4-3b16-b9d1-5753da353d32 | -15.21035 | -47.63252 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ab07efd9-3b7d-3348-b01c-83cd6e3e1eef | -14.67959 | -48.07214 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 775d952b-116b-3369-89f9-f77588553796 | -14.94842 | -46.89927 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8fc07f6b-a6dc-397e-9be6-20b70662324e | -14.94475 | -46.89877 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f8f3e70-0614-3ebf-91e6-cc14fbfd725f | -14.87581 | -48.34643 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 68e5c018-41e5-3d0c-a89d-aa8024e64369 | -14.67869 | -48.07715 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| f7c4e573-331a-3937-b7de-c61002e0d39a | -19.7322 | -45.88746 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 64b86bf3-34b5-3e5b-b194-271dd5c79530 | -14.90749 | -48.2955 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 70bb6110-e001-35e0-94c4-e453464c9a89 | -18.67899 | -47.83297 | 2025-10-03 04:14:00 | NPP-375D | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1773c9d4-f9b9-3231-857c-b8dbdb595e63 | -15.58454 | -46.93956 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3b93020e-4fd1-31b9-b522-f5218989eeb5 | -19.84799 | -44.07578 | 2025-10-03 04:14:00 | NPP-375D | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fc0bbbba-d0a9-39a9-b1c6-517d67050aa0 | -14.6719 | -48.09269 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5896e2ed-23b9-38f4-8ad9-6915b5b74b85 | -15.2387 | -48.71811 | 2025-10-03 04:14:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b4f4b2a-88da-3fc8-b3f5-8ece122497a1 | -20.95036 | -44.00014 | 2025-10-03 04:14:00 | NPP-375D | LAGOA DOURADA | MINAS GERAIS | Brasil | 3137403 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| f7516495-1510-3b39-a119-ee613d937f48 | -14.76731 | -49.28683 | 2025-10-03 04:14:00 | NPP-375D | HIDROLINA | GOIÁS | Brasil | 5209804 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 54b3dd5c-1299-383a-b44a-38ee43c66d3f | -14.91822 | -48.30367 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bdef8c0d-5ea9-36b9-a5f0-7026cb18b15e | -20.8632 | -49.479 | 2025-10-03 04:14:00 | NPP-375D | MIRASSOL | SÃO PAULO | Brasil | 3530300 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 4ff35a47-4528-3cb4-9a4a-5de615ec2a31 | -15.66044 | -44.49683 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f6d731f1-ec72-34c0-a69c-c57d98f48855 | -20.17875 | -43.77611 | 2025-10-03 04:14:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| d9cecb60-8038-3566-87ea-0e5f0e585a69 | -18.46903 | -43.71418 | 2025-10-03 04:14:00 | NPP-375D | GOUVEIA | MINAS GERAIS | Brasil | 3127602 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2284a76a-319e-3dcb-b781-7a11d38ea49f | -20.76158 | -44.56861 | 2025-10-03 04:14:00 | NPP-375D | OLIVEIRA | MINAS GERAIS | Brasil | 3145604 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| e6c33e8d-00b4-3862-87df-ba74b4fc9f80 | -18.31771 | -44.03397 | 2025-10-03 04:14:00 | NPP-375D | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a832038-a5b0-3944-b515-24a6c4757f9b | -15.83651 | -46.23976 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cd3eb90-60ed-360c-8313-997e8e0031df | -15.67864 | -46.25467 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 38913053-4a19-3037-9d9b-95011f6a31bc | -14.89434 | -46.9786 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 24fdbca4-d5f1-3799-9885-b85069499492 | -15.76199 | -43.66678 | 2025-10-03 04:14:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad6b5ee3-897d-366f-bf70-5f095e062ceb | -17.07756 | -44.91806 | 2025-10-03 04:14:00 | NPP-375D | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 061a005b-5fd6-3b9e-abd1-d9b1ac91bcfb | -16.06973 | -51.00002 | 2025-10-03 04:14:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 00ac2e6b-87c4-3f1f-8b7a-a90f4620f007 | -15.20265 | -47.99733 | 2025-10-03 04:14:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 250a161d-6637-3e4a-af21-f80dec6e7856 | -15.7015 | -48.30733 | 2025-10-03 04:14:00 | NPP-375D | COCALZINHO DE GOIÁS | GOIÁS | Brasil | 5205513 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c176d96f-1e7b-3832-8d2b-7e8aeb02ecec | -17.32056 | -49.38145 | 2025-10-03 04:14:00 | NPP-375D | MAIRIPOTABA | GOIÁS | Brasil | 5212600 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 82937b24-8882-3b84-be25-f15c87fad17c | -17.96238 | -44.3957 | 2025-10-03 04:14:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22048b85-1f2b-38b6-90b5-b93a1442930c | -19.59981 | -44.63105 | 2025-10-03 04:14:00 | NPP-375D | PEQUI | MINAS GERAIS | Brasil | 3149606 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| dc0fb559-617f-398e-9d16-8a37c06acc7c | -14.74528 | -48.12874 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 33facc32-4e38-31e3-819c-78dc4c08b37a | -19.94841 | -46.80628 | 2025-10-03 04:14:00 | NPP-375D | TAPIRA | MINAS GERAIS | Brasil | 3168101 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 07887c3c-5d9e-339e-ac06-fe4457833663 | -19.83809 | -42.2901 | 2025-10-03 04:14:00 | NPP-375D | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 95c41699-ba77-3a8c-bbe4-043062caee5a | -15.57584 | -46.94786 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f73b450d-ad26-3057-97df-89562c848827 | -15.98634 | -50.86979 | 2025-10-03 04:14:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 91054897-4ae4-3661-a50a-8cf703a75254 | -20.01808 | -41.33132 | 2025-10-03 04:14:00 | NPP-375D | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 9ab271f0-81ce-30b3-b716-c9aca9b2fc51 | -19.96757 | -43.65308 | 2025-10-03 04:14:00 | NPP-375D | CAETÉ | MINAS GERAIS | Brasil | 3110004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| db950943-cd5f-3b14-a130-00e5b9ebae82 | -14.89656 | -47.82515 | 2025-10-03 04:14:00 | NPP-375D | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 529b2382-9f3a-34bb-9ebf-76ed89ae3f9c | -19.56604 | -43.17283 | 2025-10-03 04:14:00 | NPP-375D | ITABIRA | MINAS GERAIS | Brasil | 3131703 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7de6078f-ce0c-3377-a98f-21d8d10f967d | -16.32211 | -42.36703 | 2025-10-03 04:14:00 | NPP-375D | RUBELITA | MINAS GERAIS | Brasil | 3156502 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c0ff5949-79aa-3648-8050-e9672abb4d22 | -15.83235 | -46.24293 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3b88eff4-453c-30f3-ad40-340450b99fa3 | -15.58968 | -46.93161 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6177c043-12c8-3d66-8943-8eeeed421170 | -18.23206 | -53.34956 | 2025-10-03 04:14:00 | NPP-375D | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2db04be8-d3ae-3fb9-854a-23cf6dc3afbc | -15.94297 | -46.22907 | 2025-10-03 04:14:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 27a6fda2-ba1f-345e-add9-c90000335b42 | -14.90317 | -46.9712 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c42dc399-4f91-3f95-8a6b-4ae955187009 | -18.46077 | -49.44339 | 2025-10-03 04:14:00 | NPP-375D | CACHOEIRA DOURADA | GOIÁS | Brasil | 5204250 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cc315d44-e3e9-351c-88ad-506d199254f2 | -14.94418 | -46.88058 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fcaedf5a-ba1d-3617-becf-55d4ba834be5 | -19.72112 | -45.91257 | 2025-10-03 04:14:00 | NPP-375D | LUZ | MINAS GERAIS | Brasil | 3138807 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| c22bf82d-8583-3533-8741-a2d99eb7a089 | -15.34982 | -47.06907 | 2025-10-03 04:14:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b37c80f7-3f9f-355f-b6ec-a2fdb25f3e88 | -14.91665 | -48.33471 | 2025-10-03 04:14:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| adf3e5a7-d057-3280-b9f7-189a45fc5210 | -14.9082 | -49.25273 | 2025-10-03 04:14:00 | NPP-375D | SÃO LUIZ DO NORTE | GOIÁS | Brasil | 5220157 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 03283cdf-d768-3656-8d43-e04c27dabe47 | -20.49648 | -43.929 | 2025-10-03 04:14:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 85200b49-c4a3-3148-8a53-4fd71a266df6 | -16.27457 | -47.10245 | 2025-10-03 04:14:00 | NPP-375D | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 254ad082-084f-3178-a612-f8ef69fe2c44 | -17.5181 | -43.48186 | 2025-10-03 04:14:00 | NPP-375D | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0dc03af6-7f46-3d79-aa3a-e54e501fdd27 | -14.89497 | -46.84393 | 2025-10-03 04:14:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 51b6de46-6113-334b-9c02-c8575c7edcab | -15.3174 | -46.38143 | 2025-10-03 04:14:00 | NPP-375D | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 04fab58b-b4c7-3ea3-840e-96820102155e | -15.49999 | -44.1907 | 2025-10-03 04:14:00 | NPP-375D | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 9a8e09c1-4474-3a62-8a10-73a984e6d4bd | -14.64654 | -48.25733 | 2025-10-03 04:14:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |


[Clique aqui para ver as próximas entradas](README75.md)
