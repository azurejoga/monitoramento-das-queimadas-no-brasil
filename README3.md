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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a3530e12-cafd-3658-9302-7d258d8f9adf | -9.82524 | -40.57163 | 2025-03-14 04:14:00 | NPP-375D | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 71f5235f-c841-31ca-9013-ef9cad99865d | -10.88077 | -44.17175 | 2025-03-14 04:14:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 542a18ba-42e8-3168-bbd9-f4d5da8dc880 | -7.05908 | -44.38852 | 2025-03-14 04:14:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6548b83f-10ae-3bb0-a6f1-088db2582e16 | -6.2283 | -48.05671 | 2025-03-14 04:14:00 | NPP-375D | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6543b357-5fa8-36e8-a541-c45b8751aa30 | -7.89046 | -43.54241 | 2025-03-14 04:14:00 | NPP-375D | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd7f972a-1ca5-3071-bb87-9d5740d40df2 | -6.23866 | -42.79736 | 2025-03-14 04:14:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 7b30e768-0518-3fc4-9a94-0d66e98a6c41 | -12.88362 | -44.87697 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| d6bc5d87-3e8f-348f-b227-d1813311b38c | -21.61957 | -44.18126 | 2025-03-14 04:17:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 0e079338-0247-3c59-b4e7-def76b0f0b08 | -13.90638 | -46.11649 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a10dfff7-1939-3972-b750-398b19b86a27 | -13.91312 | -46.11765 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f77b06ee-f867-3e24-8d82-2136a33660ee | -12.89415 | -44.87507 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 30b4d1a4-83c8-3e93-ab75-caf553845f35 | -13.91372 | -46.11399 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 312aea0b-6a4f-36ac-b4d8-8dd04af653ae | -11.57623 | -47.62518 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f611dc50-27ba-3cd2-b31b-8c73fe528e5c | -13.91035 | -46.11341 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 486269f6-79cb-323d-bc18-0ced399c7560 | -22.74844 | -43.27577 | 2025-03-14 04:17:00 | NPP-375D | DUQUE DE CAXIAS | RIO DE JANEIRO | Brasil | 3301702 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cd0b9f9c-598a-3f3a-940d-a2d5ddf1a3bb | -21.833 | -47.03977 | 2025-03-14 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e3ec2188-7784-3bf6-a5b2-0858fcb1045b | -22.53819 | -48.81418 | 2025-03-14 04:17:00 | NPP-375D | MACATUBA | SÃO PAULO | Brasil | 3528007 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bcc9f45b-01ab-35d3-8898-1ce97dae2cdd | -12.87754 | -44.87233 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0f336b0a-7d8a-35fb-a0f9-07f375f1905d | -15.65457 | -42.86464 | 2025-03-14 04:17:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 785f8d58-88b9-3f89-81de-269a14d50fd7 | -11.88716 | -46.94183 | 2025-03-14 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b0e9a827-cc25-3690-b921-271a5d02abf7 | -15.7151 | -41.08823 | 2025-03-14 04:17:00 | NPP-375D | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 039a0f78-a379-3f11-9842-a71bf2b8bc38 | -21.2872 | -48.61561 | 2025-03-14 04:17:00 | NPP-375D | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 99d461ed-059f-3ffa-92cd-1da5a767b833 | -13.69804 | -44.32682 | 2025-03-14 04:17:00 | NPP-375D | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bda8bb15-3900-3feb-80d2-d8bd4769ad26 | -11.5704 | -47.61528 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fa692912-7633-3471-884e-b50c7047b2ad | -21.19437 | -44.93856 | 2025-03-14 04:17:00 | NPP-375D | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 609b7064-88bc-3169-8f6b-747d2eda1ba4 | -11.56892 | -47.62391 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d9aeb0c6-4629-3497-a9ab-57509a4e1d32 | -22.78737 | -43.7558 | 2025-03-14 04:17:00 | NPP-375D | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| c9ffad6b-0abe-387e-889f-5393c535de4c | -12.89083 | -44.87452 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 6269530f-ed70-3fc6-b070-8bac7e7d2904 | -12.84799 | -43.83241 | 2025-03-14 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| cceb1f32-8226-3e16-9d38-64bff9e8def6 | -21.33189 | -48.64473 | 2025-03-14 04:17:00 | NPP-375D | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| a7d05390-c1ca-35ad-a683-b6647e873066 | -11.88395 | -46.94252 | 2025-03-14 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a5337b7-2c74-3570-9e51-2e7edd0fb348 | -12.62009 | -46.87937 | 2025-03-14 04:17:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41d2c93f-370f-3cf2-af6a-f7c1bd30ef74 | -12.8803 | -44.87642 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e9e38f1f-3d2d-3ad2-a61f-2af654dc43b1 | -12.89139 | -44.87099 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e30bb727-2fcf-3d22-8b18-084689be4563 | -11.44449 | -52.92198 | 2025-03-14 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2fbaef9a-d446-3c8e-88cc-b5e31751eca4 | -13.90975 | -46.11708 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| f4286044-e402-358f-b250-717c4d56c2c3 | -23.593 | -47.43808 | 2025-03-14 04:17:00 | NPP-375D | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 8364c617-ea61-3fe6-9df2-2f437d17ce5e | -21.83027 | -47.03543 | 2025-03-14 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 1bd7f0fe-b27d-3689-8098-d7b2797f2f2c | -21.61954 | -44.17867 | 2025-03-14 04:17:00 | NPP-375D | ANDRELÂNDIA | MINAS GERAIS | Brasil | 3102803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 60f3ea21-eec7-3816-b4c0-39ada09a40d1 | -17.59503 | -43.19894 | 2025-03-14 04:17:00 | NPP-375D | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 700ae842-ae56-357c-83fd-205797cfab0d | -11.4388 | -52.92403 | 2025-03-14 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2337a0aa-67b9-3e91-9bda-611f3dabc4d1 | -12.84854 | -43.82883 | 2025-03-14 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 22c754ed-bf64-3813-8c1a-dad41129ab9b | -21.83241 | -47.0435 | 2025-03-14 04:17:00 | NPP-375D | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7b3173e7-872a-307c-bc9f-ff68022db048 | -17.36974 | -46.07632 | 2025-03-14 04:17:00 | NPP-375D | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 155764da-2a83-3551-912c-aa321c8eec99 | -17.78012 | -42.81013 | 2025-03-14 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4fe085a3-f67b-326a-bc77-7d2f06eb667c | -11.44392 | -52.92504 | 2025-03-14 04:17:00 | NPP-375D | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 511c491e-8925-39f4-bc5f-3046b8f2b9e1 | -12.88694 | -44.87751 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 2f9eaa25-a77a-39f0-8e08-f63e96bee319 | -15.65108 | -42.86411 | 2025-03-14 04:17:00 | NPP-375D | PORTEIRINHA | MINAS GERAIS | Brasil | 3152204 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 267e767b-3729-30cf-8a44-2c723e246dd2 | -18.33407 | -40.01237 | 2025-03-14 04:17:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| dea914a4-6efd-3d49-8f66-a1cdb117e113 | -11.57258 | -47.62453 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4bfd76dc-545e-393c-bc36-1e9b511eb5ab | -11.56601 | -47.61898 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 93f6ab1e-79f5-3ffb-a99f-b265322da0c4 | -13.35686 | -41.34162 | 2025-03-14 04:17:00 | NPP-375D | IBICOARA | BAHIA | Brasil | 2912202 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| dc54945b-3363-3e22-87e8-298e1bab11d6 | -17.75342 | -42.89533 | 2025-03-14 04:17:00 | NPP-375D | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| bc50aaae-d832-3db0-af08-592abd8500b4 | -16.67987 | -43.88272 | 2025-03-14 04:17:00 | NPP-375D | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e2719bbd-23c1-3c79-af81-329bd3c5fbde | -11.56527 | -47.62331 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 21e3ec2b-32ee-3964-ba84-1bf9979a5d90 | -12.88249 | -44.88404 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e7db8f02-2c83-34f7-b5be-a4cb44a54967 | -12.89195 | -44.86744 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9929fbf7-e42f-3ff3-be29-1182745fee49 | -12.88751 | -44.87397 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 55377af5-e856-3fab-bd83-0b0bd283cd22 | -14.13521 | -41.69246 | 2025-03-14 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| da6b5b1a-5462-319e-80e1-787315535fe7 | -15.26409 | -51.47547 | 2025-03-14 04:17:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6367c5c5-0a7c-36ee-b811-be0270044e49 | -11.88364 | -46.9412 | 2025-03-14 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a21307f0-15b8-3bfb-9c15-f33f48d2695d | -23.33914 | -46.77281 | 2025-03-14 04:17:00 | NPP-375D | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 17a0abf7-fcc6-39a6-8c67-e4774efd8263 | -18.33828 | -40.01294 | 2025-03-14 04:17:00 | NPP-375D | PINHEIROS | ESPÍRITO SANTO | Brasil | 3204104 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 76a4999c-b8cc-3d1a-9ab0-9b675b9f4a42 | -14.11906 | -41.67622 | 2025-03-14 04:17:00 | NPP-375D | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 441e0361-c19a-3b93-bc1e-64c05321f001 | -21.61176 | -48.47493 | 2025-03-14 04:17:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9e91075c-49dd-37bb-ae41-93bc72ad8b8c | -12.58469 | -48.33388 | 2025-03-14 04:17:00 | NPP-375D | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b69e92a-c643-3bac-beca-01b348f1d7d2 | -22.41341 | -46.61731 | 2025-03-14 04:17:00 | NPP-375D | MONTE SIÃO | MINAS GERAIS | Brasil | 3143401 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| bcc30f82-5603-3f58-ae9d-0fd669a89011 | -15.73488 | -46.86206 | 2025-03-14 04:17:00 | NPP-375D | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fe4f6ebc-27ec-3d3e-8027-ee5fffe83452 | -12.88638 | -44.88105 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0abc45e4-f2bf-3d50-81b0-595b457f12c7 | -15.76092 | -41.42641 | 2025-03-14 04:17:00 | NPP-375D | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| f67cfdfa-6fbb-3110-abb2-52980e1d04b8 | -17.22222 | -41.21341 | 2025-03-14 04:17:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 894105ed-25ee-37e4-b734-f9e28b9af893 | -13.54818 | -43.90041 | 2025-03-14 04:17:00 | NPP-375D | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5f5b66eb-c725-3a90-adf4-752b5e85c324 | -12.89471 | -44.87153 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| fdef7d97-c69d-3483-9756-fa0f222d5b3a | -16.34873 | -43.69615 | 2025-03-14 04:17:00 | NPP-375D | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0555b52b-df38-3c36-8405-9981f79a1fab | -11.56966 | -47.6196 | 2025-03-14 04:17:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed17303e-a208-383b-963e-4a9667056f85 | -12.84465 | -43.83186 | 2025-03-14 04:17:00 | NPP-375D | SERRA DOURADA | BAHIA | Brasil | 2930303 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 5d37d4b5-3fee-33aa-9d2b-3335a4ffa29f | -12.89026 | -44.87806 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 5e366bd6-ac2f-3a07-a761-ee7a63e1c04c | -11.88784 | -46.93779 | 2025-03-14 04:17:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2203faf-2c63-30e7-abd0-2ebf97772313 | -13.90698 | -46.11283 | 2025-03-14 04:17:00 | NPP-375D | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9717d378-9886-3c60-99cc-798bc3469947 | -15.25975 | -51.47462 | 2025-03-14 04:17:00 | NPP-375D | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50f371ce-4f32-3be7-b8b0-ec0889af4e2c | -12.87974 | -44.87996 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 412f88b9-be35-3c04-b8f9-c9490bd736f7 | -12.88306 | -44.88051 | 2025-03-14 04:17:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f419e80-3f3b-3531-a8ef-e824b9a1d0a6 | -15.91504 | -43.91259 | 2025-03-14 04:17:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5e9c3824-b7cb-389c-9ba0-b1cd24abcc44 | -13.46993 | -41.77191 | 2025-03-14 04:17:00 | NPP-375D | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 4993a443-d015-3ba7-ac6e-9c855eb779d2 | -20.54502 | -45.9747 | 2025-03-14 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b4d93fd9-c15d-32f8-9c0e-3e98b4f5bb00 | -18.30042 | -54.57426 | 2025-03-14 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e1e48a50-a1a7-331e-9f90-63b2f9cb29bb | -20.0529 | -40.33641 | 2025-03-14 04:19:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 30448b45-766c-3e59-88d7-f07a43784e89 | -20.41632 | -43.55187 | 2025-03-14 04:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 6390a3f0-f0fc-33d8-bbb7-57b88c19cac9 | -20.76195 | -46.77037 | 2025-03-14 04:19:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 179b2fb5-2082-38d9-adb5-64a053d4189a | -20.54559 | -45.97102 | 2025-03-14 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5b48d995-0bba-3cd4-b649-7d652588c32b | -20.0534 | -40.33231 | 2025-03-14 04:19:00 | NPP-375D | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2313fbc9-3124-3ead-bc82-2065a3a03142 | -30.14137 | -52.60476 | 2025-03-14 04:19:00 | NPP-375D | RIO PARDO | RIO GRANDE DO SUL | Brasil | 4315701 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| d7154097-d968-35d5-b022-0cb87a461b09 | -18.30607 | -54.57231 | 2025-03-14 04:19:00 | NPP-375D | COXIM | MATO GROSSO DO SUL | Brasil | 5003306 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eccbe3a4-1f51-3b7c-8192-af7771e6924c | -19.38239 | -43.66423 | 2025-03-14 04:19:00 | NPP-375D | JABOTICATUBAS | MINAS GERAIS | Brasil | 3134608 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 23367c3f-e2c3-3a03-b208-53d6166e0596 | -19.7051 | -44.76981 | 2025-03-14 04:19:00 | NPP-375D | ONÇA DE PITANGUI | MINAS GERAIS | Brasil | 3145802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 9d7dd698-f8ff-354c-9f5e-65969e318e9d | -20.54834 | -45.97528 | 2025-03-14 04:19:00 | NPP-375D | PIUMHI | MINAS GERAIS | Brasil | 3151503 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f8046e99-75b0-3ade-9425-de502da1e16e | -19.34441 | -53.76689 | 2025-03-14 04:19:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d52eb38e-9a31-3b58-a9ba-ca0fba0a27d7 | -20.76527 | -46.77096 | 2025-03-14 04:19:00 | NPP-375D | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| db1b1cbc-719f-381c-85f9-e3edbc53e922 | -20.41862 | -43.55106 | 2025-03-14 04:19:00 | NPP-375D | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 8b7c2d2d-93c6-34ab-9ffd-a7c8afee209b | -7.0559 | -44.39016 | 2025-03-14 04:36:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README4.md)
