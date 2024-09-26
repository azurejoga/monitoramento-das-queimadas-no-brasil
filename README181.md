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

## Dados Diários - Página 181

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 70c310a5-4f4d-3dfe-b564-136b264d6556 | -9.72355 | -53.20247 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 2e0beef2-841d-38c2-8fc5-81649e853d31 | -9.61173 | -53.26547 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5f447c0c-4cdd-3bcf-ad2d-ac604161eec5 | -9.56576 | -53.39576 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e9196f34-7797-3d31-b0bf-c02140e87773 | -9.56447 | -53.40469 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 8e85c0e9-0fd3-3918-9ff5-f2d4618b1f46 | -10.45424 | -53.3108 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 20.6 |
| 0b2affa4-101d-3806-9177-803fd05d27d5 | -10.4162 | -52.93028 | 2024-09-26 13:08:00 | TERRA_M-T | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 80eb8f8d-5164-31cb-925f-a1901b8b26c7 | -10.28939 | -53.03872 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| ec07c206-549a-38be-8eff-a51818d8c488 | -10.04585 | -53.45035 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 170.2 |
| 2483db95-f31f-3bd7-b713-f34661bd9f0e | -10.04455 | -53.4593 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 116.7 |
| 0413ada7-d47d-3143-a3d7-06f4d4d566dc | -10.04326 | -53.46825 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 31.8 |
| ab73cda2-f892-33fd-bae2-25d145a39189 | -10.04197 | -53.4772 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 100.9 |
| 0c4e1e7d-5d8f-34ae-8e7a-7e2f0e445259 | -10.04068 | -53.48615 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 793.6 |
| 45872d65-2887-39e1-bade-1de8150c19a6 | -10.03938 | -53.49509 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 174.6 |
| 0edddf33-17e7-38f8-9ccb-a86ab604353d | -10.03697 | -53.44908 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 791.9 |
| bc04b6eb-c8c5-371e-bb77-b668192a9302 | -10.03568 | -53.45803 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 333.6 |
| d7015569-8ff1-381f-964e-a5f3839b65a1 | -10.03439 | -53.46698 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 180.8 |
| 6b2c034c-d71b-3727-a55a-c6cb626779f1 | -10.0331 | -53.47593 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 111.9 |
| 59905c03-53f6-3c41-9654-a91fb879c2d0 | -10.0318 | -53.48488 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 377.4 |
| 24992020-6e34-3687-9473-feac20abf187 | -10.03051 | -53.49382 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 75.3 |
| 9935bc87-ad81-3f53-8507-8cb2e3be5ded | -10.02681 | -53.45676 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 06a99e8b-850d-3bee-a6e6-0474f7bc53f6 | -10.81608 | -53.73597 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 9ec0e2c7-f2e7-3443-bf7d-c0b440e7b09e | -6.20741 | -53.29183 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 2715ec16-bfa3-3e31-a739-5630f108ea75 | -9.17625 | -54.67347 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| f5bede54-291c-30f5-beff-21deb57de9d3 | -8.71419 | -54.80434 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.3 |
| d544a823-a480-3798-938e-b2d624e50261 | -8.70648 | -54.79361 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 2f3f7ab2-8b4e-3016-a826-a0080820bc8c | -8.69874 | -54.78307 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.4 |
| 301ac5d7-a074-3f9c-b5d3-424feabf4732 | -8.69735 | -54.7924 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 19.1 |
| b9bcc104-12e8-3b33-93d1-12b21d991e3a | -8.5269 | -54.57339 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| c97e43fa-c78c-34cf-ad96-dd6eadaf93c5 | -8.57773 | -53.34086 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| fea340ee-bca8-3c06-9215-004b365e680a | -8.57644 | -53.34976 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 7f8d195b-ebee-3829-b447-d55752adee58 | -9.66429 | -54.2435 | 2024-09-26 13:08:00 | TERRA_M-T | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 4d904fff-bac2-3127-b5ce-9ef3c19c2cdf | -9.56413 | -54.04137 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ecb7ea6e-5615-315a-889d-06c664c874bb | -10.58864 | -54.22866 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ad99819b-747f-3c4e-a486-400f712b1390 | -10.58732 | -54.23767 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.1 |
| 74bd58fd-50a7-3ff3-8d0e-e83322b94357 | -10.57678 | -54.23888 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 883155f8-2d8b-3e77-aadf-d27e130ce921 | -10.0824 | -54.59644 | 2024-09-26 13:08:00 | TERRA_M-T | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 13c6ae51-4397-39ec-b9f6-295315004ab1 | -9.78536 | -53.6012 | 2024-09-26 13:08:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 22.6 |
| 7ee16a04-eff2-3c91-bf8d-5a834a5fca99 | -11.67255 | -54.44421 | 2024-09-26 13:08:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1d82e5e4-34aa-3140-9477-aaa6f83962ea | -11.67123 | -54.45326 | 2024-09-26 13:08:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| 9ee77fde-1801-3b1e-8ae8-b3b0a4638d4f | -11.6699 | -54.46232 | 2024-09-26 13:08:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 9cdbca7e-758f-3d09-8ecd-2c431b03feec | -11.39741 | -54.17603 | 2024-09-26 13:08:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.5 |
| ca8cb198-8788-3a79-bae5-7ac7b593b326 | -11.21293 | -54.74469 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| adcb7bde-6bbc-37d7-a678-16a68a8c3618 | -11.21024 | -54.763 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 107.3 |
| 18134c58-19f1-33bd-8d3e-ee924aaafee5 | -11.20888 | -54.77218 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 619.3 |
| 02d7e93d-e642-38d4-91c8-dce2a5e975d2 | -11.20753 | -54.78138 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.0 |
| ddf457f3-8746-36e8-8ebc-001bddfcadd2 | -11.20617 | -54.79059 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 21.6 |
| 42b6f046-f6da-3e1d-9677-7dcc7738e29e | -11.20263 | -54.75252 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 6d21f2a0-04b4-3f08-b6c7-fc8f79bbaa8f | -11.20128 | -54.76168 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 472.4 |
| db339d50-051c-31b1-b568-bc9d70576885 | -11.19992 | -54.77085 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 273.4 |
| d0ce591c-d519-364e-b927-3568027f2e6b | -11.19857 | -54.78004 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 46.2 |
| 52e82a1c-8c47-30b1-9b3d-d5451b14aec6 | -11.19802 | -53.90509 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| db287651-c9a7-323c-9c24-4ff491b89c94 | -11.19721 | -54.78924 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 057200e3-bda2-34c9-bcca-28fa69a8f464 | -11.19672 | -53.91407 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| c18e3edd-0ebe-3a14-bf84-5dc3c72a09d0 | -11.19231 | -54.76036 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 23.2 |
| 164978ba-73e7-31e9-9b62-7d0ba65d3438 | -11.19096 | -54.76952 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 24.3 |
| 27204be3-a501-30dc-bb29-45c6a2158eb1 | -10.99388 | -54.16571 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| d45ef12d-c1bd-3633-b32e-42d22f1163cb | -10.93195 | -54.26984 | 2024-09-26 13:08:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 935bce49-c806-36d4-929c-76b765782464 | -7.82068 | -54.73681 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 31.3 |
| 7263ab15-d68c-31b4-bb91-7f5d0f2ceb09 | -7.77991 | -55.12291 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 733eb747-e5b0-310f-8611-9a46808b5553 | -7.77842 | -55.13275 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| c1637567-a91f-32c9-9caf-6fab1d0b5b6a | -7.76658 | -55.66062 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 137c2f69-a7be-3285-8719-6bb9e5902aa8 | -7.76506 | -55.67082 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7782a307-1bde-31e4-b5c3-668fd46428ef | -7.72997 | -55.70852 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 3ae09e6b-8bb4-3090-bf5e-9d2f831a9a9a | -7.60902 | -55.35084 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| d0216c1a-ecc5-3cd9-8288-f93b27987285 | -7.6075 | -55.36097 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 52eea468-3af5-308a-9fbe-22aa96c858b6 | -7.59562 | -55.18449 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 6a5e37fc-c657-38e9-bf0b-3453faf80ad2 | -7.50438 | -55.11408 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 6994323a-1948-3fd4-ac07-4afa09a00e35 | -7.50287 | -55.12405 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 6b6e317a-40e5-3f5d-bda6-5de7f6ade547 | -7.37418 | -55.49217 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 47.0 |
| 116647e7-b3cc-36f8-97ba-3e5e40aee28f | -7.3726 | -55.50257 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| c911b7eb-0f74-39f8-8b5f-2f13a10c7420 | -7.37103 | -55.51293 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 48.7 |
| ae227a7c-133c-3bf4-881f-cc2c794090f2 | -7.36946 | -55.52332 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 2f36c97e-b8eb-3aa4-bec2-cd5c455c4bc2 | -7.36307 | -55.50115 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 23.7 |
| e33f29a1-24ac-39fa-8c65-f6a93dc92662 | -7.17797 | -55.02105 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| 3529ac27-dd5f-387d-8391-851816b3a552 | -7.17649 | -55.03089 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| b09d0aa2-be7d-39c5-aba4-96a4e3bbe5a9 | -8.51871 | -55.1816 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 22.2 |
| ec423e3c-fe65-3a10-9877-af7610152ca2 | -8.51723 | -55.1914 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 32.7 |
| 6091a9f5-e607-3dbd-9405-a797b0bf4e6b | -8.38129 | -54.93116 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 6076ff6b-f90f-3980-8568-0f2bc6ca2f7f | -8.38014 | -54.81409 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 650b5a92-7cf8-3746-90ba-265c951ff781 | -8.37986 | -54.94073 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 085b920d-837b-3b79-9540-c43c87585003 | -8.35179 | -55.06482 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| b6211214-40e5-38e0-b918-2ce246d2fc8d | -8.35032 | -55.07458 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e7be95ea-f6ac-34b4-9a4a-18ed9af904b8 | -8.31717 | -54.99439 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 38.8 |
| 4f334571-96ba-32df-b5f4-882a29e8f654 | -8.31574 | -55.00406 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 94.8 |
| 4d7980b6-4b3e-3385-8a88-7248f4b3500e | -8.30796 | -54.99307 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 79e2d505-9087-3846-b845-2d4a3fcf1c7f | -8.11545 | -54.79553 | 2024-09-26 13:08:00 | TERRA_M-T | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 11.9 |
| 6e481ac1-e8b5-3a92-9105-aa58ecb9868f | -8.10367 | -55.38335 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| fec17969-e889-33c5-8f56-7326518bb1c1 | -7.92617 | -55.76118 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| a5279759-27aa-307b-999e-a119eeeec764 | -10.50051 | -55.32169 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 7227f9c8-af54-3e2c-a683-741a9861651e | -9.69693 | -55.50916 | 2024-09-26 13:08:00 | TERRA_M-T | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 7.8 |
| abd2d6c4-ea51-39a2-b200-a3a7d9971e3d | -9.06169 | -57.11264 | 2024-09-26 13:08:00 | TERRA_M-T | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 8affd2bb-b7de-375f-8a72-dcef8f69677e | -8.34676 | -56.5047 | 2024-09-26 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 33.6 |
| f1c52cb4-42e3-3ac8-8ee3-343a2e9e0ba2 | -8.34498 | -56.51631 | 2024-09-26 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 07e8b165-699a-307d-be26-179aa1992552 | -8.33676 | -56.50309 | 2024-09-26 13:08:00 | TERRA_M-T | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5cff195f-4c41-3f82-a256-73a5cc3dec9f | -10.41397 | -57.58401 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 43984d36-7275-3edc-8030-d80ca23574dd | -10.3008 | -57.25992 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| e70290d5-fc4c-3e17-9598-0969875dd6a7 | -10.29894 | -57.27201 | 2024-09-26 13:08:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| c7132a74-b370-3a29-9317-d8aeaa9f98d6 | -10.27478 | -57.60926 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 0ab83ffd-babc-3ca1-aae5-c5043ad27f71 | -9.61668 | -57.75722 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 33.4 |
| d4ead933-533a-3881-9b6c-010b8dbbb439 | -9.61457 | -57.77056 | 2024-09-26 13:08:00 | TERRA_M-T | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 16.9 |


[Clique aqui para ver as próximas entradas](README182.md)
