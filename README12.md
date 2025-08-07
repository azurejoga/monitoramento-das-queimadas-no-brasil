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

## Dados Diários - Página 12

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cf0b4186-5982-394c-aabe-7be77b1ab352 | -12.55138 | -44.7439 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cd4af202-e70e-304f-8ea9-ade803a88953 | -9.62252 | -43.8483 | 2025-08-07 04:02:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cf74b7a3-67d8-3ef5-94f2-890634bb541d | -12.71181 | -46.38146 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 9251b6a2-30af-39c4-bee8-5d052d67e6d1 | -14.3519 | -51.09608 | 2025-08-07 04:02:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8c1c3122-fdcc-300e-a4a1-9646e644c42b | -11.75917 | -47.51402 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 863cbf7f-90bc-3ecd-975d-9dd4b437e49b | -10.43668 | -44.38133 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c97cb2ca-ccca-3e18-acb0-5cf885c4ca73 | -13.00016 | -44.88432 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 865f7301-4dee-39be-a479-a7214c442993 | -10.42354 | -44.39253 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 917f844e-11d3-3d42-a07e-798931c96265 | -12.71296 | -46.39823 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c19c7814-3707-3c25-820f-7ed6705e5c06 | -10.48193 | -44.37976 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cb4e8ac6-8270-30e9-bf26-a06b0d945e42 | -10.4396 | -44.38631 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d867c6a5-53b3-3c33-94b4-54940c68e3aa | -15.92986 | -43.51574 | 2025-08-07 04:02:00 | NOAA-20 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.2 |
| d206fe92-7888-3254-91d5-8e470b99c1f9 | -16.21738 | -40.1351 | 2025-08-07 04:02:00 | NOAA-20 | SANTA MARIA DO SALTO | MINAS GERAIS | Brasil | 3158102 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| fb0e9976-8464-381b-8695-48922a069e33 | -12.55573 | -44.74026 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1385c026-34e1-343e-b507-4255434777e0 | -10.27956 | -40.81409 | 2025-08-07 04:02:00 | NOAA-20 | CAMPO FORMOSO | BAHIA | Brasil | 2906006 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 9551e030-4c23-322c-b6a9-cc18c600dd95 | -11.77687 | -47.54034 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| cb91792a-cfc3-37fb-a5d2-b3bc233a6616 | -12.32838 | -46.06259 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 123a79e8-8faf-30c7-a4f9-4275d97a790a | -10.62717 | -44.7454 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 05e04e70-a3e4-3bbb-8c4d-426ba9d1247f | -12.71577 | -46.3822 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 37bfe414-18e6-3212-b880-d70f370da3f5 | -15.34963 | -46.34621 | 2025-08-07 04:02:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f32eff69-3042-3f9b-9c63-1d2b46a1dddf | -11.75482 | -47.51342 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e1608c09-6ab0-34fd-b9a5-afa94ba1a6ca | -10.58822 | -45.2504 | 2025-08-07 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19bcaace-c730-30e6-a64d-db76f9362641 | -7.91356 | -45.53323 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a5512283-c3fb-33e6-9734-6c54a79b0fdc | -11.61662 | -42.10849 | 2025-08-07 04:02:00 | NOAA-20 | IBIPEBA | BAHIA | Brasil | 2912400 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| b6ad86ab-01c0-322c-8d52-746f1efdc2b9 | -13.00378 | -44.88501 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 95e3ad2d-df18-3b11-bd1e-18a67307cecf | -13.00305 | -44.8893 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 350d235a-0056-3c67-93c7-7402e5ae5e4d | -15.32829 | -43.80272 | 2025-08-07 04:02:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 22819390-b70c-34c5-835a-78b44506102a | -12.34748 | -45.77061 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| de7e2357-cfbd-31f0-973f-eab7b642c754 | -11.7871 | -47.53305 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0bed5863-2b07-3c46-96af-1b474ba6b547 | -12.54105 | -47.15245 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3a848e91-bf62-38c7-ba59-7388f244a110 | -12.71445 | -47.796 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| eb5b3478-c343-3d0f-be9b-a3d79077d095 | -9.47008 | -46.29738 | 2025-08-07 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 42b57472-92f6-30f4-8cfe-158f990600d1 | -13.00449 | -44.88075 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 62ff251a-1ce2-3c5a-9a28-8beba4904e4a | -11.78776 | -47.53611 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3c34da93-9f05-3ca6-be5f-84b29a7a6eeb | -12.643 | -48.11194 | 2025-08-07 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 75924068-64cc-34fe-ae39-a3049d2b1130 | -12.70506 | -46.39664 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5584d34a-844e-364c-be7e-4f5f94dd58d1 | -10.63972 | -44.75056 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 35389f94-1cdf-3bf7-9070-85c76ada4b6f | -10.6353 | -44.76529 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| e0d831f8-8cb3-39c6-abee-16e03899a1c5 | -12.33316 | -46.05825 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5494bf9f-6938-3c15-8bff-09c52098327d | -12.33707 | -46.05896 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c62182d3-e2b7-3c06-8c66-82db06701c87 | -6.91747 | -52.84902 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 34752a22-db36-3e41-9f11-4209155eee46 | -7.91417 | -45.52969 | 2025-08-07 04:02:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 612910fa-6d1e-3c94-9443-a1d48ebf0f33 | -7.8185 | -46.88176 | 2025-08-07 04:02:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 47525501-a61a-3ab5-90bc-1efd58aa2b81 | -10.64051 | -44.75696 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| af5066c1-2117-3025-9815-3c301d306de6 | -9.08628 | -45.06063 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 57197f31-f038-3d14-a1ee-7f9326e0628b | -10.62788 | -44.76397 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 3ae03c9e-eeb6-3566-8dd2-15bd36c4f4a2 | -9.08545 | -45.06545 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 0eabb808-1e65-39f0-bbce-c5b7c72adcac | -13.00088 | -44.88005 | 2025-08-07 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 729326ef-c9a4-3eac-ac7d-2d7ff2e072d1 | -10.59204 | -45.25106 | 2025-08-07 04:02:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 166f8d13-1801-3c77-89e6-8403fe959c25 | -9.07939 | -45.05448 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 199b95d0-203b-3f20-999d-462f25b09230 | -10.63234 | -44.76014 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 8.3 |
| f5babeec-530b-3a59-b145-8323d358f40c | -8.41789 | -46.84017 | 2025-08-07 04:02:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 169ddb4b-769c-3258-8c3a-a72e87b6284e | -12.70901 | -46.39744 | 2025-08-07 04:02:00 | NOAA-20 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 7213c9b9-b22b-3f69-b7fc-5e7cc6ca58d6 | -12.37264 | -47.0464 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 224b9d8e-5c48-39ac-8114-38dde158fad9 | -8.24604 | -45.07555 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 154e4c8c-6f8a-3e28-b4c8-d64a7ea1361d | -11.89398 | -44.97173 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6ee3379-4b7e-3184-a020-97b15586c78b | -14.52528 | -45.59608 | 2025-08-07 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bc8375d4-3944-388c-a0a2-a5cfca18be36 | -6.95224 | -51.63042 | 2025-08-07 04:02:00 | NOAA-20 | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 90f50977-998a-3d40-b1cf-beb30a1611ce | -10.43013 | -44.37571 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5235d7bb-f4d8-33a9-9295-7a6ff89b1d2a | -10.63605 | -44.7608 | 2025-08-07 04:02:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| fcb3bceb-05c4-3237-83f8-bb79587f5a38 | -10.42937 | -44.4025 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4cd5f90d-8a67-3aba-ac60-78f5c04aaca5 | -10.46076 | -44.3944 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3a1b8563-e5c8-33f8-a4f8-be5ca9e98839 | -9.06698 | -45.05737 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1f954c25-9ed7-32a2-9c66-035b833ce1ba | -15.77638 | -39.3702 | 2025-08-07 04:02:00 | NOAA-20 | MASCOTE | BAHIA | Brasil | 2920908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| fdf2474c-56db-34f1-a82b-b43e1e6191d5 | -6.912 | -52.84177 | 2025-08-07 04:02:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 11300344-9f89-392d-baf6-c50edc089bda | -11.77648 | -47.51718 | 2025-08-07 04:02:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9b5623c8-5758-3ef2-8391-21caeeaca47a | -12.37611 | -47.05101 | 2025-08-07 04:02:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 11f1b5e3-ea43-313e-873e-5ebbd5b496c7 | -10.43886 | -44.39067 | 2025-08-07 04:02:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 673eabbf-68de-3d22-8c5a-7ef4191a346b | -11.28336 | -40.97549 | 2025-08-07 04:02:00 | NOAA-20 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| dc243071-32e5-3cff-b0b0-fef02fcf9b4f | -13.24185 | -47.00365 | 2025-08-07 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 76a9e15a-44eb-3d04-82ca-ba14b6aadfeb | -9.08325 | -45.05514 | 2025-08-07 04:02:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5404cb1d-71ae-3f75-8962-579ae9a448c2 | -8.24911 | -45.0812 | 2025-08-07 04:02:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 190c46c6-0094-33cd-908a-1b7f24acf59b | -12.33404 | -46.05322 | 2025-08-07 04:02:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0c0133df-bec7-3c1a-b27d-8b7e12855e8a | -11.75052 | -44.95255 | 2025-08-07 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6dde114c-0e26-34f6-93f5-e175164d075a | -8.50679 | -44.74914 | 2025-08-07 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 1facd557-9622-3085-808c-b63b42e4d229 | -21.63417 | -49.842 | 2025-08-07 04:04:00 | NOAA-20 | PROMISSÃO | SÃO PAULO | Brasil | 3541604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b35dc2fa-edfe-3065-8563-c4d791658334 | -19.84803 | -49.07507 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16dea877-75d1-3479-8e16-ab7014d14e6c | -23.12928 | -46.71935 | 2025-08-07 04:04:00 | NOAA-20 | JARINU | SÃO PAULO | Brasil | 3525201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 9b7e4373-0bcd-3d91-ace1-d4a87ae3af80 | -17.65793 | -42.26653 | 2025-08-07 04:04:00 | NOAA-20 | ANGELÂNDIA | MINAS GERAIS | Brasil | 3102852 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91b778c6-4f66-3f8d-9aa5-fa22834f0d76 | -22.33673 | -47.20927 | 2025-08-07 04:04:00 | NOAA-20 | ARARAS | SÃO PAULO | Brasil | 3503307 | 35 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a8bdaa30-06af-3d26-a1c3-ff128c183554 | -22.77977 | -43.04135 | 2025-08-07 04:04:00 | NOAA-20 | SÃO GONÇALO | RIO DE JANEIRO | Brasil | 3304904 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| b4a78fad-6202-3cea-95eb-b054d1bd310f | -20.70091 | -45.46462 | 2025-08-07 04:04:00 | NOAA-20 | CANDEIAS | MINAS GERAIS | Brasil | 3112000 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 371655ef-c9b0-3a0e-bc3e-ccfff94cd0bf | -20.02851 | -44.14707 | 2025-08-07 04:04:00 | NOAA-20 | SARZEDO | MINAS GERAIS | Brasil | 3165537 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 77544dc0-05f8-3d47-9634-4e61810ca489 | -21.23979 | -49.08336 | 2025-08-07 04:04:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| ebbcea02-1e55-3eb6-ba34-e31ce8c08dc4 | -17.20089 | -44.32402 | 2025-08-07 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2cf5d65c-8509-33f7-93fa-10f78d228053 | -18.84297 | -47.05008 | 2025-08-07 04:04:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8becad55-e91f-3593-936a-ec577f2195d7 | -21.23907 | -49.08713 | 2025-08-07 04:04:00 | NOAA-20 | MARAPOAMA | SÃO PAULO | Brasil | 3528858 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| d36b5bcd-e7e1-3a24-8839-4d4d3dc02954 | -17.59563 | -43.19735 | 2025-08-07 04:04:00 | NOAA-20 | CARBONITA | MINAS GERAIS | Brasil | 3113503 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c742fb9a-88cd-3de5-9b78-3a47953728ef | -17.68076 | -44.43822 | 2025-08-07 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ee63abe-ba8a-3652-806c-45a2d2145b8b | -17.98658 | -42.94089 | 2025-08-07 04:04:00 | NOAA-20 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 077b9750-9348-3aa7-a0bf-18ceabfd4755 | -17.67737 | -44.4376 | 2025-08-07 04:04:00 | NOAA-20 | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 52571742-dfea-3765-bcb2-acf0aa9ccfba | -21.86834 | -42.88377 | 2025-08-07 04:04:00 | NOAA-20 | ALÉM PARAÍBA | MINAS GERAIS | Brasil | 3101508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6d7fc3b6-6e2b-31a5-b35b-3c5fdff6661f | -17.24323 | -42.22692 | 2025-08-07 04:04:00 | NOAA-20 | CHAPADA DO NORTE | MINAS GERAIS | Brasil | 3116100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d13eba4e-d4ba-391d-bbbf-737f17d80505 | -19.95058 | -48.90777 | 2025-08-07 04:04:00 | NOAA-20 | FRUTAL | MINAS GERAIS | Brasil | 3127107 | 31 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 17297adc-d1bb-393b-912f-570ad86601bb | -16.03973 | -43.72057 | 2025-08-07 04:04:00 | NOAA-20 | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e99e17e5-a7dc-35dc-aa7a-1e0863dd5d43 | -17.20025 | -44.3278 | 2025-08-07 04:04:00 | NOAA-20 | JEQUITAÍ | MINAS GERAIS | Brasil | 3135605 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 46aa0e1f-5467-3e1f-abcf-28845cfc2260 | -22.06797 | -47.32194 | 2025-08-07 04:04:00 | NOAA-20 | PIRASSUNUNGA | SÃO PAULO | Brasil | 3539301 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| c1a402af-1b3f-3756-8f4f-481489d4b088 | -21.76396 | -48.86348 | 2025-08-07 04:04:00 | NOAA-20 | IBITINGA | SÃO PAULO | Brasil | 3519600 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 8afd431e-8bed-32bf-b8f6-80e76baaa35e | -18.73101 | -39.86569 | 2025-08-07 04:04:00 | NOAA-20 | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| b82b53ee-8678-3fd7-a21c-59b35aaaa5c3 | -18.89616 | -41.00428 | 2025-08-07 04:04:00 | NOAA-20 | MANTENÓPOLIS | ESPÍRITO SANTO | Brasil | 3203304 | 32 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |


[Clique aqui para ver as próximas entradas](README13.md)
