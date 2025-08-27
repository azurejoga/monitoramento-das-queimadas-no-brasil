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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ad319976-7214-3539-9cd8-1ba462aa1a38 | -7.07975 | -43.64975 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 39cac681-c963-30f8-9d21-f247ea456094 | -7.25668 | -45.35569 | 2025-08-27 03:36:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e77baec5-8bc4-37e7-a58a-681f1dd7447b | -6.8991 | -43.13538 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 80b5c3f6-2f5e-3e71-8bfa-63261d11a395 | -6.88107 | -44.40103 | 2025-08-27 03:36:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3fbf2a0a-af2a-3b3b-9d5f-eac20244a158 | -4.88176 | -37.48469 | 2025-08-27 03:36:00 | NOAA-21 | ARACATI | CEARÁ | Brasil | 2301109 | 23 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a3d01281-28e9-3aec-8036-2f5fd3a32a86 | -7.01231 | -43.10687 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 59a92b66-e6e4-3ca6-ba9f-b2310c2f7e7f | -5.74788 | -40.44506 | 2025-08-27 03:36:00 | NOAA-21 | INDEPENDÊNCIA | CEARÁ | Brasil | 2305605 | 23 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 9a2e2e59-85ab-34fd-8178-5d7d5a927bec | -6.12565 | -42.95394 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 10a08d4a-72ce-32ad-96b0-c83fe87629f8 | -6.80119 | -44.34715 | 2025-08-27 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 7ade1efd-0ffe-3c4d-b9bb-9c5f22d85a0d | -6.95438 | -44.09441 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f6c64c25-2229-3b9d-887b-c1b2752ed60b | -5.62558 | -45.73007 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ad4bfafd-c675-32ad-b921-9e7e2bfb331f | -5.16759 | -37.63893 | 2025-08-27 03:36:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 8fdd4e89-4836-3c6e-b1cb-08a5f93362b9 | -6.13219 | -42.94821 | 2025-08-27 03:36:00 | NOAA-21 | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 7fda1593-6867-33e2-ae73-e0d771a2ae0f | -5.66008 | -47.4957 | 2025-08-27 03:36:00 | NOAA-21 | ITAGUATINS | TOCANTINS | Brasil | 1710706 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3ee03d15-f254-3185-9cb1-6f65d194328d | -6.18719 | -43.01158 | 2025-08-27 03:36:00 | NOAA-21 | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f03aa3d9-2ada-3972-88da-38a4275db0b7 | -6.97013 | -44.10469 | 2025-08-27 03:36:00 | NOAA-21 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc607674-2d03-39dc-968c-5ae7f7198042 | -7.17395 | -43.85826 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0085ce78-6227-35ed-92fa-8821e80eac81 | -3.48875 | -40.67549 | 2025-08-27 03:36:00 | NOAA-21 | MORAÚJO | CEARÁ | Brasil | 2308807 | 23 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a2afe7f7-5408-3799-8fec-95f0411663a1 | -5.09928 | -43.78952 | 2025-08-27 03:36:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6d79bd21-cfdd-32a2-bf8a-a43933003627 | -5.59458 | -39.5791 | 2025-08-27 03:36:00 | NOAA-21 | SENADOR POMPEU | CEARÁ | Brasil | 2312700 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 12875b95-d17f-3aa6-a3fa-1f76cd26e70b | -6.13159 | -42.95154 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 4970c89b-9778-3053-9ac8-f99ebc14d825 | -3.36137 | -43.37041 | 2025-08-27 03:36:00 | NOAA-21 | URBANO SANTOS | MARANHÃO | Brasil | 2112605 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e3f57db5-20e4-3951-85dc-c9258b2df375 | -6.80693 | -44.34845 | 2025-08-27 03:36:00 | NOAA-21 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 65a79ea9-b936-3b1a-8fa5-758bbd480808 | -6.13274 | -42.95671 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 9.0 |
| 9f931ff0-1110-3231-9677-689ab7738532 | -4.85003 | -42.89286 | 2025-08-27 03:36:00 | NOAA-21 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a9712cc5-aec6-348d-b828-35e5744af33e | -6.49123 | -44.68251 | 2025-08-27 03:36:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2f69df25-f4c4-3fc3-968d-f22e5e575c0f | -7.1738 | -43.8508 | 2025-08-27 03:36:00 | NOAA-21 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ddabde29-05f7-34f7-8d8f-a765356a43a8 | -5.10432 | -43.79455 | 2025-08-27 03:36:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3c262913-00f1-3f55-bc81-c2e82a7d5d37 | -6.84095 | -42.82455 | 2025-08-27 03:36:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 0eb1a6a6-b07d-3d53-90ad-b7664962939b | -5.53543 | -36.84681 | 2025-08-27 03:36:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 132ca4f6-9355-3642-b455-15c04d2a73ca | -7.65331 | -42.6632 | 2025-08-27 03:36:00 | NOAA-21 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0ccd0aa6-6023-3353-bdd1-c7b1a518b05e | -7.47694 | -46.00994 | 2025-08-27 03:36:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb59a590-d770-38ff-8f89-f2673d016e2f | -4.81991 | -46.00802 | 2025-08-27 03:36:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d2a15caf-bccc-3835-8492-c1e4d6181662 | -5.6325 | -45.72138 | 2025-08-27 03:36:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6bcc86f4-9452-3ace-b32d-eba2c5b2516e | -7.08527 | -43.6507 | 2025-08-27 03:36:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 777a539a-14aa-3f9a-bc5a-d27dedbfc59a | -5.87656 | -42.93518 | 2025-08-27 03:36:00 | NOAA-21 | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 74d81ad8-892f-3829-b682-9cd280772a2f | -3.37974 | -42.33318 | 2025-08-27 03:36:00 | NOAA-21 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 8c1c733a-9bb7-374f-8493-4674b887ce62 | -7.6603 | -40.15294 | 2025-08-27 03:36:00 | NOAA-21 | IPUBI | PERNAMBUCO | Brasil | 2607307 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 77b15a46-1407-3d2a-a475-29aadf370fbd | -6.44923 | -35.02211 | 2025-08-27 03:36:00 | NOAA-21 | BAÍA FORMOSA | RIO GRANDE DO NORTE | Brasil | 2401404 | 24 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 18bffa3d-0c04-3c05-93ea-45b95775310b | -8.9052 | -47.32793 | 2025-08-27 03:38:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1f879a83-477e-312a-83da-4c5449134c55 | -9.19798 | -46.73933 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b8346ce7-971c-3c9f-a24e-b04b9350da05 | -14.12422 | -45.40543 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0c7b6d0b-fd0f-3deb-9b7a-89aa70e9759b | -10.12752 | -47.43602 | 2025-08-27 03:38:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| cf713fe0-a1f3-35c6-8184-fdd5dc437227 | -11.14262 | -46.34253 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| c7879b5b-824e-3526-94ca-2c24610d12bb | -7.8836 | -45.86989 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| db15d000-e773-389b-b32d-d5417b24a1eb | -12.89711 | -44.64735 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 35a6fa9e-ed1c-3b53-bdce-e045d3228d3c | -13.06617 | -46.33474 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| bd1c89b0-72c1-38c1-89bc-30e09703cd81 | -10.76475 | -46.39256 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c018b702-3878-388a-97ed-a6439fbf8957 | -12.76956 | -48.1758 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 6940fa28-a13a-3907-a387-aa907f968e1b | -13.45404 | -46.85688 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| df5da0d2-20df-385a-8ca3-d487a74c6e86 | -11.64573 | -44.86098 | 2025-08-27 03:38:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fc851ee3-199c-317d-ad90-18d6631698de | -12.49812 | -47.23994 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 3b3a4335-e699-34b2-95f0-d100aab5ac42 | -12.7589 | -48.19397 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| e3c6979a-91d0-3e65-8829-4b27e5a69e1b | -12.90175 | -44.65179 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d3317f5-05b5-3301-b5d0-277664d6a70d | -13.40339 | -46.88352 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 827e0acb-3b38-3b40-ae57-7a04e6942e26 | -11.82644 | -46.79565 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f4e0bee-1024-3f6a-a808-241ed0dfd355 | -11.9199 | -46.74117 | 2025-08-27 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 430d4ea4-58cb-353c-9aa1-86762a55bbd1 | -13.82591 | -45.88925 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a8fd0794-3cc7-37ee-89a8-25a1c9dc1105 | -13.44789 | -46.85624 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 5d41c893-8b82-33af-b756-960c8c4c147e | -13.62585 | -48.20461 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| d48f82d6-e2be-3dbc-bc68-dc1fa5e3128c | -12.68859 | -44.40795 | 2025-08-27 03:38:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70cf5c9a-c6da-387a-92ee-233fb2a5f474 | -13.66496 | -46.88324 | 2025-08-27 03:38:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d5bb3308-6488-375c-a20f-bdc04eaabd7c | -13.17034 | -45.29107 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 04a9cd7c-842e-323e-9c00-7c2f88622aa4 | -13.50221 | -46.87327 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| be2264f0-519c-3d19-8d24-7b00e80e82bb | -12.57312 | -43.78624 | 2025-08-27 03:38:00 | NOAA-21 | BREJOLÂNDIA | BAHIA | Brasil | 2904407 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| aef77c02-5333-3c03-83f9-1c7e30c7a31a | -8.85717 | -47.1819 | 2025-08-27 03:38:00 | NOAA-21 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 4ba8fd14-4eba-37d8-a661-16489ae92086 | -12.95302 | -44.58572 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| bfb08e55-bb1e-3783-937f-c3bad18b4acc | -11.25037 | -44.99304 | 2025-08-27 03:38:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 9bdedf19-a58e-3c96-ba42-f6c798f040dd | -14.12348 | -45.40907 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2a3d7532-fb71-3435-937e-29520a3cffc9 | -14.76351 | -47.93251 | 2025-08-27 03:38:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 47e79f4b-8974-3807-91b0-9cfed9325876 | -14.1288 | -45.40645 | 2025-08-27 03:38:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2222d8f7-edb8-3d51-b93d-461b7722c827 | -13.17082 | -45.28703 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9ee81068-79fb-3874-a856-26f644dd215b | -12.70053 | -48.1883 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 4d613029-30a6-3f71-8aa0-6b38bdfcd1b4 | -9.17262 | -40.60189 | 2025-08-27 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 70f5c0f6-6835-3d81-868d-f7530d211c87 | -9.19907 | -46.73367 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 719fd7da-4f1a-33d9-bb61-e6c858636e2f | -9.0137 | -40.34377 | 2025-08-27 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.8 |
| d33adc8e-1380-3e67-91ce-35947c223374 | -9.16828 | -40.60119 | 2025-08-27 03:38:00 | NOAA-21 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 8.4 |
| 271f9d1b-4664-33ba-ba0d-713c8987b4d4 | -13.41456 | -46.86533 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 22f3bba1-84ae-39a4-af31-8566a483d7e6 | -12.87764 | -48.10771 | 2025-08-27 03:38:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 27.5 |
| 05316ad2-90d3-37f2-98a1-caf79fd1cc33 | -8.09145 | -45.01678 | 2025-08-27 03:38:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 68f84679-9850-3d53-9683-0a851f0b2185 | -11.81216 | -46.80258 | 2025-08-27 03:38:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5a9e50c0-9af5-3210-a2c7-081db0d84215 | -12.25127 | -45.0603 | 2025-08-27 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| db634f99-605f-3ea9-bbf8-c48f6fdebd07 | -7.91872 | -45.8761 | 2025-08-27 03:38:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6a0de55c-6581-3c51-ab73-d04197d352e5 | -11.91289 | -46.74838 | 2025-08-27 03:38:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05b0e7c6-ad34-3a99-9bb1-d64ac91a6789 | -14.64133 | -41.62419 | 2025-08-27 03:38:00 | NOAA-21 | PRESIDENTE JÂNIO QUADROS | BAHIA | Brasil | 2925709 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 32922b99-844d-38b6-9434-c0438caea707 | -12.89842 | -44.64062 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 7356f906-bbcc-3a1f-bd34-656d1bb6d5a5 | -13.17512 | -45.29589 | 2025-08-27 03:38:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 753714ce-747a-3a21-b74c-8f94c4d17941 | -11.74788 | -49.09158 | 2025-08-27 03:38:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4c23c926-028f-3636-924a-42d10646affd | -13.62473 | -48.20991 | 2025-08-27 03:38:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 16eab454-e1e9-3443-8580-51122d482ae4 | -13.39733 | -46.88235 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 93ae50b9-a20a-3825-bdc5-772615514380 | -11.57896 | -44.6465 | 2025-08-27 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3d11b98b-38fb-3d16-94c9-413a2bdd2954 | -8.45651 | -43.67489 | 2025-08-27 03:38:00 | NOAA-21 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9d48e37a-3715-32d0-b719-d30328993b64 | -13.43116 | -46.99931 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| ed082aa6-01c0-3dc5-ab6a-bddc269bc386 | -13.07488 | -46.32218 | 2025-08-27 03:38:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 90e0d3cb-083b-3ed3-9149-ac7b02be27d4 | -10.77356 | -46.38007 | 2025-08-27 03:38:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 10013417-b3ae-3aad-b4af-1e8289b4746c | -13.49679 | -46.86292 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ad6d13a5-7352-3286-a1cd-46977135d614 | -13.50563 | -46.88144 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c29ace07-0034-3857-b5eb-e8ec8392ef1b | -12.24575 | -45.05923 | 2025-08-27 03:38:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| bcf2627c-90a3-3102-b4ad-399ef0484e7e | -11.57283 | -44.64902 | 2025-08-27 03:38:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b9aee796-cf0c-32cd-9243-2deb6a0dc293 | -13.45994 | -46.85875 | 2025-08-27 03:38:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |


[Clique aqui para ver as próximas entradas](README19.md)
