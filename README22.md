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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8e58ea20-35b8-3d2c-9755-4ecf278cafc4 | -12.03454 | -46.92792 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d9a0ad36-2ffd-3d73-9ee3-326cc6c67756 | -10.42216 | -49.37069 | 2025-10-24 04:17:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 99e01d67-7fe2-3f38-9f79-f9a4988ebfe1 | -5.587 | -41.31953 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| b882c6f8-18e2-3802-b7f2-734652cd5a36 | -12.07427 | -46.42543 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| caf2cfdd-697d-3b89-b7a7-e45e17acad8c | -5.10458 | -47.7939 | 2025-10-24 04:17:00 | NPP-375D | CIDELÂNDIA | MARANHÃO | Brasil | 2103257 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 55803c0b-1506-3040-82a1-e46dc223c0dd | -4.63701 | -42.51181 | 2025-10-24 04:17:00 | NPP-375D | JOSÉ DE FREITAS | PIAUÍ | Brasil | 2205508 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 074e96fe-252b-3c5a-bf47-8f3792cdd9b4 | -5.5439 | -41.37327 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9a823795-db68-338f-9410-3f0ae4b8349b | -11.09884 | -41.61518 | 2025-10-24 04:17:00 | NPP-375D | SÃO GABRIEL | BAHIA | Brasil | 2929255 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5578b2e5-a52d-315f-8941-5c618ab5db4d | -2.25136 | -47.02115 | 2025-10-24 04:17:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c19e682-1081-3728-a293-e8a395d6f45a | -4.81114 | -50.93369 | 2025-10-24 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ebb242cf-4606-3eee-af5d-201ffe762345 | -3.01445 | -49.45129 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4d1fb4b-b9a5-386e-abc9-b370a8deed29 | -11.5165 | -47.22128 | 2025-10-24 04:17:00 | NPP-375D | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 32344680-ba97-3719-9422-352cbc33a4da | -5.86089 | -48.19716 | 2025-10-24 04:17:00 | NPP-375D | ARAGUATINS | TOCANTINS | Brasil | 1702208 | 17 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c9d8e4df-a5cf-3904-8c82-8f49a2a6419a | -2.85633 | -50.7484 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f68541ef-5588-3a74-a8b1-959b68f98c39 | -12.2482 | -47.03191 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0fc631e-892b-36eb-b35a-8e9557af1a12 | -10.27234 | -47.88316 | 2025-10-24 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b5fded07-e142-3320-ad4c-405fa097e74b | -10.04244 | -47.10088 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 6f4a8be1-4b62-3005-8fbb-0f75706ea16c | -12.09758 | -47.00433 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5a66aa65-ed4f-33d7-ad6f-1fd5de640c00 | -9.35541 | -47.70189 | 2025-10-24 04:17:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b6823400-b977-3373-b8b7-9a4b2b4b7bab | -5.60959 | -41.12741 | 2025-10-24 04:17:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| acfdb360-b876-3009-8815-b92fe3328f72 | -2.87416 | -45.2558 | 2025-10-24 04:17:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 18391042-2bd5-3a5e-8d9e-559cc04db087 | -2.25889 | -47.84209 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a6a96efc-33fc-315d-8fc1-cdf6ad5684c6 | -4.59624 | -41.61015 | 2025-10-24 04:17:00 | NPP-375D | MILTON BRANDÃO | PIAUÍ | Brasil | 2206357 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 92bc93f5-8de2-3f21-aed6-6566b0f8b435 | -10.86913 | -44.41395 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9870e06b-9a30-3803-ac4d-9c40f5f174b5 | -10.94813 | -44.83222 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c0f5cb9d-3712-3d04-bce3-caf0ac638042 | -9.64417 | -46.89594 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| efbadb8f-496c-35ab-ac96-e5f565ee366d | -6.61591 | -42.10389 | 2025-10-24 04:17:00 | NPP-375D | BARRA D'ALCÂNTARA | PIAUÍ | Brasil | 2201176 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 2056d966-1e32-3639-b07b-638e2d4c990d | -12.07397 | -46.40575 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 85ed979e-d09f-3aa0-83d1-1bf5c0a04fed | -4.28314 | -40.70825 | 2025-10-24 04:17:00 | NPP-375D | IPU | CEARÁ | Brasil | 2305803 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3772b01c-ac8c-3045-99da-4c767388bf92 | -2.8017 | -49.14922 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 96169392-1585-33fc-b795-cbd76b2c3679 | -10.04091 | -47.08766 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c22303f2-e7d2-35b5-a822-65205261d048 | -11.81867 | -44.167 | 2025-10-24 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 19d70ca2-336b-3443-8e7a-ddcbbd1f43c2 | -11.87188 | -46.75562 | 2025-10-24 04:17:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| da75aeae-e98c-3dc5-94f0-e7a667a5166f | -3.46271 | -41.31224 | 2025-10-24 04:17:00 | NPP-375D | GRANJA | CEARÁ | Brasil | 2304707 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ea5c6bcb-bf61-37de-b606-cf9fd9ccf41c | -9.09186 | -46.53173 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b059f2d8-72dc-3e82-9ee3-0140e70af071 | -12.03253 | -46.5281 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ef1849f3-315a-3cac-83fc-b2112a771744 | -6.22708 | -41.37503 | 2025-10-24 04:17:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 3942c670-31ef-3f7a-8120-3a7b49bcdac3 | -1.92288 | -52.14487 | 2025-10-24 04:17:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 69f81ecb-df8b-3d97-add6-9b64e159918f | -5.65422 | -45.95184 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 53de1050-2e10-327a-a7e7-6a319280a18f | -2.85783 | -50.73949 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| acbb05bb-e412-365b-8b8a-8dd35d0cda28 | -3.28735 | -50.1937 | 2025-10-24 04:17:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0aa2230a-aa67-3234-bdf5-3c7273a10327 | -11.9778 | -49.17651 | 2025-10-24 04:17:00 | NPP-375D | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 3f691935-160a-3836-9bb1-8b24f64f07ad | -5.88804 | -46.28027 | 2025-10-24 04:17:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| afe8d6e4-10a7-3cea-b5e1-b487178684f2 | -11.78041 | -44.23673 | 2025-10-24 04:17:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 2fba5957-a56e-3015-b3b2-7e3c37d4bece | -10.03935 | -47.07464 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 03175b15-d4f3-3827-b643-8fd01ddffbb1 | -12.06991 | -46.40899 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51d084eb-bdae-308c-843c-75fc5d1ff0ab | -12.2447 | -47.03125 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 735d81b6-f186-3327-af8a-e6a11f003821 | -9.20061 | -44.54144 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| bde79613-904a-386c-8504-a2ad21670af8 | -5.43142 | -40.8798 | 2025-10-24 04:17:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.4 |
| ad5f202d-f7e3-3c20-8181-bbadcbbcdfa2 | -5.56522 | -46.5235 | 2025-10-24 04:17:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6d56fc41-33aa-3ec9-b21b-b9d3f1b662d1 | -10.01772 | -47.07087 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d60427b8-bba1-36cc-87cd-2a3c086c41cc | -2.85733 | -50.74245 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c621f2da-cf1e-3b82-98db-a4d040f3ff96 | -3.45194 | -41.85326 | 2025-10-24 04:17:00 | NPP-375D | CAXINGÓ | PIAUÍ | Brasil | 2202653 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e3eeca62-4399-3b31-9aff-fb45d868cda9 | -10.87246 | -44.41449 | 2025-10-24 04:17:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3e8cc4ef-d9cb-38a4-bb7b-566fdd8c64d8 | -5.75882 | -46.68701 | 2025-10-24 04:17:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| db8b7fe3-a211-3e0a-84a3-f55cd8f6ecc8 | -12.0752 | -46.44127 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0ca34fa4-d681-3605-bee7-261c879f7cb8 | -3.80132 | -51.76088 | 2025-10-24 04:17:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d83f537-b564-3db7-89e1-e55b16e337ff | -9.27129 | -46.45472 | 2025-10-24 04:17:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 6e34b379-be52-381d-9920-d48a2587bbfd | -9.23307 | -45.59125 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 431972d2-d502-39a6-9060-b7eed538628f | -4.61095 | -46.59716 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a711103-569d-3002-b5e6-326123d31c34 | -4.87239 | -47.53279 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 3fc54d6c-7a7a-3ec3-b845-8c4236681435 | -3.15187 | -50.16695 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4d307c09-07cc-38b9-8868-50bf12f30466 | -4.24461 | -48.12989 | 2025-10-24 04:17:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 2b78c7b9-6fab-33c4-9046-f71640a54c17 | -11.05381 | -45.39547 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5fb704d8-fa48-3e64-b1f7-b5cb18c12b27 | -2.26607 | -47.8511 | 2025-10-24 04:17:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 18016f08-bb07-3f70-900c-3eb61ec48125 | -2.80781 | -49.1407 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 39ba022c-4a1d-348b-ba23-2b89ad758dff | -2.85173 | -50.74459 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 91c840e6-817a-3c62-9e1b-f00cfcaf859f | -10.27685 | -47.87937 | 2025-10-24 04:17:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 55b62b83-8262-30f4-a77a-89b1c8676e1d | -4.81853 | -48.67504 | 2025-10-24 04:17:00 | NPP-375D | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| fcaf1d71-e58b-3f61-90fd-247407abafdf | -12.27828 | -47.02493 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 717434e2-6a6a-3199-9d88-9f2f8f0e5d20 | -10.55781 | -49.00022 | 2025-10-24 04:17:00 | NPP-375D | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e390809-a661-33e1-91ce-1b7b23cf3923 | -9.60773 | -46.8868 | 2025-10-24 04:17:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 19e55d8d-e675-3d6e-acee-d6c877e6b412 | -11.36546 | -45.93029 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a47b7f12-1c72-320e-a286-1c7183d13b84 | -8.73788 | -45.83731 | 2025-10-24 04:17:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 4fde7961-80fc-32c9-9c14-8e6e3964f899 | -10.64288 | -52.18203 | 2025-10-24 04:17:00 | NPP-375D | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 597f9662-e8d9-3fc2-98bb-7b4dc3138e06 | -2.42037 | -48.44419 | 2025-10-24 04:17:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 7f4d715a-f7cc-3426-83be-69d6d0b90cb9 | -3.22141 | -46.80679 | 2025-10-24 04:17:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5fd5b182-8f29-3950-b9e7-7ee10930e75f | -4.87869 | -47.54418 | 2025-10-24 04:17:00 | NPP-375D | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2b4e4a0-c9cd-3763-8276-57c330f6f7a0 | -2.47409 | -49.23379 | 2025-10-24 04:17:00 | NPP-375D | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 718981a7-1fe8-3463-ad58-7b35a5541039 | -12.18079 | -46.56491 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 388477f8-8042-357b-bb67-44c8c0a7b2d5 | -4.18075 | -42.98205 | 2025-10-24 04:17:00 | NPP-375D | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 066756e4-d883-3bc5-a613-e092bb2de142 | -3.78373 | -43.90147 | 2025-10-24 04:17:00 | NPP-375D | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c13bfda6-9b18-31be-be6b-953b0de99a72 | -12.06307 | -47.98387 | 2025-10-24 04:17:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 24655345-b466-3ed0-b5c0-ac02378dde44 | -5.96516 | -44.12511 | 2025-10-24 04:17:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 699d72eb-644f-3cb8-a028-a6191341dda1 | -10.61493 | -42.29963 | 2025-10-24 04:17:00 | NPP-375D | ITAGUAÇU DA BAHIA | BAHIA | Brasil | 2915353 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5964b339-6168-3596-8d7d-3f75895cba68 | -10.94808 | -50.3822 | 2025-10-24 04:17:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2d37388e-a34d-38b3-a7c2-b7e1ca9a5605 | -4.81015 | -50.93952 | 2025-10-24 04:17:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2d31b52e-42e6-33ed-9654-72f2d0d5b7f0 | -2.86642 | -50.71959 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b69f6839-d115-3714-9d36-4799dcc65a95 | -11.36119 | -45.95632 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| b545bcdc-2a0c-34dd-ba87-4069c1c8e499 | -10.97604 | -54.25224 | 2025-10-24 04:17:00 | NPP-375D | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 99fb70f3-d6ef-3654-ba59-6d7f9bb32682 | -11.36485 | -45.93402 | 2025-10-24 04:17:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.1 |
| a9dc2df2-5673-35d3-8324-6cc9df6dd65b | -12.15343 | -47.01651 | 2025-10-24 04:17:00 | NPP-375D | TAIPAS DO TOCANTINS | TOCANTINS | Brasil | 1720937 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 90d9b06a-89d2-379b-bc8d-6381fc428fd5 | -3.02288 | -49.48748 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 42e6e341-aefd-3af7-a500-6e39be065f5a | -12.06896 | -46.43623 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 6c7a8475-0894-32d9-b7ab-7f7ead7c9cc3 | -12.3179 | -47.26246 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3e5c6d72-0e37-3074-9903-71adc9840970 | -3.14698 | -50.1662 | 2025-10-24 04:17:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 04856be1-0519-3928-8c3c-f6c1986ec0c9 | -12.31367 | -47.26589 | 2025-10-24 04:17:00 | NPP-375D | CONCEIÇÃO DO TOCANTINS | TOCANTINS | Brasil | 1705607 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| e1e6b7cc-97d5-34e2-9004-ca1204680385 | -3.08918 | -49.25185 | 2025-10-24 04:17:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2684ba69-fee4-3b7b-8cc3-9eabf9f7054e | -12.06116 | -46.41919 | 2025-10-24 04:17:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d615923-b552-3a3e-aa34-dff7cf45c44f | -6.53609 | -41.67966 | 2025-10-24 04:17:00 | NPP-375D | INHUMA | PIAUÍ | Brasil | 2204709 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README23.md)
