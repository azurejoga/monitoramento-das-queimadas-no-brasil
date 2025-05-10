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
| 01ec8d10-9936-324c-8126-195a63cd93e8 | -12.64435 | -54.06671 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ecdaefa0-7204-3b92-aa74-e701f39adb76 | -11.66094 | -58.26662 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8c0f875f-9fa4-300e-9523-a8cfbbf95ffb | -11.38588 | -52.93865 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8f3e9ee4-b1ed-34d0-8b9f-f7c51e9b6f5a | -12.36669 | -63.92403 | 2025-05-10 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 97335c00-1f0d-34e1-aa00-c1d8ad01c195 | -13.97443 | -56.80719 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| f76b33cd-3bfb-395f-b259-0d20ddf05f63 | -12.64418 | -54.0696 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86266e31-e2e6-32c1-9115-97853dc7a097 | -12.64883 | -54.06512 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8aec66b5-43d5-3bfa-a913-1363d2e62ddf | -13.24993 | -50.12924 | 2025-05-10 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 9761ab28-e7f3-3bad-9aab-2cca1e1cd29a | -11.14917 | -48.67214 | 2025-05-10 05:10:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c64e63bc-ee61-3f71-bc2d-81784a9f8d01 | -13.09456 | -52.29094 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d762ee5-f81c-32aa-9323-f8781acf739e | -12.37138 | -63.92117 | 2025-05-10 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f95f225-479a-36ee-b168-3d76d3f7a365 | -13.37627 | -54.26339 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12dcf17f-7f67-32ff-a5a3-a1c3bef87a9d | -10.64299 | -44.48672 | 2025-05-10 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 191cb633-034b-35be-9f3a-217d0f542565 | -12.64042 | -54.06613 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7331b2c4-4324-35f0-a006-3f9eb4aa4697 | -10.98714 | -44.44777 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 083de369-68fa-3a21-8e90-593fb04d1460 | -11.14229 | -54.2295 | 2025-05-10 05:10:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c9cec3a-1f24-35b8-b7cb-6b2e978ce96e | -12.35823 | -54.52191 | 2025-05-10 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fc6af42f-286e-39e0-8e58-90887e2e9008 | -13.98063 | -56.80367 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 02bab9d3-4813-3b80-8b23-ff6fec963b62 | -11.77915 | -48.69748 | 2025-05-10 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a1aedad4-e3c1-3049-baa8-d338d10a9906 | -11.14872 | -48.67576 | 2025-05-10 05:10:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6627ba54-73ff-3de4-b4c1-a9e957824e50 | -7.89056 | -61.46348 | 2025-05-10 05:10:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1cf1783d-93e5-3571-b59a-651055569bb1 | -14.64789 | -45.14027 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b26264f9-82ae-3a6a-8aa3-c70bb59081ef | -12.68748 | -58.12688 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 575ff0e0-b49f-3204-a3fa-92c97019e1ba | -14.31438 | -54.64851 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5d614d66-1a0a-3100-8619-0ea86f61fe3d | -13.9795 | -56.8114 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| f0d151db-76ee-39ee-9b58-41b11f14c14f | -12.6908 | -58.12742 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8120125e-17a8-345d-b771-95ee9f393da8 | -14.64523 | -45.12449 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 0f6b465a-7dbf-3921-bd4f-29c2895b106a | -10.97051 | -44.43957 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c25efad1-e920-3199-8919-e7a12b4b47b7 | -13.98006 | -56.80753 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 17.7 |
| 773cb400-5474-3a73-adb2-407731f3c43c | -12.72728 | -54.97454 | 2025-05-10 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8034031f-5ad5-3b02-9daa-e467b645e377 | -11.97545 | -63.53211 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3ca1f3af-5aa8-35b0-956c-c84291687013 | -12.37201 | -63.91754 | 2025-05-10 05:10:00 | NOAA-20 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a8beb0b-71fe-327f-9e3f-fa7aa3d43559 | -9.48831 | -62.35474 | 2025-05-10 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e353e1d8-0558-3e0e-9de4-bcb454c7743d | -13.24954 | -50.13235 | 2025-05-10 05:10:00 | NOAA-20 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 12.9 |
| e9c34766-7269-3d3c-b8a8-a3322ad6609f | -10.98484 | -44.44099 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9db47c77-3b44-30f6-ac5c-dc226f5f97d5 | -12.64897 | -54.06222 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 70294069-0c30-3c9e-afa5-d58eab19fd2c | -13.62265 | -54.88578 | 2025-05-10 05:10:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90ce207b-7687-30ba-a025-04309fc0b0d0 | -11.39003 | -52.93922 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b9d6424-d0fc-3744-aaaf-4df2c5a9e5c9 | -10.9736 | -44.43919 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6ed8da76-7bd4-3a71-a90b-4f894e7bef79 | -11.40141 | -52.94859 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8f9c65b-cc6b-31f5-ac02-d179da563c9d | -13.09272 | -52.29713 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5b81f2ca-b322-38e2-be9d-02135af14b4a | -13.98194 | -56.80436 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5306bf03-6ebc-3041-b04d-9b6bc912d56b | -12.76553 | -47.98909 | 2025-05-10 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 71b2ea79-c43b-3146-b893-b97a8eca38a5 | -10.82125 | -56.95626 | 2025-05-10 05:10:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 835cf7d5-786f-3a7e-9d1e-ffddca759c98 | -12.64828 | -54.06729 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 33147ae1-f689-3e0e-9e36-8c32924da08d | -8.47219 | -49.61559 | 2025-05-10 05:10:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0c4e0f0c-9e8d-3da4-b72e-008c4ced78a7 | -13.97501 | -56.80332 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 27251dd9-45de-335f-82f0-17561d45895f | -8.69288 | -64.14351 | 2025-05-10 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b68030ac-aa2d-3fa1-8316-53b07da41ff1 | -12.72605 | -54.9723 | 2025-05-10 05:10:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 0d4c110a-d8a1-3df7-9465-c8370888147e | -9.49285 | -63.58743 | 2025-05-10 05:10:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 59089a0b-a341-32c2-97b5-4ce6c30d58fb | -13.98136 | -56.80823 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| d0806ece-76a0-3568-9d0d-417893a20cb8 | -11.40345 | -52.94714 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b8eebe25-6638-3328-afdb-60682c0d0b39 | -12.6324 | -54.06784 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f287162-b05d-3264-b211-05ca2cbf5691 | -14.64218 | -45.12516 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a910b8ca-3337-3520-b700-5bc6cdb7966b | -14.64861 | -45.13309 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a4da319a-320e-3f9c-a640-bf1b7e3b5b8f | -13.37695 | -54.25836 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 99fd8eb1-1a32-311f-b25f-4bee1e706253 | -12.69025 | -58.13097 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2bca1b90-7951-3f58-ae73-cbe3cf98fc82 | -13.04699 | -53.722 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 009315fd-a573-3c35-a0b7-25f05606f408 | -13.04294 | -53.72146 | 2025-05-10 05:10:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 64d7dc73-872d-3c00-b217-bb4d04e82a25 | -11.77359 | -48.69674 | 2025-05-10 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63a58737-5831-3c16-ab20-dc1238f61019 | -13.37589 | -54.26747 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3e9baf5e-2aa7-35e8-9f4d-53937dcbf23f | -14.64456 | -45.13168 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4b036887-b90e-38a4-86d0-62ffa336a889 | -12.63632 | -54.06843 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4575875-a41a-347d-8b30-8e22962995c7 | -9.16739 | -61.95245 | 2025-05-10 05:10:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cd34d0e9-4b22-3342-9e50-f69f07e56ce2 | -12.6836 | -58.1299 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 62bb8e9b-c179-36a1-92bf-7423197b0ddb | -13.09396 | -52.29538 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5c41b6d8-43e7-3695-ae39-73694ed136ff | -12.76597 | -47.9852 | 2025-05-10 05:10:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 42d150dc-6f40-37ca-86ac-ab9c0b78bbfc | -11.37559 | -55.12254 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c87a7704-f45e-3c7e-9f78-97d5323f62f8 | -11.37622 | -55.11825 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd6f60a3-96ec-3e08-9f3a-705f407b6935 | -12.68416 | -58.1482 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 66023cbf-7852-3692-adce-c33ef37bd61a | -12.63649 | -54.06555 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 25de69d1-2015-32fc-89ab-ea2e68278dcf | -11.61857 | -48.12463 | 2025-05-10 05:10:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c3a98f6b-be05-31bc-82fa-9a09858d7758 | -11.38949 | -52.94305 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5093f1b0-c2e4-31ad-bc54-5ea1143f9bcf | -14.64389 | -45.13887 | 2025-05-10 05:10:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 40741275-748a-3c0d-bba9-fd9e687c9073 | -10.64063 | -44.48032 | 2025-05-10 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdf162cd-d6ef-391f-9afb-a2189a1dbad5 | -9.66818 | -49.71339 | 2025-05-10 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2150856a-c9cb-3488-8e75-83f4bd1d290d | -11.66149 | -58.26311 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9f1c1cd0-b711-3eab-b16a-7cd82edf8dfc | -10.63984 | -44.48751 | 2025-05-10 05:10:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b030e1cb-591a-3569-a526-8df18c89abc2 | -13.08952 | -52.29475 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 5d83e019-a138-31c8-9ad6-068a185b9d5d | -12.62847 | -54.06725 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c588c5f6-bb2b-3b4b-bf2f-145858f90bab | -9.67323 | -49.71406 | 2025-05-10 05:10:00 | NOAA-20 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a443ee21-9587-3227-af24-0f6cd10be50c | -13.23297 | -56.80322 | 2025-05-10 05:10:00 | NOAA-20 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4880e76a-1ac1-3c89-bc1f-17462a2894ea | -10.98076 | -44.43995 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 86f9eb23-7f10-35c6-bacc-f994eceea832 | -12.68748 | -58.14874 | 2025-05-10 05:10:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 632fc778-028a-3411-8ffb-5c9e7b1b2086 | -12.64025 | -54.06902 | 2025-05-10 05:10:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8834fcfb-d54e-3479-9562-cf8fd860f885 | -11.15423 | -48.67657 | 2025-05-10 05:10:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 16209158-5cf7-3905-ba56-bf60948855ad | -10.65009 | -44.48763 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a4440454-5c4f-3e26-95c7-e9d91cea88df | -10.99202 | -44.44162 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 03fc5fa2-a346-30d6-9697-d8c1c40ac32f | -11.91289 | -54.4015 | 2025-05-10 05:10:00 | NOAA-20 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bc62557e-e8b1-3bba-989b-a1d6a23eb138 | -8.68852 | -64.14272 | 2025-05-10 05:10:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c9b58c0d-ddfc-3924-9226-a972f527c6e8 | -11.77313 | -48.7005 | 2025-05-10 05:10:00 | NOAA-20 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1bcebbf6-c80c-34b4-9743-923dae8b4ffe | -11.37194 | -55.12202 | 2025-05-10 05:10:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ec9c2f07-c492-3e8c-8e97-7ac86d26a189 | -11.40709 | -52.9515 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| bb52772c-f59a-3137-b0c7-6d127504ef56 | -10.51019 | -62.00011 | 2025-05-10 05:10:00 | NOAA-20 | OURO PRETO DO OESTE | RONDÔNIA | Brasil | 1100155 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f8648799-ec2e-367f-8b7b-3b81ec225e4a | -11.3993 | -52.94657 | 2025-05-10 05:10:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 70dc4290-6d55-355b-b347-1ecdd1580834 | -13.9841 | -56.80417 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f6c4038c-bf64-3def-af9f-24a2665c6c65 | -13.09012 | -52.29033 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 219a54da-1769-3b66-b0b5-cf23fbe3a43c | -13.09328 | -52.29267 | 2025-05-10 05:10:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| b71c2ee2-bf9c-342a-9f71-f9a990bf4cc5 | -10.64773 | -44.48129 | 2025-05-10 05:10:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| bdd57e97-c531-3924-ae0e-c0acf5c28f16 | -13.97731 | -56.81158 | 2025-05-10 05:10:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |


[Clique aqui para ver as próximas entradas](README8.md)
