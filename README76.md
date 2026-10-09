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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 95a481d0-0d4f-35e7-bb1b-cc6fcf708fe0 | -3.18859 | -50.54382 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cce95acc-87d1-39cf-9ba4-81f25b2f87a8 | -3.30591 | -53.70832 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 8edf9c76-213b-3e53-b818-3dd6c94b5780 | -2.97505 | -54.0397 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3a2094a-d5d0-32f7-8501-2bd76e074acb | -2.95902 | -49.1785 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| af4df5a7-3dca-3c1b-8000-4f35c3fe7a1e | -4.98908 | -44.99115 | 2026-10-09 04:25:00 | NOAA-21 | SÃO ROBERTO | MARANHÃO | Brasil | 2111672 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a66515dc-c221-3613-92ae-204c5b92ea06 | -3.1818 | -50.58557 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 7864678c-5eab-3e8f-b9ee-0828f18f09a5 | -2.99835 | -53.89759 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 76188d60-aaa8-364d-a447-38c9e5420205 | -5.8699 | -45.95945 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b68ad1c4-8ac2-396e-b5af-cae5488b976c | -3.0024 | -53.90415 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 21c3e5f7-6555-3295-966f-6aa659d2cf8f | -5.84239 | -44.92544 | 2026-10-09 04:25:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36390421-25a4-3545-90b8-b5670789e64b | -3.01305 | -54.06071 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d9ca4e4c-b869-37b6-a3ca-7839dd0dd5c9 | -2.4878 | -45.67113 | 2026-10-09 04:25:00 | NOAA-21 | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 453a3846-59b1-300d-aad8-e382b996c4ca | -3.17783 | -50.58493 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f7b7d075-88de-3bc0-89de-3d437631e09e | -5.09122 | -46.21762 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6682b8d9-22ae-3f29-9eb5-c9a9d065b233 | -3.12313 | -54.16772 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e6b6a088-8dde-387e-a5e9-7dfaee54fbbb | -3.55324 | -54.69136 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bc4e0884-1692-3d12-9705-32b99c89d401 | -3.26533 | -54.02569 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 6f5fee30-c44e-343b-aa28-be83223663bc | -6.88502 | -43.68948 | 2026-10-09 04:25:00 | NOAA-21 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a117be5-f6bd-33ab-b694-f765e8012761 | -5.09344 | -46.225 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 35381c4a-e6de-3e90-8b9a-00556f2a3299 | -3.20558 | -53.85849 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 413d58ce-0d34-3e25-9321-da6eefb4ffb3 | -2.58075 | -56.17641 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 4df24c5a-ab00-3709-a032-a9ffbdb75f5e | -2.50581 | -56.16151 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 317f0886-5816-3b77-b27d-65ee52fdce95 | -5.29768 | -45.72116 | 2026-10-09 04:25:00 | NOAA-21 | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 73c8ded6-5b92-3ca7-b011-f6fbd2cb6643 | -3.53178 | -59.5112 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 4c501e14-48ee-3878-9d83-a397271b85d8 | -4.1535 | -43.19205 | 2026-10-09 04:25:00 | NOAA-21 | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 239dd2c3-fa8b-3251-9fb6-7d9105a29dbd | -3.13747 | -54.36526 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a60b4fd9-d893-3b9f-af13-3261db52571d | -2.99892 | -50.29866 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6c5cb7d1-7f37-3bda-bca0-7936ec2fdd66 | -2.46514 | -56.08396 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e525d94c-e4fc-342b-ba98-c20287c05678 | -3.31137 | -54.02727 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5a3c9d87-701e-3389-b9f6-6011c74e2c0c | -2.76323 | -54.10984 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 217b4e0a-1df1-3bf2-9ca4-f9453d6633ac | -3.7311 | -59.46505 | 2026-10-09 04:25:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 090f28b2-2032-388b-b998-2dbf707990a6 | -2.9376 | -53.92229 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 88252e41-d8ae-345c-a19a-0d00e0035cfc | -0.87776 | -48.08342 | 2026-10-09 04:25:00 | NOAA-21 | VIGIA | PARÁ | Brasil | 1508209 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d40f507c-bc17-3f93-bbfe-3cc2e2224fa3 | -3.16026 | -50.59272 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaa4ce09-7fed-3c3e-9e38-a22e4d696ef2 | -6.05521 | -44.03393 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d6ada97b-6f4b-38a1-a4d6-83f84b52a817 | -1.78187 | -47.13543 | 2026-10-09 04:25:00 | NOAA-21 | CAPITÃO POÇO | PARÁ | Brasil | 1502301 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aed00909-e57f-3e69-bad4-7ca2c2ebb8b9 | -5.11046 | -46.22412 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e75d8754-a694-38c6-8d34-38fc9485b077 | -3.89636 | -55.89594 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| f8a5e1d5-4df5-3ff5-96b4-b1d88fc13c37 | -1.3331 | -47.95624 | 2026-10-09 04:25:00 | NOAA-21 | CASTANHAL | PARÁ | Brasil | 1502400 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 03857a98-02de-3851-9de6-38c2201e7808 | -5.09336 | -56.19435 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| fb9e5cce-6342-3b56-9f47-91c3695e4975 | -3.07737 | -53.94856 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d1e16c19-ecbc-39ed-a15f-2f9baa5a5788 | -2.36094 | -48.8834 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| cb18b790-08fe-3cdb-bd6c-9de68572cc97 | -3.84116 | -50.31322 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cb730f70-cc15-3f37-8abb-a1132e7e642a | -5.70648 | -53.47996 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 70164655-0cf5-3f65-af8f-e0154068a29a | -3.29872 | -54.01042 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95dc7040-1d59-3f67-85fe-215772b60190 | -5.99886 | -40.97874 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| 3fdc4c80-4706-3624-b774-3dfa279c077d | -3.21064 | -53.88958 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b465e02-3c68-301d-a882-18ebc023e110 | -2.40611 | -51.29579 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba3e8070-c697-3fe6-bbbc-2b09fbeaf944 | -3.00562 | -54.07467 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d1313369-c321-3a84-baa4-9ac3806b8d46 | -3.09477 | -53.93644 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| aa6bec53-4f03-3418-b0e8-aacdc463dd1c | -5.37696 | -45.86825 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5b8fa9c7-6d6e-379f-9cb9-f1dd40059e0d | -3.0249 | -54.07751 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9a12d9f2-4775-3a2d-921c-167ae1fa0203 | -3.00847 | -54.05698 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 76666351-f2a4-31c9-9c77-182921522faf | -4.80245 | -56.14254 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 80d6729e-ebd8-3c61-aa26-a8dd1b40db11 | -2.8297 | -51.28261 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 0a6ee701-68dd-34c6-b60b-ca24bc318915 | -3.0969 | -53.95472 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4250a39b-0c8f-35e6-ac7b-8b7a436773bc | -3.01737 | -54.09145 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e93058f2-1fbf-35a3-a1a2-0bcd6e1295ba | -6.83616 | -39.38993 | 2026-10-09 04:25:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 9404d45a-0c2f-3cc5-849b-53f9a27fa840 | -6.55888 | -44.36768 | 2026-10-09 04:25:00 | NOAA-21 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 6be34e04-8288-3c06-bbb3-8189e924b234 | -3.08642 | -53.95598 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 92bf85aa-2be2-3e0d-8c6a-2ebf87cf767b | -3.16316 | -50.45449 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fa2bf486-ac75-3dcc-9cd9-bd8a0e2f33cb | -3.55793 | -54.6953 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e6465bce-0986-3ce9-a058-40f152662208 | -5.95203 | -40.93461 | 2026-10-09 04:25:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d9702842-9598-3cea-85c2-103f478719bc | -5.39416 | -45.90971 | 2026-10-09 04:25:00 | NOAA-21 | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ac7d4caa-7122-3aec-a7a8-f32b7a5320a7 | -5.10218 | -46.21228 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 49d21505-8a15-3fb1-82c6-72e4bfe22e4e | -3.1797 | -58.63069 | 2026-10-09 04:25:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 43d1c4ac-c8c1-30b4-97f3-c7e6bc28baf9 | -3.94197 | -51.10131 | 2026-10-09 04:25:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 47dfe872-e4e8-3b11-896b-3becd9f1d8e1 | -5.47611 | -41.22623 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.8 |
| 2120ac8d-30db-309b-be1d-987eead65e4f | -5.74364 | -45.34563 | 2026-10-09 04:25:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ccd03a0-f6e0-3f7b-b2c7-4063f8080788 | -5.39583 | -47.80602 | 2026-10-09 04:25:00 | NOAA-21 | PRAIA NORTE | TOCANTINS | Brasil | 1718303 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| ce029b2c-cfc6-3474-89e3-d25cc8c7d6e5 | -3.01096 | -54.1059 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b43deb04-cdd0-32be-9cc5-e62e1108c043 | -4.22376 | -46.93058 | 2026-10-09 04:25:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0833bd3-d4da-3904-9f4f-2495497fe0d9 | -3.01123 | -54.0663 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4ef304f5-8ab2-3aa2-af5f-d03e15f0f5af | -3.00822 | -51.01105 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 87f1c2a2-fe11-3b49-b491-a123f5d2f3bb | -6.96522 | -45.25061 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d4bcffac-d76f-30d5-a58e-920c5c583841 | -3.80642 | -49.94447 | 2026-10-09 04:25:00 | NOAA-21 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 36044cf2-8e2e-3d48-89ba-87680fe2c0a4 | -5.69202 | -53.46007 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c7f3e267-b526-37b5-ba2b-513beac3291c | -3.00247 | -54.06205 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 47a504d6-8270-32a3-9f8f-fcb9c9dbd9ae | -6.18805 | -44.10843 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bb0511d7-a794-3843-ba26-e703ded45ad6 | -5.94257 | -45.68716 | 2026-10-09 04:25:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2e5fa5be-70ae-3675-ba79-8e7495af9200 | -4.73739 | -55.65909 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cee8464-3d94-3999-a75f-755b586ab6be | -3.18069 | -50.59241 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 81d7b205-bda5-339e-b1b4-3191059223ee | -3.17701 | -54.74623 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 667186b5-eb72-36cd-b247-a26c0cc824cf | -3.867 | -55.99797 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 66f5d138-46cb-3fa8-bcae-47b2a3874081 | -1.59259 | -47.35445 | 2026-10-09 04:25:00 | NOAA-21 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6504858f-7fd8-3b40-878a-4d75702c146d | -3.1608 | -50.44386 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b7c9859f-428d-3ced-a401-10c27dda5bd6 | -1.4255 | -54.62571 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9bfc194d-9639-3784-9889-d5ddda0e9da5 | -6.88335 | -45.89465 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2889913a-496f-3d49-8b0b-92f9e07ade89 | -2.94322 | -51.41055 | 2026-10-09 04:25:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e9a1b37b-0a80-3427-8761-ab584ceb8613 | -0.8528 | -47.54915 | 2026-10-09 04:25:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 02e355d9-2080-3a52-9491-eb7f53a8a00b | -3.2533 | -54.03596 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 99074e99-cb74-30f9-9a11-62255927422b | -2.73175 | -54.11087 | 2026-10-09 04:25:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2b58369b-db1d-3441-9be1-5c81fdac14b5 | -3.89827 | -55.89691 | 2026-10-09 04:25:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 16.1 |
| 505343f6-8bc6-31b6-a83b-8188633bd17b | -3.8766 | -55.99256 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 378adf23-182c-3369-b880-2d25c4fb4d66 | -4.74772 | -55.66437 | 2026-10-09 04:25:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52db2448-cf47-3f6a-97c6-0c43b4717833 | -6.96475 | -45.27619 | 2026-10-09 04:25:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 87f3d33c-1434-3276-a651-133426354dad | -6.88836 | -45.9061 | 2026-10-09 04:25:00 | NOAA-21 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| e510c6eb-7867-30df-abe3-1d85790b2c78 | -2.82613 | -51.27819 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6f1b85cc-d77d-38a1-b352-4e1bbe6a8f97 | -5.35597 | -43.40836 | 2026-10-09 04:25:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e2ab2dbc-672e-380a-a999-2379f46d4e83 | -3.55311 | -54.68863 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |


[Clique aqui para ver as próximas entradas](README77.md)
