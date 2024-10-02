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

## Dados Diários - Página 92

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 74806482-5da7-35bf-8baa-846e6e5ab234 | -6.23384 | -53.33118 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| eebf076f-aafa-3ee3-8f50-a93a48e56d67 | -6.23321 | -53.33504 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 170f8712-b4b3-3c29-9d5e-96e4d4b73f50 | -6.0779 | -53.35791 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a5fcd07e-d016-35ab-898b-a5fd30525db2 | -6.07727 | -53.36176 | 2024-10-02 04:46:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9a515790-0f2f-344f-9821-07dbb69b239e | -8.70637 | -54.82039 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ed877d16-b6b2-3101-86ab-0cb3df3d7037 | -8.70344 | -54.81564 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 235e5c9b-bbc2-3518-a3b2-1440805f67cf | -8.69401 | -54.80531 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4ae550d1-9309-3d96-ae64-0f04d3375e1f | -8.69328 | -54.8097 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df8642a3-46a5-35c5-9943-53805e45fafe | -8.69037 | -54.80485 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d008427d-8bdb-3cce-8209-be453eb72ab8 | -8.68965 | -54.80917 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36d595c4-5b80-378e-a055-c87d284d0f71 | -9.69135 | -53.68077 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3348ba48-7d43-32d2-96bc-2f456d96ad57 | -9.67451 | -53.65504 | 2024-10-02 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 32898e0a-d33e-3716-b9fb-6ec3e24966a8 | -9.63776 | -53.58027 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 61e33cb6-7914-36bf-8a63-87e837b782f1 | -9.63253 | -53.59088 | 2024-10-02 04:46:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0d3acb9-65c1-37ac-a28f-41c27df766ba | -10.63651 | -54.09306 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4dbde341-4d60-3dc0-b658-5a4c08478744 | -10.6337 | -54.08871 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1e10bd65-be37-337a-a2ea-b3721e3b8d74 | -10.62054 | -54.06344 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c83463c0-581a-3501-b728-1f2e0b5bd13a | -10.61772 | -54.05909 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfb16d27-9317-3518-8f3b-782207d944ce | -10.61711 | -54.06287 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0d7ab175-7d1c-366c-a8a2-9f6fe2f64e91 | -10.61368 | -54.0623 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 23bfdea1-afde-331c-b20e-12809adfd714 | -10.23578 | -54.24462 | 2024-10-02 04:46:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 406b3416-3f00-3406-ad59-30d5439bf831 | -10.99997 | -54.25825 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e1e893c6-c174-3533-b48a-851035cc39e7 | -10.8792 | -54.68659 | 2024-10-02 04:46:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 7b506d19-9ba5-3ba0-b92f-328622bd9b9d | -8.95357 | -64.36156 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6189a3fb-1386-3f5e-95cf-fd6659770e7b | -8.94696 | -64.36033 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6af6b51d-c394-332d-9760-070dd501ed62 | -7.40232 | -55.50556 | 2024-10-02 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 656dc59f-d839-33b4-b147-03d014090b7a | -8.3265 | -55.11684 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 31499078-de30-386f-8590-444a07ba3e9f | -8.19364 | -55.16931 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 70a63840-a310-3ea4-8f91-42f406815940 | -8.93156 | -54.93378 | 2024-10-02 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 747427c2-16b1-3f3e-98eb-3e8aa93e0587 | -9.69386 | -55.4996 | 2024-10-02 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e4b9d38-68dd-357d-9701-27ba420d09de | -9.57857 | -56.02143 | 2024-10-02 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9d345539-546f-332c-8153-b185b7580fb6 | -9.57394 | -56.02549 | 2024-10-02 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d74e1b73-a097-38be-88aa-4f823b06e0c8 | -10.62643 | -55.87558 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 2652be07-cc69-3216-8706-0b415b8369ed | -10.62566 | -55.88014 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7510664b-2200-3036-bc4f-17f80eae41e1 | -10.62488 | -55.88474 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3f76eba8-fc3f-33d7-84f2-544ce24f6b3d | -10.62192 | -55.87954 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ee38632b-9bdc-3b86-b4aa-66c3ecc885db | -10.62114 | -55.88416 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7a8fbd91-bdaf-3ff4-8fdd-3125e8530e43 | -10.61817 | -55.87894 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 2f1bd5c2-1254-385c-ab74-f3d43631c231 | -10.61739 | -55.88356 | 2024-10-02 04:46:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7eea7a7d-c797-3135-a08b-4eb73fe83716 | -10.00148 | -55.38873 | 2024-10-02 04:46:00 | NOAA-21 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 01907bdc-8d1c-38a8-87ec-f763163b93a2 | -6.85773 | -56.68207 | 2024-10-02 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 8daaa297-8385-3edd-969e-160d1b09bf6a | -10.33163 | -57.50501 | 2024-10-02 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 445afe9a-be75-3f89-b326-dd9eda1b9ca6 | -10.33096 | -57.50884 | 2024-10-02 04:46:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 99ee1a06-1bcf-3682-932e-ba3a52a63977 | -10.13266 | -56.76654 | 2024-10-02 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 112a662a-3a9e-3de6-abde-d638e351e314 | -10.12988 | -56.7589 | 2024-10-02 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3351b2b-163b-3b5a-8dbd-e89bb3322e99 | -10.12928 | -56.76239 | 2024-10-02 04:46:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 193043a4-9ae3-319e-95c4-6f30fb662aa7 | -9.76015 | -57.78897 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d8362332-1e1a-346c-b10b-66f4a50d4c21 | -9.75944 | -57.79308 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 49da1c75-0c4e-3ea3-bd99-78f73d5b435b | -9.71298 | -57.93326 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fc06bd93-6252-3934-b946-4b04fa2aa544 | -6.97841 | -59.09428 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d31bd62b-e331-3b10-aa45-d87d884f97df | -6.97744 | -59.09981 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9aa24243-7024-37de-831c-3e03cf8406c5 | -6.97352 | -59.09348 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d75eb00-69ca-33c4-bbbf-072ec2c6a084 | -6.97254 | -59.099 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 47a3a8b3-b33f-3e34-a996-93a096529577 | -9.20246 | -58.20971 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 53cbcaa3-9799-389f-8fa8-d8c0b072535e | -9.19803 | -58.20898 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1960fcdc-53bc-384b-8d2a-25487a0eab87 | -9.19516 | -58.19938 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 86910b5c-433a-3957-b334-2593dd743f07 | -9.19438 | -58.20382 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0d81229d-1651-3511-b02e-07331f0b59bc | -9.19073 | -58.19864 | 2024-10-02 04:46:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3f7563ef-ab5c-3a9b-966c-229fb0f89128 | -9.70914 | -58.4432 | 2024-10-02 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e53659d9-bb04-39c2-bbbb-c43d934d2300 | -9.70834 | -58.4477 | 2024-10-02 04:46:00 | NOAA-21 | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0de9509c-7594-3c0d-b188-d49cc2bbae84 | -9.56719 | -59.10164 | 2024-10-02 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b2f7c28c-441c-32cc-8373-baffceb6b012 | -3.17419 | -58.96838 | 2024-10-02 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4f0544c4-05db-3d72-b710-8944ae07da6e | -6.98545 | -59.93574 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| ec109374-b693-3593-8e8b-fa9885e39309 | -6.9849 | -59.93889 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 61c7b8a4-2cad-39ef-a7da-2eba33816802 | -6.92079 | -59.99899 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ae30f474-a2c9-3731-bc2e-187e1454ac1c | -6.9156 | -59.99801 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5c33cab0-e12c-35c6-a4d8-3a6f3dab0137 | -6.71834 | -59.1284 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e752b88a-8465-381c-8bc6-3cf2e2abbd22 | -6.71564 | -59.12535 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 34395c77-34f0-3362-a08c-c19d246e37be | -6.71465 | -59.1309 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 4a2e7e7a-83e3-3884-ada9-293a1fae2083 | -6.71343 | -59.12745 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 35e7748c-8f52-35ae-ae30-2b6651c340a2 | -6.71247 | -59.13305 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 05fca41b-d660-32d3-ab37-0b2aa85fe272 | -6.70974 | -59.12997 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c52d2035-159c-3375-b2c7-3f87924c8fa5 | -6.70757 | -59.1321 | 2024-10-02 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 66e7876c-4727-3e37-8c30-424ff988a93d | -9.93095 | -59.93167 | 2024-10-02 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 06d3399a-0524-35f1-926b-94e90471ebd4 | -9.92872 | -59.92714 | 2024-10-02 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e02c3d89-c12c-37b3-af56-f8af2fb5be05 | -9.92618 | -59.90177 | 2024-10-02 04:46:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| defbc9d2-87b3-399d-8961-2c85243ab1ae | -9.84971 | -60.74481 | 2024-10-02 04:46:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bf8f3add-70fd-3aeb-8d9c-a2e1bf781d1f | -9.8451 | -60.74067 | 2024-10-02 04:46:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4959d920-604e-3c1f-a138-c01b3c0d5498 | -9.84451 | -60.74389 | 2024-10-02 04:46:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d441a88-2def-3c20-9306-4d5131b91a2f | -9.84317 | -60.78018 | 2024-10-02 04:46:00 | NOAA-21 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 275107dc-29c8-340b-80b7-1b3dc1a6c51b | -9.39411 | -61.04503 | 2024-10-02 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 897335a0-cd0b-3ba1-8c4a-30792cac0144 | -9.39348 | -61.04844 | 2024-10-02 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 13384a9e-c300-37c5-8dbd-ba9379cda52b | -9.39286 | -61.05185 | 2024-10-02 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 5fc0a394-6dd2-398a-ab6b-b3785529406d | -8.55935 | -62.48056 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fe52895a-dcc0-320b-bb20-61ae2cabfc7b | -8.55853 | -62.48493 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e6fbd47-04cd-3365-861f-9d333da6a174 | -9.27756 | -62.16706 | 2024-10-02 04:46:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 411e49ac-5d4b-3193-b98d-db657efdadaa | -8.6991 | -62.81736 | 2024-10-02 04:46:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 47691f52-c92e-3d67-9d7c-2584690fcee5 | -8.49233 | -62.70485 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 24bce9c9-1cdc-3a0c-83a2-eb375f76448d | -8.48544 | -62.7083 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 38f57ede-56c0-3709-b1d2-d01e5790fab6 | -8.47941 | -62.70719 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16e1430b-41cd-3a07-9bcc-0a88e20ee774 | -8.47854 | -62.71173 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a5b7791-8716-3d8b-aeaa-7588edaae4a2 | -8.47592 | -62.72552 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 911eaee8-a91e-3f60-babe-46d8872bcc72 | -8.47076 | -62.71978 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 6.6 |
| d710966f-7018-3ddf-a154-286666aa08f3 | -8.46993 | -62.71643 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5b9cef2e-cb2c-342b-abf7-7e4d395f0e56 | -8.46988 | -62.7244 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0d8a8d67-4474-3b64-84c0-cf5f6c517a37 | -8.46909 | -62.72099 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 90681a84-4b1e-366f-9acc-fdf2984596d7 | -8.469 | -62.72904 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d6e7cb36-217c-39ec-8d4e-5c189a66930d | -8.46824 | -62.72566 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f7e28600-ce0e-35e9-8bd8-4113ab91366e | -8.46558 | -62.7142 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 60049182-378d-39f0-902d-19c175073a90 | -8.46472 | -62.7187 | 2024-10-02 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |


[Clique aqui para ver as próximas entradas](README93.md)
