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

## Dados Diários - Página 148

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3afa3384-6fcd-3d05-a766-4008877afdcf | -17.04832 | -57.4385 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| d1b11a40-24d6-31f0-a0df-44fa0a981654 | -17.04719 | -57.42821 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| 46368724-02e4-3948-82fb-613b2075fb1f | -17.04299 | -57.43911 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| a5dffa86-3272-3fb2-a83b-3bb3696250de | -17.04135 | -57.5234 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| ab5005e0-f6f6-3a4a-a668-bc22430b925e | -17.03946 | -57.50599 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ea1d8929-6f69-33dd-ac3d-50e6eba0f80b | -17.03636 | -57.52748 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.9 |
| ff6a6e4f-4642-3443-92b4-538023e1fa9a | -17.03457 | -57.46095 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 1ffad47b-c2c2-366c-858d-db9a83fda65e | -17.02563 | -57.52865 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| 8233c948-4bc6-3627-b747-1f9812ab4602 | -17.02526 | -57.52516 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.9 |
| c05a63ea-da86-3ded-8aae-4a86f8b803f9 | -16.99888 | -57.3301 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| f46b6f9f-6ccb-34bf-9d8d-b2790b1627b7 | -16.99699 | -57.35637 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.6 |
| 8053b666-63c7-32bf-ac43-86db1730fe7e | -16.9966 | -57.35297 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 18.8 |
| 1259e875-66f2-3ea6-a2e5-24c087ca9a16 | -16.99613 | -57.3544 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 26.4 |
| 6bec931d-f68a-3667-b45a-38a17eb80ffe | -16.99582 | -57.34622 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 43.6 |
| acd235b4-66e9-30cd-85d1-5c07e2cfc89e | -16.99504 | -57.33945 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| b9348b5a-5218-3a3b-8c1d-2a5785484664 | -16.99465 | -57.33607 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 30.1 |
| 8696f076-95a1-319b-9d70-0e438e4bb2bc | -16.99431 | -57.33746 | 2024-10-25 16:50:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 31.4 |
| 61886954-67df-3aee-b3cb-b717015c707a | -16.97374 | -57.53267 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 26.1 |
| 823fa388-b322-3682-995a-cf1ec59f34ee | -16.96799 | -57.52977 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.5 |
| 6ec5986f-7915-3c86-be69-b9fed541f921 | -16.90856 | -57.68588 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 97df41e6-08d5-32aa-a794-2a2fb6b1f659 | -16.90818 | -57.68232 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| bd0c9326-c4f8-3b2f-baac-077abe85aef5 | -16.90686 | -57.49897 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.1 |
| 0ae029f5-5db6-3fc4-8bd3-21593ef000bf | -16.90533 | -57.50154 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 19.0 |
| d1bb8d9e-1f0e-3589-b460-5e3bc4ab49fe | -16.90489 | -57.48172 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 7c46910f-d73a-30e9-87ee-060d6b0b1360 | -16.89132 | -57.8488 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 16.7 |
| 52766e81-75ad-3b0b-ab84-4a053bb8437d | -16.88665 | -57.85669 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 15.9 |
| d9a7e834-3ba4-3237-ae1a-706feb29193c | -16.87238 | -57.67622 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| 304f9502-49fc-3cc8-9cdc-0acc73765763 | -16.87199 | -57.67268 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| fb04f3a8-a6c4-3618-b5a3-d9b37e96ddfa | -16.79048 | -57.41504 | 2024-10-25 16:50:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 12.0 |
| 16ce9642-2024-3060-8141-e421ef3221cf | -18.40563 | -57.34821 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 7e444c93-faf1-320b-a818-b38385156c67 | -18.12743 | -57.37299 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 11.4 |
| 17c6ddc6-734c-3e62-8624-8a7ae8d6f598 | -18.12671 | -57.31609 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.8 |
| b57125f2-cc1d-3d8d-a682-a8413fb0c5f6 | -18.12172 | -57.32016 | 2024-10-25 16:50:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 14.0 |
| 4feb87db-da1e-3224-b55a-e6757c16f58b | -13.95781 | -58.51312 | 2024-10-25 16:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 11.2 |
| bc98b66e-428d-36e7-b832-b7632fb97a31 | -13.95149 | -58.50664 | 2024-10-25 16:50:00 | NOAA-21 | SAPEZAL | MATO GROSSO | Brasil | 5107875 | 51 | 33 | nan | nan | nan | Cerrado | 14.3 |
| 54c21712-6de2-3556-a75c-55169cf5bb8e | -15.49889 | -58.06849 | 2024-10-25 16:50:00 | NOAA-21 | MIRASSOL D'OESTE | MATO GROSSO | Brasil | 5105622 | 51 | 33 | nan | nan | nan | Amazônia | 10.2 |
| a2a44a1b-4f92-37bd-8226-e8dbe1febe94 | -11.47511 | -59.09605 | 2024-10-25 16:50:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 35806a24-55f0-383b-81a5-c5d99c8833ed | -14.68488 | -59.64024 | 2024-10-25 16:50:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 29.5 |
| 0c2a60f8-b07a-3053-aac6-b466ada01aed | -14.6818 | -59.64347 | 2024-10-25 16:50:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5cb53e84-123a-3523-8f59-4a5f548e0884 | -14.6813 | -59.63898 | 2024-10-25 16:50:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 5089f6f1-cb7c-3f5d-832b-4a53649c0104 | -14.54365 | -59.95828 | 2024-10-25 16:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 535b7cc3-d058-3b1b-b82e-78ec35412ff2 | -14.54314 | -59.95356 | 2024-10-25 16:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 6fc3815d-75c5-3f6a-83ba-38e509a31352 | -14.5376 | -59.95918 | 2024-10-25 16:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 41.3 |
| d669fed5-9b69-36d4-9300-f918eabd3fca | -14.53709 | -59.95445 | 2024-10-25 16:50:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 67bec169-89e5-36c8-98f5-8c25456e763d | -15.66851 | -59.76459 | 2024-10-25 16:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 58951da9-1aee-3a5d-ac71-030b92b7dd3b | -15.66712 | -59.76183 | 2024-10-25 16:50:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 17.3 |
| fd8b4e22-0753-37a1-8e70-046c1b976ffb | -7.06631 | -47.22402 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 56ea4299-4b2d-316f-b195-09f6c2d822dc | -7.06366 | -47.38945 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 4511514e-d4c6-360b-9068-1803f3facac6 | -7.06152 | -47.26285 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| b23cfaf2-ba8e-3c78-972c-a0ac89df1cbd | -7.03853 | -47.36266 | 2024-10-25 16:52:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| ba559f2e-32e3-3c81-b3fd-8a235465e057 | -6.99639 | -47.06745 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| daa3a061-df4d-34fd-a085-3de1c1520fef | -6.99271 | -47.04896 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 85.0 |
| 01f9c965-a3e8-3d33-97ab-a61cc7da13ae | -6.99137 | -47.04047 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 97c29fc7-677b-3407-ac9c-888a2de300b0 | -6.98841 | -47.0453 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| 6af7056b-69a2-38aa-8d58-a67d25c7d66b | -6.98774 | -47.04106 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 13.4 |
| a9c9126a-1efa-3753-b912-3d4ab2b9334d | -6.98544 | -47.05013 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 9f6c3c6d-ba2a-36de-967b-4060ed4514b0 | -6.98477 | -47.04589 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 73b806ba-7843-3abe-b1b3-c9fd5e14fb1c | -6.95005 | -47.03852 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| f6d07ba9-e38e-35a1-8568-a47c9b0b20ac | -6.94821 | -46.93354 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 6.9 |
| fe0f1314-1a81-3f12-869b-795a92be9148 | -6.93962 | -47.2043 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 133b70d4-ca15-3e45-b710-f348afeda9dc | -6.92564 | -46.83951 | 2024-10-25 16:52:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 4a9e2605-a7f8-3b3a-8a18-d7d7aba03709 | -6.90264 | -47.0681 | 2024-10-25 16:52:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 10.6 |
| e62ab383-4677-376e-8c50-1e0bfe765336 | -9.33366 | -47.96373 | 2024-10-25 16:52:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 1c9b99a9-59c1-3fd1-b85c-ae13ae325e83 | -9.30388 | -48.26377 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9157a513-ee8e-3a01-b6a8-033627fc4d06 | -9.3005 | -48.26431 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 9b2ce7e2-9961-3c1e-8c06-55ff2571d3f5 | -9.29712 | -48.26485 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9ddb5320-1332-3b11-ab64-2fcd97065a1d | -9.28749 | -48.69926 | 2024-10-25 16:52:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 8.9 |
| f9488141-1d96-31ba-bbc6-c6c8ec566bea | -9.25293 | -48.3239 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 7fb0be04-23a2-3e65-abdd-3f80901a3f75 | -9.25013 | -48.32808 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a58e3d8a-a634-395c-906f-eec03273fc10 | -9.14341 | -48.29697 | 2024-10-25 16:52:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 11.5 |
| b2e92fd9-2d3f-3602-aeef-64436e175a1a | -9.07269 | -48.00205 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 48058237-63d1-374c-9260-c8c5954c6b50 | -9.06986 | -48.00634 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| bfd6627e-c5e6-3719-ae48-c4cd6948a57f | -9.06927 | -48.00261 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 90.0 |
| 5d09dd25-54c3-373c-ab7f-61a5897eb48c | -9.06869 | -47.99889 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 12.8 |
| 270df1b4-3ab0-3fe6-a14a-9bb0b86bb568 | -8.90757 | -47.97918 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d50d9ca-b967-31aa-b1cc-d21c7e5d71d2 | -8.90458 | -47.96045 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 898db63a-943a-389f-96ae-3fcbc7e80ec7 | -9.42079 | -47.84977 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d5eb264b-a79c-3e73-b17c-d11a50ddb9a8 | -9.41737 | -47.85032 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| d4288ca3-6eb6-39ca-b148-1fceabe777fb | -9.41395 | -47.85087 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| d5ddb4cf-1b45-316a-a100-6b4082998737 | -9.40258 | -47.86832 | 2024-10-25 16:52:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c740c0f1-ad07-308a-806c-9df948ed6453 | -9.27273 | -47.91255 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 7.4 |
| a57adfe8-e332-3d76-bf3d-17875ff373e6 | -9.26931 | -47.91311 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| 5d61ed97-a71c-3c21-8ec5-78849fc30bf5 | -9.21007 | -47.78393 | 2024-10-25 16:52:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 60ca79b7-7f1a-3427-b211-b3cbc732cab3 | -9.14042 | -47.56349 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 2ac607b2-3316-3f4b-b984-2273223c661f | -9.10196 | -47.6565 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 6ea86142-5efa-3d11-981f-157f5d0ccbac | -9.08929 | -47.59952 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| bc7dbd70-09c1-38b5-8625-be7abb61284c | -9.08781 | -47.74486 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| dd6ff2ae-0552-31cb-bb7c-7cb9415e5894 | -9.0706 | -47.74765 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6e50c3fa-5a02-3ac9-8ee2-832c1152bb4b | -9.06558 | -47.75631 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 54b6d115-b7d1-31d6-a229-091053688040 | -9.0593 | -47.76122 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 5647cffa-f176-3b75-98b0-7a806612ba56 | -8.99896 | -47.75933 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 7.0 |
| e4d98956-06be-39ad-9fb1-cb6732e22792 | -8.97583 | -47.74735 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 4ba16e6d-8cea-3237-87c2-4bbaaa89dc91 | -8.95848 | -47.68361 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| dbe05d76-d599-3b28-80c1-b79c54f2b9fe | -8.95514 | -47.64089 | 2024-10-25 16:52:00 | NOAA-21 | BOM JESUS DO TOCANTINS | TOCANTINS | Brasil | 1703305 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9736a7ee-c642-3927-8e14-d5d0dbf7d94f | -8.95503 | -47.68415 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| e22fb853-3590-32a7-8766-7ab5c08b9e9e | -8.87039 | -47.65889 | 2024-10-25 16:52:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 3acdd99c-57f0-387f-a794-d019acab48c1 | -9.0072 | -47.2236 | 2024-10-25 16:52:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 37c2fca0-5ec3-3261-af46-fc7f25b45019 | -9.00644 | -47.3739 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| c082c7c9-ae04-320b-81ff-c09c97696b3a | -9.00589 | -47.37782 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 75bdb815-15d2-3997-a92d-621c5ba3de9d | -9.00527 | -47.3739 | 2024-10-25 16:52:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README149.md)
