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

## Dados Diários - Página 29

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b426723f-760a-341d-9cb0-9074ff433d28 | -8.79046 | -44.27641 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 0f1c4c04-fbe5-33e4-8c88-77334b0349cc | -7.55533 | -42.65732 | 2026-09-22 03:42:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d11ec74d-1d10-381c-aaf7-cd424defba49 | -6.57 | -44.16035 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 069c5978-acbd-3a17-a7ff-2bb72b9a5be0 | -9.62171 | -43.94353 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 80e8f9d9-ec5e-368e-ab20-455de8ac9f5d | -5.82741 | -43.85051 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e569b713-c784-364b-af27-4ebd5a3b581c | -9.62346 | -43.93459 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| f442e320-346b-3285-b3fe-7f09a5c9b7b1 | -5.32005 | -43.42073 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 53763a71-97b3-3ded-a75e-0c0404e03de0 | -6.58477 | -44.15232 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7905ad79-45c4-39ed-8520-915c1bce38d5 | -9.62259 | -43.93902 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 75d929d8-fd71-368d-b27e-237a342e4fdd | -5.78682 | -43.77502 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4b325bc2-14cb-3703-a3f2-6cdee4a70094 | -7.45413 | -44.73994 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e7ce9ef6-e320-3f6b-b4e0-3388c682f6e9 | -8.78858 | -44.28637 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| eb802b02-cd43-371a-a6aa-bf2408a183f2 | -5.31718 | -43.42197 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| eecc105f-b109-3d52-9590-989139125e9f | -7.135 | -42.08145 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4231dba-70c2-38fa-b247-015435274ec4 | -5.31915 | -43.42566 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a0b8f14c-085c-372c-b264-c17d1b8543a4 | -5.42542 | -36.75901 | 2026-09-22 03:42:00 | NPP-375D | AFONSO BEZERRA | RIO GRANDE DO NORTE | Brasil | 2400307 | 24 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 2c96a3cc-a006-325a-8059-fe3f51d3caf7 | -8.32001 | -44.74903 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 2b3b3ec4-2d8c-3c84-9130-fdd64a67a256 | -9.53476 | -45.39119 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d448e676-c5ed-3d8b-961f-9347f6055bf0 | -5.31372 | -39.1096 | 2026-09-22 03:42:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 456cda2e-aae2-34b8-9872-96c6754b2d65 | -8.48235 | -44.74052 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 960e6f08-9609-3175-b1b3-b6a7ceb17b69 | -7.45197 | -44.75126 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d1acb3fa-2e25-38ae-8778-2d85d66517fd | -6.97833 | -42.58455 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| de9c9075-4afc-3853-90a3-856a64ae8a90 | -9.61568 | -43.9423 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| de4611db-4ea3-321c-85c9-21a69b16797e | -8.78808 | -44.30377 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e50051a4-dcda-3728-9c84-5ab21569f37d | -6.70987 | -43.98589 | 2026-09-22 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4a15c367-2096-3e93-a6ed-874d4f61c12b | -5.32432 | -43.41825 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dc3fd638-1a60-32fc-8f3c-950783cb5c65 | -6.57843 | -44.15294 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 51c65dbe-f279-328d-a1dd-cead59322b6f | -5.62594 | -43.37306 | 2026-09-22 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| f04765cd-e1f0-3fc8-8b1b-3131bee2c715 | -12.02558 | -47.8082 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 51039e31-1451-3474-a358-f9fe43649a15 | -11.66434 | -43.45968 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 745b19d0-0e1e-3b61-83ff-e020493a612c | -11.85646 | -46.81414 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| ba3f8065-2454-3ce3-949c-9237625667cd | -14.63754 | -45.66989 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 714e1bd0-d5a3-3839-a7cb-e4c54261e0cc | -15.36199 | -48.11036 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 3fd8cf3f-fb78-3385-aacf-8de8475228ad | -12.84021 | -44.34249 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 0b0c4cd0-f5d2-3ccf-bd95-508c79a22d68 | -15.98844 | -43.2762 | 2026-09-22 03:45:00 | NPP-375D | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a3e4b1de-f092-39ba-9404-9faf894f2d36 | -11.38309 | -44.22797 | 2026-09-22 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d2ae43d-da91-3c87-af0c-3a18379934e4 | -14.67257 | -45.68046 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| c33fd6a3-1287-3239-8801-0ee8f64cba10 | -14.63653 | -45.67471 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b46bf0e0-c797-38ac-976e-534898f0b9d1 | -10.01444 | -45.20413 | 2026-09-22 03:45:00 | NPP-375D | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c6ff4d0e-1f08-3839-8a73-c32af758165f | -17.3568 | -41.19748 | 2026-09-22 03:45:00 | NPP-375D | NOVO ORIENTE DE MINAS | MINAS GERAIS | Brasil | 3145356 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 41bfeb9d-1709-3e7d-840c-b764520462f2 | -14.66856 | -45.66917 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 590be3e6-33e2-39b2-8c48-3b114c74aa8c | -11.42993 | -47.34927 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 34de383c-3ec1-3180-892e-0ae92450a132 | -11.39647 | -46.79666 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 877773b3-0ec0-3457-ad85-ffbf7fc1b263 | -11.43823 | -47.34527 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| a955dc00-bb4b-352b-90c3-ef2024eae50b | -11.43954 | -47.33908 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.2 |
| c7da6e63-80fa-32b7-84ae-7dc620a3a4bf | -11.8784 | -46.84664 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 84cccffb-bcdd-3ac5-a76b-8aa2316c1c79 | -14.76684 | -48.45325 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e3f17a88-cc05-321b-8ecf-f4aa4036bde8 | -12.14487 | -47.3973 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c42157d0-7d38-3a22-be71-ace9dd9bf526 | -15.35675 | -48.10142 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0ef704ee-ff58-3b02-b127-c3176a83acaf | -11.42168 | -47.35301 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| f3dbc5c4-3fb6-33bb-adf6-7ccb3cfa65d6 | -11.68053 | -43.46708 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3d7e73a0-f185-3462-9057-8cfc382c12c7 | -15.62298 | -48.32509 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4fc2e277-8ce5-3cbd-8cf1-3694f2ea85f9 | -13.18377 | -43.40707 | 2026-09-22 03:45:00 | NPP-375D | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 888b92ff-d33e-343e-8886-9b125478b285 | -11.14589 | -42.83652 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| bdae8747-58b0-3d68-b1e5-e1f04e6b2520 | -12.56425 | -45.96085 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 11.5 |
| ff5c5279-3374-3088-a1d9-6817ad2b0e10 | -16.67477 | -41.85246 | 2026-09-22 03:45:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| c8ccde12-31f7-3840-aa5a-f9b0f8d07c0b | -14.76894 | -48.44384 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 48e80889-06e2-35f0-889a-dbbf6d676e76 | -12.84501 | -44.33656 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 63cf1127-448d-3045-8f86-df993d3deb85 | -15.98418 | -43.00043 | 2026-09-22 03:45:00 | NPP-375D | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b291e80f-d748-36ca-803a-46639df0795b | -17.87168 | -44.4058 | 2026-09-22 03:45:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 09b33fe3-70d4-3cbb-8778-694ce479f3bc | -12.14782 | -47.40203 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 873b094a-4917-3561-ba08-a770614b0c3a | -11.87703 | -46.85317 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 17b7a101-c3d4-3f60-aa8a-de09d50f3b22 | -11.14267 | -42.79453 | 2026-09-22 03:45:00 | NPP-375D | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| a29d4b85-0fca-37e3-b0d6-17806760c2b2 | -12.84324 | -44.34513 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 17.1 |
| 3b91c880-7057-38a0-bc8e-3931f984a108 | -12.01834 | -47.80664 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| cf12d756-d74d-3a1e-a224-07afbcd884bf | -15.35732 | -48.10839 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6ae04482-251a-3655-b7e1-a54e8da6ac6a | -14.76185 | -48.44197 | 2026-09-22 03:45:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d97d5cd2-609d-3184-baa3-80bd0934ecbc | -15.75503 | -43.30471 | 2026-09-22 03:45:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fa6d5551-878f-30a9-b304-aefcc2afc694 | -12.15086 | -47.38749 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f4fb6080-4d0c-3e6f-9ee2-9868e47bdde3 | -11.44802 | -47.33421 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.3 |
| b94563f0-8392-350d-b5a8-2814aa7c8568 | -15.44489 | -48.43882 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 4c6ac72d-ab10-3806-a739-00161d260199 | -12.0182 | -47.8037 | 2026-09-22 03:45:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 6e5ae162-54bf-360e-8687-4949a8b5575f | -11.39818 | -46.79615 | 2026-09-22 03:45:00 | NPP-375D | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b1a4af3-0f3a-3160-a73e-2358de2d5e00 | -14.63586 | -45.6719 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b102798b-408d-3185-b362-a225e0b695d9 | -12.14644 | -47.39002 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0dca4a83-2fa8-3745-bb9b-a7a5e6a4fab2 | -11.42059 | -47.35811 | 2026-09-22 03:45:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 29cfaa83-fc71-37fd-bb59-a1e582442afe | -15.44554 | -48.46835 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6f3d8bb9-babd-389b-bf21-5be4a50e58ed | -12.10555 | -45.65485 | 2026-09-22 03:45:00 | NPP-375D | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3ddd945f-7745-3692-ba1d-08f225734c00 | -15.35884 | -48.10165 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c536ccac-eafb-3dc5-923c-d50a15197356 | -11.38483 | -44.22768 | 2026-09-22 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b0b56f3d-1d39-3bd1-bcf3-ffd2cb14f439 | -11.87972 | -46.84031 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 926531a7-b6f5-3f10-8ca7-2afdd5cb5ee2 | -11.87153 | -46.84504 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| eb8668a1-faf5-3801-a921-2af149a03255 | -12.60126 | -45.09047 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d598520f-cd5b-348f-810c-80d0ce5eb755 | -11.93301 | -46.51789 | 2026-09-22 03:45:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 790aca09-3601-38f6-8fa5-f257cbf0cf85 | -15.2399 | -42.77591 | 2026-09-22 03:45:00 | NPP-375D | SANTO ANTÔNIO DO RETIRO | MINAS GERAIS | Brasil | 3160454 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8308e323-9bd0-3296-b0da-bee9a7cec451 | -12.84605 | -44.34373 | 2026-09-22 03:45:00 | NPP-375D | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 21.0 |
| 8da6ba5d-71b0-3522-975e-114ff5222ab5 | -12.56195 | -45.9718 | 2026-09-22 03:45:00 | NPP-375D | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 37.1 |
| 77fa933f-5fe8-3026-9c7f-193de60deaed | -11.38394 | -44.23212 | 2026-09-22 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 25bbcae4-ce2a-346c-bfe7-d3794fc7dfe4 | -15.74984 | -43.30359 | 2026-09-22 03:45:00 | NPP-375D | NOVA PORTEIRINHA | MINAS GERAIS | Brasil | 3145059 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 965b244e-a027-3150-b8f6-d0b5b6b82c02 | -13.63185 | -42.48073 | 2026-09-22 03:45:00 | NPP-375D | TANQUE NOVO | BAHIA | Brasil | 2931053 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 34873698-8b9b-3e57-a2ff-10b381824140 | -16.67579 | -41.84719 | 2026-09-22 03:45:00 | NPP-375D | ITINGA | MINAS GERAIS | Brasil | 3134004 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 887e3da8-667b-3b78-a569-82dc3c9f9a83 | -11.67565 | -43.462 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 97ec9c2e-d947-3391-8fd7-a02b09adccc0 | -15.36411 | -48.11073 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 928c15d4-813f-3a94-8144-3b80906e7f86 | -11.8482 | -46.81921 | 2026-09-22 03:45:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| dc568a83-ac19-39c9-ab24-ea586d1e81ef | -15.4431 | -48.43422 | 2026-09-22 03:45:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6235f5fa-a351-36cd-a5f1-2cbca2107a03 | -11.68284 | -43.45535 | 2026-09-22 03:45:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cbe60244-e7bb-37e1-b960-22be534980df | -12.1438 | -47.38594 | 2026-09-22 03:45:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3fd69231-ff92-3fbc-8388-ae4da0598980 | -11.38222 | -44.23241 | 2026-09-22 03:45:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4c502c5-de9e-36d1-ab56-75891e33edad | -11.1445 | -42.84372 | 2026-09-22 03:45:00 | NPP-375D | XIQUE-XIQUE | BAHIA | Brasil | 2933604 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 8458694e-a4b1-32b5-bd70-70475841bd10 | -14.63483 | -45.67671 | 2026-09-22 03:45:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |


[Clique aqui para ver as próximas entradas](README30.md)
