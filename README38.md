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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b226c478-dd93-38fe-a409-af044d7a119b | -2.78163 | -49.31512 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7c361966-96ff-308d-8e78-87b421e6e7e0 | -2.77814 | -49.31458 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d7df2125-ead9-3379-a1ef-d06834fbbcb0 | -2.77466 | -49.31404 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 419efc31-4aac-36e1-b1e8-e7f13e4e0c33 | -2.76948 | -50.46322 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| da6f7f47-f15f-3504-85ca-da3db0392f2b | -2.76598 | -49.30086 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 10b272b3-6be6-32a5-8e67-9ff5f4b26648 | -2.76539 | -49.30471 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9ce0381e-dd62-3077-8394-047ee773e9a1 | -2.7648 | -49.30857 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9e8c04cd-5897-3f19-bbbb-db0e7f021cce | -2.7642 | -49.31244 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bdb6eed2-0de1-313b-920b-e81a4e3630e8 | -2.76309 | -49.29646 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 541aad5c-659b-3628-a259-dcddbdb1373e | -2.76302 | -49.32015 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0f2b7ece-f7a2-3ccd-83c3-6ad864bc372f | -2.7625 | -49.30032 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59923256-5aa8-3f56-9c26-550703c9b189 | -2.76242 | -49.32399 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 45ecc5b0-0b93-383d-9454-7a7cc399d362 | -2.7619 | -49.30418 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 2470b199-f533-3a2e-95e1-59f61eb06d99 | -2.76183 | -49.32783 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2ba5ac86-c765-33e4-8f32-8118651691b2 | -2.76131 | -49.30804 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 94e72003-1adc-362f-8b03-f8317ab0b46f | -2.76072 | -49.3119 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5f548d99-2bd8-3a76-b6b1-fba321a005f1 | -2.76012 | -49.31575 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59cddaff-6d41-3255-8e4d-43301a75fee1 | -2.75953 | -49.31961 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e66c4e38-142f-32bd-b7f4-45a3f6549035 | -2.75894 | -49.32345 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eca9ba22-0c22-38c2-912b-a376892f88c2 | -2.75842 | -49.30364 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1c5f35a5-ff7f-361d-946b-be7d098ca49b | -2.75783 | -49.3075 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6b49cd4f-04a9-37d2-a737-dabf541188ed | -2.75723 | -49.31136 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40caf8c8-8f10-3f49-acfe-ac75f5d84610 | -2.75664 | -49.31521 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1657b66f-3626-3922-bd4d-96d026240381 | -2.75605 | -49.31907 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 9a4df787-9a65-3113-b433-863009e86dcc | -2.75546 | -49.32291 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1069fa85-a993-38ce-8030-c02965165478 | -2.79879 | -49.25044 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bbb7f4c8-938f-378e-a6cd-344469ba6252 | -2.79589 | -49.24603 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| eb28306d-8f50-30fb-a346-20b443fa3c4e | -2.79469 | -49.25378 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3d4678d1-a202-303f-8e41-3af72aa96d85 | -2.78661 | -49.23664 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dd046dd1-0f7c-354a-b337-5cb9e834be75 | -2.6934 | -49.04273 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 6130124d-c280-3bad-91a5-12c30f816819 | -2.61938 | -49.1205 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 1d5bbfc0-6472-344a-ba60-7580c0a7831f | -2.58914 | -49.19968 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2fe0f6b4-591c-3020-b20c-f7d22963dc3e | -2.58312 | -49.23845 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 0f73e00e-dc6e-3071-b09f-439fde6b5547 | -2.57843 | -49.24565 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cb11e762-ee48-3178-9e2e-8e9c2acd4cf5 | -2.57717 | -49.13797 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 215df05c-2351-3f44-9e8e-c4d0a3a14f88 | -2.47846 | -49.11975 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4597d34e-9e97-3d57-bce2-0217f88ba387 | -2.47737 | -49.10359 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e4b30418-7379-348a-87b6-6b5f66c81eae | -2.46866 | -49.09021 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| becfbb9f-24b9-3dc9-bdf8-3c47156b37b2 | -2.46805 | -49.09413 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ec963d0c-fd79-39ed-ba8f-e44f0bbdd0e7 | -2.75434 | -49.30695 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ff24737d-a1d7-3fac-80b5-14348dfda195 | -2.75375 | -49.31081 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 23fc56f0-f84e-314c-a85d-095212ca5ee9 | -2.75316 | -49.31466 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4b06bfcb-3d92-300d-99e3-7ecb54c0b2b0 | -2.75257 | -49.31852 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cfcee7ca-b1d0-3ea9-91ce-8aa7c1ee71c9 | -2.75198 | -49.32237 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d5f41ab5-3337-33f8-b99b-c809ca5a18e6 | -2.74908 | -49.31797 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e5ea86cc-7d1d-3e29-b9d1-273beb441d87 | -2.7467 | -49.97333 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 713d0ea3-1d74-34ae-9b38-e741d9937995 | -2.69322 | -49.32214 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3fb3afae-5615-3c81-baf1-2cfe219b8d6d | -2.69093 | -49.31392 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dd2b2aaa-4f8c-3972-a103-29265e644a94 | -2.69034 | -49.31775 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5241e28-ae60-3575-bdf7-ab90a0b5a2de | -2.68974 | -49.32159 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9453a688-836b-320c-b863-8f9f37dca939 | -2.68914 | -49.32544 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 95352f49-66a7-39ff-bdf7-900dcfa83849 | -2.68626 | -49.32105 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bebc535e-7f07-3f2b-9aad-3435d7dcfb6f | -2.68338 | -49.31666 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5c8f442d-79c2-3250-9701-b0840c348210 | -2.642 | -49.99138 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 38611e78-b96a-3d67-aab3-3ae842cb8286 | -2.62615 | -49.98148 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 72251c35-b9af-3b31-88c8-0b54769cc5e4 | -2.62275 | -49.98095 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96450731-805c-34e1-8004-288deb0eff86 | -2.62219 | -49.9846 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 26677bfd-0e81-3a24-99bc-08c8021193c6 | -2.62112 | -49.98489 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5ab639d8-e269-3e9e-868f-02a251a17e05 | -2.54357 | -49.85674 | 2024-10-23 04:51:00 | NOAA-21 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aa448d48-b0fa-3d59-a700-536ec5b5d908 | -2.50613 | -49.73392 | 2024-10-23 04:51:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fcd8df8d-ffd9-3820-848e-30d422861714 | -2.44063 | -49.61395 | 2024-10-23 04:51:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 2b6ab56f-e652-325c-aa3a-f78371128011 | -2.4174 | -50.36925 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c7f7d8d0-3137-3fdd-be01-4578bb249e19 | -2.4074 | -50.41129 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a2cdee58-71f7-3814-b415-e38db5636139 | -2.40405 | -50.41077 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e811ff0c-f7e8-3fb2-83bd-95165ef7faba | -2.22983 | -50.30796 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| dfbc3d8d-ef91-3b5e-8745-f7641eee5027 | -2.16042 | -50.24621 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| def0307f-9e6a-3a0e-bd67-68268e65b018 | -2.69382 | -49.31829 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a508df5c-8d98-3529-9e8a-3e4294e2afae | -2.68745 | -49.31338 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 6bf25c84-8a75-3872-b020-26ec8368abd4 | -2.68686 | -49.31721 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ef8881ed-58c1-3c02-88bf-47ab0a80063f | -2.65218 | -49.99295 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6cef5824-c724-3cb3-ba23-d365c2eb1bd9 | -2.64935 | -49.98879 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 02b1907a-f99f-3ee2-9312-e06e7effd52f | -2.64879 | -49.99242 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8f84f1e-3f56-3f3b-80d8-131fc584f68d | -2.64256 | -49.98775 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ed4856db-b22d-3255-92ce-9e173a5ec3ad | -2.62503 | -49.98877 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7b93c756-bda4-36e5-be43-334c206085bd | -2.62169 | -49.98125 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 35da8101-d328-3c5d-a966-ba36afa80341 | -2.62163 | -49.98824 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f445b99-b661-30f9-8971-1bd14ef0e241 | -2.61877 | -49.1244 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| c31d8937-e83c-364d-ba20-49b00f715251 | -2.61787 | -49.26755 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 94ddab1c-e91b-3a2a-9e2b-49f2ce4e738a | -2.58601 | -49.24286 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 62c0a68b-12ea-3199-8838-3fccd1b969a5 | -2.58541 | -49.24672 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| e0ef5e07-3f0b-3ee7-923c-9ad2fc1d4639 | -2.58252 | -49.24232 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9e6bf94a-b65c-372a-b9ea-8fc75ccf863a | -2.58192 | -49.24618 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 622e6797-c0cb-3c02-bbe2-610bba1cf5a3 | -2.57903 | -49.24178 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3abd0b9c-7d3a-356f-a262-dfcc46aceff0 | -2.54898 | -49.18151 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3558e65f-3d7e-38e1-acbc-ee74c107d3bc | -2.54608 | -49.17708 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 16e31330-4bb6-3c37-9b80-3379fa471c36 | -2.49048 | -49.3861 | 2024-10-23 04:51:00 | NOAA-21 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5440a780-8063-33ed-9b83-188c34478724 | -2.47386 | -49.10305 | 2024-10-23 04:51:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 01af0ba8-a4ae-311a-b1ff-4c7dee8d974b | -2.53877 | -50.3336 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 882f99fa-be32-3315-beab-e79ff40bbb49 | -2.42292 | -50.28994 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 176e04f3-edd1-3792-a8d6-8a76930741b0 | -2.42236 | -50.29351 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8d728d68-bdf6-36ed-ad80-29134b58e8bf | -2.419 | -50.29299 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 91ad76e4-2155-3e32-8c05-3df431638b71 | -2.4046 | -50.40722 | 2024-10-23 04:51:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2c84be79-986b-325a-bce0-98af17245e72 | -2.38881 | -50.31021 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 440520de-4d0e-3831-aeff-a29bfe21547b | -2.22648 | -50.30744 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4dc4971f-76f6-3df0-bb59-e6bfd5218339 | -2.22592 | -50.31099 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4fccb87a-6da7-350c-ab1b-e574d44bb7b9 | -2.22313 | -50.30692 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3b938b18-ce18-3477-83c2-162ff8ceb2ef | -2.22257 | -50.31047 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9984abb6-30fc-33c1-bd3a-0c1a0d1e48dd | -2.20021 | -50.29974 | 2024-10-23 04:51:00 | NOAA-21 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b66594ba-3cb6-371f-9a0d-e2e2ece6d29a | -4.97092 | -49.646 | 2024-10-23 04:51:00 | NOAA-21 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3b891ec2-1ebe-31d6-9a2d-e0fe226afb64 | -4.48162 | -49.64329 | 2024-10-23 04:51:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README39.md)
