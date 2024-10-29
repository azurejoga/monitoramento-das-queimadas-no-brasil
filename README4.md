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
| 80a72759-37bf-3e1e-bcb6-2840477b383d | -10.5024 | -44.156399 | 2024-10-29 00:26:25 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 832578a7-cd50-3652-a356-21323def5b43 | -10.504 | -44.163799 | 2024-10-29 00:26:25 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 40109813-6870-346f-885c-9c23bc69035e | -11.253 | -47.891201 | 2024-10-29 00:26:26 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93456df4-e06b-3505-a5d0-a0ced14199a3 | -11.2555 | -47.903 | 2024-10-29 00:26:26 | METOP-C | SANTA ROSA DO TOCANTINS | TOCANTINS | Brasil | 1718907 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 0d2e7dbc-764d-3b3b-a6f1-e0539657ff0c | -10.3652 | -44.047901 | 2024-10-29 00:26:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f07f7e8c-0bc3-31f8-a454-12731e19bc04 | -10.3668 | -44.055302 | 2024-10-29 00:26:27 | METOP-C | JÚLIO BORGES | PIAUÍ | Brasil | 2205524 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 20abac70-a0ff-3d68-8a4c-811085b09e1f | -10.4938 | -44.5835 | 2024-10-29 00:26:27 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f3ae79ba-1898-3dfb-8ccc-e0cce3ebc3af | -10.4955 | -44.591099 | 2024-10-29 00:26:27 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 54934a9b-d3f9-32f5-8a91-15162adf8f4b | -10.4972 | -44.598701 | 2024-10-29 00:26:27 | METOP-C | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 1ed844d3-0b48-3c85-8734-a8a9da785210 | -10.5284 | -44.834801 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| fdf38d06-9e1e-38a1-bdce-e8410bebc020 | -10.5301 | -44.842602 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3b92d804-e559-39a3-85f2-972d7933e1d4 | -10.5318 | -44.850399 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0f79817c-fc9d-36bf-8843-ebd0253f9d3f | -10.5186 | -44.836899 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 934378f8-a374-3402-af5c-43d59c1f456b | -10.5203 | -44.8447 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bffaf38a-8373-3418-81fd-cb1a96112d30 | -10.522 | -44.852501 | 2024-10-29 00:26:27 | METOP-C | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e2e59aa0-f248-39e2-8995-37e8e8659796 | -12.0924 | -52.4548 | 2024-10-29 00:26:27 | METOP-C | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a7c30488-4036-3500-a09f-e9b5c80cf349 | -9.4751 | -40.373001 | 2024-10-29 00:26:28 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 0b0b720d-6886-3d49-880a-5f6649ac519a | -9.4769 | -40.3806 | 2024-10-29 00:26:28 | METOP-C | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| f2f18564-810f-3a59-b013-6ccd1f21f5a4 | -10.5516 | -45.128502 | 2024-10-29 00:26:28 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0aaf47de-4273-38ea-90e2-8ebbf437cfae | -10.5533 | -45.1366 | 2024-10-29 00:26:28 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bc631f37-6494-3877-bb35-643e66797baf | -10.5551 | -45.1446 | 2024-10-29 00:26:28 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 5df88b0c-4e69-3675-af13-738efda3e89f | -10.4569 | -44.883301 | 2024-10-29 00:26:29 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6d558686-8c8b-31f0-ae84-3ec1fed11672 | -10.4586 | -44.891102 | 2024-10-29 00:26:29 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 2611fb7b-666d-3aa3-b987-6fa51613b5bc | -10.4603 | -44.898899 | 2024-10-29 00:26:29 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 020a18bb-ffc6-3989-8890-c6a203c3828e | -10.1529 | -44.0187 | 2024-10-29 00:26:30 | METOP-C | AVELINO LOPES | PIAUÍ | Brasil | 2201101 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| bd1d660d-af00-3f52-af34-cd081656ebe5 | -9.3975 | -40.792301 | 2024-10-29 00:26:31 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| b8c7a07c-8080-3958-9435-0d1d3b5ee0ab | -9.3859 | -40.787201 | 2024-10-29 00:26:31 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 045c22fe-9ff6-357c-b7e2-fb5cc644b46c | -9.3877 | -40.794601 | 2024-10-29 00:26:31 | METOP-C | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 37d66f39-f17b-3b47-8c4f-62da742e0629 | -10.3675 | -45.084999 | 2024-10-29 00:26:31 | METOP-C | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 534d544f-d045-311f-a697-306bded57767 | -9.9719 | -43.944901 | 2024-10-29 00:26:33 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 7f755b47-b48f-326e-a227-dad4ff39b274 | -9.87 | -44.319901 | 2024-10-29 00:26:36 | METOP-C | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 87144295-62ff-361b-9425-a6c11921aec8 | -10.0987 | -45.405701 | 2024-10-29 00:26:36 | METOP-C | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f0b1b4b3-b301-3132-9656-adffaf182912 | -9.5361 | -43.013401 | 2024-10-29 00:26:37 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 8ecb486b-bbdb-3d34-a1c7-9cd72caaf79b | -9.5377 | -43.020302 | 2024-10-29 00:26:37 | METOP-C | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| fa9daca8-5c7f-3e08-98c8-9659915c02a7 | -9.7271 | -43.908798 | 2024-10-29 00:26:37 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6ae79729-b5bd-32ad-ba03-adea2002a487 | -9.7287 | -43.916 | 2024-10-29 00:26:37 | METOP-C | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9247b822-4d65-36a3-99cf-b0f8e4d6fa2f | -7.5673 | -35.137901 | 2024-10-29 00:26:38 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 0f534f34-1cf9-32b4-949c-8fa4829baf3a | -7.5713 | -35.154099 | 2024-10-29 00:26:38 | METOP-C | ALIANÇA | PERNAMBUCO | Brasil | 2600708 | 26 | 33 | nan | nan | nan | Mata Atlântica | nan |
| defed4b0-23dc-381f-92ed-77c68437b9ef | -8.538 | -39.377998 | 2024-10-29 00:26:39 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2d4f90e8-23d3-3fa6-b3b3-cc0d0c8d07f7 | -8.54 | -39.386501 | 2024-10-29 00:26:39 | METOP-C | CURAÇÁ | BAHIA | Brasil | 2909901 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 784676bd-55b5-3155-85e0-d568b2b1362b | -8.5302 | -39.388901 | 2024-10-29 00:26:39 | METOP-C | CABROBÓ | PERNAMBUCO | Brasil | 2603009 | 26 | 33 | nan | nan | nan | Caatinga | nan |
| 9586f47e-1b23-37a6-8870-8ac0f81d332e | -10.4501 | -49.029701 | 2024-10-29 00:26:43 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ff41e57-ee1e-34a5-bab3-5f3f5e2068b7 | -10.4529 | -49.043301 | 2024-10-29 00:26:43 | METOP-C | NOVA ROSALÂNDIA | TOCANTINS | Brasil | 1715002 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9ef0618b-ad14-3810-91a8-5fc9dff4b163 | -9.122 | -43.187099 | 2024-10-29 00:26:44 | METOP-C | JUREMA | PIAUÍ | Brasil | 2205532 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 2e6ab53a-0b70-34ac-a4d5-a93d72a26899 | -9.1298 | -44.4146 | 2024-10-29 00:26:48 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d6593067-e943-3347-8c03-3e834b3ebce9 | -9.1314 | -44.421902 | 2024-10-29 00:26:48 | METOP-C | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| f90fa250-d2e0-390c-89a2-ce416609cf46 | -7.5715 | -38.746201 | 2024-10-29 00:26:52 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 2de25689-c31e-3654-870a-6efba9436e18 | -7.5738 | -38.7556 | 2024-10-29 00:26:52 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 16d90ee1-41c4-38b9-8c25-5c1a55544b51 | -7.5618 | -38.748501 | 2024-10-29 00:26:53 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 993af9d4-e99c-3adb-be0c-1d080298e2ff | -7.5641 | -38.757999 | 2024-10-29 00:26:53 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 7652e5bd-bada-37f5-970b-7ca8300a4e28 | -7.552 | -38.7509 | 2024-10-29 00:26:53 | METOP-C | MAURITI | CEARÁ | Brasil | 2308104 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| f944c75a-f0b0-3a3f-b7ec-6f1688c65fb9 | -8.7308 | -44.011101 | 2024-10-29 00:26:53 | METOP-C | CRISTINO CASTRO | PIAUÍ | Brasil | 2203107 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| afc05a75-1472-3d4d-bd90-e3f338f98297 | -8.7624 | -44.705101 | 2024-10-29 00:26:55 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c0d0ad7e-966f-329f-84f4-dc135eee1292 | -8.7641 | -44.712502 | 2024-10-29 00:26:55 | METOP-C | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 18d7f5ec-0b1b-32ec-a916-9cd012e6cb89 | -8.5673 | -43.787899 | 2024-10-29 00:26:55 | METOP-C | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| c4f723d7-57f0-38fc-b1ee-5a735b037415 | -9.8722 | -49.678299 | 2024-10-29 00:26:55 | METOP-C | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2b3bcaa7-2144-3004-9b08-770afe4f57e2 | -8.3792 | -43.638901 | 2024-10-29 00:26:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 355fa766-7c45-3b92-9ac0-11c21e77112d | -8.3807 | -43.645802 | 2024-10-29 00:26:58 | METOP-C | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 0c9246c3-0ddd-369c-832e-18be02fee225 | -8.5334 | -44.6007 | 2024-10-29 00:26:59 | METOP-C | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 88ed9edc-f3cf-3781-a862-47549862e163 | -6.6829 | -37.454102 | 2024-10-29 00:27:02 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| f19ac0cd-2bf4-3356-bcef-24c119d7b528 | -6.6857 | -37.465801 | 2024-10-29 00:27:02 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| b9bcb6b7-a924-3002-922c-2d39124945ae | -6.6731 | -37.456501 | 2024-10-29 00:27:02 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| 98b06108-06e5-3a47-bcfd-fe9026f7ad55 | -6.6759 | -37.468201 | 2024-10-29 00:27:02 | METOP-C | SERRA NEGRA DO NORTE | RIO GRANDE DO NORTE | Brasil | 2413409 | 24 | 33 | nan | nan | nan | Caatinga | nan |
| c2dc246a-a230-3dd8-acde-a6a97e1d7195 | -7.1112 | -39.5881 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0a0d2a0f-5c36-3672-8fad-a23fc29c15de | -7.1148 | -39.559898 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 65014d78-3b8c-318a-9bac-f6016fbf5eea | -7.1169 | -39.568501 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| d8431acb-f697-368b-ac63-93d113986ff9 | -7.105 | -39.562199 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 97ab5076-c75e-3502-ac51-5ed5fe02110c | -7.1071 | -39.570801 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 0ef2df6a-d1d9-370c-a5fc-7e3451d47768 | -7.1091 | -39.579498 | 2024-10-29 00:27:03 | METOP-C | CRATO | CEARÁ | Brasil | 2304202 | 23 | 33 | nan | nan | nan | Caatinga | nan |
| 84496d5c-d68f-36c0-aa64-6447c4f63197 | -7.893 | -42.950199 | 2024-10-29 00:27:03 | METOP-C | PAJEÚ DO PIAUÍ | PIAUÍ | Brasil | 2207355 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 5d41bd07-3027-34c5-85bc-6124cb06c16e | -7.8832 | -42.9524 | 2024-10-29 00:27:03 | METOP-C | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b2dbb6e2-f056-3913-9598-ef0322041fd0 | -7.8619 | -43.130501 | 2024-10-29 00:27:04 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| cfe0f80b-edd8-39c9-8f47-6b5cc4ea4f2f | -8.2576 | -44.84 | 2024-10-29 00:27:04 | METOP-C | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 70708890-2093-346a-8002-1ffcfacd25e9 | -8.2592 | -44.8475 | 2024-10-29 00:27:04 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| b4417e18-2693-3f97-96a0-177a0149ee70 | -8.2609 | -44.8549 | 2024-10-29 00:27:04 | METOP-C | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 832d7dd3-fa5f-3de1-81a2-4f764112bd5a | -7.8093 | -43.1712 | 2024-10-29 00:27:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 45aa3133-02c4-3aa3-89d0-d4a1334a839c | -7.8109 | -43.178101 | 2024-10-29 00:27:05 | METOP-C | RIO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2209005 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 611a4dde-b0ab-3c57-a063-8478a2119faa | -7.343 | -41.857899 | 2024-10-29 00:27:08 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| ffc3de85-efbc-372a-9fa9-b095ba2abc7f | -7.3446 | -41.865002 | 2024-10-29 00:27:08 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| fcbbd562-e60e-3fed-8f2b-6f5b183156ee | -7.3463 | -41.872101 | 2024-10-29 00:27:08 | METOP-C | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| f1c9c4ec-ac63-3d2d-b720-c9be198b13aa | -8.2421 | -45.836399 | 2024-10-29 00:27:08 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 2880d0e4-13d9-3d5c-9766-e097d6e20578 | -8.2439 | -45.844501 | 2024-10-29 00:27:08 | METOP-C | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b701a5f2-f3e1-3806-985a-08004793a2e0 | -7.6221 | -43.662601 | 2024-10-29 00:27:10 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 95ebf3e7-5d5b-3213-8704-c33e88e91315 | -7.0151 | -41.290199 | 2024-10-29 00:27:11 | METOP-C | SANTO ANTÔNIO DE LISBOA | PIAUÍ | Brasil | 2209401 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 0324a65c-8776-3c84-9b20-8cdd6813e032 | -7.0006 | -41.316601 | 2024-10-29 00:27:11 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 65d75da2-c950-381f-a97f-79f757a4b763 | -7.0024 | -41.323898 | 2024-10-29 00:27:11 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 420dcc0a-50bd-3bca-b1fd-30d11264e817 | -7.0041 | -41.3312 | 2024-10-29 00:27:11 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 6982a35b-4e92-373c-a4cf-6c1ad1ebe986 | -7.0058 | -41.338501 | 2024-10-29 00:27:11 | METOP-C | SUSSUAPARA | PIAUÍ | Brasil | 2210938 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b8b242a7-fb0d-361d-ba39-558a40fdedfa | -8.474 | -47.7929 | 2024-10-29 00:27:11 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 19216feb-78c1-364a-85d4-2ec2c2626738 | -8.4762 | -47.803398 | 2024-10-29 00:27:11 | METOP-C | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 2ced7708-736e-37d0-b96b-f50aadb75fa9 | -6.9926 | -41.326199 | 2024-10-29 00:27:12 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| e38953f4-8036-36be-ab07-a34481e488a5 | -6.9943 | -41.3335 | 2024-10-29 00:27:12 | METOP-C | BOCAINA | PIAUÍ | Brasil | 2201804 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 8ab3d853-c426-3316-aed7-911eb0b25028 | -7.2796 | -42.5686 | 2024-10-29 00:27:12 | METOP-C | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| d41ae8aa-ccde-3efc-b615-75a685f3fe9a | -7.9244 | -45.422798 | 2024-10-29 00:27:12 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 69dc4f8f-25f5-31b0-bcaa-8950cba56fb1 | -7.9262 | -45.430599 | 2024-10-29 00:27:12 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 28bdb769-6922-3aef-b94b-ad375a6b48e0 | -7.8749 | -45.384998 | 2024-10-29 00:27:12 | METOP-C | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 243ffc72-91f5-356e-9cf3-52c6e132ae16 | -7.3357 | -43.581699 | 2024-10-29 00:27:14 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| b1c419b9-7d4e-355e-a033-bf861dde04a8 | -7.3424 | -43.565701 | 2024-10-29 00:27:14 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 34b7109f-9be0-3432-a9f2-747e4aae70fc | -7.3439 | -43.572601 | 2024-10-29 00:27:14 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 4ff5dd27-229d-3a95-8bf2-3fcb7fa5e780 | -7.3455 | -43.579498 | 2024-10-29 00:27:14 | METOP-C | CANAVIEIRA | PIAUÍ | Brasil | 2202251 | 22 | 33 | nan | nan | nan | Caatinga | nan |


[Clique aqui para ver as próximas entradas](README5.md)
