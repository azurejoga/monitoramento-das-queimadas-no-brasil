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

## Dados Diários - Página 152

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 66b29660-cd34-3ed9-a7a6-a2f59429d880 | -3.37767 | -54.12341 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 22ec285b-3522-393f-9a80-00667f5aa695 | -3.37669 | -54.10419 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 30b43e98-d300-311c-88ed-d2af645278d9 | -3.37599 | -54.1088 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 58bf0743-ec6e-3172-9237-ebe0cc428856 | -3.3753 | -54.11342 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| ba0aa818-2cb4-3278-b821-34682ab67164 | -3.37458 | -54.11815 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 53e9be30-b23a-368e-87c2-da354521e15f | -3.37387 | -54.12285 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9426ef5a-10d4-33df-b28f-0be7fbc12c85 | -3.37288 | -54.10364 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3bddb00c-0e44-3c8d-8790-df97bd98ba04 | -3.37219 | -54.10826 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b49d2ee-963b-346a-a3aa-c9edc81a7d70 | -3.37149 | -54.11288 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e108850-9daa-34f9-859e-3e4f875c90db | -3.33135 | -53.76457 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b4c192db-582a-3407-8615-0d0284b205e3 | -3.32748 | -53.76395 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cd8397f-4ee8-3e65-b449-9d80e7c03079 | -3.32677 | -53.76868 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 424e93ba-4679-3c0f-9a0a-fba5c53f85e4 | -3.32361 | -53.76332 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 30adf606-0a8c-3be3-a7b0-5dd22ea06043 | -3.3229 | -53.76804 | 2024-10-03 05:14:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 70264593-cab1-3b5c-83c8-59e20451a752 | -2.97945 | -53.7352 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4bd449e9-2392-3706-8033-1b8785a3bcba | -2.97873 | -53.74001 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6bc600d3-0b5d-39e3-8604-baba11464b55 | -2.97822 | -53.73239 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c3dd1767-8e72-36e0-9ebc-38aa41583a24 | -2.97746 | -53.73721 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 032146f3-ad1e-30fa-afd5-bc230fa7a76f | -2.97559 | -53.7346 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48a41ac0-6012-359d-b312-3478dd51d917 | -2.95102 | -53.70363 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| fe192dc2-d554-360e-8c43-870ca92701e5 | -2.95028 | -53.70846 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c6087d7d-b064-3171-9a00-9f35efeb2020 | -2.94715 | -53.70305 | 2024-10-03 05:14:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 978f2781-b15b-310a-92c7-ed8b29c3f3c3 | -4.33968 | -54.90272 | 2024-10-03 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b7eae8d8-509f-3069-9983-073b6afb32b1 | -4.33903 | -54.90703 | 2024-10-03 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19ab5988-b36a-3da0-a625-1b09b530d6c2 | -3.90987 | -54.56377 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9f109464-b839-3e19-8845-d91452c44229 | -3.79239 | -54.42437 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 17d0ab75-939c-3f56-900d-7c082004952e | -3.78862 | -54.42388 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a841d43c-7bf1-3b98-9767-e094a5c99cd3 | -3.66521 | -54.37066 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2646f17e-a5ec-3875-b675-fcb9f863dbdf | -3.65831 | -54.31427 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 857ecd97-138b-37c8-88ad-132acca4f8a7 | -3.65455 | -54.31365 | 2024-10-03 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 90a43385-3142-3c24-9135-8c0e2eba3ce5 | -6.64939 | -54.94861 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6e1fe610-5ef5-35f2-b2cc-5ddd376e3096 | -6.64872 | -54.95313 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| b4e05ccf-67b0-387a-8067-0dad9fd33be1 | -6.64562 | -54.94804 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 8f7139eb-49c3-3e51-a848-e53932bd1d8b | -6.64495 | -54.95253 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1666a4c4-1512-3802-9158-964ebd926d2f | -6.64185 | -54.94746 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| be0b6139-fa3e-355a-a940-9335f64d14d6 | -6.64118 | -54.95197 | 2024-10-03 05:14:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74ca5232-faf7-3af5-8503-23ca455ab97a | -1.34991 | -55.86637 | 2024-10-03 05:14:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 507b4574-5791-3ce5-b341-34a1eef8aa18 | -1.23417 | -55.68699 | 2024-10-03 05:14:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5e1c6bf-4c0f-373d-9bf1-12057171b2f6 | -3.44321 | -59.15824 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bda76707-49f6-3aed-a0f2-46520c91c39b | -3.44266 | -59.16174 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9b8e0844-8b3b-3af8-9210-7a38344fa5b9 | -3.4421 | -59.16525 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ee0e8ca-258f-33d9-bdee-de151da7f4d5 | -3.12435 | -59.00744 | 2024-10-03 05:14:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c0741931-6ba5-3057-be14-036631c866df | -4.22762 | -59.95474 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 024d7be4-ad2a-3047-b23a-f92cc51718a5 | -3.72668 | -59.36805 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4e906e7-db93-3a26-8a27-91751b813a77 | -3.72333 | -59.36753 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 23ccd01f-eb87-3a1c-8379-b5dcad3dc38b | -3.72278 | -59.37105 | 2024-10-03 05:14:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4abde5c-7306-3388-a4be-e68a1c20fc4f | 1.07995 | -60.42289 | 2024-10-03 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 194b3ac6-ea35-3fda-90fb-8710fdab3c9b | 0.89457 | -59.6986 | 2024-10-03 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 36f2d804-0ab3-3427-97ae-c8a793e45499 | 0.89397 | -59.69473 | 2024-10-03 05:14:00 | NOAA-20 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfc28c58-0c85-371a-b9fd-240be8a4b5e0 | -3.09034 | -61.11131 | 2024-10-03 05:14:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8a0668c6-f84e-3a21-9eab-b77c679ac245 | -3.07538 | -61.06712 | 2024-10-03 05:14:00 | NOAA-20 | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dc374c24-6931-37c4-bf76-f006cfa1c79e | -5.49988 | -60.4636 | 2024-10-03 05:14:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cf6ea7a4-9e53-327d-b082-a6b17356cfea | -1.50615 | -61.59199 | 2024-10-03 05:14:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cdc3cca3-5069-3a68-96b0-4dd9dd860251 | -1.5024 | -61.59139 | 2024-10-03 05:14:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 62a675e7-bd83-3025-b358-f73cb70f540a | -1.49866 | -61.5908 | 2024-10-03 05:14:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 6e8b3778-df75-3483-9e74-972d6085285c | -2.88338 | -61.8764 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f938d751-143d-324a-9e77-a928f8fbb4c3 | -2.88035 | -61.87134 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1677430e-78d5-38fe-9984-6ff9b0b1fd4c | -2.87964 | -61.87581 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ebf02708-4bd0-3d4c-82a1-a8a8aed3b533 | -3.11132 | -62.07759 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d5c4b169-7cd0-3cc4-b33c-bd48b928724f | -2.88859 | -61.87507 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5b9db52d-b656-3f9a-bc4f-4dd3fce23a72 | -2.88712 | -61.87696 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 646e0371-73d9-3888-be0a-0e173337eded | -2.88409 | -61.87193 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a18c6050-f180-37f3-b3e6-d08b228172c0 | -2.87893 | -61.88031 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12342096-cf1f-3c0c-b7b7-105aadc42632 | -3.29314 | -61.60212 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b0ce4846-63a0-3d32-8c35-0e429fbe7fd9 | -3.29302 | -61.51038 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 546b3f4f-cefb-3f24-a350-f8fae778a006 | -2.98796 | -61.42707 | 2024-10-03 05:14:00 | NOAA-20 | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6fb5e3e-f552-396d-a63f-81e73cf2cb4c | -8.76014 | -67.05338 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3611250-f334-3afe-af4c-f3a5f7b0b02b | -8.6958 | -66.6605 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 035b7380-9b14-32b1-9e95-88b356d28270 | -8.66706 | -67.0238 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 01e572bb-a54f-3103-ad40-e9ad3cc23c71 | -8.65883 | -66.67939 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2211befe-893d-3c69-8619-027df9685a8c | -8.65789 | -66.60292 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e8303807-192f-3760-837e-00dab83ccbd6 | -8.65703 | -66.60783 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 06ef1ecc-79ca-30e2-bf53-12eda9495b29 | -8.65416 | -66.67853 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 5aad3628-1363-37d2-9d27-e88059df415c | -8.65238 | -66.60699 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 17035049-562e-35dc-832e-64f802cfc57e | -8.64803 | -66.71336 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 682f24f4-1060-3887-b097-dc1e82b83fc2 | -8.64774 | -66.60616 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 30679a1b-c6ec-3e82-92ab-4713172ea144 | -8.64335 | -66.71249 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8aa13753-f4f9-3eda-8585-c3adb41bbe41 | -8.64246 | -66.71751 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 655da3b5-71c5-31ef-beb2-4a6171a306d2 | -8.63778 | -66.71666 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 55f06219-5b93-345a-9d90-78c6603f70bd | -9.37098 | -65.83753 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 65f4ac8f-a995-34dc-b9d4-7b76381056b7 | -9.37025 | -65.84175 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| be08a248-bd80-3b0a-917d-1ce575533e41 | -9.31227 | -66.63432 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 70e2e8ad-4eed-3665-ae9a-77b031503392 | -9.30853 | -66.62865 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6eb2c768-a63f-3ea5-9524-53f4374902ca | -9.30767 | -66.63348 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6b7f6fb7-5c21-3def-9ba2-93ebb136ae6b | -9.16609 | -67.31554 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f80a0210-4743-35f7-82e5-7123c369c49c | -9.16513 | -67.32085 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 98566517-e79c-3e9d-8064-905226e7b937 | -9.1603 | -67.31994 | 2024-10-03 05:16:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 098d2472-20e6-34c0-a6d4-576d90c2fded | -9.60198 | -66.11834 | 2024-10-03 05:16:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6165842c-2f89-386a-a9fe-8a2c89646f86 | -9.5587 | -66.60045 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7f0b7394-904f-37ac-bd50-c4e5e97d95c7 | -9.55787 | -66.60521 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e523778f-d3cb-3265-a25f-a166284a18a8 | -9.49878 | -67.11166 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 704c80c0-e52b-3335-8f59-e37ae72c76dd | -9.4975 | -67.1143 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 9d670fbf-9e61-3d05-94f8-bd79f2fdb306 | -9.47185 | -66.58451 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d3d23725-3a43-3fde-aef6-03ba817841f7 | -9.47161 | -66.58727 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 08133f0f-cd80-3fc0-ae7a-c4ec74c37044 | -9.46786 | -66.58173 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 72c937bc-5b92-3ad9-849c-2e1c95765afd | -9.46703 | -66.58646 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a41fc4a2-6c46-3fd4-887b-9d94400d0e86 | -9.42693 | -66.65315 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 685260c8-4b8a-38ed-ad9a-a5e9c126d70a | -9.4269 | -67.2356 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 02bb0758-c9c0-3502-a74d-1e885cc54068 | -9.42595 | -67.2409 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| daba4681-59de-3168-b718-2fdd5f298207 | -9.42212 | -67.23469 | 2024-10-03 05:16:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |


[Clique aqui para ver as próximas entradas](README153.md)
