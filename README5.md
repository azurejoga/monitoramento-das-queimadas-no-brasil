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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8819566d-f9a2-3b90-9664-136f5de663ee | -19.99752 | -44.2548 | 2026-07-22 04:12:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 71c98cd5-77b3-3979-87d4-0f30b7ed2aaa | -19.72621 | -46.1735 | 2026-07-22 04:12:00 | NOAA-21 | CAMPOS ALTOS | MINAS GERAIS | Brasil | 3111507 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| eec81f59-a994-3a68-9727-acda2c71395c | -19.87934 | -44.05093 | 2026-07-22 04:12:00 | NOAA-21 | CONTAGEM | MINAS GERAIS | Brasil | 3118601 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b15d52e4-8f6a-34d6-b0df-e1b9dc7c862e | -23.50277 | -46.98603 | 2026-07-22 04:12:00 | NOAA-21 | SANTANA DE PARNAÍBA | SÃO PAULO | Brasil | 3547304 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 027a0b1c-b788-36e7-a5fc-ca44e9b3c82a | -22.78194 | -43.4536 | 2026-07-22 04:12:00 | NOAA-21 | MESQUITA | RIO DE JANEIRO | Brasil | 3302858 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 492d0052-9d03-3e84-b7d5-814732f2e2a8 | -19.30533 | -46.90688 | 2026-07-22 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 1e585c7b-6ea7-3d8c-a4d0-a3698c8288c1 | -19.78816 | -47.47005 | 2026-07-22 04:12:00 | NOAA-21 | SACRAMENTO | MINAS GERAIS | Brasil | 3156908 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 90bd68b6-65e9-330e-814d-4615b6df89e2 | -19.25772 | -47.31917 | 2026-07-22 04:12:00 | NOAA-21 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6d04160d-15af-3720-807a-2c321910aa80 | -18.80526 | -47.05115 | 2026-07-22 04:12:00 | NOAA-21 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8927c7d-4483-35ba-84e9-979de5ad6894 | -22.09618 | -45.14709 | 2026-07-22 04:12:00 | NOAA-21 | CARMO DE MINAS | MINAS GERAIS | Brasil | 3114105 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 8cdc1427-badd-3964-80d3-935333d5856f | -22.0923 | -41.1832 | 2026-07-22 04:12:00 | NOAA-21 | CAMPOS DOS GOYTACAZES | RIO DE JANEIRO | Brasil | 3301009 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| df2a4312-f12f-38f1-af50-b5e27d400839 | -21.28687 | -41.74047 | 2026-07-22 04:12:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| b4d4874a-f66a-3b6f-be98-c080aea69866 | -23.27076 | -46.68071 | 2026-07-22 04:12:00 | NOAA-21 | FRANCISCO MORATO | SÃO PAULO | Brasil | 3516309 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 82e032b8-3903-3ece-9909-07bd1ac3042e | -21.28515 | -48.54711 | 2026-07-22 04:12:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ad036a58-dd40-3733-abed-7a70fc940880 | -23.2832 | -46.15884 | 2026-07-22 04:12:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2cfd1f59-e0cd-3815-a456-42d934566942 | -20.24712 | -42.25383 | 2026-07-22 04:12:00 | NOAA-21 | MATIPÓ | MINAS GERAIS | Brasil | 3140902 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| fe2a4dfb-db29-3240-aed5-2f8cb5b515f1 | -22.78399 | -43.65917 | 2026-07-22 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1a11c558-60c5-32c3-bdad-5178a32429c5 | -23.18046 | -46.12074 | 2026-07-22 04:12:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.1 |
| a0e5f122-f12a-385b-9361-76ffb6101192 | -17.53944 | -52.53296 | 2026-07-22 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b0367ce-d96f-3fb4-a2de-4c88f1587a41 | -18.54387 | -56.81517 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| d96dda16-3d9b-316b-a337-bb2050932bf3 | -20.70679 | -47.29026 | 2026-07-22 04:12:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5116421a-76b2-3c73-915c-b0f0e642e9c1 | -22.71033 | -43.68323 | 2026-07-22 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| cc6ad69a-de38-3121-9b99-eda0b3c881d1 | -17.73935 | -52.75014 | 2026-07-22 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8575a205-c1d1-3786-93a0-85f3df961935 | -23.27821 | -45.52518 | 2026-07-22 04:12:00 | NOAA-21 | REDENÇÃO DA SERRA | SÃO PAULO | Brasil | 3542305 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| b1a41657-72fc-35f9-a28b-080212fedbc5 | -19.19983 | -46.44383 | 2026-07-22 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f7d29f82-bd32-319d-83b5-a4e49d67b6e4 | -19.65608 | -44.89797 | 2026-07-22 04:12:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 295d4538-3c8b-30fd-ae0f-dfb5bd10947b | -22.15016 | -44.53078 | 2026-07-22 04:12:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 1863e6a0-19a6-391f-a290-4f46b49321ca | -18.53883 | -56.80849 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 0890e988-ebb8-3d70-b1ce-06770595e2a3 | -19.6956 | -44.92753 | 2026-07-22 04:12:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7579e216-7a80-36e9-a6ba-61bdbbd10e91 | -23.27988 | -46.15822 | 2026-07-22 04:12:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 2038c3ff-fc7a-3960-a60e-05e3d4d75c7a | -21.60058 | -46.06079 | 2026-07-22 04:12:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| e9555e14-5763-3143-b1b3-564f547e3321 | -23.52147 | -47.2149 | 2026-07-22 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.2 |
| 08233a90-14f5-3a36-a95b-40d27c2d8eda | -19.69229 | -44.92694 | 2026-07-22 04:12:00 | NOAA-21 | PITANGUI | MINAS GERAIS | Brasil | 3151404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22b8c0bd-3663-35d4-bc62-5b95eb29b58a | -23.75046 | -46.80601 | 2026-07-22 04:12:00 | NOAA-21 | ITAPECERICA DA SERRA | SÃO PAULO | Brasil | 3522208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 59660dee-0f52-32ae-8c71-dfdd38738147 | -22.21876 | -47.02758 | 2026-07-22 04:12:00 | NOAA-21 | MOGI GUAÇU | SÃO PAULO | Brasil | 3530706 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| c1d34883-ce08-3a49-bb65-93f2e7ecac01 | -20.71372 | -47.29155 | 2026-07-22 04:12:00 | NOAA-21 | PATROCÍNIO PAULISTA | SÃO PAULO | Brasil | 3536307 | 35 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5ce063db-4fd3-39ac-93f7-558214aae7dd | -17.84566 | -52.48696 | 2026-07-22 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4c1bb220-3d48-33cb-af0e-b25bfb0375aa | -18.54626 | -56.81886 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f87c97a2-f009-3c2b-bec0-8420bd6e370f | -23.18181 | -49.69451 | 2026-07-22 04:12:00 | NOAA-21 | RIBEIRÃO CLARO | PARANÁ | Brasil | 4121802 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| c321f7f2-8b5e-3835-8759-2e8769ae8e59 | -23.76744 | -47.44437 | 2026-07-22 04:12:00 | NOAA-21 | PIEDADE | SÃO PAULO | Brasil | 3537800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f3d67e44-5d15-3d38-8666-2213cce592c5 | -21.88778 | -45.56388 | 2026-07-22 04:12:00 | NOAA-21 | SÃO GONÇALO DO SAPUCAÍ | MINAS GERAIS | Brasil | 3162005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 4c0b683b-ed05-39f6-a695-03533dcac552 | -19.71748 | -50.20932 | 2026-07-22 04:12:00 | NOAA-21 | ITURAMA | MINAS GERAIS | Brasil | 3134400 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| d4b3cd59-4781-3122-8693-2e4fe923a4e8 | -20.99592 | -43.98641 | 2026-07-22 04:12:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| f8639b04-3cb7-3349-a233-5be1c6d4f3c6 | -22.57432 | -42.76493 | 2026-07-22 04:12:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| b6545c4b-3139-3d1a-89f5-58939c38fc21 | -19.19918 | -46.44768 | 2026-07-22 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 04c28d90-3700-3990-ace2-96f070398e82 | -21.0042 | -42.57829 | 2026-07-22 04:12:00 | NOAA-21 | SÃO SEBASTIÃO DA VARGEM ALEGRE | MINAS GERAIS | Brasil | 3164431 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6df6b217-9150-33a8-9ba3-28da9a18ced4 | -23.14486 | -48.67527 | 2026-07-22 04:12:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d49d6770-3cd1-3c6f-903c-cf2acef4b4bc | -22.14248 | -44.51403 | 2026-07-22 04:12:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 8733f52e-e64c-3509-b928-95ae384f9004 | -23.18106 | -46.11697 | 2026-07-22 04:12:00 | NOAA-21 | IGARATÁ | SÃO PAULO | Brasil | 3520202 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.1 |
| 47910c80-b7ee-38bc-9983-5708280e14c6 | -23.14131 | -48.67443 | 2026-07-22 04:12:00 | NOAA-21 | ITATINGA | SÃO PAULO | Brasil | 3523503 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56d94a7e-85a2-36bd-9fc5-bda076c129ea | -23.1965 | -49.15029 | 2026-07-22 04:12:00 | NOAA-21 | CERQUEIRA CÉSAR | SÃO PAULO | Brasil | 3511409 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 00ca8e86-327d-3385-88aa-bf43f47aceef | -18.53883 | -56.82265 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.9 |
| daef76c5-9733-394d-b30a-6af3bac66b28 | -22.87094 | -43.32025 | 2026-07-22 04:12:00 | NOAA-21 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| bbc3d13f-edb6-3064-9d34-e74e7bad85b6 | -23.27927 | -46.162 | 2026-07-22 04:12:00 | NOAA-21 | SANTA ISABEL | SÃO PAULO | Brasil | 3546801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 551bfd8e-9f66-3aeb-86c5-db9cc84411cd | -17.84265 | -52.48932 | 2026-07-22 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 62f3e98b-a98a-3b87-9913-71ee4a1f8cea | -17.73441 | -52.749 | 2026-07-22 04:12:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 531c3d70-3618-344c-a9f8-53b3216aa746 | -18.54119 | -56.81212 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 0753fc8a-f388-32b5-8bc3-7fc196968653 | -20.99314 | -43.98211 | 2026-07-22 04:12:00 | NOAA-21 | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| fdfc30c3-4ec3-3b5a-8123-e14eaa8d347a | -23.40919 | -46.43579 | 2026-07-22 04:12:00 | NOAA-21 | GUARULHOS | SÃO PAULO | Brasil | 3518800 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 08c7c34c-e865-3401-8fff-b908da36119b | -19.19577 | -46.44709 | 2026-07-22 04:12:00 | NOAA-21 | RIO PARANAÍBA | MINAS GERAIS | Brasil | 3155504 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8fdb8032-59b6-3986-bcb8-6d6fcafa30bb | -19.5213 | -49.68847 | 2026-07-22 04:12:00 | NOAA-21 | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 6eb62dc2-18d6-36cd-8b0a-e3146fb14cec | -23.94878 | -47.22008 | 2026-07-22 04:12:00 | NOAA-21 | IBIÚNA | SÃO PAULO | Brasil | 3519709 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| defd18a5-f764-33fa-8c1e-65539c029169 | -21.2012 | -47.88282 | 2026-07-22 04:12:00 | NOAA-21 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 8.5 |
| e54817fc-bbf1-366b-9edf-6244428d3d9c | -18.53495 | -56.81063 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 87f5efbd-0d1b-3bb7-8ada-7980721941c1 | -18.53613 | -56.80538 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| f8c8c219-467d-3cca-ad2e-f616aca3f818 | -21.63355 | -44.01171 | 2026-07-22 04:12:00 | NOAA-21 | SANTANA DO GARAMBÉU | MINAS GERAIS | Brasil | 3158706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.6 |
| 5b99aff3-e43f-343c-9439-bc623ed94d70 | -21.6033 | -46.06514 | 2026-07-22 04:12:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 1efed59b-d73b-3314-b7ed-c59a92ee45d5 | -23.38732 | -46.3378 | 2026-07-22 04:12:00 | NOAA-21 | ARUJÁ | SÃO PAULO | Brasil | 3503901 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 9cbe4f66-1dd7-3b45-b7b8-8a0372e2005a | -21.19888 | -48.269 | 2026-07-22 04:12:00 | NOAA-21 | JABOTICABAL | SÃO PAULO | Brasil | 3524303 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 000ac2b8-bf76-38a5-a3e1-6842d9bd1ecf | -22.57346 | -42.7616 | 2026-07-22 04:12:00 | NOAA-21 | CACHOEIRAS DE MACACU | RIO DE JANEIRO | Brasil | 3300803 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b5f8d30e-53ba-3d50-aa20-1652cca67119 | -21.70271 | -47.16779 | 2026-07-22 04:12:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 583f639a-15cb-3350-8865-8e1181ab90f2 | -22.14628 | -44.53395 | 2026-07-22 04:12:00 | NOAA-21 | BOCAINA DE MINAS | MINAS GERAIS | Brasil | 3107208 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 0efc01a8-626f-3c0a-9622-956da3a119bf | -20.39711 | -46.49923 | 2026-07-22 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b18563b0-5fa2-3a4f-94f4-003927681916 | -20.40113 | -46.49604 | 2026-07-22 04:12:00 | NOAA-21 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b68bf26e-54fd-3907-8e28-fff5b108b206 | -21.29047 | -41.74102 | 2026-07-22 04:12:00 | NOAA-21 | ITAPERUNA | RIO DE JANEIRO | Brasil | 3302205 | 33 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| d85ed29f-1ce3-3d62-9716-faba91994ccf | -19.86588 | -43.87097 | 2026-07-22 04:12:00 | NOAA-21 | SABARÁ | MINAS GERAIS | Brasil | 3156700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2d21ffba-f2f1-383a-af7c-276915b0b238 | -22.79698 | -49.34111 | 2026-07-22 04:12:00 | NOAA-21 | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7a925ae1-607c-319c-a803-c5d28accab93 | -21.26814 | -49.59052 | 2026-07-22 04:12:00 | NOAA-21 | MENDONÇA | SÃO PAULO | Brasil | 3529500 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 607c6c68-24d1-322a-9a1b-3cd52dece7ea | -23.78174 | -49.04107 | 2026-07-22 04:12:00 | NOAA-21 | ITABERÁ | SÃO PAULO | Brasil | 3521705 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 340f8634-7bcf-3d16-b1f7-b1bb308edb6a | -21.51509 | -48.60931 | 2026-07-22 04:12:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02cd7d06-c0f8-3c18-b387-67f7fd6068f9 | -23.52049 | -47.21486 | 2026-07-22 04:12:00 | NOAA-21 | MAIRINQUE | SÃO PAULO | Brasil | 3528403 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| b7f45551-a83b-3389-b993-12214ca0efde | -18.53762 | -56.81372 | 2026-07-22 04:12:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 427b2a64-c4a0-30a5-bf94-67eb7921ede1 | -21.59997 | -46.06454 | 2026-07-22 04:12:00 | NOAA-21 | MACHADO | MINAS GERAIS | Brasil | 3139003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| c4edea07-e2c5-3d4c-be0b-2edc9254c033 | -22.71147 | -43.67541 | 2026-07-22 04:12:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 5ed32e9c-b52d-3605-9761-e227976cb3b1 | -21.70613 | -47.16843 | 2026-07-22 04:12:00 | NOAA-21 | CASA BRANCA | SÃO PAULO | Brasil | 3510807 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9402e129-be70-3fc0-83f1-75fb87ace5cd | -20.47892 | -45.41538 | 2026-07-22 04:12:00 | NOAA-21 | FORMIGA | MINAS GERAIS | Brasil | 3126109 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| c6dcb77e-c9b2-34ac-aac1-35bafdccef4a | -17.5748 | -47.4996 | 2026-07-22 04:20:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 8973992d-a670-3cc6-b6c5-ab07d29d6585 | -17.5748 | -47.4996 | 2026-07-22 04:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 74.9 |
| f8286af1-8bf2-37bc-8675-9a8ad9b8fda1 | -17.5947 | -47.4956 | 2026-07-22 04:30:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 49.7 |
| 5f30724b-db0f-3599-be13-b8c565a371c1 | -17.5947 | -47.4956 | 2026-07-22 04:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 49.1 |
| d81f5866-2a08-370e-93c7-282c5bd56578 | -17.5748 | -47.4996 | 2026-07-22 04:40:00 | GOES-19 | CATALÃO | GOIÁS | Brasil | 5205109 | 52 | 33 | nan | nan | nan | Cerrado | 79.1 |
| 39d6ec74-7b8d-3a38-a013-a362f33311d7 | -3.73143 | -49.27068 | 2026-07-22 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9c2b55fa-9a5d-3a86-bc7c-4f149393de35 | -3.73084 | -49.2744 | 2026-07-22 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4f7b2077-2c63-38b9-b65e-50f7c8c65383 | -3.63607 | -49.70956 | 2026-07-22 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 50e99483-62cf-323a-9a57-adc50f262901 | -3.63955 | -49.71011 | 2026-07-22 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b239a9b8-2089-3fdd-b2f8-ebed8de163d8 | -3.72742 | -49.27384 | 2026-07-22 04:42:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 669d7b92-f228-37cf-b8df-ae389beb58ae | -3.72801 | -49.27013 | 2026-07-22 04:42:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41c4d15e-c2d2-3d50-ab12-02e418542829 | -3.63666 | -49.70587 | 2026-07-22 04:42:00 | NPP-375D | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 311fdb00-ccd4-30aa-b05e-8fd00bf8472c | -9.69927 | -47.70295 | 2026-07-22 04:44:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd2207a6-a7e1-30be-a051-a1cc6557694d | -4.72221 | -44.3545 | 2026-07-22 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |


[Clique aqui para ver as próximas entradas](README6.md)
