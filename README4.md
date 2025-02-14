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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb9e1a09-5411-3a87-bb28-023021d7cd42 | -6.01173 | -36.46971 | 2025-02-14 11:53:00 | TERRA_M-M | BODÓ | RIO GRANDE DO NORTE | Brasil | 2401651 | 24 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 1d4a3a84-8e62-3378-bd48-dcd59d843da9 | -7.53668 | -37.3405 | 2025-02-14 11:53:00 | TERRA_M-M | SÃO JOSÉ DO EGITO | PERNAMBUCO | Brasil | 2613602 | 26 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 88f41f02-0528-3896-8027-0ac8df334956 | -10.34827 | -36.83562 | 2025-02-14 11:53:00 | TERRA_M-M | JAPOATÃ | SERGIPE | Brasil | 2803401 | 28 | 33 | nan | nan | nan | Mata Atlântica | 17.1 |
| d0b66f31-cd03-3258-9c6e-10fbb5952b9f | -9.11392 | -37.66092 | 2025-02-14 11:53:00 | TERRA_M-M | MATA GRANDE | ALAGOAS | Brasil | 2705002 | 27 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 34c662cc-c7e3-3f50-a5ce-d267e1d90de0 | -7.93891 | -38.37673 | 2025-02-14 11:53:00 | TERRA_M-M | SERRA TALHADA | PERNAMBUCO | Brasil | 2613909 | 26 | 33 | nan | nan | nan | Caatinga | 40.2 |
| 51fc454c-870f-357d-b76a-d243311a77ff | -8.02291 | -37.105 | 2025-02-14 11:53:00 | TERRA_M-M | MONTEIRO | PARAÍBA | Brasil | 2509701 | 25 | 33 | nan | nan | nan | Caatinga | 4.2 |
| 0c40eee0-b779-38c8-9f3d-2e4b63da7dd7 | -7.14657 | -37.42436 | 2025-02-14 11:53:00 | TERRA_M-M | SANTA TERESINHA | PARAÍBA | Brasil | 2513802 | 25 | 33 | nan | nan | nan | Caatinga | 8.3 |
| 666988b3-476d-37b7-8ca1-9d7918efd2a1 | -12.0548 | -38.42552 | 2025-02-14 11:55:00 | TERRA_M-M | ALAGOINHAS | BAHIA | Brasil | 2900702 | 29 | 33 | nan | nan | nan | Mata Atlântica | 11.7 |
| c9a7e833-f7c1-3b4f-9c16-b27cf4916ade | -12.81135 | -39.54469 | 2025-02-14 11:55:00 | TERRA_M-M | SANTA TEREZINHA | BAHIA | Brasil | 2928505 | 29 | 33 | nan | nan | nan | Mata Atlântica | 21.3 |
| 31235fba-3521-3050-920c-de773ca0dd8a | -11.8195 | -38.46188 | 2025-02-14 11:55:00 | TERRA_M-M | INHAMBUPE | BAHIA | Brasil | 2913705 | 29 | 33 | nan | nan | nan | Caatinga | 6.5 |
| 301d5d72-a9c0-3d0e-89d7-5dc9f75148a9 | -11.95748 | -38.77568 | 2025-02-14 11:55:00 | TERRA_M-M | IRARÁ | BAHIA | Brasil | 2914505 | 29 | 33 | nan | nan | nan | Caatinga | 15.4 |
| f47bf3b2-fb95-3fc6-9522-1c99550b501e | -21.11725 | -41.24612 | 2025-02-14 11:57:00 | TERRA_M-M | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 9.1 |
| 9eb59e5c-354c-37dc-9a7e-bd23372b2ba6 | -18.75507 | -40.14368 | 2025-02-14 11:57:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 7b22ce02-bbda-3d6f-804e-40d859d61491 | -19.06989 | -40.56881 | 2025-02-14 11:57:00 | TERRA_M-M | SÃO DOMINGOS DO NORTE | ESPÍRITO SANTO | Brasil | 3204658 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7814cfff-a04a-3504-b6cd-181d0ef404c2 | -18.93901 | -40.39685 | 2025-02-14 11:57:00 | TERRA_M-M | SÃO GABRIEL DA PALHA | ESPÍRITO SANTO | Brasil | 3204708 | 32 | 33 | nan | nan | nan | Mata Atlântica | 7.0 |
| 1c9a0383-e314-3dd4-bb98-80fe4e459264 | -12.05 | -45.12 | 2025-02-14 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 8b87b123-3a84-33a3-854f-b88ac61a23f1 | -12.05 | -45.07 | 2025-02-14 12:00:00 | MSG-03 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 92e49ccf-39a1-3041-bc9a-ec19eea4eccf | -32.2622 | -53.1572 | 2025-02-14 12:20:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 115.9 |
| 52048d53-2230-34e3-9001-c2ac86b81fd8 | -32.2622 | -53.1572 | 2025-02-14 12:30:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 148.1 |
| be911ae7-415f-32f3-8fe9-c3ecbe41dbb4 | -32.2622 | -53.1572 | 2025-02-14 12:40:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 127.0 |
| b76fc3c2-8479-3988-9c25-38f438347f93 | -32.2622 | -53.1572 | 2025-02-14 12:50:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 155.1 |
| 35c77560-cb80-39dd-bebe-4bd19729a244 | -32.2622 | -53.1572 | 2025-02-14 13:00:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 177.2 |
| 3bc2d23a-9b42-3d42-bbb7-7c892bb60e58 | -32.2861 | -53.1501 | 2025-02-14 13:10:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 130.2 |
| bf3abf5b-0475-300e-8048-191d11c039ef | -32.2622 | -53.1572 | 2025-02-14 13:10:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 131.9 |
| 8272ed38-7103-3587-9142-2ddf0c2eaacd | -32.2861 | -53.1501 | 2025-02-14 13:20:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 142.8 |
| c338a989-3a91-3298-87c9-374df23ecacc | -32.2622 | -53.1572 | 2025-02-14 13:20:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 142.0 |
| a5d47395-28f9-3564-bdc3-aee0cb7a03ae | -32.2622 | -53.1572 | 2025-02-14 13:30:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 165.0 |
| 2aa73b85-8b28-3be0-98d8-a04ed7eac9b4 | -32.2861 | -53.1501 | 2025-02-14 13:40:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 154.9 |
| 56e2f0fc-e5be-3e9d-b40d-80bf95d2d44a | -32.2852 | -53.1748 | 2025-02-14 13:40:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 114.4 |
| c1d0ae38-3947-3020-b89b-fe5a4f15f187 | -32.2622 | -53.1572 | 2025-02-14 13:40:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 144.1 |
| 9d56f07a-f52d-36e0-9acd-4ab3be965d18 | -32.2622 | -53.1572 | 2025-02-14 13:50:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 182.2 |
| d8b8e8eb-5fb4-3112-b0ea-c4b38c3ba23a | -32.2622 | -53.1572 | 2025-02-14 14:00:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 185.7 |
| d986447a-98cc-3b89-970d-da4fc173078f | -32.2622 | -53.1572 | 2025-02-14 14:10:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 154.8 |
| f72ab8d6-830c-3335-a2f6-5b3d5aef09ba | -32.2622 | -53.1572 | 2025-02-14 14:20:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 158.2 |
| 0a7c358e-0b76-342e-bf65-1df2fac45b9d | -32.2622 | -53.1572 | 2025-02-14 14:30:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 160.8 |
| df58051c-3201-38f2-b743-01ea7fa73366 | -32.2861 | -53.1501 | 2025-02-14 14:30:00 | GOES-16 | ARROIO GRANDE | RIO GRANDE DO SUL | Brasil | 4301305 | 43 | 33 | nan | nan | nan | Pampa | 107.2 |


