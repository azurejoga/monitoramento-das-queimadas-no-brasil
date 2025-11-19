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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 39c1b9a1-d588-390b-85d2-440e2ed3a96d | -3.55709 | -43.4724 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3b47ac61-9c36-3816-8d69-c651056a962d | -4.91906 | -48.17025 | 2025-11-19 04:50:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d7ecc6d8-d878-317c-ab6b-8651ea0b023a | -1.34826 | -54.61361 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ed0a9616-7925-348b-a256-b2bd75a70b04 | -4.69355 | -45.8883 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6378d665-416b-3f79-8b8a-cbe3e28f2669 | -2.28163 | -51.93502 | 2025-11-19 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b624373a-04a3-375b-9d67-318bff560183 | -3.28514 | -44.88182 | 2025-11-19 04:50:00 | NOAA-20 | CAJARI | MARANHÃO | Brasil | 2102507 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5e57e167-5823-38a7-8fd0-1f757f9a3041 | -3.6773 | -50.16669 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7c5fdb0d-f035-3c65-af8d-6d4e9e2a0b08 | -5.04983 | -45.91006 | 2025-11-19 04:50:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a51f79c5-b671-3ef9-95fb-25b37482d2f2 | -1.43643 | -52.68015 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c674f727-4c21-3b4a-8264-8f09bd6f00f1 | -2.22137 | -44.81548 | 2025-11-19 04:50:00 | NOAA-20 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 11.2 |
| e06635cf-d169-355e-ab11-db1b2a4c5bb9 | -0.72313 | -52.37776 | 2025-11-19 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| aae392b5-410f-32be-aec4-d7a5ddf31b18 | -3.01964 | -44.46814 | 2025-11-19 04:50:00 | NOAA-20 | BACABEIRA | MARANHÃO | Brasil | 2101251 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18477802-6181-36cc-ba99-b8d635376ada | -3.17702 | -48.61679 | 2025-11-19 04:50:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f8227941-f53d-3782-b50f-63b3472cde15 | -0.76912 | -52.49283 | 2025-11-19 04:50:00 | NOAA-20 | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1464c83d-3188-3b20-8ea2-b23d6f4f8315 | -2.87681 | -52.61927 | 2025-11-19 04:50:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| debf329c-00ed-39f5-8728-a5ec2c2c191b | -2.28493 | -51.93553 | 2025-11-19 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| edb89ece-9ef9-324b-93ce-147205cc2eaf | -2.91138 | -49.08825 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7488be1c-a458-34dd-846b-f913a345ed66 | -3.68071 | -50.16722 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 0b4e6195-56ab-3217-bb98-9a9227b7641a | -4.91836 | -48.17494 | 2025-11-19 04:50:00 | NOAA-20 | VILA NOVA DOS MARTÍRIOS | MARANHÃO | Brasil | 2112852 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0bcc47d8-bf98-3c67-8505-399b32571928 | 0.91474 | -51.105 | 2025-11-19 04:50:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 551d718b-ea84-3ae9-a08b-4ba18a29a376 | -2.36496 | -52.15946 | 2025-11-19 04:50:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3b587be1-4230-376d-84ab-9796039fbba6 | -2.85588 | -49.61214 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 004c02a4-5fd1-3817-8679-cd0f51206316 | -4.48351 | -44.33529 | 2025-11-19 04:50:00 | NOAA-20 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a921f1b-9aae-35af-9967-537ae9f1fccf | -3.68129 | -50.16352 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c8bd66b-32df-3e58-b627-ddd5d9aa9eef | -2.5253 | -58.03084 | 2025-11-19 04:50:00 | NOAA-20 | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2fabe59e-be16-3e0b-a8bb-1360a78abd94 | -3.79961 | -50.0333 | 2025-11-19 04:50:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 83ecfd58-bec9-3089-bb92-ac2cfbcd4a4e | -3.36967 | -49.26043 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9dbb2ce2-b89d-35e0-9584-43eb7bf476e3 | -3.23351 | -48.51928 | 2025-11-19 04:50:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f21f17c2-c536-33a4-af13-8ddbf429413d | -1.38235 | -45.79624 | 2025-11-19 04:50:00 | NOAA-20 | GODOFREDO VIANA | MARANHÃO | Brasil | 2104305 | 21 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 296cecf7-dedf-3823-932f-79a1ea90d00d | -2.22065 | -44.82014 | 2025-11-19 04:50:00 | NOAA-20 | CENTRAL DO MARANHÃO | MARANHÃO | Brasil | 2103125 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ea8e1c0-afa1-37b9-886e-b574e05c9b76 | -3.0747 | -49.10843 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| ddc174f0-aeab-376d-86c9-15922027b316 | -1.35185 | -54.61422 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f86b17c-07ac-359d-8a50-4b3ca73b05c9 | -2.95283 | -49.57206 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6e6bcdb0-a2c9-39f4-bbe7-71f5b0804408 | -1.14679 | -54.10314 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d0b91ace-f9b7-3bcf-853f-b793683baa6e | -1.48647 | -54.19892 | 2025-11-19 04:50:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| fb7a6093-f203-3bd5-98aa-f2d3e276484a | -2.70084 | -49.30291 | 2025-11-19 04:50:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1758c572-1d02-36f5-a341-aaca82a9675b | -2.69087 | -59.42721 | 2025-11-19 04:50:00 | NOAA-20 | RIO PRETO DA EVA | AMAZONAS | Brasil | 1303569 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6eb5d940-bc1a-3043-af25-b356ec6d99a7 | -2.28591 | -46.52845 | 2025-11-19 04:50:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 03fbb23c-faf9-3136-a081-86e569ce9075 | -3.902 | -47.93967 | 2025-11-19 04:50:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ee7e0c60-c0ac-3639-9560-f96db6351075 | -3.4353 | -52.88959 | 2025-11-19 04:50:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e19ffdc-60ca-3fe8-b223-0b262c6ffc80 | -3.5542 | -43.47351 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5b3caa71-dc88-34ec-a5a3-71a7c3ce0d22 | -3.36995 | -57.24043 | 2025-11-19 04:50:00 | NOAA-20 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| defde0ae-3e59-3081-bb54-7630bbfca646 | -0.99199 | -52.43752 | 2025-11-19 04:50:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 89015c90-7bc7-3efc-86f5-c6cac2683edd | -3.56221 | -43.47321 | 2025-11-19 04:50:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1f9aca32-aa58-36cb-a1e3-a75a6aaf2504 | -2.85933 | -49.61268 | 2025-11-19 04:50:00 | NOAA-20 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7118ec7d-c60d-38ad-8f0a-c5b9273bb48f | -10.05477 | -54.34405 | 2025-11-19 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0aeffc3a-6402-3bf1-8afd-353c7670f279 | -7.83353 | -42.16257 | 2025-11-19 04:53:00 | NOAA-20 | SIMPLÍCIO MENDES | PIAUÍ | Brasil | 2210805 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 612b4559-6c9d-3c1b-a5a2-4a7f7749976c | -10.04869 | -54.33942 | 2025-11-19 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0d411d1f-3acd-3cd3-9ae4-4279e5f916c0 | -7.73707 | -47.25388 | 2025-11-19 04:53:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 36cc77f0-ca6b-3291-8d68-93f34cdad8d4 | -10.06455 | -47.91175 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d9388720-b484-32be-ad45-9eff7ca0820f | -11.62017 | -43.90814 | 2025-11-19 04:53:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a61f9ff5-b78a-393c-88be-9ba2ef7bc9e3 | -16.04179 | -59.1577 | 2025-11-19 04:53:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a16c8a4c-1ace-3ac8-a911-aab684a86d59 | -10.3967 | -54.98413 | 2025-11-19 04:53:00 | NOAA-20 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f8713c04-4e76-33bf-8b7d-1b1d336b9b43 | -11.21903 | -49.7194 | 2025-11-19 04:53:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db880e89-48b9-3b72-8572-a089d724bcdf | -8.38556 | -44.06271 | 2025-11-19 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1c6f14a0-eab4-3f53-9c08-ff08fb6c2bd1 | -7.27849 | -47.90697 | 2025-11-19 04:53:00 | NOAA-20 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 0f3e5df3-2dad-3fff-b5a7-63d4bd90dc68 | -14.79974 | -52.79045 | 2025-11-19 04:53:00 | NOAA-20 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ae7a1b8c-6418-391b-a991-28e7877edfb3 | -8.39166 | -44.06256 | 2025-11-19 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 62e76f58-6196-30a8-8612-5f5070990fbe | -11.27951 | -48.86934 | 2025-11-19 04:53:00 | NOAA-20 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4b9c87ad-e6f6-3da0-a045-47f5001adcd0 | -5.23107 | -49.57581 | 2025-11-19 04:53:00 | NOAA-20 | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a10c8d3c-4c62-3d3f-8c7b-723709c5a3a5 | -5.33712 | -50.89192 | 2025-11-19 04:53:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 24d1b011-6dd3-3227-82eb-38d74de8e355 | -10.03087 | -53.74994 | 2025-11-19 04:53:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03e01777-b78a-3d14-97df-85f50b0e9633 | -10.37029 | -49.88977 | 2025-11-19 04:53:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b13f368-7b81-355b-8dbc-ea3ea9c3dc89 | -10.77717 | -48.83567 | 2025-11-19 04:53:00 | NOAA-20 | FÁTIMA | TOCANTINS | Brasil | 1707553 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 579c9633-e07b-3e68-ad70-6c8b4c89fc69 | -10.03429 | -49.20953 | 2025-11-19 04:53:00 | NOAA-20 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1bbfa243-454b-3e21-a6c3-d6f175d46510 | -9.37729 | -48.42037 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d5a4c43e-7715-36a5-b4d2-d6e957d8ad55 | -10.82385 | -48.03053 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2fb8eedb-03e4-39ac-afae-613ffced5454 | -8.38637 | -44.06182 | 2025-11-19 04:53:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ba6d392c-ffc5-3b1d-b20b-7472bf9a0f6c | -9.69836 | -48.2984 | 2025-11-19 04:53:00 | NOAA-20 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 09005753-ec31-3b5c-b84e-9716d5f9c531 | -11.01234 | -49.04057 | 2025-11-19 04:53:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b1377773-d955-32c6-881f-0fd404506f8f | -10.53819 | -53.721 | 2025-11-19 04:53:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 9eb8fdd9-bd84-3783-918d-e643e462915c | -10.66321 | -49.37332 | 2025-11-19 04:53:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8df0a20f-1372-32ca-8da4-84ae77e3a614 | -6.34016 | -44.22932 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| f662a4e0-2fde-3973-83ea-2337691b87db | -10.09813 | -47.88498 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c42ec989-1908-395a-a11f-e96373a63de1 | -9.37678 | -48.42382 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| a484215e-998f-306a-8299-4cbb18fd84c3 | -9.3944 | -50.68306 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce917217-6f6f-349a-9e0b-3271e9f9470f | -11.84572 | -49.2284 | 2025-11-19 04:53:00 | NOAA-20 | CARIRI DO TOCANTINS | TOCANTINS | Brasil | 1703867 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| e7315ca4-6a46-3457-bb44-8e57949ceaf7 | -9.38323 | -48.43541 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 5a5a7212-3e42-3b4d-b133-b95752f7a9ea | -9.3733 | -48.41977 | 2025-11-19 04:53:00 | NOAA-20 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| ef0efde6-a6dc-30e9-8700-4afc4adbc448 | -5.38009 | -50.48323 | 2025-11-19 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15915a13-6c6b-35e7-9e87-bcf913e4d147 | -10.30164 | -57.14138 | 2025-11-19 04:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cc47ede2-eaf3-3c04-ac23-0e1ea173b1de | -8.21785 | -50.4789 | 2025-11-19 04:53:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d5e9fb40-3bfc-3e90-9a43-769138bc0b61 | -10.77312 | -48.12011 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d5448ca4-b211-3dab-a769-01c60414c7c4 | -15.54149 | -54.34496 | 2025-11-19 04:53:00 | NOAA-20 | PRIMAVERA DO LESTE | MATO GROSSO | Brasil | 5107040 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d5c888a1-cee8-3744-8921-14a5aab49711 | -10.7677 | -48.03621 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| b6e98c6e-c5a2-3e7c-b98f-b03f7f72cabf | -10.9247 | -48.66917 | 2025-11-19 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b7f896c3-6f50-3b76-8223-b404d1f156ca | -10.2987 | -57.13633 | 2025-11-19 04:53:00 | NOAA-20 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 98f930d8-dc2f-3971-aa5e-f16c1c4e4fa1 | -10.06092 | -47.90733 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dce8b5f4-3feb-3c2a-85f3-bfa1ad1bfc40 | -10.05088 | -54.34705 | 2025-11-19 04:53:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8775a486-95c2-34c0-8fbf-5823078fd20a | -14.92512 | -59.90514 | 2025-11-19 04:53:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f8a339e7-0caf-34ad-b51b-4b6c61960b95 | -10.09757 | -47.8889 | 2025-11-19 04:53:00 | NOAA-20 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b6bfdfb6-12dd-305b-aa36-ef134f1052aa | -5.38351 | -50.48377 | 2025-11-19 04:53:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9c077eab-e9c4-3d40-8d37-faef50c17443 | -11.66755 | -47.97743 | 2025-11-19 04:53:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 05c88281-6b70-3ec9-8301-0726bdcb04fb | -11.27553 | -48.50587 | 2025-11-19 04:53:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e53ca6b7-a299-3c60-b5c2-32fbb97a5dd9 | -7.6201 | -46.55431 | 2025-11-19 04:53:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e409cbad-1da5-3335-901b-20b83c8d60ac | -6.34234 | -44.22569 | 2025-11-19 04:53:00 | NOAA-20 | SUCUPIRA DO NORTE | MARANHÃO | Brasil | 2111904 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 61d8fc86-96d2-3fc7-b56d-14aecdcfbc8e | -10.7967 | -47.98036 | 2025-11-19 04:53:00 | NOAA-20 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 8deaaaff-4911-3a69-801b-ad3880e54e10 | -7.79563 | -49.618 | 2025-11-19 04:53:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b947daeb-8c4f-342f-bcd8-398eda9d9727 | -9.39562 | -50.67853 | 2025-11-19 04:53:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 787970b1-0dbf-390b-bbf9-048cebf888e1 | -18.15944 | -54.55585 | 2025-11-19 04:53:00 | NOAA-20 | PEDRO GOMES | MATO GROSSO DO SUL | Brasil | 5006408 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README19.md)
