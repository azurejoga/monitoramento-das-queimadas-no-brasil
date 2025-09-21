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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 0395e665-8900-3356-978d-ce54e91fa8e9 | -5.62319 | -45.95154 | 2025-09-21 05:21:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5c28b0c8-1eb9-3fca-a113-e8a3d96fc937 | -5.52385 | -43.85669 | 2025-09-21 05:21:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 55.9 |
| df48eb61-ac49-3fa0-837e-df9323163454 | -5.52237 | -43.84913 | 2025-09-21 05:21:00 | AQUA_M-M | GOVERNADOR EUGÊNIO BARROS | MARANHÃO | Brasil | 2104602 | 21 | 33 | nan | nan | nan | Cerrado | 27.4 |
| b966bcbf-2fd1-3f98-8a4f-d38a78873b76 | -5.63536 | -45.94857 | 2025-09-21 05:21:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 33.6 |
| 6d9c025d-8f17-3ac6-99a5-6a46291e32c2 | -8.27911 | -41.67788 | 2025-09-21 05:21:00 | AQUA_M-M | SÃO FRANCISCO DE ASSIS DO PIAUÍ | PIAUÍ | Brasil | 2209658 | 22 | 33 | nan | nan | nan | Caatinga | 4.9 |
| c6232ab4-6b07-33c6-8a82-13304e0c0054 | -5.57009 | -42.13583 | 2025-09-21 05:21:00 | AQUA_M-M | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6cce0b2f-d451-3bad-b808-a38f5fef44c2 | -12.70856 | -46.85777 | 2025-09-21 05:23:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.2 |
| cfa3c0bd-5aa3-3839-b00a-8a91efbdae38 | -12.07256 | -44.80926 | 2025-09-21 05:23:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 1ccc4905-4c3b-359f-932a-31eee19750ed | -14.47361 | -46.4995 | 2025-09-21 05:23:00 | AQUA_M-M | SIMOLÂNDIA | GOIÁS | Brasil | 5220686 | 52 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 58415edf-8e43-3baa-a4c7-a9e0be42a9b9 | -12.69879 | -46.8338 | 2025-09-21 05:23:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 9fe37c0a-d2e0-3b89-a3ff-c55dde0a9169 | -11.20737 | -42.18578 | 2025-09-21 05:23:00 | AQUA_M-M | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 18.5 |
| 227e158e-8f93-35a4-a8b0-1050b6f6c689 | -14.9714 | -44.41923 | 2025-09-21 05:23:00 | AQUA_M-M | ITACARAMBI | MINAS GERAIS | Brasil | 3132107 | 31 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 478296a5-e2c9-3741-be08-5c7063025f70 | -12.71244 | -46.83604 | 2025-09-21 05:23:00 | AQUA_M-M | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 8e14f2f1-a3dd-3c81-a6e0-b2db4b3c31d5 | -11.20557 | -42.19708 | 2025-09-21 05:23:00 | AQUA_M-M | CENTRAL | BAHIA | Brasil | 2907608 | 29 | 33 | nan | nan | nan | Caatinga | 7.2 |
| ada90e17-c269-3fa9-943f-254be11fec7e | -9.4187 | -44.69576 | 2025-09-21 05:23:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 12.1 |
| bd1c6b0e-3ff4-39cc-959d-9882bdd28f2c | -10.26803 | -46.04667 | 2025-09-21 05:23:00 | AQUA_M-M | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 28.0 |
| 996816ed-b686-35e2-855d-f3359b88246c | -9.42605 | -44.70827 | 2025-09-21 05:23:00 | AQUA_M-M | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 14.9 |
| 785501a0-34c8-3d03-a62f-b08179e97517 | -13.53274 | -43.00154 | 2025-09-21 05:23:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 73.1 |
| 7076b94d-5c75-3e03-a35b-7c0610e5c76e | -11.48355 | -43.56895 | 2025-09-21 05:23:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 22.5 |
| b4ae3198-aa7f-343d-8add-e5ccd59114e2 | -12.06967 | -44.82645 | 2025-09-21 05:23:00 | AQUA_M-M | ANGICAL | BAHIA | Brasil | 2901403 | 29 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 38b76dfd-6de5-341f-b356-62bbad694746 | -13.53471 | -42.9896 | 2025-09-21 05:23:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 19.2 |
| 439c32ad-8277-39e3-814a-b854fe577024 | -11.48585 | -43.55528 | 2025-09-21 05:23:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 20.3 |
| 42086100-aebb-34a1-8539-d693c919016f | -11.49201 | -43.5846 | 2025-09-21 05:23:00 | AQUA_M-M | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 25.3 |
| b43ad5f7-6eb0-3a79-9e17-05f2a5670ef4 | -13.53078 | -43.01341 | 2025-09-21 05:23:00 | AQUA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 7dbb1ab6-724e-3fb9-ac66-57cfc34897a3 | -19.85584 | -42.12455 | 2025-09-21 05:27:00 | AQUA_M-M | SANTA RITA DE MINAS | MINAS GERAIS | Brasil | 3159357 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 7e239a0c-568d-30f4-948b-6a057cd17fd8 | -23.4169 | -45.70931 | 2025-09-21 05:27:00 | AQUA_M-M | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 8.5 |
| 28eac2d1-f085-31db-ab70-1e4feeac7ef1 | -21.11715 | -42.98154 | 2025-09-21 05:27:00 | AQUA_M-M | UBÁ | MINAS GERAIS | Brasil | 3169901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.4 |
| 8842ef80-8c60-3899-a02d-64dcb6b18898 | -22.46481 | -48.22281 | 2025-09-21 05:27:00 | AQUA_M-M | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 27.0 |
| ec0075a8-a415-3f7d-b26a-21de11ef00de | -23.4154 | -45.71465 | 2025-09-21 05:27:00 | AQUA_M-M | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | 11.9 |
| 5e3e8a35-33f6-3d00-91d6-8bce0f52f9a1 | -22.48097 | -48.20502 | 2025-09-21 05:27:00 | AQUA_M-M | TORRINHA | SÃO PAULO | Brasil | 3554706 | 35 | 33 | nan | nan | nan | Cerrado | 20.5 |
| 85048de7-5f69-3950-9d55-74df606c74d4 | -20.6853 | -43.194 | 2025-09-21 05:27:00 | AQUA_M-M | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.3 |
| ad5d259c-2e90-34be-8a2f-dc2a5497ec9e | -15.822 | -59.5017 | 2025-09-21 05:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 70.9 |
| 73ffaf60-fa28-30bb-a06c-85d6a7a1f90f | -15.8218 | -59.5217 | 2025-09-21 05:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 90.8 |
| 949175fa-ebb9-3529-a31b-c8031ab27de1 | -15.9783 | -59.4069 | 2025-09-21 05:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 04b2381b-2e08-31ab-adf4-8bb31d3bcc85 | -15.9586 | -59.4288 | 2025-09-21 05:40:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 75.2 |
| 2ac6c613-e7ed-343a-8975-f7e1f291d0ae | 4.33299 | -60.74264 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8c840486-215f-31b5-9b7e-420585b34fbf | 4.33379 | -60.72411 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 345cbe78-7528-3098-ba36-df430fcf8d06 | 4.32705 | -60.7297 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cbab270c-7126-3657-9f09-eb866a3494fd | 4.32926 | -60.74324 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 51895e11-bce5-3c79-bd01-a06ef5a448ca | 4.32099 | -60.73944 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5161a910-91fa-382c-a296-8861fd49f9d6 | 3.98276 | -59.65889 | 2025-09-21 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d624889a-9a95-390c-bf19-e40b0bc05c5b | 4.32624 | -60.74815 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d84c38ef-d5ac-39d8-8c0a-42c87f089b69 | 4.32551 | -60.74367 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 413479b8-3136-36c5-abb2-92e6eec152aa | 4.324 | -60.73447 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 558b4ab7-d73d-3fc6-bbd8-f34f6040c6f7 | -1.1232 | -54.14125 | 2025-09-21 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 15ec3982-4417-384f-afbb-6950c27eb315 | 4.33226 | -60.73819 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef1b348-8ade-3c3b-b5a1-b87d6732aef9 | 3.8755 | -59.6171 | 2025-09-21 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a86d748b-6b7d-313c-8c50-5d4ed6d1286c | 4.33527 | -60.73315 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 35d186e4-0445-3da3-9ac2-8bffa2f6aea3 | -1.12244 | -54.14618 | 2025-09-21 05:46:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| cb9870f0-58bf-387a-ace5-f3d4408ab19e | 4.33454 | -60.72869 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70935ddb-921a-36f0-8dbc-648cce97276b | 4.32779 | -60.73423 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| f1e3fda2-407d-3143-a8a7-4cd2645c3c67 | 3.98784 | -59.66489 | 2025-09-21 05:46:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a1990ab-4553-3dd2-928c-fcee0289ff0b | 4.02232 | -60.77029 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 594e91c0-079d-358a-bf36-3043dd793d91 | 4.32475 | -60.73907 | 2025-09-21 05:46:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 091380f2-a3e2-3775-b550-0e24182bfc23 | -3.75638 | -54.81599 | 2025-09-21 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 5c694c2d-d776-3ce0-a73f-c160bb27bb11 | -3.76327 | -54.81252 | 2025-09-21 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e13372f1-8c63-3d5f-962e-25ed96de41b1 | -4.37233 | -56.03228 | 2025-09-21 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 13b250e5-109d-373b-8586-5c75c0cd2a3f | -3.64765 | -58.16121 | 2025-09-21 05:48:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8d8aebe5-b191-36fc-b249-acc8187e800e | -3.59746 | -58.58678 | 2025-09-21 05:48:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 107a61b5-7a37-3866-b922-09346cd958cd | -4.37293 | -56.02812 | 2025-09-21 05:48:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1471a63d-8041-396c-8909-0ab55d94704c | -3.65265 | -58.16199 | 2025-09-21 05:48:00 | NOAA-21 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| d8494598-bcc1-37fc-b1be-860da169d74f | -3.75985 | -61.1996 | 2025-09-21 05:48:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 56bbf345-80fc-327e-8fb5-e2396bededb0 | -3.30132 | -52.58622 | 2025-09-21 05:48:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 8e17c93b-d64f-3b25-a8da-004a24377b10 | -3.76261 | -54.81713 | 2025-09-21 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 91f01838-38a5-3e1d-b7f8-87841de28715 | -3.75704 | -54.81134 | 2025-09-21 05:48:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| a3fc3e2a-031a-30ac-bbc2-35227e28144c | -2.80498 | -58.35135 | 2025-09-21 05:48:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 84a57f95-81e3-396f-903b-bf14374e7016 | -2.80579 | -58.34586 | 2025-09-21 05:48:00 | NOAA-21 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4d4ecd5a-83c0-3747-be76-df9da04b6921 | -3.75972 | -61.20037 | 2025-09-21 05:48:00 | NOAA-21 | BERURI | AMAZONAS | Brasil | 1300631 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eddc2060-a32f-3f4f-8fe6-d462d1b7cb22 | -15.8218 | -59.5217 | 2025-09-21 05:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 61.6 |
| 3da09393-a2c7-3e69-a928-f7fa104a0a8f | -15.978 | -59.4269 | 2025-09-21 05:50:00 | GOES-19 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 56b36a21-6eac-3a9b-9db8-15b858e86417 | -9.55463 | -68.5779 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bf44a09e-e76a-3e17-b9fb-45d523cb4d98 | -8.2075 | -61.19872 | 2025-09-21 05:50:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85c40a19-c323-3936-ba43-0b33a162a8ec | -7.85609 | -70.1125 | 2025-09-21 05:50:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18bd5bfb-c943-32d9-b669-950abd9f1ba8 | -10.10331 | -64.88734 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8e04a9e1-df51-3332-8c40-bf1804b03c7d | -10.19652 | -68.80173 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd62aaef-08ae-33ed-bc5f-19b8b7dde2c0 | -8.03709 | -71.36758 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1d580632-05d3-352f-8bfa-f1abe14fa64a | -7.97994 | -71.33929 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d5829021-990d-3026-a175-e9fe146e5524 | -9.39497 | -68.29623 | 2025-09-21 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b0d4a389-3177-32ba-bb6e-2ff2d5d07de4 | -10.15869 | -64.73532 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d03e04fa-37e5-36ea-857f-53a9e33b25e1 | -8.53505 | -67.07621 | 2025-09-21 05:50:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6483f2bb-d314-3560-ad76-bb84feb39f7c | -9.49036 | -66.54599 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4bc9df67-12fa-31db-9274-f4477140a011 | -10.11043 | -64.88842 | 2025-09-21 05:50:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffdfce03-6a18-3fe8-93b3-bd7dd824abed | -9.72918 | -68.40105 | 2025-09-21 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4cc65a7e-78bd-3c34-a6b6-8b8c7e38e7c6 | -9.44106 | -68.96787 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d3d1f255-3f17-3d4e-86fc-6ea4ff56d6d4 | -8.22644 | -71.03091 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 607c72d9-1831-3ebe-861c-8b25469deece | -9.59547 | -68.57733 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5aa7eb41-f84d-314a-bb17-925a0ecd1da4 | -8.27072 | -70.83344 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ed5418a8-1877-30a9-9ee1-891e66fd7d62 | -9.68188 | -63.17213 | 2025-09-21 05:50:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 85e57751-b2a1-391e-8b70-ffe35093eebd | -9.11555 | -60.96317 | 2025-09-21 05:50:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 689d11e9-34a3-387b-83cd-c16a252e0fda | -9.3911 | -68.2992 | 2025-09-21 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 386367f2-a158-306f-974e-ce786412de44 | -8.79299 | -69.01827 | 2025-09-21 05:50:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 256ddf2c-b692-3abb-a9d7-bc2591c91567 | -8.98868 | -65.45364 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d93f82ac-5818-3e05-870f-a27b1ac1b9aa | -8.23828 | -70.8694 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fece2706-a11d-3ca2-8fde-e2775da62eff | -10.25107 | -68.82144 | 2025-09-21 05:50:00 | NOAA-21 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8f532763-4f26-3add-8538-c02353a0bce9 | -8.9898 | -65.44608 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 43abdd7a-ee44-361f-b985-9be5cc119845 | -9.74128 | -68.43175 | 2025-09-21 05:50:00 | NOAA-21 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 483e34dd-7593-32a8-9d66-88398ac0ce7c | -9.27291 | -65.50014 | 2025-09-21 05:50:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 125bf3f1-bf68-38a3-ba56-12f2c3d33528 | -9.40007 | -68.95047 | 2025-09-21 05:50:00 | NOAA-21 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b97271ce-184a-3f53-81c5-4c2d085a1bf2 | -8.03717 | -71.37038 | 2025-09-21 05:50:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b68d5a68-9850-387e-8ce5-1b9701586cfe | -9.44652 | -56.71751 | 2025-09-21 05:50:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README44.md)
