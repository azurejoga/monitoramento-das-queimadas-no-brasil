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

## Dados Diários - Página 113

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| bcd0a373-87d3-33c7-a226-1d8a348103bb | -9.41598 | -47.33685 | 2025-10-01 04:51:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| faaae7fa-d8d8-3422-8fc0-317d08d8b37b | -10.47752 | -55.62179 | 2025-10-01 04:51:00 | NPP-375D | COLÍDER | MATO GROSSO | Brasil | 5103205 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 74c0e7a5-e169-3aae-b7f7-a593fc0559ab | -13.77314 | -47.97566 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 27.6 |
| ec89a679-7e6c-3bc7-82cc-c4e05a1b370f | -14.18878 | -46.124 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 7.4 |
| fe9e9b90-60b4-32b6-8680-1a1dd3e83d75 | -11.13278 | -43.37825 | 2025-10-01 04:51:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 0.6 |
| 1c332ff6-cccd-31ed-ba38-816b2437b422 | -11.9468 | -43.91857 | 2025-10-01 04:51:00 | NPP-375D | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d5dba423-9b25-3679-ae29-96ef333cc293 | -8.98655 | -50.19748 | 2025-10-01 04:51:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| be33a712-b229-3ab7-9f39-1f2dda62b0ce | -14.43571 | -46.36259 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 6f24c842-e5b5-30a3-8e8a-c938a16d92e7 | -14.35838 | -47.14055 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 31baeb62-d805-3ce6-9b93-ac5f9d5cdfb9 | -11.57182 | -50.18181 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 26f69917-4447-3f7e-b70b-370e59db84be | -15.01105 | -56.03926 | 2025-10-01 04:51:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 153d6b29-ea20-3bcf-ad09-62cb95eabf32 | -11.81847 | -44.988 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 3b82a8f1-8ab0-3457-a92e-c3cdac108768 | -12.83772 | -47.03295 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 400e18c1-abe1-30ff-b41c-ad0cb3a56cc2 | -11.62881 | -47.49414 | 2025-10-01 04:51:00 | NPP-375D | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 68c9bfe1-817f-3126-a7d4-9ba125f91a40 | -14.90067 | -48.13233 | 2025-10-01 04:51:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7c3bdd50-5105-35a8-bb33-371fc837ef9b | -14.19051 | -46.1103 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ebf3c937-5793-3ff3-8992-a861213418c4 | -13.36437 | -47.29081 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 262f84bf-24d6-35ee-b104-ded7ef6f8175 | -14.7015 | -48.22675 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 177ac346-878f-330d-9cfb-3e71c8bd5021 | -13.33172 | -48.14653 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| feb070f2-e8e3-32ba-aff3-937a0d12b35b | -13.55567 | -47.27616 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3c8d31aa-e3ea-3a99-998e-4a9538393577 | -13.35196 | -48.14436 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 309f5c2c-83a0-352e-bead-20a6c93331aa | -13.70972 | -48.6533 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 1faa6e92-1e2f-3a19-b07b-1db78aa679a4 | -10.74325 | -45.37747 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 5064b430-bbf7-3077-b918-0e973e906dae | -13.73541 | -48.69078 | 2025-10-01 04:51:00 | NPP-375D | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e5b00396-118d-3755-ae1e-f442a3c82d17 | -12.88051 | -46.90788 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 489e92a5-36e5-33ed-9ad4-689890f01b72 | -14.0473 | -47.97107 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 10.9 |
| e57baccc-a15b-31eb-acd2-7e1e15a02866 | -16.08071 | -51.04808 | 2025-10-01 04:51:00 | NPP-375D | FAZENDA NOVA | GOIÁS | Brasil | 5207600 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f8750b08-7fc1-3515-a756-e686817420c5 | -13.94061 | -48.11397 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 6a1eb8b4-7c77-3b38-aa35-a66d80da7125 | -14.50994 | -48.49082 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2437211a-8b1d-3246-9286-0d2c6dde42fc | -15.15621 | -49.102 | 2025-10-01 04:51:00 | NPP-375D | SANTA RITA DO NOVO DESTINO | GOIÁS | Brasil | 5219456 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| a3803102-f79b-349c-be9b-72bae6b919e7 | -15.63544 | -46.2518 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 975bee61-5350-3181-8a09-3af7267ef474 | -13.29599 | -47.23651 | 2025-10-01 04:51:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| cbf5b443-507f-3802-888d-4a2cf290e180 | -13.29606 | -46.38475 | 2025-10-01 04:51:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 517c3907-3c97-3d9a-bf82-abc4ac93af40 | -13.0991 | -47.04044 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6f320699-55e9-31dd-a795-3a1fcd7fafd8 | -14.18992 | -46.11496 | 2025-10-01 04:51:00 | NPP-375D | POSSE | GOIÁS | Brasil | 5218300 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 0f3adb66-8c0a-34d2-8491-7304b293fe58 | -14.71091 | -48.12803 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.2 |
| a88ca64f-8518-36d7-94ab-055ff62a9a69 | -11.83826 | -48.05867 | 2025-10-01 04:51:00 | NPP-375D | SÃO VALÉRIO | TOCANTINS | Brasil | 1720499 | 17 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 5b785c1c-26fd-3de9-838c-0e224b7ef11c | -10.90563 | -46.51187 | 2025-10-01 04:51:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 68a021b5-b7d7-3475-8f63-ade2795b6324 | -12.88413 | -46.91265 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 733a3af4-c604-327c-9ee5-2cecfb0850f0 | -14.51131 | -48.47939 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 830b3b61-8448-3cdb-a4e4-2076f0f5ea91 | -9.4186 | -63.2136 | 2025-10-01 04:51:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 20c005f5-a4e5-3067-bc72-6fcf12892b88 | -11.35982 | -49.37397 | 2025-10-01 04:51:00 | NPP-375D | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 7a0336a6-2265-3680-8367-3cee459ca9a8 | -14.35415 | -47.14 | 2025-10-01 04:51:00 | NPP-375D | FLORES DE GOIÁS | GOIÁS | Brasil | 5207907 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5d66b139-864f-3948-9069-a79c1473dc15 | -14.68077 | -45.28704 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f460a615-1fdb-33d0-b0de-4e4e305f49f9 | -15.75737 | -43.69565 | 2025-10-01 04:51:00 | NPP-375D | SÃO JOÃO DA PONTE | MINAS GERAIS | Brasil | 3162401 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 47255d32-9cbf-3f97-81ce-1fa73fdff84d | -11.76242 | -46.86401 | 2025-10-01 04:51:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b53ec5c5-6f68-3966-81bb-99cb3414da0b | -11.20321 | -47.73618 | 2025-10-01 04:51:00 | NPP-375D | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 63a7c302-ef7c-3e32-b3f1-9a7aae4a914a | -12.78353 | -46.86652 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d62f270-e3dd-37f1-8dc7-bf1862442fe3 | -14.79408 | -45.77913 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2386a76-4420-323d-9036-e39bf2d76cb5 | -14.18981 | -46.10852 | 2025-10-01 04:51:00 | NPP-375D | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1fbc6ffa-5672-38b5-bb46-31cdc798877b | -15.48527 | -45.90245 | 2025-10-01 04:51:00 | NPP-375D | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f608ca66-56f5-3e6e-9898-ed6914ea6c4d | -12.14965 | -47.77392 | 2025-10-01 04:51:00 | NPP-375D | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 2ac9a90a-222d-385f-8c46-a56b889f48bb | -15.237 | -48.73395 | 2025-10-01 04:51:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4d930421-bcbf-36e6-a644-cebec6c0ee06 | -15.33896 | -46.27819 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 4.3 |
| d100c682-d957-3bc5-84ce-477f7b67672d | -15.48419 | -48.55253 | 2025-10-01 04:51:00 | NPP-375D | PADRE BERNARDO | GOIÁS | Brasil | 5215603 | 52 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 1d9d748b-8136-33d6-bc62-e5dec1b8ff8f | -14.20701 | -44.93379 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| be3e3005-62c7-362d-8804-2da38f54a2e3 | -10.06805 | -50.26006 | 2025-10-01 04:51:00 | NPP-375D | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aac75436-7f42-39dc-9c74-49f094c23b2b | -9.93903 | -43.59911 | 2025-10-01 04:51:00 | NPP-375D | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| fa26a4f7-b4ab-376a-b088-34b4e4806fbf | -11.05235 | -47.82181 | 2025-10-01 04:51:00 | NPP-375D | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 4.8 |
| a4f98448-a0b4-3990-b669-7d6e136945a1 | -13.77711 | -47.97619 | 2025-10-01 04:51:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 8afea674-37b1-33b7-8909-8140ec9677b8 | -14.39596 | -46.21117 | 2025-10-01 04:51:00 | NPP-375D | BURITINÓPOLIS | GOIÁS | Brasil | 5203962 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd59c60c-c248-373b-aa15-4d37bf85c123 | -13.7682 | -51.22628 | 2025-10-01 04:51:00 | NPP-375D | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 03d98a2a-d3cb-314d-858d-57cf3c1fdc7d | -14.78627 | -45.80388 | 2025-10-01 04:51:00 | NPP-375D | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 13.2 |
| eef45538-302b-3ddc-a2ff-bff9d8bdec99 | -13.30303 | -48.70341 | 2025-10-01 04:51:00 | NPP-375D | MONTIVIDIU DO NORTE | GOIÁS | Brasil | 5213772 | 52 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a17f1b7b-0efb-30c6-9c13-1bb444eafc9c | -14.99625 | -46.95137 | 2025-10-01 04:51:00 | NPP-375D | VILA BOA | GOIÁS | Brasil | 5222203 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 700e9948-9ede-3e80-aa5a-c8a382f876b5 | -12.82919 | -46.87587 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ecfd2e9e-fe63-3aec-a96f-917751ca75c3 | -14.6825 | -48.12789 | 2025-10-01 04:51:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 51d60785-2a23-352a-8d83-3b9180b25ae4 | -10.79856 | -45.35423 | 2025-10-01 04:51:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7d898cb1-4e05-33ae-a8a4-de29ad0c48f6 | -12.76406 | -46.91448 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c2ffa03b-c82d-3b41-98af-0df7055a7fea | -11.81628 | -44.93151 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 00414f48-6903-34fb-9b97-4a39e965d0ad | -14.04987 | -47.98222 | 2025-10-01 04:51:00 | NPP-375D | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 489f06e9-7a90-362d-8a46-011fb1c128e1 | -11.4606 | -45.09447 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9e42a783-e6b4-3275-a5e7-01e3fa6f519f | -12.42894 | -50.18183 | 2025-10-01 04:51:00 | NPP-375D | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 25554744-b525-3727-ad53-699150dacff5 | -11.57037 | -50.18145 | 2025-10-01 04:51:00 | NPP-375D | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6a745af3-fdfc-3c69-9734-1e05a75a3ae2 | -13.20964 | -47.32848 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 38a95348-2e6b-3b26-a190-2080333abb5f | -12.83722 | -47.03664 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8d7acd00-967d-3295-b73c-c8d0d5194bb9 | -11.84413 | -45.01133 | 2025-10-01 04:51:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2f697b30-ecd6-3012-88a3-9031ebc43e77 | -13.14955 | -47.4109 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 26dfe31e-70b1-303d-b00e-6f3d2cbfea36 | -13.23982 | -47.32215 | 2025-10-01 04:51:00 | NPP-375D | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 9d5c4c15-79c0-3e96-8ffd-26cedba20959 | -13.5624 | -48.20468 | 2025-10-01 04:51:00 | NPP-375D | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| bacbae31-2231-340a-9bc6-afe32f24ca5f | -10.04019 | -52.09528 | 2025-10-01 04:51:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 42750541-212d-3f75-991b-36ca1a05c9a3 | -12.00208 | -46.58424 | 2025-10-01 04:51:00 | NPP-375D | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3dfa5a1b-592e-34aa-8588-69949ad44ad4 | -12.94422 | -48.4136 | 2025-10-01 04:51:00 | NPP-375D | PALMEIRÓPOLIS | TOCANTINS | Brasil | 1715754 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 8c2a00ce-3591-335a-b406-98f18d9840ec | -18.62673 | -48.51361 | 2025-10-01 04:53:00 | NPP-375D | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 0.2 |
| 34dac149-8885-3c3e-9c1d-ffa04fde2d24 | -21.04613 | -45.67859 | 2025-10-01 04:53:00 | NPP-375D | BOA ESPERANÇA | MINAS GERAIS | Brasil | 3107109 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f8dd874a-19c9-374d-a790-a1759136c92e | -19.16482 | -44.52742 | 2025-10-01 04:53:00 | NPP-375D | CURVELO | MINAS GERAIS | Brasil | 3120904 | 31 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 87bbfa33-f65a-3bba-9e3c-96a3acb5ce81 | -22.10848 | -44.69931 | 2025-10-01 04:53:00 | NPP-375D | BAEPENDI | MINAS GERAIS | Brasil | 3104908 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 895c9b22-8963-3ec9-bc11-b7441a3137af | -16.25588 | -50.93562 | 2025-10-01 04:53:00 | NPP-375D | JAUPACI | GOIÁS | Brasil | 5212006 | 52 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 8b59bb57-c46c-34d8-b080-c2bab2be1cab | -20.50007 | -43.94009 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS | MINAS GERAIS | Brasil | 3118007 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| be48421c-f4b1-31d5-bf5e-4e3cf2673e3b | -22.27845 | -46.72729 | 2025-10-01 04:53:00 | NPP-375D | ESPÍRITO SANTO DO PINHAL | SÃO PAULO | Brasil | 3515186 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4958b080-7b9c-30ae-9c18-cd80e81b0433 | -17.67529 | -47.26083 | 2025-10-01 04:53:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 78e2636c-6362-3604-9cba-b04cc6483790 | -15.25305 | -56.85036 | 2025-10-01 04:53:00 | NPP-375D | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3e74c29e-3f72-323c-8ceb-3f4c984df38b | -20.68735 | -43.37382 | 2025-10-01 04:53:00 | NPP-375D | PIRANGA | MINAS GERAIS | Brasil | 3150802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 9312c697-21c6-3a09-aea2-6b4d1b015bc7 | -18.96426 | -43.71286 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f1500b42-118d-3792-8cab-8422c80cec84 | -20.12048 | -46.33576 | 2025-10-01 04:53:00 | NPP-375D | SÃO ROQUE DE MINAS | MINAS GERAIS | Brasil | 3164308 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b0e709ca-8594-3e9d-86d0-e236c231dbd6 | -17.96073 | -45.04157 | 2025-10-01 04:53:00 | NPP-375D | LASSANCE | MINAS GERAIS | Brasil | 3138104 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e9d24dc8-8f3f-3bc8-b8d5-d48ca2789f10 | -22.10736 | -47.80503 | 2025-10-01 04:53:00 | NPP-375D | SÃO CARLOS | SÃO PAULO | Brasil | 3548906 | 35 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b7e19c22-f3ec-31b1-b723-2a29f9c1d9c0 | -18.959 | -43.7085 | 2025-10-01 04:53:00 | NPP-375D | CONGONHAS DO NORTE | MINAS GERAIS | Brasil | 3118106 | 31 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50244931-ee00-32d2-bd90-89c87edcf857 | -16.41494 | -52.17907 | 2025-10-01 04:53:00 | NPP-375D | BOM JARDIM DE GOIÁS | GOIÁS | Brasil | 5203401 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| f00e4823-05b7-3e5b-8395-7b6fc4d78329 | -20.22828 | -43.89252 | 2025-10-01 04:53:00 | NPP-375D | ITABIRITO | MINAS GERAIS | Brasil | 3131901 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |


[Clique aqui para ver as próximas entradas](README114.md)
