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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1fa156c-8374-389e-8d5d-d2572c8d2e5f | -4.27726 | -46.92809 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eff62da1-57e1-37fa-a0b2-196d86bb9ab3 | -6.24574 | -42.92799 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 93798048-aa41-3500-95fd-bc5b7cedf9af | -5.49115 | -43.0728 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 240b57f3-90fe-3d61-80de-46efd033b80d | -5.67128 | -42.68201 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17997cf4-7549-3671-b348-25add2f1b873 | -6.2823 | -44.08017 | 2025-10-12 04:14:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e24e6821-2b55-3d87-88b2-fd85938ac8ef | -7.70272 | -42.37389 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 6035e19d-b043-3b77-af77-ff2608e17ae5 | -10.3921 | -44.17976 | 2025-10-12 04:14:00 | NOAA-21 | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c2bc7865-3160-3281-b056-aa778c7eac75 | -5.91462 | -45.4332 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 2acaa80f-ccef-31ad-afc3-911cf020ff84 | -7.50663 | -42.14405 | 2025-10-12 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| df482334-61c9-3ce5-8eb0-79f5db9e0b37 | -7.40319 | -42.96998 | 2025-10-12 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| fa1ea92e-358f-3e0d-aad3-38ce9ff1dc54 | -6.32879 | -41.60138 | 2025-10-12 04:14:00 | NOAA-21 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1a4f44ca-00f9-3139-9ca2-92ff89d8ccb6 | -7.74002 | -42.41943 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 394e6743-8a2e-3180-b947-1913db248ab8 | -8.21878 | -43.34756 | 2025-10-12 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bf729f94-ac9b-3e4b-b882-c8bda4a75fba | -6.74259 | -42.16031 | 2025-10-12 04:14:00 | NOAA-21 | TANQUE DO PIAUÍ | PIAUÍ | Brasil | 2210979 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| b4ef5739-b8a1-3881-adfc-1ae1905aac1c | -9.40147 | -42.67025 | 2025-10-12 04:14:00 | NOAA-21 | FARTURA DO PIAUÍ | PIAUÍ | Brasil | 2203750 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| d8918fb7-d3c7-38cb-8ce5-3ba331aad4d4 | -7.549 | -43.83946 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| af6005f2-95c5-35ea-b049-56397135de9e | -9.24053 | -47.04688 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e7b9927b-6d22-36b4-a8fd-95f620d2d9c3 | -5.91873 | -45.42988 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 1dc22ea9-fc2f-3951-b55a-0a70bd77be63 | -5.58447 | -42.99949 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| afa56611-6902-3ccc-af71-5e684b9722b9 | -4.2688 | -46.93166 | 2025-10-12 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b370a18b-7785-3ddd-af3f-fc2e0dcf05d5 | -6.32175 | -44.25983 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4dab743f-b5d7-39bf-bba7-7c13dfe788ef | -5.46782 | -43.39756 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6f5441d5-f357-38c7-9919-488acc6dc324 | -7.00728 | -40.68958 | 2025-10-12 04:14:00 | NOAA-21 | PIO IX | PIAUÍ | Brasil | 2208205 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| c9c4191b-634c-3fa2-87a9-1ceb253948c6 | -5.29062 | -42.53045 | 2025-10-12 04:14:00 | NOAA-21 | PAU D'ARCO DO PIAUÍ | PIAUÍ | Brasil | 2207793 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| f6bccbdc-e464-3dca-8f92-cd64229b0ee7 | -9.0052 | -47.35172 | 2025-10-12 04:14:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d3925e07-2b8d-38bd-95df-8ae264646d17 | -5.94094 | -43.93586 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 00ca15f4-4bb5-317b-be48-219f745a9141 | -5.49169 | -43.06936 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 28a34d1c-eaf5-3b2c-86bc-11e4793f232d | -6.25649 | -43.03193 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6c005b53-b63a-31d5-814f-0220cda84121 | -6.98622 | -42.03453 | 2025-10-12 04:14:00 | NOAA-21 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 6b6f9a15-3d40-3371-bb85-1912a49c657e | -5.74279 | -41.32362 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5cf14062-066b-3cc4-8b24-663e10ac1bdb | -6.04479 | -42.4727 | 2025-10-12 04:14:00 | NOAA-21 | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 0ca9ef2f-67d8-3eb3-a748-3d0c1c6cdb26 | -7.00506 | -49.34165 | 2025-10-12 04:14:00 | NOAA-21 | XINGUARA | PARÁ | Brasil | 1508407 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 13bf06b6-90e9-32e6-852d-d74cf0e41185 | -7.35812 | -44.80657 | 2025-10-12 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8a7015bb-dbd3-3a2f-975c-06318e6861c1 | -5.48434 | -43.40015 | 2025-10-12 04:14:00 | NOAA-21 | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6c18e16b-b0f8-3644-8a70-79af8e56e212 | -9.52677 | -47.86134 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e8acb73f-cdbe-3deb-acf7-58aa66ce2efc | -6.76825 | -42.83075 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d6cd049c-2808-3bfa-a95c-1875f679a0c8 | -5.59602 | -41.11183 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 12ec0aa6-8f36-3449-9761-5e530fc0aecb | -6.65705 | -41.38382 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| d4d766f0-5a22-348f-9ca0-f2c1083efa80 | -7.88403 | -44.49881 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 31a3c006-9fe1-3d35-9491-9f38ac9e7347 | -7.86283 | -44.11779 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d9fca792-b117-3b87-a639-56fbaa74b815 | -7.14622 | -42.52046 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 92882084-900b-37e0-b0b6-466c62970e78 | -6.24983 | -41.56362 | 2025-10-12 04:14:00 | NOAA-21 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 605628c1-81f8-3ba1-a0b2-862db8a1bfcd | -5.11949 | -43.01412 | 2025-10-12 04:14:00 | NOAA-21 | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| d67f95f0-6053-3cc2-9e07-7b19965085fd | -7.65084 | -42.57764 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 71e9f97a-0811-3e88-aea5-cfe1ba3cc359 | -6.67287 | -41.37106 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOÃO DA CANABRAVA | PIAUÍ | Brasil | 2209856 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| e5bae878-7b2a-336c-a815-d2596e70e6bf | -5.55996 | -41.32191 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 62c91e9f-739b-383f-922c-269d47c449c6 | -5.47167 | -43.39462 | 2025-10-12 04:14:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b966f77e-5e0f-3c42-9558-45a4e963ce75 | -5.5986 | -41.10105 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 54ab1299-9568-3971-ad42-e5873b943d09 | -7.27105 | -42.96712 | 2025-10-12 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 85697b0f-f844-3792-b9e2-700d99e17d5a | -3.82705 | -47.73684 | 2025-10-12 04:14:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 34a444af-45c4-3b51-b560-6322469b4035 | -4.47238 | -44.9199 | 2025-10-12 04:14:00 | NOAA-21 | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75b34119-31ba-3231-997d-7b3f15e6c222 | -5.81335 | -44.0312 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| fd2b2186-1a3d-39ae-811e-c753f1d5752c | -5.36508 | -44.91999 | 2025-10-12 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e6efbc94-c240-3107-a3c3-c9f0631af2a6 | -5.91651 | -45.4216 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 159137fb-24d9-392b-a856-46b74bfbe0ad | -5.80945 | -44.03419 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 954e47da-9de0-38a2-ac1b-f42ac8f1ee35 | -6.88811 | -44.69755 | 2025-10-12 04:14:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| f8f9f14b-4ae7-3e58-af00-a9bbe83915ba | -11.50288 | -43.48949 | 2025-10-12 04:14:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 8d4b855c-f327-355f-973d-40e1258d4552 | -9.43196 | -46.95221 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07f5efff-07f5-3623-95ca-d97699538024 | -5.58333 | -42.98523 | 2025-10-12 04:14:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 2daf271f-da7a-3414-bcb2-443e3a2d2f92 | -4.67865 | -43.26197 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 121b4476-947d-3f38-9da7-9326a21ad067 | -7.48892 | -42.76675 | 2025-10-12 04:14:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f7e47ebd-95db-3620-a509-09d37423dbc2 | -9.34889 | -46.88407 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 64e2ab85-99b6-37de-a3ee-065294028aa0 | -7.45932 | -43.89283 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4f73024c-1582-302e-853e-8f2204f02e03 | -9.23691 | -47.0463 | 2025-10-12 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 22be6d2f-ed09-32cd-ae8d-147189bddad7 | -7.01715 | -42.73899 | 2025-10-12 04:14:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| eb0b5745-5ad8-3dc6-b349-68dfbfabaeb6 | -7.28989 | -41.96482 | 2025-10-12 04:14:00 | NOAA-21 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 3c35ecf0-14cb-3b05-9b45-4523b88cfcc1 | -4.67643 | -43.25455 | 2025-10-12 04:14:00 | NOAA-21 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 32163a9d-2e32-34b6-ae3a-9888994249f0 | -5.42944 | -41.37232 | 2025-10-12 04:14:00 | NOAA-21 | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 5d57f67d-d2a1-38b1-8aa9-95f54765b42e | -6.50259 | -42.43762 | 2025-10-12 04:14:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| f72d820a-d291-3f35-b70e-7284b20b35bf | -7.68191 | -42.57573 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 01d74cd7-e7a5-3b4a-aa63-2bc0d439037d | -4.57928 | -45.69541 | 2025-10-12 04:14:00 | NOAA-21 | PAULO RAMOS | MARANHÃO | Brasil | 2108108 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4fd48507-a25b-39fc-8963-a8a4f709f9e8 | -7.8623 | -44.52816 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| af979295-9107-3815-99e1-8b3ca322a182 | -4.54239 | -49.68768 | 2025-10-12 04:14:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 64e3dc50-0fb0-32fc-bb7b-583441329f19 | -7.51664 | -45.13382 | 2025-10-12 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d02ed4cc-e885-3f6c-85a1-37b72e965eee | -6.2532 | -43.03142 | 2025-10-12 04:14:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 713c694d-703e-341a-adef-0406dc39cfae | -5.91177 | -45.42879 | 2025-10-12 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 8.9 |
| ca6dc48e-ead2-3455-bc04-090ceb100c7d | -6.16796 | -44.66883 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a8fbcb75-5110-3851-bfd6-7b4c8660497e | -7.50609 | -42.14761 | 2025-10-12 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 56b61e35-f688-3569-898d-d16bff311af4 | -4.6181 | -45.77326 | 2025-10-12 04:14:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2a0bafbf-d841-3414-b591-86b25328cdf9 | -8.02386 | -44.47468 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| dd8fc394-1e28-3631-8109-dd3800c6fcd3 | -7.83601 | -44.80164 | 2025-10-12 04:14:00 | NOAA-21 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fefe8db1-257c-34dc-b82c-a2c77f15b0b5 | -7.5457 | -43.83892 | 2025-10-12 04:14:00 | NOAA-21 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9247eb95-c21f-3c27-ba0d-491b6426145e | -10.15994 | -44.5496 | 2025-10-12 04:14:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 146f67b5-7294-303f-8ef8-77b44b3e9116 | -6.43304 | -43.36006 | 2025-10-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d2e8731c-cf73-39e2-8c1d-3e1a3a456113 | -8.68974 | -48.57532 | 2025-10-12 04:14:00 | NOAA-21 | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 994c36ce-0d76-3ff7-bc5f-ef6eb9f9e67a | -6.57547 | -43.10357 | 2025-10-12 04:14:00 | NOAA-21 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1b2d55e6-80d9-3a1e-a20b-2863a326a0e7 | -5.80223 | -44.03669 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a0f39229-7808-3f81-8a7a-2c14546fa34d | -6.31898 | -44.25578 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f8d92218-f58b-3812-a0bd-e55759502b0d | -7.85566 | -44.12023 | 2025-10-12 04:14:00 | NOAA-21 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7de62043-1174-355f-866b-27d34c047b33 | -7.67143 | -42.40109 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8c4dd6f9-1eee-3c72-b225-a9487d3768f9 | -6.58346 | -44.62323 | 2025-10-12 04:14:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2019a599-576f-3d2b-93f5-864dac3a0a75 | -5.60441 | -42.56932 | 2025-10-12 04:14:00 | NOAA-21 | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 0651df80-7708-3ffe-b2a9-3c538376f750 | -6.6097 | -42.4932 | 2025-10-12 04:14:00 | NOAA-21 | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f1433e78-6734-3a92-982b-67737bd1b76d | -9.52221 | -47.86531 | 2025-10-12 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 397221f3-9cb1-34b4-a93a-a4a44f200676 | -7.65524 | -42.57115 | 2025-10-12 04:14:00 | NOAA-21 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 09aad509-bd2c-3e26-bc53-cd799b8a42f5 | -6.16572 | -42.54804 | 2025-10-12 04:14:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| cf769d8f-b2fb-35bf-b5c6-d1ae8f5e0d3f | -11.75806 | -43.31151 | 2025-10-12 04:14:00 | NOAA-21 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3f80773-1f89-3166-8c04-767a1da15ab5 | -7.50554 | -42.15118 | 2025-10-12 04:14:00 | NOAA-21 | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| f999979a-c64e-31b1-9c1d-f9a621ab5001 | -5.81724 | -44.0282 | 2025-10-12 04:14:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e79c6cad-5ad8-3589-8ea1-47a2aa5196e8 | -7.6808 | -42.38458 | 2025-10-12 04:14:00 | NOAA-21 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |


[Clique aqui para ver as próximas entradas](README17.md)
