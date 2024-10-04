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

## Dados Diários - Página 187

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1abcaf36-3086-3a52-b2eb-cd1e40b070be | -7.67105 | -45.21512 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 173.0 |
| 6767be11-1588-37a7-a7c1-d43e7446ec11 | -7.66472 | -45.25331 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 53.9 |
| 1d579f28-9064-378f-b1aa-756aa9aeef39 | -7.65736 | -45.21884 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 7429722e-5c56-3f49-baf6-8556b08dea05 | -7.86789 | -45.33992 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 48.1 |
| c23b7454-fc43-35cb-b779-a9ba596661b1 | -7.86028 | -45.30526 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 84.1 |
| 956b66ca-853a-3088-8835-bb751dfe17ab | -7.8538 | -45.34299 | 2024-10-04 11:57:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 182.4 |
| 9e02f4d7-36a1-3b34-87e8-a82f0b5a078d | -8.57571 | -44.07165 | 2024-10-04 11:57:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b6afbd57-acd0-3f16-8375-2444488a7230 | -8.57213 | -44.07687 | 2024-10-04 11:57:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 141.5 |
| 95453513-acba-3e44-97a6-142fc4549170 | -8.56044 | -44.06884 | 2024-10-04 11:57:00 | TERRA_M-M | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 165.3 |
| 43efa18d-744e-3055-a14b-231f981884e6 | -10.90085 | -46.61233 | 2024-10-04 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| 7dae8028-ac20-3f9c-a662-2b5ac5b584c7 | -10.79891 | -45.57656 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 6db14f8c-3752-32af-b410-a32dd2a4bd97 | -10.89327 | -46.65489 | 2024-10-04 11:57:00 | TERRA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 59.1 |
| 3ca76b0c-0ac4-3053-b1e4-13b09458f0f1 | -10.72229 | -46.17339 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 251.8 |
| 27ec0881-04de-37e0-8900-771f063d8d76 | -10.72362 | -46.1818 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 228.5 |
| b818b97e-8c56-333b-9d97-e0ba1a327d32 | -10.72902 | -46.13485 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 257.3 |
| 00a989e1-099b-36e7-803d-32e50cdb7de3 | -10.73066 | -46.14295 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 512.0 |
| 4311ec05-7c37-3aca-a87d-6cdf4b97ad30 | -10.73921 | -46.1778 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 970.5 |
| 770a3911-d40b-309c-a64d-bb8b56dc5e20 | -10.74057 | -46.18597 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 493.3 |
| a04f1afa-0227-30dd-a416-778d5c12ac94 | -10.74606 | -46.13826 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 764.6 |
| 25375ce0-7887-3fbb-a582-08171f221682 | -10.74769 | -46.14644 | 2024-10-04 11:57:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 788.5 |
| ac7cd666-eb65-3463-a9b3-e5dec763f9b5 | -14.21207 | -40.23341 | 2024-10-04 12:00:00 | TERRA_M-T | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 6c148628-49ca-3232-8956-604f560063ac | -16.26042 | -40.3202 | 2024-10-04 12:00:00 | TERRA_M-T | JACINTO | MINAS GERAIS | Brasil | 3134707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.0 |
| d27f6d19-e1d0-38a9-959f-71585a4345cd | -16.13966 | -39.79434 | 2024-10-04 12:00:00 | TERRA_M-T | ITAGIMIRIM | BAHIA | Brasil | 2915304 | 29 | 33 | nan | nan | nan | Mata Atlântica | 24.1 |
| 8ddbe3f5-e380-3b18-8aa7-e545c330e1c7 | -15.42334 | -39.84378 | 2024-10-04 12:00:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| 7b61d55d-256f-3389-b85c-f29a70a174ac | -15.22197 | -39.95045 | 2024-10-04 12:00:00 | TERRA_M-T | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 16.7 |
| a73ead2b-e1d0-357f-8251-a4a6059c231f | -17.90143 | -40.12077 | 2024-10-04 12:00:00 | TERRA_M-T | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 10.9 |
| 2243509f-46cc-3ae9-8ba6-a3c85931f511 | -16.8915 | -40.60702 | 2024-10-04 12:00:00 | TERRA_M-T | SANTA HELENA DE MINAS | MINAS GERAIS | Brasil | 3157658 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.4 |
| a841be60-d181-3689-b72d-b7e9ab7ec41f | -16.62707 | -41.03737 | 2024-10-04 12:00:00 | TERRA_M-T | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 4d7b287d-cacc-356e-becd-01a3b1895602 | -15.19352 | -41.00407 | 2024-10-04 12:00:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 17.3 |
| 8dbf6423-71cb-3c63-b0e0-74dedcde05ba | -15.18972 | -40.99739 | 2024-10-04 12:00:00 | TERRA_M-T | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 23.8 |
| 9df62062-7597-330a-b1ae-bcef0d890533 | -14.91188 | -41.78933 | 2024-10-04 12:00:00 | TERRA_M-T | PIRIPÁ | BAHIA | Brasil | 2924702 | 29 | 33 | nan | nan | nan | Caatinga | 45.9 |
| 51678248-3217-31c9-b13a-257496d02486 | -14.40809 | -42.18597 | 2024-10-04 12:00:00 | TERRA_M-T | CACULÉ | BAHIA | Brasil | 2905008 | 29 | 33 | nan | nan | nan | Caatinga | 25.3 |
| 42cc288d-45aa-3d68-a358-489a3647a0db | -14.30135 | -41.30142 | 2024-10-04 12:00:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| ad378a15-a278-3a13-aaad-b5dc8a095dbc | -14.30122 | -41.2948 | 2024-10-04 12:00:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 23.0 |
| cce69b06-154a-34ec-aed7-a9bc4f42df3a | -14.29891 | -41.30914 | 2024-10-04 12:00:00 | TERRA_M-T | ARACATU | BAHIA | Brasil | 2902005 | 29 | 33 | nan | nan | nan | Caatinga | 19.8 |
| ccca8d25-bcf2-3b78-9aa0-cca31390a18e | -14.23047 | -40.8852 | 2024-10-04 12:00:00 | TERRA_M-T | CAETANOS | BAHIA | Brasil | 2905156 | 29 | 33 | nan | nan | nan | Caatinga | 41.1 |
| d78f73d1-7ce3-32db-89d8-5083e476af8c | -16.25539 | -42.17144 | 2024-10-04 12:00:00 | TERRA_M-T | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 17.2 |
| 4f6997bd-5c69-3e95-916c-f694d1b59045 | -18.97671 | -43.2099 | 2024-10-04 12:00:00 | TERRA_M-T | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.5 |
| 8c89a840-de22-3517-a28e-7ec39931f283 | -18.97148 | -43.21593 | 2024-10-04 12:00:00 | TERRA_M-T | DOM JOAQUIM | MINAS GERAIS | Brasil | 3122603 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.3 |
| b87991ed-5680-3bfc-a2ab-91b57cce6853 | -18.59283 | -42.47694 | 2024-10-04 12:00:00 | TERRA_M-T | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 24.8 |
| f3402515-d08f-3a9e-91bd-e515d71c07d5 | -18.54233 | -42.23086 | 2024-10-04 12:00:00 | TERRA_M-T | COROACI | MINAS GERAIS | Brasil | 3119203 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.9 |
| 4d540353-09a0-35f2-a5b5-ec3924810251 | -13.28773 | -42.34628 | 2024-10-04 12:00:00 | TERRA_M-T | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 50.9 |
| 6e26c111-6674-3321-949e-3aad5b0c3137 | -12.9333 | -42.89532 | 2024-10-04 12:00:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 32.2 |
| fdbf5c07-45b2-3a3f-8e6b-858ffbd53394 | -12.93143 | -42.90233 | 2024-10-04 12:00:00 | TERRA_M-T | MACAÚBAS | BAHIA | Brasil | 2919801 | 29 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 3d79c171-b926-3922-8d86-4479b1f66b14 | -14.3469 | -42.47718 | 2024-10-04 12:00:00 | TERRA_M-T | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 18.2 |
| 8e5c4b48-dbe5-3a1d-8831-b6042fe600a9 | -14.31849 | -42.39365 | 2024-10-04 12:00:00 | TERRA_M-T | IBIASSUCÊ | BAHIA | Brasil | 2912004 | 29 | 33 | nan | nan | nan | Caatinga | 17.2 |
| 29398782-be53-314b-8c33-8e5232ae920e | -16.30272 | -43.66746 | 2024-10-04 12:00:00 | TERRA_M-T | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 76396229-1aa2-3c9a-b55e-a65bc6ee556b | -16.11349 | -43.99201 | 2024-10-04 12:00:00 | TERRA_M-T | PATIS | MINAS GERAIS | Brasil | 3147956 | 31 | 33 | nan | nan | nan | Cerrado | 39.5 |
| d685513f-571c-35a2-bfce-b283279deec5 | -15.41165 | -43.78929 | 2024-10-04 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 49.9 |
| 3ca2c463-b1a3-3494-8be6-9330d73d1202 | -15.37235 | -43.79718 | 2024-10-04 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0a957dcb-9bbb-3670-b02f-80b54837ab7b | -15.36847 | -43.80343 | 2024-10-04 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 30.8 |
| e0e82f9a-29b4-350f-892d-049a315d926a | -15.35922 | -43.79469 | 2024-10-04 12:00:00 | TERRA_M-T | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 40.5 |
| 3dff3879-63c2-3425-ba3c-f1eb6c8633d5 | -17.6939 | -43.78104 | 2024-10-04 12:00:00 | TERRA_M-T | BOCAIÚVA | MINAS GERAIS | Brasil | 3107307 | 31 | 33 | nan | nan | nan | Cerrado | 20.4 |
| 9aa0b76d-90bf-3974-bd7a-030b08172639 | -19.23316 | -43.3726 | 2024-10-04 12:00:00 | TERRA_M-T | MORRO DO PILAR | MINAS GERAIS | Brasil | 3143708 | 31 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 67a4db38-a7d6-31dd-bcc2-7e6306e1ae72 | -18.8604 | -43.5976 | 2024-10-04 12:00:00 | TERRA_M-T | CONCEIÇÃO DO MATO DENTRO | MINAS GERAIS | Brasil | 3117504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 28.5 |
| 82bf1a2e-eda5-3f22-a5c1-6f5b252cc01b | -18.33319 | -44.0386 | 2024-10-04 12:00:00 | TERRA_M-T | MONJOLOS | MINAS GERAIS | Brasil | 3142502 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0dae95d4-c01f-3bfa-b019-7f050d9d0f7b | -20.35424 | -44.83001 | 2024-10-04 12:00:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 5687f42a-b8b7-3e02-bb9f-1fa3ac43081d | -20.35238 | -44.84443 | 2024-10-04 12:00:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 107.8 |
| f08db16d-c747-327c-a3e0-0accca7b4b79 | -20.35029 | -44.8511 | 2024-10-04 12:00:00 | TERRA_M-T | CLÁUDIO | MINAS GERAIS | Brasil | 3116605 | 31 | 33 | nan | nan | nan | Cerrado | 56.2 |
| c7ef3ffc-26e6-34af-bc7e-6a7f378c4070 | -21.50345 | -45.33023 | 2024-10-04 12:00:00 | TERRA_M-T | VARGINHA | MINAS GERAIS | Brasil | 3170701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 22.3 |
| 1a9341a9-c990-3fa9-9950-377ce9aa37b1 | -17.37616 | -44.90086 | 2024-10-04 12:00:00 | TERRA_M-T | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 6833bac5-43f0-333d-a33c-400def1fd2bf | -19.61307 | -46.28555 | 2024-10-04 12:00:00 | TERRA_M-T | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 078d2a53-d305-3630-9e97-b20e96002fe7 | -19.61213 | -46.27933 | 2024-10-04 12:00:00 | TERRA_M-T | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 61.3 |
| 50cbf241-1afc-3926-b87f-cbeed8c5166d | -15.61502 | -47.21033 | 2024-10-04 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 117.0 |
| f49bb2ea-b0b2-33fb-8004-3ba935c5ab60 | -15.62894 | -47.2051 | 2024-10-04 12:00:00 | TERRA_M-T | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 105.0 |
| 156cb842-ea6e-3f5b-b50d-e5dc13b0ec53 | -21.83159 | -48.39769 | 2024-10-04 12:00:00 | TERRA_M-T | GAVIÃO PEIXOTO | SÃO PAULO | Brasil | 3516853 | 35 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 1fec2f24-890d-3df5-8b4f-49d8b580d441 | -21.84115 | -48.39262 | 2024-10-04 12:00:00 | TERRA_M-T | ARARAQUARA | SÃO PAULO | Brasil | 3503208 | 35 | 33 | nan | nan | nan | Cerrado | 62.1 |
| cb44ebad-1384-3b79-834a-75b55be1fb2a | -16.94398 | -47.14589 | 2024-10-04 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 155.7 |
| 59b0afd9-25f9-37b4-97c6-7ec85362ac38 | -16.94967 | -47.1549 | 2024-10-04 12:00:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 81.8 |
| 1733fbbc-9270-3c5e-835a-0ee988b162a1 | -17.60525 | -46.97037 | 2024-10-04 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 26a39077-b5f5-334c-8ac6-4f06acdbf2f3 | -17.61346 | -46.9778 | 2024-10-04 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 54.5 |
| 20af4756-a392-3747-aa82-052a8d92bf6d | -17.62105 | -46.97403 | 2024-10-04 12:00:00 | TERRA_M-T | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 33.4 |
| cb156793-b226-37bb-89ba-791a2f38c94f | -13.13672 | -46.33409 | 2024-10-04 12:00:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 152.0 |
| f9585eea-632f-39a2-9e1f-9a88649e0d74 | -13.14845 | -46.33 | 2024-10-04 12:00:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 309.0 |
| 9b716076-7d89-3864-bed4-de2f4994eecb | -13.15334 | -46.33689 | 2024-10-04 12:00:00 | TERRA_M-T | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 155.2 |
| 52d23008-50cf-3166-8239-e1724da128be | -13.19296 | -45.48363 | 2024-10-04 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 337d125e-5911-3f87-8187-140ddcfea92a | -13.20252 | -45.49285 | 2024-10-04 12:00:00 | TERRA_M-T | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 43.0 |
| 06e49b9a-6135-3d1c-8efe-9b1bb55a74d8 | -10.75 | -46.17 | 2024-10-04 12:04:23 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 399cfdd3-c5ad-3969-88da-f71a3e366ae8 | -6.61 | -41.98 | 2024-10-04 12:04:47 | MSG-03 | NOVO ORIENTE DO PIAUÍ | PIAUÍ | Brasil | 2206902 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a01b555a-0517-3ca0-b13c-01ffd77915e2 | -6.64 | -42.03 | 2024-10-04 12:04:47 | MSG-03 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| a9915008-a26d-3996-bb47-2243d2acbd4d | -6.64 | -41.99 | 2024-10-04 12:04:47 | MSG-03 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 651f3a33-c7a7-3ffe-bbec-5d5e13e6a0f4 | -5.71 | -43.81 | 2024-10-04 12:04:55 | MSG-03 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 38af370a-4084-37b6-9b58-ea09efa171a2 | -10.2761 | -47.6995 | 2024-10-04 12:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 57.9 |
| c9ef05b9-2416-3450-855c-988cc18461b2 | -10.2378 | -47.726 | 2024-10-04 12:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 100.7 |
| c8adb4b3-3e1d-352c-b357-3d109f8dfd65 | -10.2571 | -47.7017 | 2024-10-04 12:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 183.3 |
| 2f9dec02-b216-34c6-95f8-ee0e33982762 | -10.2381 | -47.7038 | 2024-10-04 12:06:04 | GOES-16 | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 73.6 |
| f1b301f3-a4c1-39d8-9d6a-2f88a0b72947 | -10.7168 | -46.1489 | 2024-10-04 12:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 101.7 |
| ce516e8e-ecda-3538-ae58-548900cbb263 | -10.7165 | -46.1716 | 2024-10-04 12:06:06 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 97.5 |
| dab9eaab-3f78-341a-a78d-68ef75f517db | -10.7355 | -46.1692 | 2024-10-04 12:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 416.6 |
| ca9bdf93-7f4b-3eb6-9022-737115572116 | -10.8021 | -45.5698 | 2024-10-04 12:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 91.3 |
| 7c125a9f-8ebe-3590-91f0-9325c1bb5a80 | -10.7309 | -47.7126 | 2024-10-04 12:06:07 | GOES-16 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 76.8 |
| b4cf71ac-25e0-3a5e-95de-9314bea7a62a | -10.7359 | -46.1465 | 2024-10-04 12:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 296.0 |
| 59e36bec-c02e-3b1a-bad5-c126764806f3 | -10.8018 | -45.5927 | 2024-10-04 12:06:07 | GOES-16 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 18d7e121-8180-3fa5-92a1-e7ca24a2f089 | -10.8992 | -46.6442 | 2024-10-04 12:06:08 | GOES-16 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 117.7 |
| f6a7001f-9c4e-3ca7-8e99-1cb042329ae9 | -11.2369 | -46.9597 | 2024-10-04 12:06:09 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 245.9 |
| 7d5a6fde-59e5-349e-a528-697daa428794 | -11.2971 | -43.4088 | 2024-10-04 12:06:09 | GOES-16 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 97.0 |
| 2f871114-fdfe-352c-8374-4efbbcb2afcb | -11.3341 | -46.8349 | 2024-10-04 12:06:10 | GOES-16 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 116.3 |
| df8b2d01-e9d3-3b09-aa69-877d64dcb241 | -11.404 | -47.2287 | 2024-10-04 12:06:10 | GOES-16 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 82.0 |
| f11d1c97-e79c-39eb-8c00-b97b5a7aaa1e | -13.0598 | -51.1195 | 2024-10-04 12:06:20 | GOES-16 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 221.3 |
| a84a4145-5a8e-3e3c-bc82-3a86d2630755 | -13.1587 | -48.6764 | 2024-10-04 12:06:20 | GOES-16 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 80.3 |


[Clique aqui para ver as próximas entradas](README188.md)
