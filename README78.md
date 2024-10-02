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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 48c1c115-b472-3cd9-a159-8057d485e96c | -23.27286 | -46.65383 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 329fc903-5d2f-35aa-afeb-41c00ae8c1bf | -23.2719 | -46.65888 | 2024-10-02 03:57:00 | NOAA-20 | FRANCO DA ROCHA | SÃO PAULO | Brasil | 3516408 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| f9b6dd50-2e58-3512-bd22-92fd34b2fcf0 | -23.22151 | -46.47036 | 2024-10-02 03:57:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| fc1975e3-b318-3edd-9b49-11afaeb91885 | -23.21777 | -46.46954 | 2024-10-02 03:57:00 | NOAA-20 | BOM JESUS DOS PERDÕES | SÃO PAULO | Brasil | 3507100 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 892f7537-c988-35be-9628-1f91fb081a82 | -23.15789 | -46.32822 | 2024-10-02 03:57:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 1d142aaa-2e92-3325-a529-31a56e13a3c4 | -23.11792 | -46.26698 | 2024-10-02 03:57:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| dc64099d-21d0-31cd-ac21-963c7563b226 | -23.11576 | -46.2637 | 2024-10-02 03:57:00 | NOAA-20 | NAZARÉ PAULISTA | SÃO PAULO | Brasil | 3532405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 3c47c7e1-d760-3854-91f3-c82b958e7680 | -23.0942 | -46.37905 | 2024-10-02 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 91b86261-9788-33c1-8d22-00a996fde0e2 | -23.09323 | -46.38208 | 2024-10-02 03:57:00 | NOAA-20 | PIRACAIA | SÃO PAULO | Brasil | 3538600 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.8 |
| c0c8227d-b809-3f12-8633-5abbfd4925b4 | -23.03463 | -46.88411 | 2024-10-02 03:57:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| cf10cffb-df70-3814-81b7-747e7ecacea0 | -23.03081 | -46.88319 | 2024-10-02 03:57:00 | NOAA-20 | ITATIBA | SÃO PAULO | Brasil | 3523404 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 1e980e90-597c-3258-9bc8-32339cc8a41e | -23.06588 | -45.90625 | 2024-10-02 03:57:00 | NOAA-20 | SÃO JOSÉ DOS CAMPOS | SÃO PAULO | Brasil | 3549904 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b80444a6-d3d9-33fe-b4fb-c7e47e2061bb | -22.94167 | -46.46478 | 2024-10-02 03:57:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| aa4b789c-86df-3ba3-bc1c-b50c96f76a08 | -22.9379 | -46.46405 | 2024-10-02 03:57:00 | NOAA-20 | BRAGANÇA PAULISTA | SÃO PAULO | Brasil | 3507605 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| d149de51-a92f-3d99-8a72-996ed8fce6ea | -22.90683 | -46.44186 | 2024-10-02 03:57:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5b134e7f-4c84-3b73-9a12-7a9562568ab7 | -22.8983 | -46.42469 | 2024-10-02 03:57:00 | NOAA-20 | VARGEM | SÃO PAULO | Brasil | 3556354 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dbd92d34-612d-3347-99c9-b649af7a1400 | -22.7748 | -46.82121 | 2024-10-02 03:57:00 | NOAA-20 | AMPARO | SÃO PAULO | Brasil | 3501905 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 61bfb581-54b5-33ab-b2fa-b1d9be962497 | -22.71862 | -46.6844 | 2024-10-02 03:57:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 2c3cffa0-0a4c-3dd4-8821-b96f3e91d166 | -22.71654 | -46.68551 | 2024-10-02 03:57:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 7.6 |
| 95f707a0-9553-3791-b8d6-a0fba9a6be3d | -22.71481 | -46.68356 | 2024-10-02 03:57:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.2 |
| e00243f5-cb33-35f7-bc0a-6917be3e4460 | -22.71272 | -46.6847 | 2024-10-02 03:57:00 | NOAA-20 | MONTE ALEGRE DO SUL | SÃO PAULO | Brasil | 3531209 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| 22b95b46-c806-3e6c-af39-e108d1cca28d | -22.7009 | -46.48011 | 2024-10-02 03:57:00 | NOAA-20 | SOCORRO | SÃO PAULO | Brasil | 3552106 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 540dfdb1-ee58-3ec0-bb68-4579fa6a00a6 | -22.62264 | -46.24935 | 2024-10-02 03:57:00 | NOAA-20 | MUNHOZ | MINAS GERAIS | Brasil | 3143807 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 178807e1-c664-35cc-bfbb-f883e8300713 | -22.108 | -48.46138 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 19141952-6cc4-3da0-8618-10cb199d8766 | -22.10282 | -48.46494 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5cc4f1b-0eac-3ff3-9aac-2a0b67eff641 | -22.09851 | -48.4641 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9b882970-55e7-3476-8b6a-4cc837b65a16 | -22.09421 | -48.46326 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 1e164475-d06d-33ee-97e5-7701f30c69e8 | -22.09337 | -48.4675 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 73572171-63fe-3bb4-a584-ddcee7e4d57f | -22.08734 | -48.47532 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 00b13df3-db0f-3d24-8144-b3c46d30a054 | -22.08474 | -48.46588 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 48578d69-0023-3999-9210-0cd3992c548c | -22.08388 | -48.4702 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| ba8dd412-dc8e-3f57-9b59-d92bb4665d02 | -22.08301 | -48.47458 | 2024-10-02 03:57:00 | NOAA-20 | BOCAINA | SÃO PAULO | Brasil | 3506805 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 0cbaf133-b92c-39f0-982a-bcd63afe3f2d | -21.89565 | -48.47594 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 35e297ab-6bf8-3c1f-9288-513a2cb4b2a9 | -21.89474 | -48.48054 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c054c373-8713-3ed3-bd01-d724dab9c6bc | -21.8905 | -48.47927 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 24de2fe1-b4ba-369c-94bc-91e6c70c88d6 | -21.88959 | -48.48388 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c528ecb8-3027-30fd-a2da-1b9956234046 | -21.88624 | -48.47807 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c6b4b3cd-2095-3fa5-9673-a71bb7e5de6f | -21.88532 | -48.48271 | 2024-10-02 03:57:00 | NOAA-20 | BOA ESPERANÇA DO SUL | SÃO PAULO | Brasil | 3506706 | 35 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 13bc2035-60cc-38db-80c4-8bf6cfbfc78a | -21.62531 | -47.82701 | 2024-10-02 03:57:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 75a18410-a53d-359b-9c34-1a2f67b78b69 | -21.62116 | -47.82609 | 2024-10-02 03:57:00 | NOAA-20 | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 22f168bf-d82b-3929-ab34-804196d66483 | -21.60664 | -47.80632 | 2024-10-02 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 2.2 |
| cd3e79d0-bee9-3dde-86aa-3213a23b6bb1 | -21.60327 | -47.80132 | 2024-10-02 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 226a08e3-2372-3641-adcc-c7e2511b6a94 | -21.58535 | -47.7374 | 2024-10-02 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.1 |
| c64ebb77-d01a-32fe-81b8-d86041e79ae7 | -21.58455 | -47.74154 | 2024-10-02 03:57:00 | NOAA-20 | LUÍS ANTÔNIO | SÃO PAULO | Brasil | 3527603 | 35 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 90cf7738-dc22-3b4b-bff0-18a716b30bbf | -21.28895 | -47.62069 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0a4533b3-fd2d-33c6-a122-6ceae493ccff | -21.28811 | -47.62505 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| a782520b-d5d9-3d99-98bf-5495a1c1880a | -21.28728 | -47.6294 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9b354679-e9e7-3a8a-b260-a087d03da102 | -21.2857 | -47.61523 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b5965d3b-feea-3c1d-9b67-98661e1a5ce8 | -21.28489 | -47.61944 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ff9e748b-22c1-3bf1-84c4-ef4f7ccb4789 | -21.28405 | -47.62379 | 2024-10-02 03:57:00 | NOAA-20 | SERRA AZUL | SÃO PAULO | Brasil | 3551405 | 35 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 53b8abf5-d7c5-3688-b4c2-b2cdef85b3d2 | -22.82587 | -48.60953 | 2024-10-02 03:57:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 28b1709f-25a6-3422-b8d4-da55dcd1cd99 | -22.82249 | -48.60416 | 2024-10-02 03:57:00 | NOAA-20 | PRATÂNIA | SÃO PAULO | Brasil | 3541059 | 35 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c0088af4-2def-37e3-9cd2-fa446634875f | -22.65137 | -47.26242 | 2024-10-02 03:57:00 | NOAA-20 | COSMÓPOLIS | SÃO PAULO | Brasil | 3512803 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 19161613-76ad-39f2-b3ec-39ebce57013e | -22.65032 | -47.26792 | 2024-10-02 03:57:00 | NOAA-20 | LIMEIRA | SÃO PAULO | Brasil | 3526902 | 35 | 33 | nan | nan | nan | Cerrado | 5.2 |
| b67079e9-fc60-318b-8883-aafbcce6c3bc | -22.92204 | -47.2821 | 2024-10-02 03:57:00 | NOAA-20 | MONTE MOR | SÃO PAULO | Brasil | 3531803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 950648f3-0c99-35d5-9468-560da5336030 | -23.81737 | -47.64454 | 2024-10-02 03:57:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| aef37324-1812-34b3-830a-6acc9afb9c46 | -23.81629 | -47.65019 | 2024-10-02 03:57:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 6da8a1a8-e656-3f0d-8559-41db9d841d4d | -23.81233 | -47.64933 | 2024-10-02 03:57:00 | NOAA-20 | PILAR DO SUL | SÃO PAULO | Brasil | 3537909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 4e00f93f-9ad1-321c-8771-4094f92645ab | -23.98466 | -48.91879 | 2024-10-02 03:57:00 | NOAA-20 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 62cd7fe4-0f85-3b79-9908-98df0326984b | -22.37065 | -49.30948 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 53d50442-b444-36a2-bfcf-032e629a4fa2 | -22.40115 | -49.3213 | 2024-10-02 03:57:00 | NOAA-20 | CABRÁLIA PAULISTA | SÃO PAULO | Brasil | 3508306 | 35 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| 1b35baf9-3e61-3b4e-b716-ff556f1308f6 | -22.39158 | -49.29888 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 33.1 |
| 2ff4b924-239f-3a4a-8b58-ae7664c81843 | -22.39061 | -49.30368 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| e1978e08-0e90-3c13-8dd4-ebc2d062ecbe | -22.38708 | -49.29791 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| ffe00ba0-ca93-38de-a20b-baaa2e4b08be | -22.38612 | -49.30269 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 69df9168-f358-3445-9252-20e2b65954b5 | -22.38556 | -49.28227 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 6609bd71-260d-3883-bcbe-db100d4d3d94 | -22.38515 | -49.30746 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 414a4820-0015-3018-a852-6c2cf9eca461 | -22.38454 | -49.28727 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| eebb2330-99f4-311c-bdf7-de1996b760b7 | -22.38419 | -49.31223 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| b894bcc6-9c07-3756-a3d5-d6501ef537d5 | -22.38356 | -49.29214 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| 916d9e00-e624-36ca-8dc0-c3372c0016fc | -22.38323 | -49.31697 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| ad24bcdc-264e-3d73-abd9-17b677c3b927 | -22.38259 | -49.29694 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 10.7 |
| b0275ee8-4f03-3536-b5c6-38701b06fe35 | -22.38161 | -49.30175 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| b2590da0-60d3-33e9-a29b-b85132eab631 | -22.38107 | -49.28125 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 0acd2591-7e84-3edb-8608-945e73ef5890 | -22.38064 | -49.30656 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.6 |
| 7b35476d-6cdb-3787-9bc0-1ce524405991 | -22.38004 | -49.28634 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| a89517b7-d52b-3170-ba30-b9a9eea04b30 | -22.37967 | -49.31135 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 14902d51-ff29-32d3-9bd0-4dbd2f6ee13f | -22.37906 | -49.29119 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| 47a5e62f-5ea1-3fe5-9701-75c19afaf9f5 | -22.37871 | -49.31607 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 7ddb94e1-4a08-3dc3-9d55-e093b25899f3 | -22.37809 | -49.29598 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| c233d982-be8e-3ecb-9f0c-8fdeedca52d7 | -22.37711 | -49.30081 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 820c3d26-ac5b-323d-9b29-e2e90c8e9e00 | -22.37659 | -49.28024 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 8e671de5-f326-3ff9-8798-511a641115c2 | -22.37613 | -49.30563 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| 151ad020-e0f5-3c84-b8db-d804a7281946 | -22.37556 | -49.28533 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 2fefca09-6db8-3c05-b853-06b2d17ec2bd | -22.37516 | -49.31043 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3d59968-3b20-33f6-b445-34e044235b8c | -22.37456 | -49.29023 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| f721cbe6-e0dc-37fb-bde5-238a0fd9f6a9 | -22.37359 | -49.29504 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 13.9 |
| dd5f3465-5561-36c5-96d1-ebac5b1032a3 | -22.3726 | -49.29987 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| fda5606c-6dd7-3d8d-8124-e03eadd7f37c | -22.3721 | -49.27927 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| 720799ea-3d64-3d12-b443-467419b1ec2e | -22.37162 | -49.3047 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.2 |
| f5ed55ac-0360-36ab-a7da-062bd0503a97 | -22.37107 | -49.28431 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| 27bbdb37-cdc4-3f09-81ad-d53db5ccd429 | -22.37007 | -49.28924 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 0a1fb8c1-3c21-31db-87b6-16064ef131e4 | -22.3691 | -49.29401 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| c51c611a-2788-3170-b7ea-bc69abcf19ab | -22.36813 | -49.29878 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9b1e0876-7624-3431-bce9-8ce050822176 | -22.36715 | -49.30358 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| afd192df-9d0d-38a7-a2b0-30932ce7ff3a | -22.36658 | -49.28332 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 26.4 |
| fb5b4322-ec2e-3ddf-acb2-c7d604ad69c0 | -22.36559 | -49.28821 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| 42eca6bb-2538-30f8-9407-ff3f803953b1 | -22.36463 | -49.2929 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 23.1 |
| beeaf956-b6a0-31eb-b700-88abd8d59b9a | -22.36367 | -49.29762 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 1cf1cfab-14f7-3cf4-a0bb-3d1d46a94732 | -22.36269 | -49.30241 | 2024-10-02 03:57:00 | NOAA-20 | PIRATININGA | SÃO PAULO | Brasil | 3539400 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |


[Clique aqui para ver as próximas entradas](README79.md)
