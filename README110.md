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

## Dados Diários - Página 110

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 19d17f1a-b094-3818-9060-5a23eb5d5c27 | -12.14056 | -44.84774 | 2025-09-11 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6444f7b8-0205-33ba-bb01-d49d765bde23 | -14.51667 | -53.92756 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4076f67-3839-3f8b-8893-aefd77440cab | -11.47639 | -49.26707 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cca19b98-a459-3cdd-9063-283d9424184d | -12.47942 | -47.48911 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 9cd84f68-4c27-3899-99e9-503d5da0637e | -11.76795 | -46.47895 | 2025-09-11 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0eb377db-f49c-3c48-95ac-9c0c7c2c4a14 | -15.14458 | -52.45031 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| dc3a492b-4d78-3bb5-b9b7-899bde02f0ac | -14.1344 | -45.3991 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 16500bd3-63cf-382a-b555-3ad0000cc42d | -11.15395 | -52.03003 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 40fbffb0-5e68-35e5-8644-f2b61eac5777 | -15.66902 | -47.03075 | 2025-09-11 04:46:00 | NOAA-20 | CABECEIRAS | GOIÁS | Brasil | 5204003 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 79e1cf26-cf6b-3fa4-a45d-9f362c23b89e | -11.48054 | -43.64884 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 25f5ffa6-eb4e-3cc3-a9cb-c54c2b79e2af | -11.45261 | -43.5837 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a1454576-bac8-3c08-93a8-613d591ddcaf | -15.15732 | -52.41203 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 90d7b7c0-1d87-37d4-81f2-823f1540ad63 | -11.35424 | -46.5126 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 6be4d4cf-b69e-3ae2-b302-9f59ad779b3b | -11.59927 | -52.22042 | 2025-09-11 04:46:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fad1566d-425e-3de9-8e08-f6f330998623 | -15.70233 | -43.85233 | 2025-09-11 04:46:00 | NOAA-20 | VARZELÂNDIA | MINAS GERAIS | Brasil | 3170909 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1e6f0b1e-531c-30ea-b8c6-43d8ec08a2b4 | -13.58628 | -47.67923 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 26a70161-dc0b-33df-a69c-777cc126067b | -9.79509 | -51.10084 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad053e5f-7822-3ec7-a209-601bcf29e760 | -12.85929 | -52.94982 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 57a02411-14de-35a7-bc49-bd5a0b19e1d5 | -9.91014 | -49.91158 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6b7d52f4-bfec-3fa2-a86b-da934ec098c5 | -11.13519 | -52.06293 | 2025-09-11 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| de28cf03-fde2-3d48-9c5a-fd85b66604df | -14.13035 | -45.3934 | 2025-09-11 04:46:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e5bb0db5-7177-3896-a071-45791c9a43b5 | -10.57161 | -52.04004 | 2025-09-11 04:46:00 | NOAA-20 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| faa8368f-af75-3b4e-83c4-bb42d7cbe028 | -9.99574 | -51.70745 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5fa697d4-b831-3f9f-80d9-d08f91b287b4 | -14.31098 | -54.75633 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3918babf-c2a9-3248-ab5b-33420bf429dc | -11.35785 | -46.51742 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4ccc46f9-d5ce-3b0f-92aa-558734d213ba | -11.49115 | -43.64705 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 96749da5-e16c-3210-a067-1b7ee9997386 | -14.56964 | -48.76452 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 995eff20-3172-3816-ae91-385d74bb2460 | -13.58389 | -47.69668 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 579ec101-fce1-3564-a0ca-d8ae8349b940 | -13.28156 | -54.25131 | 2025-09-11 04:46:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 66034555-8795-3ea8-a8bb-0e98d38a0b3a | -9.84259 | -47.78592 | 2025-09-11 04:46:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 62a51d45-2807-318a-bae5-ba8dfe52fbb7 | -12.84765 | -52.95878 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8b64037f-cfd6-3852-bf5e-d8677a8896cf | -12.59081 | -44.79361 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 815644eb-d942-3747-9e03-a4c4c95237e2 | -13.24744 | -51.77477 | 2025-09-11 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ae4a95ee-d90e-3e7b-98c8-daa37eb2030e | -11.16261 | -57.18187 | 2025-09-11 04:46:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f26abf2-f8e8-3649-934a-1b017c6e1402 | -13.59077 | -47.67629 | 2025-09-11 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fdcef14f-6502-3ecd-bece-f9a64cd1c2bb | -14.41332 | -47.32731 | 2025-09-11 04:46:00 | NOAA-20 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c513d86d-0bfb-3f16-bd32-02e4d086e5a2 | -15.09939 | -50.06082 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0e740f1f-6377-3b35-a4ad-5ac20b8cf699 | -15.11609 | -50.12157 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2f966faa-b969-39be-9a0c-5c70b3e68332 | -11.363 | -46.54216 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 35.1 |
| 1a8c5522-9caf-319b-a631-4ab083c59356 | -11.13587 | -48.34644 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 09db651b-223f-33b8-a99c-d261aa91ecf6 | -9.7116 | -43.53443 | 2025-09-11 04:46:00 | NOAA-20 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 30d9c85f-36fc-3cc3-8ee8-0d5837ce5494 | -9.79741 | -61.52518 | 2025-09-11 04:46:00 | NOAA-20 | JI-PARANÁ | RONDÔNIA | Brasil | 1100122 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d0d27b71-799d-3908-b0c0-f0fe32e97b7f | -12.40036 | -63.81264 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b7cbb7-c5a4-322a-88ea-2998337c3683 | -11.48852 | -43.65049 | 2025-09-11 04:46:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 348f324c-a640-3405-8dce-1b1cd7f211e1 | -12.59149 | -44.78835 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c18d1aa0-0d4c-358c-bb5e-61805e0c8c08 | -12.42607 | -47.80705 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 28427675-c995-3b74-bfcb-b8d8fecf544a | -15.80503 | -52.27942 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cd937c30-b69d-3c6d-b0b5-c5ed2e437298 | -9.9164 | -49.87028 | 2025-09-11 04:46:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6c89d5f7-e440-3c62-9174-55f5217d27b8 | -15.13683 | -52.43429 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b24d0934-f5c0-3a6f-ba5c-2647e7cc1e6a | -12.9602 | -54.75415 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 937a9a72-9813-3af4-b92b-c35a9f77e7ba | -11.47907 | -49.25586 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b3acf743-7511-3833-9f4e-8acfe928a2c8 | -9.99022 | -51.69941 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b32b45f-3e6e-3cbe-bc56-7d5096da8c0d | -9.98356 | -49.0628 | 2025-09-11 04:46:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| f548eee7-9356-35f2-875f-132330cefc75 | -11.74397 | -48.12251 | 2025-09-11 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| bfb23d68-5793-3b89-9ea4-c55f1eee0880 | -12.86878 | -62.12569 | 2025-09-11 04:46:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e492dd83-7252-3de9-9b43-2f4ff2fa092e | -9.33684 | -48.94243 | 2025-09-11 04:46:00 | NOAA-20 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6d4be2db-db66-33df-a0d9-2589c2092f50 | -11.10443 | -48.40605 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0ea41d9b-b12e-3663-bd06-e5fef0c74bd1 | -11.09872 | -48.44554 | 2025-09-11 04:46:00 | NOAA-20 | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| fdca5f3f-01b1-334c-8420-18135df77113 | -11.91154 | -50.6934 | 2025-09-11 04:46:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0feec164-3856-3f4a-8688-8e5dc398bc30 | -10.5623 | -49.44176 | 2025-09-11 04:46:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7cff4b87-5d66-3667-acd7-189712ed80b3 | -12.83001 | -52.94134 | 2025-09-11 04:46:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc49f330-90b0-3c80-a610-b76da815b558 | -15.15455 | -52.45197 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 360923df-ac8c-3b2d-9c3c-e779c2f11313 | -15.14513 | -52.40263 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6bb23c45-ea6b-3b44-9d4a-5280ae654bf4 | -8.87559 | -49.55782 | 2025-09-11 04:46:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 339b6d5e-8e5d-3fe4-b79d-6337216a522d | -15.16064 | -52.41258 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 52dbf78c-df61-34c4-a617-e767f121b1c1 | -15.66336 | -53.89418 | 2025-09-11 04:46:00 | NOAA-20 | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 484d2d0d-2527-366a-b9f0-2323b10edc1e | -12.00519 | -50.40174 | 2025-09-11 04:46:00 | NOAA-20 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7806002d-9f47-3d72-9c99-f91223916e54 | -12.01556 | -47.6005 | 2025-09-11 04:46:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b14856bd-93e0-32e3-8930-838b43b16b2f | -10.54817 | -51.5196 | 2025-09-11 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 665b3ca6-2fc3-3158-b99d-cb79f10b3b70 | -12.60133 | -56.96112 | 2025-09-11 04:46:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d733b50-adde-3077-8d70-2e2efc1555c1 | -12.98089 | -46.74329 | 2025-09-11 04:46:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88d6b22b-08d5-3c45-938c-1deba7c40cfe | -14.77658 | -48.23135 | 2025-09-11 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62d1773f-4890-308f-bb6d-6d6340217d2b | -9.09538 | -50.42853 | 2025-09-11 04:46:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34f96a0d-2465-39b5-9ffe-9774c72db8b2 | -9.88113 | -51.87511 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3e752a5f-7642-3851-8b6c-36d2e3dbd0c2 | -9.97643 | -51.70079 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f82ee7ba-1a9b-382d-94a9-de9fc6b63f0d | -15.11078 | -50.08296 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ded3260a-2c61-3280-ab50-6f1f276a5066 | -14.27721 | -49.39714 | 2025-09-11 04:46:00 | NOAA-20 | NOVA IGUAÇU DE GOIÁS | GOIÁS | Brasil | 5214879 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 8acbe123-beb3-32e6-8d73-d51317828121 | -10.3965 | -48.57953 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2f99734-2d95-3621-98a5-441cc7a91be5 | -12.39942 | -63.81733 | 2025-09-11 04:46:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 037a8a14-d2c6-39ed-8b48-b0e5d474d476 | -12.97447 | -48.03247 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 15b39425-963b-3e15-9322-657f1429460b | -9.88992 | -51.88367 | 2025-09-11 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bd5bf527-b70f-31f0-a200-9ffc38a22623 | -12.4339 | -47.80816 | 2025-09-11 04:46:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 1825df7c-cba0-3882-82eb-9f12b7a13174 | -11.8635 | -46.7592 | 2025-09-11 04:46:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 20ae3909-5491-3e92-b0ea-33d8c8719e6b | -15.13461 | -52.44864 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| ba150b22-a998-3321-95bf-ced2fda14f69 | -11.43734 | -49.29127 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9053c73c-af29-3eed-b62b-15c2b909960f | -10.65314 | -48.63607 | 2025-09-11 04:46:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 824dc3ed-742c-3988-af0d-24c62114dfd6 | -9.98417 | -49.05875 | 2025-09-11 04:46:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b4cd4fed-4657-3a57-88c8-891639ead294 | -13.13675 | -54.91531 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 92e8e203-0747-355b-98e1-e0b8799f0f6e | -10.31117 | -48.80294 | 2025-09-11 04:46:00 | NOAA-20 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| d22d3ed7-85f9-3e6e-ab76-418f04a7fd7a | -11.22581 | -54.99886 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| da84b4bd-f0d9-314c-aee5-977f133e07ca | -12.53408 | -45.3352 | 2025-09-11 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 28c4737e-8901-3625-9669-18879dca71bd | -15.11793 | -50.08392 | 2025-09-11 04:46:00 | NOAA-20 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 029aadfc-effd-374e-9501-0f5e40a34eb1 | -12.93819 | -54.75827 | 2025-09-11 04:46:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d81eab5-726e-3ed6-801d-8b50c5b690fd | -11.47578 | -49.24608 | 2025-09-11 04:46:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b36fc5aa-73bb-396d-a9bb-5775ac1d85d8 | -13.67204 | -44.22525 | 2025-09-11 04:46:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbf841f4-3fc2-3b1d-86ba-7bc37482ce6d | -15.16451 | -52.43163 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a1da85a5-2c27-384d-9764-15e82a56ce95 | -15.79254 | -52.25515 | 2025-09-11 04:46:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 02566131-3e8f-315a-8f3e-102ce8b60990 | -11.79023 | -47.32251 | 2025-09-11 04:46:00 | NOAA-20 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d40fd5c9-7df4-3ebd-b829-fb08ec8d1a9b | -16.2627 | -46.78505 | 2025-09-11 04:46:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 1131df2e-e8fd-38e9-aeb5-5f2bcc565e6a | -11.22267 | -54.99983 | 2025-09-11 04:46:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README111.md)
