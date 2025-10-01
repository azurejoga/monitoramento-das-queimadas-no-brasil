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

## Dados Diários - Página 127

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e70c666b-eb16-3b8f-879d-becc369e82db | -13.54057 | -47.27023 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 7767d6eb-ed30-39a0-9dd5-57dee432c9d3 | -11.56833 | -50.18907 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 7d23d280-c507-3479-8590-abaa77b7c318 | -12.85477 | -46.94814 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| eb738194-8aa0-3dd3-964e-0ce758f38f01 | -11.83648 | -48.06145 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 44cbf58a-ea41-3692-be3a-76f43df1b243 | -12.97887 | -48.42015 | 2025-10-01 05:10:00 | NOAA-20 | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| e34effba-ea47-3254-a3d0-44f361763dbb | -10.47704 | -55.61965 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63572ca4-ee7f-356b-863b-c2e20e8778ac | -9.2993 | -54.53115 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dcb7ab7f-5d56-37a3-8b4f-1a75163bc5d8 | -6.30753 | -55.14584 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33615b12-14eb-3afd-aa6d-3c2b0b51a7d0 | -11.15077 | -54.12189 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 73cd0b17-20d0-39f1-9b1a-06f28dc826ec | -11.67071 | -46.97029 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 14.5 |
| 96443235-dfa2-3677-a49e-36e43e869001 | -9.58045 | -54.59869 | 2025-10-01 05:10:00 | NOAA-20 | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 23f4082c-31f0-39b5-9b05-61ce2b052b7f | -11.48372 | -54.60152 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 81a771b8-a2ed-3dc0-a869-1456962fec7e | -11.15911 | -54.11819 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4797bcb4-1b07-3fdb-b16b-d9c0cc721dc9 | -11.7655 | -46.84735 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ffa737c1-cff7-3df4-b992-79e6b2c0824d | -10.18961 | -52.55552 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 626c2ed4-f0f5-3145-adc6-07cd822d0535 | -10.07088 | -50.27706 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.7 |
| dabaebd6-2799-34da-b315-48426e8a5388 | -11.84176 | -48.06614 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| a0080c69-f36f-375f-93ba-0d002b4f8083 | -11.45512 | -45.03048 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 15ed3a30-1b80-33df-b8d2-456c01f91d2c | -12.82329 | -47.01971 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| a0e4a665-dffd-3751-ae6d-61f6f9ef1d9c | -13.33394 | -47.81469 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c605316-8e67-3c5c-9335-4fb1c66367d6 | -12.37628 | -50.20358 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3fcecd61-bacb-3dba-b8d3-c8ac14075a4e | -12.46041 | -50.22218 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12859f64-0a0e-31f2-859d-5b92c93465fe | -13.35862 | -48.10273 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8d6a02bc-0802-3af4-86c0-58985373237f | -8.14921 | -46.27972 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3e571b3d-7f0f-38b5-ac7c-a6b9b7f203fc | -7.39605 | -46.98147 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 275d5fff-c228-3526-b3f6-28ab436b420a | -9.41187 | -47.33998 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| c64473a0-71a2-3269-aeab-1a9001a01c39 | -11.57004 | -50.17762 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 22e01796-c3cb-34c8-99c1-aa58cd373293 | -10.48055 | -55.62019 | 2025-10-01 05:10:00 | NOAA-20 | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff28a1bd-6a10-3eea-9eac-41a1c84a697a | -13.41152 | -48.20241 | 2025-10-01 05:10:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c7998021-5b61-3a4a-941c-4c2a45aefccd | -7.76749 | -47.38664 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 90e6aa39-f63c-37f8-8d1c-47460b5e0851 | -10.93174 | -54.3342 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c21ca7ce-1b37-33bc-a436-862ac825baaa | -10.625 | -48.59918 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 843a0177-8f04-35a6-a7cc-a80cef3a8a10 | -7.02039 | -44.46463 | 2025-10-01 05:10:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac160f15-f4fb-3e10-af5f-01dc6e47d540 | -7.39626 | -44.60785 | 2025-10-01 05:10:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 5c96f0dc-e52a-32ee-b2fe-3957a3a3e29f | -7.29938 | -47.30781 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 80ab41c8-d89b-3ef9-8edc-5e18671673a5 | -10.77964 | -45.37208 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03fc9a44-2bbe-3e56-a6cd-57b6e92824fb | -11.48745 | -54.60208 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b8683bc-ff6f-3cda-b83a-2cbf31132b58 | -7.12764 | -47.78533 | 2025-10-01 05:10:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3af81c39-f6c3-3b72-9818-48221645ba75 | -13.0632 | -47.08558 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d71251f1-b1df-3abb-8c2a-bfcacd9690fd | -13.28856 | -47.24008 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ef2c91f7-a518-31cb-918a-facaa58ce0b0 | -11.76014 | -46.85342 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8f42df53-bee3-3fbe-88fe-add7a01e635d | -11.59985 | -45.05367 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9c979907-8e54-359b-b1e5-b99c93fde09d | -8.55707 | -44.75904 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 567d8171-50a7-3735-b445-870065d2e937 | -8.98361 | -50.19912 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0270424c-b354-3ee8-ad03-544db717e0f8 | -12.61868 | -44.86353 | 2025-10-01 05:10:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 3c5d4270-5376-3096-ad5e-d757a5e97cda | -11.82674 | -44.96409 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| e3aca8ca-b4ee-3088-97fd-5d442d526c86 | -11.82314 | -44.99645 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a5e6e5e1-31ac-39a4-bdd1-bba89fc5055b | -10.63178 | -48.58964 | 2025-10-01 05:10:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5f0f71f2-cdcb-30d9-ba61-1bddfd59f72d | -7.29886 | -47.3116 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| debcd482-089e-3e74-a054-b5bd0c87c63d | -11.92154 | -47.89833 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 1dd1df3c-f390-3564-a035-758a1e88e2e7 | -10.07242 | -50.29043 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 8859440e-5333-392c-8374-248322138d5b | -12.46584 | -50.21984 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a1a2763d-b9e6-3f31-87f1-0da695add4af | -11.14695 | -54.3139 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 286db84f-66fe-3931-bb6e-1292c66bae69 | -11.46169 | -45.09794 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a9e1cedf-8e01-3c6d-b0d8-8f7f36c1c4f5 | -8.55572 | -44.75847 | 2025-10-01 05:10:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4d085ce5-3168-3ba7-a7fc-0af4b6154b31 | -7.88286 | -47.2785 | 2025-10-01 05:10:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 93c9b5ae-1882-3fb9-aa84-7df67d327504 | -13.23425 | -47.33219 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 825901cb-0923-3c60-a270-d48b54381a29 | -9.51766 | -54.74427 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| db89ea78-acd5-3343-8048-e8c257b5745c | -13.31434 | -47.22158 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| f8b37e44-4204-3f03-9955-5ed664c15b76 | -13.30713 | -47.22997 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fcbd2002-c27b-3795-a79a-93f89e71e7f1 | -11.15206 | -54.30511 | 2025-10-01 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6411485-f638-3f11-acd3-83550e664edd | -10.06552 | -50.26738 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 12.1 |
| 55d613db-d997-3ec1-9f12-f1f78cfcd67e | -10.74223 | -45.37841 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6c921d11-994d-3a84-8582-364d79531bec | -12.43449 | -50.1823 | 2025-10-01 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3db75855-44b4-3fd6-9277-fb5eaadc03be | -11.82606 | -44.97025 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 882fd03a-a1d5-3cf2-a11a-fd559bd49241 | -8.92527 | -47.57892 | 2025-10-01 05:10:00 | NOAA-20 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| c16b26da-793f-3696-b405-cadb2eca1eef | -13.53376 | -47.26139 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6ec9f7e6-8aac-39be-90b7-3c08dfbc9a51 | -7.26218 | -48.48093 | 2025-10-01 05:10:00 | NOAA-20 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 86602ff6-3d6a-3323-ae85-c592f9fd8a97 | -11.75396 | -46.83757 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f7a54fc4-3a6f-38f4-8019-861f2e0cff8b | -7.16269 | -50.54564 | 2025-10-01 05:10:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7eb14104-c01e-320a-9fa9-f1785fcf9e08 | -13.32704 | -47.33422 | 2025-10-01 05:10:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 1b6c4be2-582c-320e-97c2-a34b3868b4da | -13.34154 | -48.14799 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 90e7e924-060c-3d20-a5cb-4dac996d955f | -10.06756 | -50.28976 | 2025-10-01 05:10:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ebd37ed2-ccc6-3943-a606-a9187dea68d0 | -13.33161 | -47.83463 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 24cda7e6-e191-359a-8a27-13d8efe91a5f | -9.43269 | -54.71123 | 2025-10-01 05:10:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4e92d788-5eaa-385f-bbbc-9112efb8d2b8 | -7.63051 | -45.45839 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c13cb97f-1c66-3387-a1ed-477ad4f31d55 | -9.81205 | -47.8595 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3fc5a42b-ab09-3e3c-b91c-5e37b828de42 | -9.81826 | -47.85637 | 2025-10-01 05:10:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 8a11e7b4-af96-3d14-ba77-75e89921861b | -7.63125 | -45.45299 | 2025-10-01 05:10:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a557b359-af8a-344a-885c-0ff7dcf4f7e9 | -11.30998 | -53.95411 | 2025-10-01 05:10:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| bd4a9fee-7a2f-3d47-86cd-118c82bc0ce9 | -7.55501 | -46.2835 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4da5e637-5903-305b-9891-82bda1d28e91 | -13.32421 | -48.15057 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7a59ab1-b887-3268-848f-1e38e46c895d | -7.82931 | -47.05875 | 2025-10-01 05:10:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bc5546e3-fe0f-3bbc-8689-ce9a62fc9151 | -11.82745 | -44.95768 | 2025-10-01 05:10:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 863e01b2-1c18-3e66-8b05-b688ea4d415f | -8.89604 | -46.62929 | 2025-10-01 05:10:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6372515-03eb-32ab-ae68-53995b2c1be2 | -12.76217 | -46.88785 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 9de5a4b3-02e5-3c4e-adfb-28abe52a21d6 | -11.41569 | -55.06504 | 2025-10-01 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9d22e7d2-7747-3dfa-affc-1bf2569ac59a | -12.82275 | -47.0243 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9557a269-0b79-3315-813b-c4afddb9874b | -11.75884 | -46.86425 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 1298b0ef-51c8-31f1-8e3e-58beb68e19ff | -11.87101 | -48.02365 | 2025-10-01 05:10:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed01820a-6f87-30d4-acf7-996e4064069d | -12.85519 | -46.9444 | 2025-10-01 05:10:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 36fee5fd-470b-3a5a-b88c-f87e801d46f4 | -11.04524 | -47.82719 | 2025-10-01 05:10:00 | NOAA-20 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 81507d0b-1b15-3e3c-828d-d29d788fec24 | -12.36579 | -50.20523 | 2025-10-01 05:10:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3101b560-bf46-3bda-a952-6abad35f89d4 | -10.19431 | -52.55231 | 2025-10-01 05:10:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a267f327-b368-3d8b-939b-12dd56bc05d2 | -11.67129 | -46.96532 | 2025-10-01 05:10:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| 5814af84-e5a0-3a22-82d6-3f8cf02894e1 | -9.44545 | -50.90162 | 2025-10-01 05:10:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a3c401a9-3c35-3428-bb41-657cb3ff73ea | -13.02848 | -48.67397 | 2025-10-01 05:10:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 7382e055-1d08-35eb-b79a-47454d4ea80c | -12.1742 | -51.4143 | 2025-10-01 05:10:00 | NOAA-20 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 34c9846f-7b3e-3b8b-ae23-6d1d7bb4e50b | -8.21642 | -55.20148 | 2025-10-01 05:10:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9c2e4ff3-25cb-3955-96eb-e936bb86ebb8 | -13.32728 | -47.87167 | 2025-10-01 05:10:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |


[Clique aqui para ver as próximas entradas](README128.md)
