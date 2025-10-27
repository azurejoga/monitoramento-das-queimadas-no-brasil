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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9eef6655-2e40-3882-916d-e749127735ef | -13.30208 | -43.37081 | 2025-10-27 00:11:00 | TERRA_M-M | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 87504ac2-7082-3183-ba6d-0abb7957f1dc | -13.89169 | -48.49062 | 2025-10-27 00:11:00 | TERRA_M-M | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 24.0 |
| b2d87c5b-6b8b-30e1-ba36-6e14af034a55 | -13.54019 | -49.56295 | 2025-10-27 00:11:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 14.8 |
| d228379d-ed45-3003-acdf-af2ab670db48 | -13.59923 | -43.11761 | 2025-10-27 00:11:00 | TERRA_M-M | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 16.5 |
| 36467756-8bd3-311b-99fa-104f080404d5 | -13.54241 | -49.55539 | 2025-10-27 00:11:00 | TERRA_M-M | BONÓPOLIS | GOIÁS | Brasil | 5203575 | 52 | 33 | nan | nan | nan | Cerrado | 12.2 |
| eb2e4dd5-b8be-37d5-a8fa-d6149ce58a64 | -12.53079 | -47.56619 | 2025-10-27 00:11:00 | TERRA_M-M | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 216.8 |
| 5be7e66f-7a18-35cb-971e-d802cd88f074 | -17.32168 | -43.61095 | 2025-10-27 00:11:00 | TERRA_M-M | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 65d9239a-5584-3f72-b596-6dc5cfc71116 | -6.10478 | -41.77724 | 2025-10-27 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 31.8 |
| 98b7bedb-1344-3d5f-ac80-67bac8a0e656 | -5.55124 | -43.95148 | 2025-10-27 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 43.6 |
| fd545a59-828a-3f91-bced-b82f13bb3fe5 | -7.78551 | -45.38165 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 2a82a6c6-5af8-3d3f-913b-7501486cfb86 | -7.67667 | -46.33877 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 0016d651-b790-3be3-a1ba-1952c39d1d95 | -6.4327 | -42.35698 | 2025-10-27 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 6.8 |
| 927a7741-6a62-3179-9c28-31371c20c800 | -5.12431 | -47.74247 | 2025-10-27 00:13:00 | TERRA_M-M | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 7a52c446-c237-3a1d-a03f-a73df8affb79 | -7.33929 | -42.45752 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| e2ea4bf3-e351-335a-94d8-f10ced41fb15 | -5.08086 | -47.14469 | 2025-10-27 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ea6bcce2-748b-316e-a89c-f3cad8fd50b8 | -7.54578 | -46.25694 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 942f40fc-db7e-3edd-b680-3df53bf5a6c3 | -10.68953 | -48.06482 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 3720ecbb-4cbb-3856-99de-bd86fd2857a0 | -10.76391 | -44.18781 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 483475dc-127b-32e8-9792-2510badf0ecf | -7.79509 | -45.37451 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 18.3 |
| e619ee03-0c26-3429-b7e0-57df1135f5e6 | -9.252 | -45.59815 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 542920fa-2376-36ee-8089-9ba93f002b19 | -8.10678 | -47.06029 | 2025-10-27 00:13:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 433dee7f-ad62-30c8-9797-f68ccb902f96 | -10.82945 | -47.8901 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.2 |
| 7555f007-e9ea-3540-a67a-ea02c12d311c | -4.80819 | -38.65047 | 2025-10-27 00:13:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 62.3 |
| e030d644-ea71-3acc-b739-fddf2b22e73e | -9.20327 | -44.56765 | 2025-10-27 00:13:00 | TERRA_M-M | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 63475eb1-420d-333d-be3c-574cce1b7f3a | -5.78407 | -35.37992 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO GONÇALO DO AMARANTE | RIO GRANDE DO NORTE | Brasil | 2412005 | 24 | 33 | nan | nan | nan | Caatinga | 42.1 |
| 2be0a8f6-4ef6-362d-b2a8-cfa796e0eb53 | -6.11821 | -41.7292 | 2025-10-27 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 9.7 |
| 154a3404-b15c-3e89-8ee9-553d6683f617 | -5.60898 | -47.10487 | 2025-10-27 00:13:00 | TERRA_M-M | BURITIRANA | MARANHÃO | Brasil | 2102358 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| dae5e6a2-13f0-3cf0-bc95-011dc072823b | -5.64234 | -48.24941 | 2025-10-27 00:13:00 | TERRA_M-M | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 1a36f709-d6f1-3c79-8af2-ee4400b18e92 | -4.48213 | -43.68695 | 2025-10-27 00:13:00 | TERRA_M-M | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 1348c44f-0429-3003-b73a-ca2384bfe2a8 | -6.49427 | -42.21217 | 2025-10-27 00:13:00 | TERRA_M-M | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 8.1 |
| 3b184ea8-b475-3d66-8a54-7b109fa99165 | -4.8087 | -38.66577 | 2025-10-27 00:13:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 11.9 |
| 85d52c47-4156-3d11-973a-ebd10955c7df | -7.43886 | -41.87046 | 2025-10-27 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 44.2 |
| 3007c24e-0360-3ab1-8dd4-82359dd0b2c3 | -6.11149 | -41.7533 | 2025-10-27 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| b81ababf-3ae6-313c-bdc2-48812de13505 | -9.30311 | -45.22992 | 2025-10-27 00:13:00 | TERRA_M-M | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 1a833bae-0ca3-3b91-b45f-4cb61abda2b6 | -7.83011 | -46.44814 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.3 |
| 027d9384-20db-3a92-98ce-1b9b685c14e2 | -7.85129 | -46.47869 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 33.9 |
| 312b2412-b72f-301e-a285-fc7e293f58b4 | -6.79081 | -40.99842 | 2025-10-27 00:13:00 | TERRA_M-M | MONSENHOR HIPÓLITO | PIAUÍ | Brasil | 2206506 | 22 | 33 | nan | nan | nan | Caatinga | 138.7 |
| 7df3446b-0e81-310d-a99a-c3c22d1a44f2 | -9.26792 | -46.40226 | 2025-10-27 00:13:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| a4d36868-b487-3f5d-9f93-89284e00c31f | -4.44427 | -43.41735 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 76.2 |
| 2a9180fc-b203-35bd-acc2-884b58818806 | -7.599 | -45.69629 | 2025-10-27 00:13:00 | TERRA_M-M | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 7d9b5f54-75e0-30c1-b4a0-c4db6a4f057b | -4.45627 | -43.43549 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 28.5 |
| cb392319-82ec-39e9-bb81-6e51dd95ec5c | -6.92615 | -50.7364 | 2025-10-27 00:13:00 | TERRA_M-M | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| ab760b4a-3f86-3913-96a3-0590d6baf0e5 | -4.95124 | -44.87315 | 2025-10-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 9d6c40c3-c9aa-3c52-a366-ab1298610121 | -7.39205 | -44.7943 | 2025-10-27 00:13:00 | TERRA_M-M | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| e0113bf1-e6e0-329c-b58f-a851a3b56b8d | -10.01984 | -44.07141 | 2025-10-27 00:13:00 | TERRA_M-M | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d7e44ea3-4bbf-3331-8b8a-a22670c94903 | -6.12655 | -41.71611 | 2025-10-27 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.2 |
| db1dace1-4fda-326a-95f4-408abc06db2f | -7.00695 | -46.97684 | 2025-10-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 79a72691-c9e2-3f7b-bf2a-0aff543629da | -5.5403 | -41.4113 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 10.4 |
| 8bef86ea-62da-3b16-97b1-c759a86ed944 | -5.54225 | -43.95277 | 2025-10-27 00:13:00 | TERRA_M-M | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 4afa58a3-6012-3672-a854-eb5d64082655 | -10.90011 | -48.02495 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| a990a947-ed9b-3d06-99e6-76f12bbf626b | -11.42681 | -46.11175 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 10.3 |
| d4b0d8be-c27a-3e9a-b6ae-33b4151a88c6 | -6.62578 | -46.12295 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 7.3 |
| bfbe47f9-0d8b-37b6-a04f-3fcf22709269 | -9.03114 | -47.46822 | 2025-10-27 00:13:00 | TERRA_M-M | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 94da32a5-59f4-333d-889d-4c8c7683e800 | -7.79631 | -45.38348 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| c0c5a703-2943-3f2c-8c73-b2a0522fd051 | -7.85849 | -45.37472 | 2025-10-27 00:13:00 | TERRA_M-M | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 5fd4748b-bbb9-3ebf-8e93-b11514113f08 | -10.73503 | -44.18886 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 094c4bf1-da05-3ab9-975c-7c909786f193 | -6.45337 | -42.33743 | 2025-10-27 00:13:00 | TERRA_M-M | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 11.1 |
| 1ee45856-1cb8-3c49-9563-4fda0e486731 | -5.80169 | -43.96267 | 2025-10-27 00:13:00 | TERRA_M-M | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4bd77f74-d41c-3ebe-98dd-c054f2ed08da | -8.49118 | -41.22415 | 2025-10-27 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 12.8 |
| 66706cb5-3479-3b06-919a-df99a21949c1 | -10.66679 | -48.05457 | 2025-10-27 00:13:00 | TERRA_M-M | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 4660df81-aba7-331e-a97a-9aa492c43060 | -7.84597 | -46.49564 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 28.7 |
| 663ea34d-1cef-3ffb-91d5-8c1832909fde | -6.64052 | -44.62556 | 2025-10-27 00:13:00 | TERRA_M-M | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 7.9 |
| e85e0e0f-4aa2-3f52-bc7a-62f5f5f8a2e4 | -11.15429 | -46.20908 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 17412602-3377-348b-bbf1-c9e8d449d08e | -6.14567 | -43.13443 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 03016ce4-0c38-3593-b715-d4f4d804d15d | -9.46294 | -47.72702 | 2025-10-27 00:13:00 | TERRA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 112.7 |
| 47f7b149-8bcf-3e80-becc-eb2a4a18106e | -8.03722 | -46.75831 | 2025-10-27 00:13:00 | TERRA_M-M | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| b7fa0639-dc6d-39de-a08f-e6eb2680a6f8 | -10.67955 | -44.58683 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 0fcc93a1-ecf5-31d5-b8cf-5fb7b232d4d6 | -7.42911 | -41.87191 | 2025-10-27 00:13:00 | TERRA_M-M | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 19.5 |
| 7ce0e789-9781-3232-9d31-b3cc46d9369a | -5.28606 | -44.62953 | 2025-10-27 00:13:00 | TERRA_M-M | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 29629c61-7894-37c1-8807-39adba878063 | -6.57936 | -48.76004 | 2025-10-27 00:13:00 | TERRA_M-M | PIÇARRA | PARÁ | Brasil | 1505635 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 75a5f934-2cba-34f2-9f24-270e829637c7 | -7.93094 | -47.19234 | 2025-10-27 00:13:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 5fccb7a5-78c6-3298-9d79-8dc1261ec944 | -6.98091 | -39.11945 | 2025-10-27 00:13:00 | TERRA_M-M | AURORA | CEARÁ | Brasil | 2301703 | 23 | 33 | nan | nan | nan | Caatinga | 12.3 |
| 37d84d1c-4630-3cf8-a934-073e9f1690a6 | -6.14142 | -41.81878 | 2025-10-27 00:13:00 | TERRA_M-M | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 0f06247b-3e92-3cdb-9830-af8fdf1e4b50 | -7.85386 | -46.49815 | 2025-10-27 00:13:00 | TERRA_M-M | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| d3e0f99a-c8ed-36da-9213-8cce7c5940b3 | -8.9763 | -44.25891 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 7eca28e7-d1d1-3ed7-8d0b-3f1ba80e3e3f | -10.04955 | -48.16498 | 2025-10-27 00:13:00 | TERRA_M-M | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 31.0 |
| 81220f46-01e6-32ba-8439-b9f11ec0ce2b | -4.8059 | -43.30083 | 2025-10-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 374e667b-f827-3f89-ab78-83ab96ee5818 | -9.27125 | -45.60479 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 2a02f0f1-c660-3c42-8dd0-ccf537e85830 | -5.64238 | -47.63519 | 2025-10-27 00:13:00 | TERRA_M-M | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 17.0 |
| 9b3d4cda-306f-3151-9298-2344251395b3 | -9.48346 | -46.86085 | 2025-10-27 00:13:00 | TERRA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 6b284b3e-7d5b-3d48-8a87-e1c44f7003bd | -11.15561 | -46.21917 | 2025-10-27 00:13:00 | TERRA_M-M | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 90048a70-a9c2-38e6-b8f9-2de0d00a7ba6 | -4.44564 | -43.42709 | 2025-10-27 00:13:00 | TERRA_M-M | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 32a2e6d4-b459-3684-b04e-ca7541414c6e | -5.07133 | -44.73558 | 2025-10-27 00:13:00 | TERRA_M-M | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 65023aac-25e2-39f4-bce6-0494ce67ea34 | -6.99891 | -46.9881 | 2025-10-27 00:13:00 | TERRA_M-M | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| c325fc0c-32f3-38e8-b870-b7243ea425db | -5.65838 | -46.45639 | 2025-10-27 00:13:00 | TERRA_M-M | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 1b48006f-fe6b-37e3-9ea0-6f699033f23f | -6.5412 | -41.61189 | 2025-10-27 00:13:00 | TERRA_M-M | LAGOA DO SÍTIO | PIAUÍ | Brasil | 2205599 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 003dddba-c532-3589-9a17-ec3c088fdbde | -5.08849 | -47.14766 | 2025-10-27 00:13:00 | TERRA_M-M | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 45e02115-715f-3cbb-a76f-650fb92f1637 | -5.42922 | -40.87271 | 2025-10-27 00:13:00 | TERRA_M-M | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 10.8 |
| 14e08a70-a5e6-340b-9fdc-5b7da6512455 | -5.54097 | -43.9436 | 2025-10-27 00:13:00 | TERRA_M-M | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 9.6 |
| fae7e91f-1c66-34e4-b316-8eafc13e1e39 | -7.83799 | -46.43725 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c9eae21a-f942-3370-893e-d9d6fdb9dade | -10.20919 | -44.71203 | 2025-10-27 00:13:00 | TERRA_M-M | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8dd9d4fc-390b-3812-aa5c-6272154854ec | -7.90956 | -45.681 | 2025-10-27 00:13:00 | TERRA_M-M | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 64e10136-930f-3537-b821-bc8624a41023 | -5.1038 | -43.20338 | 2025-10-27 00:13:00 | TERRA_M-M | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 13.9 |
| cf27832d-0ce0-3227-b349-977a7ab58bb4 | -8.49205 | -41.23005 | 2025-10-27 00:13:00 | TERRA_M-M | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 16.1 |
| 28028635-bbf3-3d84-9671-47e847ba0608 | -8.36168 | -46.16553 | 2025-10-27 00:13:00 | TERRA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 68beef25-774c-34a4-8a6c-946d4a13ace0 | -8.86034 | -44.28149 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA LUZ | PIAUÍ | Brasil | 2209302 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a6bbfd7a-4e95-3c07-9775-a9ca958be635 | -9.13177 | -45.86547 | 2025-10-27 00:13:00 | TERRA_M-M | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 24.3 |
| 5e6c003a-f89b-31d8-b3a4-823ca4125af1 | -8.09727 | -47.06161 | 2025-10-27 00:13:00 | TERRA_M-M | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 543c1d32-c6db-382b-ae78-54bdfdd99d57 | -4.81858 | -38.64299 | 2025-10-27 00:13:00 | TERRA_M-M | IBARETAMA | CEARÁ | Brasil | 2305266 | 23 | 33 | nan | nan | nan | Caatinga | 23.5 |
| 419bf87a-f652-3a22-ae79-9c10e2bdda20 | -5.54886 | -41.3974 | 2025-10-27 00:13:00 | TERRA_M-M | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 8.4 |


[Clique aqui para ver as próximas entradas](README4.md)
