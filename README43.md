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
| f116f14b-05c1-33fa-93c0-3b0e2417272f | -12.44671 | -45.55399 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb7c6f35-0976-315b-9dd4-4617e7dfef6e | -15.55766 | -46.83558 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59706a06-7bd8-3d92-9420-9fc10147a69d | -13.34869 | -48.05112 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 528efc3d-b650-39ed-84a5-85d7b831a5f9 | -15.62186 | -52.54398 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 05fcc1c4-8a79-3962-96bb-d9f0360007f1 | -13.72439 | -48.06588 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 114fe85a-bb87-3100-8a50-dc413ff30e2e | -11.48169 | -59.08863 | 2025-10-06 04:27:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c2c1874-9f5e-3ce7-b9d8-4c4469a77e4d | -13.36355 | -48.04271 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 58892724-c238-3b7a-9fc1-1fd044a63467 | -10.81274 | -48.82043 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a27eb19a-ccb9-3988-acb3-bf5ace79d0c5 | -12.25759 | -49.21294 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| c427c806-e367-39fb-b457-9af0c96f8235 | -8.62169 | -54.95772 | 2025-10-06 04:27:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| cb3a08c4-0aef-37ef-8e1c-c50db235aa24 | -14.88476 | -50.13231 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0c9cedb7-4b9f-338f-ab7c-84e6ed7e53e9 | -13.25416 | -47.80803 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| ad7a92cd-7bc0-3b51-9fba-f0c67a692231 | -13.6048 | -48.69221 | 2025-10-06 04:27:00 | NOAA-21 | TROMBAS | GOIÁS | Brasil | 5221452 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 84ea836d-46e0-32d3-bd45-d91549cd1921 | -10.27655 | -44.35711 | 2025-10-06 04:27:00 | NOAA-21 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f1510a2b-c586-3a8c-92f3-5188446f19ef | -12.44336 | -45.5769 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 3f25123d-05d2-3806-bde6-594745d4c85f | -16.04042 | -50.95075 | 2025-10-06 04:27:00 | NOAA-21 | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 853b1df6-baed-3117-99f4-103139518b62 | -12.4093 | -51.12947 | 2025-10-06 04:27:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8b1e2b0b-d253-337b-ab8c-5693497d9f69 | -12.99265 | -51.04313 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 68695c1b-c78b-39fa-a494-985614727d88 | -14.32595 | -47.65382 | 2025-10-06 04:27:00 | NOAA-21 | ALTO PARAÍSO DE GOIÁS | GOIÁS | Brasil | 5200605 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e50d9ad1-ae0c-3e30-ab9b-6c121b3f6c30 | -15.23208 | -50.07869 | 2025-10-06 04:27:00 | NOAA-21 | ARAGUAPAZ | GOIÁS | Brasil | 5202155 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d840dec6-443e-34ee-9d7e-7b934e16195a | -14.90777 | -46.84436 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7f2deca9-060a-3529-ab7e-b9521cad552c | -11.84476 | -45.05778 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2a266fdc-d546-3ae3-a63b-ef303a00c826 | -11.92931 | -47.03144 | 2025-10-06 04:27:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 99598ae3-28dc-3a6e-8e7f-75b95d19b22a | -10.85537 | -47.97736 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ad735033-31ab-3a4a-9481-b2dfcd6b18b7 | -10.96551 | -47.06045 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 511c00fe-da0c-3ef3-bb18-56354cb90130 | -15.60521 | -52.55045 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| c8cd7745-2280-3f6f-acd5-377d1f5c7cec | -15.59183 | -52.53842 | 2025-10-06 04:27:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6ffeb030-5637-3e7c-89fc-3e339f1345b8 | -11.44062 | -43.48332 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 15d0d815-403e-3713-a4e5-1c2b1c52cf42 | -11.41806 | -55.06671 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a0c9df43-77aa-3bf7-967d-d72399f3a447 | -14.70189 | -48.36154 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 1cf8d7e6-c47e-3f5b-8c81-fc6fd4be9fb8 | -13.77469 | -45.74262 | 2025-10-06 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d08807b1-94f2-3c95-bbe6-dd36accaf67f | -11.25842 | -47.77683 | 2025-10-06 04:27:00 | NOAA-21 | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 07b6b7dd-3a56-3f4e-83e1-672bd2708e25 | -15.27481 | -48.00522 | 2025-10-06 04:27:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c2a24d2e-9964-37ac-9b3c-0c046cda8a10 | -12.81789 | -46.84649 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e08a5b85-7cfa-3cbb-85cc-08a28c0453bd | -13.32668 | -48.06198 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7c29e8f7-39f3-3399-b2e5-96b6fd2b6f7b | -11.14394 | -47.16097 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 5ebc8dda-c9d8-358e-8cab-24fae808c2e1 | -12.47821 | -45.55489 | 2025-10-06 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| cd573e0d-103c-307c-b982-139226c70909 | -13.06672 | -47.9217 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0c82d235-6768-3482-b5d8-eadeee6021f9 | -13.27394 | -47.81124 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 068cb610-9dca-3b6a-b407-ebf64b8fc73f | -14.68206 | -48.38007 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0f8a05c7-a6f7-355d-8083-bb7f7d12ec3c | -13.36025 | -48.04217 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d97f0f56-037d-3e6b-b5c6-9050ed7b43ef | -11.42128 | -55.06958 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 64bc8107-f720-3730-92aa-91b37f1dd393 | -11.11432 | -47.19918 | 2025-10-06 04:27:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 5a4b69d7-2275-3524-8d87-b7ed876f9159 | -10.21977 | -48.18539 | 2025-10-06 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5549109-8565-35a1-84ef-2c4e6e49b451 | -12.82399 | -46.85117 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fa39d9f5-576d-33d0-abdd-eca4243d0fdf | -13.2766 | -47.577 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5dac8b07-7b52-3c1f-8204-105dd461e5ec | -14.85474 | -48.75162 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 89476762-8ef7-3ef5-adc6-672029e5b900 | -14.20068 | -46.67032 | 2025-10-06 04:27:00 | NOAA-21 | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 680cbdd9-dc85-3edc-b39c-1389a4043c2e | -11.84359 | -44.92082 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5c58c825-d3e8-39c0-9c50-38455ed2d7a1 | -13.22559 | -47.81779 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 5c4a7c33-f43d-3841-a4a6-67ece6667c55 | -16.24119 | -49.66253 | 2025-10-06 04:27:00 | NOAA-21 | ITAUÇU | GOIÁS | Brasil | 5211404 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a84f44bc-59d2-3289-9e98-f651d492b9cf | -16.35124 | -47.05456 | 2025-10-06 04:27:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 159cdaa2-ec59-3d0b-9e2f-2541a4588d22 | -15.33188 | -46.37202 | 2025-10-06 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 484d3abc-8680-3b2c-a348-8314a9768293 | -13.33599 | -47.56499 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| ad63f21b-d9c9-398a-9f5b-b8699939c121 | -14.69814 | -48.29921 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1e5a2692-c6ae-3928-bbf6-22cfe0379f60 | -11.50021 | -54.46739 | 2025-10-06 04:27:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b52e3af5-0bba-3fda-b238-e58cafe43081 | -15.19469 | -46.37566 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 3.1 |
| c83c0222-aa20-3144-8436-5d81e4a70937 | -9.55835 | -50.78366 | 2025-10-06 04:27:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a85a60e-7f6a-3bd5-9467-2ff410ba511b | -9.67327 | -49.95261 | 2025-10-06 04:27:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 62b44e74-d985-3979-9398-5a1491428640 | -10.73939 | -47.87223 | 2025-10-06 04:27:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d78b5225-e6d2-3b29-a2a8-58ddf3f3b15e | -15.99679 | -50.93455 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1f1db6cd-2e96-3e06-a118-ceafbfae1f5b | -13.34209 | -48.05005 | 2025-10-06 04:27:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0f9f9e47-832d-3211-b29e-458f9e9e7a77 | -14.68039 | -48.3907 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a1cb5eb9-51cd-3bc7-a4e6-acdf7c85d3cc | -13.63567 | -48.71189 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f5fd307f-a0a6-30f2-9d15-e9f1c6db2aa0 | -13.72384 | -48.0694 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 314ec3c9-58de-3c07-b8d1-0333b92b2133 | -12.90774 | -54.74364 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 37400242-3c4b-3c11-899d-4c441837e92b | -15.21298 | -46.39363 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 61fb87ee-b87c-3ed1-a6e9-4793d1c3c2eb | -10.13762 | -45.40834 | 2025-10-06 04:27:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8557f3ee-6236-36f9-8390-a5a23c70d902 | -11.40872 | -43.48606 | 2025-10-06 04:27:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b3577f2b-40cb-3ab5-9c0a-47e6e18d33d4 | -12.95763 | -51.04271 | 2025-10-06 04:27:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d9fee75f-03f5-3714-9dc9-bf45364ed6f6 | -15.98173 | -50.85499 | 2025-10-06 04:27:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 32f5bb4e-4f01-364a-b0d2-301db0734229 | -12.59221 | -48.12146 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 152f6e97-94b9-30c1-b25a-27997e27bbbf | -13.26204 | -48.47131 | 2025-10-06 04:27:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ffd70baa-09d8-3cd7-93a4-66a4313dc5fd | -12.25482 | -49.2087 | 2025-10-06 04:27:00 | NOAA-21 | FIGUEIRÓPOLIS | TOCANTINS | Brasil | 1707652 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fdf5282e-9fdd-3ec3-9733-644ae8c9da94 | -11.21077 | -54.98534 | 2025-10-06 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e605d21-6e4b-3ebd-acd1-fb5c9ef55d72 | -13.05604 | -47.92004 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ff275edf-c15d-3c5d-a7e0-98b08b1fc70d | -12.54809 | -48.16479 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6f05946a-59e6-3d90-9a63-0a88ec720a8d | -12.92751 | -47.80852 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0a2dcdcb-487b-3346-be37-f6de3df2de87 | -14.94741 | -46.83249 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35d32c32-bd52-3e99-998a-8ba52ca33b8a | -14.66795 | -48.27607 | 2025-10-06 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| a5fb1c2f-5db3-3d79-9d73-3c17070cf795 | -12.92553 | -54.72313 | 2025-10-06 04:27:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| e445557d-8f3f-3556-b6e4-a19a7a32c704 | -10.04674 | -49.20966 | 2025-10-06 04:27:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a943886d-45ae-3610-97f1-a31008847e7a | -11.02483 | -46.54487 | 2025-10-06 04:27:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7c506cad-6747-30da-830f-d4f1fea79689 | -11.64125 | -45.0613 | 2025-10-06 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b9d14cc5-0432-3f6c-abb4-d648b9ffab97 | -11.67063 | -44.26601 | 2025-10-06 04:27:00 | NOAA-21 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 063a7fa7-6330-3631-985d-de16b37d6c3b | -11.93995 | -46.42971 | 2025-10-06 04:27:00 | NOAA-21 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| ed2211c3-444d-36ea-942d-52410f728dac | -13.63784 | -48.7196 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSO | GOIÁS | Brasil | 5208103 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d1865640-e705-3d68-9815-44f1fd4eefd6 | -10.87841 | -51.64635 | 2025-10-06 04:27:00 | NOAA-21 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0dcb8528-02e1-304e-95d3-9d587d1b6787 | -10.42156 | -50.34485 | 2025-10-06 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d24efea4-97e3-335d-b606-77d55ccc98ac | -9.67681 | -48.40882 | 2025-10-06 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6681cc27-52f4-30fc-9f5b-d78a25456607 | -10.81215 | -48.82409 | 2025-10-06 04:27:00 | NOAA-21 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e338a0d8-e57d-3cae-bb6d-15e80aab40f4 | -13.0511 | -47.90842 | 2025-10-06 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e455e8ce-272a-3cd1-86f0-6ab70dd763f7 | -9.2716 | -51.80087 | 2025-10-06 04:27:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da7fcfc5-9399-38b8-be14-d93e36058ed0 | -12.91278 | -46.80268 | 2025-10-06 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| de07f670-9151-36b4-af83-ade4fe759272 | -14.91556 | -46.83833 | 2025-10-06 04:27:00 | NOAA-21 | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 9dca6732-b33c-3ea0-8925-df0643ebcdd5 | -11.11197 | -47.71042 | 2025-10-06 04:27:00 | NOAA-21 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cae59b65-563e-34bc-98d8-ebb34efe846f | -13.73428 | -48.0675 | 2025-10-06 04:27:00 | NOAA-21 | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| e0cb0b23-02e4-3821-bec7-8cb72d1ad6b1 | -14.49162 | -47.54912 | 2025-10-06 04:27:00 | NOAA-21 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 766bfcb6-3b41-3b84-91f1-682a89f6057c | -15.00218 | -49.97427 | 2025-10-06 04:27:00 | NOAA-21 | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9ca2007b-6bb6-3b66-a2e2-0ac93ea2e674 | -15.57983 | -47.27678 | 2025-10-06 04:27:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |


[Clique aqui para ver as próximas entradas](README44.md)
