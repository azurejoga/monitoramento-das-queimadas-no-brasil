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

## Dados Diários - Página 26

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8ada7feb-6e1c-3f30-91ee-f08066541522 | -11.05441 | -44.60053 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8b4f95fb-d87e-36b0-bdf5-3d16eefe85d5 | -11.18277 | -55.01968 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1f9ae557-af0f-3c60-a4d9-77160913d645 | -12.54547 | -45.62647 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1258bbe3-77c3-3955-8361-33664be90c95 | -9.05863 | -49.53271 | 2025-08-23 04:02:00 | NOAA-20 | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| da61d512-ae5b-3cf1-b27f-30ea9badbc46 | -11.18571 | -55.02905 | 2025-08-23 04:02:00 | NOAA-20 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 90ad3085-2f4e-3a87-82a7-2925eff14c4a | -12.94428 | -46.30115 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7edf2f98-270e-3fc8-b93b-98209dab9794 | -13.04545 | -46.34397 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 58619297-0e6a-39b8-b3ca-354b4d00bb35 | -13.47449 | -46.8982 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b248cc8-8f25-3356-9355-4e415da2badb | -13.47854 | -46.89897 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3a899e75-82cd-3add-81d4-5c016dde9d67 | -11.13407 | -44.77142 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 6476a221-d929-30b7-a049-2191b28d38ff | -8.46351 | -44.62844 | 2025-08-23 04:02:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 494c0178-a3e9-3900-b37f-f0c9612138ec | -15.22344 | -40.09001 | 2025-08-23 04:02:00 | NOAA-20 | ITAPETINGA | BAHIA | Brasil | 2916401 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 37fefe17-00c2-3459-a7ea-48e17e32720d | -13.39574 | -46.34671 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e230cc71-6840-374d-8116-d9c3326b13bd | -12.95679 | -46.2993 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| b476c2e3-3c67-3f1f-a372-5aea099846c1 | -14.78764 | -45.50062 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8e7e4aed-9c45-382d-ba83-8743d80951f1 | -8.89608 | -47.32857 | 2025-08-23 04:02:00 | NOAA-20 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 813cf905-4ee6-3cbc-8a51-1571cb1120e4 | -10.85908 | -45.19945 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e9d52d75-cff1-3ecf-978d-dec1c9308a76 | -14.93909 | -48.01038 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3561c320-6c37-38bd-adf8-3b4ab0a5b0b7 | -13.3781 | -46.21782 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0208fb14-a392-36cb-8021-567f57142e37 | -13.41688 | -46.27172 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 46.0 |
| 503912b6-1196-39b6-9cac-6ea22eb58879 | -12.93939 | -46.30589 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| e1d33cf0-d5ca-3f78-9272-d8aa0677a06c | -14.79557 | -45.43376 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fad65f36-b6ef-3bb5-bb07-5b7ec5eceae4 | -13.04335 | -46.33284 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3cf514d4-f332-3cdc-8f2b-c879a9a4e5e8 | -11.13114 | -44.76631 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b900a377-59ed-3d8c-aee7-34ec49b53b8f | -10.22048 | -47.5672 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 317d3324-a48a-3052-a9c4-e1cf5d6e826b | -13.04637 | -46.33879 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7dd4447-b497-3809-9325-e41d3ce7b2f0 | -12.99711 | -45.21753 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 79476a68-cfe0-3c9a-bb06-0d9bc931ad3f | -14.78554 | -45.49105 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6096876d-4e58-31a0-8f02-78f7e07535d3 | -12.18679 | -47.21049 | 2025-08-23 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5d318ac6-9cc8-3995-983e-bffff471b06b | -12.31441 | -49.99257 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2165a1d5-0a00-3800-8bdf-dcdffed07189 | -9.44626 | -47.65165 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 56820a9c-d86b-30d8-93f3-7576c0f581ec | -12.17857 | -47.2101 | 2025-08-23 04:02:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 820e0fcb-9f02-3248-842d-69b8a8b20ffd | -13.37189 | -47.51345 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| c17a2e63-1308-3224-92be-e47910bad542 | -10.64026 | -50.13253 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ae750e03-0549-377d-ac8b-3e9c4b6cabc6 | -10.6159 | -47.35338 | 2025-08-23 04:02:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7f442dbf-e321-3a85-950b-47ec34ea8c1d | -12.79012 | -48.72124 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2896e55a-c5ef-3102-9005-db00e0f8573d | -14.7481 | -45.40456 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8e97ad7-5434-3a82-b53f-cd9d57bad6d1 | -14.94685 | -48.01593 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 9491bf6c-88e3-35cd-b170-b58586601801 | -13.46362 | -47.02895 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| b1c97c46-0a82-314a-985e-bf1f76d2dcfc | -9.56378 | -48.50595 | 2025-08-23 04:02:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| c3385c98-8c57-3fcd-987d-be697183e0ae | -13.49926 | -47.04224 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a2813373-b0b5-3b27-b47b-9708a8f155ee | -14.9108 | -47.99709 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 08a4bab7-abaf-3184-b076-4932bee16fb2 | -12.99108 | -45.23031 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 18.9 |
| 341d4691-0554-378a-b6a9-08e5d073ead3 | -13.03645 | -46.32592 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 3b996cdb-c1a0-3d7e-a3ec-b6c125d6d004 | -13.48837 | -47.03222 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0cf55148-ba53-3a87-ae96-bf796d6a2bbe | -12.94034 | -46.30048 | 2025-08-23 04:02:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 39141092-c448-3d4e-97cd-5c610d221aa9 | -13.37004 | -47.49961 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db08cfa8-8f9a-343f-8eec-c88d5d503975 | -11.12744 | -44.76566 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 65008e19-d9dd-366a-80b6-44fc7bb82d86 | -14.4769 | -46.04943 | 2025-08-23 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 29eefb94-571b-3d49-a9ee-7fe1a97e47e3 | -12.29815 | -50.00594 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| b929a7fd-1a3b-3f59-ad5c-c58c00a09920 | -14.47521 | -46.05898 | 2025-08-23 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 54f4779f-2fac-32a8-8945-46ceb401c4ff | -11.32726 | -47.84776 | 2025-08-23 04:02:00 | NOAA-20 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 2a9105fd-ed80-3347-aa69-f3308d2f8736 | -13.04037 | -46.32671 | 2025-08-23 04:02:00 | NOAA-20 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9ff3265e-755f-3d86-a8a1-8e0d29292c00 | -13.1842 | -44.03807 | 2025-08-23 04:02:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| daf8abf5-42c0-3e98-b8c5-a30e433f54fb | -14.79269 | -45.4287 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cce7c894-5823-3b16-aeb5-b4fdc24bc3b7 | -9.82587 | -46.3764 | 2025-08-23 04:02:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4b7c2f98-003a-3046-9c4a-774a017d2e11 | -14.1208 | -41.88865 | 2025-08-23 04:02:00 | NOAA-20 | BRUMADO | BAHIA | Brasil | 2904605 | 29 | 33 | nan | nan | nan | Caatinga | 0.4 |
| 3b4171ad-901d-3272-9e4d-2a4e39dd77bb | -9.55007 | -47.93717 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e07ffe8d-4c53-3b3c-849a-7e8c3e6b957c | -14.79052 | -45.50577 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 53e4525d-bc09-3e5d-b810-837b5a699768 | -8.84811 | -49.8606 | 2025-08-23 04:02:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f93b9552-9b7b-3a1b-b7f2-15d49cf37c67 | -8.52814 | -48.83541 | 2025-08-23 04:02:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9dec2699-4c61-3acc-871f-335e74fd6a98 | -13.37693 | -47.5097 | 2025-08-23 04:02:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 1982ef70-166d-379b-a907-51393016dff2 | -14.92145 | -47.32333 | 2025-08-23 04:02:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| 4a2951ae-bc25-308d-9aad-355ffc754e3a | -15.90571 | -42.30511 | 2025-08-23 04:02:00 | NOAA-20 | SALINAS | MINAS GERAIS | Brasil | 3157005 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 191a39f2-a5f2-367e-ac45-395376a2a174 | -13.45952 | -47.02831 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d740a2e2-a4e9-38f0-a734-d348ee6dbd3d | -9.8758 | -47.80806 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4540de2f-93a4-3d0e-a113-c66cd613adad | -13.17425 | -46.91595 | 2025-08-23 04:02:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6a0ec74c-ce62-3c82-8c5a-e5e845d759e3 | -11.98006 | -44.89175 | 2025-08-23 04:02:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4282b05a-e806-3d24-80e4-b971dcc5072c | -12.77803 | -48.71687 | 2025-08-23 04:02:00 | NOAA-20 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 182f96b3-3dd8-3012-bc2e-93f383c710d6 | -8.78194 | -46.74785 | 2025-08-23 04:02:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| ab84c8f5-739c-30e1-956a-fe371e81e725 | -14.79633 | -45.42939 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e68247dd-5686-3338-85c1-3db544382b9a | -10.62418 | -50.16022 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 31a28707-4e2e-3b32-b7b5-0ffdd201a2eb | -14.80209 | -45.43955 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cb0c9976-25fa-3170-85af-b62bac251aa7 | -14.80419 | -45.4491 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87e91dc8-b871-3d4d-9210-99adec37d6a0 | -10.2107 | -47.57026 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DO TOCANTINS | TOCANTINS | Brasil | 1711951 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c0b4c2e7-b7bc-39e2-b567-b26d505d12f5 | -9.44541 | -47.65644 | 2025-08-23 04:02:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 510dfe76-644d-3111-9d7a-5a1e4739831d | -11.05883 | -44.59674 | 2025-08-23 04:02:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2335fb70-4ef7-3273-841f-7236b1ea653f | -12.30436 | -50.0009 | 2025-08-23 04:02:00 | NOAA-20 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| aca0d4c7-4a83-30f1-9ad8-ebb7358746f0 | -14.47606 | -46.05418 | 2025-08-23 04:02:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 91ff8e84-a65f-3fd4-94a2-52216597ae0d | -14.78842 | -45.49618 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 2bd475c6-6f49-3845-bbb5-9c29ca0680df | -11.19272 | -55.03047 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| b31fea58-932f-30b1-b51e-4d6e26ee2264 | -11.1954 | -55.02928 | 2025-08-23 04:02:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 768b0b75-61cf-3072-b608-c27abbd93018 | -14.8152 | -47.94966 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 30a10b74-e574-3d5e-95d9-75f59b8d8e4b | -12.66188 | -44.52731 | 2025-08-23 04:02:00 | NOAA-20 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 144f987c-deff-3a3e-bf35-27f5e1b41fac | -15.06475 | -48.48528 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| eeedc5a3-e77e-3c78-a5e2-90c77a296ac5 | -9.37413 | -48.249 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| cf3c3b55-5dfd-3561-9efb-d179c20a6b1a | -14.79572 | -45.49759 | 2025-08-23 04:02:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fd1db33e-8ce1-3862-a355-41e65187fb41 | -12.70231 | -48.10229 | 2025-08-23 04:02:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c4104309-b5bf-33f5-8900-c829ac4c4215 | -9.78611 | -41.78082 | 2025-08-23 04:02:00 | NOAA-20 | SENTO SÉ | BAHIA | Brasil | 2930204 | 29 | 33 | nan | nan | nan | Caatinga | 1.0 |
| c64f0f9f-76cf-33ec-bf1b-db74151d6079 | -9.37322 | -48.25417 | 2025-08-23 04:02:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4e319039-9c74-3c55-92c4-5c6d53304320 | -13.33197 | -40.34198 | 2025-08-23 04:02:00 | NOAA-20 | MARACÁS | BAHIA | Brasil | 2920502 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| b825e460-29e3-3659-b69c-1d291c92ae1b | -12.94333 | -46.30653 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| ddef3bd9-b44c-3ac3-a4d3-1a60085b843b | -12.95777 | -46.24752 | 2025-08-23 04:02:00 | NOAA-20 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fa4ab96e-af77-3413-bd1b-d304faf97052 | -14.94408 | -48.00705 | 2025-08-23 04:02:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 287a0497-6a35-32a8-8c12-b7a88f8da4dc | -13.37152 | -54.40549 | 2025-08-23 04:02:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 167053f9-77e5-3ecb-9380-73f15850f086 | -11.7826 | -46.41174 | 2025-08-23 04:02:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3a85700f-b846-3529-adaa-cbf9133c2134 | -8.1575 | -47.31342 | 2025-08-23 04:02:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b398ae19-1f69-3396-9a70-69b99beacb69 | -10.74249 | -48.25827 | 2025-08-23 04:02:00 | NOAA-20 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 3a78c06a-7a37-3bde-aba6-7969d5598598 | -10.63438 | -50.13478 | 2025-08-23 04:02:00 | NOAA-20 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 526753cd-1422-3d8f-867d-bf9b7f264a8c | -15.06832 | -48.49039 | 2025-08-23 04:02:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |


[Clique aqui para ver as próximas entradas](README27.md)
