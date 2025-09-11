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

## Dados Diários - Página 100

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 87d221ed-e2b3-3f76-839b-112366ab9090 | -15.81115 | -52.28414 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f9c98937-103a-3164-b7a4-d188a6e3f1f5 | -12.48072 | -53.82598 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd95e177-1482-3833-a0de-096687dedbc3 | -9.68187 | -46.76542 | 2025-09-11 04:46:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1409ee79-09c7-3f7a-a133-0597e059aad4 | -10.56097 | -43.66397 | 2025-09-11 04:46:00 | NOAA-20 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8fb2a08c-4c5d-3d0b-a901-f7fae61090ee | -13.01626 | -48.72454 | 2025-09-11 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6d949423-dfa2-3292-a50f-29d9495386d2 | -10.20554 | -51.69056 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 073245e7-0376-3a41-8305-2bb3f5be0b2c | -9.08941 | -49.85382 | 2025-09-11 04:46:00 | NOAA-20 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d8c23a99-1fc9-3d75-914e-534b02370de6 | -15.24866 | -53.76875 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c9b8527a-229c-3a0f-a250-c8c97a4d7fbe | -9.71214 | -48.33472 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| b86686ba-bd29-3196-9661-1099f26a96bd | -11.46048 | -43.60336 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 746160a7-5dbc-3eaa-a670-bc11ebe33668 | -9.80298 | -47.7659 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a7b600aa-92fa-3dd3-81cf-c21af8f4e60b | -15.28349 | -53.78581 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fc813066-7a5a-3270-a93f-6b0e65a615e0 | -11.47612 | -49.25122 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0422ef6d-0bb8-3b1e-bf93-e88b09c52bdb | -15.15676 | -52.41563 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e214f039-2a08-3eb2-ab7e-a20167829add | -14.4128 | -47.33118 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bd11f70c-95f2-3111-bd3a-20b72795e247 | -10.4827 | -49.37061 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| dcfe5582-158f-349d-81a5-485d6b4a8a83 | -10.32435 | -48.81332 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e6a5d632-f831-361a-adb6-514f8b75e975 | -10.65375 | -48.63191 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6692f8b5-d95e-37d6-8a67-52144568cff7 | -12.40447 | -63.82351 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2a189cb5-7c20-35f5-bcdc-4c9db516c0af | -12.39847 | -63.82205 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 78522139-5fb2-3d37-a51b-65a9c5ce8466 | -11.34429 | -46.49157 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 94e05f35-e7d6-30fb-be8f-026c50dc407b | -11.48439 | -43.6838 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3b660c0e-ebb7-3d36-849d-76bca9337ac9 | -15.98517 | -42.98171 | 2025-09-11 04:46:00 | NOAA-20 | RIACHO DOS MACHADOS | MINAS GERAIS | Brasil | 3154507 | 31 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 08d75461-7511-310b-b1a1-a7584fe5773a | -11.99336 | -47.58684 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 457a1d5a-e021-3656-bbea-7f6173b38d82 | -15.12372 | -50.144 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a35ce4ed-96ff-334f-84ee-531f72749189 | -14.89034 | -55.87307 | 2025-09-11 04:46:00 | NOAA-20 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2dd76919-c677-3e69-a41e-9d9ed4e4bf64 | -9.8993 | -49.91374 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 6577689a-b751-3d95-bebb-1eb7c9af53ef | -10.31836 | -48.80409 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f80d42e7-97ba-3c88-a478-6ab10ac42135 | -11.14477 | -45.28279 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c1f8edaf-bbda-3351-9671-19589f9351bb | -9.45553 | -46.42711 | 2025-09-11 04:46:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 81bb377b-08d5-3129-8980-177c96f5cf1b | -13.13328 | -54.9147 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 366d6a9a-1d27-37fb-bd84-c299e22336db | -15.67068 | -47.03216 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 5d1441b4-8aa5-37cb-a71b-04ff2553ef65 | -11.7835 | -50.57159 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 48f19c57-7f98-3ffd-aae8-4b13781c481d | -11.68373 | -46.89579 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c64f005a-10c7-3b24-99ba-032181defe17 | -12.38619 | -54.17073 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0a09922e-8c3b-39c8-bd5c-dbdd0f521c54 | -11.64322 | -46.91648 | 2025-09-11 04:46:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| cbf75b3c-9362-35bb-bb31-d42ff7712300 | -12.02987 | -47.61286 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f086b935-aed7-39fd-8ed6-52ad982e6a9c | -11.11145 | -51.99802 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9499ad6d-1c7c-3af8-82d9-d02314dd6b85 | -9.90501 | -49.92229 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eae5b78e-4f3c-3fd1-910d-54edff66a706 | -10.54932 | -49.89475 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6430e007-4ea9-3a17-89e3-fd173eb231e3 | -11.46599 | -43.60101 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b5fcaa9-5f71-361f-96ed-58252dce0cdc | -11.48684 | -43.64039 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b42871a3-6963-3358-86f2-63f8ea9e95e1 | -9.72776 | -48.09889 | 2025-09-11 04:46:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61fe14ce-d485-3ac2-9617-90b480b69a8c | -15.13658 | -48.61282 | 2025-09-11 04:46:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 7.8 |
| f85ad49b-acca-38d4-83c3-ead4aebfefed | -13.18357 | -51.76817 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 66af0ad4-5822-324a-aa0c-a1e8a171b9d9 | -11.76807 | -46.4779 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| ba0460bc-74b6-3cb1-a9b6-611941e6bb28 | -12.16588 | -48.49029 | 2025-09-11 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8a10e7b3-10d2-3390-a149-b578c77c4235 | -12.85266 | -52.94872 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 280e02c5-9497-3cbb-b900-d208c276658b | -9.02291 | -49.53344 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| de1f42f9-f090-3635-904e-9c4846c4d49e | -12.92438 | -54.75586 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 5c6a6712-a448-3790-974a-deddb3133a7a | -14.28087 | -49.39771 | 2025-09-11 04:46:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 20ea7838-2b2b-3bd1-ac9f-d9aefe36d469 | -11.48133 | -43.64281 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a7321860-abf2-3700-933b-2f4d40ad1ef1 | -12.21128 | -53.86826 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e2f9d5f-e365-3cbc-82ec-7c4b47dba7e7 | -11.45536 | -43.60274 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 6.1 |
| d3125f6b-3fad-3b22-8178-134f965439bd | -12.60822 | -56.96743 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| f42c9ef4-fc60-3830-ae76-884b6cd6ac38 | -15.12853 | -52.42183 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e97ee7c9-2067-3b0d-8094-b5aa2c99c910 | -9.75631 | -47.84841 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b16d10ad-4c31-387c-b84e-7fcc44432334 | -11.10593 | -51.98993 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9dfaa4e0-633d-3b29-aa64-1766a659be8a | -11.11685 | -48.39885 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 724fe8b8-6731-37dd-9deb-912b24ef56c8 | -11.48094 | -43.64582 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 619fe633-c03c-36fb-a802-018c52e4b229 | -10.0185 | -51.7364 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5100bbe2-ac54-35d1-a2ba-63856be1d866 | -13.04232 | -48.00164 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 806cfb19-d5c6-3eab-a8f9-42e6070327a3 | -8.51764 | -54.76835 | 2025-09-11 04:46:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 9a919331-3590-31e7-aae7-a3c953ee9545 | -10.01905 | -51.73291 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5c1167e5-2389-37aa-b8e1-401a29660725 | -11.14954 | -52.05806 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0958e56-7012-3a27-b397-d5fbeb4ef486 | -12.82725 | -52.93726 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a7f425eb-02bc-3a3e-912c-2821e0c0c3af | -12.16653 | -48.48571 | 2025-09-11 04:46:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7e0be7bc-c820-365e-9afa-d409b9118516 | -11.48756 | -43.6743 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2bd54100-0721-3088-8073-9d97aca3a0eb | -15.79755 | -52.24482 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c3b69ed6-c9d8-3549-b672-ab1c56287436 | -9.72239 | -43.53003 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 696d2621-08eb-3beb-a795-f85d3fa70584 | -15.16285 | -52.42031 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 91fefaab-b2b5-3651-87a4-6b9e505c0f8d | -14.28149 | -54.74358 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 037a11e2-2f46-362d-af33-3a8c82993c8f | -11.11863 | -52.06026 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f15906b0-40a6-34cf-a281-c005e296f341 | -15.12118 | -52.40586 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 82d4dbfe-e61d-3a88-920d-22cb0c8a65f1 | -9.08885 | -49.81197 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 80183344-e58f-3af8-a77f-774560bc6ab8 | -9.31764 | -46.75172 | 2025-09-11 04:46:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c954b976-dca1-3932-b461-066cbdd3b0b4 | -9.91926 | -49.87457 | 2025-09-11 04:46:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8f6df38f-8d92-3e7e-901a-49ad00a08085 | -10.55103 | -49.88335 | 2025-09-11 04:46:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0499fea4-c412-3822-abb4-7e76626373b7 | -15.66585 | -47.03555 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 54fc04cd-2423-3ad6-9437-13edc4f0fd5f | -9.99298 | -51.70343 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49d7a5ef-a209-3415-96d7-ce541e2f9617 | -12.05838 | -50.94832 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3111f720-9a22-3bb7-830e-23afa00dfb66 | -10.19506 | -51.69247 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 556f7abf-9118-3fa2-b736-229b1cc35c94 | -16.06096 | -49.96257 | 2025-09-11 04:46:00 | NOAA-20 | ITABERAÍ | GOIÁS | Brasil | 5210406 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f24d4b85-50c5-308c-b5b4-8fc9f2f2149c | -9.59871 | -50.9222 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a460129-8105-385c-863c-6b64d4ccd0bf | -9.9836 | -51.69835 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f8d7a09b-87a8-324e-9ff0-8be6e4fa7a46 | -13.88432 | -49.14326 | 2025-09-11 04:46:00 | NOAA-20 | MARA ROSA | GOIÁS | Brasil | 5212808 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5d4a965e-2398-31d4-9c8f-674ecb025588 | -11.48518 | -43.69236 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 350c9e56-a99b-3e14-a139-e3670d77d912 | -9.88385 | -51.87912 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 87275809-28cc-395a-badd-2b74ccc99400 | -12.84313 | -47.97134 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a16dd020-cdaf-3109-b5f5-07474dfb9ba4 | -11.45693 | -43.59055 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b98b7c50-cd94-3182-9919-dc95fed07a94 | -11.41595 | -43.54388 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 57db430b-e4dd-3042-abb1-9a6901e272a0 | -14.4459 | -52.94632 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bd1df776-0cba-351e-9140-b3a1a3d94337 | -11.34219 | -46.47544 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| cd44db27-e96b-3575-9096-ba04f62addc6 | -12.41498 | -44.71897 | 2025-09-11 04:46:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 59a432da-bf24-339b-9b24-4f15ed5ba6a1 | -12.21901 | -53.88468 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd327f24-ff16-3c9e-a4a5-eeba38eca195 | -14.56072 | -48.77274 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db00e369-94f3-391b-858c-9f72337f170e | -14.43984 | -52.94167 | 2025-09-11 04:46:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8bdb5dc-a6bd-3b1c-8fe3-026232f27350 | -11.77176 | -46.48244 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6743a81a-c940-3fd4-8cb5-adf644bd0b8d | -11.22157 | -55.00229 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 61f535b3-c700-38cf-85ea-45c11510bb86 | -15.10246 | -50.11518 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README101.md)
