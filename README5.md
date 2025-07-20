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
| bf9b500f-6892-3a75-9103-5d20031da555 | -10.65619 | -46.80775 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 17.5 |
| fb00e36f-e026-36db-80a4-fa1cb95c1e1c | -10.63451 | -48.0942 | 2025-07-20 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c90b086b-5e21-3f3b-891e-1915f784e60d | -10.62853 | -45.23568 | 2025-07-20 03:49:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 87226a89-2bb5-3a08-a02d-4b7055a35527 | -11.81997 | -47.5108 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eeb91363-a9f3-3d5d-a60f-17297dd1a3cc | -10.65731 | -46.8089 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 5977631a-7521-318e-9637-eb7acb040914 | -11.83459 | -47.51245 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 80dc07bd-13fc-31e9-aec6-4c9f962a23ff | -12.34739 | -50.32799 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 91816b9e-ba53-398a-b69e-0eda953fd526 | -11.81344 | -47.51626 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5a820bb1-09b3-3d61-8358-e799ee788082 | -12.98031 | -46.91285 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82c9d066-b3d2-33be-984b-020d908117b3 | -10.66947 | -46.80129 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| c1e552de-4084-3820-8947-843ca50700f7 | -11.81869 | -47.50928 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e31f79c-0245-3cbe-ab56-8824a603b38f | -11.82466 | -47.50694 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8c8a47bb-eb2a-364d-8606-4215da146c63 | -12.35881 | -50.32181 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 213612ac-8a15-34fc-a132-4401d10289d4 | -9.61831 | -49.01722 | 2025-07-20 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| b157f062-1d3a-3306-ab15-13b54e014d44 | -13.54351 | -43.70827 | 2025-07-20 03:49:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d1f06a0d-80ac-3eda-b6d1-25469ed7fa1a | -12.68249 | -44.32888 | 2025-07-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 96fb6133-ce71-3135-a56e-5c5d4f1bc2b1 | -11.95625 | -46.75212 | 2025-07-20 03:49:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c13246bb-13ec-3f47-b71d-31b750b369c1 | -10.68074 | -49.67789 | 2025-07-20 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5959aa0c-a536-31d6-a0c5-8ccfe0e2e2fb | -8.0157 | -43.68546 | 2025-07-20 03:49:00 | NOAA-21 | ELISEU MARTINS | PIAUÍ | Brasil | 2203602 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| e65f4e35-3aa7-3e2f-8702-4029a2892697 | -10.69366 | -46.78653 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f6da37da-af63-3727-ba5c-600cac9d213e | -7.70126 | -47.29149 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef08078b-cc85-357d-be0b-f366737f2dd3 | -11.81404 | -47.51308 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 4409ee21-c20d-32f8-9cbd-45cef0a2b69c | -7.29409 | -39.62759 | 2025-07-20 03:49:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 39d623b3-70ab-3a55-80f5-4d2d21d624d6 | -9.8017 | -48.56364 | 2025-07-20 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9d4c2906-9f72-3422-83b0-d32a5c65f461 | -12.34524 | -50.32434 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| dbd708a2-11ce-3d60-87f2-7908add8b1ec | -10.96771 | -45.10179 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 11.7 |
| cc1a2630-fa1b-30f8-bba3-c6c916947528 | -10.66428 | -46.8004 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| a5ea6e14-ad49-3872-94bd-4da27c38a5b2 | -11.5517 | -47.09222 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8026ad11-8f4d-3ff9-9a63-f2527a6cb315 | -9.63226 | -40.60249 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 71721fc2-b081-3d95-82f0-ec0463894aee | -10.67063 | -46.79513 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 2491993d-1a00-34dc-829f-fb3215dcff1b | -9.6174 | -49.02193 | 2025-07-20 03:49:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 2af9dfd8-e360-3153-b25a-04e5e935ff85 | -10.97603 | -45.1082 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| cec9125e-5975-324b-8666-59000159d78d | -8.25894 | -46.36113 | 2025-07-20 03:49:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4f4f65ed-4c17-3e85-ad31-2bfa16c4e53f | -11.49568 | -48.07792 | 2025-07-20 03:49:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 0bd42c6a-a02f-3ef0-bf00-da00a7237df5 | -7.23143 | -44.12846 | 2025-07-20 03:49:00 | NOAA-21 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a9654bb-6c2b-319a-bacd-9b6e4744f202 | -12.66142 | -47.09942 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 92b4134a-2d21-3670-8965-3b809d803bc9 | -10.97051 | -45.11235 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 20.1 |
| ab1cc019-00af-335f-bfee-50f020062514 | -10.66487 | -46.7973 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 964edc50-cf9f-38c1-94d8-ceff66878101 | -10.69882 | -46.7875 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7df1c01c-9a8f-323c-aade-3e47582e580e | -10.69355 | -46.81556 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c1e6f49b-f0c8-37eb-8814-da4c03583138 | -9.63159 | -40.60659 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 8096404d-6c0d-35a3-bb3b-aec4ae38b3c8 | -8.7469 | -47.73047 | 2025-07-20 03:49:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 88bdccae-a126-3a98-93cf-079d3f240ac7 | -10.54624 | -49.49426 | 2025-07-20 03:49:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 32e76ba3-f818-39d4-b217-c8b550640fe4 | -9.5348 | -40.33446 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 42.5 |
| 09ace91e-b731-3f20-bb40-8e3d344a50eb | -12.68039 | -46.83141 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 13a249d2-5f09-3d48-9f44-76dff749e2c3 | -9.60176 | -43.86 | 2025-07-20 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 63bcf910-afa1-39a7-a8f3-cb2fbf2bc675 | -11.8331 | -47.49943 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 207f3068-0cda-35ab-b581-7a912fa7b83d | -11.83127 | -47.50124 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c22553d6-2826-384e-8784-2831c94c0e2c | -11.83247 | -47.50276 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d95df9cc-e797-31d9-b475-42c832e9b66a | -7.70196 | -47.2876 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 66924857-e8b6-31a0-b62c-e534b5b1c813 | -12.05752 | -41.06309 | 2025-07-20 03:49:00 | NOAA-21 | UTINGA | BAHIA | Brasil | 2932804 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4fe44351-40c6-319d-b898-05a0f0d8e5fd | -11.8365 | -47.51066 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c736cf41-1f8c-3d76-afe5-bf79e2032c19 | -11.28289 | -40.98249 | 2025-07-20 03:49:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bbf2d3e4-4714-35a5-908b-cda455e2cf7c | -9.56068 | -40.65819 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| baeadce3-5dfd-3a5e-b4d1-ce967963acff | -12.65889 | -47.10027 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| adf7274e-4c3d-35b0-8345-b207c6f8bf73 | -9.53832 | -40.33504 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 42.5 |
| 27bdfe8a-a1f2-3440-895e-949c8028212c | -6.36309 | -45.39 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 9599ba2c-2f8a-3d83-8745-9c7be059837d | -10.6321 | -48.09327 | 2025-07-20 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c12e7511-12b7-355b-8b30-340c51233a13 | -10.6579 | -46.80578 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 4c8468c6-0512-3c76-a2fb-253839e998c7 | -11.8206 | -47.50743 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f4b57b6-d632-3a58-bbe0-5e137bc30b02 | -12.35256 | -50.32051 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d8ad4640-9102-3f1b-92ce-35e2c6faa7a5 | -13.71257 | -42.50828 | 2025-07-20 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 606fcd45-c64c-31f4-b2cb-ebc623a80fff | -11.82718 | -47.50169 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a64b4338-3129-3ff8-af09-d3e5a16efe16 | -9.48074 | -40.37569 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 447deeb0-c2e9-38b6-947d-65240eaab42d | -9.63582 | -40.60308 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 9.9 |
| fa181c0b-fb90-3229-bb9c-65a2ae8c41c5 | -11.83525 | -47.50908 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 47b9ae84-033b-365a-8a98-17a9103c75d4 | -10.62886 | -48.09328 | 2025-07-20 03:49:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 369ba16b-1ab9-3ac9-b223-f569bd4193fa | -9.60535 | -43.86497 | 2025-07-20 03:49:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| c9a87332-d182-38bc-bd8a-28337e5a57be | -11.82532 | -47.50354 | 2025-07-20 03:49:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ffd7336d-a32b-3a6c-b4de-739119bad14f | -9.54184 | -40.33562 | 2025-07-20 03:49:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 714e5419-853c-3ccf-a49d-4f57036cbe1b | -6.99379 | -43.31237 | 2025-07-20 03:49:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f0376511-7d80-3a67-9c3a-97cc3d485fe4 | -6.81018 | -43.80605 | 2025-07-20 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 327929d7-793b-3a45-8c62-9430455f662e | -10.69871 | -46.81658 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c33b3f7a-43f4-3bc6-bea3-0765421408c5 | -11.48632 | -47.32405 | 2025-07-20 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9c4c1a1c-1bd0-32d1-b386-baf28e8583aa | -7.6956 | -47.29064 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f039c7a2-dea3-33f7-ac09-f52be2d6b955 | -13.71115 | -42.50915 | 2025-07-20 03:49:00 | NOAA-21 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| e1b24e97-6ee6-3194-9e70-62dd32d43757 | -10.66195 | -46.80548 | 2025-07-20 03:49:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| dc5c1188-3cc4-385a-8acf-af5530e69d00 | -12.97982 | -46.91545 | 2025-07-20 03:49:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bb8c5be2-b473-3bcd-a3e5-81800f332f46 | -8.35882 | -46.6461 | 2025-07-20 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3be60ab-8a27-31be-b306-524a93a5b076 | -9.80402 | -48.56118 | 2025-07-20 03:49:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b7a3cf8-0e28-3bac-884e-e62881f1dfd5 | -7.74837 | -42.16157 | 2025-07-20 03:49:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 8c679fcd-c7d5-3c0a-a6b8-1ccb0a245b28 | -12.71036 | -45.02792 | 2025-07-20 03:49:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83e87078-8a4a-3bca-927a-612ee1afef0e | -6.36357 | -45.3872 | 2025-07-20 03:49:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 06e75f41-8d36-3f1c-9f79-8e023f9d3f87 | -11.56211 | -47.09409 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2dfd2764-94a4-35ef-a2fd-a4e2457da188 | -7.17125 | -44.0942 | 2025-07-20 03:49:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| c32c079b-4c74-3bf7-9330-b3feeefce6ca | -7.70687 | -47.29252 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f8e05f1b-6767-307c-8468-95511b243b4b | -11.48695 | -47.32076 | 2025-07-20 03:49:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b1550273-ad65-3a3c-9af3-8baad58ff265 | -8.35346 | -46.64531 | 2025-07-20 03:49:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 80bc02f4-0298-3be8-8739-47dd1676ebe3 | -7.76092 | -42.16013 | 2025-07-20 03:49:00 | NOAA-21 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 1115e15d-cccc-3f68-83ba-8ed423d54c16 | -12.35648 | -46.43142 | 2025-07-20 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 6457f98c-0773-3259-9599-931cf40b8d59 | -12.38174 | -50.33712 | 2025-07-20 03:49:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c8493d00-3e6f-3ee3-a0e2-f600f1e71d82 | -9.11277 | -48.12026 | 2025-07-20 03:49:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3972ebf7-8425-3ddc-bc8b-792656de9254 | -12.354 | -46.42849 | 2025-07-20 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 13920bc0-1bdc-3c49-aa3d-1f8b69183962 | -12.35758 | -46.42542 | 2025-07-20 03:49:00 | NOAA-21 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| c152eeb5-fe6a-3de2-a4a2-9baf338469cf | -11.8349 | -48.21087 | 2025-07-20 03:49:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a3f45bba-bdb3-3e54-bd0e-2fd6d7d6ba22 | -7.70759 | -47.2886 | 2025-07-20 03:49:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| b949d566-f9e8-3c97-acc9-a890eb0c7ffb | -6.86323 | -47.81895 | 2025-07-20 03:49:00 | NOAA-21 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 19aafa33-6e15-3920-88c9-aeddd886e143 | -12.68672 | -44.32968 | 2025-07-20 03:49:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 67da6d0b-8a1b-35e4-9061-4bd2745f5fbd | -10.68171 | -49.67299 | 2025-07-20 03:49:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| a30771c7-b3b6-3866-8eb9-62d0c38367d2 | -6.8147 | -43.80682 | 2025-07-20 03:49:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README6.md)
