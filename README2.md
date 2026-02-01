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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3c1f19b7-5858-3726-9157-463558c3960c | -23.38837 | -47.96865 | 2026-02-01 04:21:00 | NOAA-21 | TATUÍ | SÃO PAULO | Brasil | 3554003 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| 28f304de-e8e6-3d35-a4af-a47a8407fe3e | -31.03636 | -53.48722 | 2026-02-01 04:23:00 | NOAA-21 | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.8 |
| f7140b34-3cda-38dd-ab62-7bc3aa27100a | -28.85918 | -49.5916 | 2026-02-01 04:23:00 | NOAA-21 | MELEIRO | SANTA CATARINA | Brasil | 4210803 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ede7a9ea-c134-3956-91f6-0f783e9365fa | -7.00677 | -45.85566 | 2026-02-01 04:44:00 | NPP-375D | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 005814be-0304-301b-b1b3-6729e4daa534 | -2.4443 | -47.07781 | 2026-02-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b831c0b4-aa25-3378-86a5-5ba8ae4a36d3 | -2.02616 | -47.89604 | 2026-02-01 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f1893ac1-2f0d-33fc-8117-2f1755628acc | -2.53253 | -47.79961 | 2026-02-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e552783-dd61-3a04-ab3d-a5e0b26bf46d | -5.98489 | -45.73925 | 2026-02-01 04:44:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9135920a-faf2-3619-ad89-d315bef07610 | -4.73428 | -48.9571 | 2026-02-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2ca1aa6d-31cb-3d9d-bd08-ef5fcae5715f | -2.44713 | -47.08199 | 2026-02-01 04:44:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| df756b43-5767-347e-b6f7-7ece3dcd2617 | -1.50428 | -46.02977 | 2026-02-01 04:44:00 | NPP-375D | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3f8e5ebe-d524-35ba-80df-34aa61fd2279 | -4.39564 | -48.12109 | 2026-02-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1b7be47c-c6c0-342b-8b78-d1e48d5a52ff | -4.63121 | -48.38108 | 2026-02-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9bb1bfcb-866c-302c-b9e9-1088ce581075 | -1.50729 | -47.33043 | 2026-02-01 04:44:00 | NPP-375D | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0f4d94c-8a45-3477-9105-e7f2e87dd987 | -4.1 | -47.73728 | 2026-02-01 04:44:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9705b381-5200-3458-8c0a-ca45cad939e0 | -2.14983 | -47.88355 | 2026-02-01 04:44:00 | NPP-375D | SÃO DOMINGOS DO CAPIM | PARÁ | Brasil | 1507201 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9be5988f-13cc-37be-919d-5b276fa67590 | -4.96911 | -50.90989 | 2026-02-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 180a67be-69e2-3125-80c0-fc42c89c2a79 | -2.26114 | -47.86517 | 2026-02-01 04:44:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 17677e00-f175-3b0c-a1fb-c381bf8c8112 | -4.05386 | -47.1596 | 2026-02-01 04:44:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 79d4d0f2-263f-35b8-a1c2-5b101c912b9c | -4.25906 | -48.83611 | 2026-02-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e0291af-a034-3bb9-92d7-abab7e6be4d0 | -2.58121 | -47.49249 | 2026-02-01 04:44:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8a6dfec6-4c2c-3d6a-a35a-c4b0436db650 | -5.37771 | -43.07148 | 2026-02-01 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1887e21a-49e2-3719-aad6-bff0aa344b1d | -5.3771 | -43.07562 | 2026-02-01 04:44:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 634edc2c-21df-39c2-9c10-99de532610cc | -9.57067 | -44.57264 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 896bdc69-7a35-3e36-b0ac-9bd48d5b3d97 | -7.86278 | -45.9757 | 2026-02-01 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 76144250-f693-3941-a746-cf274219dbc3 | -8.43061 | -48.03984 | 2026-02-01 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e4e5361e-def5-3b1c-adf4-82383c509fd8 | -8.51515 | -48.12515 | 2026-02-01 04:46:00 | NPP-375D | TUPIRATINS | TOCANTINS | Brasil | 1721307 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1c6a99a5-1c48-364b-9490-c077f7bcff7c | -8.43119 | -48.03607 | 2026-02-01 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 319e1cf4-d903-3ede-976a-b19fef6c9ba0 | -9.57435 | -44.57714 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b23948ba-be00-3dfe-96db-fed900063c32 | -9.5749 | -44.57327 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d8c92c27-1600-3231-9929-fb14bec37c7d | -9.57012 | -44.57651 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO DO GURGUÉIA | PIAUÍ | Brasil | 2208700 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6af13c09-58f2-329e-9afe-2875762e89b2 | -7.90558 | -50.37231 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01528665-6880-3264-ade0-43bf7a52ff07 | -8.43003 | -48.0436 | 2026-02-01 04:46:00 | NPP-375D | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 2ac08334-e846-3216-8ddc-3a0ae8b909c2 | -7.90169 | -50.37527 | 2026-02-01 04:46:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 04e9de2e-9aa4-3532-aa14-2c36a4cfcd4e | -18.81251 | -51.60292 | 2026-02-01 04:48:00 | NPP-375D | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0208515a-4727-37c3-bd94-e577ee3d1d79 | -16.58186 | -57.808 | 2026-02-01 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4bb493c4-de82-3754-a02b-d185ff9afd22 | -19.40999 | -54.17694 | 2026-02-01 04:48:00 | NPP-375D | CAMAPUÃ | MATO GROSSO DO SUL | Brasil | 5002605 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 72ed4067-da43-3548-9da1-673641d680d1 | -21.15668 | -46.92469 | 2026-02-01 04:48:00 | NPP-375D | MONTE SANTO DE MINAS | MINAS GERAIS | Brasil | 3143203 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 580aa07a-7c01-3b28-814c-fd7487dc8481 | -16.58263 | -57.80392 | 2026-02-01 04:48:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| a037b5a6-547c-3890-9055-c7900cfd3839 | -20.91774 | -56.37947 | 2026-02-01 04:50:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| efd985fc-589f-341c-b7fb-46f5d8093aef | -20.75409 | -54.77496 | 2026-02-01 04:50:00 | NPP-375D | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 83373281-299b-3eba-9ed9-f2760d12b1b3 | -20.91932 | -56.37059 | 2026-02-01 04:50:00 | NPP-375D | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 529d6514-a3c3-3dc3-8606-41a0571fdc90 | -21.51418 | -49.13388 | 2026-02-01 04:50:00 | NPP-375D | NOVO HORIZONTE | SÃO PAULO | Brasil | 3533502 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.9 |
| 73e0ac44-45d9-3baa-9d47-b39870803e3a | -23.27371 | -51.20139 | 2026-02-01 04:50:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 2b3e1010-e512-353c-992a-768cdd54e16b | -26.01897 | -52.70096 | 2026-02-01 04:50:00 | NPP-375D | PATO BRANCO | PARANÁ | Brasil | 4118501 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 67792683-76fb-3e28-a2b8-b91d70e95627 | -23.27719 | -51.20201 | 2026-02-01 04:50:00 | NPP-375D | LONDRINA | PARANÁ | Brasil | 4113700 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 302fb793-4dcd-38b1-a998-bbbc883dbb6b | -26.1142 | -53.29986 | 2026-02-01 04:50:00 | NPP-375D | MANFRINÓPOLIS | PARANÁ | Brasil | 4114351 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8cca630c-ac0e-37f4-bc76-1f1e7dc7c971 | -31.03604 | -53.48862 | 2026-02-01 04:53:00 | NPP-375D | PINHEIRO MACHADO | RIO GRANDE DO SUL | Brasil | 4314506 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0f6de1f5-a4bf-3e79-ac57-d177bd24437e | -29.36717 | -49.93325 | 2026-02-01 04:53:00 | NPP-375D | MORRINHOS DO SUL | RIO GRANDE DO SUL | Brasil | 4312443 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 6868c663-ca38-384d-a539-b380a14c8d90 | 4.37542 | -60.96487 | 2026-02-01 05:01:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 37f3e8b1-5afe-394b-8b2a-ddf98d590d3e | 4.08503 | -60.24382 | 2026-02-01 05:01:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| eda4b1f4-1786-33af-92b1-af422bd1648f | -4.73101 | -48.95725 | 2026-02-01 05:03:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 19e50939-382c-3b37-98a7-c422375c7cec | -1.52241 | -45.92473 | 2026-02-01 05:03:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a9c4692b-5069-35ad-b484-1f67a681c60e | 3.26511 | -61.03304 | 2026-02-01 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0974fff4-777c-372d-ba63-3e77035d0b35 | -1.51765 | -45.92063 | 2026-02-01 05:03:00 | NOAA-20 | LUÍS DOMINGUES | MARANHÃO | Brasil | 2106201 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8c8a4006-83f1-3020-98b6-ef10a2159851 | 3.37038 | -60.45105 | 2026-02-01 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 227ad81b-2557-3cec-ba93-48b3cf8a2a7b | 3.26437 | -61.02814 | 2026-02-01 05:03:00 | NOAA-20 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 95ca003e-3f83-31d1-819d-1f23ae281266 | -2.26008 | -47.86724 | 2026-02-01 05:03:00 | NOAA-20 | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 87e7773d-fcdd-33a1-af33-6edb536f2c57 | 3.84258 | -59.67025 | 2026-02-01 05:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1c48d407-f590-3544-a892-0381dcfd07f7 | 3.36971 | -60.44649 | 2026-02-01 05:03:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d349f764-9751-32f2-8ff8-752741dae5fb | 4.16259 | -61.04682 | 2026-02-01 05:03:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 799505e3-b161-3984-bec2-0677af551d69 | -4.25542 | -48.8376 | 2026-02-01 05:03:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10f3637d-4e44-3206-8c87-ab76762a2f66 | -1.68373 | -53.91658 | 2026-02-01 05:03:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| eb6fe48a-9598-3b41-9a09-3b72b9e11cb4 | -8.42875 | -48.04486 | 2026-02-01 05:05:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b5a38d0f-fa63-36ec-b04e-3b129ff8764b | -8.42914 | -48.04195 | 2026-02-01 05:05:00 | NOAA-20 | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c723a7d8-23c4-3c12-a1e3-4168a1de802e | -16.58208 | -57.80593 | 2026-02-01 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 33828472-d23c-328a-850a-cc17bf281560 | -16.57876 | -57.80537 | 2026-02-01 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 9b19e66e-34d7-3a7f-bf41-976d620577e6 | -16.5854 | -57.80648 | 2026-02-01 05:08:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 14ff0d23-5723-3aa3-9b8f-86077f80b4ac | -20.91908 | -56.37178 | 2026-02-01 05:10:00 | NOAA-20 | BONITO | MATO GROSSO DO SUL | Brasil | 5002209 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e11a6d32-12b2-37a7-b1fa-504a30b7a079 | -29.77452 | -51.17874 | 2026-02-01 05:12:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| e9734654-b2d1-300d-b174-1bd04a6b9db4 | -29.77482 | -51.1749 | 2026-02-01 05:12:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.5 |
| 0793cd4d-b60e-3766-9f65-40cbb17d17f5 | -8.51161 | -35.99743 | 2026-02-01 05:29:00 | AQUA_M-M | ALTINHO | PERNAMBUCO | Brasil | 2600807 | 26 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 21e5832a-8cb4-3727-94eb-2b0b09136223 | 4.16659 | -61.0377 | 2026-02-01 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 28f2c815-c262-3fae-ba16-a0afddf2a59e | 4.16313 | -61.04192 | 2026-02-01 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dba5f089-dd84-3e7c-b06a-8461d323e1ec | 4.1707 | -60.64807 | 2026-02-01 05:52:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a9ed7a47-4eff-3d97-991e-fd0e0a080c7e | -4.39109 | -45.61954 | 2026-02-01 12:12:00 | TERRA_M-T | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1a8722e-f7c7-3f0c-92d0-1332b341e088 | -2.40616 | -44.87995 | 2026-02-01 12:12:00 | TERRA_M-T | BEQUIMÃO | MARANHÃO | Brasil | 2101905 | 21 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 5617e429-9230-3738-b1a9-31e46295b589 | -5.63553 | -45.79974 | 2026-02-01 12:12:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 9033d19b-f4c5-3494-a723-e710c7a8d948 | -5.64515 | -45.80109 | 2026-02-01 12:12:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 48d45cbd-b823-3337-8e7c-9e282ad27d32 | -25.90923 | -49.57234 | 2026-02-01 12:18:00 | TERRA_M-T | QUITANDINHA | PARANÁ | Brasil | 4121208 | 41 | 33 | nan | nan | nan | Mata Atlântica | 5.2 |
| 0f3316d7-1f3b-3704-bb95-ba2f17386e70 | -26.32638 | -49.9973 | 2026-02-01 12:18:00 | TERRA_M-T | ITAIÓPOLIS | SANTA CATARINA | Brasil | 4208104 | 42 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 4fa6e86e-d579-34ca-98b2-12dd4baba6a6 | -29.03236 | -51.18107 | 2026-02-01 12:18:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 3f31725d-7a4f-387b-902f-7d76c4f4951e | -28.97361 | -51.0712 | 2026-02-01 12:18:00 | TERRA_M-T | SÃO MARCOS | RIO GRANDE DO SUL | Brasil | 4319000 | 43 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 3bc1cc5d-50e0-3199-86e2-e9ae6c0f5468 | -29.00505 | -51.24656 | 2026-02-01 12:18:00 | TERRA_M-T | FLORES DA CUNHA | RIO GRANDE DO SUL | Brasil | 4308201 | 43 | 33 | nan | nan | nan | Mata Atlântica | 4.9 |
| 9894a2e7-41c9-3dc1-9072-09965dca99ac | -4.1019 | -44.2068 | 2026-02-01 14:30:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 122.7 |
| 01ad528b-9832-3f83-8ba0-633942348250 | -4.1019 | -44.2068 | 2026-02-01 14:40:00 | GOES-19 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 144.7 |


