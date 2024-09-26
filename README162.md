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

## Dados Diários - Página 162

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cd1ac01b-d88b-3e7b-944d-363ff6730b81 | -9.09977 | -61.33805 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf067a17-df8d-387a-ac44-131ad4e8da11 | -9.09921 | -61.3421 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f1ce5e6e-619f-3b05-aa27-d9f9ebb2459a | -9.09888 | -61.31288 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2efac0b3-3594-3087-8d5c-6e5cbb0cbde4 | -9.09832 | -61.31696 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 37daf96b-d9fd-33bc-a938-dc8f35d6f50a | -9.07381 | -61.36745 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28158974-e8c0-3618-8f60-df2659a7a856 | -9.07325 | -61.37154 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b73ff1be-f1db-33b9-8ac4-53552dcf515e | -9.07268 | -61.37564 | 2024-09-26 05:46:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| ef0b6e65-4176-31b6-b6fc-1844789ef986 | -9.4323 | -65.442 | 2024-09-26 05:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 7c77191d-3945-31a1-8476-20a3b493d151 | -9.4322 | -65.4607 | 2024-09-26 05:46:01 | GOES-16 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 16ff9e7a-273a-307d-be0b-825fc78ae078 | -11.26 | -65.2801 | 2024-09-26 05:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 61.3 |
| 0f4abeeb-08ce-3131-aa66-1b817ffe035b | -11.2599 | -65.299 | 2024-09-26 05:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 65.4 |
| 6342eb7b-53ff-3ca2-96e4-be203d1e427e | -11.2788 | -65.2793 | 2024-09-26 05:46:11 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 39.9 |
| 87846294-499d-337e-82a7-9368c52855e6 | -12.67653 | -54.67248 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2e539920-96e2-3064-b78c-12fb341e4f2c | -12.67561 | -54.67264 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 902f4622-7957-3a20-a913-01f7b3fa10e5 | -12.66955 | -54.67191 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4a0921a8-a77e-36bf-871a-2656f398e069 | -12.6688 | -54.67864 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5ba0a54d-d2df-31f4-8480-6126bc2814c2 | -12.66864 | -54.67202 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 35d1f582-9071-34d6-bd9c-9b735553596f | -12.66804 | -54.68544 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b04f285a-fb27-3954-b59a-6c176adfeede | -12.66793 | -54.67878 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 976533ee-44e1-334d-8432-b66717614774 | -12.66722 | -54.6856 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 7f135682-789e-300c-83e4-82a7196c4fc9 | -12.66183 | -54.678 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 23d6431b-cab5-30c5-aaae-e0ac2b1e2003 | -12.66168 | -54.67125 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 173abd05-96f2-3664-a34f-e31d5a61ba02 | -12.66108 | -54.68478 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c974108a-5055-37d9-8838-6c4ff8ad4a77 | -12.66097 | -54.67807 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9bfd77bb-e063-3f35-8f9e-ca40fad4b5cd | -12.66033 | -54.69157 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c6d10b09-2b67-328b-942b-21ef4bb8a8e2 | -12.66027 | -54.68485 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc21436e-f48e-3576-b362-16f1baac89ee | -12.65956 | -54.69166 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa851135-fd41-3a28-9ff1-85277d8ff656 | -12.65416 | -54.68374 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c5740ea6-4de7-318a-86da-66fc0abc07b5 | -12.65335 | -54.68379 | 2024-09-26 05:48:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| eb6ce88d-27cd-38c5-bdea-e063e158a1d0 | -15.85012 | -57.42203 | 2024-09-26 05:48:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d45fddb9-5b4a-3094-aae6-ee0c27faabae | -15.84438 | -57.41784 | 2024-09-26 05:48:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 12364a7f-2c15-30a4-b34b-907dea65e0dc | -15.844 | -57.42144 | 2024-09-26 05:48:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 136cd0bd-6d6e-3a25-adb2-fb8ba18ef32c | -15.83833 | -57.41659 | 2024-09-26 05:48:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| f2526ca1-7b1b-35ca-b7d4-6ea862b97408 | -15.60023 | -56.95609 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 487ffede-5f03-3e24-81d8-e90f462500ea | -15.59984 | -56.95993 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8238a287-7abf-3ef4-b6f4-8ad862f46aa2 | -15.5931 | -56.96383 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0a6f169e-750e-325c-9f86-6323a856ca8d | -15.58928 | -56.93882 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 100ab8ac-0563-3d00-8715-735fdd5ffaa1 | -15.58578 | -56.93777 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| c0abb932-ae51-30b1-81e5-9d3cf2ee8e71 | -15.58351 | -56.93299 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 18ad8b40-b825-3001-a01a-0d46d261b673 | -15.58285 | -56.93955 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 480d627b-c30b-37a1-9281-d9e6ca89fe2f | -15.56011 | -56.94031 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ed93694c-cdbe-33e2-9f0b-95f17c01456c | -15.55432 | -56.93499 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 907f191e-1efb-39f5-b211-50aeeddcb641 | -15.55369 | -56.94088 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4a34e510-d928-32c0-ad16-70a5564fd39f | -15.54791 | -56.93549 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 9ea8ecb0-f976-3398-92ff-28793596e44c | -15.54269 | -56.92469 | 2024-09-26 05:48:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c2a1b958-312e-32b9-aef9-920b4929d722 | -15.35498 | -58.1795 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 888a0318-b107-3f73-9608-74151a5d3392 | -15.35465 | -58.1783 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| b82fd5f3-a89a-3eda-8eb7-3ed6f9f5448c | -15.35463 | -58.18275 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 7be2a7c7-1573-34a5-9666-a79dfe25d3a4 | -15.35426 | -58.18167 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 43e1b04a-ca01-379d-b3f9-ac6ebc14354d | -15.35391 | -58.18481 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c206ac9a-722b-310d-bd15-8f7f8ece811f | -15.34424 | -58.17015 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 619d8d85-66a6-3b98-adb2-8011b9f62aa9 | -15.34401 | -58.16852 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3e40b6ec-132f-3ed7-b4c4-152aa5959a5f | -15.34377 | -58.17458 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e838c2bd-2b92-3585-a535-b25fa8e8b126 | -15.3435 | -58.17303 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f64025af-276a-3a35-b6b3-fc09601cd3d1 | -15.343 | -58.1774 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 15eef8f6-3bb3-3334-afa4-71d03858f07f | -15.33829 | -58.16719 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 443336f5-6b94-3eb7-8c91-489d1e798be1 | -15.31316 | -58.18183 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d11584a-5bc8-38e4-b720-81f9babc7249 | -15.31266 | -58.18628 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 327779db-653f-3a27-9bde-5084a7f134a4 | -15.30795 | -58.17593 | 2024-09-26 05:48:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| a3bf4b66-5689-3298-b5f7-f9b6821377f2 | -12.27472 | -59.21771 | 2024-09-26 05:48:00 | NOAA-20 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 32c89267-1003-3637-9d38-71c471eb9cb7 | -14.50666 | -59.63377 | 2024-09-26 05:48:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d74410bf-16b4-38a2-bd85-e46a05afc202 | -14.45441 | -60.1062 | 2024-09-26 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bf47cbf9-28c1-34a0-8f03-951ee1662c9a | -14.45404 | -60.1092 | 2024-09-26 05:48:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3ec14391-e6d5-3054-b1c8-b316cf3e2776 | -14.42341 | -60.06567 | 2024-09-26 05:48:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5777737a-5b7f-3db3-967f-35c69ef4c8d3 | -12.14766 | -60.91781 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6a11ab76-9544-32d7-bd4e-0b7da4c34ff5 | -12.14303 | -60.91722 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 095dfc15-4bbe-38d1-8ec6-f1f4550c1a37 | -11.95572 | -60.36171 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 6.3 |
| c9f77439-c44e-3b12-acac-684fe82e9ea8 | -11.95503 | -60.36696 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 487165d5-c975-3af8-97d0-137e69dda0e2 | -11.95093 | -60.36107 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 10e8b05e-3f05-3144-8ed7-6c3258dff6fc | -11.95024 | -60.36631 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17444b3e-2680-3c1b-8867-21e45d834420 | -11.93998 | -60.37029 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d194615e-eed0-3295-b463-8445b7a7dd86 | -11.93929 | -60.3756 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 682b3b9c-5f0b-341c-92a0-da41c61c77fe | -13.49659 | -61.27318 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 41df6afb-9079-374e-8423-46cf139d1e5c | -13.49259 | -61.26773 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e48d025e-2bb4-3854-bf37-3d01908196c0 | -13.49138 | -61.27737 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 33684293-93c4-3146-ae79-4caa28080a77 | -13.48799 | -61.26711 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e6938d6b-8952-3692-b742-ca3bcbd735f9 | -13.48618 | -61.28157 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1868dcb8-4ddb-3377-8311-1eafee33bdc3 | -13.48604 | -61.28367 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 6b06ff66-6ab6-358b-92f2-3ecc2bb3dfb7 | -13.48557 | -61.28639 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 9dd85e29-5885-3be8-86c7-354aaef37ce6 | -13.47278 | -61.31404 | 2024-09-26 05:48:00 | NOAA-20 | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d12d73c6-5931-3473-83b2-e4ea59eadd71 | -11.99849 | -63.03841 | 2024-09-26 05:48:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e8f569f-4c9e-3479-9eba-d9a8d8a80bf9 | -11.99449 | -63.03784 | 2024-09-26 05:48:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5279e8a7-a9b5-3e1f-adf9-7494b4af1808 | -11.994 | -63.04136 | 2024-09-26 05:48:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7a6e180-aeee-37af-8d4a-c789b4aa42aa | -12.29575 | -62.31547 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fda3898-d311-3f4a-8fe7-a4a03148e68a | -12.29523 | -62.31938 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d582a095-53ca-316d-a117-5fe9241fe540 | -12.29471 | -62.3233 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ee998492-5b38-359d-91db-719eeac12320 | -12.28156 | -62.32537 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5541c3e4-4362-3e63-8203-e5a8fa8773ad | -12.28103 | -62.3293 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 828a97c4-4ea6-3e8a-a41c-215a29a4c3cf | -12.27735 | -62.32475 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a38e177-855c-35ab-bb7a-38106a7992f2 | -12.27683 | -62.32867 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 98d30162-abaa-333c-9bba-338f09ba33d0 | -12.27631 | -62.33261 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dc22f58a-cb11-3195-b827-a2e28b9063ad | -12.27418 | -62.31633 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ff480a87-dc68-34a6-8548-2582a1e0eb86 | -12.27365 | -62.32026 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ffdc9b39-aef1-3a5f-8dd7-10229028c369 | -12.27314 | -62.32417 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 8be65073-8719-345c-b706-279baeec60e8 | -12.26996 | -62.31578 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0496d62e-b260-320b-8bf8-2b89f9b5b45f | -12.26944 | -62.31971 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 0a03a2be-152f-33e6-a8be-a22afab08f34 | -12.26941 | -62.31628 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 651517a0-4abe-32c4-8de7-daca25ac585b | -12.26886 | -62.3202 | 2024-09-26 05:48:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 0dfcefb8-c127-3f09-bd6b-08960a7c3590 | -12.85029 | -62.69689 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 65352a9c-e830-3083-ba7e-9043466ac6cc | -12.84976 | -62.70069 | 2024-09-26 05:48:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README163.md)
