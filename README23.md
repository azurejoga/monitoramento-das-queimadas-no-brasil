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

## Dados Diários - Página 23

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 77dda721-3a86-324a-9211-b4881b987864 | -4.06006 | -46.91032 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 89e70575-4522-3f5b-a2c9-1cdb5983d344 | -4.06816 | -47.10357 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3d7a894-4559-387d-844b-9e23cce7a5d7 | -3.76855 | -47.15798 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a53f419c-979c-3913-b311-8513921ec91e | -3.77156 | -47.16284 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cd4c0421-be4d-31da-a4ae-259c84a6d586 | -4.04393 | -47.01556 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 932747af-342b-3988-a5f7-f26b20e1e1b6 | -3.30238 | -53.37405 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| fc0aa63e-4ee6-30fa-ae21-20a567ccff84 | -4.12948 | -54.89761 | 2024-12-17 04:44:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bd633868-fc84-3147-8151-74cd0459f865 | -2.73899 | -47.83657 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46269a4b-6e5e-3459-b365-df6af16d1d96 | -3.15499 | -53.18118 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 9bf1fe3e-bce7-30dc-bac8-cd2a487dada4 | -4.12 | -43.56906 | 2024-12-17 04:44:00 | NPP-375D | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d84912d3-4de9-3a75-9d31-e03b684e6ed7 | -4.96138 | -43.71525 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a6d4b6f1-8c6c-328c-95e6-1956665d277c | -5.10097 | -43.90904 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| c1093832-48e7-3813-9de9-471297904504 | -3.92258 | -46.92746 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 69d20591-65d1-33d5-9077-9d06121e6be8 | -5.08643 | -43.91198 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f85fe80e-26a0-3d15-9bd4-dfd607c6384d | -4.06072 | -46.906 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7545ca47-c9fe-3b35-988e-475a6c8d5fad | -4.38174 | -46.55053 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 5a85c0b3-3748-30d9-9368-62bbe0b3cc2f | -4.02704 | -46.97712 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9227cb97-37d7-361e-b84f-6d0db32a4d15 | -3.29715 | -53.36052 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b305f5c4-1727-348a-a70a-86c885888f1d | -3.7679 | -47.16228 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d39a7856-ba18-39f3-a609-014cecb5adc0 | -3.29584 | -53.36877 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e21a7af2-2279-30e8-af7f-d281b7e10e02 | -1.52054 | -46.05003 | 2024-12-17 04:44:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7d78077-f4bb-319f-bc52-1a0ca7ac5735 | -5.09636 | -43.90844 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 19b8c501-470b-3aa3-a321-f06e1b2fcb36 | -3.2965 | -53.36462 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5011f022-b6df-3f95-9c0a-25b356aec1a8 | -3.15207 | -53.17657 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 34d8898c-c767-3e94-81b9-334a3570962f | -5.09032 | -43.91432 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 20.1 |
| a0e14c1f-abdb-3e3b-83cd-b01bf75897ff | -4.06146 | -47.09813 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 02eff26b-5915-3a50-abfe-e10463f39a64 | -3.68752 | -47.15162 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c41ee5dd-3b5a-3921-aeab-16734c3ae048 | -4.67628 | -44.03738 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8b2697b7-4972-3095-a767-b0c6f60b0069 | -3.92256 | -45.44094 | 2024-12-17 04:44:00 | NPP-375D | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 97bf9af1-acad-3ba6-a26e-8258032c26c9 | -4.09701 | -46.7192 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 351b8335-4767-38a6-8188-7d70e1b6f61d | -2.84463 | -52.57328 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 21080fd6-c272-3038-8e6d-439f47504ed4 | -3.01593 | -48.02708 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a94fdb7-f424-35de-8789-f2f504e2019d | -4.10499 | -46.6924 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1dc5976-d9a5-3901-9df9-fab9905fac63 | -4.70231 | -44.38467 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9431569-e9f0-3af2-9e03-6134898a3516 | -5.29658 | -44.93471 | 2024-12-17 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8ee12f83-af0f-3fa8-acc2-deb553b0133b | -4.39846 | -44.87983 | 2024-12-17 04:44:00 | NPP-375D | LAGO DO JUNCO | MARANHÃO | Brasil | 2105807 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8582e31e-4fb1-37a2-8cae-e1728adf6632 | -3.26767 | -53.08752 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8d218d3f-8403-3617-9ad6-6a780edc7400 | -3.30074 | -53.36111 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1cb39e88-006f-3abb-86f6-bd1b1a03c823 | -3.87665 | -47.04265 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5888da8-0e2b-3c89-92ce-a4ce88f50388 | -3.12059 | -52.7009 | 2024-12-17 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7080884c-0ed8-373c-9098-f91428a868cd | -4.01665 | -46.89481 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 46bb5238-5861-398e-bb09-729967e8b56a | -4.02038 | -46.89539 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a94f02a7-fe60-3e4c-9c2f-4b9c69813338 | -4.24777 | -45.99694 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 646966b0-f9ee-3902-b5f8-a96f49b705be | -4.40007 | -41.43106 | 2024-12-17 04:44:00 | NPP-375D | PEDRO II | PIAUÍ | Brasil | 2207900 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 8392c068-a0b5-32de-86b7-cc7799ac58b4 | -5.11374 | -43.20014 | 2024-12-17 04:44:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 8f000234-72ae-37df-bc30-c9327e78567a | -6.09065 | -46.66504 | 2024-12-17 04:44:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a571556b-a06d-30be-9153-6e5382cee6e0 | -4.92983 | -43.96197 | 2024-12-17 04:44:00 | NPP-375D | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 40b0a111-6b22-3313-a3db-7772a7bec74a | -4.05938 | -46.91471 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 33984ad1-dcfd-3808-8466-117e1e05da1a | -5.09165 | -43.90495 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 842eac1c-84e4-3563-a2e0-ea84cc5511b2 | -4.56907 | -46.58311 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1d145020-9db3-3a01-8f54-dfecfead353a | -5.0956 | -43.91021 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 1884c9d2-012e-3c8b-91ac-0f8a8ef4ea20 | -3.87086 | -47.04414 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18346192-a26e-3607-bfbc-6baf7adf2b1f | -4.07554 | -47.10469 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 66bcb175-f9bf-3fca-acda-287b6068a7b6 | -4.70675 | -44.38525 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0cf785ce-a610-3b8d-9fa6-fe86addb4388 | -3.4375 | -45.60451 | 2024-12-17 04:44:00 | NPP-375D | GOVERNADOR NEWTON BELLO | MARANHÃO | Brasil | 2104651 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2dcb6ff0-386c-3493-b1e8-10acfe519795 | -3.13898 | -48.60465 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa557a67-b3f2-36a4-91a8-6e80af3ae824 | -3.7854 | -47.12117 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 676b49a1-f569-31c6-9ab8-44532e6fd082 | -6.03131 | -42.15271 | 2024-12-17 04:44:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| c02aa890-2897-30fc-8caf-7683649e0b82 | -0.79659 | -52.34367 | 2024-12-17 04:44:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0aa206fc-4ccf-3261-8866-08d15bc4c265 | -5.09174 | -43.90787 | 2024-12-17 04:44:00 | NPP-375D | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 23.6 |
| d3b9101f-1bdf-32ab-baa7-bb8bb65a8850 | -4.03025 | -46.90574 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 75235c63-25db-3d70-bd45-f75eab6f765b | -4.37651 | -46.54679 | 2024-12-17 04:44:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 92f16924-99ad-30ac-a7db-313abd2d7579 | -1.28428 | -53.19026 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2d866274-78df-3576-acda-2e9bcf70013d | -4.06836 | -47.46215 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94c0aa98-4b75-36ca-b830-d8d9e07252f7 | -1.40775 | -47.47528 | 2024-12-17 04:44:00 | NPP-375D | SANTA MARIA DO PARÁ | PARÁ | Brasil | 1506609 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bae9d29f-2cbb-3776-95d1-174557b68bed | -1.6319 | -45.85551 | 2024-12-17 04:44:00 | NPP-375D | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f415d325-ff44-3ed5-aebe-33c2cf2962e0 | -3.89491 | -47.10953 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 41205c18-9a24-3fed-b958-eb3daf8a7530 | -1.29749 | -47.7454 | 2024-12-17 04:44:00 | NPP-375D | SÃO FRANCISCO DO PARÁ | PARÁ | Brasil | 1507409 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0783779e-0f0d-31b9-be1f-0bdfdf7475a9 | -5.6794 | -46.50531 | 2024-12-17 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d4bc463d-881a-3f61-b1c8-015cfda71bbf | -4.70563 | -44.38293 | 2024-12-17 04:44:00 | NPP-375D | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 24523d4f-d21b-372b-a8cb-6b96741d9a2d | -2.57342 | -49.41079 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 012b27df-0a9b-310b-8bc9-422f4821bd17 | -3.99444 | -44.16961 | 2024-12-17 04:44:00 | NPP-375D | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2d74a536-146e-3332-b2cd-38fea26caca4 | -4.02447 | -47.04379 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd6ad63a-bfd6-382f-aa66-645881ea740f | -3.08673 | -47.78012 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b8e0c810-1d29-37d9-88c3-36d925c665e8 | -4.02192 | -46.8088 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 217e0b24-8f77-3b64-aa81-c26d5a8aea1c | -3.89416 | -47.18838 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| db78da43-a3c0-3b57-a613-d7485de1a326 | -3.96719 | -47.03218 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| caceb8d8-a005-313a-be99-06e29558a069 | -4.78939 | -46.39817 | 2024-12-17 04:44:00 | NPP-375D | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 11.4 |
| e83c9c99-4704-3d2c-be7a-1561c57aaee8 | -4.02811 | -46.86942 | 2024-12-17 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 16030ade-3c9a-3c77-a1c0-42c53427ae67 | -3.04187 | -47.95231 | 2024-12-17 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e15ee92-6377-3fc5-b71b-d2cf8acc450a | -3.30861 | -53.36515 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 312f8520-49aa-3d18-988a-db5685ada4a8 | -3.29943 | -53.36935 | 2024-12-17 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f67a8d8f-7d6e-3e86-b5b9-e3e1b67ee571 | -4.51723 | -47.94079 | 2024-12-17 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef5743d0-2714-30b1-b177-102b180b205f | -4.57994 | -47.08841 | 2024-12-17 04:44:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8942e57d-d357-3b3b-8500-e148b65be235 | -3.78369 | -47.10772 | 2024-12-17 04:44:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc1d5767-97d9-33ee-ac92-ad02afd05ba6 | -5.20848 | -44.55975 | 2024-12-17 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d54d69e5-835f-34e1-8697-3a76f0ed9023 | -2.57677 | -49.4113 | 2024-12-17 04:44:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 695c56a4-5d2c-34f6-a40f-56c4a9edb52b | -3.95678 | -47.02612 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2512600-0948-3928-9767-9f36f08037bb | -3.86848 | -47.03487 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 3d6d3b3f-e367-3d2d-b4bc-8d5a68a519d1 | -4.04754 | -46.9174 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 56c4b13e-726a-3d72-abfa-2db019a33a6c | -3.99535 | -46.57522 | 2024-12-17 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 441bda4c-72ba-3634-879a-c1288fb20403 | -1.37924 | -53.4819 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 06f5e472-d5cd-3f35-b477-b91e9c5296d0 | -2.74249 | -47.83712 | 2024-12-17 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11baf8c2-5302-33db-a936-39381bee14b3 | -1.46146 | -53.4798 | 2024-12-17 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e694b407-00aa-3b38-964b-50e69afbb3eb | -3.9788 | -48.39093 | 2024-12-17 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 082bfccb-240d-3439-b8f7-cac72bf7f6ad | -3.28006 | -48.81977 | 2024-12-17 04:44:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e9bfa628-7c93-377e-8c61-db46b62d5df0 | -1.28456 | -53.18883 | 2024-12-17 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 88aeac51-2546-370c-9d18-0097e1113de4 | -6.03085 | -42.15598 | 2024-12-17 04:44:00 | NPP-375D | SÃO FÉLIX DO PIAUÍ | PIAUÍ | Brasil | 2209609 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| f572d288-abbe-31ba-b3e1-d6db65588b00 | -4.24677 | -45.9941 | 2024-12-17 04:44:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c94178b0-5494-3d6d-a0ac-73f13574bdc2 | -4.11395 | -47.18837 | 2024-12-17 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README24.md)
