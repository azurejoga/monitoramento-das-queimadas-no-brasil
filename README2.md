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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8245ba83-9a98-3c80-8275-ba2c6820d994 | -11.61658 | -52.55104 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 222b7ec7-ce28-375d-8eee-f4d6027434f0 | -6.72506 | -44.37165 | 2026-06-01 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8f63e33a-d9d1-3932-aa33-d1c788a4d01b | -8.14251 | -40.80118 | 2026-06-01 04:17:00 | NOAA-20 | BETÂNIA DO PIAUÍ | PIAUÍ | Brasil | 2201739 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 78292902-65ca-34a0-990a-95456f2ac8e8 | -7.16502 | -44.06964 | 2026-06-01 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99771141-ca79-3e02-870a-ba69e2c89aa6 | -10.80385 | -49.39723 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4d954a86-151b-3f78-8797-c37627f7e9af | -6.72302 | -44.37149 | 2026-06-01 04:17:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e028e663-62ad-3b78-96a6-783614ef0f79 | -11.62873 | -52.56573 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8fdae542-70ea-3575-9393-995936a41720 | -12.06032 | -48.07491 | 2026-06-01 04:17:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99744987-e847-3a8a-928e-e8a7836f4895 | -10.72588 | -46.93354 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bd295143-390b-3eed-a980-d56e66c6b3ad | -6.99344 | -42.88153 | 2026-06-01 04:17:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| e87492db-d1a5-3d27-ae79-8572e7a626cd | -5.61352 | -37.53075 | 2026-06-01 04:17:00 | NOAA-20 | CARAÚBAS | RIO GRANDE DO NORTE | Brasil | 2402303 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 9bec0c5b-510b-3a23-975f-f2da52b6bd5b | -11.32617 | -47.18152 | 2026-06-01 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 8bc4fd9e-f55a-33f6-9135-1846813665a7 | -10.75904 | -46.90947 | 2026-06-01 04:17:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6427005c-9748-3b16-ae02-5b69f3e78d04 | -11.33479 | -47.19576 | 2026-06-01 04:17:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cb47969c-baea-3ed3-a2a4-bf1a5380f519 | -7.16891 | -44.06666 | 2026-06-01 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 87b20611-d66c-3f39-ab53-6138b5ff104b | -10.66246 | -49.72565 | 2026-06-01 04:17:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 72498564-802e-3cff-807e-64397ea53d1c | -10.80792 | -49.39802 | 2026-06-01 04:17:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 849aac29-321b-3816-9f3a-c4a85e1976b0 | -11.61491 | -52.55714 | 2026-06-01 04:17:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 27d1ebdb-86fe-3c02-9907-e17ce64e81d0 | -12.31905 | -47.89912 | 2026-06-01 04:17:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d9880f1b-2f53-31c5-b61b-9b99d3826954 | -7.30025 | -46.99121 | 2026-06-01 04:17:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22ff54ef-5858-3334-aba1-18afd838b7d8 | -7.17168 | -44.07069 | 2026-06-01 04:17:00 | NOAA-20 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d8f2d8ec-7c9c-3c74-b479-fdf5882a81d9 | -10.86356 | -46.93563 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 621ad413-2d2f-30ad-9124-689ceb2738af | -10.74062 | -46.91072 | 2026-06-01 04:17:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26425b1f-1770-3355-bd20-304e63f8d348 | -14.2266 | -47.9819 | 2026-06-01 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc0d5c00-b741-306c-ad93-5e124df4eee2 | -7.95479 | -46.84445 | 2026-06-01 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20b58b51-f32d-3953-8423-3494b52341f4 | -20.94806 | -49.16064 | 2026-06-01 04:19:00 | NOAA-20 | UCHOA | SÃO PAULO | Brasil | 3555604 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 7397650c-4632-3dc3-ad68-fd05e2b05512 | -9.37408 | -50.54616 | 2026-06-01 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 51ecf00f-5079-3c17-aa07-8a252fb8dbd1 | -19.50784 | -46.81038 | 2026-06-01 04:19:00 | NOAA-20 | IBIÁ | MINAS GERAIS | Brasil | 3129509 | 31 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 77623e00-cd24-3026-92eb-2181ad9ba6a5 | -20.18583 | -42.32061 | 2026-06-01 04:19:00 | NOAA-20 | ABRE CAMPO | MINAS GERAIS | Brasil | 3100302 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ee03411e-6283-3c00-a5ee-bd62866cc70f | -7.61222 | -49.4687 | 2026-06-01 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a83ae0b-589e-35e9-9f05-4c366ffdf746 | -20.3082 | -50.54282 | 2026-06-01 04:19:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| d9dddd0c-c1df-37b3-b413-4a48cf7741a3 | -9.70221 | -48.23486 | 2026-06-01 04:19:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 903fbc58-9b32-3fa6-a004-8cc596ccf76c | -14.98765 | -49.5612 | 2026-06-01 04:19:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6b62ec5d-7c30-38a9-941b-5a36620de749 | -9.36958 | -50.54534 | 2026-06-01 04:19:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f3a5cf3c-8b70-326b-be84-213c94f5d652 | -14.98673 | -49.559 | 2026-06-01 04:19:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1e748420-6e3a-39cd-9148-6136473f1267 | -7.95461 | -46.84571 | 2026-06-01 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 922af67f-3a87-34b7-85de-27722c81df0d | -13.98875 | -53.8791 | 2026-06-01 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0758e47-32a1-354c-b40d-db109db48e5c | -20.08658 | -40.4064 | 2026-06-01 04:19:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| cc664e43-1570-307d-93fe-7b6bfbdf9baa | -7.49804 | -55.0047 | 2026-06-01 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8cd262d9-bdc9-34af-ad01-ab0186c44467 | -9.50889 | -47.39127 | 2026-06-01 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 629fb876-1d4c-3cdc-a8bf-17c7ce5e4a9a | -8.73178 | -48.32777 | 2026-06-01 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4a0cf8f2-b8af-3dc5-81c0-3ecc37fb9316 | -13.53381 | -49.90291 | 2026-06-01 04:19:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 7449b1a5-bf67-382f-9bf8-e9fbcf64c129 | -8.14946 | -47.41096 | 2026-06-01 04:19:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c58aab24-9640-36fb-98d0-609585c6e16b | -19.8502 | -48.06833 | 2026-06-01 04:19:00 | NOAA-20 | UBERABA | MINAS GERAIS | Brasil | 3170107 | 31 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 985e7b20-42ca-36be-913b-77a5d5daa476 | -7.60983 | -49.46681 | 2026-06-01 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 74f71986-1d8d-35e5-9d08-83754b4dcbe1 | -15.34967 | -43.66125 | 2026-06-01 04:19:00 | NOAA-20 | JAÍBA | MINAS GERAIS | Brasil | 3135050 | 31 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 8809e60a-bb1c-3d1d-b7c5-01fa2be13af7 | -13.98356 | -53.87814 | 2026-06-01 04:19:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b2ad2f95-5826-3a64-ac02-5cc4b5ae7508 | -20.08587 | -40.40755 | 2026-06-01 04:19:00 | NOAA-20 | SERRA | ESPÍRITO SANTO | Brasil | 3205002 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 884dadf1-f380-3bb0-a020-f4108ec5ea66 | -8.72784 | -48.3271 | 2026-06-01 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 841bb8a6-8fa0-3c60-947d-5101a9924235 | -9.51565 | -40.32691 | 2026-06-01 04:19:00 | NOAA-20 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 15f2435b-d945-3004-95a6-7cb77362cdd6 | -14.98587 | -49.56391 | 2026-06-01 04:19:00 | NOAA-20 | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4bf27ca0-c4fc-3baa-a6c2-b12727198d73 | -21.38774 | -47.01919 | 2026-06-01 04:19:00 | NOAA-20 | MOCOCA | SÃO PAULO | Brasil | 3530508 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3b9b9ab6-4b9d-3d16-a8ad-79184b5039ae | -14.2287 | -47.9912 | 2026-06-01 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d4a426fd-5032-3558-970a-1219ab388b30 | -7.95332 | -46.83095 | 2026-06-01 04:19:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 731ad400-a4cf-314a-9221-1be5d500eddc | -8.73263 | -48.32275 | 2026-06-01 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 452f8854-7c52-39d7-bd61-bb2043a7e962 | -7.50426 | -55.00584 | 2026-06-01 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 662ba7eb-4c64-384a-8617-abc3d23dd104 | -8.73571 | -48.32847 | 2026-06-01 04:19:00 | NOAA-20 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| ba02d414-c646-32ba-ab79-f9aa23be5ad9 | -8.11879 | -49.86266 | 2026-06-01 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 541ee2c7-09ff-3355-84bb-d352c365ab58 | -14.23586 | -47.99252 | 2026-06-01 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c0d7965b-6d89-31c5-aba8-e1985db5bcef | -8.11804 | -49.86696 | 2026-06-01 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 56b2a5dd-5ccd-3912-9ab1-c6f7c93ec39b | -13.53784 | -49.90365 | 2026-06-01 04:19:00 | NOAA-20 | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b605de3d-9a57-3119-9a03-2a8243015562 | -14.23151 | -47.99636 | 2026-06-01 04:19:00 | NOAA-20 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9faf262f-35c4-377b-9e59-0610a37c9cf3 | -7.5005 | -55.00356 | 2026-06-01 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| bc4c8f46-30fa-3f5c-a1af-513eb90610ed | -8.12319 | -49.86343 | 2026-06-01 04:19:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fecd7b55-dc72-3098-94cb-5fa816f56df4 | -7.49962 | -55.0084 | 2026-06-01 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb57f891-5ae4-3eb5-a17d-df08acaf0396 | -15.0018 | -41.95808 | 2026-06-01 04:19:00 | NOAA-20 | CORDEIROS | BAHIA | Brasil | 2909000 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 3fb70bbe-2b5f-3c47-8b98-9bb3590a8f6a | -14.08823 | -58.74721 | 2026-06-01 04:19:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 59de2b5d-d7fb-3f75-81c8-d63b75271676 | -7.50584 | -55.00957 | 2026-06-01 04:19:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32c90f4b-5a85-31bb-969d-42d7995f637e | -20.3339 | -41.95653 | 2026-06-01 04:19:00 | NOAA-20 | MANHUMIRIM | MINAS GERAIS | Brasil | 3139508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 2c0413e4-8f77-3bb0-8c01-cb9c2a14072b | -20.31195 | -50.54364 | 2026-06-01 04:19:00 | NOAA-20 | JALES | SÃO PAULO | Brasil | 3524808 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7a643bb2-744c-38b0-ab54-92338ffe46a4 | -14.30249 | -49.24117 | 2026-06-01 04:19:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9ce17a75-cca4-394d-b74c-b3b59a9b3cf7 | -22.55389 | -47.05643 | 2026-06-01 04:21:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3f9efe7b-bc21-3e37-89ce-8103f29399f4 | -22.55057 | -47.05582 | 2026-06-01 04:21:00 | NOAA-20 | ARTUR NOGUEIRA | SÃO PAULO | Brasil | 3503802 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 823e76b2-d69f-35a2-88f8-3c96d68e8c44 | -22.26358 | -48.23348 | 2026-06-01 04:21:00 | NOAA-20 | BROTAS | SÃO PAULO | Brasil | 3507902 | 35 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 712a92aa-284e-315f-815e-660f4643cda4 | -22.69917 | -43.35996 | 2026-06-01 04:21:00 | NOAA-20 | BELFORD ROXO | RIO DE JANEIRO | Brasil | 3300456 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c3dfd1e1-9953-35cd-ae64-f489266fc43a | -6.99413 | -42.88588 | 2026-06-01 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| cb67934b-ac58-3f6c-ac70-2452a7e564cb | -6.99493 | -42.87964 | 2026-06-01 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 3f68f406-037c-3b42-a7dc-d46af6a905bd | -8.12697 | -49.86578 | 2026-06-01 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 6fc6ef48-d44e-3171-a727-17e2dd3f3db1 | -7.50557 | -55.00558 | 2026-06-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5736a706-d5b8-33c0-936d-c4fdf58ec198 | -7.50836 | -55.00963 | 2026-06-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b52295d9-a139-33d9-8ed0-24dc0c90793e | -8.02705 | -49.58667 | 2026-06-01 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d45aa63-a7c6-39e1-b1c4-41c2349f39df | -8.12263 | -49.86512 | 2026-06-01 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a8d63105-82ba-3192-b653-e61415b4b5d4 | -8.11828 | -49.86448 | 2026-06-01 05:04:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| f3b9450e-fbc2-3aad-99ae-04307a500fe7 | -7.50503 | -55.00909 | 2026-06-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 44037145-59fb-3450-aa55-f17ed54e1494 | -7.50225 | -55.00506 | 2026-06-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b4793812-2f09-3942-b5f0-cd030e5093d3 | -7.50278 | -55.00155 | 2026-06-01 05:04:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 46657110-658c-38e1-93c5-4330c47ed49d | -6.98733 | -42.88508 | 2026-06-01 05:04:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 8afc150f-b34a-302f-b8e2-4d678cb0b3ca | -5.10288 | -46.94696 | 2026-06-01 05:04:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e6e381b2-6040-3abb-8920-49193711754d | -10.56995 | -57.32451 | 2026-06-01 05:06:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1a59b11e-4d4b-3cc6-bad9-79bc5c7c3438 | -13.99243 | -53.87672 | 2026-06-01 05:06:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 08504cff-2d70-32d8-a3ae-2f073242dc63 | -12.31689 | -47.90849 | 2026-06-01 05:06:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0f63489-efeb-3128-bd73-db99acd226db | -11.62964 | -56.86077 | 2026-06-01 05:06:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e3ce06-b53f-30cb-ae14-36a313c6d10e | -10.06516 | -51.66225 | 2026-06-01 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 46aee2cc-f605-3459-bb83-90b1f326317b | -9.3699 | -50.54361 | 2026-06-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 77246190-59f2-3f0d-97dd-ce15e386292d | -9.37413 | -50.54422 | 2026-06-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 99ff1a13-6cbe-370f-825a-3fafd1b57a9e | -11.63595 | -52.56404 | 2026-06-01 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b2c6776-78f3-3b30-918f-d29e026ca6cf | -10.06045 | -51.6668 | 2026-06-01 05:06:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2b5a4474-7281-35b8-9a72-63a3bbc4f1f4 | -9.37836 | -50.54483 | 2026-06-01 05:06:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2cc9ce4-1a7a-3f09-aeb1-65f8d8870143 | -12.06125 | -48.07869 | 2026-06-01 05:06:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c9a48099-7425-32ca-89d8-7f03283820cc | -8.73846 | -48.32545 | 2026-06-01 05:06:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |


[Clique aqui para ver as próximas entradas](README3.md)
