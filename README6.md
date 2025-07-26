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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1469cfa-dad4-31ce-b028-6b9cc59f6adf | -15.14918 | -46.19274 | 2025-07-26 03:38:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d726a795-cd9c-3eeb-b922-2d714c382c31 | -9.13234 | -45.8759 | 2025-07-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| 8d8b8585-ee89-3fa9-ba88-412402198cf1 | -14.95135 | -46.96437 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f3549167-8a8b-325a-a812-b1949a36733b | -11.92702 | -44.55162 | 2025-07-26 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 4ed72ea5-ec63-3831-9f58-3ec897b8319c | -13.70037 | -45.68744 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| bf1701ce-baa5-3298-bd2d-44c72423a5bd | -11.74445 | -48.18629 | 2025-07-26 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 616c3cad-af7f-3e51-b242-ebe90d82b730 | -12.05135 | -45.4422 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8bf16114-2ebe-316f-97a5-83aa63b7e4c1 | -13.7227 | -45.69207 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 139f1beb-b701-3824-9d68-ffee24a30e96 | -13.64452 | -45.70452 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b591653b-5a0f-3445-8226-d7b48c044906 | -13.11588 | -47.34208 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e709c7d9-698f-3235-82b6-d3e460cc62ff | -14.58454 | -43.58366 | 2025-07-26 03:38:00 | NOAA-21 | IUIU | BAHIA | Brasil | 2917334 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d6a149c-3761-3d2e-a2a1-1fc91c5721d2 | -12.41969 | -45.38313 | 2025-07-26 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a69c6565-2b8b-32e6-99b4-2ed29a1230ed | -15.78602 | -41.32932 | 2025-07-26 03:38:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 897e8f2d-81e1-3b28-b594-b60923fa35d6 | -13.23882 | -40.5999 | 2025-07-26 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| ca05a473-84d5-35c1-a2b2-67b1b635f39e | -12.04846 | -45.43888 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5153b2fe-06a4-3af7-a9f6-5b7fb5f53cc3 | -13.10011 | -47.33729 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a847f8cd-564f-3ce8-8598-9f591126c2b8 | -9.13327 | -45.87102 | 2025-07-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| a0d021f4-eff0-3c2f-bfec-8bbd3d16138d | -13.64153 | -45.70239 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc403045-9d43-3aed-b740-a16a79afea54 | -12.41893 | -45.38697 | 2025-07-26 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4f9f14a9-60d4-3149-9e26-4444c0c0ea64 | -13.54452 | -43.56813 | 2025-07-26 03:38:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 94a39522-b0e8-3b01-b6e5-16f629256018 | -12.71052 | -47.79764 | 2025-07-26 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 11ccf2c8-edae-376e-af33-1172f436a7c2 | -12.72727 | -41.80876 | 2025-07-26 03:38:00 | NOAA-21 | BONINAL | BAHIA | Brasil | 2904001 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 709f251a-4036-3795-a79e-a89451e14d05 | -13.69785 | -45.6709 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ddb79ee5-d182-3f81-ad45-f42020e232e7 | -12.29945 | -40.08754 | 2025-07-26 03:38:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 0e9eddf0-c0a5-3d2f-84a1-c3de0d007a3c | -13.11479 | -47.34732 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6d047a2-6470-3c27-817c-cd971e468ade | -9.47483 | -40.37004 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| c3989bdd-ea70-38f6-b676-f1008fe2ac46 | -13.67721 | -44.22628 | 2025-07-26 03:38:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3a489d61-beea-3f78-a77a-9eb57759364e | -12.69085 | -47.003 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b6c7bc1f-1c3b-3aec-ba29-783c57f662b9 | -10.62602 | -44.76537 | 2025-07-26 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| f64f0476-2347-33c5-af89-0ce517201403 | -10.62045 | -44.76433 | 2025-07-26 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 3f24bc49-6cda-3212-94c8-b142039f8b0d | -9.46703 | -40.36456 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d8167e5c-c35c-38c2-b75d-7ced87bc3a2b | -9.13878 | -40.55717 | 2025-07-26 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9ebf355e-9ec6-3997-af55-71dcf88dd6fa | -11.9277 | -44.54814 | 2025-07-26 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c2508426-779c-38c3-8df2-a05790a8dfad | -13.11779 | -47.33292 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9c719bb6-7900-3a30-a799-ef1e6e891d11 | -13.11367 | -47.3527 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| efcbf7f2-6ebd-3ced-9d12-7dd1d27ed155 | -8.28958 | -45.00515 | 2025-07-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 53044206-0c42-3dae-bd13-86ffded38583 | -13.91406 | -41.30478 | 2025-07-26 03:38:00 | NOAA-21 | ITUAÇU | BAHIA | Brasil | 2917201 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6cb65dd1-bb53-32d3-bc5a-7c34761ae81a | -12.71742 | -46.27139 | 2025-07-26 03:38:00 | NOAA-21 | AURORA DO TOCANTINS | TOCANTINS | Brasil | 1702703 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e016270c-6012-365a-aeee-54875813972e | -13.69247 | -45.69786 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| a9c5e47e-f45d-39f8-b64b-c9f21108abbd | -15.05224 | -46.50666 | 2025-07-26 03:38:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f6db7599-d227-38b0-ae26-1c6d3354a887 | -13.17771 | -42.32513 | 2025-07-26 03:38:00 | NOAA-21 | CATURAMA | BAHIA | Brasil | 2907558 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 5ecd848e-2931-3c93-a222-23486387f50c | -9.36272 | -40.31445 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| d23ef85b-3bd4-3a02-af89-7dfc41955e85 | -12.29882 | -40.09106 | 2025-07-26 03:38:00 | NOAA-21 | IPIRÁ | BAHIA | Brasil | 2914000 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 2f55394b-d8f7-312c-bbab-fe14c243fcca | -11.11076 | -45.11987 | 2025-07-26 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 630b6d03-4d83-374a-bd57-8063ed4e8b7d | -14.94254 | -46.94749 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e2dfa09f-fd74-3175-8cc9-aad5f01e6d9d | -10.35 | -46.65128 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8d17aea6-7a09-3355-8416-814390219c59 | -11.74325 | -48.19224 | 2025-07-26 03:38:00 | NOAA-21 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 9.6 |
| bd0d4e80-d86b-3b2e-80f7-4c33a6d5a1c8 | -12.42121 | -45.37547 | 2025-07-26 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ef00a309-cd8f-3acc-813c-ffe8ff83c3c5 | -13.72195 | -45.69587 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 6484f34a-940a-3fbc-91d4-a1a66084b412 | -13.64373 | -45.70845 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 47821451-9524-32af-8022-bbd039a3d772 | -13.23947 | -40.5962 | 2025-07-26 03:38:00 | NOAA-21 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Caatinga | 13.9 |
| 6f568223-a33a-3bab-b188-d5fd5d2e7d1f | -12.04202 | -45.44164 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b5183d7a-1795-3b44-9cb1-fb511b67a9ef | -9.50384 | -40.3793 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4b77c338-3561-3cf6-9bd3-e6802b248946 | -10.35635 | -46.65217 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9c04bb00-77f5-3668-a419-46d7055f2b79 | -8.29545 | -45.00631 | 2025-07-26 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4de2a11e-677f-301d-9e81-86066848595f | -9.47413 | -40.37404 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 18.8 |
| fd51642a-aa0f-3984-a720-2646f5db020d | -13.12632 | -47.32319 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 3aec8a4e-9cf0-31f7-acd2-6de28a80d945 | -15.87494 | -43.28699 | 2025-07-26 03:38:00 | NOAA-21 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 86111578-1b7b-333d-8513-fb066fd1f4eb | -13.09351 | -47.33778 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ae33cbc8-2e5f-36f6-8e22-83799f605279 | -9.91332 | -47.76357 | 2025-07-26 03:38:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e923f7ca-98fc-365e-a96c-02dc8cf5e80d | -10.62674 | -44.76157 | 2025-07-26 03:38:00 | NOAA-21 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 0df8a26a-37bf-3406-a566-bf11934c498e | -11.92165 | -44.55059 | 2025-07-26 03:38:00 | NOAA-21 | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8cb0c477-72d8-3ece-84bc-885b33b9f167 | -14.22007 | -43.95889 | 2025-07-26 03:38:00 | NOAA-21 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| de59f727-9e80-3f37-a847-13c5dbc9100f | -12.68566 | -46.99694 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 958b8d9e-9c45-3037-a284-b55bca4c01ca | -13.63969 | -45.69962 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| cd108d6c-9642-30ae-98b5-98632a628902 | -11.45886 | -45.19493 | 2025-07-26 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8844072c-fd4f-3d7a-abbe-ebc2379b9398 | -13.69709 | -45.67474 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 4e9606dc-ef9a-34a8-84e9-c08d644a5289 | -15.78941 | -41.33376 | 2025-07-26 03:38:00 | NOAA-21 | PEDRA AZUL | MINAS GERAIS | Brasil | 3148707 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 294aa475-f032-32a1-9860-d524ae451ace | -12.70674 | -40.90148 | 2025-07-26 03:38:00 | NOAA-21 | IBIQUERA | BAHIA | Brasil | 2912608 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 0ba22665-d3ae-3ca7-bef6-9d262002ed5b | -14.94697 | -46.9558 | 2025-07-26 03:38:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 8739c374-33c7-3cfe-a9d8-d64df389837f | -9.35848 | -40.31372 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 28.2 |
| c0bdf9e7-1ccf-35a1-9d30-1eeaf391db48 | -9.49957 | -43.17113 | 2025-07-26 03:38:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 06c6ad3b-d788-3d89-b805-38a7daa60544 | -9.76539 | -35.84565 | 2025-07-26 03:38:00 | NOAA-21 | MARECHAL DEODORO | ALAGOAS | Brasil | 2704708 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| d7ccd851-9b84-3c7b-9242-12ba6b17a1d7 | -13.12551 | -47.32708 | 2025-07-26 03:38:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 514b12b6-9522-33cb-9c7d-0c1da54ff36d | -13.69632 | -45.67859 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| efc4d8ff-5101-3937-af68-d2f6949c627b | -9.47058 | -40.3693 | 2025-07-26 03:38:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 55225df1-32c8-320d-a2a4-a689aee6a25f | -9.13445 | -40.55642 | 2025-07-26 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 62a2105a-a1ae-3058-af3c-84987b44c8a0 | -13.70191 | -45.67971 | 2025-07-26 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2d24b4b0-7f0e-3aee-9c8b-ec59c9f2d93a | -8.87039 | -45.5858 | 2025-07-26 03:38:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f78781a3-667b-3cce-9200-cc1adc45718c | -12.0457 | -45.44103 | 2025-07-26 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60908657-9bc2-3c0c-8ce5-fa61ce14956c | -10.35115 | -46.64549 | 2025-07-26 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| d446233e-4f6f-378c-b65d-69255e935998 | -11.94709 | -43.83074 | 2025-07-26 03:38:00 | NOAA-21 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| df4a5b78-80aa-31f2-b193-6bb5a4ec4ffc | -9.50014 | -43.16803 | 2025-07-26 03:38:00 | NOAA-21 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 1c9b0a44-2c15-3741-b96a-182c2fcdb534 | -14.9528 | -46.9388 | 2025-07-26 03:40:00 | GOES-19 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 99842781-191e-39f7-bada-f1e29e21ce74 | -7.2408 | -43.0664 | 2025-07-26 03:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.0 |
| 87955217-5a58-3364-80eb-174f2c3ce055 | -9.363 | -40.3031 | 2025-07-26 03:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 61.2 |
| a521307c-caf3-35f8-9bf2-f16bf0838187 | -16.12275 | -47.40414 | 2025-07-26 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0d47fe13-9249-3e54-980d-c8b4f85bd014 | -18.65995 | -43.96149 | 2025-07-26 03:40:00 | NOAA-21 | SANTANA DE PIRAPAMA | MINAS GERAIS | Brasil | 3158508 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 096f1103-4dfd-36ec-9bd6-44602466d59e | -19.97133 | -48.42933 | 2025-07-26 03:40:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 8858eb99-f5c4-37b9-b0da-f8b5d17b0cf4 | -18.24605 | -44.78572 | 2025-07-26 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 53fc09e9-77d6-373a-ae08-e52482313a2e | -16.66333 | -43.7672 | 2025-07-26 03:40:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9aadcf3-b626-32cb-a201-0faaf287d6c3 | -18.252 | -44.7812 | 2025-07-26 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| babdea8f-0434-3577-9527-065bba546122 | -18.25943 | -44.7844 | 2025-07-26 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3146fea9-5da7-395c-87e7-d73c9575db11 | -16.69308 | -41.01549 | 2025-07-26 03:40:00 | NOAA-21 | JOAÍMA | MINAS GERAIS | Brasil | 3136009 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 06f74b64-4dc4-31e2-b4a8-aea5102690c0 | -18.91833 | -40.09796 | 2025-07-26 03:40:00 | NOAA-21 | JAGUARÉ | ESPÍRITO SANTO | Brasil | 3203056 | 32 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 2a98e4cf-fa42-312b-9d66-63f8cca4ba74 | -17.86905 | -39.66511 | 2025-07-26 03:40:00 | NOAA-21 | NOVA VIÇOSA | BAHIA | Brasil | 2923001 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 57a90b6f-951a-3d9f-915d-ab060d3b175d | -18.25686 | -44.78218 | 2025-07-26 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 82922989-1fdd-304a-8144-a968c409c10a | -21.38779 | -48.67545 | 2025-07-26 03:40:00 | NOAA-21 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 97abff7a-714a-3f37-8b3d-e43106ccf830 | -18.25089 | -44.78679 | 2025-07-26 03:40:00 | NOAA-21 | CORINTO | MINAS GERAIS | Brasil | 3119104 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7c1eabe7-d7cc-3fff-a107-ecf17d55c21e | -16.12175 | -47.40874 | 2025-07-26 03:40:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |


[Clique aqui para ver as próximas entradas](README7.md)
