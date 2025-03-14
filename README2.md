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
| ed314072-b8b3-3b03-a662-f5a136f9562d | -15.15739 | -40.24584 | 2025-03-14 03:49:00 | NOAA-21 | ITAMBÉ | BAHIA | Brasil | 2915809 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 566ad6d7-0325-345c-a7e0-60bdf7bf2bdd | -11.93911 | -41.26786 | 2025-03-14 03:49:00 | NOAA-21 | BONITO | BAHIA | Brasil | 2904050 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a1f69660-1ac8-38da-aa72-ce83e1b7df23 | -13.47027 | -41.77188 | 2025-03-14 03:49:00 | NOAA-21 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 38f9efa0-e85c-34b2-8671-3dea1661cf24 | -12.70125 | -38.168 | 2025-03-14 03:49:00 | NOAA-21 | CAMAÇARI | BAHIA | Brasil | 2905701 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0d1e80f8-7dde-30d4-acb2-dd58046707b6 | -12.87999 | -44.88107 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 469e420e-0d0f-349b-9393-cd1a405210bf | -9.02889 | -40.58443 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| c4828030-7554-3794-aff2-b0f0d89e24cf | -11.35009 | -47.55173 | 2025-03-14 03:49:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 868bd3bd-043b-3b62-872a-50a3c332fce9 | -11.95724 | -37.83469 | 2025-03-14 03:49:00 | NOAA-21 | ESPLANADA | BAHIA | Brasil | 2910602 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6c67fbd4-ff00-3847-adea-bb5cdf49aed2 | -11.88814 | -46.93985 | 2025-03-14 03:49:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b99fc66e-ada1-3e41-abcb-797ec64f3353 | -9.02528 | -40.58384 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.6 |
| 7565969b-1ed9-359c-b306-1c6e3548d60f | -12.88081 | -44.87664 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 71ca0a4f-7968-3a54-9711-aa9141025807 | -7.88991 | -43.5438 | 2025-03-14 03:49:00 | NOAA-21 | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 816fa2b3-a33d-3954-8725-451a1f9d5bb1 | -13.35788 | -41.34035 | 2025-03-14 03:49:00 | NOAA-21 | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| f68285fe-61ef-3196-81e3-07b9cffd70bf | -10.30517 | -38.75336 | 2025-03-14 03:49:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 7b2ab384-17c8-37a6-a95c-2ef3ec4c87c4 | -10.14375 | -42.16724 | 2025-03-14 03:49:00 | NOAA-21 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 940272b6-dbd9-3165-894e-ab41e9932e78 | -9.02766 | -40.57935 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6819b9b7-3a4f-3905-96e0-3eefd06206c6 | -9.02596 | -40.57967 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| d9da9f65-6d93-3e17-8836-62c671419758 | -12.88441 | -44.88185 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 0667c52f-5823-33df-a485-4e2173ae93a4 | -11.56527 | -47.61859 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7b9e187a-3538-37e9-b31d-1227177063ea | -11.57286 | -47.6167 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44f2e6de-fc2b-33ae-85b9-d4bda377988c | -11.57544 | -47.62414 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 38b25568-ebdf-36b7-ab49-13186ffb8fc1 | -11.96155 | -47.01145 | 2025-03-14 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e93e0e12-86f1-3747-a18d-35b27495d4e4 | -14.2052 | -47.021 | 2025-03-14 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d2f77df-6315-343f-ac5e-4b764f28b34f | -15.71494 | -41.08944 | 2025-03-14 03:49:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 31a4e48b-d760-3070-8071-7ece578838bc | -12.84475 | -43.83179 | 2025-03-14 03:49:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 9e7c5faa-08a2-37d0-a432-d4fde6a487e4 | -11.96216 | -47.00826 | 2025-03-14 03:49:00 | NOAA-21 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 1b931138-6e6f-3da3-b56f-d68a09156f49 | -9.76714 | -37.66132 | 2025-03-14 03:49:00 | NOAA-21 | POÇO REDONDO | SERGIPE | Brasil | 2805406 | 28 | 33 | nan | nan | nan | Caatinga | 2.1 |
| e8ce796f-e511-37f8-9dcc-1a8f2c78c52b | -14.20576 | -47.01811 | 2025-03-14 03:49:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f624b072-ce90-3c9a-96fd-1af58adb678e | -11.56459 | -47.62217 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 9dce1389-b137-3118-b79a-c8b692b648c1 | -12.88523 | -44.87742 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| da9807f0-1023-37fa-b530-47e3b5d02ba5 | -12.84888 | -43.83253 | 2025-03-14 03:49:00 | NOAA-21 | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 62506a20-5c4f-3fd9-b9db-2e495bd7986f | -12.89126 | -44.8694 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a31a2cc5-3c2f-3fe4-a8d4-5e4842bc99e1 | -9.02956 | -40.58027 | 2025-03-14 03:49:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 5.2 |
| fc146aea-1393-343e-b2af-f0572c0f174a | -11.57069 | -47.61956 | 2025-03-14 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d329d4aa-964e-3493-98c0-cb057c80b165 | -12.89045 | -44.8738 | 2025-03-14 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 17.8 |
| a9821a06-6e66-3af8-895a-b3222c46f618 | -8.87836 | -36.53082 | 2025-03-14 03:49:00 | NOAA-21 | GARANHUNS | PERNAMBUCO | Brasil | 2606002 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 586b3ec0-eab8-3116-bc0f-19234694f3d5 | -20.41801 | -43.55164 | 2025-03-14 03:51:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 0ba46bd9-8e8c-3f40-b9d6-fa8f48bc1af9 | -17.75205 | -42.89282 | 2025-03-14 03:51:00 | NOAA-21 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eaeeca86-6204-3045-a595-486803aeea35 | -18.33239 | -40.01317 | 2025-03-14 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 154c7c71-3a9a-30f0-8954-71397fa487cf | -22.69655 | -43.43176 | 2025-03-14 03:51:00 | NOAA-21 | NOVA IGUAÇU | RIO DE JANEIRO | Brasil | 3303500 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 18a9ae73-d37c-3b19-9375-f8cef8a1d518 | -19.61957 | -40.26255 | 2025-03-14 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 18f746fc-1023-3472-aed5-b7a152f56c72 | -18.04006 | -39.92562 | 2025-03-14 03:51:00 | NOAA-21 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 3c6f6a13-dd2a-364a-969a-e15356a0131a | -20.76587 | -46.76958 | 2025-03-14 03:51:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dafb7d88-cafa-3ad7-8b1a-afe1a621c670 | -18.16405 | -41.2682 | 2025-03-14 03:51:00 | NOAA-21 | ATALÉIA | MINAS GERAIS | Brasil | 3104700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 461f07ac-9829-3c21-9332-eb271b4823d3 | -15.7631 | -41.42895 | 2025-03-14 03:51:00 | NOAA-21 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 5c488dc8-987e-353f-a7fa-2734a6f16d23 | -15.65456 | -42.86201 | 2025-03-14 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 4d516a51-f0d8-3668-bad0-5e9671318eeb | -15.65375 | -42.86666 | 2025-03-14 03:51:00 | NOAA-21 | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 01245639-bf29-3f02-a898-392a27ee2bdb | -16.48377 | -39.07397 | 2025-03-14 03:51:00 | NOAA-21 | PORTO SEGURO | BAHIA | Brasil | 2925303 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f4c99e6a-c9d2-39b6-8ba1-924e725849bf | -15.9157 | -43.91539 | 2025-03-14 03:51:00 | NOAA-21 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 070accf8-4608-3880-bc42-95f18b7bd9ff | -17.3697 | -46.07542 | 2025-03-14 03:51:00 | NOAA-21 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 63d4469c-3c2a-3d24-994f-451ade724619 | -19.83378 | -40.11209 | 2025-03-14 03:51:00 | NOAA-21 | ARACRUZ | ESPÍRITO SANTO | Brasil | 3200607 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1b89b866-e03a-375e-b47b-eb319da1d647 | -18.33902 | -40.01432 | 2025-03-14 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 4.0 |
| 2e59c1db-ae15-3806-b3b3-099939110906 | -20.05373 | -40.33511 | 2025-03-14 03:51:00 | NOAA-21 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 1d8e7b6d-afd2-34d0-a906-95edf705f827 | -17.09612 | -43.80286 | 2025-03-14 03:51:00 | NOAA-21 | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f91258a7-ec6d-3d21-b469-d770c3377a57 | -19.70594 | -44.76855 | 2025-03-14 03:51:00 | NOAA-21 | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| daa9cb41-4eee-3ab2-aa9d-eba102a7d51d | -15.26529 | -51.47597 | 2025-03-14 03:51:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e36d7d03-41ad-3e80-bc5b-94ffd63aebbb | -18.6097 | -44.25822 | 2025-03-14 03:51:00 | NOAA-21 | INIMUTABA | MINAS GERAIS | Brasil | 3131109 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| f801e2de-6e9f-3865-8b3e-6296bcea052e | -16.68066 | -43.88489 | 2025-03-14 03:51:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce24af4f-e0d7-3a16-b284-dd628eac6d5d | -18.37199 | -39.95661 | 2025-03-14 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 528d6549-04bc-3842-bc65-027616c4b04e | -22.78473 | -43.75793 | 2025-03-14 03:51:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 89ec219a-4db8-302d-afeb-e372888a709c | -18.3357 | -40.01374 | 2025-03-14 03:51:00 | NOAA-21 | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 8a7359e4-22ed-3680-bde2-dfbae5a4cf7a | -17.22421 | -41.2128 | 2025-03-14 03:51:00 | NOAA-21 | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| c4f999d2-41b4-3559-9e59-c7eb8c2b26ad | -21.61396 | -48.4744 | 2025-03-14 03:51:00 | NOAA-21 | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d15644dd-bea9-33bc-836e-6c962ece46b6 | -22.53841 | -48.81162 | 2025-03-14 03:53:00 | NOAA-21 | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 77d308af-695b-351e-8bbb-f26de9c16037 | -22.617 | -47.45887 | 2025-03-14 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 76d858d0-2c57-32d6-b81a-8bb282e1dbb7 | -23.40535 | -46.55676 | 2025-03-14 03:53:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 6280fc9a-0aca-3bb0-b2af-f49009357255 | -22.61635 | -47.46076 | 2025-03-14 03:53:00 | NOAA-21 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 48f5fc9f-03d0-3ea6-8f9b-eaaffb7e6713 | -6.52229 | -43.63515 | 2025-03-14 04:14:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 69106e22-f08f-3ef4-b95d-7a56af6a42a2 | -6.22547 | -48.04879 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 997e6be6-7252-3253-9854-1e13e9d9682a | -10.14132 | -42.16936 | 2025-03-14 04:14:00 | NPP-375D | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 5b36594c-9b4e-309b-901f-7b4f6d8e6b1b | -7.24551 | -44.77289 | 2025-03-14 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 74c4e2ec-7aea-3f82-b2e5-15d013ecc76b | -9.82952 | -40.56792 | 2025-03-14 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 869e0e05-f2a6-36ef-b233-b908ab6d7ab1 | -9.28497 | -48.32145 | 2025-03-14 04:14:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 45a41ea7-96ed-3da7-a1ed-152adda9e8c6 | -7.24948 | -44.76981 | 2025-03-14 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23d91e00-922d-3598-97be-eee012677153 | -9.02737 | -40.58191 | 2025-03-14 04:14:00 | NPP-375D | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 10.6 |
| b18e6a7e-49e7-3011-baed-3eea499ce446 | -6.23293 | -48.05389 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 18583180-7de2-317c-a3b1-4907660598f5 | -6.2492 | -48.03084 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 90212cd8-7f69-3634-bab6-7c73ae192360 | -8.63485 | -40.44318 | 2025-03-14 04:14:00 | NPP-375D | DORMENTES | PERNAMBUCO | Brasil | 2605152 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6ef85ab4-56e4-3b78-8782-979934e36066 | -7.88991 | -43.54588 | 2025-03-14 04:14:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bace864-b090-3264-9ddc-b9f8257790d4 | -6.22891 | -48.05308 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 1067e188-b52f-320e-9b11-8d171563fea9 | -6.10267 | -42.66942 | 2025-03-14 04:14:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1b102c32-d01f-3fb6-95fb-18dd7b4984ac | -6.97923 | -35.19722 | 2025-03-14 04:14:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 3efc7de1-a582-3e6f-880c-0a57dae18f63 | -6.25206 | -48.03859 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| db1e3bb5-0ec5-350f-987a-30d93eca734d | -6.2295 | -48.04953 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 83f5c74b-c55c-3473-8eea-5fb8e51582c1 | -6.22487 | -48.05238 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5a039318-49f8-3d87-850c-5958bafa8e46 | -6.96165 | -42.80109 | 2025-03-14 04:14:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 8ef37faa-691f-3a97-aa52-257ceff92361 | -6.63706 | -47.85822 | 2025-03-14 04:14:00 | NPP-375D | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f4b8076-311f-3acc-a3ff-e5c4e6d0b7c0 | -6.97427 | -35.19649 | 2025-03-14 04:14:00 | NPP-375D | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 6664fe32-2594-3e23-9254-bd148e5d7918 | -5.44762 | -45.42956 | 2025-03-14 04:14:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2fe9e154-5d15-3df3-b6cf-79acc8eb19d5 | -7.24096 | -44.7796 | 2025-03-14 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2edc012b-8871-3a9f-b00a-926f8b5a5533 | -9.82888 | -40.57219 | 2025-03-14 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 322400d6-a3a2-3175-8c22-9d1ac7fd492d | -7.24154 | -44.77597 | 2025-03-14 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1749863a-25f5-3648-bc3b-18fd7ec131ae | -7.24493 | -44.77651 | 2025-03-14 04:14:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| af319869-44af-3399-97b1-5e5f24b24c28 | -10.30335 | -38.75106 | 2025-03-14 04:14:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bf319364-5552-3a18-8ed0-b64ca511d36c | -6.23352 | -48.0503 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5a8a739-e33e-3c75-ae22-6349ae0b4dca | -10.30744 | -38.7516 | 2025-03-14 04:14:00 | NPP-375D | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 7b3e5aa1-4111-3261-8490-87cba7c7fb58 | -8.10901 | -43.14585 | 2025-03-14 04:14:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| edad8304-eda3-3e2d-bd02-98c15b1eea1a | -6.23232 | -48.0575 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f7d364a9-8c6d-38ac-a6e6-6a7c40fc3e30 | -5.4441 | -45.42898 | 2025-03-14 04:14:00 | NPP-375D | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 9e35e3c2-a32c-3a50-9aeb-8215fd82b93d | -6.08389 | -42.68069 | 2025-03-14 04:14:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README3.md)
