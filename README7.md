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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2a9c71d2-1683-31a6-92da-3952a59eff72 | -7.24924 | -43.08707 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| a99da21e-9690-3c51-84fd-8641be928799 | -6.67097 | -42.47459 | 2025-06-19 03:30:00 | NOAA-21 | CAJAZEIRAS DO PIAUÍ | PIAUÍ | Brasil | 2202075 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 809bd7ad-ddd8-3db1-9bf3-ae2a09c67061 | -6.68103 | -43.21447 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 7fbc92c8-3c92-3512-bd0e-edf44928ef4f | -5.77648 | -43.45674 | 2025-06-19 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 117b9328-a9bd-3a7a-9724-a5e4582d49a2 | -7.23824 | -43.08076 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| f658ca60-ac68-3260-af3d-a33c7c16abed | -6.32339 | -43.75692 | 2025-06-19 03:30:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9c6596df-ba76-35f7-99c9-68eb29a8ddcb | -6.67357 | -43.20787 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 556a3b4b-0fb7-307f-be0b-9a3d4c8c8772 | -6.65718 | -42.48589 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b7778c75-58ce-3dde-a5bd-7d9ceed66c97 | -8.06638 | -43.1064 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 3a5a4456-e703-33fd-9bbb-cd6abe2901c4 | -7.23274 | -43.08614 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 5a8fcb17-6af0-38e6-8640-4fab8cd678da | -5.12535 | -45.02962 | 2025-06-19 03:30:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5043b5a4-0700-3ba1-a151-c0d6ba89df71 | -8.07877 | -43.10335 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 17.4 |
| f13cf986-a1fe-35c1-9872-ef8df20a081e | -9.43342 | -40.38468 | 2025-06-19 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.0 |
| a910bcd3-b9ad-3a8c-9f56-d473c018cc7c | -8.07065 | -43.11453 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 21.8 |
| e6ee4a98-2bea-3e2e-a5c5-7e1963baf6a3 | -7.23664 | -43.08944 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| 6e3f2f09-c765-312c-9d48-ccd61cec884b | -8.12648 | -43.13758 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| 47d38908-3bc4-35d7-af7c-d3d8f97eb16f | -9.42867 | -40.38386 | 2025-06-19 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 78da82da-dc37-3bd3-a89b-d7c679fda66a | -8.07143 | -43.11039 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| a70b140b-db6d-3f7e-bd8f-8c73ea4ca1de | -8.07801 | -43.1074 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| bc929979-0ee1-36d9-bf6b-e827e8c2ffed | -8.07724 | -43.11148 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 9fac0f08-282a-34b7-b129-ce9348a939cf | -6.68271 | -43.2053 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| dc339c22-0e6d-3bd7-9504-23ef3ca61cae | -5.12502 | -45.03674 | 2025-06-19 03:30:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.6 |
| ecf2feb5-4788-359e-8b47-3509ce409f85 | -6.66484 | -42.48547 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 59681064-df8f-3659-8be8-fe7a65c2b3f9 | -9.33267 | -37.97976 | 2025-06-19 03:30:00 | NOAA-21 | ÁGUA BRANCA | ALAGOAS | Brasil | 2700102 | 27 | 33 | nan | nan | nan | Caatinga | 1.4 |
| d7e7b6b5-4a05-351e-8bab-32d6789193ad | -7.23586 | -43.09367 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| fc8cb87d-93fe-3f1e-91ab-df34b0384878 | -8.07872 | -43.10456 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 33.0 |
| cd649e48-9b0f-37f8-bf6c-e0819eb8e5f1 | -6.67674 | -43.20418 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| b0601fa7-58ea-39c3-a6e9-f76b2ed681b2 | -7.24333 | -43.08612 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| ee1ef1f3-8e5f-3946-addd-f7ff74c44809 | -6.67139 | -42.4819 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| eacab277-f568-3952-8a17-69f76f5be5e3 | -6.65641 | -42.49026 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 3d5be027-092a-32f5-ab23-ac81aa45da55 | -6.67438 | -43.20327 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 0355287a-5402-365c-9f53-1122c6a6b2e6 | -8.06563 | -43.10931 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 682aaaf8-f1f5-3da9-98a5-8a0dcdfd6b44 | -6.68186 | -43.20992 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 39f6c9d4-4811-3a5c-89c8-6c0cbf422d8b | -6.68868 | -43.20644 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 837f3f3b-d92d-38b6-93be-61debaba4d98 | -7.23234 | -43.0798 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 052ce78c-f43a-3e33-8925-0951c17afa83 | -6.68617 | -43.22018 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 1fe8a6f4-4000-3886-b23c-7fdf6c28c64f | -7.23743 | -43.08513 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 18.4 |
| a2fc8e57-a856-3875-985e-85a516fa345d | -7.2343 | -43.1021 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 0fbc25c6-1845-3169-87a8-672d975cc4b5 | -5.12423 | -45.03588 | 2025-06-19 03:30:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 53b19439-defa-365e-b1d9-9a9a1562a34b | -7.17479 | -43.20545 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 573490a3-7672-3a69-809e-a17f12b2a190 | -9.42991 | -40.38216 | 2025-06-19 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 73794b6a-2299-3594-94e2-4b0c5792c84e | -4.00935 | -43.24213 | 2025-06-19 03:30:00 | NOAA-21 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 5ba44102-de95-332a-b432-7e21001e4e63 | -8.07143 | -43.11165 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 00deb3ec-75cc-39cd-93d9-798cf4259c51 | -6.6759 | -43.20876 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 1a61a71e-62a4-3d6a-b037-3fb658396eef | -6.66955 | -42.48262 | 2025-06-19 03:30:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 5b11dcd1-6371-3e01-8d48-945fb3465b93 | -8.12722 | -43.13354 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 22.2 |
| da275d19-80b4-3c00-8e98-4b370e22ad7a | -5.77562 | -43.46151 | 2025-06-19 03:30:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| adb1b8c9-cb4a-3ed3-ae4f-2ac8d43fd221 | -7.23315 | -43.07545 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 15.1 |
| 6e1610a0-7e49-3f00-aeae-d9d32393b592 | -6.70467 | -43.25458 | 2025-06-19 03:30:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 59e852f8-8d5b-3eae-a322-1867e6ea100e | -10.69601 | -37.04804 | 2025-06-19 03:30:00 | NOAA-21 | ROSÁRIO DO CATETE | SERGIPE | Brasil | 2806107 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 4ffb923c-5d81-3af9-b158-f331e710d928 | -7.17399 | -43.20987 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 2c25ebf0-7697-30e3-a4fe-60b7438d0c2c | -8.12797 | -43.12951 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 15e9a234-1dde-36b3-9c92-8c79a53ed181 | -6.29771 | -44.23798 | 2025-06-19 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 5e0e56a2-8463-3597-9dc0-691cf82f30a5 | -7.23904 | -43.07642 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 16.8 |
| 83287a12-4fff-3e7d-bef6-74802d67838a | -4.83905 | -43.18755 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6e356158-44b8-3457-8b75-ad558194e26c | -6.2412 | -44.65633 | 2025-06-19 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 6b2e3855-4b13-32c5-bd7c-a90c6b8203d3 | -4.84524 | -43.18843 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 056c5c8c-97ca-3780-b6c8-cffae5df3b51 | -7.16724 | -43.21329 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 923823f2-cdf8-379d-abca-4ec52d25ad31 | -8.07724 | -43.11275 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 32.3 |
| 2905e534-93cd-33e9-b6ab-4746de3d66a6 | -7.16643 | -43.21779 | 2025-06-19 03:30:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| f775f569-6e2b-3232-a3ce-25920c0dca62 | -9.42896 | -40.38735 | 2025-06-19 03:30:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| aa9d915e-96f6-361f-8ec0-f5a83975b21e | -6.2914 | -44.23629 | 2025-06-19 03:30:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4a676338-abd6-3309-ad58-5ad3f5c5c0e1 | -4.84608 | -43.18373 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 99c18a6e-7fde-3699-92bb-a40ace7b9899 | -5.12618 | -45.03045 | 2025-06-19 03:30:00 | NOAA-21 | SÃO RAIMUNDO DO DOCA BEZERRA | MARANHÃO | Brasil | 2111631 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 37cd1b34-75bb-39e9-a1fb-1d3ed320f9b8 | -4.84518 | -43.19123 | 2025-06-19 03:30:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dc080000-033c-3f1e-b582-cb13c02e6a13 | -8.06641 | -43.10517 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| e8e8a245-d650-36d7-a054-c839f5247efa | -8.07221 | -43.10626 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 34.0 |
| 457b1aaa-e682-3413-bd12-6cd50192b104 | -8.06563 | -43.11056 | 2025-06-19 03:30:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 587d033c-858f-3645-9215-840c32205ed5 | -12.26476 | -44.61106 | 2025-06-19 03:32:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b722602e-4176-3afa-9a05-9622ecd902ae | -14.21189 | -45.5164 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 29a0fa7e-de90-32ab-9c75-9f7d74ea3948 | -14.81687 | -48.47345 | 2025-06-19 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 22.1 |
| 795f5367-c3ac-390a-b61a-eb99813307a4 | -16.68368 | -43.88489 | 2025-06-19 03:32:00 | NOAA-21 | MONTES CLAROS | MINAS GERAIS | Brasil | 3143302 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4b29051b-d5cc-3baa-988b-38f53d205be2 | -15.29484 | -48.66052 | 2025-06-19 03:32:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8ee96047-f947-30ce-902c-57f1acfd4d8c | -12.26658 | -44.60198 | 2025-06-19 03:32:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| f70e9854-f451-3ec2-a37b-5c56b7f5188c | -13.44541 | -44.48236 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c0ffc841-3351-398d-815d-364169aa09a6 | -13.64348 | -43.18217 | 2025-06-19 03:32:00 | NOAA-21 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 4.9 |
| 7fe0d263-4270-3495-977c-c8955855636c | -14.82076 | -48.47318 | 2025-06-19 03:32:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 9fa8aaaa-250f-3cc6-8a96-2e2c1ce8816f | -11.9122 | -44.17798 | 2025-06-19 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6a37e9b1-0539-37a0-add1-57e9b0fd4d9c | -13.4461 | -44.48094 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5e6abf4e-1787-39aa-9d20-fe2385ba7b00 | -14.20995 | -45.52592 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 29fc9884-15e7-3043-a586-960e046133cd | -14.21285 | -45.5117 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 413152dc-2f69-32e3-919b-a254840a4b1c | -14.21205 | -45.51927 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 57e5bfdf-fec1-3a9a-a7f2-da3d7a7c4352 | -11.41974 | -41.39636 | 2025-06-19 03:32:00 | NOAA-21 | MORRO DO CHAPÉU | BAHIA | Brasil | 2921708 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cadd701d-892c-3cf9-9dbf-c9ac7e64397d | -14.21105 | -45.52402 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 3ad710d7-9c5b-35a8-ac05-bd3a5f85ff6c | -12.75631 | -44.40929 | 2025-06-19 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 86562b99-56b5-31f3-b805-10bdd651bdcb | -12.76793 | -44.41163 | 2025-06-19 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a33aa3bd-6738-39c6-b094-f8e014eeca0a | -12.26567 | -44.60652 | 2025-06-19 03:32:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 7.0 |
| b155c16d-e934-3c2f-84c6-dbaf02754088 | -14.21403 | -45.50989 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c063b3f7-3fdb-3aef-87fe-78c147d2d0b6 | -12.78186 | -38.49664 | 2025-06-19 03:32:00 | NOAA-21 | CANDEIAS | BAHIA | Brasil | 2906501 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| 14c2f72f-e43d-364d-b0c5-c935b812b0a6 | -15.29327 | -48.66743 | 2025-06-19 03:32:00 | NOAA-21 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0b3db10d-49b6-3d2d-a32d-90ab78b20a61 | -11.91136 | -44.18222 | 2025-06-19 03:32:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 67b9fe17-03d6-3ae4-88ff-1f3393e2ce4a | -14.2181 | -45.52058 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 4eda671d-d9d7-3c3e-a3c3-8dbdf9ef4565 | -13.08323 | -43.50742 | 2025-06-19 03:32:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ea7a4275-fe0a-3e7d-918d-586fb3022776 | -12.76212 | -44.41045 | 2025-06-19 03:32:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 2e4af09b-3f13-3231-9592-3795b8a6c426 | -15.80042 | -42.03415 | 2025-06-19 03:32:00 | NOAA-21 | TAIOBEIRAS | MINAS GERAIS | Brasil | 3168002 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| a8bc4b76-5f00-3e9d-9b3c-9c9dc9f5c25c | -14.22007 | -45.51123 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b5e31a31-445d-39e8-b970-59d03f2a550a | -13.44516 | -44.48552 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 38aa5bc9-e4b0-3a3b-8a0b-4f304085c0c4 | -14.21304 | -45.51456 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5ba4c651-ade5-3c10-9457-b66ceea60706 | -14.21908 | -45.51589 | 2025-06-19 03:32:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 72703744-19d7-3bef-86ca-8bae94722f2c | -13.08265 | -43.50722 | 2025-06-19 03:32:00 | NOAA-21 | SÍTIO DO MATO | BAHIA | Brasil | 2930758 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README8.md)
