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

## Dados Diários - Página 34

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ca9c275-fb7e-3377-a391-1b27546bf9fb | -11.04908 | -45.40184 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 302077cc-4fad-309c-a2a1-7cac39a5469b | -10.01478 | -47.06726 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b8b3b9a2-d9c9-39b8-87df-5a101b139168 | -9.34871 | -46.59443 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5713bda7-f87a-3cfd-822d-3bb5d63a608b | -6.98333 | -47.35976 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 89f8b235-9b4c-3d12-8433-8bc2f72fadb2 | -9.86128 | -48.27527 | 2025-10-24 04:38:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 64549dfb-ab6a-32cd-8317-b579009a3d42 | -2.63606 | -54.8674 | 2025-10-24 04:38:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c9e1fd02-9266-3604-9fc2-aa762c632316 | -6.43128 | -45.66837 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3c0c89f-709b-33bf-9f0d-bd6e5d5d4522 | -9.26036 | -45.34492 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1eb6b01c-9214-3489-87ad-d3156195ce0d | -6.89399 | -43.61939 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a37c6d44-06fd-3d75-899a-6c6b2d7cfe26 | -3.38601 | -52.96906 | 2025-10-24 04:38:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 90a29710-2298-3dc2-8407-149a23067991 | -8.05754 | -46.48346 | 2025-10-24 04:38:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 534f4686-374d-3746-b813-b179d512eabe | -3.84564 | -48.16159 | 2025-10-24 04:38:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ffbcadf6-ca02-310f-b7a3-75f445564d12 | -3.79202 | -50.372 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 244da1b8-517a-394e-bc9a-c88226586e36 | -10.64218 | -44.78289 | 2025-10-24 04:38:00 | NOAA-20 | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 94845c6f-b539-3f62-b273-a92d2ca7306f | -3.32123 | -51.55707 | 2025-10-24 04:38:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cfb22bbd-a42c-37df-8b58-1ddb322e375c | -4.63493 | -42.51475 | 2025-10-24 04:38:00 | NOAA-20 | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 600aa9fe-1603-38ce-b0be-29cf47114d5a | -6.30267 | -41.88481 | 2025-10-24 04:38:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 26182067-b5b4-3e16-bc8a-92cf3ddcc65d | -2.54369 | -51.23492 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e46c680c-ee18-3570-bb8b-7c717bd23aa2 | -11.04457 | -45.4048 | 2025-10-24 04:38:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 34b1ae94-141a-3c48-830d-635599f48c59 | -5.62243 | -50.01123 | 2025-10-24 04:38:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f56a1a2f-faee-30a3-a05d-e1522f879821 | -3.82657 | -47.47812 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d342e093-9146-3ac7-9608-035b183aa22c | -4.27636 | -40.70747 | 2025-10-24 04:38:00 | NOAA-20 | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.3 |
| bd6bd2d3-1c10-377f-b43c-44f927be770c | -7.78149 | -45.40435 | 2025-10-24 04:38:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8ac18ad9-c2d0-3662-8d8a-28be10898e0d | -4.852 | -42.966 | 2025-10-24 04:38:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2c28a9ca-3a0a-3bb8-9ecb-76f6597fe7b0 | -3.99701 | -43.28164 | 2025-10-24 04:38:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9bf22be1-d1fa-3707-ac55-44c718282b73 | -9.36936 | -50.8102 | 2025-10-24 04:38:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c2545734-3173-3d43-8d80-7dab5ead3ad7 | -8.10975 | -47.04735 | 2025-10-24 04:38:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e0aee68c-35f6-384f-90e3-393a97b84604 | -7.45808 | -49.40733 | 2025-10-24 04:38:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aca0af7f-f84a-3dfb-9831-53fce60108f6 | -8.56434 | -44.86601 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1eea8b6c-2cc5-3cc2-9bfa-cb91a1be4478 | -7.55306 | -47.36201 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 194b2157-e2ad-3b2c-a6a2-cafb7355eb85 | -9.7818 | -43.85998 | 2025-10-24 04:38:00 | NOAA-20 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| b776587d-1e7f-366e-9142-1763bbac1719 | -9.24268 | -46.40277 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 6bf12b87-94b4-3b38-a35c-9d1af6f592a5 | -3.14895 | -50.16072 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dab541ec-14f1-3683-80a4-ab8cf093d562 | -8.342 | -46.18198 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c82db747-cfd2-33b2-9365-46e7e0d6cfea | -4.28281 | -48.25475 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 45be6d7b-c568-36ff-966a-bea71b729b10 | -6.44668 | -43.81828 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 809e9608-f7ac-3ac7-a5e0-eaae36dd253b | -2.87772 | -50.71651 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 89732bcc-3df4-33a4-8c86-800334040b18 | -3.87141 | -45.56228 | 2025-10-24 04:38:00 | NOAA-20 | TUFILÂNDIA | MARANHÃO | Brasil | 2112274 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| beeffdcb-b8a1-3bbd-90cf-096d53b4aa53 | -4.84262 | -47.80497 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| afecc13c-1507-3fbe-8960-180f507feed5 | -3.15953 | -49.17226 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48565d8f-5ed3-347f-9990-f9dbcf87ceab | -4.03419 | -51.15928 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 60a22a8c-e3c2-3d6f-988d-ee382c406199 | -3.51005 | -45.83986 | 2025-10-24 04:38:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9905bf5b-d270-31db-9a6a-9b36702c5b5d | -8.64452 | -44.79257 | 2025-10-24 04:38:00 | NOAA-20 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a31f01b0-6a74-3d03-afb1-44455cc22c66 | -9.2332 | -51.83372 | 2025-10-24 04:38:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2459edc4-65d9-3a66-be1b-e36cb815609f | -4.82076 | -48.67891 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6eb8d46f-1623-382b-9ee8-f32c072e27df | -6.13087 | -41.72438 | 2025-10-24 04:38:00 | NOAA-20 | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 2f648895-f1eb-3ab2-8461-1b6d7c8959f6 | -5.0203 | -46.82213 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cca07cc0-305a-3afe-ad00-4f511627e6fe | -5.48137 | -48.86437 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8752ff3f-101f-386f-a2be-b3a47e127824 | -9.26925 | -46.4516 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c8bf00e6-e1b8-3755-a9e5-f1bd6b3d8823 | -4.47425 | -48.11792 | 2025-10-24 04:38:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cfcf0e87-5301-3c53-8da1-58ea91fc8cc7 | -3.92806 | -47.69983 | 2025-10-24 04:38:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 36c2dbae-2d82-3794-93fb-5715d0b37550 | -7.48784 | -42.57632 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| d81a703e-f993-301b-baea-9f95c4cf3334 | -6.53725 | -41.68754 | 2025-10-24 04:38:00 | NOAA-20 | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 99797379-6e7e-30ec-983a-b20dac1a6423 | -9.99996 | -48.10025 | 2025-10-24 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9bfd9026-3336-39a5-ac1d-9f793f107a79 | -6.89823 | -43.61998 | 2025-10-24 04:38:00 | NOAA-20 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 59e5fb62-0311-3493-92f9-18c384ddb6f0 | -10.04272 | -47.10114 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5995d359-4a5d-39d4-b547-dd97c2084067 | -6.43062 | -45.67279 | 2025-10-24 04:38:00 | NOAA-20 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4bef5754-b4d9-3216-9f29-278daf55069a | -9.27745 | -46.97316 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| ac5d807e-55bc-3e25-ac55-2b4856aa179d | -9.92844 | -47.99702 | 2025-10-24 04:38:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 00100df7-7691-34c3-b461-30aaa77119ee | -8.68697 | -47.05569 | 2025-10-24 04:38:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 768edbcd-b248-3fe5-9896-bcffb0d508ac | -3.28845 | -50.19303 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 96a0f958-a083-355e-8e0f-b15725432849 | -9.30806 | -45.20783 | 2025-10-24 04:38:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f8744135-6b42-3fd1-b421-4af83fe72ff0 | -4.98429 | -44.1464 | 2025-10-24 04:38:00 | NOAA-20 | GOVERNADOR ARCHER | MARANHÃO | Brasil | 2104503 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| faab473c-a7a2-38f7-8137-72ec1d817cfc | -9.2673 | -46.46467 | 2025-10-24 04:38:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3441fefc-5391-3b64-97ff-4317d0311adc | -3.67478 | -52.0118 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c0fe784-bc09-36a2-a147-2317308504e3 | -5.56766 | -46.52475 | 2025-10-24 04:38:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2fc96f32-a4bf-3a97-b79b-c31f946e938f | -6.98438 | -48.68103 | 2025-10-24 04:38:00 | NOAA-20 | ARAGOMINAS | TOCANTINS | Brasil | 1701309 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d8a7f70b-da20-3288-9fc9-5ddbdd9d4f1c | -6.44629 | -47.2756 | 2025-10-24 04:38:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bbe1ff6d-4839-35c4-a85d-e340ce35f55d | -9.63619 | -46.89633 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 183b7c9a-f2e7-3eb2-8694-a2d41c0abd15 | -7.18654 | -43.86709 | 2025-10-24 04:38:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d679335-f129-3409-9e87-2140cd4de745 | -3.49187 | -50.05571 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 27656c4b-a75c-31f0-9b60-45d57ea37919 | -2.58337 | -51.34762 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2654a69a-b25e-30e4-bf04-909a1b7f7bbd | -7.54903 | -47.3653 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 13.5 |
| ce817105-619d-3931-b05f-80374eedde07 | -3.24151 | -48.76137 | 2025-10-24 04:38:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5436ef83-0e7e-3b39-8718-1991ab1447a5 | -9.23641 | -45.62301 | 2025-10-24 04:38:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2d2afdc4-8cd5-34e1-81b6-4d52cd154463 | -3.12289 | -49.10235 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 248ad170-9a69-379f-8dee-f8c0f6a959e7 | -8.32732 | -46.25463 | 2025-10-24 04:38:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b2f9bcd8-a70f-3f4e-8cfe-d95c153765ba | -3.79854 | -51.76152 | 2025-10-24 04:38:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cac74eb0-b746-308e-883c-f31c5ee773f1 | -3.69849 | -49.56691 | 2025-10-24 04:38:00 | NOAA-20 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0024d388-22b0-379f-8d3d-b385ef423c51 | -7.2997 | -46.9549 | 2025-10-24 04:38:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 771ca94f-b1f6-33cd-89dc-5dd2f74ba617 | -6.78868 | -45.42626 | 2025-10-24 04:38:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| bab96346-1e9c-308c-bb8b-99090ae8457e | -6.85179 | -46.92992 | 2025-10-24 04:38:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| aefc673d-8983-3bce-b632-7f5541689bb9 | -3.15622 | -49.17174 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2e057106-9be3-3569-9482-9ec59cc4f2a2 | -4.60807 | -46.59466 | 2025-10-24 04:38:00 | NOAA-20 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 959c9a6a-6901-3c6c-98fb-2b63f305d876 | -10.04287 | -47.07568 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c4fe18bb-bbac-3559-91d1-56eed6b5fd6a | -2.59828 | -51.34577 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 10c46b1f-c238-3ab1-9bba-279c68b4926f | -2.80314 | -49.14755 | 2025-10-24 04:38:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 12f1a2e2-1352-3049-a3f2-1a9c9f39b588 | -2.86367 | -50.72231 | 2025-10-24 04:38:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5c481910-1a3a-3a2f-aff4-1d528c33424c | -7.63012 | -48.39155 | 2025-10-24 04:38:00 | NOAA-20 | NOVA OLINDA | TOCANTINS | Brasil | 1714880 | 17 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a8d155d3-682e-329b-8525-6f6e00ac6b87 | -3.32838 | -50.22533 | 2025-10-24 04:38:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea29d814-e0f3-3c1d-9ca1-f327b3dad75b | -7.62683 | -42.1969 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b4f10661-aa7a-3e29-bcab-a6b5cd738d09 | -9.6043 | -46.91273 | 2025-10-24 04:38:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| f4d2bc46-13aa-3406-9c0e-2c11b75549a3 | -7.63084 | -42.20256 | 2025-10-24 04:38:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1fbbfd2c-217f-366c-8977-a8a7c188268a | -6.44199 | -43.82136 | 2025-10-24 04:38:00 | NOAA-20 | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5f27c6d5-694d-3a49-9a40-bcfa90745437 | -11.06436 | -44.78585 | 2025-10-24 04:38:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1e43476-b137-3885-8e59-e4dceee65ebd | -6.28754 | -47.01308 | 2025-10-24 04:38:00 | NOAA-20 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d00cd274-b165-3bdb-a5d1-13fcf872de80 | -5.59793 | -45.19107 | 2025-10-24 04:38:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbfe05ac-809b-345a-9f55-382de6b1229d | -4.87098 | -47.53613 | 2025-10-24 04:38:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c8643c5f-b8f8-3b88-a65c-47a1599f9c7e | -6.46882 | -44.12695 | 2025-10-24 04:38:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 533287b2-cc54-3faf-8c90-a8b1150b4145 | -9.93039 | -47.46521 | 2025-10-24 04:38:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README35.md)
