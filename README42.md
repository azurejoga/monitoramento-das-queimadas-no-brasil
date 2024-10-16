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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7c07378d-5256-3583-aa0d-bed6f175d3ea | -6.09012 | -46.0956 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e55a46be-2b70-399c-b829-58e719503f10 | -6.08673 | -46.09507 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 565aaa60-3118-3be0-a5e0-7c40c088fa39 | -5.98756 | -45.74052 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2b4ec6c7-91cf-3f83-ab30-86f45716c2c3 | -5.70332 | -45.67553 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f396ed4a-c553-3b1d-8504-aab894474b05 | -5.60768 | -45.19859 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c7b8939d-1808-3daf-83a5-0cc5d71002a1 | -5.60709 | -45.20245 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a1253ed0-2316-373a-8a0d-5b3a1bdeefb6 | -5.60419 | -45.19806 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 858807fb-9a47-3363-891b-d9be642bdb8f | -5.6036 | -45.20192 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 27415d03-59fa-3ed6-9812-685d4daab7cb | -5.5149 | -45.39773 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 525f24c2-288b-3e33-b08f-03e093549892 | -5.51144 | -45.39719 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f07a1a6d-ffe6-393f-be35-2b6046b7d40c | -5.45095 | -45.88015 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffbbc2b2-0129-31c1-b23e-2a940c2b05b0 | -5.42241 | -45.47721 | 2024-10-16 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa7250e1-73f4-3b8d-b864-7ce341ac6524 | -5.41552 | -45.47615 | 2024-10-16 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 64a12668-7855-3060-bf21-3b568f08c65c | -5.40695 | -46.00756 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b0f1822d-5a5e-3aa0-aa6d-05065120c2c2 | -5.40357 | -46.00705 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ae0e180-26a1-3d0c-a1ae-352dc0dc2d9d | -5.35847 | -45.88874 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8f18c96b-d448-31c0-a263-05397506dfcd | -5.35452 | -45.89186 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9c1752f5-e468-37c9-b17b-ce489a2cec87 | -5.30652 | -45.40973 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22658526-a5d8-3324-b6b7-0dac9e337d48 | -5.30306 | -45.40921 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 75f0ff0d-7277-3e6f-b31e-3e1b9ea22ebc | -5.25569 | -45.85054 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| aa4f5b84-b29a-3dda-9cf6-c2e001688342 | -5.19606 | -45.55865 | 2024-10-16 04:29:00 | NOAA-20 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cf5a5300-0e5f-3bfa-9160-27b25e8984a9 | -5.17071 | -45.72155 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 785a4af0-2e0b-32ed-94a7-2c14a8cdfe57 | -5.14175 | -45.77335 | 2024-10-16 04:29:00 | NOAA-20 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dc215640-60ee-3e5e-bd86-550a345cc95e | -5.13582 | -46.08831 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a346dac0-b26a-3bbc-a55f-d686f4ccfc1f | -5.13527 | -46.09192 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fe8c797a-c5b3-364f-8974-ddd3745f624e | -5.09471 | -45.83006 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64129bbe-5a15-3e97-9189-13fcf478d333 | -5.09415 | -45.83373 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16cfc6ed-7359-3a02-a191-62002d411711 | -5.09075 | -45.83321 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 535ab58b-1f29-3969-9bed-c47439666329 | -5.05227 | -46.08298 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2d5beab3-aed8-3168-8691-f94e02fe25a7 | -5.04891 | -46.08247 | 2024-10-16 04:29:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 4ac6ba12-90e9-3bf9-9c61-29b254dcbc70 | -5.56233 | -45.06533 | 2024-10-16 04:29:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| cb469d0b-8ab4-3b4a-9d2a-f27c5f0fc74b | -6.01554 | -46.42021 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d455e7ba-f7a7-3c58-bb02-6f33325d3574 | -5.57979 | -46.31702 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ce928d5-73aa-331e-8c9c-deba0109f584 | -5.55956 | -46.29212 | 2024-10-16 04:29:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3c7e62e7-4450-3cf0-97f3-2bf5f58c6c6b | -5.49407 | -46.43522 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9c6fba69-8222-39b4-9ebb-8caeafc5ac8b | -5.49351 | -46.43876 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5fa4421a-b7a1-3e50-919d-f5d2ef9f5c29 | -5.47946 | -46.3748 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 58abe5c3-9f90-33ed-8d7b-f2c928869aa5 | -5.40809 | -46.41486 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5b0637d0-63c1-3b93-8d3f-f4025537e1e6 | -5.28335 | -46.34877 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 337664d8-8867-3955-85ba-85d3f8f1531d | -5.28 | -46.34827 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6a24e17c-4ca1-35b7-a186-fce1d74de248 | -5.27944 | -46.35185 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d2ecf61d-0379-377c-bd7d-ced2ee69c7a9 | -5.27553 | -46.35492 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ed01818e-300d-373e-a657-c7e30860605c | -5.27498 | -46.35847 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c0e962fb-fc68-3312-ab08-3545e09e5d5b | -5.27442 | -46.36203 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06b2e623-3d66-3f74-b114-3a9393fb6b68 | -5.27388 | -46.36555 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c70a72a7-95a0-3c51-bae3-46164957b4bc | -5.27278 | -46.37261 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9df8c38c-6401-3314-852d-ae123da6d777 | -5.27107 | -46.36152 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c032fcd1-b8c0-3ccf-99ff-3ec6a16b2f9e | -5.27052 | -46.36506 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9af4062e-1bac-3f22-b064-8860ab6455d4 | -5.26998 | -46.36858 | 2024-10-16 04:29:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f8917d9-8af3-305f-b68d-b8b1f7159c9a | -1.97617 | -46.36209 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| a9675d51-6bec-35fd-b553-02349e6f5ab8 | -1.97286 | -46.36158 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1bddfb73-7e93-3760-8dc1-1405685a4f9f | -3.30145 | -47.00931 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9c7db6dd-537a-341b-8881-640760ad5f6d | -3.2982 | -46.55365 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f22f54da-d07e-3930-b64f-c16f15e8da9f | -3.29489 | -46.55314 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6971cfad-498f-3d38-b78c-ed2cced7e9e3 | -3.29435 | -46.55659 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5cd16b85-e2e5-3abf-80f0-d8a32b963dad | -3.29104 | -46.55608 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 166fac2b-3aee-3dab-9832-792e4a6b0270 | -3.28773 | -46.55556 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b3b10dba-341e-3550-8c42-fb71f900db2e | -3.28718 | -46.55902 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 26c88222-d408-3d93-bcb6-5221a43de6eb | -3.28652 | -46.51995 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 33f6b2d1-77de-397e-8475-704400f7d734 | -3.28641 | -47.12658 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 23.0 |
| 679d38a0-aff4-3cb0-bcbc-316a11855d40 | -3.28598 | -46.52341 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8055d01a-e397-3ba8-9cae-289242dad982 | -3.28365 | -47.12263 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e91b591d-a029-36c7-8023-eb82f917b939 | -3.28267 | -46.5229 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 45004582-523f-3d05-bfc8-dafc06e68c1e | -3.25287 | -46.88546 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac72d6b-8464-36d3-b84c-fdd82918e902 | -3.25233 | -46.8889 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 634833e6-490f-3494-ab96-7e86a03b1d8b | -3.24903 | -46.88839 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b8ac9422-3846-3eee-9630-83adea3ec3b9 | -3.24626 | -46.88444 | 2024-10-16 04:29:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| acea29d3-80a0-3bf6-ad28-19ea4bf6d81c | -3.22194 | -46.5206 | 2024-10-16 04:29:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 41a6af78-b325-3f16-bb3c-99ab5217bd57 | -3.07788 | -45.94449 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54c5e3d5-68a0-3a2d-967b-4705b81f74d9 | -3.07398 | -45.94751 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e4a4e36d-e40d-3202-8030-d479b1db6603 | -3.07287 | -45.95455 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02fb9543-26a8-3e81-8578-be8ed86ccbb2 | -3.06953 | -45.95403 | 2024-10-16 04:29:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c899d48e-2fa3-3979-a690-3d3d97ec3a60 | -2.53855 | -47.32297 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e4b6af98-f142-3a39-a1dd-67b5610c0fd8 | -2.53 | -47.22656 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 29393a35-1b58-369d-b55b-4c3f7822272d | -2.34526 | -47.25718 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7e1458b5-4bf7-37d4-8c5f-b4258d5fa85e | -2.34196 | -47.25666 | 2024-10-16 04:29:00 | NOAA-20 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f758508-ee18-324f-97f5-32af4f8fa02a | -2.33441 | -46.48105 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db96f1ef-8a00-37cb-ab81-e40a9d2d300d | -2.33387 | -46.48449 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e93a02ef-5b5e-3f9e-bc77-a10921c8c8f4 | -2.3311 | -46.48054 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bc66f73b-688f-387a-8305-fdf001f906e3 | -2.33056 | -46.48398 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 64afcb5d-0aa8-3e4e-84ff-e95a88c7ed16 | -2.33002 | -46.48743 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| d821ee5e-b0fb-32b6-9897-cbec93db19da | -2.32671 | -46.48691 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 2945a583-17b1-33d4-b766-ec9d3a1f318c | -2.32617 | -46.49036 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 6af5fda0-8c9d-38c2-8dfd-e3ddfa64c616 | -2.32551 | -46.45145 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58fb4ab2-33c8-3c2d-a51f-c10d1e2cf425 | -2.29842 | -46.60234 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6928f032-0ebf-3cf7-ae3b-d41cbb3c573a | -2.25817 | -46.75089 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4edf4536-94ea-35f6-8850-a58896404c42 | -2.25655 | -46.76118 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5a284375-d539-3709-9552-6d3c78384203 | -2.25318 | -46.73957 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8e3c888d-2c70-35c9-a024-6eb2f2f5aa62 | -2.2521 | -46.74643 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56b2484e-4a42-36e8-8120-e56e0a2fb08b | -2.24934 | -46.74249 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e885a68e-99f5-3967-8424-38517d7c77c9 | -2.2269 | -46.77768 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b69369d9-cd6d-3d35-9155-443689b2132c | -2.22414 | -46.77373 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6442c7c6-1f1b-36bc-941a-23c00c8501e1 | -2.2236 | -46.77716 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3db01e5f-fbed-321c-8b6e-384e96060d3b | -2.20352 | -46.45012 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0b02e3a0-20e1-392f-93b9-7d9334053f17 | -2.20021 | -46.44961 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fc607ef7-5b99-3541-905e-f8b8ab4ca92e | -2.19765 | -46.74853 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b48d2a50-14c2-3856-b511-5857e5bb778f | -2.19721 | -46.72725 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 744e45c6-b6ec-3982-953e-4877ba056fb8 | -2.19397 | -46.74784 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b0cac74-f454-35e8-988a-aa8e17f94b9b | -2.19391 | -46.72674 | 2024-10-16 04:29:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5328cdf6-809a-3ae8-b66e-f7ae9fc1d21a | -2.19251 | -46.45547 | 2024-10-16 04:29:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
