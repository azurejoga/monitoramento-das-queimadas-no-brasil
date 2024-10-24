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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 16fdb3f2-d897-3ac1-81ed-27843aeb719a | -3.79217 | -52.38817 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c1832cf1-2b91-38a0-ad3e-6d455d0e6341 | -3.78864 | -52.40998 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| eba79d19-0bdd-37ea-8635-a38868a198ba | -3.78811 | -52.38756 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| fbc18c81-b7d9-38f9-834d-5c3967aea35f | -3.78754 | -52.39107 | 2024-10-24 04:32:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 963b60fe-ddaa-3d7c-8d63-7505281a0e3d | -3.75808 | -52.2921 | 2024-10-24 04:32:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ddbbe0d-7d2b-38cf-9477-8ff9a919bdd7 | -3.67557 | -52.68897 | 2024-10-24 04:32:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 963b8fe7-a326-31c3-9745-eb1fd426b777 | -1.90663 | -54.58667 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4e01a0e0-9b7f-3a1f-ae82-f20c93f7d7db | -1.66179 | -53.68305 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7acc6c82-5e4d-3676-bc03-176b1566e77a | -1.60958 | -54.77521 | 2024-10-24 04:32:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 82d74368-9dd4-3f31-80a8-be2d90b89d46 | -1.5511 | -53.69752 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ee232e47-1735-336e-9a1c-8d8e5d7f20f4 | -1.55038 | -53.70214 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6081929-def8-3284-a718-2dd17b6d00a8 | -1.55038 | -53.70126 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca1aa33b-62b1-3292-87e2-78a648066633 | -1.54581 | -53.70128 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d3009a6e-00d2-36b2-9fe2-2ed0ba98e444 | -1.54581 | -53.70043 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2695034b-8f2e-392a-84f4-e4a0d3d30dd8 | -1.54124 | -53.69962 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12ad525a-c8da-3a56-a8a9-2e04d369827b | -1.54122 | -53.70049 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c7358182-189a-38e5-a38b-52fa1fa826df | -1.49595 | -54.17932 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 3c293023-e889-3a63-a43b-294ff9e381c0 | -1.49509 | -54.18457 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ac67de2-ef5e-3de2-83ca-622649396a3c | -1.49118 | -54.17865 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 58572cbd-be39-3054-a4f2-a2bc33b9be3a | -1.49033 | -54.18385 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 0a7f0fb9-7dbd-32f9-b96d-a77a5aac0481 | -1.1684 | -53.50256 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7d8324b8-1121-3766-a99d-a633fb3214ea | -1.16761 | -53.50742 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6641ae18-4172-3e23-bb7e-6d23e88b11c4 | -1.1638 | -53.5021 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d25025f0-f771-3e49-a042-a261d25e5619 | -1.16302 | -53.50694 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 722bc4c1-f3ae-3540-b263-bcca0eaad63b | -1.12501 | -54.1611 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8b3c854e-9372-3f00-9ee1-35335aa7f0ee | -1.12026 | -54.16024 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4be69c2b-573b-3a4c-a4ed-92070ba95779 | -1.09703 | -54.18312 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3afbd42d-d26f-36ea-bb5a-7df8cdec34cf | -1.084 | -54.11202 | 2024-10-24 04:32:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7d9cda01-a948-338d-8254-2a38a6c923b5 | -1.07605 | -53.66747 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6868140f-6205-3be7-821f-61d29f471d60 | -1.07526 | -53.67244 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| fc5f1348-37b8-3495-9e6e-2c42eb305f39 | -1.07223 | -53.66173 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 68b55d27-9aeb-3be1-a45f-5dc81cfb5d95 | -1.07145 | -53.66662 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c275d0c5-a172-3685-8f90-afde4d544935 | -1.07066 | -53.67157 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 363639b4-cb10-328b-81c0-3eec0b2d4cd0 | -1.06683 | -53.66591 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6258774b-8fb4-3895-b7cf-1b421aeac413 | -1.06373 | -53.65575 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b8e7ae10-70f2-33ee-9aa1-e0b0ee197300 | -1.06298 | -53.66043 | 2024-10-24 04:32:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c703c670-24af-340c-9051-a36a855f3da6 | -2.99637 | -54.10261 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 626fa602-fb83-357d-8640-5d8f0c66e8eb | -2.99607 | -54.10051 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 031ec27d-93e7-3b34-b170-b4e1c16a6cad | -2.94679 | -53.70733 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4a894616-b60c-3d77-9498-0ab5c101daaf | -2.94302 | -53.70213 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d2b2d777-b04b-3d4a-ab15-d8856ca43ebd | -2.94298 | -54.19785 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 2fae789b-d0c2-3929-8c27-f9b09710d575 | -2.9423 | -53.70662 | 2024-10-24 04:32:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 443c738e-2985-3883-b259-a14cab4cac99 | -2.94219 | -54.20269 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 66c3f2ad-6626-33ac-83e3-4de1074cf1af | -2.93846 | -53.91006 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ace0762-c27d-3ee0-b885-ffa127d4c68d | -2.93769 | -53.91471 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| da3102f0-c6a0-3a41-9f16-273c5d487d16 | -2.93691 | -53.91939 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4a8f7b61-a3a2-3338-a3f1-8f572dd0e6e3 | -2.93614 | -53.92405 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c37d0a45-4b40-3301-b551-8d0fd48db248 | -2.93313 | -53.91398 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 060faeff-5a11-3ef9-9b9e-135855ac3f4a | -2.9308 | -53.92796 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ebba25ce-0f53-3273-b9bd-c767412c3fc7 | -2.93057 | -53.92545 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 74eee496-6413-395e-af4c-c6df9ed57095 | -2.93003 | -53.93258 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b598acdb-a4cd-3cdf-a829-0949052814c8 | -2.92983 | -53.93009 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b638aff5-4c39-3a07-abfe-e618c7db4be4 | -2.92702 | -53.9226 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 82a73ea4-9fb0-3c6f-a803-166b7afb1a2c | -2.9263 | -53.87106 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a0244ffe-0e40-3b7d-92a9-8a56e4514baa | -2.92624 | -53.92723 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3fb8274-6968-3ba3-9cec-2e2dee8132c4 | -2.92601 | -53.9247 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d7469c9e-e274-31e1-bedb-1d5aaf726b50 | -2.92547 | -53.93184 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fd81a39f-f4cc-3258-868c-1a435d20323e | -2.92527 | -53.92933 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 67fb0006-20f7-343f-b96f-a99f81231068 | -2.92169 | -53.92647 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 948acca4-132e-37ce-8d74-4ecf9615679f | -2.92145 | -53.92395 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 17bf6503-fbb0-3493-9769-d66bc9b147fb | -2.92091 | -53.93108 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ada83bd9-de94-3218-b8de-ad5da5c58e6e | -2.92071 | -53.92857 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 62001c81-2833-3343-b556-b5e981073f2a | -2.91997 | -53.93319 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ea82a365-e9ae-3cd0-8e6e-2ac378752bbb | -2.91713 | -53.92573 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 57a70b03-e6dc-32f5-9638-67e2b9cd2349 | -2.91635 | -53.93036 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3892e909-0575-39ba-aeb7-59054332a8f4 | -2.91615 | -53.92783 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7a8b3f3e-e88c-3c00-b14e-36c0d0179eab | -2.91557 | -53.93498 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecaa2e9a-70d8-31b5-89e7-9818a86184ef | -2.91541 | -53.93246 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| edabb320-66ef-3f49-b510-5148740cd191 | -2.85905 | -54.59191 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ccb69329-217e-3136-8361-c17eb6253a02 | -2.85821 | -54.59698 | 2024-10-24 04:32:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 05d67011-488e-3fe6-b095-72e113631564 | -2.80852 | -53.98387 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cdbbfa06-bd65-3c39-b010-592a8d228239 | -2.80779 | -53.98748 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 495834b3-c15a-3ac1-8ed0-42e8cb104e43 | -2.80777 | -53.98856 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 623fdc60-a0a9-37e5-b8f3-c0058d06a3e5 | -2.79797 | -54.10308 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8a317122-b1f2-3715-b4bb-817fddd8d56c | -2.75799 | -54.03417 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a66f9d71-8ece-3b64-82c9-dfb698e6b30b | -2.75337 | -54.03345 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 410f8d7e-16a2-3517-a84c-8b4f59522dd9 | -2.74877 | -54.03272 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1e949241-f68e-3ee5-b608-f8cd564975d3 | -2.73463 | -54.14879 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fac182eb-fa90-3578-b6c6-fefd35ed5d79 | -2.73383 | -54.15372 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| b3620519-b630-38ad-94ae-4ad9dd1c9cd5 | -2.62091 | -54.51655 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bd8ee318-e24c-3f01-99fe-2d85f2c8ef6d | -2.61996 | -54.51989 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 07f7c97d-1e4d-39ac-9318-643a5ddd54de | -2.60545 | -54.54943 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1efb54ce-083e-36a5-a3e8-33d5e33c7fb2 | -2.6053 | -54.55122 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| eec092d0-cf22-301e-9a89-55d71f67d8d7 | -2.57769 | -54.01522 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6381b421-d72f-3b66-98e6-362d518a2920 | -2.57736 | -54.013 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 87c7a03c-a286-37c9-af15-c41dabfa122b | -2.57055 | -54.22596 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e4fd33d7-6d3f-3bc1-b799-2e40d9c37dea | -2.56769 | -54.01856 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 09005bd4-a223-3962-8bb7-876cd7224515 | -2.56384 | -54.01302 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 093b77a7-0426-349e-a803-439888a5537a | -2.49536 | -54.14191 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 8d883ff8-cc09-3096-b4de-0821ce64176d | -2.49069 | -54.1412 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 1ff35d9e-8baa-3d20-81fe-e9d708738bda | -2.44391 | -54.57598 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4d11b1cb-949a-3d18-8d96-3df3e84f98e2 | -2.44305 | -54.58121 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3820b1e7-e7a9-3e12-b8e7-cb019e289bca | -2.42171 | -54.28495 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6dee7964-bbbd-3540-8f2d-0f54721e9002 | -2.41904 | -54.28292 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 2fdf1cec-7810-3349-94b6-fa8d128197d5 | -2.41895 | -53.80372 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f8eff8c-d54d-3e21-bae1-a18cac97da4b | -2.41818 | -53.80841 | 2024-10-24 04:32:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 883dc51d-a4e5-3eb6-9135-54058c88270a | -2.41699 | -54.2842 | 2024-10-24 04:32:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d397ce89-18ee-3355-9d67-87dcb566a21f | -3.65119 | -54.21325 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7e7633e8-c814-3790-8b40-6f47aac13ef3 | -3.6504 | -54.21792 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf12e9a5-0c82-3cba-9005-b9354b9e15f9 | -3.63499 | -53.96842 | 2024-10-24 04:32:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |


[Clique aqui para ver as próximas entradas](README38.md)
