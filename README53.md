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

## Dados Diários - Página 53

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8cff7f82-f327-3f74-8321-6697504c0180 | -15.03509 | -54.89679 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.5 |
| e1254811-0017-33b0-9a2a-ba9aa6bb114c | -13.37555 | -46.21764 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 1ba74b23-f581-3435-aa52-e2b9f518a64c | -11.32681 | -55.21693 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f84847f1-534f-3bff-9c84-d38db303e72b | -14.80173 | -45.43943 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 88f43c8a-9320-322f-aabc-e2cfa0b9bd61 | -13.38588 | -47.5151 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 9fe39017-157c-35ad-9237-2d8817161402 | -13.37625 | -46.21208 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 152f9875-6f41-37ab-8dd6-1b0411447e61 | -14.27553 | -58.55287 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0ceb3321-6d80-3358-8b56-989eeb37e5ea | -13.49722 | -47.03577 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| a0829219-df72-3012-9fff-32f87bb406af | -16.28261 | -54.89883 | 2025-08-23 04:53:00 | NOAA-21 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 0edc94aa-166b-31a6-a602-b6b990f52149 | -9.84618 | -64.29357 | 2025-08-23 04:53:00 | NOAA-21 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec5080c1-75f9-3cda-8b16-5de12613ac33 | -12.17837 | -47.20801 | 2025-08-23 04:53:00 | NOAA-21 | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 641bf693-651c-3dee-a7df-cad45736f001 | -14.79225 | -45.42802 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4be6c418-2600-3012-892e-3651988414f6 | -13.03876 | -46.31971 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| b1de4c8a-3acd-3e34-ba16-a330ca25c82d | -14.44648 | -52.05564 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4c6ac895-6004-35e7-96de-d4c568b59acf | -12.94523 | -46.30745 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| cd6e72b9-2db6-314a-8dd1-cb8c42e77a0c | -15.06853 | -56.39352 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 4.0 |
| e0ef27d4-bd4f-3cf1-9fbc-1e7f863429b2 | -9.95589 | -60.18953 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 19.5 |
| a3870115-4fd1-3e48-8ced-fe815da67ed9 | -14.29045 | -58.55566 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3a4d781-66f4-380c-a197-d6def6e2a901 | -12.78819 | -48.7163 | 2025-08-23 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f6e75e26-7ec0-32dd-a118-e430c77a386d | -16.51877 | -46.73478 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 265331fa-b49f-3d4f-a512-91a1e261a8c8 | -11.32623 | -55.22054 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 1e8484bd-4f66-3198-b6c8-bc5276f325f3 | -13.50882 | -47.05759 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b32c3759-6c10-3971-b1cf-ec98fcbf29f6 | -10.71451 | -60.40197 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f74e8f80-454e-333e-994f-bdd66609797b | -14.64874 | -54.86573 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| da8953fe-e2ed-3537-95ff-41c5a2a67462 | -14.68267 | -56.60618 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 42ec1733-e90b-3f93-bc7c-cfc8657df44a | -13.12808 | -46.89904 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 0aceeede-be85-3b46-88fd-60bec8047562 | -14.30246 | -58.55309 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 366473c7-31bd-3bb0-bf32-fe79451fefdd | -14.67154 | -56.58854 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3c8b613a-0f0c-3787-aedd-56744d7f6c41 | -15.03839 | -54.89734 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e7e6425a-e724-30ed-b00e-4da1e42d93b0 | -14.74788 | -55.99311 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0b1ebfe2-8999-3e4f-92bd-58f57a935ee4 | -14.68397 | -56.19426 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 76037602-748f-3bc5-92b7-0f608127026b | -12.50482 | -53.80851 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cc08a293-2dac-38ea-9252-677c2c845c32 | -14.75161 | -45.40558 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 63050795-4f77-3810-94a2-4bac48687250 | -14.6124 | -54.83787 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 018c9201-2d1c-308a-97c3-a15e479fbf9d | -14.67115 | -56.61223 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dbfd3071-2bf2-38bf-8713-6dd31f55f784 | -17.26815 | -46.76137 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 82073782-26fe-3c1b-8e48-b90b494a6099 | -13.47347 | -46.90364 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 61d5dae8-a2db-3975-9882-aa3f5832db76 | -17.26731 | -46.77057 | 2025-08-23 04:53:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 5c1b43bb-0306-3ba6-ba0b-788415322888 | -13.37308 | -47.50703 | 2025-08-23 04:53:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c6104872-b2c0-37a7-a5ae-36ef9b5ee957 | -16.33154 | -46.76977 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0379e222-cdc2-30cd-b56c-ab69a5defa58 | -9.5151 | -60.52813 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5669470e-4350-3e18-8468-40c3d6c7f407 | -12.94922 | -46.2974 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 4c4408c5-5f39-3642-b971-461287753338 | -14.6816 | -54.87457 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7e91427e-4183-329f-965b-f7718ed30455 | -8.88199 | -62.42389 | 2025-08-23 04:53:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 766e6c2a-734e-3f47-8132-ebf177c6339f | -12.93246 | -46.17308 | 2025-08-23 04:53:00 | NOAA-21 | LAVANDEIRA | TOCANTINS | Brasil | 1712157 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 843c1a95-96c7-327e-aafd-2df1d710f305 | -14.94791 | -48.01424 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| ad1fd00c-ad24-346e-88a4-194b2670dde5 | -14.67092 | -56.59231 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ad56d78d-03e6-3056-9d4d-3925f514e4ae | -12.49601 | -53.82156 | 2025-08-23 04:53:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8ced97e-9b66-3cd2-b46f-afa1bd464b5b | -13.42713 | -57.17173 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 13656cf4-f1c8-34d7-b106-fd4e0e16573b | -9.957 | -60.20176 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 29c12e38-0f35-3551-bee5-4210e141b515 | -13.02636 | -56.82647 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 9c9a2c1f-1bca-31ff-9a90-063641c3a13a | -11.19102 | -55.02042 | 2025-08-23 04:53:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8b122b6a-8950-32d0-8a5c-b20c4ba83dc8 | -13.18171 | -54.9572 | 2025-08-23 04:53:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 435273a1-d037-30db-99ce-0285354656d4 | -15.54457 | -51.70487 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 4d5a77f9-5aff-3d69-8d7f-30fcdf37bd56 | -14.4712 | -55.93869 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 70a67a4c-323d-32ff-b319-302c0440320f | -13.04305 | -46.32526 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 06fe7208-26b6-3cfc-b964-c3e29bf59a26 | -12.99173 | -45.22517 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 13.3 |
| b5289540-c1d5-3e4b-b4bf-a28bf784645d | -10.45858 | -59.13324 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2097c94-3efd-3eb5-8072-c3493e05b2ff | -12.99621 | -45.23247 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| faf748cf-4597-3585-8566-6295c9e54e48 | -15.55715 | -51.71974 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 13d53b6a-b649-397c-836f-3ae58df00acd | -14.47585 | -46.06172 | 2025-08-23 04:53:00 | NOAA-21 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 173f7113-1296-3584-865c-f2f55891f22d | -14.80361 | -47.94581 | 2025-08-23 04:53:00 | NOAA-21 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 308882dc-e97c-3ec8-8c02-dd718120b136 | -13.39143 | -46.34664 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 0c836959-592c-37c7-89b2-3f5ed8cc8752 | -14.65254 | -56.59742 | 2025-08-23 04:53:00 | NOAA-21 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d132233b-337b-39c8-b2b9-f8340cda77ef | -13.38734 | -46.21485 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 94447d3d-3721-37e9-a5ce-4a3e3bf6e42f | -14.67829 | -54.87402 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6e8c67f8-2d75-3b98-97eb-00ee3df27455 | -11.18987 | -55.02759 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0e3756fa-01ec-37bc-93ee-1eac98255bdb | -11.64991 | -51.58781 | 2025-08-23 04:53:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 80b0dd20-c0db-3ffd-b3cb-b21028e8176e | -14.66496 | -54.91555 | 2025-08-23 04:53:00 | NOAA-21 | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 98487e20-16ec-3714-a6ed-ba7ec0e71d07 | -14.9735 | -54.55143 | 2025-08-23 04:53:00 | NOAA-21 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 2fac1f4b-0ae4-346d-9c80-af92dd5d7c7a | -13.64665 | -46.88842 | 2025-08-23 04:53:00 | NOAA-21 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 8c2416e0-df67-3c73-87c9-0b02a879346f | -15.19942 | -48.25414 | 2025-08-23 04:53:00 | NOAA-21 | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a7ec2cac-2349-31e8-946a-93e3b5c8dcc2 | -8.70327 | -62.87794 | 2025-08-23 04:53:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 53d43842-6ab6-3ab6-a489-f8267f81d1a6 | -12.94589 | -46.30231 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 94b50d3b-b255-30e6-85cb-d34a6f185b82 | -9.96017 | -60.18414 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| bdcbad5d-49f1-3758-b689-9a657abe3bbb | -14.6587 | -54.84552 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cef4212d-6b96-3c8d-844e-c00e59b7b5ab | -9.81495 | -64.2712 | 2025-08-23 04:53:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ff03fb71-bc20-36ed-a678-4c32817b86c4 | -14.79022 | -45.49279 | 2025-08-23 04:53:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 5533a306-2516-377b-a386-2c4bbb38658e | -12.29899 | -50.00057 | 2025-08-23 04:53:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c70f2d39-c0e5-3ff9-bcf6-07e8f49296ed | -14.43591 | -52.04725 | 2025-08-23 04:53:00 | NOAA-21 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f0d28863-fbf1-365a-9419-0348d8c08d90 | -14.62073 | -54.80646 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 15962dbf-deaf-3357-a53f-bbab90bb3bf8 | -13.48843 | -47.02973 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b08bfa68-c0c6-3129-af9b-b63eead40aaa | -13.45256 | -47.03062 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6e29c39e-96c5-3332-bef5-4415bbd0798a | -14.74767 | -56.29298 | 2025-08-23 04:53:00 | NOAA-21 | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 09768d2f-729e-30cd-9d96-59e2d33a5e3b | -9.4323 | -62.25417 | 2025-08-23 04:53:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 4a80a7f5-d33b-30f7-a90a-ca791f24a783 | -14.61742 | -54.80592 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 919dcfb0-4f37-39f0-8d5b-af18b2e2b383 | -13.43066 | -57.17233 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a1a44a5-6bfc-3343-a26e-83f6c30df2d7 | -14.28672 | -58.55497 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1637a5cb-6ff1-37fd-8e8d-10a2254a1fa6 | -13.03729 | -56.87639 | 2025-08-23 04:53:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 31111c82-a28e-3884-9312-52a5be1da9dc | -14.76643 | -55.98495 | 2025-08-23 04:53:00 | NOAA-21 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ff738ca-fa1b-3339-af35-1886953f3746 | -16.41983 | -49.15509 | 2025-08-23 04:53:00 | NOAA-21 | NERÓPOLIS | GOIÁS | Brasil | 5214507 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| ecedfd6d-9802-38ea-b268-d015e7597bf4 | -12.94102 | -46.30156 | 2025-08-23 04:53:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 0a9f7ced-bea9-3018-9293-145899838420 | -11.18698 | -55.04555 | 2025-08-23 04:53:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d4835e84-31f6-3d36-a73e-394188d7f8fd | -9.94767 | -60.17738 | 2025-08-23 04:53:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 2dfdfb5a-ac8b-3617-b095-968047640f39 | -16.51831 | -46.73459 | 2025-08-23 04:53:00 | NOAA-21 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 31618b38-8480-338e-8672-308387b1fde7 | -13.18879 | -59.17039 | 2025-08-23 04:53:00 | NOAA-21 | CAMPOS DE JÚLIO | MATO GROSSO | Brasil | 5102686 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a3dae251-57fd-3078-949a-9d60507d0752 | -14.33662 | -58.57832 | 2025-08-23 04:53:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 489ee0a6-0be3-3fde-9d0a-53e9576c1901 | -15.54938 | -51.697 | 2025-08-23 04:53:00 | NOAA-21 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 21e650fd-3fda-32e0-b5cc-31fb1f16cff1 | -13.14508 | -46.91584 | 2025-08-23 04:53:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 3.8 |
| deb5abf9-2533-35b2-b0e5-a073ae5dbef1 | -14.61678 | -54.85316 | 2025-08-23 04:53:00 | NOAA-21 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README54.md)
