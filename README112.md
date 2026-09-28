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

## Dados Diários - Página 112

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 25ed9fe2-960b-321e-b519-506b06b208cb | -10.78913 | -48.73903 | 2026-09-28 16:26:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e4061d44-3575-37e2-874a-d4f3fbb6e8f9 | -8.03863 | -54.894 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| cfc444b0-2bef-3360-8c7b-3a2c49bf7b15 | -7.28538 | -44.30527 | 2026-09-28 16:26:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 6.8 |
| cc8b8076-b1f3-330f-be37-b82148aecb29 | -7.5155 | -44.8896 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f6bf7484-0140-3dc2-9e04-cb39b10f99e3 | -9.27115 | -40.8119 | 2026-09-28 16:26:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 7db159ad-513d-3f64-998a-c9ab3d024bbe | -4.32506 | -48.6328 | 2026-09-28 16:26:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 07a8bc96-5ced-3494-92e6-3382a460ae0f | -8.03357 | -42.84968 | 2026-09-28 16:26:00 | NOAA-20 | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | 8.8 |
| dce3d2b5-f1de-32e5-97cc-7ba87efc31d7 | -6.99597 | -42.699 | 2026-09-28 16:26:00 | NOAA-20 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 19afd3d8-9621-3281-9b70-85fdcc1a5d5d | -8.3906 | -45.47115 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 08c947d6-4911-353c-b8e1-92a44daa324f | -10.50936 | -51.28805 | 2026-09-28 16:26:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2e4563b2-f5e8-3f7d-8ead-85cd5b7a9a0a | -7.41137 | -42.619 | 2026-09-28 16:26:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 4.2 |
| ad023abd-7e80-3f94-b895-e705293ed23e | -7.5077 | -44.57957 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 110c9e76-43d1-3d1b-a997-040cf7339cbe | -10.26861 | -44.62413 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 9984e6d7-8294-3f5e-9a9c-3ef0c6da816f | -6.55108 | -47.47162 | 2026-09-28 16:26:00 | NOAA-20 | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 82d8750d-8c0b-32d5-8ed5-ae64e9bf9191 | -4.0577 | -38.77586 | 2026-09-28 16:26:00 | NOAA-20 | MARANGUAPE | CEARÁ | Brasil | 2307700 | 23 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 510c1977-ddff-38b3-8c7b-7844ea495d5b | -3.67574 | -39.05209 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO AMARANTE | CEARÁ | Brasil | 2312403 | 23 | 33 | nan | nan | nan | Caatinga | 4.4 |
| c1f545de-15e8-3621-9a5f-f58fa28660eb | -11.30624 | -48.73009 | 2026-09-28 16:26:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| d7cf1f07-1bd7-3308-b634-5e990f19285c | -6.26987 | -38.43948 | 2026-09-28 16:26:00 | NOAA-20 | CORONEL JOÃO PESSOA | RIO GRANDE DO NORTE | Brasil | 2402907 | 24 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 74f0c3ac-e3e5-3279-b2ee-6c1fad9f053c | -10.10604 | -43.96096 | 2026-09-28 16:26:00 | NOAA-20 | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 14.1 |
| 0d572af2-97e2-348a-a1f4-3d6474394aa6 | -5.86263 | -45.92096 | 2026-09-28 16:26:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0b80d93d-1830-387d-93c7-aa830242d965 | -8.27364 | -54.70252 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e02d1c21-9392-39eb-980d-00cdcb408a65 | -6.93603 | -41.59899 | 2026-09-28 16:26:00 | NOAA-20 | PICOS | PIAUÍ | Brasil | 2208007 | 22 | 33 | nan | nan | nan | Caatinga | 6.7 |
| 428b4278-1998-3f27-94b7-c8c945799994 | -3.33961 | -43.33558 | 2026-09-28 16:26:00 | NOAA-20 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 4495feb1-e007-3c60-9271-9efc55586947 | -10.96755 | -50.68266 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 112716f6-8d43-377e-b7fb-7855c8657dac | -7.38487 | -42.08986 | 2026-09-28 16:26:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 21.3 |
| 26c1002f-9707-39b4-bc34-990c96cd35a7 | -11.13005 | -50.06933 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 51.8 |
| b752acf6-db4a-3423-ae19-c880fc7c3a75 | -10.65132 | -50.71627 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 22e49f68-eec6-34d9-af94-bdd399a39b63 | -8.11125 | -44.00061 | 2026-09-28 16:26:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 495b3218-1d13-37be-8423-43eb4d85e9b0 | -10.9215 | -50.65924 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 41ab899f-c514-3cf6-b76d-774f46004ea3 | -7.45651 | -44.58719 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48de5599-a77b-3fe5-8b78-b392fdd89b72 | -7.4913 | -45.9674 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a0738e9c-f46a-3b06-bb51-bc00b0f27b79 | -9.51917 | -46.36093 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 64e84248-ed88-3b68-b5da-86eb1bdff8cc | -6.20456 | -52.909 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 8c490a8a-c16d-382f-ade5-3bc40e218035 | -7.25791 | -43.35134 | 2026-09-28 16:26:00 | NOAA-20 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 90ec59a5-b3ce-3f44-972f-aefeb344356a | -7.20696 | -45.0737 | 2026-09-28 16:26:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1f199d31-15f7-3f86-8107-3c8e9dc14c1e | -7.43925 | -55.63013 | 2026-09-28 16:26:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.4 |
| 2c47506c-b740-3a0c-8350-5d783e948f09 | -9.36689 | -49.17638 | 2026-09-28 16:26:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 17d236a3-93b0-321e-91e8-5bbea43bbabd | -7.31683 | -44.58876 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 0a2deb14-046d-3a45-b7f7-b7ba4646024e | -6.69832 | -45.64501 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 04e0e2f3-fe68-3d61-baf7-235d6bcb529c | -11.37808 | -47.44339 | 2026-09-28 16:26:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 83e65564-2f0f-3958-ab15-88960429198f | -6.6906 | -45.64196 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 468ba690-8439-3317-aa75-2a876572b169 | -9.1121 | -49.90123 | 2026-09-28 16:26:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 18b2a32f-901e-3f3e-be17-2603b0d1c1f5 | -5.72759 | -43.28271 | 2026-09-28 16:26:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| fb9e1291-fd15-3c6d-91a6-dc33dc36ee0c | -9.52188 | -46.38042 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.4 |
| 937d4ed3-22e4-35fd-9ce8-f25709fbeccb | -10.26451 | -44.62066 | 2026-09-28 16:26:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 2f27f46f-dd1c-3443-a856-74ac66a1b45f | -7.27365 | -46.93005 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| d6685794-b7be-33be-9d2f-bed079f92724 | -11.55138 | -50.65675 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.9 |
| ca285104-3464-3e94-a288-2341a2bc017a | -5.73652 | -45.01999 | 2026-09-28 16:26:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| b42fa4b7-32ac-316c-bf66-3c998c541e54 | -10.01589 | -50.24185 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 25418b95-9cb9-3af7-afab-dd93929435d7 | -7.95005 | -37.75268 | 2026-09-28 16:26:00 | NOAA-20 | FLORES | PERNAMBUCO | Brasil | 2605608 | 26 | 33 | nan | nan | nan | Caatinga | 14.3 |
| 425a29af-7dde-37ac-aaeb-24f4d4cc2f16 | -11.69363 | -50.60123 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| dbeeb19b-82ee-3485-b36d-eea018cf9ac8 | -6.96167 | -39.42701 | 2026-09-28 16:26:00 | NOAA-20 | FARIAS BRITO | CEARÁ | Brasil | 2304301 | 23 | 33 | nan | nan | nan | Caatinga | 9.8 |
| f1fe616d-c5f9-367b-9ff0-abfbeda82d64 | -9.68072 | -45.5708 | 2026-09-28 16:26:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 13.4 |
| be3f02b9-71d9-33c3-9e43-64e50d1595ec | -11.86527 | -50.47856 | 2026-09-28 16:26:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 7b0cb305-2939-367d-819c-d772622b3526 | -7.64104 | -45.51653 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| d444fa16-42b8-3212-ae0e-f4fe283cc0c7 | -9.29695 | -46.44441 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 77e89055-80bf-3bab-8739-fea0275bc2d5 | -10.96311 | -50.6898 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 29.1 |
| 016e5fd7-034d-3649-835b-8cc29cc9ddb4 | -7.49114 | -45.96593 | 2026-09-28 16:26:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 092008d0-d851-3a41-b5f3-1a56db0cc24b | -11.027 | -49.7125 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 20.7 |
| 50a12422-1a6f-30e9-a265-dfaad4f569bb | -7.34392 | -38.72713 | 2026-09-28 16:26:00 | NOAA-20 | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | 8.2 |
| 1a41cc85-9fa8-3266-8471-d28a860ff25a | -7.22948 | -44.85294 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c3478367-11df-3b40-98a2-135448f81e07 | -9.39181 | -46.39172 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 3ae348a2-ae15-3da0-9698-4804375a60ab | -7.50949 | -55.03007 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 25.8 |
| 26d83cc4-b251-30a0-8172-2ffc0681af8d | -9.82441 | -44.94332 | 2026-09-28 16:26:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 143.5 |
| ee301575-78be-3b34-81c6-0a0581cac6fd | -5.72405 | -53.45558 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.1 |
| fdc8fb4b-0e6c-30d9-ac50-42d66408b7c0 | -9.40267 | -46.38526 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 32.2 |
| e0391d91-f36e-38d7-9100-be1514d657dc | -6.66858 | -45.4154 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| a45534fd-5bbd-3f81-ad80-3030483cbf45 | -11.29318 | -47.67136 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 892d53c5-3d69-37f8-ad35-205217b0460d | -7.98507 | -45.01171 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ee7575b8-1569-3b0d-b004-531ff7d18df3 | -6.35843 | -45.80881 | 2026-09-28 16:26:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 190f6562-b34e-3953-8f24-90acda783db0 | -8.5822 | -45.09369 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 20c72965-0551-3e9e-b90c-a7faf3cf69d5 | -6.6953 | -45.67451 | 2026-09-28 16:26:00 | NOAA-20 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 48.3 |
| a044c85c-6921-39ef-a0d8-4efebc2b039f | -8.24334 | -45.46674 | 2026-09-28 16:26:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 13.8 |
| 24c73e79-dfc6-38dc-b68d-bf626d8ff6ed | -7.58033 | -39.10638 | 2026-09-28 16:26:00 | NOAA-20 | PORTEIRAS | CEARÁ | Brasil | 2311108 | 23 | 33 | nan | nan | nan | Caatinga | 10.5 |
| ca7e6899-b889-3a4f-9ed4-35970b8cb958 | -6.20111 | -52.91006 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| f6f55da9-8518-3b00-be96-49a470b5d1b5 | -10.11581 | -50.18705 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 295459b6-62e7-3582-a3cf-9b12136e138f | -9.29718 | -46.26284 | 2026-09-28 16:26:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 6070cf7f-5344-3abc-8b63-86ca4278e730 | -7.59475 | -44.78791 | 2026-09-28 16:26:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 3fe2a64c-ee0f-33ab-90e7-4a44f5670b02 | -11.13531 | -51.17868 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 126.3 |
| c4663051-02a5-3b37-9722-6add4047e46e | -5.97752 | -53.52922 | 2026-09-28 16:26:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5d84b4e5-b66f-319e-8e84-2147f9087be2 | -9.00065 | -51.25667 | 2026-09-28 16:26:00 | NOAA-20 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 347e84b0-a5a3-3790-8cde-0f2bca1a9119 | -9.98253 | -45.36187 | 2026-09-28 16:26:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bc3b6c87-9cda-30a0-a895-4c25a32264ed | -10.12118 | -50.1893 | 2026-09-28 16:26:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| c1c0d9bf-be37-3eff-95b6-46d2abe7beeb | -6.16999 | -52.82696 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 6d9566b2-5ab1-39ee-8c3d-fa75f39aa860 | -11.15413 | -50.05727 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 15.1 |
| b956544d-b7bf-30ba-8a50-3b1fa3e3b456 | -11.02912 | -49.71098 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 40.1 |
| 9dce7c81-b287-3725-8262-5eb189c0a524 | -6.19943 | -52.91375 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 745389ac-d97c-329b-83e0-2f369c142f57 | -7.12683 | -47.60717 | 2026-09-28 16:26:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e72a95e3-7d4a-334c-872f-90341ba29ee3 | -9.07803 | -49.8678 | 2026-09-28 16:26:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 1a64d045-8beb-3056-bf6d-73660129c1d0 | -11.03118 | -49.70631 | 2026-09-28 16:26:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 16.4 |
| ca78d3ea-c9d8-32dd-a6d9-e93b065fc40a | -7.63806 | -45.52113 | 2026-09-28 16:26:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52a945d8-2478-32ab-98e3-62fca64e2aad | -10.93719 | -47.59109 | 2026-09-28 16:26:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| e9f55211-4aaa-355d-9a10-b2442ad5cd71 | -11.05579 | -47.66973 | 2026-09-28 16:26:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 9cb599b6-4a74-3479-88ea-a82c8b1adb14 | -3.88583 | -40.83178 | 2026-09-28 16:26:00 | NOAA-20 | MUCAMBO | CEARÁ | Brasil | 2309003 | 23 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 6ab4082c-8787-339a-a429-18f04bc047f6 | -7.02254 | -37.9071 | 2026-09-28 16:26:00 | NOAA-20 | COREMAS | PARAÍBA | Brasil | 2504801 | 25 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 0a7e741e-34ec-34ab-b1d9-264034a0222c | -7.99549 | -44.97884 | 2026-09-28 16:26:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 4bf759f2-008f-3127-ac59-3df67155cf57 | -10.92717 | -50.70103 | 2026-09-28 16:26:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 168a56ea-4f46-3bd1-adba-9f579b6552c1 | -7.20268 | -44.85361 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f16739ee-ca84-3aee-bea7-51dc2a3d3775 | -11.12817 | -50.05459 | 2026-09-28 16:26:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3d6862f0-c234-33cf-839e-29dbdffe6d08 | -6.89655 | -52.48016 | 2026-09-28 16:26:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |


[Clique aqui para ver as próximas entradas](README113.md)
