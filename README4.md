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
| e2d564dd-909b-30d5-acba-febc0a504038 | -12.12733 | -57.17455 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 11.9 |
| c188235b-7899-3414-af81-3b14c33e1813 | -11.93495 | -50.92806 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 130.7 |
| d2293a0d-da33-3d2b-82e6-0b4f7c2d3e31 | -11.34239 | -54.1202 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 35.8 |
| 01e5b37c-45ae-36ab-a5ac-23526c638863 | -11.38139 | -54.0538 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 45.6 |
| 2a9bcf59-9c98-3947-9856-edb593303539 | -11.96034 | -50.94 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 770.3 |
| 97b09c0c-4b8d-3802-8595-b07824c54f54 | -10.3938 | -61.25016 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 120.3 |
| 25d7764f-2a35-3154-913b-0f2a5675f5d1 | -9.96393 | -59.26437 | 2026-09-29 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 7a11115f-00d8-38b2-b171-9e4705e93e30 | -11.94699 | -50.94233 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 312.8 |
| d22f550b-1db0-3cb5-b22e-03438e3de92a | -9.13015 | -49.97791 | 2026-09-29 00:37:00 | TERRA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| 0983947e-a494-3627-8544-d7469ee87d0b | -11.96529 | -50.94563 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 581.3 |
| fb5ce94b-03c4-3d42-8888-4adb2207bf61 | -10.38404 | -61.25132 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 70.7 |
| ae9f1202-7322-3766-b1ee-800634093a06 | -11.32989 | -54.10883 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 21dd8e40-1e4b-3e8c-82aa-29e001b28b60 | -10.85081 | -60.74884 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| c1c5247e-1af7-3faf-ac42-8397a343e7ab | -10.79423 | -48.74677 | 2026-09-29 00:37:00 | TERRA_M-M | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 30.2 |
| 54643faa-11ae-3c82-933c-4aa312562b0e | -12.16602 | -50.82263 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 20.4 |
| fe19377b-0d00-33d1-9749-e3cdaf28f719 | -15.09949 | -53.89714 | 2026-09-29 00:37:00 | TERRA_M-M | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 255.8 |
| d3f1b202-ded4-3ec1-9775-03f21804400a | -11.98219 | -50.96547 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 796.1 |
| e7f2f75c-4489-317e-8a8a-6444000a519e | -11.99075 | -50.95749 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 187.7 |
| aa75d728-14f7-38ad-9dce-4158337928be | -11.93859 | -50.95034 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 39.7 |
| b8d7ea26-4e7a-3cb6-9ea8-e0b3e22d168f | -12.10954 | -57.1772 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| d61657a9-5efb-3f9d-8add-ee6823ff717b | -9.69623 | -58.11625 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5b33859e-fb79-3a4a-a313-a446c9f8b5a2 | -11.98573 | -50.98758 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 450.7 |
| 94e0b5e6-a6be-3c36-a440-2ef6285749d1 | -11.95077 | -50.96449 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 120.6 |
| f838cef1-c9e3-3185-876b-4afc00b88af5 | -11.99537 | -57.61325 | 2026-09-29 00:37:00 | TERRA_M-M | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f73e79b1-860c-3e18-9e68-eb54495ac36c | -12.13622 | -57.17324 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 12.9 |
| e28f113f-f642-3105-a883-a85f06f2d2d1 | -8.94952 | -57.4543 | 2026-09-29 00:37:00 | TERRA_M-M | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 900d146b-7131-3e1b-b4a6-3c2380b65917 | -14.22327 | -48.51792 | 2026-09-29 00:37:00 | TERRA_M-M | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 57.8 |
| e86408cb-d7d9-311d-875b-2ae9450e45ff | -9.92716 | -60.71495 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 32.1 |
| c59c36ce-fddd-3879-a531-c138966cf81e | -11.99444 | -50.97957 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 560.7 |
| c6524178-f39b-3eb4-8c0a-d75414f80a0e | -9.6874 | -58.11753 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 10.5 |
| a3066ba7-19ae-3c90-b432-47f59a89dc28 | -11.35366 | -54.05104 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 21.4 |
| e8611f2c-57ae-3df4-bf38-a26cf27705cf | -11.37081 | -54.0554 | 2026-09-29 00:37:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| accd664c-87fd-3ef5-b98d-c8d01e4df02f | -10.26457 | -59.03188 | 2026-09-29 00:37:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ba5c53de-e9b2-31c7-843d-151593c901bd | -10.81407 | -60.72828 | 2026-09-29 00:37:00 | TERRA_M-M | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d6d5f8f3-b04a-3f5d-91cc-ea63c7205ad6 | -12.13493 | -57.1641 | 2026-09-29 00:37:00 | TERRA_M-M | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e274f504-062f-39fd-ad38-b6c90d5ba387 | -11.9641 | -50.96216 | 2026-09-29 00:37:00 | TERRA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 957.7 |
| 8767c4be-f67e-376c-8e4e-4dbe9d390c70 | 1.65171 | -55.88084 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 00e3cf50-29c1-3f33-852b-552a1d9a3c93 | -6.09773 | -57.62829 | 2026-09-29 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 672deb75-0bd8-3da8-844c-93872c49062a | -9.4821 | -66.79153 | 2026-09-29 00:39:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.3 |
| b8f14c38-20e2-31cb-8953-6759b71a565f | 1.68183 | -55.91629 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 24.9 |
| e325bdc9-efe0-3921-86b3-9cb396115023 | 1.66107 | -55.89783 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 29.7 |
| 8b71c164-32b7-37cb-97b5-5f4da0922f37 | -8.56971 | -67.0162 | 2026-09-29 00:39:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 28.3 |
| d73449da-799e-37d2-82d6-6dc6a535ded6 | -3.70677 | -54.21738 | 2026-09-29 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 35.2 |
| 766546ae-d5b5-3cea-8c08-d008871cbc16 | 1.67041 | -55.91478 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| d0f6b102-6421-342e-9ea0-cde05c089f86 | -2.87396 | -49.64016 | 2026-09-29 00:39:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 29.2 |
| 470ff50d-8cb9-397d-afc9-f5659136d1ad | -8.56947 | -67.01109 | 2026-09-29 00:39:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.2 |
| 702b0cd6-0eb5-3e37-8797-a3476c456a34 | 1.87251 | -55.60165 | 2026-09-29 00:39:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| f38e3d6d-137b-32a3-9611-08555f70ba77 | 1.6725 | -55.8994 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 41f0aabe-4ea9-36a0-8294-33bb6379fa80 | -7.96887 | -54.90747 | 2026-09-29 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 28b20285-0a32-3c24-b9ad-fb982a291b8a | -9.12387 | -67.84574 | 2026-09-29 00:39:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 83.1 |
| f0479896-8330-3728-8034-e290fcaa1d2f | 1.68905 | -55.94831 | 2026-09-29 00:39:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| e82e3065-3806-3f5e-8635-b0bd66410986 | -8.5663 | -66.98833 | 2026-09-29 00:39:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 6c8a9fe2-01d8-3e8c-9f0d-55d5987fae05 | -6.67677 | -55.10979 | 2026-09-29 00:39:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 2fb56af3-c66a-3aea-be12-8ecca2c8bf93 | -3.70919 | -54.23423 | 2026-09-29 00:39:00 | TERRA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 23.5 |
| 0a9c9406-a60e-365d-9339-5982af0c93fb | -2.87264 | -49.64545 | 2026-09-29 00:39:00 | TERRA_M-M | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 32.4 |
| 8ea0ba88-b234-310d-9772-98f5cdc98c42 | -6.16432 | -57.70568 | 2026-09-29 00:39:00 | TERRA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 71223de2-2c97-3e35-a0c4-826ca2c99411 | -9.11677 | -67.8399 | 2026-09-29 00:39:00 | TERRA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d01ce6ad-c84f-3526-a528-93917a7351da | -9.48215 | -66.78591 | 2026-09-29 00:39:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 27.2 |
| dfff2164-19f5-379f-bc67-1cb02ab2f458 | 1.6567 | -55.8833 | 2026-09-29 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| af530578-9273-38ce-b2d2-2bb31d8f93ff | -10.3707 | -61.2513 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 1c3702cc-c04a-33d0-ad03-6670e265c419 | -8.5738 | -66.994 | 2026-09-29 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 66.4 |
| 7de5bb47-44cd-3b84-b32d-5717d3915ae6 | -7.3825 | -72.4621 | 2026-09-29 00:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 77.1 |
| 09adfffc-3da0-35c1-941f-9015bc1e7641 | -7.8483 | -45.8363 | 2026-09-29 00:40:00 | GOES-19 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 76.4 |
| 170a5041-b6df-3fee-ba16-a6227e1c2703 | -5.6081 | -45.0038 | 2026-09-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 25c2f563-b402-39e7-9e24-bff4767ccc72 | -11.1775 | -44.7832 | 2026-09-29 00:40:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 61.3 |
| cc7d6710-1bce-33b1-b473-9f621efa6958 | -10.7291 | -50.4912 | 2026-09-29 00:40:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 41.6 |
| b1a774c0-17f1-3050-9043-c7d8acfb4ec4 | -10.8424 | -60.7622 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| 6222f59c-8ac0-357c-b0bd-453bd56474c5 | -10.3705 | -61.2705 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 52.7 |
| e0ca096a-6295-3488-856a-081f98c8d5b3 | -6.2947 | -43.6427 | 2026-09-29 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 178.9 |
| a9738c92-14b4-3543-bf16-6ec54b6e9bee | -5.6268 | -45.0025 | 2026-09-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.4 |
| 21c85e9f-07bc-3ecf-84c6-794c3fcf3b1a | -10.8103 | -48.7574 | 2026-09-29 00:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 107.1 |
| 499818cb-0056-3025-b765-60fd51325e4f | -18.5885 | -48.415 | 2026-09-29 00:40:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 85.5 |
| 174b81ed-35f0-3bab-9481-a65323ef218d | -10.7913 | -48.7596 | 2026-09-29 00:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 93.0 |
| 7ffdcd73-a54e-34d2-b70c-357fb3f72f54 | -7.3825 | -72.4803 | 2026-09-29 00:40:00 | GOES-19 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 6fc7387d-655b-35c4-bcc2-a63bd21d4266 | -10.3894 | -61.2502 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 128.4 |
| a92d35dc-50ed-3944-995b-2dfe06933bc2 | -7.8297 | -45.8156 | 2026-09-29 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 198.1 |
| 52ef8209-07b6-3a79-8e2e-775fbe874fbd | -10.4079 | -61.2685 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 4d7e3210-ab21-3ae2-b43c-2fe33f329d6f | -8.5738 | -67.0125 | 2026-09-29 00:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| 7cc6400b-6598-3ea3-a825-699aa49af646 | -5.7374 | -45.176 | 2026-09-29 00:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 568abb7d-f2cb-359c-a313-db9631206668 | -10.3892 | -61.2695 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| 069158c6-333c-3133-896a-38202577f22e | 1.675 | -55.9028 | 2026-09-29 00:40:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 53.5 |
| 61798658-2c6a-3501-a189-b577619ecbd6 | -18.5684 | -48.4191 | 2026-09-29 00:40:00 | GOES-19 | ARAGUARI | MINAS GERAIS | Brasil | 3103504 | 31 | 33 | nan | nan | nan | Mata Atlântica | 94.6 |
| 7381cd7f-edcd-3d3a-9b5c-c0b212fa3ae6 | -9.9266 | -60.7171 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 72.3 |
| a406f798-0d16-3423-bf13-5403b3ed8772 | -7.8488 | -45.7912 | 2026-09-29 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 80.5 |
| 024196c5-4b09-3164-a7a9-f5aaf70906d4 | -9.9265 | -60.7363 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| b22ae9ac-8e2a-3f0b-80ad-6b687d51e57d | -10.8106 | -48.7355 | 2026-09-29 00:40:00 | GOES-19 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 80.9 |
| 1a5c3c9d-a271-3359-8276-870277ec2888 | -10.7916 | -48.7377 | 2026-09-29 00:40:00 | GOES-19 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 69.2 |
| e09ad4bc-b03e-3094-bf0a-1b538b5af8f3 | -7.7025 | -48.8667 | 2026-09-29 00:40:00 | GOES-19 | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 51.6 |
| d49db595-d13d-355c-b131-ac141e4851b6 | -9.1256 | -67.8507 | 2026-09-29 00:40:00 | GOES-19 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 72ca3a1e-562a-3be4-ace4-1fbd8cd96412 | -6.2949 | -43.6194 | 2026-09-29 00:40:00 | GOES-19 | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 58.9 |
| 28cc4e63-1a4e-3d3a-ab9f-a1226613b73a | -10.8426 | -60.7429 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 90.5 |
| e6d3019b-3a0f-3787-87fe-36814dbb8108 | -10.4081 | -61.2492 | 2026-09-29 00:40:00 | GOES-19 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 74.4 |
| 85046d0f-b295-3b9d-938d-85de2f73910f | -7.83 | -45.793 | 2026-09-29 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.8 |
| b4ab1e09-d2ee-3370-a496-c0835b0ee1ce | -7.8486 | -45.8138 | 2026-09-29 00:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 370.2 |
| 1b46a3f1-8b0c-30e1-a18d-a71366379ac5 | -9.9568 | -59.2629 | 2026-09-29 00:40:00 | GOES-19 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2a7bd582-8c29-3de5-8e9f-412eda6563c1 | -15.4585 | -46.1367 | 2026-09-29 00:40:00 | GOES-19 | ARINOS | MINAS GERAIS | Brasil | 3104502 | 31 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 39270b43-d52a-38ae-8388-418725b38688 | 2.7889 | -60.00713 | 2026-09-29 00:41:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ad7e818e-5289-3314-a495-f8ed63487fcd | 2.79014 | -59.99804 | 2026-09-29 00:41:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| f984bce2-40c7-3cd3-aa15-7d94d0813a61 | 3.28328 | -60.63182 | 2026-09-29 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c1d22157-60a3-34bb-b758-3eae2d47e820 | 3.28571 | -60.61413 | 2026-09-29 00:41:00 | TERRA_M-M | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 8.2 |


[Clique aqui para ver as próximas entradas](README5.md)
