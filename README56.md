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

## Dados Diários - Página 56

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80fdda33-3ee6-3388-90c1-16d343fc3c36 | -7.33789 | -42.47124 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 32609e47-5d7f-3486-9dab-6e30b3cb76f2 | -7.42433 | -45.98368 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dc6ae1b7-3b43-3cc1-a5f1-981ea253c7b7 | -3.04709 | -50.26225 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| d09080d7-ef17-3ea0-98dd-229df0e13d94 | -8.76375 | -46.51295 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 4857067a-15b0-32db-acb2-a8560a036f75 | -3.77146 | -51.71148 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5044d1c0-9367-3178-ac63-b03f0f990f24 | -5.65257 | -46.4542 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb8ff9c2-8d6a-38ee-9f50-0f9d174cf17b | -8.24829 | -46.9142 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d67b022-b748-34c2-abfa-cf1b97aecb2b | -6.30002 | -41.88842 | 2025-10-29 04:44:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 11.2 |
| 6d5b4b1d-96b3-34d4-be26-99ffdc12d607 | -6.13992 | -41.68466 | 2025-10-29 04:44:00 | NOAA-20 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4c43201a-5b63-3f5e-b586-c3be9b43cf86 | -6.53145 | -43.57323 | 2025-10-29 04:44:00 | NOAA-20 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 288898b9-5c8c-3fe6-9a08-eb2b915fb388 | -3.74608 | -51.75169 | 2025-10-29 04:44:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 970cd5c7-2d1a-382a-ab44-b3e6ffc70588 | -5.62235 | -44.01146 | 2025-10-29 04:44:00 | NOAA-20 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70f0b4b4-8c3c-3955-97e6-f31e40a7a834 | -4.30168 | -48.06774 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8f628de2-4e3f-3d62-a01a-b5559a24df9b | -7.44959 | -49.40956 | 2025-10-29 04:44:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| a85d8404-5a4d-308c-aa14-474bc2f24506 | -3.40719 | -52.66602 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70f9f274-e2e6-3933-92fb-b79d0003343a | -3.40371 | -52.66548 | 2025-10-29 04:44:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 463bd2b3-4ba0-3c7b-87ca-5f5243be2e03 | -3.25178 | -52.91031 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a2d5c567-3c0f-3471-95aa-5d7b27ff63e0 | -1.49321 | -47.80787 | 2025-10-29 04:44:00 | NOAA-20 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 96f33ca3-0305-319e-88ab-c4a2b3cc2050 | -4.21184 | -50.09328 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| be54ca5b-40ab-3b90-a342-530a8e737f11 | -3.15879 | -49.25071 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c3bbc753-e2d5-36f0-af0e-afee14c0b365 | -6.90581 | -42.86599 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68412f8e-95a9-36ff-b226-819c745d7e6d | -2.42381 | -49.3003 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a74e9f53-161d-30c2-812a-c02798709379 | -8.00267 | -46.20752 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 88de34e5-7fb4-367c-a7b9-37dff4b0d201 | -7.28081 | -44.10126 | 2025-10-29 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cf451fbc-ee2c-3fc7-8d70-fe33e1fcc6d0 | -4.08309 | -42.92022 | 2025-10-29 04:44:00 | NOAA-20 | DUQUE BACELAR | MARANHÃO | Brasil | 2103901 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0f2b1592-ba2d-3945-9fff-10994214ec6d | -4.00742 | -49.03462 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7072acdd-20d2-36c3-afb2-bb069efa9ec8 | -8.61371 | -44.8067 | 2025-10-29 04:44:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a23b0183-b132-3c44-9bcc-4aa2b1203bcb | -2.42049 | -49.29978 | 2025-10-29 04:44:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 03d0bbce-c7bf-356d-b3ca-cae300a1fa48 | -4.21293 | -50.0864 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8e79639f-9f61-3791-a73b-3402f2fc8447 | -4.63515 | -48.69328 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4ddae64-9d8f-33be-a6e7-a3b6de6c45ab | -3.04049 | -50.26122 | 2025-10-29 04:44:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 838d9e9d-1d72-3578-a76d-3a0af4327b59 | -3.82697 | -55.81762 | 2025-10-29 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 398b0a25-1cb6-3c46-ae1d-2297f436bf35 | -7.90064 | -45.681 | 2025-10-29 04:44:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecff2167-3096-3b33-a7a9-cd5b80ee2338 | -4.21125 | -50.07554 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 04d6b1ac-68f8-3abc-8de9-0f9111019fa9 | -7.50581 | -46.2741 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bda985b7-e453-32dc-9e27-47eb6ec7d1e8 | -3.24207 | -48.7781 | 2025-10-29 04:44:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2ec61b14-66ce-348a-b2bb-17d860e3b5eb | -7.74231 | -44.72667 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1d337cb4-1296-36b7-995c-76745cc0f4e0 | -7.85606 | -44.23201 | 2025-10-29 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3014c5e-419e-365d-9922-a8ca54a25cb1 | -3.3275 | -54.08435 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa53a86c-1540-3080-9872-b540dc4f4d8e | -6.98349 | -47.33702 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| af957e84-8a89-3a63-9bbc-fbec5b3d0618 | -3.81116 | -48.65404 | 2025-10-29 04:44:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 79de1f73-8cb1-3967-b25f-54c46b8c8e34 | -8.24513 | -46.90873 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| fe6638dd-ac17-36d9-9e83-e83246d220fe | -4.4118 | -47.96526 | 2025-10-29 04:44:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d5f72ea-0d61-3356-9b74-4d364b736f6d | -8.4059 | -46.92906 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2e9d1cde-03e6-3f50-ad36-ae8734f8b630 | -4.48341 | -43.44364 | 2025-10-29 04:44:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 16.6 |
| a84fdb97-95c8-301c-a7b1-fb5119286ef7 | -5.75496 | -43.39251 | 2025-10-29 04:44:00 | NOAA-20 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 9b504658-f4c8-3526-bea1-2e3c9edf41c6 | -6.1166 | -48.10094 | 2025-10-29 04:44:00 | NOAA-20 | SÃO BENTO DO TOCANTINS | TOCANTINS | Brasil | 1720101 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8b64060-1868-3ab8-93cd-9d0d9732d8e6 | -6.11235 | -42.44732 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 6ad69121-2a36-386d-a2ed-c5c10d01666d | -7.36122 | -47.63357 | 2025-10-29 04:44:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1e5081b7-d1e1-3355-baac-6afac49cb4c5 | -6.10813 | -42.44057 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 699774ee-2c76-30a4-bcd5-0ef9357804ae | -6.12285 | -41.70583 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| f5695ec5-395f-3c82-92e2-41ac49e4266a | -5.79399 | -50.16428 | 2025-10-29 04:44:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 60f872cd-1c44-3790-9e22-2b838da433cb | -7.74709 | -44.71696 | 2025-10-29 04:44:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5894bc15-b62c-3464-b6a6-3c7135a7253b | -6.09826 | -42.4732 | 2025-10-29 04:44:00 | NOAA-20 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 26.0 |
| ed9a7ee1-9b58-3c66-9279-aea081548944 | -2.44634 | -49.00378 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8df73836-9d7f-35e0-9bda-f1bf363afcdf | -4.32276 | -55.61512 | 2025-10-29 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| be14caa2-f732-355d-951a-cf157f9985f0 | -3.51695 | -52.83796 | 2025-10-29 04:44:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 890ac2e2-d229-32d2-a5b4-fb652730b07a | -6.49768 | -42.23559 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 6c098bf5-3d83-35d0-b4be-ef2d34515a17 | -6.80064 | -46.40796 | 2025-10-29 04:44:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| edda1f99-76df-340d-99b9-29debbe86216 | -8.51145 | -47.1996 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9cd33695-ef9f-3df4-b65e-f7a3f405c39f | -2.63681 | -47.95628 | 2025-10-29 04:44:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c276712e-be54-3961-90af-3970fd3a8ab1 | -7.07489 | -44.93642 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 52abfc82-9d3b-3ecd-80b8-2a32b7da9c5f | -6.91123 | -42.86378 | 2025-10-29 04:44:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| d55ce118-ef6f-334c-ab60-b0c21b18428f | -8.72102 | -48.0087 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e5a0cead-0500-30e9-a159-accd58bf18b5 | -6.58364 | -42.65173 | 2025-10-29 04:44:00 | NOAA-20 | FRANCISCO AYRES | PIAUÍ | Brasil | 2204105 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 02ebdd74-81ac-334a-a41d-59dcf7e30cd0 | -7.85673 | -44.22718 | 2025-10-29 04:44:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 70805934-b1a0-39d6-8592-b6f0c9f5e674 | -4.20631 | -50.08537 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| c115f4ed-bf89-3454-8ab9-3e58e125df4a | -7.20166 | -44.16264 | 2025-10-29 04:44:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c7709621-1247-3433-bf0b-4e23a617341a | -7.06858 | -44.47322 | 2025-10-29 04:44:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 6be36f68-aea4-399a-991e-63ad3a4d2f30 | -6.47929 | -42.24451 | 2025-10-29 04:44:00 | NOAA-20 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c0eb2d46-51c2-3f4e-a7ee-8fba596b300e | -3.48112 | -53.96989 | 2025-10-29 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 614472e6-9497-3abe-aa9b-4016a4c1e32f | -5.65642 | -46.45477 | 2025-10-29 04:44:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5006aa46-dce0-389d-bd74-087dfce7fdf1 | -4.2939 | -44.4851 | 2025-10-29 04:44:00 | NOAA-20 | SÃO LUÍS GONZAGA DO MARANHÃO | MARANHÃO | Brasil | 2111409 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f24f3ddc-eb01-3887-ab84-4049e6bcf72e | -6.62795 | -47.18346 | 2025-10-29 04:44:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 034edb43-0a5c-3657-97b3-7499f3a0690c | -7.2971 | -44.98308 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 689fb445-e478-3c09-9a2f-a359811b7ed3 | -8.25534 | -46.92008 | 2025-10-29 04:44:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| da45afed-78a3-32e3-9e2a-439efe8702b6 | -4.21569 | -50.09035 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8ffbca7e-89a5-3290-a8f9-1e11a488d651 | -8.64817 | -47.21743 | 2025-10-29 04:44:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9461a072-203a-3b74-8f6a-f4c46813d3f4 | -7.28093 | -46.89801 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 77c9d45d-a357-3c3c-85d9-c22272f38d11 | -7.63638 | -46.92787 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976efa81-81e8-3585-8c7a-a8b2ef1cbdbc | -2.82956 | -49.39898 | 2025-10-29 04:44:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1f2fc904-e377-36a0-9b74-f55399e681c6 | -3.19816 | -51.00414 | 2025-10-29 04:44:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d478b77f-73bc-3c42-8226-a3f3da4644b3 | -4.49518 | -50.96762 | 2025-10-29 04:44:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5576816d-6f60-3816-ba1d-4e27541ec483 | -4.25075 | -48.57478 | 2025-10-29 04:44:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ca0c26db-68c1-35d6-bb2a-b43f6eb4e7bb | -6.49809 | -42.23264 | 2025-10-29 04:44:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8d07d1e4-1320-3fbb-b1c9-a729b961e5cc | -7.07258 | -44.95282 | 2025-10-29 04:44:00 | NOAA-20 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 82a69cae-289c-3ba6-ae34-e262ea066024 | -4.20908 | -50.08932 | 2025-10-29 04:44:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 32.5 |
| bfba6050-680d-3b74-8580-2758866e9e52 | -7.79541 | -46.45454 | 2025-10-29 04:44:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 65772577-14c7-3af9-b80e-03bf75a741d4 | -8.00316 | -46.20407 | 2025-10-29 04:44:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 0e2fd466-1656-3acf-8b48-8f15292097f1 | -7.15805 | -47.25133 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 181648fa-959d-3ca2-a101-58b43b72c56a | -4.8677 | -48.52731 | 2025-10-29 04:44:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b29959a0-2397-3c30-a985-c618be9f2e36 | -6.98777 | -46.23127 | 2025-10-29 04:44:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f2192d37-49b7-35fc-9f53-bfc56b6cb800 | -7.14693 | -45.80737 | 2025-10-29 04:44:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b534a197-e512-3f26-a9b6-83f15cece383 | -3.66425 | -49.81644 | 2025-10-29 04:44:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e2435ce-30e8-3dba-bebf-40101ca85bc0 | -4.70087 | -46.10846 | 2025-10-29 04:44:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78ac266f-51b3-3855-88f8-f2cfc556ba6b | -6.1381 | -41.85497 | 2025-10-29 04:44:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a637a0bf-b25d-3c87-81ea-f68d7291b7a1 | -7.37349 | -47.02874 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dcc9ac19-79c5-3e86-99bd-4557068726c1 | -8.5472 | -50.03846 | 2025-10-29 04:44:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 9dec50e9-de83-3542-94b2-036ad892b19c | -7.54062 | -47.30826 | 2025-10-29 04:44:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 86d0c683-286a-3957-b235-18591165cd0a | -2.76808 | -45.40015 | 2025-10-29 04:44:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 7.3 |


[Clique aqui para ver as próximas entradas](README57.md)
