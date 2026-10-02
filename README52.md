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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1cd42950-36b6-32cb-9be2-2e7b38d37260 | -7.74829 | -54.79708 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a460b371-fd5e-3a49-9bc1-541790d1568e | -8.21364 | -54.71911 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5fd94829-ef27-3e73-9e2b-f2d56a7c00b9 | -3.28675 | -53.84519 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.7 |
| 6b030920-75d9-39e8-add4-08ea93ee1437 | -4.35808 | -47.77518 | 2026-10-02 04:57:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef2cc05-4b25-35e8-92ce-5ee98b766d54 | -6.66554 | -55.08591 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4935781d-7eb8-3070-a965-3bda493942f2 | -8.25928 | -54.72978 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00e429e7-bf2c-3b56-ba3a-637a075ff9cd | -4.28136 | -50.76126 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08568e92-d432-3df1-a6e0-efa98def3cae | -6.18259 | -52.89846 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 84176ec1-26c0-3272-8f04-03cc157095a3 | -6.24396 | -53.13852 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b4f96593-4ef5-30ee-946a-35224f8ba9e9 | -6.40295 | -55.24044 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d522f75-73ac-3549-8d03-58aa4b973411 | -3.1138 | -50.28321 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf185537-4609-3cec-baf4-e6d5b3b5306f | -3.18597 | -54.10038 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| c0c658c6-2494-349b-935b-9fdad051885c | -7.49469 | -55.00451 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 411bd457-5057-35c2-8cfc-f0285f450bf1 | -2.89947 | -54.1468 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 64a49e00-50d7-3bf1-9748-6e112af3ee49 | -5.87531 | -53.49911 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| effe1c81-e2b5-336c-8670-b29ceb4b3b60 | -1.60273 | -55.13224 | 2026-10-02 04:57:00 | NOAA-21 | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6af2ce2c-556e-3896-b907-bbde1105dcc3 | -5.37277 | -56.03516 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e5c12bb7-6881-3fe5-98e9-24a4db3152ce | -3.02068 | -54.1974 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0d69e0b3-08dc-3efa-942b-6128bcb33d53 | -1.44639 | -48.92905 | 2026-10-02 04:57:00 | NOAA-21 | PONTA DE PEDRAS | PARÁ | Brasil | 1505700 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| e1139397-dd46-3f7c-b6bf-6bc4d0d60737 | -2.89873 | -54.08672 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ae1f48f3-cfa8-36a9-86f1-0f66d950d201 | -7.28043 | -55.58896 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 13c6e1e6-2845-3faf-839f-1ed4a2b5bbf6 | -7.18227 | -52.62664 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ea153d08-7871-39e6-ba19-d8dc404385bc | -6.31884 | -54.77888 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3a397fa-8541-3b41-b502-2b44563726c4 | -8.91442 | -49.26265 | 2026-10-02 04:57:00 | NOAA-21 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 9d80eeec-6bb6-345c-a0c3-595e1f4c455a | -3.22404 | -54.31108 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e9c6b36d-922b-3bc0-a855-f86fb9165d98 | -7.6345 | -55.04855 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1248fff4-214b-3abb-8adc-efb31bf44a5b | -8.20048 | -54.73829 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4f7f5546-9370-316b-b924-02c2cc1ecb01 | -2.11172 | -49.00217 | 2026-10-02 04:57:00 | NOAA-21 | IGARAPÉ-MIRI | PARÁ | Brasil | 1503309 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 83e9f7f1-4747-33e7-8584-b9e860c87979 | -3.12302 | -50.27413 | 2026-10-02 04:57:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d08758-ca3b-3bfe-9e22-90cfa4398338 | -2.93148 | -48.75276 | 2026-10-02 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4cc8af2a-b8f0-3ff3-8eec-3bbe61c64297 | -3.16171 | -54.07878 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06beb360-bae2-39e0-b8f2-3f77ca829d08 | -6.68458 | -55.33192 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dccf0664-133b-36f6-9f00-cf79dedce264 | -5.97072 | -55.36957 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b7a6fb35-d824-3f5c-94a4-b529a2416040 | -7.40714 | -55.58369 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ff3c1b0-335f-3466-8f1e-f2287c0e0716 | -5.90304 | -53.49606 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b99776ae-a1cf-3145-b35e-16789642fa56 | -4.69103 | -55.79679 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 405586b6-2672-3d2f-8366-2175b985d121 | -2.0459 | -56.87014 | 2026-10-02 04:57:00 | NOAA-21 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 27633bb7-ca75-32fc-8c6f-dc2b418c7745 | -7.50125 | -54.98426 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a7381b77-3033-3840-aeb5-05b48ee33e03 | -6.1046 | -55.68212 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ba91a915-ba34-39da-a2ac-6421e8e87a44 | -7.0574 | -55.62202 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 51156b18-95a6-35aa-836b-abb22358d31c | -7.03905 | -55.63002 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7065da3b-702e-3297-9488-ec0f8a54ec44 | -3.68929 | -55.48761 | 2026-10-02 04:57:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6a5d6f20-f96b-331e-913b-3a19d79f2046 | -5.87584 | -53.49566 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 24d5d908-7986-31f5-9995-a5b0eeabc33a | -7.54869 | -55.03141 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18cad9bc-cd7f-3b38-bf1b-f7e4e1eff7a5 | -7.84916 | -56.61101 | 2026-10-02 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bc8382a0-91c2-36dd-8f8f-1abc67e70a98 | -3.28016 | -53.84417 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 94c6e04c-19ba-32a1-a898-8c23a96f0528 | -6.70893 | -44.83596 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f7dea9de-b951-3cbf-b064-cb8472fed892 | -8.10473 | -55.34832 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a3ebe2c-1525-3375-8e7e-3429c490c413 | -6.87725 | -55.55381 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7adbb575-b645-3c2f-82c7-7682d67d7a3f | -3.29718 | -53.84328 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4ea1ad26-8d7a-3fca-bba7-662ef2949a8a | -4.69181 | -55.74824 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1c9799f6-de05-3cfd-a21e-2fbd2f3c5da3 | -6.43033 | -52.70256 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 15198fc6-325e-3eb7-a553-b4ff8c8bdd67 | -6.24379 | -43.77801 | 2026-10-02 04:57:00 | NOAA-21 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 66bf93fd-157d-34cf-8f7d-4f68a2484773 | -4.00003 | -48.40151 | 2026-10-02 04:57:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f94c1124-5fe3-35a1-89db-b172793ceeed | -4.89554 | -48.3744 | 2026-10-02 04:57:00 | NOAA-21 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 22314aab-89a3-3bf9-af28-58f86474fd01 | -7.72345 | -54.76132 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f03c1d03-6dd5-3d77-9132-7aeef2556093 | -6.07889 | -53.30446 | 2026-10-02 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e439667b-0f47-33c9-8671-9cbeae4d0a70 | -3.27146 | -54.00794 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d9e0570-1752-32f1-b288-05f4fcd75c37 | -4.27464 | -50.78144 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 133b4b3c-3046-3ba1-b5ff-bfba8b6e8579 | -5.87146 | -53.50204 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d39076b1-f98c-3d86-bdd7-5c2dbb2339b9 | -3.16064 | -54.08566 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b534cc66-d146-3529-b718-8a233a4fb089 | -4.27603 | -50.74769 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c8cb5919-3b9a-3af3-a518-2cd3869521a1 | -3.47118 | -54.62373 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 08c46bfd-4216-35f5-90c6-2a84157b822f | -8.16418 | -54.74961 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cef24038-73d0-3f06-b5da-45f89466e989 | -8.06267 | -54.83287 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9307b1d8-67cd-346a-96e0-270226f5aa34 | -4.38567 | -54.82468 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 470f603e-32fa-3566-94ef-26e14c30a7e7 | -8.08211 | -54.8856 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d29e43ab-b9b1-3b31-b3d9-25aeb31b4449 | -3.142 | -59.0173 | 2026-10-02 04:57:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 328da6ac-4334-33e1-b072-1b657dfa0177 | -6.09384 | -47.66942 | 2026-10-02 04:57:00 | NOAA-21 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 73c46fd7-725a-3f85-99bf-8a13e7691eba | -7.82718 | -55.1222 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 800aff36-d513-35bb-bcc4-2a177413a5a3 | -4.26758 | -50.75488 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d3fde5c6-5a61-3229-bc38-949280179669 | -3.85451 | -54.21964 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b4eb33e4-672d-3d1d-9835-0cd6dc1808fd | -6.22081 | -47.47443 | 2026-10-02 04:57:00 | NOAA-21 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6b45bd11-c66a-3c83-99b1-e3913eb7d621 | -4.28731 | -50.77069 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c727c004-9f5d-35f1-a110-b7d98e6ce1be | -2.90425 | -54.09462 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0a6ef5b7-97b7-307a-9873-ececcd27da40 | -7.29596 | -55.59862 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d6d69136-ecf8-3a60-bf68-5686277a7412 | -7.72453 | -54.7544 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 756b68f5-2614-3a7f-8275-e6e276f251bf | -2.90203 | -54.08723 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| aa35a73a-e022-3d80-ab5e-50872eabdc40 | -2.89819 | -54.09016 | 2026-10-02 04:57:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e656b1e-5dd0-3d94-902c-e659f27965c9 | -7.71919 | -54.81023 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60666600-89f8-37d2-bfb3-f9fb6f9865f0 | -3.58619 | -52.21992 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10d1fac6-01ca-3f83-a17d-328eb0aacd39 | -8.38445 | -46.29557 | 2026-10-02 04:57:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 5d6319c8-a16d-3566-a5c3-14df0c736012 | -7.28265 | -55.59651 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7d8638ab-0a5f-387a-b77d-a97685ea3c4c | -8.41369 | -47.63642 | 2026-10-02 04:57:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 70d9d9e2-dcc0-380f-9e9b-7218422225bf | -7.72579 | -54.81126 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c966fc35-8fe6-3d6c-849a-05f612482511 | -5.14072 | -49.86604 | 2026-10-02 04:57:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5791c45e-d7cf-3f25-9ddf-c7a810ca354e | -5.86089 | -53.48259 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fe0d150a-da9e-3ff0-9da0-e89d5fb83a44 | -3.16625 | -49.00991 | 2026-10-02 04:57:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 10e91a4c-ee2d-39a9-be43-cd76d40ffe17 | -2.90601 | -54.12663 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 89392fca-2200-3347-ae77-c444a31a3f56 | -3.67888 | -54.40772 | 2026-10-02 04:57:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2085703b-c382-3316-9038-d2b97fb6dc3b | -3.07115 | -54.37587 | 2026-10-02 04:57:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 53c464cc-ed99-3d90-906c-c2b03c7f3393 | -8.06159 | -54.83979 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 2ac7890f-8d4d-328d-b975-d2df441d727b | -5.08623 | -50.92938 | 2026-10-02 04:57:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fadabed0-55cb-3d02-8010-46e56e979dc4 | -1.9753 | -54.26827 | 2026-10-02 04:57:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8acc9f63-77df-3f32-8006-cddd4653ea1d | -7.38818 | -55.20813 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5c8d51c-877b-3001-838f-0c27cef286b3 | -5.37551 | -56.0621 | 2026-10-02 04:57:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1103f841-4aec-339b-9314-d897f43e7a3a | -7.8327 | -55.13018 | 2026-10-02 04:57:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97fdf2e5-fa16-3767-ac92-68099e2103ec | -2.89724 | -54.1394 | 2026-10-02 04:57:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73767989-e83b-321f-a971-d9e426a13889 | -6.36069 | -55.14085 | 2026-10-02 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6a0ec43-7802-3cda-b67d-94d78ba35b5a | -4.27541 | -50.75181 | 2026-10-02 04:57:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README53.md)
