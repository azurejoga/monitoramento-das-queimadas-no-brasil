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

## Dados Diários - Página 60

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9e9237fc-79e7-3de2-9044-2ea36dd6927a | -5.5354 | -51.44151 | 2026-10-10 04:44:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1eb527be-01b8-3ee6-952b-f1d436c9fbe4 | -3.18844 | -50.58649 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5b2f4bc4-2e9b-3e8c-8933-88eafbad4aa0 | -3.10147 | -51.36399 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d0acc4b-20e5-34e7-ae60-cce9c29aeb5b | -2.47097 | -56.08452 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86625c68-42bc-38d6-8e3a-63bd1d98caa0 | -3.22626 | -49.43917 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 682a12d8-1003-3c6a-b760-137435a13fa5 | -3.29815 | -53.99472 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 689ac5b8-1dd4-335b-919e-bc66bffccbe0 | -3.34761 | -50.41073 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cae17c12-3c5c-3761-8712-cdee394df53f | -2.50353 | -56.20101 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1ccbb092-4050-36a1-8a18-4647da6e9eb0 | -6.07582 | -44.66057 | 2026-10-10 04:44:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9ee4899-8ad0-3103-a4d4-6c39f563a1af | -5.7472 | -45.13756 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e2cc3df2-c92d-3b2e-9d21-38a0e8644ef1 | -4.45447 | -47.91634 | 2026-10-10 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 27924df8-4528-3f82-af0e-46ded72177e6 | -3.01817 | -54.12519 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01f8cd54-43c9-39e9-8a34-cee4590eafcd | -2.4236 | -57.99941 | 2026-10-10 04:44:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| abce9fb8-2c01-34dc-a425-de23a86f6335 | -5.32259 | -45.20621 | 2026-10-10 04:44:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0999390d-d910-3c8c-bc20-55ad3897afd5 | -3.3483 | -50.40649 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db8d5ddc-8e10-3ce4-827b-c0a64c10d7b6 | -3.03218 | -59.15978 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| beed2c1b-1c9c-35fa-8919-cd2d11947de6 | -4.08936 | -53.99578 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 23a871ba-0a9e-3ea4-9d37-8a5f1c439714 | -1.56135 | -51.6995 | 2026-10-10 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e374d981-d9ce-3293-81fd-276e303f332d | -7.33191 | -43.99027 | 2026-10-10 04:44:00 | NPP-375D | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2e3faf05-d304-3ba1-9ba1-920be75b5042 | -7.07211 | -41.59663 | 2026-10-10 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c5d5bc34-fa36-3bfd-8580-3da8f82cc7f8 | -5.45621 | -44.78509 | 2026-10-10 04:44:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 302889df-89af-33ef-85a5-792681fd0a24 | -5.88517 | -43.40631 | 2026-10-10 04:44:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d72f4122-fcb8-3a0e-9448-b9f4b2514122 | -1.11464 | -54.16545 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ade6c8af-e7f7-3876-9e9a-29dc94f9270e | -7.22464 | -44.17123 | 2026-10-10 04:44:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 66e7556d-589a-30d7-9d2d-7eddf91da76f | -5.08644 | -46.21045 | 2026-10-10 04:44:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d87921be-e436-345a-af87-7b948239e564 | -5.68821 | -53.47421 | 2026-10-10 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fd4a3663-aa32-3657-97a3-8d92f00d689e | -5.60148 | -47.27998 | 2026-10-10 04:44:00 | NPP-375D | DAVINÓPOLIS | MARANHÃO | Brasil | 2103752 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 52c0c3bb-a301-3eb0-be3a-0c94641146d6 | -3.57814 | -54.69239 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 149043a8-c039-313a-a896-f422c592a3a0 | -3.26909 | -50.39136 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8f7bbfe0-38de-303f-a034-73f0c43c103f | -3.30663 | -54.00076 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dd5407d4-cdb3-341c-8cb8-cde118f4a20c | -2.73742 | -54.13182 | 2026-10-10 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1d1feb59-8f00-36fd-a708-e6f35add235e | -3.11661 | -54.17861 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1d19c025-6a92-37b2-8392-fff0c6b07390 | -3.00537 | -51.02063 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 435a88a6-4347-35c5-8881-fb4d8361b4c3 | -6.93479 | -44.5658 | 2026-10-10 04:44:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| aea72d5a-3a65-3a9f-863f-659fe9cdf448 | -1.19393 | -55.66377 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bf39d0c-d271-38cb-9f51-b03ea2e29a37 | -3.30969 | -54.01102 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 73d2ffbf-5e10-3f2e-82b3-58d9b8e7ea9d | -3.11313 | -54.16139 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 69302b3f-6341-3942-aa26-79c598b777ab | -2.47202 | -56.09013 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 72ed4282-831d-359a-a79f-1ae31714a339 | -3.31197 | -54.02604 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75154fc7-0ea3-397a-a922-903aff9389f9 | -3.56826 | -53.00835 | 2026-10-10 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 699e8172-71d2-3a47-923e-dbde3126e3a5 | -3.46224 | -50.58289 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 20a68aa7-4abe-3e65-82cb-fd24b565ac88 | -2.47149 | -56.08125 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3c811ce7-0e12-318a-9194-94e565650c35 | -2.4712 | -56.06226 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fb5ace31-96ef-3b0b-ba91-8af6136e6278 | -3.22665 | -49.4381 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b2b30771-55ed-3e71-a103-4ca8097d190e | -3.55801 | -54.69427 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 441820f4-cbb0-3e0d-a6c5-d8fc5f9f3dbd | -7.1856 | -41.99356 | 2026-10-10 04:44:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| daeb2b2f-5875-3ddc-89e6-e96442176a98 | -1.53486 | -51.60485 | 2026-10-10 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| e86c1b25-534b-3263-b7ee-06b167da0ad1 | -2.31674 | -48.58882 | 2026-10-10 04:44:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4c33798-32f7-3486-8edc-6a391a0f4725 | -3.60044 | -54.58958 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9ccdc0e4-e850-37b2-85f4-c6192298cbfa | -1.89511 | -53.99002 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 75227481-a955-3a3b-8e72-26da7dd81882 | -6.23738 | -44.10401 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 810c708b-9275-32c4-9680-8e9964c85d59 | -7.20751 | -44.33672 | 2026-10-10 04:44:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2b3fd253-c6c9-30a5-92d1-b56d34ac4b85 | -3.60265 | -54.60569 | 2026-10-10 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e3c7f428-a378-3fa0-8b6f-7c9a7b02d952 | -5.09428 | -46.13826 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4255267-b276-3b12-811f-8bf5db548f3d | -1.32497 | -55.45119 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| be39673c-5f74-3d3f-a39d-c41e74489b72 | -3.26474 | -50.39505 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 578ab572-c847-36f5-8c43-725d8b71d809 | -3.20351 | -50.82547 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 531a3df5-2500-3016-9fd8-8a97cd50bb37 | -7.0982 | -41.75595 | 2026-10-10 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 25b4dd8c-992e-35e8-84d7-d695fcddfafc | -3.18878 | -49.24809 | 2026-10-10 04:44:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 97ed6326-8c1d-31f1-b7eb-571b4fe8e987 | -3.18147 | -58.63252 | 2026-10-10 04:44:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9d13e8f4-25af-31b2-8c59-793c0f3ee017 | -5.87623 | -50.0974 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| d52fc044-4e9b-3d37-b8ec-dbe686eb68c7 | -3.17267 | -44.29721 | 2026-10-10 04:44:00 | NPP-375D | SANTA RITA | MARANHÃO | Brasil | 2110203 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0c3d2597-8306-3930-8a69-c31955c19261 | -2.83573 | -54.80944 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 60af97f3-4a45-37f0-9cfd-ab1816b8b6f8 | -6.69899 | -40.46513 | 2026-10-10 04:44:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a7cfe918-62a3-365f-b238-6d79cf3881d1 | -3.19852 | -50.54786 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1c138fd9-04db-3167-a2fe-7f7532419059 | -4.17774 | -48.74486 | 2026-10-10 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| c0ce03de-68ee-3adb-8112-5f9438d5046a | -5.99542 | -41.37276 | 2026-10-10 04:44:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 89c1826c-1fde-3374-a630-3b7a06ebd7fe | -7.1459 | -45.0121 | 2026-10-10 04:44:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6c1f3588-7d67-33a1-8e46-65d6b7a4740f | -0.97601 | -52.45839 | 2026-10-10 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ae9c1e2f-f517-3bea-887a-3df89b88322e | -4.31129 | -50.78519 | 2026-10-10 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 72afb145-4713-3ac5-b6c6-3b78e45e9b6f | -1.95745 | -54.3911 | 2026-10-10 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 43eb5719-9e4a-3d67-a7a9-123ad1933bf4 | -7.07143 | -41.60136 | 2026-10-10 04:44:00 | NPP-375D | PAQUETÁ | PIAUÍ | Brasil | 2207553 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 927d4c91-3266-349f-854d-29a31a349730 | -3.31909 | -53.83951 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 72ac5afe-9a40-380d-ad5c-3a23ecb005ef | -2.83081 | -54.80865 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e3740648-04ca-3a1c-a399-444dfc7016d9 | -3.11358 | -54.16799 | 2026-10-10 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 65d41a01-42a0-3f86-b6c0-1c78006c68f2 | -3.7476 | -50.01178 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| dd505009-d974-33cb-8010-b843498139a8 | -2.82702 | -51.28099 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 323032dd-759c-3cdc-969e-7f9f1ec1c365 | -4.11885 | -54.0151 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 438258b6-080a-3ea9-be8a-92e166e9c11e | -3.04374 | -54.26162 | 2026-10-10 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1064b279-b2cd-3d48-a993-fe0b98c6c08c | -3.10225 | -51.35918 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3b33ce0c-7f64-367c-aca0-3b8670b22bc5 | -2.53132 | -56.27012 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4e13243d-b359-3423-8a07-23c5af088e1a | -3.9556 | -55.33645 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8540547-570d-3a4b-bd69-f75d6e733dc3 | -2.47485 | -56.07345 | 2026-10-10 04:44:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ebf31351-194e-34d7-9e13-600a3984ff03 | -3.74825 | -50.00775 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| eaade0a9-17ea-3ca3-8819-15f7df6e4f3c | -3.07807 | -51.41 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 096c1e2c-9a98-3369-a817-bb5518aad879 | -3.20382 | -53.85555 | 2026-10-10 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ee738750-b12e-397f-9e0b-e5ea7e9c1839 | -4.9982 | -45.77123 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9b7a17f7-33f5-33e2-a115-366bc4c01913 | -3.10182 | -50.31367 | 2026-10-10 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ce9ea8bf-80e7-34db-b127-c64199121a1a | -5.6721 | -49.82354 | 2026-10-10 04:44:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e7691801-c44d-3d06-b97e-ad53bdc331b6 | -1.99901 | -47.9548 | 2026-10-10 04:44:00 | NPP-375D | CONCÓRDIA DO PARÁ | PARÁ | Brasil | 1502756 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 47e3f8c6-401f-3b1a-a1b0-04ed4c77b025 | -7.05829 | -40.94794 | 2026-10-10 04:44:00 | NPP-375D | ALAGOINHA DO PIAUÍ | PIAUÍ | Brasil | 2200251 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| d9f8d140-7356-3084-8e04-e2ceb2de3f6b | -6.08816 | -44.26328 | 2026-10-10 04:44:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d45adfe6-866e-3027-9a34-5b21e986bc78 | -3.52208 | -50.34504 | 2026-10-10 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 170cd71e-300b-3332-8e1b-d4933c449a96 | -1.7316 | -56.06451 | 2026-10-10 04:44:00 | NPP-375D | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 12ca6e18-74b2-3cbc-b3ec-2a65de588880 | -5.9512 | -45.38107 | 2026-10-10 04:44:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99a85b64-9bd6-39c8-8a53-1ef48c02f8ed | -2.94546 | -51.41151 | 2026-10-10 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 28086073-a85d-333e-ae27-76cb396f888b | -1.65024 | -55.20089 | 2026-10-10 04:44:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5755fd58-64fe-32c3-a3fc-2e688560c435 | -4.99774 | -45.77439 | 2026-10-10 04:44:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1334349-d578-3f9d-97cf-595b6da3768a | -5.95928 | -43.90426 | 2026-10-10 04:44:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfd24291-3050-3cf1-8177-ddf192322df9 | -3.55019 | -55.51992 | 2026-10-10 04:44:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |


[Clique aqui para ver as próximas entradas](README61.md)
