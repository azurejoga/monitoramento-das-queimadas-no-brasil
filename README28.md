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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 80ee1c0d-9231-3ddf-b374-3824f3a4b1d7 | -6.57 | -44.16227 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| af2562d6-7d16-3f04-b89f-c60e8b4793d6 | -8.79315 | -44.27786 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 271a61a6-afbd-3e3f-9662-747b1648aace | -7.39017 | -44.78855 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| cfcfc315-278d-3919-aa4d-dd7dc2c67c62 | -9.62082 | -43.94809 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 558af2b0-8cf6-38b8-8889-1bf3dffdee1d | -5.76292 | -45.08976 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7d0106db-9cfb-3acf-a54b-a8d8eb283377 | -6.97758 | -42.58856 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| c6bf7b73-fa2f-34de-a79c-0d74251a6988 | -5.33875 | -43.29947 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0bd9e651-fd8d-3a99-a2f2-49e23d91d7e9 | -6.5838 | -44.15767 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 93390fe6-b74e-3ccc-82b6-dde5c7dbf287 | -6.58584 | -44.14892 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5252ae76-6a15-3e4a-b536-84cc5929a646 | -5.75627 | -45.08867 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 6c60f2d9-4e5f-3971-bb62-8540898d220e | -6.90519 | -41.69531 | 2026-09-22 03:42:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3c2d8cf1-7906-3c45-8e9c-fb9f098438b2 | -7.34497 | -45.34596 | 2026-09-22 03:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 593d0eae-3b05-34f4-81e5-ee346107c694 | -7.4919 | -35.24746 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 419cb276-705c-3ca7-a33c-57b536a19444 | -7.82294 | -45.25826 | 2026-09-22 03:42:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 7.1 |
| ece35c02-be3e-3467-83bf-a89a2b90b92d | -5.76325 | -45.08944 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 17.0 |
| d225f057-509a-3168-94c7-002336a4c247 | -9.544 | -45.39227 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 47747545-d2df-34ca-baad-90046efb3f06 | -8.10382 | -44.44901 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| cb71de8a-232b-3f00-881b-b612b8beeac5 | -8.79119 | -44.28786 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 1ecd4b1f-7f31-3e75-97e6-bd4363c43a4e | -9.61264 | -43.92083 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 81b6b418-85d7-3323-8ba6-2c7d7e065b0a | -5.3353 | -43.30227 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 98953b95-5546-35e3-a4ba-a29171e46775 | -8.3073 | -40.59631 | 2026-09-22 03:42:00 | NPP-375D | SANTA FILOMENA | PERNAMBUCO | Brasil | 2612554 | 26 | 33 | nan | nan | nan | Caatinga | 5.7 |
| a4d95dea-ae89-38fb-9256-099e48c8405e | -9.53745 | -45.39072 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe58b3f8-fc7f-3908-a2dc-78f4f53fa363 | -5.81317 | -35.5729 | 2026-09-22 03:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ba4d6152-0441-3fb1-b415-cf11ab4ab979 | -6.57095 | -44.15512 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fe237715-e370-35c2-96a1-1733ead72a5a | -7.49339 | -35.24636 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| cd5dbf3b-b0b6-35ed-a299-85e5c7a080d9 | -6.7092 | -43.98271 | 2026-09-22 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d3b3db1f-4b80-3983-bfd4-da431d2c0b5a | -9.62127 | -43.94142 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9125e404-123b-3e88-b344-bf2588086558 | -9.61143 | -43.932 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 91e8f11d-2035-3056-b502-d44f3ec96032 | -7.44804 | -44.75071 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 9.7 |
| 8e6f9ba5-f9c9-3fa3-99ca-51871efce945 | -5.73711 | -43.7226 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ab1f627b-026e-3471-bf61-05dc8a15de88 | -7.49629 | -35.2511 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 62f5f144-a55b-3246-8b8d-fd588f4ef02c | -8.79139 | -44.27149 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c6d3f7cd-dd7f-38fa-82f9-ef5293534429 | -9.54253 | -45.38665 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6392e611-7a99-3a05-b848-69ce60868663 | -5.75745 | -45.08214 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 22.6 |
| 44f52208-eb60-380a-a88a-8c32db5b1393 | -5.31258 | -39.1127 | 2026-09-22 03:42:00 | NPP-375D | QUIXERAMOBIM | CEARÁ | Brasil | 2311405 | 23 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 49d171a9-038a-364a-896a-54e7944189ca | -9.61524 | -43.94016 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 091006e5-c2ca-3a0d-8945-98c2ef2acf4a | -4.57809 | -42.94296 | 2026-09-22 03:42:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 86273b5c-d425-3abd-818d-1b024364e561 | -9.61321 | -43.92297 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| e48ca6db-1837-31fa-93f8-209e926b8956 | -9.61093 | -43.92985 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 6a14903c-2d49-3160-87a9-d488b273b846 | -5.99211 | -44.73104 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| c9719700-5aa3-3d5c-87f0-2869db7f0eb2 | -6.58574 | -44.14695 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c1b92ca5-2607-3898-adcf-9c847cc50c43 | -5.65341 | -43.42047 | 2026-09-22 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d74babaa-c59d-3a8a-b015-e514f0bd3c45 | -9.28936 | -46.18971 | 2026-09-22 03:42:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c8738ce-a499-3ffb-bcff-602e4bf244d4 | -7.49699 | -35.24696 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| d64056f6-2ac2-3d4a-9489-7634d948b30f | -7.35178 | -45.34731 | 2026-09-22 03:42:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 54a1c234-df1e-3f0a-aace-3daa90ab4c2e | -7.49122 | -35.25163 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 908d2d7a-b13a-3b82-9784-e6bc499801d6 | -8.79411 | -44.27298 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| d6dcd2b3-209f-3623-8fc0-f195780b0997 | -9.60537 | -43.93094 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd91c436-818b-31c9-a2f8-51fea00e71fa | -5.99322 | -44.72504 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| bc83b93d-c11e-35ec-bc07-65201decf5b4 | -5.75055 | -45.08096 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.8 |
| dd14bc18-672b-3bd6-ace3-bfabc93fc633 | -8.7856 | -44.30218 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| dc73d010-ac45-3c02-8782-9e7cb4aa4ee0 | -5.73803 | -43.71757 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2465824e-9c61-3aeb-b84f-a937f39c45eb | -9.61657 | -43.93775 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| aae09e29-a59c-39e1-acf5-d3ddc5618992 | -5.98651 | -44.72373 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 34247a89-cd9b-3585-825b-27f57e6e1aea | -8.48593 | -44.75245 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 2928482e-296c-36de-bafc-0217028bcf14 | -5.31804 | -43.4171 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 92b5efe5-dde1-3df7-b6b0-9a0a9cc8c4e8 | -6.89356 | -41.69706 | 2026-09-22 03:42:00 | NPP-375D | IPIRANGA DO PIAUÍ | PIAUÍ | Brasil | 2204808 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 742e1ddc-9c86-3cc9-b45a-52f9ffcddf1e | -6.58484 | -44.15427 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 01ff9828-27ff-381b-99ce-60d2cb1bcf8f | -9.52808 | -45.3903 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 52c708f1-1dfc-3054-9952-9e96b1f3f88c | -8.78666 | -44.29652 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 60904cac-8066-38df-ad00-d47139ba07f5 | -9.61178 | -43.92535 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 50809620-2ad9-35b7-aa74-a5181538d961 | -7.81551 | -38.86255 | 2026-09-22 03:42:00 | NPP-375D | SÃO JOSÉ DO BELMONTE | PERNAMBUCO | Brasil | 2613503 | 26 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 51af6b19-5588-3647-9fdc-60965bfa0c4e | -7.39688 | -44.7892 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| edab8209-87b5-3df0-b154-6b28f07c7f0e | -6.71719 | -43.98196 | 2026-09-22 03:42:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d64f765a-383d-3290-aad4-ff5d3fcd896e | -7.45306 | -44.74557 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 40368c29-b012-3e8a-9c9e-10fc04ae8e4b | -5.79022 | -43.86722 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9884f516-dc08-32e6-8361-f3be727eba6f | -7.02164 | -42.08437 | 2026-09-22 03:42:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.4 |
| 55287760-f7ce-3359-a7fc-8715541db93d | -5.99991 | -44.72644 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 56eafbf5-116c-37d1-91cf-01484b0faf35 | -6.57739 | -44.15632 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| e6140a44-f918-31c2-83a6-712065d50a28 | -5.32345 | -43.42319 | 2026-09-22 03:42:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4e517a7a-1976-359f-95ca-31a4827b9e08 | -8.487 | -44.74702 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7c04ad2d-24ef-3433-a127-3f428bcca4d2 | -5.78136 | -43.76878 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3f81777a-4e71-3cae-b215-4475f94c5e60 | -5.60967 | -44.8475 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7324deec-9572-3d68-b3e1-9348266b8f45 | -5.81391 | -35.5716 | 2026-09-22 03:42:00 | NPP-375D | IELMO MARINHO | RIO GRANDE DO NORTE | Brasil | 2404606 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 73e87465-7dc1-3836-866a-b4aee79d9265 | -6.57836 | -44.15096 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 508e4aaf-20d2-3244-bc47-b5a0aeb42682 | -8.48133 | -44.74591 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6a38a56-8bff-3d9e-91c1-09d83964231d | -7.39326 | -44.78863 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ff9d7df6-e01a-3171-9aab-44878d541e9e | -6.59584 | -39.13657 | 2026-09-22 03:42:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |
| 102e3a73-4b87-3532-bfcd-25e7a7203c13 | -9.62773 | -43.94483 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 586a91a4-6111-3aa2-a805-bb59e3f9baf3 | -5.8338 | -43.85174 | 2026-09-22 03:42:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 5776b3f5-4856-3b3b-b3bd-9ed54961a1ac | -6.57742 | -44.15826 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| ef64e463-b806-3a8a-a182-ef345fc7560f | -7.44909 | -44.74504 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 354064a6-0b06-3513-8f21-c8358b0f9c5c | -8.79019 | -44.29297 | 2026-09-22 03:42:00 | NPP-375D | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 59d5ac35-9525-388f-a442-b9b9243dbee3 | -7.38907 | -44.79421 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 33020829-2e68-388e-bd10-0c29e513dfa5 | -5.7494 | -45.0873 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 19.3 |
| ac1a7ac3-82b8-3143-80e8-74e91506f939 | -5.61078 | -44.84155 | 2026-09-22 03:42:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d687de91-2efd-34ba-b514-b828f8cbc8c9 | -6.78563 | -39.25997 | 2026-09-22 03:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 674f860d-9634-3ae9-89ec-32ca58a4d5e5 | -9.62729 | -43.94275 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| d8c93c8e-0340-34eb-8fa1-22481a9550c2 | -9.62041 | -43.94596 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 3939ceec-da8c-3532-9276-64019241b816 | -9.53072 | -45.39006 | 2026-09-22 03:42:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b5895c76-657a-30ff-b7ab-ca608d1b5d14 | -7.39219 | -44.79431 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| e338a635-d268-3fcc-b52f-44a1a55779e5 | -9.61955 | -43.95055 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 6ee6dcd4-2582-30da-b7af-fbbb81480011 | -5.65432 | -43.41553 | 2026-09-22 03:42:00 | NPP-375D | PARNARAMA | MARANHÃO | Brasil | 2107803 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 92f90d05-a6cb-3b03-ba8e-fa305bbfbb3f | -5.75594 | -45.08903 | 2026-09-22 03:42:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 0f4801fe-ba08-3970-b0a3-c4c37a93cc17 | -8.10483 | -44.44365 | 2026-09-22 03:42:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b2d104c1-374e-3911-a776-9602a527e41a | -7.49269 | -35.25053 | 2026-09-22 03:42:00 | NPP-375D | FERREIROS | PERNAMBUCO | Brasil | 2605509 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 79f2439e-b692-364d-9514-a20b5c7d3fd1 | -6.7903 | -39.26078 | 2026-09-22 03:42:00 | NPP-375D | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 33ef319c-f6ed-3062-8be0-be495b4621aa | -9.62432 | -43.93023 | 2026-09-22 03:42:00 | NPP-375D | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 20e92e94-3946-3377-b349-664e0bca2aef | -6.57099 | -44.15706 | 2026-09-22 03:42:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6894109f-fca9-381a-ab3e-66ef8e29b575 | -6.59119 | -39.1358 | 2026-09-22 03:42:00 | NPP-375D | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 7.6 |


[Clique aqui para ver as próximas entradas](README29.md)
