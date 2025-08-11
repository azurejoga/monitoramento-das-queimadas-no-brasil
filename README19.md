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

## Dados Diários - Página 19

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 463f9549-41f8-3d55-9c7d-f7438b9b3fcd | -15.43012 | -53.92636 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 31571710-beaf-377a-b4ce-38669528b67e | -14.59979 | -49.61093 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZINHA DE GOIÁS | GOIÁS | Brasil | 5219704 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 0b211014-3f0c-3fbd-94b9-5cb2e31837be | -18.32184 | -43.67928 | 2025-08-11 04:27:00 | NOAA-20 | DATAS | MINAS GERAIS | Brasil | 3121001 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3cad961-ca7c-3f90-a55e-cf917cca10cc | -17.22836 | -46.95496 | 2025-08-11 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a33d5eac-3bc0-3e90-9aee-288288a8ef17 | -12.57547 | -41.27703 | 2025-08-11 04:27:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| d78d06a6-a4d9-3458-a32b-06685d5b5e82 | -11.70617 | -50.10819 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 08c1cdb9-a0d7-3247-8d43-1e9776afac20 | -16.30074 | -52.91986 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79c840db-ed05-3843-b326-c4a4a76aae89 | -11.77875 | -47.56135 | 2025-08-11 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a838fdd0-072f-364b-bbd4-a76733545293 | -16.40293 | -42.58836 | 2025-08-11 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f0999ef5-c978-3d6e-84a5-7dc7757086a8 | -11.77843 | -49.56482 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d3d61060-e1fe-34ae-896b-9b44f35b112a | -12.57489 | -41.28143 | 2025-08-11 04:27:00 | NOAA-20 | ANDARAÍ | BAHIA | Brasil | 2901304 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 26ca2f82-e504-39ac-a164-db4b171d0626 | -19.41949 | -43.36496 | 2025-08-11 04:27:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61606402-d224-382c-96a9-8b724104cb42 | -19.24062 | -44.06292 | 2025-08-11 04:27:00 | NOAA-20 | JEQUITIBÁ | MINAS GERAIS | Brasil | 3135704 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2543a0dc-dbe1-3ca7-bf5b-36a322982902 | -16.29498 | -47.70023 | 2025-08-11 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ff18e035-a225-333e-abce-fb62eba9e3bc | -17.857 | -44.42338 | 2025-08-11 04:27:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3c4b040e-e898-3da8-85ae-2e66f5d7481c | -15.43897 | -53.92418 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 412edb50-7786-326d-bed4-3d445086d1a9 | -14.83323 | -51.22789 | 2025-08-11 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b1b41d2e-921e-33d8-91a7-1f2c8d4f50cc | -14.83024 | -51.22837 | 2025-08-11 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5aebfdd9-0680-3f0f-bc9b-08870650e60c | -18.63387 | -46.8553 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 20.1 |
| 2f3bae88-36d7-3f3b-9d3f-d30b0e9c3e6d | -16.29983 | -52.9249 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| ea0b0bf4-19d0-3d05-9b60-89c50405ffca | -18.71925 | -49.16153 | 2025-08-11 04:27:00 | NOAA-20 | CANÁPOLIS | MINAS GERAIS | Brasil | 3111804 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 553c1ae9-933b-3e2e-ab88-b03fd5416205 | -12.6081 | -47.14199 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2f6521e2-28fc-336f-874c-69033b88e4e5 | -14.5718 | -43.72668 | 2025-08-11 04:27:00 | NOAA-20 | MALHADA | BAHIA | Brasil | 2920205 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c7ff73d-885b-3c6d-bf54-22deef0c804a | -19.4237 | -43.36578 | 2025-08-11 04:27:00 | NOAA-20 | ITAMBÉ DO MATO DENTRO | MINAS GERAIS | Brasil | 3132800 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 28ca0411-9f3f-3903-bd14-7091ae5ab0b9 | -16.29553 | -47.69658 | 2025-08-11 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2ab8111f-8e15-38da-bd71-f2a8dbe9868e | -13.34589 | -52.25977 | 2025-08-11 04:27:00 | NOAA-20 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a781a86a-7028-3355-8cf2-0ec73f626a68 | -15.95909 | -43.01814 | 2025-08-11 04:27:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b76b5da6-19d6-3c50-91af-14cfc20c60bb | -11.7793 | -47.55783 | 2025-08-11 04:27:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9bbf7224-c61a-389c-acb5-ff10a9d315a3 | -14.11087 | -45.3959 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7bcc1ce1-5fb4-3f17-bcf0-d7be13274908 | -11.77819 | -47.39211 | 2025-08-11 04:27:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| df4bb7ab-626c-3225-a161-1d54ca1b3d60 | -18.61537 | -46.86052 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 0a096eba-4246-3334-ac19-70dd0d4473da | -14.08492 | -46.57692 | 2025-08-11 04:27:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7fc12aa4-23d0-344d-8293-a619c13f0a7c | -18.61884 | -46.86106 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b078cc4b-d291-3b32-ad7f-f2d678d7780b | -11.26861 | -50.18782 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0246c9f3-4952-34ad-b82f-ed0ef3b75528 | -15.44897 | -53.93375 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 46a9c9fe-4661-3519-840c-2f747a3aed3c | -19.4989 | -44.27667 | 2025-08-11 04:27:00 | NOAA-20 | SETE LAGOAS | MINAS GERAIS | Brasil | 3167202 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0db0cdc3-ad74-335e-94c7-71a1f0b6dfe2 | -13.97112 | -42.58643 | 2025-08-11 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| ff558590-2edf-38be-81a7-9b8db2351c64 | -14.1144 | -45.39645 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ac497caf-37e6-3cf3-bb78-8343b85066d2 | -11.71796 | -50.10209 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c9a05b9a-8b2b-38ff-afa9-4d455bc5dc64 | -15.39925 | -49.12711 | 2025-08-11 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 880cbaec-912f-3285-8034-2ef672c49ef5 | -14.83379 | -51.22902 | 2025-08-11 04:27:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8b66172f-eb47-30c7-a629-209293040c16 | -16.30833 | -52.92124 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b8c763d-7bd9-3bc1-9836-a7ed19c52ca4 | -18.1794 | -47.00054 | 2025-08-11 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4930b3b3-9e8d-37c5-b0d3-068143ace95e | -14.57164 | -47.14867 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1508ec60-629c-3415-8e0d-28dd68ac37c6 | -16.20884 | -49.98368 | 2025-08-11 04:27:00 | NOAA-20 | MOSSÂMEDES | GOIÁS | Brasil | 5213905 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b0f30dd9-5a6e-3684-9496-a74e1c064ee2 | -16.29887 | -47.69712 | 2025-08-11 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c064b861-3bad-3787-96e5-171e13df3a77 | -16.39844 | -48.10994 | 2025-08-11 04:27:00 | NOAA-20 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d2888b45-d5ad-318a-863a-541ee8e66598 | -18.6304 | -46.85471 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8ff04f8f-24ed-3c75-8305-744342918309 | -12.70269 | -46.36789 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afc97b82-fb29-37b2-bc5a-7fd41235522a | -16.29048 | -52.93319 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 421fa4fe-a2a4-3c2e-b8fc-3e1492374258 | -15.41107 | -53.91491 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| bbc7b6f0-abae-31a1-8f8f-31efb1168a80 | -13.62335 | -46.94013 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c84739bc-ceb2-3d57-b037-9461c6a1e4d4 | -18.1628 | -46.99373 | 2025-08-11 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 67a0cf78-33d1-3950-8ba7-6181c6d6a106 | -11.71381 | -50.10544 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47d6c912-1e80-3726-a5f3-968c087e7139 | -14.12086 | -45.4016 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 362c1a0f-5213-3578-a1fa-b2da41eeb1b6 | -15.41175 | -53.91116 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 45e02484-3db4-366f-8bb2-7079aec7a2d7 | -14.11966 | -45.40972 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a281fb6-33b6-3ae6-9400-db9a9b0d688d | -11.39262 | -50.59405 | 2025-08-11 04:27:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9e6e7cb3-c53a-345d-9a65-72d858dfa838 | -12.54755 | -47.07427 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 42424c92-bccb-3bc9-807a-a290bbc9253d | -16.22084 | -48.70306 | 2025-08-11 04:27:00 | NOAA-20 | ABADIÂNIA | GOIÁS | Brasil | 5200100 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| df6a001c-60c0-3af2-af8b-4d7429e2f95d | -18.62809 | -46.84616 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ed9a2e33-6c18-3858-bec5-cb081db76dfa | -14.5722 | -47.14504 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72eb6e28-c796-3665-a778-589b433ed63e | -15.16924 | -48.28637 | 2025-08-11 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6c1dc59b-ab95-3b2e-9e1f-f0231dbce7a7 | -13.615 | -46.92746 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 670adc33-45a7-35e2-a2ed-0f571eeb923a | -15.41787 | -53.92401 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4200759d-b12a-3e96-9ce9-7870402ae393 | -16.04828 | -48.48298 | 2025-08-11 04:27:00 | NOAA-20 | ALEXÂNIA | GOIÁS | Brasil | 5200308 | 52 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c3012d54-6f64-3438-86e5-2c1b97c79228 | -14.47065 | -47.84668 | 2025-08-11 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 37e0e5dd-d6ad-335c-ab9a-523e71a7080a | -17.2528 | -44.87976 | 2025-08-11 04:27:00 | NOAA-20 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b8d87500-3e49-3992-b1c5-8955ba42b5b6 | -15.09808 | -46.53666 | 2025-08-11 04:27:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6321d39f-8086-3ded-9557-e52c3ca6c9e2 | -18.79747 | -43.87314 | 2025-08-11 04:27:00 | NOAA-20 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d80055de-36fe-3a5a-9f3b-5fc300b62f1e | -14.12111 | -44.87194 | 2025-08-11 04:27:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f50b4837-71d5-3f7c-b95d-988c296b2c0e | -14.11733 | -45.40106 | 2025-08-11 04:27:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b5cb9822-0721-3977-b952-a982304db939 | -14.48134 | -47.07489 | 2025-08-11 04:27:00 | NOAA-20 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7dee8a8e-6fb8-332f-8eff-821b3a96d4a9 | -12.54533 | -47.06663 | 2025-08-11 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 61ce17e8-e16e-3930-8d7b-61f757434c2a | -11.71316 | -50.10939 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5c31c97f-d022-3d4a-9e2d-d71014b8d32a | -18.7813 | -42.91362 | 2025-08-11 04:27:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4f0abe34-d036-3592-82bf-3491d6e197d9 | -15.42945 | -53.93013 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 36.2 |
| 7672c0e6-c0e0-39a9-af7f-43d124e2f805 | -19.21868 | -46.8008 | 2025-08-11 04:27:00 | NOAA-20 | SERRA DO SALITRE | MINAS GERAIS | Brasil | 3166808 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 38334886-00f7-32f1-87b6-2ab512acfd23 | -15.42672 | -53.92181 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 32.5 |
| 72766496-ddd5-3050-8916-6932eb4dd214 | -15.44987 | -53.93406 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| c4c6f613-9260-3fbd-99b5-3767d376f3aa | -11.69589 | -50.12675 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b89650df-53df-3d8e-9ab4-ea363b755acc | -12.70662 | -46.36475 | 2025-08-11 04:27:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5be768f-319c-302a-a458-e40b5f8fe4ea | -15.39593 | -49.12654 | 2025-08-11 04:27:00 | NOAA-20 | GOIANÉSIA | GOIÁS | Brasil | 5208608 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 58ed1b65-b512-3378-8cdb-bcbf66a93866 | -16.28716 | -52.93486 | 2025-08-11 04:27:00 | NOAA-20 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81901d47-18f7-3765-9987-5fdec615d110 | -16.10733 | -44.51825 | 2025-08-11 04:27:00 | NOAA-20 | LUISLÂNDIA | MINAS GERAIS | Brasil | 3138682 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b7119c33-625c-3248-aba5-835520d36fb8 | -13.61445 | -46.93108 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08b2ed86-a59f-3a8d-b9e6-b69a10e52b06 | -15.40698 | -53.91412 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 1f2e1a84-4c92-3caa-90f6-c76611604b8e | -18.77869 | -42.91127 | 2025-08-11 04:27:00 | NOAA-20 | GUANHÃES | MINAS GERAIS | Brasil | 3128006 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 48af91ad-b292-3443-9257-2107cdbc0719 | -16.39386 | -42.59115 | 2025-08-11 04:27:00 | NOAA-20 | PADRE CARVALHO | MINAS GERAIS | Brasil | 3146255 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f4ffe33c-8bce-32c1-b332-74b633826ec8 | -18.62751 | -46.85015 | 2025-08-11 04:27:00 | NOAA-20 | COROMANDEL | MINAS GERAIS | Brasil | 3119302 | 31 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8c72a107-6c6a-337c-a107-0caeb8a530e0 | -13.59216 | -46.94241 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| cbf116a1-c91b-3bc2-9413-95534046ba81 | -18.45654 | -45.9007 | 2025-08-11 04:27:00 | NOAA-20 | VARJÃO DE MINAS | MINAS GERAIS | Brasil | 3170750 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 83054fee-b43e-314b-8f75-228d323adebc | -13.61779 | -46.93166 | 2025-08-11 04:27:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 8e9c6d84-5f45-37fe-8b43-4e263fd11dd5 | -13.96646 | -42.58966 | 2025-08-11 04:27:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| f28d8d04-7a41-327d-ae2a-439cd23767bf | -15.44103 | -53.93626 | 2025-08-11 04:27:00 | NOAA-20 | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2fc000f3-caf8-32b7-8fa0-c26fff2c5b98 | -13.64185 | -49.02389 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 025c899b-635d-326c-b6ab-60e4fa73904c | -14.08436 | -46.58065 | 2025-08-11 04:27:00 | NOAA-20 | IACIARA | GOIÁS | Brasil | 5209903 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9ff775b-4349-31f7-9315-27f53f0cdb54 | -11.70966 | -50.10879 | 2025-08-11 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4100980f-2d7a-3721-8316-2b7f6beac845 | -13.64087 | -49.00874 | 2025-08-11 04:27:00 | NOAA-20 | SANTA TEREZA DE GOIÁS | GOIÁS | Brasil | 5219605 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f08d0d5f-1d6f-3233-b1f4-add930ca643d | -16.01225 | -51.36135 | 2025-08-11 04:27:00 | NOAA-20 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README20.md)
