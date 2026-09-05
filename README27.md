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

## Dados Diários - Página 27

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 35a4291c-0436-33b0-a3f9-d4a16a974b0c | -5.3467 | -56.03076 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 0cdb2200-2e97-3181-8ab0-053980c4ddfc | -3.12306 | -57.69646 | 2026-09-05 05:40:00 | NPP-375D | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6b8560d5-ef4b-31fe-86b0-e012e9a5b66c | -3.0371 | -59.36103 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7f803151-7a59-3074-b2de-da2899dfad09 | -5.17166 | -56.05695 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3666aa52-c8d9-3f3a-8aac-bd14242e8a55 | -2.73666 | -60.07149 | 2026-09-05 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| da2b9e13-0da8-3e91-82ee-cede82f095fd | -3.41833 | -58.30432 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 169a46e5-6bce-35ae-91ae-494fa277d8d6 | -5.32519 | -56.02751 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6b7396c3-344e-351e-af0d-77593e79b96f | -3.42107 | -61.32772 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| dfe55679-b47e-3f8b-a045-67b5068b823b | -2.9182 | -60.99666 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e2af3cf5-2308-3cf3-ab79-8b1287204f36 | -3.1729 | -61.13973 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| cdce88e9-f4c8-30ce-8b8d-b13ced132fe2 | -4.28213 | -59.97027 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 872f4d2a-9c05-3771-b4be-9424e08bb0eb | -4.22109 | -59.55712 | 2026-09-05 05:40:00 | NPP-375D | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fab1819d-0e13-3799-aa81-d792411500c0 | -5.18406 | -60.24908 | 2026-09-05 05:40:00 | NPP-375D | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fa380839-5aa1-36cc-bb7b-8312678678b0 | -3.78073 | -59.71715 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dd12f5e3-d738-3282-a430-4597276ce766 | -5.31658 | -56.01541 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f6377401-9599-38c7-b19f-860eb80d6cbd | -3.23189 | -50.56999 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee773474-37c3-368f-859e-68b32c21691f | -5.32763 | -56.02948 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 87166923-a48f-3aa0-8138-fd80894288c4 | -5.31288 | -56.01072 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b47e4831-131b-367a-bbef-a5e941d0af60 | -2.91209 | -60.99216 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f816f1c-cf87-3a6c-ada7-c6db22305849 | -3.76586 | -61.75665 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cab54da5-e302-31ed-883b-7af76a564074 | -4.27957 | -54.77953 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 61aae328-6bf2-34ce-8488-4ebc74870063 | -5.31717 | -56.02217 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| df10ab73-4a62-3a38-ad52-826a09aa4f0c | 2.45272 | -60.76035 | 2026-09-05 05:40:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5479bcca-380d-3373-8459-97a14777219d | -2.80539 | -48.6794 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0faeb01-818f-31cb-a474-91e283a58a25 | -4.67998 | -55.63416 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 1a3ae441-170c-3e89-a852-79098fa4207a | -3.76976 | -61.77496 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 98616d0d-f23e-3f1e-8e26-273444bd90cc | -3.13659 | -60.63924 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 65335208-b025-3770-882b-81ea944a3d34 | -2.74626 | -60.23642 | 2026-09-05 05:40:00 | NPP-375D | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 308943f9-d720-353b-af78-eee8fad52e84 | -3.39176 | -61.34082 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3a182121-c9a5-3cfe-bc03-44aa0ad1a10e | -1.18534 | -53.82075 | 2026-09-05 05:40:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 516247b4-0d95-3bc6-8cd5-29321e518696 | -4.48695 | -55.08387 | 2026-09-05 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e1a948fc-1c65-3757-9619-1a595a0496f4 | -5.84943 | -52.04339 | 2026-09-05 05:40:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 9310cf70-db92-3ea7-b2ff-94f7745ed8e7 | -5.17226 | -56.05296 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d762560f-e6a6-3223-9d13-dc71b88f107f | -4.91947 | -55.80164 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 08716379-dd12-3c34-9024-7b5d8f3561eb | -4.28102 | -54.76986 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 58c5c7e1-027f-301e-af3c-674af92640e8 | -3.77195 | -61.76115 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ae2f68fb-484b-302d-b09e-228dcc37cbcc | -4.67439 | -55.64166 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96f11a5d-fbde-3063-bd21-ccd69daf6137 | -3.80806 | -55.88319 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9cdc901c-de30-3e0f-8e22-2c68e137096a | -3.23039 | -50.56813 | 2026-09-05 05:40:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1c5a8e3b-dd59-3efe-8395-3d5198b6a161 | -4.68058 | -55.63013 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fc3842a0-2bc1-3323-8c77-c566ada358e5 | -3.4061 | -61.31476 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2f35a7e-b8a3-3c0f-bed5-d345b3b94aea | -5.33809 | -56.02948 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 44278219-32b4-383b-bc8d-6d2edc4e70dd | -2.75471 | -54.67389 | 2026-09-05 05:40:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 955a6541-4bda-3cd8-9da0-e27a2a038bed | -5.33066 | -56.02007 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f02f2422-bb37-3cfd-b839-3a9a0b335263 | -5.31473 | -56.02754 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72aa007b-a9b3-3282-bca2-5825980e6800 | -2.75983 | -49.47571 | 2026-09-05 05:40:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a1581d57-fa38-3ed5-8faf-841d7de70849 | -4.67063 | -55.63684 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8bb781b3-7c26-3b4f-ba1b-20cab41f825e | -3.39614 | -61.31319 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6cb8ea63-b22d-3889-917f-22173546d69b | -3.83424 | -60.76926 | 2026-09-05 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c1be6a0e-365f-30f9-9c3d-b30fe85244f3 | -4.48167 | -55.08081 | 2026-09-05 05:40:00 | NPP-375D | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 38dfe447-d57a-37e4-8dea-509c9f7f69c7 | -5.31534 | -56.02351 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 023a7999-f127-3955-99c1-8628154e1450 | -5.32334 | -56.0288 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0e6e75b5-04df-3ba6-821f-818aa43348a4 | -5.34121 | -56.03823 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3f09184a-4a9a-3407-8b07-695b17c32d93 | -5.34729 | -56.02671 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| cc0acdda-75c5-375d-90c4-326f9cd167f1 | -3.4122 | -61.31924 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 473eb332-f6fa-30e8-a0f4-7b2511e856f4 | 0.97558 | -59.38407 | 2026-09-05 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ad8ca80a-dc83-365f-a0d9-7850520cc4a6 | -3.43944 | -52.81074 | 2026-09-05 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4ae866f2-91b2-3e53-aad7-7c490b5c5dc8 | -3.79168 | -55.87667 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b2ea2a59-fe17-3b9b-bc4e-be26b3442ed1 | -3.72035 | -59.3704 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0251bc23-61d7-3823-beaa-b20c5e0d97ca | -3.17399 | -61.13282 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a99c78e7-d78e-3b23-909b-7b464b80ce11 | -4.64597 | -55.74284 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e6882dfa-0e97-3cd9-bc23-569166ea6986 | -3.82755 | -60.76822 | 2026-09-05 05:40:00 | NPP-375D | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f0074d12-58c7-3468-b42e-2415431ae960 | -5.14725 | -55.95527 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1cf461f7-6b7b-3cb7-bdb4-2f4e5b29d45a | -3.0943 | -61.18756 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8e3f5ad6-4dbd-3cce-96f0-6fbd26923a7c | -4.16144 | -49.70639 | 2026-09-05 05:40:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cc691fc0-9184-3869-b1db-26048ac588ec | -3.19964 | -61.22889 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3b3e7cd-d02e-3353-8a21-205516ec2a9d | -5.29874 | -56.01694 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| aeb556d1-12d6-31c1-a488-ad7a8b96a7e3 | -3.13938 | -60.64326 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| e918dabb-ecec-39a3-b2a0-7c97e8501cf5 | -5.17534 | -56.0616 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d9770677-1f68-3efc-8060-68459d56c67b | -3.62847 | -54.60589 | 2026-09-05 05:40:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eb574c2d-9fc9-3824-9734-58872aed04bf | -5.33007 | -56.02413 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 76daf1b7-d795-3dde-91c3-fb8e7c147bf0 | -3.76324 | -59.42279 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fdc2ca3-9757-3c9d-9cbe-4779efc852d4 | -5.34848 | -56.01858 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 25b92ebd-9732-377d-8943-62ea20029991 | -4.66622 | -55.63641 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| ef25bf38-8613-3d95-badb-7c760e472e63 | -4.14745 | -60.69229 | 2026-09-05 05:40:00 | NPP-375D | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a85ce978-4198-32f3-9221-53cf69b75f61 | -3.19909 | -61.23234 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 373408c2-5502-3cfe-8cb2-774b0acf17ca | -3.07252 | -61.08854 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| fea8ab97-adad-350c-aaab-e3fafcbae9f0 | -3.03996 | -59.36535 | 2026-09-05 05:40:00 | NPP-375D | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| af08b1ec-2276-3e1f-84d4-52b6f424f0e2 | -3.20296 | -61.22941 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6affcf37-9718-3a29-8dd8-247859c34bdb | 0.97782 | -59.3982 | 2026-09-05 05:40:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32340663-4434-3243-b37b-3731149076f0 | -5.15156 | -55.95589 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7141ca2b-5017-3b53-92d6-a475ab910692 | -3.77363 | -61.77203 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 7b88058c-351b-37ce-b8fb-6fc292430634 | -3.76531 | -61.7601 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 841bb818-36b3-3ca9-8160-e6f617f1b6ee | -3.72095 | -59.3666 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1ca4899-e197-3813-a927-cefa7e08c80d | -2.80468 | -48.67341 | 2026-09-05 05:40:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ccf2a09a-e913-3e7b-91c4-d9da211163bb | -4.6762 | -55.62946 | 2026-09-05 05:40:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5368753-2752-3b1a-9bf8-69942893a0ae | -5.32147 | -56.0228 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 57dd7cff-15d2-3a29-a433-80dd8959f25a | -5.34417 | -56.01795 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 3ccdcd6a-c12e-30b2-8f62-3ca11974aa6f | -3.66793 | -59.27238 | 2026-09-05 05:40:00 | NPP-375D | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d0494490-a3ed-314a-aea1-43e5913de1f3 | -3.07639 | -61.0856 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ae214513-3399-3059-b35f-833d760657c3 | -2.91875 | -60.9932 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 77879035-8535-3bbc-8345-61469fecbe02 | -5.3332 | -56.03288 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b35bfe66-a146-3f3c-ba10-2d55b89eaec4 | -5.33691 | -56.03759 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 60d5ed28-8102-3075-91ae-b646ae44939f | -5.3418 | -56.03418 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 6ecb4e4b-a59e-352b-bf03-664419b5520d | -3.41165 | -61.3227 | 2026-09-05 05:40:00 | NPP-375D | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| da155085-9663-3dc0-9035-53ab1ff9d04c | -2.91542 | -60.99268 | 2026-09-05 05:40:00 | NPP-375D | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7bcc2c9c-150e-36eb-adb3-821a01e64c24 | -3.79533 | -55.88123 | 2026-09-05 05:40:00 | NPP-375D | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6f2251ce-0fa8-3a15-b72f-57954bce7574 | -3.43924 | -52.81067 | 2026-09-05 05:40:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 612034e6-6765-39ef-9dbb-feecfb370953 | -3.77308 | -61.77548 | 2026-09-05 05:40:00 | NPP-375D | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 87edf307-df49-39db-bce1-ae811cb4c455 | -4.6503 | -55.74363 | 2026-09-05 05:40:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README28.md)
