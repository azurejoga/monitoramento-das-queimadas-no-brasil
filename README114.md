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

## Dados Diários - Página 114

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11e11fb5-f305-3642-8274-8462d6a32ce4 | -3.98402 | -55.81636 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 997d8ff5-d155-3d74-83fa-1372f9f9081f | -8.66254 | -66.58519 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 9f1d0c9a-0819-3be1-a44f-5c1ded2d3ed6 | -4.44458 | -54.97025 | 2026-10-05 17:15:00 | NPP-375 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| b6cb4c1b-8e09-3798-bab5-c23124a258f6 | -8.65728 | -54.57132 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 335c4de9-35dd-309b-97d4-f405d54b5584 | -3.4721 | -50.10318 | 2026-10-05 17:15:00 | NPP-375 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 20c33275-a31c-386c-ad8e-9c3238a5c856 | -6.72669 | -43.06139 | 2026-10-05 17:15:00 | NPP-375 | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e55a05fb-be2d-3934-976f-6775b24f7a90 | -6.51344 | -55.38814 | 2026-10-05 17:15:00 | NPP-375 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.6 |
| aafc9248-76b2-39a3-a39e-fa8858738141 | -3.07536 | -54.17356 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 89cddc08-ae68-3687-bf89-01d6a89d97fa | -8.99796 | -54.42577 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a1ce1699-08a3-3210-a117-2b5944e15856 | -4.93106 | -45.14761 | 2026-10-05 17:15:00 | NPP-375 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 22.2 |
| f764c327-344f-3605-8c33-05bd4c945c2a | -2.85524 | -51.30297 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 72a763ec-c693-31be-b89e-16682b50e1af | -3.0881 | -54.1681 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 390ed837-3ae5-3f77-897a-e6597804578d | -9.0325 | -45.16915 | 2026-10-05 17:15:00 | NPP-375 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 1f311c16-d6f1-388b-b3e1-af0ca8d1cc62 | -4.93897 | -42.71801 | 2026-10-05 17:15:00 | NPP-375 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 7.6 |
| 8dec7f8c-9f93-3e40-8fbb-30b23be1978b | -4.13289 | -54.01377 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c9d9fd59-901d-3b53-a17f-1a5a90f07b42 | -5.74276 | -45.0575 | 2026-10-05 17:15:00 | NPP-375 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| d3b98d1a-75d6-3680-aab9-baa5da0c9021 | -2.99334 | -54.10192 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 8e9f9ea4-9e42-3015-8e0d-d3c413185cf8 | -4.01133 | -55.67517 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c2274b12-4e07-38ff-9fe7-1e5b77b0775b | -3.50848 | -54.61795 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| c2873ed7-1d50-3579-b411-1d025249be5c | -9.16379 | -45.13313 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 14.8 |
| b230aabc-bc53-3f6a-964e-63817511fee1 | -3.10212 | -53.73371 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 91a91349-8020-3375-8781-a1e323692a80 | -3.82899 | -55.62104 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| b9b8aa92-6353-384c-b09a-8a74d7ae9ea3 | -3.08132 | -49.54691 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 4a4566ac-d0ae-33cc-aa1f-26d56979e71b | -6.18422 | -43.38711 | 2026-10-05 17:15:00 | NPP-375 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d9dbbdc6-b446-3e35-9cc1-163919c551ae | -3.23152 | -53.86962 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 3f7bfedd-32ea-38e4-aa1d-6a61fc8c4b06 | -3.67991 | -55.95213 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 63d2da1e-463d-374e-9b6c-1eda7bab9c59 | -6.32016 | -43.34739 | 2026-10-05 17:15:00 | NPP-375 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 12.6 |
| b9c9bae4-a5c7-3dec-9f15-8af8ec6443d4 | -6.88035 | -43.68056 | 2026-10-05 17:15:00 | NPP-375 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 30.5 |
| a0216e31-66df-3af4-9130-972d7dd24e5d | -9.40094 | -65.89029 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.0 |
| c6d89b3e-d3f4-305e-93bc-aafea30e0260 | -5.80642 | -43.82139 | 2026-10-05 17:15:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 978b7aac-6f26-3966-a398-195649370823 | -7.90377 | -44.19557 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 7d3b5c99-c3d3-3041-9a5b-c4a8a59f7dc8 | -6.15628 | -53.91626 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| aa934f87-4546-312b-947c-32edb95f6ddc | -7.90204 | -44.18568 | 2026-10-05 17:15:00 | NPP-375 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 9de1cb86-d8aa-394e-98cd-29bc63f79ea7 | -7.21043 | -55.19949 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| cf686d61-6400-3970-81f6-cd21c389e8d4 | -9.34111 | -64.71935 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 62f45e72-ff41-3498-ab91-f9783bfa58b9 | -5.93416 | -47.66967 | 2026-10-05 17:15:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9086e73b-045c-3ef2-8bbe-00226965f3ab | -3.70965 | -54.18663 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| ff78207f-4129-3162-8e17-0056981a44e9 | -5.68564 | -53.49075 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.0 |
| b0333555-dbd6-37d8-901b-6ea2338238b0 | -2.3302 | -48.39116 | 2026-10-05 17:15:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| bc4351f0-dbf9-34ef-8d82-fa0f2b771bbe | -3.6918 | -55.96163 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 34b1e9c7-0cd7-3132-b9c4-9ed561f51579 | -5.87889 | -45.96906 | 2026-10-05 17:15:00 | NPP-375 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| cae813fc-06f9-381e-892a-6f20e67497dd | -5.79187 | -43.75751 | 2026-10-05 17:15:00 | NPP-375 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 5842dfa3-b2b4-3227-93ab-3d90a184bb7e | -6.74138 | -41.20191 | 2026-10-05 17:15:00 | NPP-375 | SÃO LUIS DO PIAUÍ | PIAUÍ | Brasil | 2210375 | 22 | 33 | nan | nan | nan | Caatinga | 22.6 |
| f1f2bb20-a03a-3649-925f-3691e2a2a70b | -8.59871 | -67.14102 | 2026-10-05 17:15:00 | NPP-375 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 82f38769-62b4-3725-a046-ac322759f384 | -3.69415 | -44.97182 | 2026-10-05 17:15:00 | NPP-375 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5905a157-3e24-3736-b6bd-1ba42f000b12 | -2.69057 | -49.03638 | 2026-10-05 17:15:00 | NPP-375 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 29acd57d-ba09-34c9-a3a6-96c8606adc98 | -9.15389 | -45.13383 | 2026-10-05 17:15:00 | NPP-375 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ca869779-4590-3fdf-aa24-99b8266665f4 | -4.91492 | -41.74023 | 2026-10-05 17:15:00 | NPP-375 | SIGEFREDO PACHECO | PIAUÍ | Brasil | 2210656 | 22 | 33 | nan | nan | nan | Caatinga | 23.6 |
| 41f3fa4f-6368-3a3a-8cc5-6a4c5f09d600 | -4.37524 | -43.93272 | 2026-10-05 17:15:00 | NPP-375 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| efeba0dc-b751-3a2f-bf39-b23805c4254d | -3.91963 | -44.14788 | 2026-10-05 17:15:00 | NPP-375 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 195cf3c8-4597-3061-b2ac-287218908d9b | -9.73532 | -65.08771 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 94d169d6-adda-30f0-90d2-be8617735e38 | -3.49851 | -54.61946 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| faa84e14-fc9d-375f-8dc9-a905841b821d | -7.23099 | -55.2003 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 771d8d88-4996-30d3-ba32-3fe3ebfd63f2 | -6.67976 | -45.22883 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 174cc84d-7837-3a69-a7db-a0b8fb05c4d6 | -4.78226 | -42.57809 | 2026-10-05 17:15:00 | NPP-375 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 9731e2a1-aff2-3cf6-970d-14e66ae1e186 | -8.53261 | -54.59799 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 27.9 |
| 5c92b0d7-ae9c-31ac-ba33-3c750e0d7dca | -3.27883 | -54.00045 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2946338c-7b7c-3bfd-90ee-ae72a83f1ee9 | -5.47024 | -41.22871 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 28.6 |
| 7032fd59-e3e3-338e-bb5b-b3fc24789b1d | -4.65274 | -49.74545 | 2026-10-05 17:15:00 | NPP-375 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 39.6 |
| f0074dc2-37eb-3dd4-a948-bb1a32070a97 | -8.81266 | -49.30807 | 2026-10-05 17:15:00 | NPP-375 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 7fde3058-ea44-3cef-a526-369f36469513 | -4.85358 | -44.52085 | 2026-10-05 17:15:00 | NPP-375 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 25.6 |
| ccb0ed0d-200f-36fe-8330-afc5fb642108 | -3.22069 | -54.30642 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.0 |
| 7b801eed-a69d-3564-9a44-45f6ff8f0699 | -8.05834 | -46.72266 | 2026-10-05 17:15:00 | NPP-375 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 484b0b5f-9a24-359e-884a-e0cb8eafeba7 | -3.64735 | -54.04444 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 4467c5f1-2f8f-3295-9ed1-b8ba3a81a5d7 | -7.16196 | -39.66353 | 2026-10-05 17:15:00 | NPP-375 | NOVA OLINDA | CEARÁ | Brasil | 2309201 | 23 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 2fe70d9d-6a17-3c48-a036-f73f7bde02ee | -3.81864 | -41.7934 | 2026-10-05 17:15:00 | NPP-375 | SÃO JOSÉ DO DIVINO | PIAUÍ | Brasil | 2210052 | 22 | 33 | nan | nan | nan | Caatinga | 7.6 |
| a4cd1608-3364-3859-a3da-a64de91163e9 | -7.48313 | -44.43498 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 505c3256-bb98-307f-81f3-9a115dce753f | -3.22873 | -53.87359 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 12.2 |
| abf22fd0-e2b0-3464-b277-b150da2b7891 | -3.06102 | -54.16867 | 2026-10-05 17:15:00 | NPP-375 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ffc4a397-96c6-3abc-ae8a-eaa76987c2a2 | -4.71355 | -47.93097 | 2026-10-05 17:15:00 | NPP-375 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 3e0e4efe-8a9b-3cbf-8a1e-3cf0e9fbb021 | -9.46592 | -64.3319 | 2026-10-05 17:15:00 | NPP-375 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 15.0 |
| ada3a64e-a3a2-30f0-be54-c97a3cf14c9a | -4.27577 | -59.41281 | 2026-10-05 17:15:00 | NPP-375 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f45e2509-2c0d-3c37-a48b-96bf7fc3205f | -4.80602 | -42.1416 | 2026-10-05 17:15:00 | NPP-375 | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | 16.4 |
| 5afb4ae9-b34b-33fd-8b24-0edbfdcf50a5 | -8.53492 | -54.59019 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 2dc7b4d8-ffdb-32e7-baaf-124f6a5363f8 | -5.71834 | -40.12445 | 2026-10-05 17:15:00 | NPP-375 | TAUÁ | CEARÁ | Brasil | 2313302 | 23 | 33 | nan | nan | nan | Caatinga | 8.6 |
| c42d1f6b-5340-32bd-98a9-f732666befc0 | -8.66051 | -66.58411 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 09178a7d-2126-37a2-bbf6-9a026dc8d60d | -7.65472 | -44.3721 | 2026-10-05 17:15:00 | NPP-375 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 25b3c60c-3cc1-3272-84a4-33294ca05fe1 | -5.97185 | -55.35696 | 2026-10-05 17:15:00 | NPP-375 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 152b136b-014d-38ac-af34-97786ef62c8b | -6.7145 | -45.22927 | 2026-10-05 17:15:00 | NPP-375 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 0ae5e245-461e-3c94-bfe9-51054ba67f56 | -5.94244 | -41.34724 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 730a823b-5e98-3ed9-b553-c549461a60c1 | -8.53528 | -50.43437 | 2026-10-05 17:15:00 | NPP-375 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| b87afa19-6dd5-3b8d-83e0-8a006a05b997 | -4.82798 | -43.38293 | 2026-10-05 17:15:00 | NPP-375 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| acf160ec-11fa-30a0-a0fd-de62fba8bd3f | -3.09891 | -53.71285 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 120.0 |
| eb44a48f-3ddd-394c-b490-788bbc83d5a2 | -2.41802 | -48.06246 | 2026-10-05 17:15:00 | NPP-375 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f67cbf59-0aa7-3e0e-91ca-abac94724818 | -2.62836 | -49.30947 | 2026-10-05 17:15:00 | NPP-375 | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 704ae6b6-c526-3167-bdb4-e224aae137c9 | -2.80795 | -49.87181 | 2026-10-05 17:15:00 | NPP-375 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| d9adc061-61c1-36d8-b746-917fa73acf9b | -8.536 | -54.59748 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 18551366-65db-3044-82c5-f0fc3e26ab32 | -5.84729 | -53.81615 | 2026-10-05 17:15:00 | NPP-375 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ae9b3349-8ca7-3a00-bc61-f402fd35d4c4 | -3.23313 | -54.34334 | 2026-10-05 17:15:00 | NPP-375 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 6adef083-0d3b-3d40-91aa-f33dd0764bce | -3.66336 | -54.28205 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| e1db0f9b-ea6b-365e-a514-de55def34d80 | -10.86798 | -61.41467 | 2026-10-05 17:15:00 | NPP-375 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1cdfadf7-affd-32ac-99de-ed474e9ca2e1 | -3.46388 | -54.59288 | 2026-10-05 17:15:00 | NPP-375 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 01a2f8c8-b6a0-3318-98f3-1edc2b8b4a4d | -6.71123 | -66.48676 | 2026-10-05 17:15:00 | NPP-375 | ITAMARATI | AMAZONAS | Brasil | 1301951 | 13 | 33 | nan | nan | nan | Amazônia | 17.2 |
| 14ac0c3e-41f9-3d95-b549-52d1e2c39b92 | -2.85558 | -51.28165 | 2026-10-05 17:15:00 | NPP-375 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 9853786e-4298-3792-83eb-45004ceaec4d | -5.98994 | -40.91217 | 2026-10-05 17:15:00 | NPP-375 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 13.5 |
| 4547bd46-b9fe-35ac-901b-b2abf20822e3 | -3.6765 | -55.95265 | 2026-10-05 17:15:00 | NPP-375 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| 7cf14683-b6d9-317c-bcac-b18cb8e9f69f | -6.09223 | -47.65269 | 2026-10-05 17:15:00 | NPP-375 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| d7e32e32-7a3c-37a9-8ba2-53207f77a9be | -5.46796 | -41.23244 | 2026-10-05 17:15:00 | NPP-375 | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 41.3 |
| 5103eac2-896b-3024-9161-6dcdb0292642 | -9.33982 | -65.842 | 2026-10-05 17:15:00 | NPP-375 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 33f60f9c-72dc-3d71-874a-93f6215c4ba5 | -3.37952 | -54.10788 | 2026-10-05 17:15:00 | NPP-375 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README115.md)
