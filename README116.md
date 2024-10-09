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

## Dados Diários - Página 116

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c845d931-3868-363a-a846-7db1a1ff4a3d | -9.47964 | -48.79834 | 2024-10-09 04:38:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39b7e0b6-2226-355d-b5f4-cc63ea9b9235 | -9.47462 | -52.10088 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e6886a75-6adc-34f6-8e63-0dbde2f29ea2 | -9.47399 | -52.10471 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 69088451-271f-39aa-98c5-8393ff45f2bd | -9.47116 | -52.10029 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 64c696c9-b64d-3386-9ebb-43b970593a8f | -9.4695 | -52.10096 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ba687688-e6a5-3897-a231-169586fb4bda | -9.46771 | -52.09972 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e556661f-55a7-3516-a4a0-d217f770cdd7 | -9.46666 | -52.09655 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8260de9-afc5-3b34-ad1f-e534fb8a06cf | -9.46604 | -52.10039 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c60aa636-0c3a-357b-8192-bc6dbf13520a | -9.44514 | -48.88854 | 2024-10-09 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe1373b9-6803-3996-bec6-69869d4e3980 | -9.43675 | -57.83339 | 2024-10-09 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2cd3ad42-74c1-3204-841e-54e51dcbc71e | -9.43188 | -57.83252 | 2024-10-09 04:38:00 | NPP-375D | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 619cb53e-523b-39c0-a6c1-543f3509fb55 | -9.39909 | -53.20197 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c83febac-e512-3b6c-9bcc-faed6a6e110e | -9.39875 | -53.2027 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 985f482c-dadf-3daa-b611-ff515ba8d2d7 | -9.34017 | -49.85078 | 2024-10-09 04:38:00 | NPP-375D | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b975c972-ce39-32f8-8c2b-e4e4fefe8198 | -9.33549 | -52.54937 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8d578d3a-534e-353a-ad4c-0b7d6fd5aac6 | -9.32126 | -49.40984 | 2024-10-09 04:38:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6a2e2208-9cdd-3240-80aa-787f9f16c018 | -9.31639 | -54.52682 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf730f77-0e77-3c5a-a6a3-87b5e42b06cc | -9.31554 | -54.53175 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 077c6ce2-36a6-3416-8b5d-8853ebd46c05 | -9.31247 | -54.52611 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6d87b3b0-cb25-3096-9462-fe9a9bff0b15 | -9.31162 | -54.53107 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 60abd680-91f1-3c8d-b902-9fd043dab94c | -9.30856 | -54.52544 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 90071b5c-6ef0-32ae-9979-23c7daf0dfd5 | -9.3077 | -54.53044 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 96576d56-aae1-3420-a0f0-41982da891b1 | -9.30685 | -54.5354 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 99737709-547d-314c-8e8e-5e4bb3688ba9 | -9.30378 | -54.5298 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 34004c1f-024b-31df-a569-2234715e03c5 | -9.2649 | -46.75306 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 357d97cf-7fdd-32d1-bb9c-e8d4d73eb5d5 | -9.262 | -46.72236 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 92028835-5e61-3285-9046-f3e3b07da065 | -9.26189 | -46.74833 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 9.2 |
| f070030a-6f7b-370a-a797-dd59055af271 | -9.26127 | -46.75252 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 36.3 |
| 3879f92d-8509-3ec4-91cc-bc919963bb72 | -9.25961 | -46.71332 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a49010e1-9835-364f-b195-d2cb027065f6 | -9.25899 | -46.71755 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ea6290f0-1eee-3a35-b1f0-007e72251b5f | -9.25837 | -46.72179 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| b61203a9-d81b-3239-b447-9061cb812523 | -9.25764 | -46.75195 | 2024-10-09 04:38:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 8ada210b-1186-3c1d-9279-4ea497eaee65 | -9.25238 | -50.36379 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 38a73622-f9a5-3541-b191-90267946d4d6 | -9.24905 | -50.36326 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dd210c61-2f7c-3307-ab08-1a6896117f9e | -9.21122 | -47.95315 | 2024-10-09 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 8b7657c7-ec9a-3d47-9fb3-4b7bf5d76ed7 | -9.21065 | -47.95691 | 2024-10-09 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| cd5790b8-5611-33a9-ae63-5f585fb975a2 | -9.20721 | -47.95636 | 2024-10-09 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 18e28fc2-225b-340a-be65-2b6a2ae7c175 | -9.20636 | -51.4991 | 2024-10-09 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18e3cb42-b01d-34b2-b261-799f5b3aec89 | -9.18617 | -47.69616 | 2024-10-09 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0a66c0ff-4b8d-3196-8d4b-740ae664ebe2 | -9.13166 | -58.90714 | 2024-10-09 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 35c4532f-84d0-398a-b07d-bf50e5434726 | -9.13108 | -58.91035 | 2024-10-09 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b03957c5-1689-3923-b527-6aa418c37d63 | -9.1206 | -50.29588 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 6eaf8446-39eb-34e7-9928-6670e88e6ce5 | -9.11783 | -50.29185 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 751f72db-c62e-318b-b3c2-03b3d74dbcea | -9.11727 | -50.29535 | 2024-10-09 04:38:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 31443c2b-fbf3-33f2-b285-5075f7572c8f | -9.10996 | -51.51332 | 2024-10-09 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 778c0d79-3e41-3adf-aa4e-b86a057ca17b | -9.10342 | -58.97276 | 2024-10-09 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 818da073-e31b-31da-a53c-b9fc8bb6ad44 | -9.10195 | -46.10703 | 2024-10-09 04:38:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f777d02e-1a18-3fa9-b919-184663de210a | -9.09813 | -58.97182 | 2024-10-09 04:38:00 | NPP-375D | COTRIGUAÇU | MATO GROSSO | Brasil | 5103379 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 54f295f2-ccc6-395d-8b18-99714e1be678 | -9.03274 | -51.5158 | 2024-10-09 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 503d929c-7d8d-35d0-b1ef-020118a8593a | -9.02933 | -51.51525 | 2024-10-09 04:38:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 03e1aa72-29fa-3d64-8378-19fa9f732677 | -8.98495 | -52.7926 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b5870480-a798-326f-b191-4ba72e41aeec | -8.98428 | -52.79663 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d2691c31-c2ff-3a65-bb21-691d003fd910 | -8.98359 | -52.80083 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca9d7bd5-b562-355a-b665-10985b27ba6b | -8.98138 | -52.79199 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dab2b835-f1e2-39cd-8d32-30f908ccc592 | -8.98072 | -52.79597 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 08f21df2-fa06-3389-8eb7-715e81e8dbd9 | -8.98002 | -52.80018 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ea365de-62f2-3d0a-a0a2-3cf555e92bc8 | -8.96773 | -52.7856 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c734a99b-0848-38b8-90cd-8621309698ee | -8.96416 | -52.78498 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bbae5af0-ac2c-3072-b72b-452cb6e0b358 | -8.94492 | -52.79018 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0e26568-30b1-3ff9-9bf3-d80eb71572a2 | -8.94424 | -52.79426 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f5116f1-40bf-3021-8d92-d6f00f4019c2 | -8.93998 | -52.79773 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 303914ad-8748-32f6-ace8-e3bf1e9c717e | -8.93572 | -52.80118 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 294435fa-2c37-3c8e-b282-f2f57026b6a4 | -8.92147 | -47.05913 | 2024-10-09 04:38:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f9b04e8c-615a-34a2-92e8-edbcd48f1224 | -8.91391 | -47.91338 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bdc7f0c4-2166-370f-9a5a-6c29047d2ce2 | -8.87522 | -53.05112 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22bd14b2-0831-318e-891d-9ebf39a09168 | -8.86783 | -53.0507 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8a938161-9f26-3409-b21d-243ab467d210 | -8.8668 | -53.0115 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82cf519e-6040-39c0-a857-4e5371261d61 | -8.8661 | -53.01576 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 087b406b-7f90-35a2-9476-6f45d08fc895 | -8.86594 | -52.99404 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6a0e7f5b-e510-329a-8aab-3591afee88e3 | -8.8642 | -53.05013 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f8331a2-16a9-3262-aa4a-0bb6cd488e9e | -8.86319 | -53.01087 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd4a2801-fcab-39a6-9f9c-30bced3b407d | -8.86235 | -52.99331 | 2024-10-09 04:38:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2e7cdb4-73a0-3134-b9ee-81a3bfce09f4 | -8.86167 | -52.99741 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 89809754-8140-3429-a3f6-29edc1d8ba1d | -8.86097 | -53.00171 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b32b2699-1724-3067-9a13-ea113a927dac | -8.74867 | -49.78586 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e82ad374-b7e6-3b19-b819-456330291f90 | -8.74552 | -49.56719 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da877ad1-d3d9-370d-90ff-550500fd7774 | -8.74498 | -49.57069 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfb2304c-ac05-3b63-a5bf-2abefd03a9da | -8.7422 | -49.56667 | 2024-10-09 04:38:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7709226b-96a5-3606-8041-31fdf44da76d | -8.62262 | -54.93273 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d651376d-2ca9-3e07-8f2d-ae28dcd511f7 | -8.61917 | -54.92844 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 456552b5-f3d8-3513-8638-94cb544b4196 | -8.61856 | -54.93202 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 12d0b877-22de-3296-b35f-0d44442d97f1 | -8.56577 | -50.53162 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6ca1db20-2734-3c9a-a0e3-2d1bcbbf1dd6 | -8.56243 | -50.53109 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| aaae766d-9113-3eae-bb94-733ab952759d | -8.55965 | -50.52703 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f1fa95c6-069e-3fd1-85b4-8bb6b86a5a05 | -8.55909 | -50.53055 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e860ddb-a218-3be1-80a1-c5530f33f415 | -8.52687 | -48.7757 | 2024-10-09 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 07274b49-0d60-3b77-8fce-ad144bd824ee | -8.52632 | -48.77924 | 2024-10-09 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5c3f1304-441f-3119-b155-aec48006275c | -8.52406 | -50.02544 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4c2c8c0-1839-35e2-87cf-88673024c4fb | -8.52351 | -50.02893 | 2024-10-09 04:38:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5985ea8f-71a4-3d5f-9465-3498033c786c | -8.52351 | -48.77516 | 2024-10-09 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 702d7412-870a-34e5-af53-be69275fb3ce | -8.52297 | -48.77871 | 2024-10-09 04:38:00 | NPP-375D | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7fa21afe-9063-3cdc-938c-fba31606b2ac | -8.51091 | -55.15435 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e88c5a1c-6641-37ce-ba3b-2202bb7015a2 | -8.50679 | -55.15364 | 2024-10-09 04:38:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bbe1d51d-e812-36da-bade-c1d0e9b36213 | -8.50434 | -55.21871 | 2024-10-09 04:38:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 862fc22d-e649-390a-a9be-ee7a863bdc18 | -8.50327 | -48.1365 | 2024-10-09 04:38:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a682a0ee-3860-3499-99c4-2721d257c5e6 | -8.50118 | -48.64449 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0ebff9e1-8fe1-339a-9f67-3bbae7683b8b | -8.49782 | -48.64397 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 14db896c-834d-3c33-bc22-cab295b55cfa | -8.49726 | -48.64756 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4468ea68-7c33-3ddb-9ae3-de3b7edd2468 | -8.49558 | -48.63627 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 2.7 |
| baadaec3-2bc9-30bb-8221-a3bac9cb070b | -8.49502 | -48.63986 | 2024-10-09 04:38:00 | NPP-375D | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Amazônia | 18.0 |


[Clique aqui para ver as próximas entradas](README117.md)
