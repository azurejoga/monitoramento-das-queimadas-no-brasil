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

## Dados Diários - Página 83

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 934bfd3a-2595-3623-b699-b66868fea2c9 | -14.42417 | -47.33036 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 43259ede-c0b3-3bf0-acd7-9df5579e1d49 | -15.66255 | -47.04267 | 2025-09-12 04:27:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 72e31b74-be10-383b-963e-df5e5f2a65f4 | -13.36514 | -41.92257 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8aa345e-c34b-3201-b59a-a53e62f06d2a | -15.79063 | -52.24077 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 2ba678a6-dd22-30a8-838c-9f098fe26adf | -18.9796 | -47.90044 | 2025-09-12 04:27:00 | NOAA-20 | INDIANÓPOLIS | MINAS GERAIS | Brasil | 3130705 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c11f14e2-4870-3ad1-8a97-56eecd3283a4 | -14.04666 | -40.6346 | 2025-09-12 04:27:00 | NOAA-20 | MANOEL VITORINO | BAHIA | Brasil | 2920403 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 525dea27-526d-39a7-bb43-9ddc058cfa73 | -13.92167 | -48.24073 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| e4688cab-cff7-3027-9a71-ad6f19a31fca | -13.90449 | -48.26336 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 33.8 |
| be4331da-fb19-3824-8a7b-e718a9cd7bdb | -18.6778 | -47.67489 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 846f24b4-2444-39e6-b727-0b090aaa1166 | -18.54155 | -48.41319 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 64d74150-5bdd-3179-9d28-4703eda6c303 | -15.07942 | -48.00475 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| eeb970ed-54ca-3732-a8a7-34c6c1f4163e | -17.13982 | -48.5037 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| acd8ecaa-3fe0-3a81-98b1-7020072f74a3 | -18.65589 | -47.65959 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9643477b-bbf1-3498-a77a-1f1fb93d2cf1 | -17.21516 | -48.6937 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5617c71e-b656-3639-abc0-7b74ddbacb9f | -12.45611 | -47.50039 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8af4d61d-5e71-39e6-9ec5-6b54fac2f876 | -12.98414 | -48.00584 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 74f5d90f-3cc2-3a69-8c4a-d89eab34b242 | -15.23676 | -53.84301 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 808fa986-e559-37a1-b83b-ad6277cadf9a | -14.11548 | -44.32139 | 2025-09-12 04:27:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 108807d7-dcfb-36a9-aa42-f8ae33f409de | -15.79516 | -52.22594 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2c203fd1-c5bc-382b-8964-cb369d755378 | -12.90204 | -48.7925 | 2025-09-12 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5187b3b8-7b5f-3dbf-af9f-d459ae54eb91 | -17.35763 | -46.6998 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 16c202a7-2d58-3372-9923-371072d725ee | -17.80966 | -50.00455 | 2025-09-12 04:27:00 | NOAA-20 | GOIATUBA | GOIÁS | Brasil | 5209101 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 11b86348-eb8e-3339-b6c8-216709ff223a | -17.36508 | -46.69701 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 72ee9a28-7e08-3290-8104-b52a463c0d57 | -15.24013 | -48.17036 | 2025-09-12 04:27:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b545fdf4-3c8b-3355-8eb5-c0c40d599444 | -17.86224 | -44.17036 | 2025-09-12 04:27:00 | NOAA-20 | BUENÓPOLIS | MINAS GERAIS | Brasil | 3109204 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1dd04613-a066-3d47-a24a-6820909d0fcc | -14.38481 | -52.95436 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 23b48acf-31e5-3567-929e-d879fb12823e | -11.9541 | -51.18158 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 41a93876-a673-3898-8f87-c78a1cca366b | -14.50983 | -53.91687 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bfc7bfbd-01ea-3968-9c07-114d8ec96a5d | -12.99188 | -47.99984 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8c1243e4-b197-3b8d-9dfb-03ed06f35527 | -12.93197 | -54.75452 | 2025-09-12 04:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| af20c835-3081-3656-a38d-b4c5616991aa | -19.22342 | -47.22472 | 2025-09-12 04:27:00 | NOAA-20 | PERDIZES | MINAS GERAIS | Brasil | 3149804 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 927e9a1c-ac60-3a03-b70a-da8ee1730e28 | -17.36452 | -46.70089 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ef248b21-7dca-3cb8-a1c5-f0ae2d8b1cb4 | -17.35933 | -46.68812 | 2025-09-12 04:27:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c91d7e08-c82a-363f-9f66-b5f10f593c45 | -13.1722 | -50.09219 | 2025-09-12 04:27:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4aa70f49-f3fb-3e8b-bb13-77a792926e31 | -18.29796 | -50.42705 | 2025-09-12 04:27:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Cerrado | 13.7 |
| c28c4f53-ebf6-32a8-9d2c-bb416108f887 | -17.13877 | -48.48872 | 2025-09-12 04:27:00 | NOAA-20 | PIRES DO RIO | GOIÁS | Brasil | 5217401 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f009a8b2-1469-3d5e-83f4-3eb0ae4aa5d3 | -19.20624 | -43.80048 | 2025-09-12 04:27:00 | NOAA-20 | BALDIM | MINAS GERAIS | Brasil | 3105004 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8dd171fc-827e-3ca2-896c-06fb8e6e269b | -18.61468 | -48.24857 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 85c050d0-1268-3494-9bc7-6fa2bde81f6c | -17.66777 | -46.67834 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8354722c-6c85-3e9f-98fa-7bcb8d4ad8a9 | -17.37179 | -52.9176 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| f2824412-1b57-3fbd-88e9-03757521cbbb | -17.3809 | -52.95398 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3b1793a1-4503-3f99-9c3c-d5c96229ea6f | -11.94488 | -51.18248 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ab9bc398-ee63-3b64-a7cd-f4bbd267d2e0 | -18.64625 | -48.1478 | 2025-09-12 04:27:00 | NOAA-20 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 15cea187-7eae-35f2-8e4d-241a3b2868d5 | -19.88259 | -41.41981 | 2025-09-12 04:27:00 | NOAA-20 | MUTUM | MINAS GERAIS | Brasil | 3144003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 47df1547-34dd-34bb-b637-a98b1d6f82e8 | -12.90087 | -48.79971 | 2025-09-12 04:27:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b58a4117-ee2b-3598-bbd5-6b85788d5911 | -15.11729 | -48.60339 | 2025-09-12 04:27:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| be888b74-4c7f-3c6f-939d-df97fe1a2174 | -17.21185 | -48.69313 | 2025-09-12 04:27:00 | NOAA-20 | CRISTIANÓPOLIS | GOIÁS | Brasil | 5206305 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c77b6354-cdf3-3274-94b6-69162e3b1ec0 | -12.87111 | -47.94816 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 38f84f48-f688-3acc-9683-651b1dd1689f | -15.15279 | -52.40146 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 3a035206-c3c3-3429-a499-2a3154308d27 | -17.83196 | -52.05315 | 2025-09-12 04:27:00 | NOAA-20 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| e413149b-d5ff-33d4-9c7d-6c3c273cd77b | -15.79665 | -52.22802 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2422ffb2-a188-3f1b-b7cb-7da0c3701168 | -13.36563 | -41.91899 | 2025-09-12 04:27:00 | NOAA-20 | RIO DE CONTAS | BAHIA | Brasil | 2926707 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 6417971a-d156-339f-912c-73e7adb48044 | -18.01971 | -46.85663 | 2025-09-12 04:27:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 3.9 |
| af42487e-e39c-393d-b8f5-5429a0f66515 | -13.78473 | -46.2762 | 2025-09-12 04:27:00 | NOAA-20 | GUARANI DE GOIÁS | GOIÁS | Brasil | 5209408 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| bcf88853-c5a0-3628-876d-a771915b36af | -11.6391 | -50.58128 | 2025-09-12 04:27:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22b63b41-3547-37b3-ad9f-6ceb363dc6c4 | -17.37629 | -52.95804 | 2025-09-12 04:27:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4ea2bc58-3a3e-3dc0-bc3f-d6a69b089d79 | -12.98789 | -46.74495 | 2025-09-12 04:27:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 281d8631-042b-36f1-9d19-0f29ddc417d3 | -14.38753 | -47.34661 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 911bfbfa-06cd-3966-91da-4c5d7bc5f701 | -12.96448 | -46.74128 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 394a30c7-8f1a-372e-8998-95d8fb5513e2 | -18.31554 | -52.07428 | 2025-09-12 04:27:00 | NOAA-20 | SERRANÓPOLIS | GOIÁS | Brasil | 5220504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| df42e9e0-472e-398e-8830-7d7075055267 | -15.22933 | -44.04084 | 2025-09-12 04:27:00 | NOAA-20 | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 83329fd2-a901-3fd5-98a2-f6ee9460dc56 | -19.06847 | -48.73743 | 2025-09-12 04:27:00 | NOAA-20 | MONTE ALEGRE DE MINAS | MINAS GERAIS | Brasil | 3142809 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 144ddfbd-0642-32f3-9cc0-7708f1a55dfe | -11.97755 | -51.14724 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c00e521c-1084-3420-a4a0-a691df17f2c5 | -13.17847 | -47.26574 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fff7571e-094b-31ea-a93e-317027318980 | -12.45943 | -47.50093 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b2793f7-7a05-338e-9d67-8bfbd2db90f6 | -13.90006 | -48.2699 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 36.0 |
| dc463998-6f24-3786-bee1-47020ff0f571 | -18.65026 | -47.65098 | 2025-09-12 04:27:00 | NOAA-20 | ESTRELA DO SUL | MINAS GERAIS | Brasil | 3124807 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 71185a1b-c82c-3e9e-89eb-963e2bf86990 | -14.0842 | -54.00419 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cc7fc2c8-84d3-38dd-abda-ada8446690b7 | -15.08807 | -48.01326 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7832c202-cd77-3eb9-a438-dbaff0c3b7e2 | -16.95397 | -45.81718 | 2025-09-12 04:27:00 | NOAA-20 | BRASILÂNDIA DE MINAS | MINAS GERAIS | Brasil | 3108552 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 50437907-b776-386d-9477-1aff0982616f | -11.98199 | -51.14347 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7092ddd0-62ca-3e47-9779-69023ee90752 | -14.51273 | -53.90131 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| aba7b6ca-ac40-3be6-84a5-4c3931bb3e8d | -16.41383 | -45.68568 | 2025-09-12 04:27:00 | NOAA-20 | SÃO ROMÃO | MINAS GERAIS | Brasil | 3164209 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 57c9e9fc-c57f-3912-a607-f45acdf914d2 | -14.77428 | -48.23947 | 2025-09-12 04:27:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 654e48ea-24bf-3791-a319-7b3916240fa8 | -17.27193 | -46.09153 | 2025-09-12 04:27:00 | NOAA-20 | JOÃO PINHEIRO | MINAS GERAIS | Brasil | 3136306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f08b4a9c-963b-3c58-a60c-65c80d178f3e | -11.92394 | -50.69575 | 2025-09-12 04:27:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 88eefff6-8157-35d9-9f8a-6ad343a04a4e | -12.14976 | -48.69394 | 2025-09-12 04:27:00 | NOAA-20 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 12fca0b2-46ef-3a03-9868-62781a857c7e | -11.95041 | -51.18093 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 2349ba44-4a64-3046-87c2-979dda2ed311 | -12.53702 | -49.13494 | 2025-09-12 04:27:00 | NOAA-20 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a6ae536d-d44c-32f3-8e86-de9a2ba6eda9 | -18.17421 | -50.47455 | 2025-09-12 04:27:00 | NOAA-20 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b9e3aa36-4930-319d-94ee-d373e1719e0d | -15.16033 | -52.40287 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e31c86f6-5020-3072-b360-22999879da18 | -11.97679 | -51.15165 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 513ad89e-41d4-3dff-813e-3566fa07b8c1 | -11.98123 | -51.14788 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f3a00b81-0862-37a6-8abd-5e136dc7be38 | -14.28513 | -53.08518 | 2025-09-12 04:27:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 2854af47-9ddd-3664-ab2b-c325a55df59f | -14.1853 | -46.19468 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d2a8994d-8f59-3beb-a9fc-3a965b86b932 | -14.16454 | -46.19213 | 2025-09-12 04:27:00 | NOAA-20 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 51d7be21-c530-3e81-a15b-392dda0c0279 | -13.14335 | -47.14307 | 2025-09-12 04:27:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 11987db9-0cce-3174-93f1-9a7658d60775 | -15.57224 | -54.75589 | 2025-09-12 04:27:00 | NOAA-20 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d6142260-65b8-3fa8-9608-a1e351e9807c | -15.79219 | -52.23176 | 2025-09-12 04:27:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 8a8374cf-cdae-3dc0-985b-350f5584f79b | -13.22991 | -51.74601 | 2025-09-12 04:27:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abe719a3-f49d-3fcd-b6d1-0eff548eae24 | -14.41643 | -47.31427 | 2025-09-12 04:27:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| db4e15f4-f0d6-3099-825f-e6ec4182d003 | -17.34133 | -42.51833 | 2025-09-12 04:27:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 492db471-951f-36db-8585-aa00ff8b9c8a | -16.26916 | -46.7826 | 2025-09-12 04:27:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b1dc983-c1d0-3791-9aaa-87d818d3c4e7 | -15.10519 | -48.01244 | 2025-09-12 04:27:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 91044e6e-1263-364c-9de5-b39379872b24 | -13.95103 | -48.20565 | 2025-09-12 04:27:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dc67c3d-4912-36a2-b5b4-0e669189f3e4 | -12.51156 | -53.8032 | 2025-09-12 04:27:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2c8f9fc8-54ac-3e83-89c1-afabc7f4fefb | -19.17001 | -47.96194 | 2025-09-12 04:27:00 | NOAA-20 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0ad94b31-2f26-3f87-bf2e-d26192692477 | -19.74148 | -45.94889 | 2025-09-12 04:27:00 | NOAA-20 | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0bf0ebda-be5e-3d4b-8c43-9be3910ef465 | -11.94933 | -51.17871 | 2025-09-12 04:27:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b03613fe-bad0-3ed4-8b47-5ff3dc62885c | -12.82143 | -47.96157 | 2025-09-12 04:27:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |


[Clique aqui para ver as próximas entradas](README84.md)
