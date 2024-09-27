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

## Dados Diários - Página 117

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9fb2fe0c-dde8-3922-b1da-9bece763d5ed | -11.18925 | -53.90958 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3208d691-182b-3d84-9aa7-8bc8c815467a | -11.18882 | -53.91299 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f4619b2-fd7d-3833-ba08-21677a6b23ef | -11.18838 | -53.91639 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84748ddb-0d10-3e64-bc8c-2ad540faa158 | -11.18794 | -53.91977 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3979ed44-8577-3fe5-ae28-adddb1955143 | -11.13809 | -54.18264 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 94104673-ae62-3534-86ab-b6350d138f26 | -11.13768 | -54.18586 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9607c136-1212-336b-b487-3cbf8b8f9b93 | -11.13246 | -54.18518 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 372c7beb-3aaf-3d55-9a13-3151a3bd7b3a | -11.01397 | -53.94064 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9dab71e1-45cc-34b2-ac6c-bf05ceb7f37e | -11.00867 | -53.93996 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2a2e0a6b-4439-3401-83ce-5d531f86c6aa | -10.9397 | -54.26772 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f22901b9-1e5d-3dae-8bc1-26829b115af6 | -10.93929 | -54.27085 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 45e15c73-8b01-3818-ba2f-84a19a80c7c0 | -10.93494 | -54.26392 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| c5987734-0be7-3b22-8616-e79c662a9528 | -10.93018 | -54.26004 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f5efaec8-02c3-3f0b-a93c-31a679ba1338 | -10.92976 | -54.26323 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| c2f07158-bd66-3bc0-b15d-bdef85352340 | -10.92893 | -54.26958 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| a484d5ac-6c85-3298-b697-f4c9ba3c6680 | -10.92583 | -54.253 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 54370f1e-e9d3-31f9-bf0e-3a47f2fdaea6 | -10.92542 | -54.25617 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 9bb82e56-38a3-3c6a-b3b3-9128ab3e500f | -10.9246 | -54.26246 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| f7affe39-6aa0-34ad-b217-4f09a3778071 | -10.92418 | -54.26562 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 8f669d18-1ae6-341a-ada1-2640e889bb76 | -10.92377 | -54.2688 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 15362696-284f-3017-8090-0cdf28ce9dc4 | -10.92024 | -54.25549 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 05263463-065b-3b4d-9624-e4a8e87e5da5 | -10.91983 | -54.2586 | 2024-09-27 05:27:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 688e0866-cf31-326b-95aa-69e18f010a85 | -12.44846 | -55.00353 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2c7bb6c3-e2bd-3637-9b25-90e8946327e3 | -12.44808 | -55.00647 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 933db140-6752-31ad-b83e-63e623f1f059 | -12.44381 | -54.99994 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6d7f3167-4d56-3315-af4f-a5527d71e2db | -12.44344 | -55.00283 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| c64b0983-0b98-31c8-94fe-27f18094c80f | -12.44306 | -55.00578 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 11f10a57-7345-3358-a819-794e1fdb707d | -12.44957 | -54.99487 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| df021042-5c7d-3782-9eff-5541eecee8c8 | -12.4492 | -54.99775 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 112868e0-14f4-39b9-b604-a0414460f122 | -12.44883 | -55.00063 | 2024-09-27 05:27:00 | NOAA-20 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2df50f46-ee23-3b49-892f-cbe3f96bcc58 | -12.69241 | -54.68591 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 322dd92d-4e57-3acb-8b90-2dd9c3fc299f | -12.69161 | -54.69228 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6d46e87e-719c-3809-86b5-d100325fc69d | -12.68605 | -54.69485 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fee9eb42-ae05-3a0a-9409-8b982105cc7b | -12.68564 | -54.69805 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| ce20f169-c3ad-3e57-8e9c-bee3882bfb99 | -12.68524 | -54.70125 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e8bf8147-1297-3afe-8671-0a8645c282dc | -12.68009 | -54.7006 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1be5cd01-9d49-3dd8-8b88-171ba3765cea | -12.67138 | -54.68654 | 2024-09-27 05:27:00 | NOAA-20 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5287e1b4-0b2e-3ab0-8b15-6668d34f8506 | -7.8663 | -55.51678 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0cde9038-e3f2-3a0d-8f04-6362e9176e32 | -7.72854 | -55.43376 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6022eaea-a816-3e2d-82d8-14bd46fb27cf | -7.69636 | -55.32908 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 88e892e0-ec17-34e7-99c8-e6550cf6dfc3 | -7.69621 | -55.33176 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 934b90de-815f-3687-ac14-adc881aa9fbb | -7.69163 | -55.33102 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ea341719-333c-36df-bb41-aee2b73c83df | -7.69114 | -55.33308 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cbfaf19c-190f-3888-a728-c804e98a92db | -7.67652 | -56.14817 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20633f66-ffd3-3fd0-b765-24c7f4ff2ac0 | -7.62414 | -55.3788 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e1cbedf2-dd77-3714-aa8f-6e8d609a2b14 | -7.61625 | -54.97253 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 572bac77-0012-35b8-bf61-72c9b60e517a | -7.61304 | -55.35803 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ae1d151d-c897-3a7b-a27c-fa9c1a4f9194 | -7.60976 | -55.348 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73ab6f4f-b403-3083-a94b-53af0ce70d83 | -7.60973 | -55.28039 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55b8cb93-1f31-3491-8352-c671ffa6a2ab | -7.60584 | -55.34257 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e1ca390d-df7d-3162-9546-b46c5a7cb01a | -7.60578 | -55.27504 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 53397551-a374-327d-a300-028c07024c1f | -7.60572 | -55.27705 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 54aea7a0-c9ba-3724-bc0b-231e66ad261a | -7.60513 | -55.27974 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ef509b23-d79d-36df-b381-8e2eb7db9396 | -7.60505 | -55.28173 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 60f05f03-f704-31d6-927d-4d3dd07de992 | -7.60212 | -56.04149 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bfbb1839-c311-3b15-b8c8-3168373d30f9 | -7.59964 | -55.18875 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28d2d9b3-1743-35e6-a84f-60c071dfa718 | -7.59779 | -55.1687 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 38dc060f-a066-3b9c-8412-cd539fed9417 | -7.59711 | -55.17349 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 16d92c8b-e2dd-3982-b439-cd2b50c99a39 | -7.59248 | -55.17282 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c810cd8-7fba-3a12-a06e-ac6b4024ef08 | -7.56597 | -55.15976 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 256a4c00-51e5-30ca-a014-0e7bebcf33cd | -7.5653 | -55.16449 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2df811e8-1b79-331d-aa81-9d74d9b170b6 | -7.55683 | -55.12373 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d399c6f5-71ef-3e14-85f8-fe27e424cccc | -7.55613 | -55.12871 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7c66248e-aa57-31be-95d1-e47083779697 | -7.55218 | -55.12307 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0c454f56-4a09-3196-b088-e9623c401c06 | -7.37389 | -55.49767 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 57b8eb27-2940-328d-8135-d0ead2dd36b6 | -7.37326 | -55.50217 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 48f63232-808a-3ec3-aa73-b97c0ba9fedc | -7.29761 | -55.11092 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2023234c-db1f-373d-8b1b-0c0a29645e4e | -7.29627 | -55.11151 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5a1a0922-1eb7-33a9-aa3a-14b4f5c4aee5 | -7.29574 | -55.31894 | 2024-09-27 05:27:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 5912d33a-1d17-3114-a589-f5fa3b1585af | -7.29297 | -55.11032 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 001a9d93-067d-3c90-87e3-8df9320c998f | -7.29227 | -55.11515 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0eed89b1-d426-3379-aaad-e863411e991b | -7.29163 | -55.11093 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 996cf982-c95a-3f06-b9cd-cf3523c25bf9 | -7.19444 | -55.03688 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 76a75ba7-23c2-3881-97b1-7a6b9ec1e7d3 | -7.19085 | -55.03861 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 113b912f-4b85-347d-ad7c-f58212ee8209 | -7.18619 | -55.03799 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9394d5de-3bad-3981-8947-f5f860db747f | -7.1855 | -55.04278 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c2265259-d0c0-3d33-bcd9-e242f69c92dd | -7.18364 | -55.02273 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 68cd12cf-8805-331c-a63c-f363d3f84e6a | -7.18293 | -55.02768 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c6c82266-5342-3f01-8ca8-a19aba7d322c | -7.92982 | -54.72394 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 284dcc59-358f-360a-9b15-f12269aaff68 | -7.92572 | -54.71814 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5cf02d77-2262-344d-847b-09eb268da906 | -7.9209 | -54.71757 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5c352a3-bb25-377d-b01c-379c20246e86 | -7.91609 | -54.71693 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| c797d291-635a-353c-aeef-c75352722079 | -7.88939 | -54.73393 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 88d41bf4-fe58-3f67-a09f-975898256f77 | -7.88921 | -54.73481 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 426da318-e70c-3d22-b7f2-d24ad636d01e | -7.88526 | -54.72857 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| c8a9f752-fbba-32db-b4a8-7d46db78976a | -7.88504 | -54.7295 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 60a7bea6-9713-3ee1-8262-9903148909d8 | -7.82626 | -54.73094 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7f338eeb-387b-31f2-8aeb-166c1dc56ed7 | -7.8256 | -54.73574 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 48e988c4-d433-3d91-b8d7-47937167b685 | -7.82141 | -54.73072 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 405081c6-7066-304f-ba9d-54ca107d4985 | -7.82077 | -54.73534 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fc7477c1-0ed1-3cb4-bd4b-d65d86686186 | -7.82012 | -54.74008 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 22cc101f-e098-325b-9483-318538c41429 | -7.81727 | -54.72529 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1de7776e-0e3c-3baf-9eda-211a06e76f2d | -7.81659 | -54.73021 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| d37a9320-aad4-3f69-ab0a-f0e5786393bb | -7.81245 | -54.72479 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 134b7c23-96ca-3d0e-bcb2-84e0784af80f | -7.81178 | -54.72965 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 8ff2dfea-3dcc-344f-965d-bad7996c1e7a | -7.80919 | -54.71289 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| c5bd78f4-59ad-307d-b545-8af4fd533035 | -7.80839 | -54.71877 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| ce318fb4-be9a-318a-83be-74048aa914d7 | -7.80767 | -54.72403 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 76c04c37-d93c-350d-acee-972cf3bc6231 | -7.80445 | -54.71178 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 7392beca-c355-3d15-be35-94269661dd22 | -7.80364 | -54.71773 | 2024-09-27 05:27:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |


[Clique aqui para ver as próximas entradas](README118.md)
