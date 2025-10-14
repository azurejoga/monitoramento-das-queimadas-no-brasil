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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 79e2b340-6dfa-391a-aaa6-79fda0c0ab1a | -8.97573 | -61.97893 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6b1ce4b7-5ec6-3391-a709-9ebd876e8501 | -12.13892 | -53.6124 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3ab7cd70-81a0-3ebf-85dc-03afe06f4d64 | -8.66011 | -54.71174 | 2025-10-14 05:18:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 98ea996d-8fd8-318b-9e19-b5cfce2a028a | -12.7903 | -50.64873 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 787bb8c2-1a5c-3090-a916-f4e0e81b7b85 | -12.78987 | -50.6524 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 3e58d65d-8d6e-32f9-9d81-9d378eee6e1f | -12.86435 | -50.64139 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e170273e-b46c-39fd-9d93-e2b017b1f277 | -14.86711 | -60.06456 | 2025-10-14 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0a22e0c2-a8d0-3024-b99f-4f5bbd08fe01 | -14.86379 | -60.06402 | 2025-10-14 05:21:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a250c694-b29d-3411-8b5b-27d6cbffa8cd | -15.14739 | -56.45365 | 2025-10-14 05:21:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47bb2776-397f-307d-8f84-888314e9b7a5 | -15.61947 | -56.12092 | 2025-10-14 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8b514826-f89c-3aa2-a519-a33de2920f58 | -15.15125 | -56.45423 | 2025-10-14 05:21:00 | NOAA-21 | JANGADA | MATO GROSSO | Brasil | 5104906 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 6e759c79-2e90-3232-9a99-0aedc5daba01 | -15.61877 | -56.12623 | 2025-10-14 05:21:00 | NOAA-21 | CUIABÁ | MATO GROSSO | Brasil | 5103403 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 45a6423d-6aab-34e5-9cc9-9787f30bbfb8 | -3.03745 | -40.10939 | 2025-10-14 05:25:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 12.2 |
| acdf1932-b921-31c0-85ea-078356404cc7 | -3.04424 | -40.10559 | 2025-10-14 05:25:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 15.4 |
| a78aadbe-2d61-3fc9-b5ed-eb0758912b9e | -3.04265 | -40.11578 | 2025-10-14 05:25:00 | AQUA_M-M | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 6e7174cc-04a3-3c12-88f7-606e160baa61 | -6.43846 | -41.83217 | 2025-10-14 05:27:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 56a111fb-93f2-344c-90ec-372719fdd79a | -5.10489 | -43.19972 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 23.7 |
| 59099446-a53f-3e73-a590-db7fb2e9cae2 | -4.65574 | -43.12938 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 36a536bb-e504-3cc6-8960-742801c76476 | -4.66958 | -43.11573 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.1 |
| b146bde5-95b5-3ce5-a44b-fa82ebca363f | -7.53143 | -42.69491 | 2025-10-14 05:27:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 10.7 |
| f3750452-033b-36dd-b138-e79f2c53c320 | -10.81133 | -43.95808 | 2025-10-14 05:27:00 | AQUA_M-M | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 9.1 |
| 72688889-caa8-33bf-8e29-1970c904b624 | -7.75296 | -45.71836 | 2025-10-14 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 1164f589-307d-3feb-b246-836bd64a6f09 | -5.49007 | -45.39677 | 2025-10-14 05:27:00 | AQUA_M-M | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 4fa8fa37-c166-36f4-8b01-a242c588370d | -5.65149 | -43.60331 | 2025-10-14 05:27:00 | AQUA_M-M | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 20.4 |
| b63073f8-7259-3d59-890b-52d6d035b24d | -7.79549 | -46.01027 | 2025-10-14 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 126.6 |
| a6be805c-aed1-3fdf-8b35-db2790e19eac | -5.49449 | -43.06949 | 2025-10-14 05:27:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 335b6ce0-aa62-3b5d-8784-7b4573ac62ef | -7.79171 | -46.03297 | 2025-10-14 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 86065a4d-f8a2-3b16-a409-690ed57f7f6a | -4.66717 | -43.13116 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 35.5 |
| 211c3b74-8b89-39eb-8fff-a5520de2b1ed | -6.5359 | -43.55661 | 2025-10-14 05:27:00 | AQUA_M-M | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 02a2682f-a78e-3d0c-8686-3fdc647ecc0b | -6.44852 | -41.83364 | 2025-10-14 05:27:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| eb78e92a-9dc3-3cc4-b019-b04713c03459 | -7.78186 | -46.00806 | 2025-10-14 05:27:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 96de7d73-c996-30e5-af89-5cd4e837fb7c | -7.63728 | -42.56874 | 2025-10-14 05:27:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| 21a1c531-8324-3585-b84a-d81229b0004b | -6.44031 | -41.82036 | 2025-10-14 05:27:00 | AQUA_M-M | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 43ba7ef7-089b-31a7-9719-f1e57fa1ae26 | -7.64628 | -42.56281 | 2025-10-14 05:27:00 | AQUA_M-M | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 55478002-c7f2-3b0b-abbc-0be0b1942389 | -7.53567 | -42.70192 | 2025-10-14 05:27:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 11.5 |
| 5beca0bd-a904-3d84-b997-63c800ae2b27 | -4.66474 | -43.1467 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 14.5 |
| e5eeeb21-a59c-3c29-9deb-57874ecf59e1 | -4.65816 | -43.11397 | 2025-10-14 05:27:00 | AQUA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 21.8 |
| 1a9fecb3-86f5-3f9a-a77b-97299639f211 | -5.4968 | -43.05486 | 2025-10-14 05:27:00 | AQUA_M-M | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 14.4 |
| 26a8c172-65b2-3465-8b02-c6dfc09af827 | -7.07937 | -41.94001 | 2025-10-14 05:27:00 | AQUA_M-M | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 403480bb-e698-339c-a317-abb0c19e8e6f | -7.73958 | -45.71657 | 2025-10-14 05:27:00 | AQUA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 27.8 |
| 61d5e51d-0dfb-3973-8b0f-43e9166fc1c9 | -7.40264 | -39.7844 | 2025-10-14 05:27:00 | AQUA_M-M | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 6.9 |
| d236a45b-c2aa-3d55-b7ea-69f79d9ce210 | -13.53586 | -43.00323 | 2025-10-14 05:29:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 10.9 |
| 267b5636-ec33-35c8-a1b3-b045658219d1 | -15.78335 | -43.28219 | 2025-10-14 05:29:00 | AQUA_M-M | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 8c581af8-cac0-341e-a8a7-a163db3578fd | -11.74238 | -43.28149 | 2025-10-14 05:29:00 | AQUA_M-M | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 27.9 |
| 770b99e0-2b3f-3899-b04c-57d7931e1e7e | 4.35516 | -60.75747 | 2025-10-14 05:42:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a0dae14-615b-340c-8431-20ca42f50167 | -2.87596 | -50.73623 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f9382be0-dd57-3e8e-8eb2-571fb8e62c33 | 1.10012 | -50.99566 | 2025-10-14 05:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 12f2ec67-a973-32f5-bfac-06554470886d | 1.10583 | -50.98851 | 2025-10-14 05:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fc77c25-8eea-3740-9eb8-5c16dc162f29 | -5.10157 | -56.15709 | 2025-10-14 05:44:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cdf86e6f-e95b-3dea-80a2-db6edad951fe | -2.87811 | -50.73367 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 516f8ad1-9159-3671-84ea-0a4d56df8431 | -2.87707 | -50.74083 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd8cd196-c985-380a-8a17-efeb1dbf1dd2 | -1.42387 | -60.40296 | 2025-10-14 05:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 420b8b5c-4d01-3457-bdbe-446e2c3029c5 | -2.88315 | -50.73732 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e35c4294-f73d-3ace-81e7-638cf49dfd67 | -1.43237 | -60.29733 | 2025-10-14 05:44:00 | NPP-375D | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ebfbee4c-0929-3509-9aef-c45437998697 | -2.88426 | -50.74196 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c2d4404-d40a-3b7f-bb4f-f61d08077af0 | 1.11156 | -50.98143 | 2025-10-14 05:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7b1acdc4-6000-32bc-b94f-800c2066b2fb | 1.09439 | -51.00265 | 2025-10-14 05:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c276dcee-4135-39ec-8da2-1913f439b23b | 1.09342 | -50.9968 | 2025-10-14 05:44:00 | NPP-375D | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 96acf84f-a6da-3178-bcf7-6ce0a18de301 | -2.88207 | -50.74445 | 2025-10-14 05:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b13d12e3-dcde-3343-8e8e-fa3870889fae | -7.4876 | -63.76841 | 2025-10-14 05:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dff1fc0-bd2e-3168-9f5b-ec9a5efbb12e | -9.22648 | -62.20366 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dd943053-142d-36e7-8d45-8aeb84305af8 | -9.41256 | -62.29448 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 467d3113-31fd-3620-9d14-e8ef8131d15f | -8.97488 | -61.97673 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 85672d32-1139-3205-b4e3-e1126ae4b0c8 | -9.17903 | -61.81027 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2f1d44fd-26d7-36b6-ba35-97ae920affa8 | -8.9587 | -62.1657 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 220ba17c-f627-3306-abe6-4a4b2125e50e | -8.84695 | -62.29683 | 2025-10-14 05:46:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3767e048-eb99-3a37-903f-861027669113 | -9.4163 | -62.29505 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed8e2cea-fb07-3661-bd5d-d7759e246704 | -9.66871 | -62.5182 | 2025-10-14 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5db04f76-a9d0-338d-a4e5-309d72585415 | -7.72192 | -55.20847 | 2025-10-14 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bd3bb05d-bca6-3bd6-926a-b020a00d82e2 | -9.66935 | -62.51384 | 2025-10-14 05:46:00 | NPP-375D | RIO CRESPO | RONDÔNIA | Brasil | 1100262 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4cfe75a-4f46-3313-b9bf-ee75cbc4e3bc | -8.84324 | -62.29626 | 2025-10-14 05:46:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a013cf37-cae3-34c1-bfb5-7e49b2505283 | -8.97867 | -61.97731 | 2025-10-14 05:46:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4911fafd-295d-3213-bb8c-e2fd88c1c842 | -14.86434 | -60.06604 | 2025-10-14 05:48:00 | NPP-375D | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 927c2d14-ac41-3bd1-ba1e-64fddf9a10e7 | -8.84619 | -62.30056 | 2025-10-14 06:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 09e1c81c-23cc-382d-91c3-3564e7e42132 | -8.97454 | -61.97723 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 251fa74c-295d-3675-aeff-f0b0611112e7 | -8.97735 | -61.97652 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 803eb9a2-b717-3563-9d39-0f1bd43b4666 | -8.9802 | -61.97801 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 26572a4d-2ff5-3b18-a4c5-851c4333f85a | -8.97685 | -61.98042 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6920b34a-56b6-3496-8b4f-2a98b807769f | -8.84067 | -62.29971 | 2025-10-14 06:05:00 | NOAA-20 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20cc7456-2471-3b8e-bd8a-418047553d80 | -8.97402 | -61.98111 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f090b4ee-7df3-37f8-ab4b-ea07587cbfa9 | -8.97967 | -61.9819 | 2025-10-14 06:05:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9611e0d9-0cb4-3b64-954c-2283bcc1aca4 | -9.0036 | -63.65451 | 2025-10-14 06:05:00 | NOAA-20 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bd427fec-05ef-34ea-b40e-914821ca2ae3 | -11.79486 | -62.75039 | 2025-10-14 06:08:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bb9882c-90e9-3c7b-87a0-75af10a46fee | -10.8093 | -43.9744 | 2025-10-14 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 88.1 |
| c5f2275f-6844-39f3-b91a-06e45eb3a3d3 | -10.8097 | -43.951 | 2025-10-14 11:50:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 200.3 |
| 255d7f8a-2c18-3f00-9ca4-a9834c080d0e | -11.1178 | -46.0739 | 2025-10-14 12:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 163.2 |
| 681f5a3f-b0a5-3800-8bbf-64e715de199f | 1.8768 | -55.7029 | 2025-10-14 12:00:00 | GOES-19 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 72.0 |
| c399a2ed-146a-33ca-880b-0f0aabf459a0 | -12.7242 | -45.1293 | 2025-10-14 12:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 86.2 |
| aaaf072e-cb74-3203-9271-984de8b79f4e | -10.8097 | -43.951 | 2025-10-14 12:00:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 152.9 |
| a559e7f8-86ab-3d29-8a12-8c26a4b3a117 | -10.8093 | -43.9744 | 2025-10-14 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 7bf10f3d-350e-3eb2-a203-69d4953d985c | -10.8097 | -43.951 | 2025-10-14 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 116.5 |
| fd80cbd7-545f-3f07-8f96-5f84044f2476 | -11.1178 | -46.0739 | 2025-10-14 12:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 165.9 |
| c6806094-38b8-37e0-83af-87f6575d5d9d | -10.8285 | -43.9717 | 2025-10-14 12:10:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 111.2 |
| 88a22a71-e3f1-3472-8cfc-19bc57ed203c | 1.87016 | -55.71885 | 2025-10-14 12:14:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 103.2 |
| 78baf097-9aee-3991-8230-486b6c271ed3 | 1.76976 | -55.77778 | 2025-10-14 12:14:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 41.7 |
| e898feb5-005b-3143-81f0-60f714e96090 | 1.86767 | -55.72483 | 2025-10-14 12:14:00 | TERRA_M-T | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 69.8 |
| ec0484b8-362e-3387-8bc2-bcc9211a892e | 1.12356 | -50.98197 | 2025-10-14 12:14:00 | TERRA_M-T | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 37b8ccaa-054a-3eec-8641-a953adb3eb45 | -7.54531 | -42.68322 | 2025-10-14 12:17:00 | TERRA_M-T | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 37.3 |
| 18304ae4-02a2-3296-b0f2-88f37503c56c | -3.904 | -40.39786 | 2025-10-14 12:17:00 | TERRA_M-T | GROAÍRAS | CEARÁ | Brasil | 2304905 | 23 | 33 | nan | nan | nan | Caatinga | 24.2 |
| d998b6a7-4ac2-356f-a821-009a1aaf0c0a | -6.45158 | -41.83219 | 2025-10-14 12:17:00 | TERRA_M-T | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 16.7 |


[Clique aqui para ver as próximas entradas](README39.md)
