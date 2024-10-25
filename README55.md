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

## Dados Diários - Página 55

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d4c06d1c-e4e4-3481-9e9c-b00514604f4e | -7.42404 | -47.37548 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cded3f1-939b-3b48-8f77-1ac4603afefa | -7.36995 | -47.23063 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8d0cd2bc-457c-329a-9fcc-83c9f1a262d4 | -7.3494 | -46.9882 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9cbc3692-ee30-3f3c-93b2-1df96220232c | -7.27908 | -47.18979 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b96f865-5419-372f-bfb3-40e2f3e28901 | -7.27848 | -47.19365 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| da50b4d1-ad08-3368-832a-4e17e19b5569 | -7.24272 | -46.95706 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3afcc794-f253-3bcb-a58e-7d17f44ba3fe | -7.19256 | -46.95425 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 11298c18-95d0-3e8b-90e0-84fc9e5cf05b | -7.18904 | -46.95374 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 511f5fc2-5e74-3b76-958e-40c37bbe4a76 | -7.18843 | -46.9577 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bf35602f-7a07-3229-b36d-4aa70f463cdf | -7.18782 | -46.96167 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 23047103-a768-3449-84a0-f15d4df31458 | -7.18722 | -46.96564 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ff7e9cf2-089d-31f8-b0c5-2ee76a5121b7 | -7.18429 | -46.96123 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d9b65d7e-fa22-3fea-92f7-39557a78a298 | -7.13544 | -47.06959 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 669a5fd3-90ec-3732-a23e-7805f2b18e26 | -7.123 | -47.19855 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80ae3028-a76d-3b94-a594-9cb232611b2e | -7.12243 | -47.20231 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5377db0d-9c4b-35d4-987a-65df528bbd48 | -7.11951 | -47.19805 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71d7d78f-9e88-3e63-a86c-4a986392733e | -7.11507 | -46.85058 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 195afcc4-5ae8-33a7-b6b1-ce6188b3c4a3 | -6.99356 | -47.38642 | 2024-10-25 04:38:00 | NPP-375D | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0fb90ee4-814e-3006-aa0a-3620cd3836e4 | -6.82171 | -46.78789 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 85cd4224-3ea5-373e-a3d6-c426bdf659cf | -6.81818 | -46.78735 | 2024-10-25 04:38:00 | NPP-375D | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99b23d71-fa9b-3f2e-9d70-85014c0c70e9 | -6.66824 | -47.11213 | 2024-10-25 04:38:00 | NPP-375D | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| bfb0f535-fce1-39a1-9b54-f6c14706c37a | -9.27652 | -48.2612 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| e13bd7a5-0e1b-3b7f-8a0c-988f1a9cd1f9 | -9.25041 | -48.31747 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eeed4525-7157-309c-8980-6edc01f46845 | -9.24985 | -48.32116 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 68d08dfb-874c-3989-8ef7-9fdfd1fdda70 | -9.247 | -48.31694 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d7ce7abd-b8d2-3690-9fbf-ab54d31aa805 | -9.24644 | -48.32063 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 58fb920f-5ffe-3745-bbcc-29bddd5548e0 | -9.24587 | -48.32432 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7821b5b4-8b18-308d-ba85-027b2238007b | -9.2419 | -48.32747 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7ae493a8-7e21-3ccd-b255-a51a5d431afd | -9.23049 | -48.28797 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 435dc254-c51a-367c-bc7e-2d35918bba3b | -9.03565 | -48.71708 | 2024-10-25 04:38:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8699f0f-dc3a-3157-a9b7-9dc124466ec0 | -9.03228 | -48.71656 | 2024-10-25 04:38:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6c312372-d057-3070-8d3c-7cf550de16aa | -8.909 | -48.53872 | 2024-10-25 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| a0440b32-d2a0-320b-a9f7-c4e63f199453 | -8.90844 | -48.54234 | 2024-10-25 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 7.6 |
| dda75061-4643-3070-ba5b-51eb1f859a46 | -8.90506 | -48.54179 | 2024-10-25 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f4f32611-fc6c-3afa-9b8d-bb7ffe6408f7 | -8.56116 | -48.14975 | 2024-10-25 04:38:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6fb4ec15-4660-3fe9-897a-63bd474a7b76 | -9.03619 | -48.71352 | 2024-10-25 04:38:00 | NPP-375D | COLMÉIA | TOCANTINS | Brasil | 1716703 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fb8acd54-a58b-3a3e-a03a-f4b23c598945 | -8.90563 | -48.53817 | 2024-10-25 04:38:00 | NPP-375D | GUARAÍ | TOCANTINS | Brasil | 1709302 | 17 | 33 | nan | nan | nan | Amazônia | 9.6 |
| defd3f97-322c-33bd-a2d4-7e3cd17b291a | -9.29145 | -48.25145 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 74c9bee7-b730-3142-ad5c-534c70717641 | -9.24531 | -48.328 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8b5fafb8-ad4e-3cb5-8ece-eac59bd99424 | -9.24303 | -48.32011 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| abdb32b3-b513-3656-a7d0-e0cd65badb76 | -9.22993 | -48.29166 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1aed0e99-360e-3625-9704-dc4ff3d8cdb1 | -9.10382 | -47.65207 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0876b255-8bf7-3950-828d-f0dae4f20baf | -9.0766 | -47.99488 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1673f4a4-28d6-3d2d-8c5b-799b8661fbd1 | -9.07373 | -47.9906 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a64e9acb-32ae-3017-80fb-0facb08148ea | -9.07316 | -47.99435 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7be980de-647d-31a9-8600-ab2e86eeab5c | -9.06915 | -47.99758 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c03b9565-8180-38df-824b-d310671a4add | -9.06857 | -48.00133 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc228d5d-75e9-3473-98dd-c929774dd2d2 | -9.04659 | -47.81991 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6a3e6469-c230-374f-bd9d-b1212720151e | -9.04313 | -47.81939 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2f8f94fa-1c6b-3923-a160-d067a4ff6341 | -9.01869 | -47.75722 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56b3fe51-1f86-3a66-a2f6-df75ff0f103f | -9.01522 | -47.75669 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5abe5de2-930d-3b12-a10e-c8d43b374a37 | -8.95792 | -47.64164 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| aff35516-0974-3111-979c-d35c5719e01e | -8.95506 | -47.22858 | 2024-10-25 04:38:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46c158e6-00e5-35dd-98e7-ea4d26053382 | -8.95501 | -47.63724 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 1654ae10-71a8-398f-b691-80020e5d6259 | -8.91264 | -47.72227 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 11dbb1d3-dd33-3a8b-a973-50ecd9298d84 | -8.82338 | -47.93753 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cca53ae6-21ca-3fc8-8519-bf0e65a2f79a | -8.81994 | -47.93701 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| df7e6479-0052-3455-aff6-ca4179cb0d02 | -8.80962 | -47.93542 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4d50886e-7cb6-3635-aefe-b69c2711567e | -8.66873 | -47.97271 | 2024-10-25 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e35e5a1d-3c99-378d-8c29-18d48bc0d397 | -8.46717 | -47.80819 | 2024-10-25 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8a325fad-0300-3bce-8e64-e376a2e3edd2 | -9.27016 | -47.91094 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| ff83b586-04ae-34d9-9332-7de8b725e264 | -9.2667 | -47.91042 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8e47dddd-15a3-341c-aaab-64689e83c27d | -9.26613 | -47.9142 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 24cd87fd-b324-33a7-a122-5a3a3242b768 | -9.20925 | -47.78536 | 2024-10-25 04:38:00 | NPP-375D | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8094d15-a58d-359a-a99e-9dcc56ebf9eb | -9.07717 | -47.99112 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6e3201cc-adfc-33e2-9445-4b06cf2184ea | -9.07259 | -47.9981 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| c5606428-5812-3152-853b-755f92a498b1 | -9.07201 | -48.00185 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| bf23360f-dfeb-3a3f-9ba5-f9df6c36067c | -9.03967 | -47.81887 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37c6389e-de3e-34c1-83e3-2f249b15473b | -8.9585 | -47.63779 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| bcecd6db-cfd2-3315-91cf-3bd1e35f13ff | -8.95444 | -47.6411 | 2024-10-25 04:38:00 | NPP-375D | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 0614d0b5-fb76-3882-bd4c-82f32ec74d4f | -8.91206 | -47.72609 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42e8fded-ff09-3340-a6fb-c21542e83901 | -8.90917 | -47.72174 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 9aee2d32-16e5-3218-a493-6683ff1d7abd | -8.90859 | -47.72558 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0fa26a07-bbd9-35d2-85ad-b17c5067bb8f | -8.81306 | -47.93596 | 2024-10-25 04:38:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9e031cfa-f13c-3203-bee3-ba715e2d3e4e | -8.67336 | -47.87377 | 2024-10-25 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 23ce0dca-72a1-3dc8-8892-90c7915417b8 | -8.46659 | -47.81197 | 2024-10-25 04:38:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f6b8afdb-df4d-3334-a47d-5858fafafaa1 | -9.93824 | -48.8779 | 2024-10-25 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ae5dd101-c899-397f-99af-71f910a7a011 | -9.93542 | -48.87375 | 2024-10-25 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19d8cb9f-9586-33b1-acb0-77885108e046 | -9.93486 | -48.87737 | 2024-10-25 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 8611df93-703e-344f-8c53-c67c6391f192 | -9.91984 | -48.13509 | 2024-10-25 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9653895d-95a8-36b8-8798-7c94896c3fa2 | -9.91636 | -48.9078 | 2024-10-25 04:38:00 | NPP-375D | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| df869194-b88b-310e-a5ab-2af5a93a5d85 | -9.8711 | -48.20114 | 2024-10-25 04:38:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 68692d62-9ae7-3ddd-b528-eccc5167c6f3 | -9.85001 | -48.56964 | 2024-10-25 04:38:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1756e6aa-27ba-3836-be5e-fe27f3cdfcdd | -9.60353 | -48.87822 | 2024-10-25 04:38:00 | NPP-375D | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 34656b23-22c7-3a6d-aa6b-f03e4d1728ec | -9.95519 | -47.94895 | 2024-10-25 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 10db1d20-48aa-37ff-875c-b7a0d547f60c | -9.71475 | -47.6603 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b48b5456-e012-337a-9ee7-9381e2b4dac1 | -9.58265 | -47.67361 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 46ac4cab-f7fb-3fe8-8086-f944747d7370 | -9.55633 | -47.72925 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bad42412-7ada-35a4-8745-aa07fe6f3166 | -9.53724 | -47.61865 | 2024-10-25 04:38:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 58bdb958-a1d1-301d-91e9-ba49568ec2af | -10.30003 | -47.66778 | 2024-10-25 04:38:00 | NPP-375D | SANTA TEREZA DO TOCANTINS | TOCANTINS | Brasil | 1719004 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ae7a234f-a386-3d65-84b8-aae8e88179f2 | -10.17776 | -47.90695 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 681b2d5c-d4f9-3206-84ff-6ae60a184d93 | -10.17717 | -47.91085 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 655358d2-6831-3b70-9dbd-e6dd0d0a0b8d | -10.17428 | -47.90641 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 720b9c8e-489d-3756-a898-272d40a4aa1d | -10.10997 | -48.19094 | 2024-10-25 04:38:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5140f733-6dd9-372e-a716-824e0f81ce3e | -10.05705 | -48.0584 | 2024-10-25 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cd03f4f-fc25-3587-ab24-db71f69f19c4 | -10.05646 | -48.06226 | 2024-10-25 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 77da0f97-b027-38d3-88cc-4deb5a42e492 | -10.053 | -48.06174 | 2024-10-25 04:38:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9f799a32-6e20-3c50-aeea-6d9533303d63 | -10.02753 | -47.47019 | 2024-10-25 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e846303b-ab13-3630-babb-30b214b5133e | -10.02105 | -47.46507 | 2024-10-25 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fabfa805-3091-3e17-801c-df3c16f8d050 | -10.02045 | -47.46907 | 2024-10-25 04:38:00 | NPP-375D | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |


[Clique aqui para ver as próximas entradas](README56.md)
