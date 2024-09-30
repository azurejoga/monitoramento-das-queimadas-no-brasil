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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a1fb5d20-8c32-33f1-b1b3-5527ec54158b | -11.05245 | -52.47653 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 010d1f45-7a8d-3137-a0d4-2c8a46bb5fdb | -11.05204 | -52.47981 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91728d76-a3a4-3e0f-9ccc-be35a9ff2c0e | -11.05175 | -52.43888 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 07b88e84-c40b-3a07-8553-c7d88d133917 | -11.05163 | -52.48308 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 91c6e1fe-915d-3a12-9613-0ab92f7c6110 | -11.05133 | -52.44225 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e0ddff2e-1087-3d3d-a224-72cd4675d1e2 | -11.05122 | -52.48634 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c61b27b5-5c82-3102-a1fe-43a80fd6af11 | -11.05091 | -52.4456 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4685f9d6-726d-3508-86bc-032d3c5d0eec | -11.05081 | -52.4896 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f45a4cb7-38de-3a32-b64c-80f540effc79 | -11.0505 | -52.44891 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 157fd95c-14cc-3ca0-9170-72f166220b2f | -11.05041 | -52.49286 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4ffa11f3-f1b7-3daf-b6bc-280e243b16c1 | -11.05009 | -52.45221 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9db3be48-ce60-3e30-b21f-6729e0719d49 | -11.04967 | -52.45558 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 457190d1-9378-3a80-833d-877614454c6a | -11.04924 | -52.45904 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c9a8666a-da4c-3819-8dd0-8834cd4d50af | -11.04882 | -52.46247 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0d347540-09f3-3567-a7bf-d43d489e63e9 | -11.0484 | -52.46581 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 11f84633-01b0-3e99-b2a0-a2633da8a266 | -11.048 | -52.46908 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| fe6fdfd9-7e7b-30e8-ad4c-e860c84ec420 | -11.04522 | -52.44808 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5a5e2432-2539-36b8-8d81-b90778db1501 | -11.04481 | -52.45138 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf538120-c596-3ce2-ad05-99b527cd505e | -11.06594 | -52.45468 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 0638dd69-5a61-3849-9cb9-300eb324db25 | -11.06552 | -52.45805 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 29.0 |
| 87749ba4-df14-3ab4-a2e5-d41bfaba219d | -11.0651 | -52.46141 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bbfda5e9-faad-359f-a467-57611f3118ad | -11.06468 | -52.46476 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 76592d49-f6bb-3209-a69f-a94c39878563 | -11.06447 | -52.42336 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 472ab058-82f5-38cd-9263-543841ba15aa | -11.06426 | -52.46809 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0e612262-b34b-37d6-b3fd-3c833056ded8 | -11.06404 | -52.42676 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8977d59b-1a35-397f-a324-986d743b2194 | -11.06384 | -52.47142 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f491acbf-8b8d-3e3a-aded-b8496a973251 | -11.06376 | -52.51474 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2c08fb-5956-382c-8375-7a8f631f5d9a | -11.06362 | -52.43016 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 00ab7f13-360d-3567-b9b8-6f61b2b07758 | -11.06342 | -52.47475 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 935af132-449c-35e4-b6a9-62d547015e03 | -11.06319 | -52.43359 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5fd460ba-f7c7-3835-9345-6ba6dce5cc61 | -11.063 | -52.47809 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 638ff290-5d76-371d-920b-33cefeee01bd | -11.06276 | -52.43703 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 28984a8a-dec5-3ea6-9093-40e2cd9a6b27 | -11.06259 | -52.48138 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 30e75d5c-cf72-3911-bf13-3beacee029e0 | -11.06234 | -52.44043 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2893782b-17de-3d62-8be5-b8508c93688c | -11.06218 | -52.48465 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 48b41935-2906-35b6-a881-4462076d5028 | -11.06191 | -52.44383 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 1f53610e-01a5-3f82-b11c-7f38f28eb0ee | -11.06177 | -52.4879 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5b6812c-e6e5-37c9-982e-1ef25e4d45fa | -11.06149 | -52.44722 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 9b48594d-205a-3793-b9f7-10240809cf44 | -11.06022 | -52.45734 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 331eda44-b67d-362c-86cd-ee5240494c7d | -11.0598 | -52.4607 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 1468acdd-9ab9-30fa-a78a-48dae482fae7 | -11.05938 | -52.46405 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 11.3 |
| 6256a5e6-a6ac-380e-8c3f-415f74cb348f | -11.05897 | -52.46738 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ddf2fec2-a192-36e0-ab40-0337754733ed | -11.05855 | -52.47071 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a7005fb1-94fe-32a1-bec7-8810318663ea | -11.05833 | -52.42936 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 036b0815-66b1-3bda-8f77-511d208ea095 | -11.05814 | -52.47403 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b30bc215-77fb-3e81-bfb8-5c449b48afa1 | -11.0579 | -52.43279 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a6277088-bffa-3244-858d-359ad2c8aed4 | -11.05772 | -52.47734 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 30a8ba08-abda-306c-a503-4c42eeda386d | -11.05747 | -52.43624 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 01ccd519-2f12-3793-8b4a-6b3248cf0fff | -11.05731 | -52.48063 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aa4aa2e4-deed-3a2d-9399-6c86b06fb13a | -11.05704 | -52.43966 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 4f6aea0c-5c81-33b7-9ec4-ca792d75495d | -11.0569 | -52.48391 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b97a777-650c-38d5-ba0c-b3845102ff05 | -11.05662 | -52.44305 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| dee872ce-93d0-3c74-88e0-bc5c6d958796 | -11.05649 | -52.48717 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d84b64ba-89e9-3b75-b3a1-95a6cc51cec7 | -11.0562 | -52.44642 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3214477f-f285-32dd-91ab-93d723899abd | -11.05608 | -52.49042 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ee5ac5b2-7991-3633-a67e-b3f99e04d2e1 | -11.05579 | -52.44974 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 45.9 |
| a9449f65-78ba-3360-a45c-b90c48d56ced | -11.05568 | -52.49366 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9c2e3a34-1bde-3412-8c2b-8470ab7c7af4 | -11.05537 | -52.45305 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 96d86683-db59-39ee-b24c-0062f333fe0c | -11.05495 | -52.45643 | 2024-09-30 05:23:00 | NOAA-21 | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 110.5 |
| 86fdb570-ce12-33ce-862b-45a3875be926 | -2.20199 | -52.05206 | 2024-09-30 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 555776b6-74bb-3cc5-8746-266f4044e290 | -0.79677 | -52.48431 | 2024-09-30 05:23:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3802644a-5ecf-3686-9388-ced3bd862a2d | -0.79405 | -52.48207 | 2024-09-30 05:23:00 | NOAA-21 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2906216-12b8-3b6c-a660-bb106a742781 | -2.85659 | -53.32654 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b84a4976-9899-3bc2-a791-b718d16219c4 | -2.85345 | -53.31724 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9503c390-d6e5-3703-a580-8b3222a83801 | -2.85281 | -53.32157 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ee77d2e-6e77-3eb7-80cb-06bee2df29cd | -2.85217 | -53.32589 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b391bece-74d1-30ef-a913-bb24c8b6d9e6 | -2.75844 | -53.22864 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2b449b01-a0ca-3ba3-9561-caa269bf9551 | -2.7578 | -53.23292 | 2024-09-30 05:23:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 09178a76-1dcd-3a3d-947c-d0d3454735a9 | -2.68409 | -52.43414 | 2024-09-30 05:23:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f0dee160-cb33-311e-a6d4-e4ee3192c3b0 | -11.21604 | -54.7605 | 2024-09-30 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 84abf13c-bc39-3925-9199-1a6dd5a02408 | -11.21541 | -54.76516 | 2024-09-30 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| a0896a49-8d83-3f1f-aa6d-f891100867c6 | -11.21479 | -54.76978 | 2024-09-30 05:23:00 | NOAA-21 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 76b3b55b-20bf-3846-8934-5e206813adf5 | -2.14733 | -53.67195 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b4475005-cb22-3f1f-9fe3-493af595c2a0 | -2.14486 | -53.65929 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 625d5834-e4c3-353b-8591-3d0048f61b6a | -2.14427 | -53.66328 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| df0d2318-292d-3129-83b4-4c93cf699e91 | -2.14308 | -53.67123 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e7a79c4-2e73-3d31-9dc3-7a25efbb89b3 | -2.14061 | -53.65852 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6d16f0be-386d-3ba1-bad0-d338450c5663 | -2.14002 | -53.66251 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cc4d2499-fb73-3abc-afa0-6ef1fffc9eca | -2.13934 | -53.6437 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| af4abefc-c3a8-3862-80df-908a577d2318 | -2.13875 | -53.64173 | 2024-09-30 05:23:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1345c7d5-8f55-3025-bdc4-bedd2b4ed050 | -1.29647 | -54.55295 | 2024-09-30 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2aaa0145-6c9e-3fcf-9679-81cf31ad21fe | -1.0832 | -54.12598 | 2024-09-30 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 04d74399-c981-353f-8efe-cef81c17bc29 | -1.08301 | -54.12659 | 2024-09-30 05:23:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc37f969-7ace-3e81-b1ef-2f883be47d68 | -2.97115 | -54.73398 | 2024-09-30 05:23:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 23c7752d-7802-32e5-afa4-2eb72b0460b6 | -2.94656 | -54.0888 | 2024-09-30 05:23:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bec49aa5-24f4-3e6f-a656-918cdaf35c08 | -1.42599 | -55.34332 | 2024-09-30 05:23:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| acf4d34b-04be-36e5-9ce9-845ef1900ba6 | -1.41515 | -55.49314 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c60ac1c-83ef-382c-953b-f27062a10653 | -1.41428 | -55.49105 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf5b188d-0ba6-30d0-9517-8d3eb14c2c4b | -1.41357 | -55.49556 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c478f89a-4e73-3e50-8db3-b0e1953d3a78 | -1.36108 | -55.68365 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b36e32be-13ff-380b-b6be-4cccd8d14bc1 | -1.36039 | -55.68805 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4579a6e0-62d7-3f80-b6da-385de3776302 | -1.35668 | -55.68747 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1abf10ac-5b5f-3c78-9934-c9e32ddb313b | -1.3218 | -55.83834 | 2024-09-30 05:23:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 15490850-7fcf-31f9-9a99-a299f5d82d21 | -1.23977 | -55.88404 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b9ba056-4266-3124-b270-7a2f14be6555 | -1.23611 | -55.88347 | 2024-09-30 05:23:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b71edddc-da89-3a88-accb-9172f96794b3 | -9.26318 | -57.05445 | 2024-09-30 05:23:00 | NOAA-21 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c05d7ef2-3b61-34c9-8874-0bfa3b0f78a7 | -9.90044 | -57.06106 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f950da0c-02b5-3b12-afdf-733ad4fa6da1 | -9.89976 | -57.06581 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b946dd41-2264-30de-aba2-21c51ddbaa40 | -9.8966 | -57.06055 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fa2f7f67-47df-392e-91a3-40788770b773 | -9.67494 | -56.95919 | 2024-09-30 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
