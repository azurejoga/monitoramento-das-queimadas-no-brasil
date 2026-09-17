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

## Dados Diários - Página 31

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ae5e5b68-b11d-3111-b03e-3315eed21ec7 | -12.51605 | -50.84869 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b34a83cb-e241-3402-abd4-e8858596a5c7 | -12.48054 | -50.85675 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 77.0 |
| a76d0e45-3086-31b2-9fe0-7c805beba26a | -12.46814 | -50.8197 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8ec74b3b-a2d4-31e7-8e34-2596ce25162b | -9.61861 | -45.34789 | 2026-09-17 03:55:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ccf42f46-f625-341e-a160-9f8bfb577035 | -7.13029 | -42.1735 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b28ca26d-dfa7-3cc0-a120-e7d59aa5a751 | -9.5929 | -46.6503 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 67d8f3e9-1a60-3957-8f59-41891e2ba27e | -7.08974 | -41.84769 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f014b3fe-1012-3010-99d9-b5a0ffca32a4 | -7.44908 | -46.16836 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f7f3360f-2171-391b-894e-026cd715a890 | -12.17146 | -38.59657 | 2026-09-17 03:55:00 | NOAA-20 | PEDRÃO | BAHIA | Brasil | 2924108 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| a181bc6b-66f9-3873-bab1-59e3589441a2 | -12.42965 | -50.87423 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0d124969-59b3-3fc5-84f4-de4b7d3f109b | -7.37703 | -44.51958 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1e3433ea-4892-3afd-a2d4-76144e3761b3 | -12.4535 | -50.7937 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 33.2 |
| 27992e5a-da1e-344b-843c-588bec7a00fa | -9.51276 | -43.13402 | 2026-09-17 03:55:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| a0ce20fa-b5dc-3bff-83e8-bc5cd3d055b6 | -9.59227 | -46.65365 | 2026-09-17 03:55:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 2c10a919-7697-3995-b8c0-e97f15ce5f13 | -10.1203 | -45.5724 | 2026-09-17 03:55:00 | NOAA-20 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 18462d08-a883-3ace-9bf4-d35e03650cbf | -7.17445 | -42.10868 | 2026-09-17 03:55:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ba8e2063-2eba-3fc4-9fd3-977fb99e9db9 | -11.26593 | -43.47811 | 2026-09-17 03:55:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0bd92c6e-04d9-3a6d-9295-d3ef58be0714 | -7.57708 | -44.92819 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 20d803c1-5585-3476-a4e3-90a0e91739f4 | -7.96765 | -44.83145 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d80c7de5-5497-3765-9bc8-8e3e21be5710 | -8.2616 | -42.17484 | 2026-09-17 03:55:00 | NOAA-20 | PEDRO LAURENTINO | PIAUÍ | Brasil | 2207934 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| a4a202c6-7404-3546-bad1-c97fe43ba3e3 | -9.11832 | -45.73807 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 865651ef-9400-31e8-b757-7ba0fd0d1d20 | -12.44434 | -50.83724 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 2bdb5adf-f04f-3acf-b591-4045fe53eeea | -12.70929 | -48.26813 | 2026-09-17 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c726638c-052a-3beb-8469-0fa738e48542 | -12.70715 | -48.2791 | 2026-09-17 03:55:00 | NOAA-20 | SÃO SALVADOR DO TOCANTINS | TOCANTINS | Brasil | 1720259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b33635a0-2990-319d-9449-4f95b0588806 | -7.45827 | -46.8404 | 2026-09-17 03:55:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| f580ed39-efff-3086-9ca2-6c27c5fa86b0 | -11.5737 | -46.87702 | 2026-09-17 03:55:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 79062cce-53c8-3e41-a3ce-daca05236c4c | -7.64977 | -44.3231 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ad61919a-ded2-37aa-b5a2-231fe87794c4 | -7.80968 | -44.86429 | 2026-09-17 03:55:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 15071005-adab-386d-8981-093f2d2fa735 | -8.85542 | -45.87982 | 2026-09-17 03:55:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cece7b9b-2b25-3839-a95c-aa9628bd3cb2 | -7.09631 | -41.83292 | 2026-09-17 03:55:00 | NOAA-20 | SANTA CRUZ DO PIAUÍ | PIAUÍ | Brasil | 2209104 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| edad390c-0d1c-3c77-a9b3-768ee6b0f884 | -12.48612 | -50.9271 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 7aa3835b-b843-3fab-856c-a8ad7d137120 | -7.58545 | -46.33738 | 2026-09-17 03:55:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 1c4ca6c0-1f1a-36ec-b0a0-326704ef3324 | -12.47113 | -50.83748 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 42.1 |
| d1fc876b-ed5a-3b85-9aef-29ccee6d1c05 | -11.89494 | -47.58549 | 2026-09-17 03:55:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| e9819982-ebb5-3cd2-bb63-a14b6ffb29d8 | -7.08867 | -41.76208 | 2026-09-17 03:55:00 | NOAA-20 | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| b52859ef-bc0b-3c05-ad04-810203467a2a | -11.02396 | -47.56803 | 2026-09-17 03:55:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9203f562-b88b-34f1-b9ca-ca5efe26a316 | -12.45389 | -50.78815 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 50a76e26-9762-3918-8425-5ecbec54f960 | -7.0391 | -42.07158 | 2026-09-17 03:55:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 1d60cde6-054e-339a-b6dc-a22a9b4abc13 | -12.47898 | -50.89661 | 2026-09-17 03:55:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a92f9ba-11b8-33b4-acb3-bc370d7f2365 | -6.78524 | -48.66362 | 2026-09-17 03:55:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2c78eb9b-9835-3baa-b31b-d8f5723dc870 | -14.79187 | -42.691 | 2026-09-17 03:57:00 | NOAA-20 | URANDI | BAHIA | Brasil | 2932606 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7df63bdc-f65a-3292-b1ef-7a0b99449237 | -15.98475 | -43.00379 | 2026-09-17 03:57:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d9c92db2-18b5-381e-9103-bbabed9c67ae | -14.86065 | -47.914 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| baa33867-0ab7-35bb-9e45-fe5d15fab936 | -14.57018 | -46.59496 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c196e428-c0fc-3dbb-8156-dedce4aaee64 | -14.18162 | -45.15355 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| cb315824-4bcc-3372-9c34-76d7d94f90f0 | -14.85878 | -47.91644 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 57bd67b6-93d2-35fe-9e22-655ec4e64cab | -14.1587 | -45.13137 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81b32749-e9e6-3e2d-9849-180961cf6b3c | -14.14142 | -48.74899 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2e89d82f-7e75-3383-be04-853f3b248213 | -17.77184 | -46.47908 | 2026-09-17 03:57:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| debbc16b-2ea5-3b22-93fe-96a7a313a7ea | -14.18394 | -45.14085 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 0e21d063-0b1e-3fe5-a460-62eee7e1c3c3 | -13.75256 | -48.80966 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 00cc34ed-dea8-3645-8200-74acfa354611 | -16.61684 | -43.41346 | 2026-09-17 03:57:00 | NOAA-20 | GRÃO MOGOL | MINAS GERAIS | Brasil | 3127800 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6bfc2df5-3b4b-3572-9793-b830dc383bb4 | -17.77627 | -46.48003 | 2026-09-17 03:57:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dd837ca0-4ef9-37b0-bfc1-7bbc5b14d708 | -14.32695 | -48.93331 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 3ad48b61-23ae-3ebd-a469-7bc6b189b858 | -14.95861 | -47.53281 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 433c1441-fb6a-3c3e-b17a-46924aa79c20 | -14.55494 | -46.59736 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 881403f7-fcae-31c0-8ac9-02ab27490c1f | -14.17806 | -45.14841 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 1fbe39b6-fdbe-366d-baf2-5bf80dc49902 | -15.42094 | -41.204 | 2026-09-17 03:57:00 | NOAA-20 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fcd0f9c9-a429-309e-b2a5-0c8a054385f6 | -16.14084 | -43.54853 | 2026-09-17 03:57:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| dcb89958-85b0-3fbb-b3db-5f00a3e4159a | -16.98641 | -45.47028 | 2026-09-17 03:57:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| baf820f9-fac3-36af-8d4f-77297c4fc4c1 | -14.18116 | -45.1315 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7c5c8095-9027-38d3-b4ed-dfd09890841d | -13.74967 | -48.79534 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e3dc7adb-70dc-3137-a012-1cd8dd9f0a59 | -15.05937 | -40.99067 | 2026-09-17 03:57:00 | NOAA-20 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| eee9c8a5-d611-30b6-8c99-4f2e34d3af09 | -14.95915 | -47.53011 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a04a57f4-d0d7-341b-bc38-07ca3120406a | -14.57006 | -46.59734 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ecbb349b-6994-3c21-adc8-a17a4095f94b | -14.15358 | -45.1347 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d0020405-49b1-39ec-9c7b-71e51f8f977f | -14.57694 | -46.58527 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| edf83acd-23c5-3de2-97d7-8aac1881ab64 | -15.10306 | -42.00718 | 2026-09-17 03:57:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 0dc15012-6716-3bef-9aed-b01cb6e33211 | -14.12718 | -48.73427 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 9d8b20e6-bcb0-3935-84b3-03ace4f2f666 | -13.75352 | -48.80491 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 5.0 |
| c2f58666-73fd-3ab7-b7a3-af9180e057df | -16.09103 | -45.13399 | 2026-09-17 03:57:00 | NOAA-20 | PINTÓPOLIS | MINAS GERAIS | Brasil | 3150570 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 967d3f88-7347-3a7a-99bb-62bca411aea7 | -14.55393 | -46.60265 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 15.0 |
| 575dcab4-3cb6-343e-a610-6c96f5544084 | -17.76976 | -46.47632 | 2026-09-17 03:57:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 2.7 |
| d342763e-f138-3aa1-b344-0932f134dbe1 | -13.74685 | -48.80927 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e797e444-af8e-339e-98be-2f9e7bbdabd5 | -20.44595 | -46.53867 | 2026-09-17 03:57:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 685fba8d-1e43-3ab2-85d5-536a80de80e1 | -14.57594 | -46.59058 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| af835b1d-6c4c-31f3-892e-fe5d68c746a2 | -14.15279 | -45.13896 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 96cd1144-80d7-323f-a6fb-161deab3ab24 | -14.18239 | -45.14931 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| d8c13083-6efb-3283-a23d-6c1027269364 | -15.77528 | -43.82745 | 2026-09-17 03:57:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 0.9 |
| de5bd0ef-3648-3922-99bc-026464dae72c | -14.12643 | -48.738 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d888f6da-fdc5-346e-8856-013bf3574c6e | -16.99485 | -45.472 | 2026-09-17 03:57:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 7.5 |
| ab11403c-fdb6-380e-81f0-f1f81b3981b1 | -18.27042 | -47.18877 | 2026-09-17 03:57:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ce46c830-48e3-3758-b840-6ba553023aa5 | -16.67356 | -41.8487 | 2026-09-17 03:57:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| bae2d402-483b-30d1-9e91-a2fccb698865 | -16.99563 | -45.46791 | 2026-09-17 03:57:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 1646d9bd-353b-39d7-97cb-2102341c3904 | -14.85937 | -47.91338 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe32fa20-d880-3e9b-89dc-e4200de52aba | -16.99063 | -45.47113 | 2026-09-17 03:57:00 | NOAA-20 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8348f728-a679-3f2b-9852-6593452e2d54 | -18.88576 | -46.84365 | 2026-09-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 387a9e5b-5252-36d4-a4c9-1769de2b1a0e | -16.67286 | -41.85277 | 2026-09-17 03:57:00 | NOAA-20 | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 2e644052-5f2d-3577-91dd-d0bc1acb9c5f | -14.85424 | -47.9123 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 6c703f05-6073-35a0-836e-ff6799926322 | -14.17372 | -45.14753 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3219229e-9cc3-365f-ac62-62260c780bea | -14.22044 | -47.71554 | 2026-09-17 03:57:00 | NOAA-20 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3377bd21-164f-35a7-a755-6aace14b6759 | -16.13996 | -43.55342 | 2026-09-17 03:57:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22f07952-d089-31bc-a71b-6f78f7ce011b | -14.5769 | -46.58764 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 2aef0aef-5822-3efa-b73d-e9ef34be6a89 | -18.88297 | -46.84513 | 2026-09-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 77b5e9a7-4b1f-3c0c-b605-38b70cd19c59 | -15.36238 | -42.19432 | 2026-09-17 03:57:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3162708 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| b6a0acb0-d2c1-3de2-bd43-dc819b48c840 | -18.9877 | -46.94873 | 2026-09-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 47a5a475-a0f5-3f68-bad7-271b5a610b04 | -13.75532 | -48.79598 | 2026-09-17 03:57:00 | NOAA-20 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cb9292a3-80a0-38a7-a968-379dcf69409d | -14.15714 | -45.13981 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b74ac6e0-34e9-3e9c-ac5e-56cf761ac248 | -14.55767 | -46.60893 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 90f63bf7-f729-3d67-bdb9-032b9c6f283b | -14.56918 | -46.60027 | 2026-09-17 03:57:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README32.md)
