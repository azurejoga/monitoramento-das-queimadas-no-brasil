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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e16e2628-f565-3957-b056-3224aa14b86e | -3.7434 | -44.37597 | 2025-09-06 04:17:00 | NPP-375D | MATÕES DO NORTE | MARANHÃO | Brasil | 2106631 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9492d20a-ff29-3219-a9c9-ef3998e0ccd1 | -6.16819 | -43.18496 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5aebafde-8ae8-3dc6-99df-2867631251c1 | -8.02943 | -44.13612 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c0e95deb-3087-3aac-9cd7-08efa2d420bc | -5.72746 | -43.91423 | 2025-09-06 04:17:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71a53ab8-5c62-37d8-9a5d-e6fd348959b2 | -7.80023 | -45.42923 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5eac866-64da-3ecf-9834-adc13a25f961 | -5.94995 | -53.80651 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 475cfcaf-8474-31ef-b369-62517d10346b | -5.03442 | -49.75903 | 2025-09-06 04:17:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 07774b5c-3bc7-38e6-8d4a-964962ee8858 | -6.66458 | -48.39719 | 2025-09-06 04:17:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5e62fa53-57ce-314f-a7d1-73c66f675305 | -12.93621 | -48.04529 | 2025-09-06 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e4639d9-6fd5-349e-adb1-0b9c2a7467d4 | -6.38864 | -43.00968 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 24b01f67-ddd3-3271-93ca-47d19d207e73 | -6.15267 | -43.1754 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 85b6b48e-3276-3584-b2ef-58fe6a94ea2d | -6.15102 | -43.18581 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 3f25e54d-425d-3495-8782-686730e93644 | -6.16041 | -43.16951 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c61be418-73ac-379e-aa35-d9b7309667be | -11.47397 | -55.55101 | 2025-09-06 04:17:00 | NPP-375D | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c037eac-d47b-3133-a5cb-2ac1ccd39d1f | -6.27317 | -53.43748 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b363ee94-e89c-3110-92b6-3ccef267e8be | -5.93696 | -43.02005 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 94324ee2-a4e7-3f05-9234-e970e9d19e19 | -3.24416 | -50.79958 | 2025-09-06 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 68011adc-9baf-3cb0-ba69-8efbf1fcbcde | -12.96607 | -54.7823 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1ac739b2-02a0-3dae-b284-36e93c758868 | -7.33644 | -48.49821 | 2025-09-06 04:17:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 79d20679-169a-3a05-a72e-5df8ce8003ef | -15.63581 | -41.85804 | 2025-09-06 04:17:00 | NPP-375D | BERIZAL | MINAS GERAIS | Brasil | 3106655 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 99683253-b987-3973-88a8-ba8d46e56e4f | -12.50387 | -53.85479 | 2025-09-06 04:17:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 170cc999-0cf6-3819-8272-2e8ae9bacbbf | -5.9496 | -42.96163 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 5e94c840-3504-390d-bfaf-dec9c82f2b86 | -12.94922 | -54.79546 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b48cb87e-298e-3a67-a3c0-0386e73340e7 | -9.01701 | -49.79818 | 2025-09-06 04:17:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 16580973-7166-3c23-80e2-8367507fd82c | -4.03375 | -42.5181 | 2025-09-06 04:17:00 | NPP-375D | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 95e9d7ef-2eba-3771-a6e0-68f38e712db2 | -5.86956 | -46.04614 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 138f6162-aefc-3656-bfd3-62db2566d72f | -10.06481 | -48.07613 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 174b2bd5-b11b-332a-a67e-7c3de481a84d | -12.96122 | -54.77726 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02551e2d-caf8-341d-8e6d-6f25ed619dba | -14.59085 | -48.09443 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 362e6c92-5980-356f-9184-da41854ed596 | -6.86358 | -44.82174 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 331c08d9-6bf9-3293-b58b-a6811b328ffe | -5.73092 | -49.28864 | 2025-09-06 04:17:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 024795d9-d9cb-31ef-aa93-fb7b0146eb75 | -5.99618 | -44.15767 | 2025-09-06 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 57c063e3-7493-3f3d-9cac-373778f695ca | -16.41846 | -47.82267 | 2025-09-06 04:17:00 | NPP-375D | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e5f11e65-7cf1-3c4f-a320-3f3fee07f85b | -5.98846 | -44.72515 | 2025-09-06 04:17:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e573f2bd-40f1-3f28-b7ca-f19f32a033bb | -6.22976 | -42.64342 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f2f10151-bb6a-3017-bb87-e48265f7de4a | -12.96683 | -54.77851 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0ba6c7c-c6ee-38a6-a40d-bb68c9dc2afc | -5.95636 | -43.02666 | 2025-09-06 04:17:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fdc5a33-789f-3b23-a5d7-088aeae44370 | -6.30956 | -44.57602 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d8b05431-8221-33f3-89d7-2c858eab92b1 | -15.06902 | -50.06718 | 2025-09-06 04:17:00 | NPP-375D | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 11daa618-be45-3e71-956f-1a8ce03e3540 | -6.15989 | -43.19433 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 017b4d2d-5a3e-3679-bf47-780961cdca01 | -12.95655 | -54.80043 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5fefa3c8-9afe-3f1c-bc58-0294232bc4eb | -13.31809 | -51.64516 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8f8e27a2-7574-3ee1-8c82-def42dd3fcaf | -6.60636 | -43.98486 | 2025-09-06 04:17:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e0e7362f-2447-30c9-9f92-426d3ba92a67 | -5.94906 | -46.17375 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6a4df15f-d02e-3cea-883d-4050801bf999 | -16.40923 | -45.6503 | 2025-09-06 04:17:00 | NPP-375D | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0cceb91c-a4cd-3df0-94e4-b458eb3075b4 | -6.18622 | -53.25964 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7899ec6c-16ec-3423-a584-cefdfaadaa1e | -6.86298 | -44.82549 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 027b2148-3b5d-3702-affd-3a1c9cc09ff1 | -5.17895 | -43.10592 | 2025-09-06 04:17:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9a8de814-5ac7-33f4-9d8b-9d4675e900ca | -6.66395 | -48.40106 | 2025-09-06 04:17:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d0135b1-f2bd-3c60-9d8a-17e4a33be0ec | -13.01536 | -54.82916 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e7dd1130-8a7e-3386-97e4-2b1c8e1d19b9 | -5.94609 | -46.17072 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16080251-24c3-3ce8-9858-b79677198951 | -4.13517 | -40.631 | 2025-09-06 04:17:00 | NPP-375D | RERIUTABA | CEARÁ | Brasil | 2311702 | 23 | 33 | nan | nan | nan | Caatinga | 1.0 |
| e0f0a6ec-0a07-392e-8c4a-7636cd045c0e | -8.07646 | -45.48799 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f16186d7-d29f-3d9e-b438-2dd831f0aedd | -16.54669 | -42.34526 | 2025-09-06 04:17:00 | NPP-375D | VIRGEM DA LAPA | MINAS GERAIS | Brasil | 3171600 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e4fea0b5-0fa9-364b-a1f0-be698c88a20a | -7.34531 | -44.32755 | 2025-09-06 04:17:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9d3d64e2-7741-3e20-ab0c-9ca8b2bf8da2 | -9.71242 | -49.49319 | 2025-09-06 04:17:00 | NPP-375D | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4736cdcd-5274-327b-9333-9d2c00c2207a | -13.89335 | -48.02208 | 2025-09-06 04:17:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bb739f6f-244d-3057-8764-2f63fa9db684 | -2.78413 | -49.62152 | 2025-09-06 04:17:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5f92daed-b2f0-3ece-90d0-895ef2e309a8 | -15.20995 | -52.37221 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 31a030e3-c613-3258-9f02-92ecd89bbc88 | -5.6536 | -43.61383 | 2025-09-06 04:17:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a040a08d-21fd-38f5-a7b1-879c68d21cd8 | -13.72099 | -46.90952 | 2025-09-06 04:17:00 | NPP-375D | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ac3a7e8-8728-3750-9403-fe56743d7194 | -7.03131 | -49.30576 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66784d6f-a7bf-385a-995b-82313d30e815 | -2.56575 | -48.9693 | 2025-09-06 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d954a044-e633-35a4-8e21-e854f01ca212 | -7.34286 | -43.94696 | 2025-09-06 04:17:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ede30f9d-f419-3419-8567-dd129f02c6d4 | -9.87785 | -46.54616 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 810a4dde-0e19-3c8b-86fc-b30ccc00ade9 | -14.56546 | -48.09069 | 2025-09-06 04:17:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b3324b1-edbe-3a41-bd66-3fb7e3739170 | -6.23145 | -42.43669 | 2025-09-06 04:17:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| ecbc2491-d5f6-324a-8834-4e2211fc1265 | -5.95142 | -53.78698 | 2025-09-06 04:17:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cf20ba7e-045c-36dd-a0d3-ae9261c19d8c | -5.46925 | -44.13234 | 2025-09-06 04:17:00 | NPP-375D | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 856fc287-aab3-3327-97b7-83724165002f | -16.90093 | -45.74435 | 2025-09-06 04:17:00 | NPP-375D | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d20057a0-255b-3433-af50-6512ac010f7b | -15.07328 | -48.11795 | 2025-09-06 04:17:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ed45955d-03e9-39e3-aed3-c6434b22066c | -10.60061 | -44.32988 | 2025-09-06 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| 05f4180f-7e0c-365b-9ec0-2cba223311ce | -8.343 | -47.48152 | 2025-09-06 04:17:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d501f675-89a6-3e49-a3db-c49550ad2e4c | -8.02304 | -45.42456 | 2025-09-06 04:17:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e65a298d-c8f3-3dfb-a439-52b69684560e | -4.63742 | -42.52784 | 2025-09-06 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 2a078eff-3044-3ab2-a63a-075ca61a797c | -6.88472 | -44.71247 | 2025-09-06 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b4826e23-85a3-3836-93af-dc4943033f1a | -6.20354 | -43.57904 | 2025-09-06 04:17:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0800af0c-e219-3aa4-9604-a02283c27c43 | -5.38237 | -45.96519 | 2025-09-06 04:17:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19477560-eb7a-38ac-9d63-638b5b8644f6 | -8.50137 | -45.08651 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f06432fc-ebc4-3fff-9a9c-12cbf289a1d9 | -6.53924 | -49.50257 | 2025-09-06 04:17:00 | NPP-375D | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8bf4b3d6-99b8-35b1-baf6-a547454235e4 | -7.96181 | -44.94376 | 2025-09-06 04:17:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8a49a04b-ffe6-3959-94df-c4bd9d3fced4 | -6.6221 | -43.73518 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92a724a0-fb16-332f-a422-e08227c8c5d8 | -13.00659 | -54.8438 | 2025-09-06 04:17:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2c498014-a184-311c-9173-5e61df31514d | -6.40009 | -46.08806 | 2025-09-06 04:17:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0e4b2723-12ed-3225-9adb-f229ad905215 | -14.12573 | -51.70386 | 2025-09-06 04:17:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5537b607-a8c2-3b76-b5d8-e3c2953604da | -9.18443 | -46.04271 | 2025-09-06 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74314847-5f9a-3e0e-8abf-04f7eb0757e9 | -6.87417 | -52.79097 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e8207d3-93e3-34b7-bfef-d992e858b6a3 | -3.69546 | -49.54784 | 2025-09-06 04:17:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 0cfd3199-8439-347f-9fcd-7798c5dac755 | -6.36612 | -44.68233 | 2025-09-06 04:17:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6d3480b5-2655-3a24-b707-397dec66ff00 | -5.5833 | -45.13209 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 294fb5de-0510-388f-bac4-6f16f1b3c85e | -6.88531 | -44.70883 | 2025-09-06 04:17:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 21dd30aa-1e2f-3509-b88a-47f3a64df575 | -5.94425 | -45.66058 | 2025-09-06 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e2673f07-d288-3b13-92b1-b1192df14595 | -9.84644 | -47.83119 | 2025-09-06 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 20958ce1-d843-3c60-8e27-f4dcdc00d61b | -6.37592 | -43.81417 | 2025-09-06 04:17:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c832d6a0-aba1-3333-acdc-22c6fe414fd7 | -6.22643 | -42.6429 | 2025-09-06 04:17:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b09f8ac0-7f99-3a07-b75f-cda93a148600 | -5.97844 | -43.61126 | 2025-09-06 04:17:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| b3b4f008-a7d4-3a81-8dda-6eda4a5d39b0 | -15.84573 | -52.29741 | 2025-09-06 04:17:00 | NPP-375D | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 34391ee4-4faf-397b-8b1c-7354c37a54a0 | -6.18838 | -53.24756 | 2025-09-06 04:17:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b8bc776b-b320-3c84-b610-0e0ea372e122 | -6.15764 | -43.16552 | 2025-09-06 04:17:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 739b3b5f-e096-338e-9092-9ff74d40a49e | -10.06795 | -48.06961 | 2025-09-06 04:17:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README33.md)
