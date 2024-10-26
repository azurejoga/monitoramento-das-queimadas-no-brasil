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

## Dados Diários - Página 94

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| beaa990e-c849-3968-946b-4c6d95bf3969 | -3.12182 | -53.71249 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d046f909-4d21-3592-9630-0d039a848361 | -3.12132 | -53.71588 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9f655969-5c00-3f0a-ab03-f10e3cc37115 | -3.12082 | -53.71927 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 157b3c5a-47b2-3465-9355-7bbdc39422c8 | -3.10911 | -53.72431 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 15408e90-87d5-3ecf-89dc-8f4fb64c94b2 | -3.10861 | -53.7277 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c412bab3-cc80-37bd-a539-22a9ce57aa5a | -3.10812 | -53.73109 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 89f52895-a8c1-3906-9d97-40fca18124d8 | -3.10762 | -53.73449 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 44242f3c-f25c-322f-8c5e-e07a936cf89a | -3.10425 | -53.72009 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 26911501-12a5-35b0-8117-00e65cf33373 | -3.10375 | -53.72347 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 5c4aeb57-a648-3105-bc19-3282fcdf66c1 | -3.10325 | -53.72687 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| d73fecb2-f612-3cc5-8eda-bf06b1301c69 | -3.10276 | -53.73026 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| aefc77bf-8d6a-36a1-86c5-776f544ac392 | -3.10226 | -53.73365 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 4e9079c7-829a-3cfa-9164-8dc346c8824f | -3.09888 | -53.71926 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7bae261c-6bec-3d78-8e7b-3aa812e66524 | -3.09839 | -53.72264 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 78560263-5476-398f-becb-edbf2c805864 | -3.083 | -53.82805 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8335fdad-eef8-3df4-aa18-cede4c606879 | -3.08253 | -53.83129 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3a771614-3da3-346c-b968-fccc8e4a4130 | -3.07674 | -53.83368 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f3cf84e1-2a20-3f45-85ee-c6d4422b555a | -2.94702 | -53.70111 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 69287eca-6e10-3ac5-aa33-dbf21555ed2f | -2.94651 | -53.7045 | 2024-10-26 05:36:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f0cfc0fd-1cbf-3c9f-80a0-9bbd2e02f1d5 | -2.83986 | -53.98458 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd3b1e0d-8b66-32df-baa3-a8185e0a4a0b | -2.80962 | -54.00526 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52293c5e-d1ca-3fcf-afe7-6c1817fd2b51 | -2.80652 | -54.10321 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb01158a-c0a3-36f8-9792-557ceb22f90c | -2.80606 | -54.10637 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3091448b-ba87-31b0-aff7-5a583d7abed4 | -2.80551 | -54.10207 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| cbb6d720-36d9-379c-951d-1674eea43086 | -2.80503 | -54.10521 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| df9b12f7-3f8f-31b1-aac1-eb7d5d6241cc | -2.80438 | -54.00446 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8bd7d34f-e5ac-3e0f-9687-519d2a1432f4 | -2.80132 | -54.10238 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd4a9278-b847-3095-96f8-d1c615bfd964 | -2.80086 | -54.10554 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b26507a6-0aea-33de-8343-5f15ce9e20d2 | -2.79983 | -54.10439 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| efa577f5-74ec-32c6-9d4b-6ca60729b2bf | -2.79935 | -54.10754 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 76a78d7a-fc2f-3ffa-b7d7-443b95127b41 | -2.79915 | -54.00365 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1f955e86-7922-3c2b-90b2-4e85c4a12d21 | -2.79475 | -54.11102 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| da5b4865-16af-30f3-8fc5-853f81434755 | -2.68289 | -54.02673 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f7dd4cd6-f294-3ef0-b134-70eaaa8c09f3 | -2.68242 | -54.02983 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c99f2263-368f-37d0-b798-cab247c65c4b | -2.67768 | -54.02582 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 181203a6-6e8f-3e46-b3c1-7536b2b49add | -2.67721 | -54.02896 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 7afdac72-be8f-3862-87ab-e1780ecfb369 | -2.56551 | -54.02011 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 97add30f-a960-3a2b-8880-53623011ea87 | -2.56077 | -54.01617 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| de8512a6-88d6-3727-8e61-8f5dd6e11b31 | -2.47544 | -54.04533 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c4a31b94-b0db-3bf4-814c-8c437f7c81b3 | -2.47024 | -54.04456 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b91ba276-998e-3db4-8ac2-0b748a2819c4 | -2.26884 | -53.63366 | 2024-10-26 05:36:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d19dc3c-501c-3737-a31c-8751db8990e1 | -3.51138 | -54.0207 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a8b34e3c-f6d1-3c5c-b772-e713985a8d12 | -3.5109 | -54.024 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3ce26d99-508c-39e8-8727-55973f89d7a5 | -3.50198 | -54.44176 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 055a7375-9294-375b-a664-0283492881c7 | -3.49966 | -54.43822 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b6ec991d-b54d-31f4-aeae-8d8bf7d697ba | -3.49924 | -54.44117 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e2237dd7-914a-3b12-b7e1-a3ce21eb6fdf | -3.49727 | -54.43812 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fd522b00-5897-35a8-85d8-190684b10e23 | -3.49683 | -54.44104 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc5e7452-f169-3613-b509-2d65c85dcded | -3.49211 | -54.43747 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8dccbf0b-f25b-3f84-aea3-75151472bade | -3.49168 | -54.44036 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 67b316ea-e693-373a-b203-05bcf6836204 | -3.49124 | -54.44324 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 65bb5026-e154-3aa3-9659-b036f662d161 | -3.48696 | -54.43678 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 39684117-8cfa-36b9-a7a6-d0a9d3543074 | -3.48652 | -54.4397 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3f001397-af4a-3499-ab00-e803d3ce82bb | -3.48293 | -54.46368 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10dedd17-f2a4-3e57-a200-ba44f4ca741b | -3.44185 | -54.12902 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2a0da79e-ec3d-32cf-832b-82d293852215 | -3.44139 | -54.13223 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 81e181e7-36c3-35bb-ae74-7110a5e0a25c | -3.4411 | -54.13185 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| faedf2d3-2675-32ab-a63d-d8bdd4ab5ff7 | -3.4295 | -54.57721 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5cc4a764-93a0-3a8f-b1e5-64fdc674fc6a | -3.42904 | -54.58027 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 63923988-17a5-3177-9424-f8d81a58c98e | -3.42439 | -54.57658 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8acc0b64-11a2-3e00-8f7c-fa6d1617ff33 | -3.42394 | -54.57962 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 1849991e-213f-3afd-bf0e-908a8dd10f7f | -3.41885 | -54.5789 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d1f82025-bc8a-3219-afba-9a829544a9a0 | -3.41841 | -54.58188 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 07d423f7-45ac-3f63-8da7-81886dc0a9dd | -3.41508 | -53.87024 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ee6622fc-44dc-3661-8d9f-3b34ebd93b91 | -3.15072 | -54.35064 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5d324daa-5b2c-3fad-8cb7-af108a54c3cf | -3.13915 | -54.28646 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5b733943-4a70-3776-8b0d-0c2a7406e75e | -3.1387 | -54.28949 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2efac8a1-1cd2-392d-a5d4-4b31d83307e9 | -3.13582 | -54.27319 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| eccac7c2-46da-3406-a7b2-7a0c50c27cdb | -3.13535 | -54.27638 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d46c05d0-4d07-3bc8-bec5-400ae6644feb | -3.13488 | -54.27955 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9160e00c-a33d-3e1b-87ed-67391407f44b | -3.13063 | -54.2725 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 907ba1ce-9e3b-3610-b549-dbc10ad3e78e | -3.13017 | -54.27567 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d6c05822-2859-3cbd-84d6-b9a638b779d9 | -3.11248 | -54.99224 | 2024-10-26 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 43f2d0c8-3903-390c-9d40-a8c24cd1af48 | -3.1104 | -54.99133 | 2024-10-26 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b37e9c47-e206-3ada-988b-d9ea8f7a56a6 | -3.07091 | -54.7832 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d885d353-b93e-3f34-b5d3-fba2ff72002a | -3.04089 | -54.84872 | 2024-10-26 05:36:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f1e23ae7-87a6-3ed0-850d-848a795169ef | -3.01155 | -54.49375 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b9676eb0-b598-3025-be67-13647e9eb270 | -2.98039 | -54.63409 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 856463b0-e172-37f5-9f0d-ccbeb77d9efa | -2.97996 | -54.63699 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 1face323-e57e-37f6-9e92-beeb81c25cb8 | -2.78051 | -54.7354 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 54e8616f-781d-33f9-8c31-59d9a4f9245b | -2.7773 | -54.72287 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9e7217ab-5457-3730-95fa-f972cf100489 | -2.77685 | -54.72589 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 824ebdda-3291-3df2-9df7-ddbded721693 | -2.77552 | -54.73476 | 2024-10-26 05:36:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a5950a41-61ad-3ce5-90ff-5c38b53388f2 | -2.36394 | -54.33151 | 2024-10-26 05:36:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4b521557-9fe2-303d-91d5-f946ae6763a2 | -2.15333 | -54.92212 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 60cdfede-b30b-32c2-af30-5511df172c2d | -2.15043 | -54.92075 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 21edd6cf-1be5-3c76-988f-3d03afcaba2c | -2.14959 | -54.92615 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 43a36460-f9dc-33a9-9356-4bfb4f013254 | -2.14847 | -54.92134 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9c9322b7-c691-3740-9dd4-65035976466d | -2.14767 | -54.92674 | 2024-10-26 05:36:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 99a5d9ff-c2c9-3c8f-b977-b80cb3685b88 | -3.66073 | -53.84618 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c890571e-bac5-33bb-a303-4a05c3cc3bfd | -3.6538 | -54.22342 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5109d46d-ba2d-303a-a0a8-276d32210b01 | -3.65304 | -54.22395 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7cab1276-206e-3024-8008-9985eaeb61b9 | -3.63224 | -53.9657 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| a64f00c0-3222-3398-b7e0-f59dcc2fc00f | -3.63177 | -53.96886 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdf2eb78-ef41-3b21-b9b3-f9829341ba3b | -3.61635 | -54.03706 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 528aad2c-298e-3db1-8df2-6d3a6d75785b | -3.61588 | -54.04029 | 2024-10-26 05:36:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 264b5319-4403-3a13-8fb7-0f30b4ec9116 | -3.58674 | -54.66169 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8f18b153-8084-374d-9543-65ccb1263fe8 | -3.58628 | -54.66468 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 19085d31-827f-3edd-81ef-d2e67993db85 | -3.58564 | -54.66145 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 25c6195e-f0da-384b-8710-a5bcbec0e368 | -3.58521 | -54.66444 | 2024-10-26 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |


[Clique aqui para ver as próximas entradas](README95.md)
