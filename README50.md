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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 009b1918-d3c3-3987-9e57-b2aa57d0315c | -13.60948 | -47.31288 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3b0cbcad-e70f-3ada-bd61-0f65d304182b | -11.0467 | -51.72815 | 2025-09-27 04:46:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| ea4de998-eec3-3b77-9b89-79250cbb86d0 | -11.97402 | -47.88226 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| aae6153c-182d-3d04-905a-6516e061db8a | -13.79343 | -48.334 | 2025-09-27 04:46:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 133e57fb-f1c4-3bb1-bf3d-3a2c2a90d5ed | -11.61126 | -45.42844 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0ec12a3b-f00e-3ba8-a472-01cac902fd48 | -11.67179 | -44.46685 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 41e7fd8a-4223-302a-a9db-6322e8e44f7b | -13.6255 | -48.07991 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e3e263f1-d228-36c3-8831-f68c41781780 | -10.17821 | -46.92739 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c9dd7506-0e42-3fbc-b539-cf027f6e464b | -15.27981 | -46.4348 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6a7a6bb1-5dc2-3065-b6fa-bed6150805d0 | -12.02981 | -47.07116 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 14.8 |
| fd0a6605-092d-3789-8f3c-9e5a1dc45e32 | -15.27926 | -46.43914 | 2025-09-27 04:46:00 | NOAA-20 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 66f00106-31f0-33e3-aa78-8bc146d0709b | -13.83081 | -47.95815 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a248eafb-cdf0-36a2-9ce7-a9287bbca1f9 | -15.9394 | -57.49311 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 809c5b30-eeb6-3864-985c-0c4497e6034b | -13.75558 | -47.86775 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee43093e-b0c9-35f0-be1b-d31b9cde3645 | -15.42787 | -48.22076 | 2025-09-27 04:46:00 | NOAA-20 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| b2c26b63-1bf5-3631-a788-91767ae248c3 | -11.36773 | -45.00644 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 477b3653-3924-338e-9aff-5079f716d1d4 | -13.50069 | -47.4121 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e4650158-595e-3168-b147-52e5ffb2f3de | -11.34866 | -45.01218 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d92aa51a-ae1b-3211-89b7-2cc536b080f3 | -10.11137 | -45.33488 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 935f26f7-a48a-378c-848c-d3f90a0cf424 | -10.39497 | -46.13127 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f18e931b-72e4-361b-8c96-64be65738391 | -14.46591 | -46.84641 | 2025-09-27 04:46:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c8bdd882-5560-3f60-85c2-3ddec2224feb | -14.78066 | -60.18403 | 2025-09-27 04:46:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 501de976-8ea1-3ce9-9909-412d423ccc35 | -13.75459 | -47.87001 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 37212c2c-f06b-3c69-b1fb-b3326c6f3276 | -13.6312 | -48.07267 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| a25d1e4c-e1c7-3174-8823-933c59449dc9 | -17.10709 | -46.87146 | 2025-09-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| eda95d89-966a-39c7-9225-c36ccaec758b | -10.16275 | -51.56144 | 2025-09-27 04:46:00 | NOAA-20 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3df0ab05-0f3a-3f15-92ac-7207a16be2b2 | -11.54965 | -45.29091 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 174789d4-0361-3c4e-baa6-526830eb590d | -17.11156 | -46.87162 | 2025-09-27 04:46:00 | NOAA-20 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 176563ad-3883-3147-bb38-65e4f67df2e8 | -10.92774 | -48.82836 | 2025-09-27 04:46:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b253d0d-2fec-3316-87cc-2756c19e69d0 | -15.90421 | -57.49949 | 2025-09-27 04:46:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 69b247fb-1499-37c6-b920-1faa2357d66c | -11.68976 | -44.40413 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4ffae7bf-4c41-3a82-957a-44e8c2124143 | -13.61297 | -47.31624 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c8d47a76-7b61-3dba-b954-7f5cf93e371d | -14.63486 | -48.29725 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 09280d96-a112-385f-b90e-287455b5ab21 | -16.71371 | -51.47931 | 2025-09-27 04:46:00 | NOAA-20 | PALESTINA DE GOIÁS | GOIÁS | Brasil | 5215652 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0e961565-118d-35fc-9009-1174a7e60ace | -11.98831 | -46.61209 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 85a50876-059a-37e0-aee6-4f9e136c6965 | -12.29603 | -47.21436 | 2025-09-27 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| d13f6cf8-6399-3067-8115-69466ef4488f | -12.65032 | -51.67701 | 2025-09-27 04:46:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 25223564-102d-3a9c-b05d-1e0738dc599f | -11.65061 | -52.86785 | 2025-09-27 04:46:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cde5e625-53c9-34fd-90ea-69a2d3515447 | -10.48958 | -48.05304 | 2025-09-27 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d7d69546-94d1-3730-b2dd-9401aeab18b9 | -12.96758 | -48.90881 | 2025-09-27 04:46:00 | NOAA-20 | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 1cac183c-c60c-3937-a1ff-ad6ffc5e0778 | -11.97897 | -47.90265 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 00d7636f-5192-39f5-ac16-23c146b36a75 | -11.97797 | -46.61481 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bee7de4d-a13d-3137-b66e-1ef03b898187 | -13.62922 | -48.08712 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6304581b-755e-3db6-afaf-468064523749 | -13.33727 | -47.302 | 2025-09-27 04:46:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 07b40e80-a09b-37fd-bc65-a1b62a58bc22 | -13.62597 | -48.08189 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 4966d465-1ca6-3da5-a9c7-c4edb2dedca0 | -11.96361 | -47.90028 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a1581d82-ae6a-3051-9b59-3bccc2bbf905 | -11.96429 | -47.89545 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 84c5fd81-8216-38e2-93d1-6fad23bb5df3 | -14.57153 | -49.10958 | 2025-09-27 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9e1d9118-401c-3fb5-b70d-4fbb38ac7fc7 | -11.69313 | -44.45348 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ee557967-a861-3bfc-8f1c-e0f01e5bc802 | -11.34804 | -45.01348 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d47eb6c9-21d9-3999-9432-51a849bf3d63 | -11.43385 | -44.96929 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 990e390c-b740-3608-9c15-32cc3f1b3d59 | -13.80819 | -47.91898 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a80c407f-83aa-35d6-9f49-28898b5b00cb | -14.63098 | -48.2966 | 2025-09-27 04:46:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9ae2495-c016-3293-aebe-2ac941676d7c | -15.0317 | -46.96265 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 86fcc554-7962-3023-bfba-4f5c92d4e156 | -12.03438 | -47.06812 | 2025-09-27 04:46:00 | NOAA-20 | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 12871d9a-a5f1-36a5-bf90-b3fd97a90a41 | -10.88973 | -53.75323 | 2025-09-27 04:46:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f948e398-4cdf-3a86-a438-af0a177c3bf9 | -10.12023 | -45.33609 | 2025-09-27 04:46:00 | NOAA-20 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 72ea0d7c-5cc8-358b-992e-48d40d67bd3d | -11.6279 | -44.43155 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74177a96-05ae-320a-8f45-1eb62ab36163 | -15.56168 | -47.91983 | 2025-09-27 04:46:00 | NOAA-20 | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d2451eb0-8be3-3b06-99be-afda537949e6 | -12.29011 | -45.65199 | 2025-09-27 04:46:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 601fbe14-8b13-3d41-872b-e7fcbc81cecf | -14.06779 | -48.82223 | 2025-09-27 04:46:00 | NOAA-20 | URUAÇU | GOIÁS | Brasil | 5221601 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 8faf9046-6eb3-3031-868f-92891e42e782 | -9.8912 | -49.12585 | 2025-09-27 04:46:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 2da66ad1-55c1-34a8-9a63-ddcd68321f72 | -11.99299 | -46.60894 | 2025-09-27 04:46:00 | NOAA-20 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f90a7c19-14c1-3902-86fd-0a3ddef28499 | -11.72227 | -62.59247 | 2025-09-27 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d837753b-5004-3b54-b4d4-3436e6b5029f | -15.01794 | -46.96839 | 2025-09-27 04:46:00 | NOAA-20 | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3ce3df93-8e6a-3f9b-8b00-ff2044d5fb55 | -11.38152 | -44.93726 | 2025-09-27 04:46:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 464c3d7a-e713-394d-b33e-b8109453a617 | -13.60239 | -47.30399 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 79914df3-c6d8-3e44-97a2-a83b8bcb1df1 | -12.83902 | -44.70369 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 58566436-acb9-3334-8863-2354b3edf646 | -9.76481 | -48.58785 | 2025-09-27 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d9f76391-acc7-3537-9a01-1305a8c594d9 | -13.62985 | -48.08251 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 6353c1f6-cabf-3e2d-b244-35f1e1efd4d1 | -11.97966 | -47.89783 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.0 |
| e4609137-fe5f-3a13-beca-bd7e8c2c604b | -11.72305 | -62.58851 | 2025-09-27 04:46:00 | NOAA-20 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2cab4a59-e903-3d2f-8334-4e64681374fd | -15.32312 | -47.8778 | 2025-09-27 04:46:00 | NOAA-20 | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9c26a0ae-3e06-3178-ba51-a3ff30894d18 | -11.77727 | -43.7661 | 2025-09-27 04:46:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 81f8fc9e-ebf3-3b9e-bf6a-ed70a42cd895 | -10.26463 | -48.08424 | 2025-09-27 04:46:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 54e2ddb7-e4e5-3bc3-8833-e0ab00ee936b | -14.95064 | -47.50571 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b2a5e948-dc84-328d-9540-4fccedf8842e | -10.03598 | -52.08519 | 2025-09-27 04:46:00 | NOAA-20 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bd38624-8e94-3d77-9fc9-9a30738a3fdf | -13.78387 | -46.93052 | 2025-09-27 04:46:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5541a6ad-b31a-37de-bfd0-f1009e0e6006 | -13.50828 | -47.41704 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ae930e87-5e7d-3ac4-85ce-47fd10fc4c03 | -15.19211 | -50.10058 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f1c9ee51-d01d-35c8-823d-282fd837c3e2 | -10.49112 | -48.05146 | 2025-09-27 04:46:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| fc077baa-b31c-3c6a-8d0c-e93cf384a0af | -13.4297 | -46.51566 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 951d51a1-c37e-3efc-9fd6-bf288a9a1c84 | -13.70723 | -47.89719 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| fb5e9a86-333f-304a-9369-657da8d328a2 | -15.53176 | -44.32837 | 2025-09-27 04:46:00 | NOAA-20 | PEDRAS DE MARIA DA CRUZ | MINAS GERAIS | Brasil | 3149150 | 31 | 33 | nan | nan | nan | Caatinga | 1.0 |
| f890884c-6e7d-3277-a3aa-50ad84ca2e47 | -13.70792 | -47.89222 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 4afee8f8-3033-32fb-a51f-e41478859e8f | -11.35326 | -45.01284 | 2025-09-27 04:46:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cbd19fd9-a6e9-320a-83f7-4830a0015edf | -15.1927 | -50.09649 | 2025-09-27 04:46:00 | NOAA-20 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 05e8e02d-971f-36d9-b440-e4685a1ac93d | -11.6925 | -44.42082 | 2025-09-27 04:46:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 446f63e6-4a15-3563-b7eb-234e5cddf7e2 | -12.82595 | -44.6911 | 2025-09-27 04:46:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 26d77f4f-362a-3f82-b407-6c507e0a6713 | -15.28707 | -49.48275 | 2025-09-27 04:46:00 | NOAA-20 | SANTA ISABEL | GOIÁS | Brasil | 5219357 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 771b70f1-bac7-3719-b8d1-ad47cc06ac6a | -9.76364 | -48.58518 | 2025-09-27 04:46:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6ea80a04-cb34-344a-afb7-2398323be17f | -10.40283 | -46.13641 | 2025-09-27 04:46:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c2e8e4e-825a-3474-b5d7-f64f8762a719 | -12.29956 | -47.21854 | 2025-09-27 04:46:00 | NOAA-20 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c73d75f6-8d47-33f5-b014-381ce30d3ddf | -13.0665 | -48.71857 | 2025-09-27 04:46:00 | NOAA-20 | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b7a6696a-3bbb-3cb6-b81a-598c37d9be39 | -11.97335 | -47.88697 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cfaf27cc-ef45-319f-9f7d-fc30bf9a7654 | -13.50473 | -47.41278 | 2025-09-27 04:46:00 | NOAA-20 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| bc7d8807-b1e6-3016-832f-00039f5b19d8 | -13.1791 | -47.40101 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5113af1d-31de-3665-9c39-403f7a4725cf | -12.86304 | -60.20746 | 2025-09-27 04:46:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4820c58a-0dbe-3b41-95b4-94483705ca18 | -11.94845 | -47.86842 | 2025-09-27 04:46:00 | NOAA-20 | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ccce68d3-0fd4-3363-8829-cca58d5a7c2c | -12.96739 | -46.91442 | 2025-09-27 04:46:00 | NOAA-20 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |


[Clique aqui para ver as próximas entradas](README51.md)
