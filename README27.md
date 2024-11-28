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
| 5ec1080e-70ae-37e4-9453-cff7e51b23ba | -5.89643 | -35.42478 | 2024-11-28 03:38:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| b4bf0a4e-f957-3092-a990-1461958e36a9 | -5.11336 | -38.07248 | 2024-11-28 03:38:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 57d9a11b-b339-38b2-9eab-76611132f02e | -5.97335 | -45.36311 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| d9ac0051-b4e3-3acf-9f94-c1fc9a3310da | -5.38219 | -35.61313 | 2024-11-28 03:38:00 | NOAA-21 | PUREZA | RIO GRANDE DO NORTE | Brasil | 2410405 | 24 | 33 | nan | nan | nan | Caatinga | 0.6 |
| b5ac0546-d910-30f8-9844-4606b3b9bb6f | -9.17311 | -44.7243 | 2024-11-28 03:38:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d375775-b4d0-3e7d-af33-7ad4f50f8cb4 | -6.77393 | -35.42546 | 2024-11-28 03:38:00 | NOAA-21 | PIRPIRITUBA | PARAÍBA | Brasil | 2511806 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| cede4401-8377-3579-9b82-0b9b5d755097 | -5.62531 | -39.69456 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b454bf4f-2d88-3ea5-a893-374b2c21a739 | -6.6039 | -39.19809 | 2024-11-28 03:38:00 | NOAA-21 | CEDRO | CEARÁ | Brasil | 2303808 | 23 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 2ef61bec-ad7b-3d83-beb5-9a6e68b6b395 | -6.66394 | -39.24203 | 2024-11-28 03:38:00 | NOAA-21 | VÁRZEA ALEGRE | CEARÁ | Brasil | 2314003 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 80b07960-7c5a-3cbb-a3d0-d8137fc25421 | -6.09133 | -41.94166 | 2024-11-28 03:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f7be1704-e7b0-30bd-910d-ff93c3687795 | -5.0895 | -45.83755 | 2024-11-28 03:38:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| b535be18-a7c9-3b4a-af4d-5c066b106786 | -5.97874 | -45.3688 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3e7b53a6-6884-397e-9508-055edfcad471 | -4.77052 | -44.42299 | 2024-11-28 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| f923e2d1-2327-32ac-86d3-92f52d87a6bf | -5.95074 | -39.66753 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 36.2 |
| 62c4a514-e381-3cec-8e38-ae646e5923db | -8.12687 | -47.98187 | 2024-11-28 03:38:00 | NOAA-21 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 34441f1a-e11c-3887-8e33-7265a34d5959 | -7.35674 | -35.11513 | 2024-11-28 03:38:00 | NOAA-21 | PEDRAS DE FOGO | PARAÍBA | Brasil | 2511202 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.5 |
| 7c556129-d787-3303-ae2b-8a45845381bf | -6.75669 | -35.09941 | 2024-11-28 03:38:00 | NOAA-21 | RIO TINTO | PARAÍBA | Brasil | 2512903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.4 |
| 30de00e2-2ce2-3464-aca7-a0c22717b7d5 | -4.72515 | -43.25484 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| cc906519-2796-3f63-b00b-1b2ba73b7171 | -6.25081 | -37.20887 | 2024-11-28 03:38:00 | NOAA-21 | SÃO FERNANDO | RIO GRANDE DO NORTE | Brasil | 2411809 | 24 | 33 | nan | nan | nan | Caatinga | 3.8 |
| c488974f-e125-37c6-a375-69a9b9b86a41 | -6.16311 | -42.62495 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 0e036b5c-010b-374d-b6a9-820694607bbc | -4.04073 | -46.53815 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5c65e9ed-aa9b-3114-90ab-78a650aa864a | -6.50079 | -39.59692 | 2024-11-28 03:38:00 | NOAA-21 | JUCÁS | CEARÁ | Brasil | 2307403 | 23 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 665c78e1-531e-3cde-a0b2-b1869ad3a7b1 | -3.91415 | -47.20247 | 2024-11-28 03:38:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| fe71b4b1-ae2e-31ee-97b1-cd7651395f23 | -9.99569 | -36.25548 | 2024-11-28 03:38:00 | NOAA-21 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 80677baf-5395-3c6d-8194-ed5dd68513dc | -3.86851 | -46.34183 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 8eddb88e-2516-362c-b22c-3b9cfb360b37 | -6.17521 | -42.61706 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 857897ca-b7a8-3572-a1f1-b7c6c9b0b041 | -6.8678 | -44.75725 | 2024-11-28 03:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| fa9596ae-153a-3c03-971f-ad746097f0e9 | -3.67446 | -45.78991 | 2024-11-28 03:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b1ecef71-6b25-37c8-8cb2-d49326e37519 | -7.68985 | -42.98089 | 2024-11-28 03:38:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| f9bb96d9-69f3-3223-937d-35f00298b98a | -7.12526 | -35.2678 | 2024-11-28 03:38:00 | NOAA-21 | SAPÉ | PARAÍBA | Brasil | 2515302 | 25 | 33 | nan | nan | nan | Caatinga | 0.8 |
| b9c0bd9a-7d29-3e49-b3a0-74921ccd842d | -6.15901 | -42.61777 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 8e2140c0-5b3e-3f1b-a8b0-64292fdfe0c3 | -10.09518 | -36.49147 | 2024-11-28 03:38:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 12.1 |
| f4d73872-f89b-3949-9378-e44db418efe8 | -9.85456 | -36.39165 | 2024-11-28 03:38:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| b8af51c6-2f0f-395c-be0f-df9092c8a55a | -5.97424 | -45.35825 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 324c2dff-65c3-3453-a8ab-1f45c2633847 | -4.03953 | -46.54515 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 1c416bdf-705e-36f8-87b8-569f8cd5a203 | -4.04013 | -46.54294 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2bc07998-c794-3555-b94f-91a8c1fc6655 | -4.6593 | -44.03624 | 2024-11-28 03:38:00 | NOAA-21 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0d7af2b9-515f-3603-81eb-a018a0ba9cc4 | -6.08685 | -41.93788 | 2024-11-28 03:38:00 | NOAA-21 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 39172bd1-f7b5-304c-a14b-00799dd3f5bd | -6.72113 | -39.12406 | 2024-11-28 03:38:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 58b52217-4c84-3def-a98e-221efff67511 | -6.86619 | -44.76612 | 2024-11-28 03:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0d7695dd-1781-37e0-98b6-9a99a0a1037b | -6.16888 | -42.62261 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 944137d9-3f80-38bf-84b5-925a1a59e590 | -6.72113 | -39.12391 | 2024-11-28 03:38:00 | NOAA-21 | LAVRAS DA MANGABEIRA | CEARÁ | Brasil | 2307502 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| bc91c0d4-31f5-3290-b762-db0b138ed961 | -9.00179 | -35.99659 | 2024-11-28 03:38:00 | NOAA-21 | SÃO JOSÉ DA LAJE | ALAGOAS | Brasil | 2708303 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.7 |
| 0d1d9303-081e-3e3b-9807-67b9b2d3cd7d | -9.85516 | -36.38795 | 2024-11-28 03:38:00 | NOAA-21 | JUNQUEIRO | ALAGOAS | Brasil | 2704005 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7c7f5f4d-9535-32f3-8bd6-c340b51d4520 | -5.98108 | -45.36682 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 42.1 |
| 80f1a0a6-bfee-34db-a912-2b322d8e8d21 | -5.94646 | -39.66682 | 2024-11-28 03:38:00 | NOAA-21 | MOMBAÇA | CEARÁ | Brasil | 2308500 | 23 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 98a856e2-40e9-3cbd-af0e-962d06d709d9 | -6.16532 | -42.61231 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 6e80d794-270c-3f42-b010-9a4037d59380 | -5.90785 | -42.56775 | 2024-11-28 03:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 85abb33e-4bfd-3e35-b5e7-2b90e4ec1117 | -4.08726 | -46.14776 | 2024-11-28 03:38:00 | NOAA-21 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 23.6 |
| 266dd644-887d-352f-b799-d13d8c8a53c5 | -8.50614 | -43.28318 | 2024-11-28 03:38:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0a38ea6b-0178-3ffc-a0fd-157ef7c1970b | -4.92858 | -45.42468 | 2024-11-28 03:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 6.8 |
| f2a8fe37-d1f2-357e-8468-e6220c359657 | -4.80841 | -43.29848 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 48946bfa-dcd1-3e97-8996-f844e729d18a | -6.3571 | -47.06623 | 2024-11-28 03:38:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2e842b5b-971e-3829-9713-aad2018ad255 | -4.80728 | -43.29836 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 60bbe7be-835c-3a08-b05f-dc6f1f3f27e2 | -5.89701 | -35.42113 | 2024-11-28 03:38:00 | NOAA-21 | MACAÍBA | RIO GRANDE DO NORTE | Brasil | 2407104 | 24 | 33 | nan | nan | nan | Caatinga | 3.4 |
| 63e044ef-838a-3a57-81fa-d5d4a345bfc5 | -5.98277 | -45.35715 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| f4f0821b-f74c-3670-b35b-7afee2520704 | -7.69042 | -42.97773 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 1ee21f07-c861-337a-a80b-36fd8ddd6ff6 | -4.93499 | -45.4255 | 2024-11-28 03:38:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a8a91df2-281d-3092-9752-5b5c86384481 | -8.85578 | -39.87956 | 2024-11-28 03:38:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| a53a12e3-d5ef-3da4-9b15-a733eee14167 | -7.81506 | -35.55006 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | PERNAMBUCO | Brasil | 2602209 | 26 | 33 | nan | nan | nan | Caatinga | 2.8 |
| d84b9783-7dd4-3ea4-8966-c92a6877b5df | -6.01139 | -38.66269 | 2024-11-28 03:38:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 11.0 |
| 6c19abe4-1619-33dd-8f8a-c7f25ba0ba8d | -6.867 | -44.76165 | 2024-11-28 03:38:00 | NOAA-21 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 588bb7a0-ddcd-3ba0-9210-f00e3b7b6582 | -5.9836 | -45.35241 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 36.6 |
| 3f5b9a04-1c2d-3a8e-9183-ec2449b89951 | -5.39047 | -40.65829 | 2024-11-28 03:38:00 | NOAA-21 | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bcf389d8-2f93-356d-bfd3-c4adb667d6a0 | -8.6609 | -39.57204 | 2024-11-28 03:38:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.8 |
| b7e36961-4479-3e28-899d-728c38ad1d42 | -4.09507 | -44.86053 | 2024-11-28 03:38:00 | NOAA-21 | LAGO VERDE | MARANHÃO | Brasil | 2105906 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf27c449-7799-363f-96b3-5f5cb019ae08 | -6.73543 | -38.78515 | 2024-11-28 03:38:00 | NOAA-21 | IPAUMIRIM | CEARÁ | Brasil | 2305704 | 23 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 969088ab-77d0-3a11-a06b-68a232d7d408 | -8.17338 | -35.24165 | 2024-11-28 03:38:00 | NOAA-21 | VITÓRIA DE SANTO ANTÃO | PERNAMBUCO | Brasil | 2616407 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 5641c2d0-0a5c-3249-a64d-9259c2aebbd7 | -4.00351 | -44.28455 | 2024-11-28 03:38:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| afa741cb-6b31-37fa-b2b5-1bec0b6853aa | -10.09457 | -36.49518 | 2024-11-28 03:38:00 | NOAA-21 | PENEDO | ALAGOAS | Brasil | 2706703 | 27 | 33 | nan | nan | nan | Caatinga | 12.1 |
| a2b6d1e6-4ad7-3b87-afed-a3b623ea54c4 | -4.78175 | -44.42924 | 2024-11-28 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e583b691-6bcb-3736-a463-9ecf61103523 | -6.59044 | -44.17636 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2a5d499a-8459-38c1-801f-af16fc60c393 | -6.16477 | -42.61548 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| f35de6b5-88ef-352d-ac0b-4961080ceff9 | -7.68968 | -42.9766 | 2024-11-28 03:38:00 | NOAA-21 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 01b26a44-2188-3be5-b25a-a17e5d47cf2c | -5.82965 | -44.10786 | 2024-11-28 03:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 1101d4c7-56e3-3cdd-9375-f797506be861 | -6.83157 | -44.39488 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 0c77c6aa-abe8-3fe6-9e6c-6e9c9f18ed49 | -8.19387 | -35.94955 | 2024-11-28 03:38:00 | NOAA-21 | CARUARU | PERNAMBUCO | Brasil | 2604106 | 26 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 7ef6c597-4aa1-3ff3-8555-92d7db6ed965 | -7.74773 | -34.85665 | 2024-11-28 03:38:00 | NOAA-21 | ILHA DE ITAMARACÁ | PERNAMBUCO | Brasil | 2607604 | 26 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 985e7ad0-f848-31a1-aa79-7233b832fe7a | -6.01196 | -38.65919 | 2024-11-28 03:38:00 | NOAA-21 | JAGUARIBE | CEARÁ | Brasil | 2306900 | 23 | 33 | nan | nan | nan | Caatinga | 7.2 |
| 6274b901-4287-3b2d-a2af-d2b696acfce3 | -5.98052 | -45.35905 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| 07bbcdbe-0bc5-3a5a-a7f6-f86a1cd527ae | -9.97988 | -44.0911 | 2024-11-28 03:38:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| ae56e125-426c-30f0-865d-3dcf43f324c2 | -6.95029 | -39.12915 | 2024-11-28 03:38:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 59c0b81a-8d49-3b3f-93bb-51255647cf30 | -6.5897 | -44.1804 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a2c2e47d-71a6-3836-80f2-aac8ec70085f | -4.05757 | -46.68463 | 2024-11-28 03:38:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 685c4cf7-ac98-3f2b-8639-4ddb47fa8bc3 | -5.58198 | -43.14952 | 2024-11-28 03:38:00 | NOAA-21 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 8fe5ee44-5198-3d24-a0cc-018a315b542d | -4.72445 | -43.2543 | 2024-11-28 03:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4a4fa590-c20f-38bb-a990-ca13156e76ee | -6.58894 | -44.17659 | 2024-11-28 03:38:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| d8aa7087-fc2b-344c-8eb6-7e7919abcec6 | -6.16366 | -42.6218 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 5.2 |
| 524a6488-1f5f-3f5e-b978-27fbe0d64295 | -5.98587 | -45.36492 | 2024-11-28 03:38:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 63.6 |
| a2514038-6049-38d6-9fa8-431f36451014 | -4.77655 | -44.42374 | 2024-11-28 03:38:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 990429b8-54a4-3d50-b57c-9a37eabf57d0 | -6.99439 | -34.90917 | 2024-11-28 03:38:00 | NOAA-21 | SANTA RITA | PARAÍBA | Brasil | 2513703 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| 7657f480-bdf6-3a46-8dc6-1e13b3fbad31 | -5.9073 | -42.57099 | 2024-11-28 03:38:00 | NOAA-21 | OLHO D'ÁGUA DO PIAUÍ | PIAUÍ | Brasil | 2207108 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 353910bd-3e21-3857-9569-02935fef0e6e | -8.85514 | -39.88336 | 2024-11-28 03:38:00 | NOAA-21 | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| c98d4355-429e-36c9-add7-01eb040a9c10 | -7.31653 | -35.19613 | 2024-11-28 03:38:00 | NOAA-21 | JURIPIRANGA | PARAÍBA | Brasil | 2507903 | 25 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 8ab04d0b-580b-37fe-bf1b-1e06c1c468fe | -6.93301 | -39.25548 | 2024-11-28 03:38:00 | NOAA-21 | CARIRIAÇU | CEARÁ | Brasil | 2303204 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| 4fc608d6-f65c-3866-9b07-8592e1c40bd3 | -6.17576 | -42.61387 | 2024-11-28 03:38:00 | NOAA-21 | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fbbf9a13-0982-3342-b45d-7bfde14df090 | -5.19473 | -44.24884 | 2024-11-28 03:38:00 | NOAA-21 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 265d7882-35a7-3602-b2ae-d798dc78cdfd | -5.82315 | -44.11102 | 2024-11-28 03:38:00 | NOAA-21 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| aacac52f-34a6-3e5f-9344-7c258be8b6a9 | -6.17465 | -42.62025 | 2024-11-28 03:38:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 8d9fc0b9-6312-301c-b917-9b2d6e9b7138 | -7.28744 | -39.70166 | 2024-11-28 03:38:00 | NOAA-21 | SANTANA DO CARIRI | CEARÁ | Brasil | 2312106 | 23 | 33 | nan | nan | nan | Caatinga | 0.7 |


[Clique aqui para ver as próximas entradas](README28.md)
