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

## Dados Diários - Página 161

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0d906d7a-3b04-3630-8fcd-6f1f96613f08 | -11.99782 | -43.47478 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 8f585caf-c19a-3bdb-ab0d-45a2af671f76 | -5.92162 | -55.69396 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 937e961e-b075-3ab2-851b-b842f6fa4665 | -8.17125 | -46.38909 | 2026-10-09 05:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e2ba5cfb-ebff-34e2-a074-eac2f1030874 | -3.55504 | -54.68738 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 4f89248b-9d3a-30f8-96b9-8a5067b0dcd5 | -8.71273 | -62.42078 | 2026-10-09 05:04:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f1b6ff0-5dc6-33c3-bfdb-77b0fd97879c | -8.65566 | -54.53222 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 76c97d75-3803-3c5c-af66-518e3e40923d | -3.16668 | -54.74041 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa27a841-f284-389f-ab12-cb99ff20281b | -3.76007 | -58.50971 | 2026-10-09 05:04:00 | NPP-375D | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4e515e68-73db-31b6-80d2-ec27c69d5319 | -6.93275 | -55.60442 | 2026-10-09 05:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 787d873c-c1e4-3abe-81e5-cc099dd3c348 | -2.90754 | -54.02535 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b6fe02c2-a2e4-392d-95cb-ea4a091c770b | -9.92712 | -44.79705 | 2026-10-09 05:04:00 | NPP-375D | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c69c538d-bde4-3c44-9124-c29d171dcf7f | -5.16161 | -60.32851 | 2026-10-09 05:04:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a5726f55-1324-36fe-a73c-3ccc42cd1651 | -3.02131 | -54.18885 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d07ef4f2-5ccd-387f-ab7c-2cdad3bcc843 | -3.00324 | -54.07604 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 25527cdf-54ff-3761-9100-d7e8ab2f85ef | -2.88073 | -54.11985 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ca4408fd-5de1-3eb0-96f0-f7a3d3c53bde | -3.60643 | -54.56285 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5b50ed3-1a22-36d8-83c3-3c0aa4a3d3b8 | -9.86842 | -47.47171 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 616f9a6d-1237-362d-9bb3-6cd76c78cb2b | -7.11819 | -52.68183 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 8f48f9a8-db63-3fd2-9250-5dcccb58635f | -5.69408 | -53.46689 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 3448d1c8-fde4-3143-83ef-32b74439349a | -4.07572 | -59.84582 | 2026-10-09 05:04:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 88f34a8e-d4d8-346c-b67f-2299987b1fd9 | -12.00601 | -43.4553 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 857fba1e-568f-387d-a3bf-a5aafd6852d9 | -5.82738 | -52.04961 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a71e1912-dd59-32ac-ace7-bc2a94c70096 | -3.09453 | -53.95654 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ec4f073f-32fc-3121-ba2a-0902a69d03be | -8.98175 | -45.90399 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 344a3e91-f559-3b32-b316-91653a4b9045 | -3.48588 | -50.4879 | 2026-10-09 05:04:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9fb4afd-3fc8-380d-8f5f-24de5e8fcbf7 | -5.36135 | -42.88183 | 2026-10-09 05:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 058e2029-fd97-39c6-a401-42875763321f | -7.08326 | -52.68697 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cc2e556c-b216-3469-b226-7cd21c1b8a48 | -3.22351 | -53.89482 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1dfcb8b3-d8eb-3639-8755-91321115dd67 | -3.27842 | -54.07022 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 973b44ce-b38c-3a90-aeb2-8ab0573cc845 | -10.84462 | -48.76942 | 2026-10-09 05:04:00 | NPP-375D | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 25be93c1-bb5d-340b-b71c-975e6f7edc5c | -4.46913 | -55.90091 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a78e037-4675-3760-8b44-35fafe2e2c57 | -8.96554 | -45.91729 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 848164e0-80a9-39e3-bddb-de651cd4e8f5 | -6.12649 | -53.06272 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1837df87-abb7-3b77-9a13-24fb9d956e86 | -12.00409 | -43.47132 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d23c5e95-53ce-3c1b-9b01-1d8c29389c5d | -3.497 | -54.61629 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b91e0b9a-700e-31fc-bc8c-39ab5a8a6b19 | -11.27525 | -45.19202 | 2026-10-09 05:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 7bb0b595-9a0e-3f01-881e-d5c380e97be2 | -5.71809 | -53.49573 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.5 |
| e95e73b3-2142-31b1-a4ab-14196b5f3d2d | -2.56706 | -56.16682 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 919cf94d-c8be-3cd6-9ef4-a65fc9f87d46 | -8.91043 | -45.22047 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3b36bfb1-e244-3b78-81e6-8b21f9d858e1 | -3.05428 | -53.91895 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5d6799bf-2d38-3ddd-a2ed-6229e2b25719 | -6.49521 | -62.85291 | 2026-10-09 05:04:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68e89b0d-ffa1-3a9b-ab98-01a83f6fbde3 | -3.30891 | -54.03595 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| abdf1963-9bbc-383c-9a1b-0b2275fbb1c0 | -3.08417 | -54.26986 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4f19aa5b-4533-3391-bfb2-8bfa3ae5e646 | -8.98107 | -45.90881 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d74e914d-8313-30c0-9277-25c8112449ba | -6.17154 | -53.08065 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c07f4e7f-e5df-37e8-91b2-3d9b9e14c5e0 | -5.95426 | -55.34014 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f3d36c0f-930e-3056-bf9f-c41b9c1faa4f | -3.01972 | -54.06593 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 159353d8-d863-3124-82ec-27fc17c88490 | -3.5668 | -54.67132 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e43eea28-ffa4-3248-a641-7aa0535c3138 | -5.70756 | -53.4473 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62c48183-3461-38c8-bb19-a803552eec10 | -8.99978 | -45.91175 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 34ebcced-03e6-3316-8751-6c92cf3565e8 | -6.38964 | -55.26757 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 523a11f6-8706-34a1-aae1-1214e09f76cd | -3.01691 | -54.21607 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da82b109-5f7c-343c-9275-1a197568e17d | -3.89585 | -55.8895 | 2026-10-09 05:04:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c43067fc-7627-32f8-b410-a9d8f5525391 | -3.08409 | -54.24672 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1fc7dd0c-d1dc-3a6e-a3ec-33519e1abe60 | -5.70804 | -53.47248 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5aa232da-13ef-3298-942a-4d9deb01a56d | -6.13872 | -53.07184 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f876b47d-5627-3d32-a43a-30edc35e6e3f | -2.99153 | -54.08207 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a3c7dc33-3c53-3366-8a73-81d4ad8febfc | -11.06683 | -44.06196 | 2026-10-09 05:04:00 | NPP-375D | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5215b480-c8fd-30ba-b565-3bd0ab7539d5 | -9.29531 | -47.43205 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| e9cc522a-93ce-34f0-9865-23e473d3d5b7 | -9.29758 | -47.41626 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6b828d7a-7b2a-3c7d-8d66-7fd3cbfc0c90 | -9.88065 | -50.51711 | 2026-10-09 05:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 784f689a-ab16-3117-8a28-49f7174d5649 | -6.57614 | -53.02357 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1c9dcf58-e018-32cf-a537-60a2aab37601 | -9.018 | -44.37881 | 2026-10-09 05:04:00 | NPP-375D | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2b72bb7e-2792-3ee0-b58d-a336464807e2 | -3.26797 | -54.06853 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f3c4b654-8185-35d9-936b-2502461a0f65 | -5.85989 | -53.45999 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2135e8d9-7582-3b49-8283-381cfb9f150d | -9.00109 | -45.91326 | 2026-10-09 05:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2f101f8d-0729-355d-817d-61aaa382a6f8 | -3.20462 | -58.84306 | 2026-10-09 05:04:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6ad6d140-8ce2-3f83-92fd-dc3afd4d43da | -8.73448 | -45.16477 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9598abcc-b9b9-3bd8-bb47-6cbe093ade60 | -3.00674 | -54.07963 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bcbb941c-806c-3133-b929-82139ff14e38 | -5.43835 | -43.44434 | 2026-10-09 05:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 9.3 |
| cbfd2f15-3e9e-328f-825d-a2525bf09fcf | -2.57555 | -56.18865 | 2026-10-09 05:04:00 | NPP-375D | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9322cf72-4453-346b-ba83-28822ebec804 | -6.15505 | -47.9164 | 2026-10-09 05:04:00 | NPP-375D | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efe1847f-3660-32f9-ba78-8cfcd1c5c87a | -3.30787 | -53.86508 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b5668aca-28ed-3b25-9aba-c417af4d3ae3 | -3.00834 | -54.24667 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9785bfb1-7497-3fce-8e05-2289b6fa1e2a | -3.25387 | -54.02327 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b6039274-0891-3b6a-94ea-cf954a27169c | -3.59955 | -54.67244 | 2026-10-09 05:04:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9de4c0f-aec9-3757-be2d-b5f9068dd1a1 | -8.49059 | -54.62542 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73c32bb6-c7c0-3587-aedf-3ff6e6954597 | -6.48565 | -55.29874 | 2026-10-09 05:04:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 049bd6a3-e045-300a-ad84-5cbb1caad23b | -11.86861 | -43.56371 | 2026-10-09 05:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 186defa7-f906-3b66-8b2f-7fb18bf15acc | -12.01306 | -43.49403 | 2026-10-09 05:04:00 | NPP-375D | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 4f4d0b80-be02-3afe-b56b-6ace40f31b7b | -4.50406 | -43.61872 | 2026-10-09 05:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3386c50e-85bf-31e0-b030-cd8d39803ba2 | -5.89014 | -57.71735 | 2026-10-09 05:04:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f87f510-c0f9-3589-a50c-0fa92bd81012 | -8.72839 | -45.13615 | 2026-10-09 05:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| b37d49c4-8fe8-39c6-aa23-b6f4568a6c47 | -7.8977 | -55.00264 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 33acddc6-138c-3865-ab96-76d9f9d43f57 | -3.00612 | -54.08044 | 2026-10-09 05:04:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a19efd0f-108c-3a60-9ab0-b035d291af4a | -6.4519 | -53.69001 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9dbdb8f7-0dd2-3ba1-a587-841715419a16 | -3.20635 | -53.86899 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8e43c131-bffb-346a-82df-1064ba40e256 | -3.52918 | -59.57289 | 2026-10-09 05:04:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 27c0adc5-8b64-3447-ae8e-e536e68ac19c | -5.87454 | -53.62691 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ad79ed9e-3e1f-3f2b-a255-954a68515967 | -4.82552 | -45.8368 | 2026-10-09 05:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8753fa68-937c-3e05-9ad1-b8775e7f8bee | -6.24926 | -52.86383 | 2026-10-09 05:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3ec687f6-074e-35a6-af81-ddd4b9b9b5a2 | -3.0785 | -54.28189 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7b05d804-cf42-37bc-a22b-5657b0389d6d | -2.47217 | -58.00685 | 2026-10-09 05:04:00 | NPP-375D | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d066cffc-dea8-38ea-b6a1-478106fca95a | -2.99262 | -53.85202 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 8f4afe2c-4495-368f-98d1-a8c1afcea862 | -2.9346 | -54.05722 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ae87e56d-5be7-3a7f-bb25-c83dba6aea32 | -6.41838 | -55.19731 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8e562162-2bf0-3fb4-beca-8050cc60fb5c | -3.08578 | -54.2821 | 2026-10-09 05:04:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 241e6658-e5f2-31d4-aa65-f14e238108fc | -9.29474 | -47.436 | 2026-10-09 05:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 13.2 |
| 9363b277-0d47-3e4d-9356-69ebbf04db01 | -6.00773 | -53.49142 | 2026-10-09 05:04:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 66f4ab43-bdbb-3324-835a-66c58b873556 | -3.30465 | -54.06262 | 2026-10-09 05:04:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README162.md)
