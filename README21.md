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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8be8bf16-2869-3cce-9ff7-8da0caf5d6e8 | -17.6749 | -46.6715 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 91.3 |
| ac5b2620-fe28-3878-b66c-c120aeb9bb86 | -16.3153 | -52.9201 | 2025-08-12 04:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 27820312-4643-362e-a4af-8e21461d6022 | -8.5211 | -43.3063 | 2025-08-12 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 54.9 |
| e18b812e-af20-36c8-a0d4-d7b38602a82c | -17.6555 | -46.6523 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 95.2 |
| e8e22c7b-7329-3df3-8e7b-d7a56620513a | -3.9684 | -47.8901 | 2025-08-12 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 66fa446d-53ae-373c-b302-200587d22477 | -13.3427 | -50.2448 | 2025-08-12 04:30:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 70.1 |
| d383e5bd-37c2-3b57-8307-c02dd2576d36 | -12.555 | -47.0034 | 2025-08-12 04:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 803f1110-7e27-37e3-bcdf-4488f5e458b9 | -7.1483 | -60.1174 | 2025-08-12 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.2 |
| a5a8a396-083f-38d6-b800-32ab2ddcc76f | -12.5742 | -47.0006 | 2025-08-12 04:30:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 92.4 |
| b952a315-5810-3f40-b063-ce87467ec385 | -16.2961 | -52.9016 | 2025-08-12 04:30:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 79.7 |
| d5f9ae4b-3b2f-3fb0-a3a6-b54da203fbc2 | -3.9686 | -47.8684 | 2025-08-12 04:30:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| d25aa0bb-b61c-3381-ba89-5d54d975faad | -17.6544 | -46.699 | 2025-08-12 04:30:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 032fea43-a456-3198-9082-3645a109ed43 | -9.723 | -49.4806 | 2025-08-12 04:30:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 34.0 |
| 6eb21689-5b5b-3742-bfc9-f10629445e90 | -7.1299 | -60.1182 | 2025-08-12 04:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 5ec49680-f546-3814-906b-c0a62a4f111a | -3.9686 | -47.8684 | 2025-08-12 04:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| 4863bb0b-2b99-3644-a421-964951bc3376 | -17.6555 | -46.6523 | 2025-08-12 04:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 94.5 |
| cbe922d3-e699-33a2-b161-8cf0467b8a0e | -17.6549 | -46.6757 | 2025-08-12 04:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 255.7 |
| 413b99d8-95d9-3212-8df2-78df178307b0 | -12.5742 | -47.0006 | 2025-08-12 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 86.3 |
| 30367b92-6ea0-3271-b864-3a4bc0d74efc | -16.2961 | -52.9016 | 2025-08-12 04:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 82.1 |
| 3e635777-aab2-3219-b990-def0e5741af8 | -13.3427 | -50.2448 | 2025-08-12 04:40:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 0967d53e-0a12-304d-b50e-40746de87d83 | -8.5211 | -43.3063 | 2025-08-12 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 52.7 |
| dfbf4662-adbf-3307-b20a-bf0037e75d33 | -17.6544 | -46.699 | 2025-08-12 04:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.4 |
| a5270994-8001-3da6-b21c-f52bf991138d | -7.1483 | -60.1174 | 2025-08-12 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 79168b96-ff28-3df9-9aba-49735787d618 | -3.9684 | -47.8901 | 2025-08-12 04:40:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 29a613e1-c430-315a-8d25-966a2db616f7 | -17.6749 | -46.6715 | 2025-08-12 04:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 0d3bea63-4cf4-3fc4-9a88-832b6e6278d9 | -12.555 | -47.0034 | 2025-08-12 04:40:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 76.2 |
| ce19c92d-b6d0-306a-bc2a-b80eec991aab | -16.3153 | -52.9201 | 2025-08-12 04:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 55.2 |
| e50d36bf-58b8-3b35-8116-3201fd2c86f1 | -16.3157 | -52.8988 | 2025-08-12 04:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 44aeecfb-95d8-3858-80ea-bcbb196157e1 | -9.723 | -49.4806 | 2025-08-12 04:40:00 | GOES-19 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 33.3 |
| 718ea638-1241-3e8d-b1f5-5348e6ff94d2 | -17.6349 | -46.6799 | 2025-08-12 04:40:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 13b2c9d7-8982-39a2-8934-f9afe96b7a70 | -16.2957 | -52.923 | 2025-08-12 04:40:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 72.2 |
| 533aecdd-4deb-3e90-8afe-f44ddb884091 | -8.9401 | -60.7288 | 2025-08-12 04:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.3 |
| b7ae4374-60f1-30a9-9a2c-a4ee8ea711bc | -7.1299 | -60.1182 | 2025-08-12 04:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| ce7c976f-17fb-374d-8fc1-98c119e47eae | -8.5211 | -43.3063 | 2025-08-12 04:50:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 57.6 |
| 4688b549-98d7-3633-a2b9-8d2f4b58011b | -12.5742 | -47.0006 | 2025-08-12 04:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 75.2 |
| f8323f5b-a7a8-344a-9ff1-e66756b6a7b2 | -16.3157 | -52.8988 | 2025-08-12 04:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 9bf27e15-b565-31c3-95dd-b9d952dd4fd9 | -17.6743 | -46.6948 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 47.3 |
| a0b7b41e-390e-369d-bbdb-e24fcac3c068 | -16.2961 | -52.9016 | 2025-08-12 04:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 83.6 |
| d1d905cd-8e7b-3ba6-9e0e-a33ab996856e | -16.3153 | -52.9201 | 2025-08-12 04:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 892280a1-b89f-3630-8767-e917bfb7d376 | -7.1298 | -60.1374 | 2025-08-12 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 43.7 |
| 7cb35dc8-8a77-3d8a-bad8-97ae99b3b341 | -3.9684 | -47.8901 | 2025-08-12 04:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 6e82cdbc-1434-34be-9983-f509af0aabb8 | -17.6544 | -46.699 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 71.2 |
| 4213d813-97ff-38a4-86df-55300b7ec51c | -6.5856 | -44.564 | 2025-08-12 04:50:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 45.9 |
| 33c00ee7-59ba-335b-a95d-0395ee8da591 | -3.9686 | -47.8684 | 2025-08-12 04:50:00 | GOES-19 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 76.0 |
| ae0f1ab8-8b52-35dc-a9b3-394645027494 | -8.9401 | -60.7288 | 2025-08-12 04:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 41.2 |
| d62e04e2-a87d-3cab-b98d-af6b44237597 | -13.3427 | -50.2448 | 2025-08-12 04:50:00 | GOES-19 | SÃO MIGUEL DO ARAGUAIA | GOIÁS | Brasil | 5220207 | 52 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 57b0a7f3-7842-3842-8b08-549206eb3955 | -17.6555 | -46.6523 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 70.8 |
| 56480e4f-1da8-3423-959f-2a3c6003498c | -17.6749 | -46.6715 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 86.2 |
| 38291a8b-85e9-3dec-aaf5-8dd7ea24b291 | -12.555 | -47.0034 | 2025-08-12 04:50:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 104.7 |
| a8750451-f5fd-3fd7-95ea-27cd501a6baa | -17.6549 | -46.6757 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 221.3 |
| 8ec5c2d4-c110-3d6b-b5de-7034954d3659 | -7.1299 | -60.1182 | 2025-08-12 04:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 6bcf9b3b-d376-3bc0-81c5-683d5f4f5d34 | -16.2957 | -52.923 | 2025-08-12 04:50:00 | GOES-19 | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 66.3 |
| 90f9151a-e52e-39c1-8997-905713b13da4 | -17.6349 | -46.6799 | 2025-08-12 04:50:00 | GOES-19 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 75.9 |
| b7994031-4e89-3d3b-bbb4-b10e77e1c244 | -1.59391 | -50.43513 | 2025-08-12 04:55:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 48bbbcd7-97c1-31f4-8635-af7458eb26fd | -1.59071 | -50.43597 | 2025-08-12 04:55:00 | NOAA-21 | BREVES | PARÁ | Brasil | 1501808 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8471d01-3c05-384c-b96a-94cfcb90868a | -8.57445 | -54.70535 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4cd45bab-7186-3fd2-8e69-acbd076e3fdf | -8.57776 | -54.70587 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0f090339-c0f3-35d7-9839-3bdaedd075cf | -7.64522 | -56.72666 | 2025-08-12 04:57:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6d77e0c8-9d1a-3d73-b9a3-9e3ed7039adb | -9.07129 | -45.054 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d99207b1-e1fb-3782-8c13-89743e8f05f1 | -8.57661 | -54.69146 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cf7be784-fd66-3547-a76d-8d06360b5a14 | -6.61006 | -43.89265 | 2025-08-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 7937b59a-8237-37fe-9a95-7faefc4c4f57 | -7.13816 | -60.11993 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 8f5f5fb1-ca08-3a01-a3e9-0ad94daa6b99 | -8.56994 | -54.66905 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 99637d01-962c-340f-8fe3-62f611f4b701 | -9.64985 | -48.13869 | 2025-08-12 04:57:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 351a741f-e1a2-3bb4-b681-015ad6cabe8d | -8.5783 | -54.70239 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 73c95ac1-1b6e-3245-829a-73c3065afad7 | -8.57108 | -54.68347 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| a57df486-d55d-3f4d-92b5-100bd79eb52a | -5.84604 | -59.91695 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c4dd81df-c5d4-3288-9265-cb67685c0114 | -8.52146 | -43.30611 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| f1646bb2-260f-3910-841d-411405f75795 | -7.12293 | -44.62174 | 2025-08-12 04:57:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 5831d536-28f3-3789-b87d-f87273e41523 | -3.1758 | -48.80682 | 2025-08-12 04:57:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 10bde682-da08-3337-9938-589e02a0ed35 | -6.10492 | -59.93112 | 2025-08-12 04:57:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2ca55203-53c2-3d0e-9d32-ee8cd159f646 | -7.06375 | -59.20772 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d6d75aee-8072-39b4-b4f6-4e106bff99a1 | -8.57 | -54.69042 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4283d17e-1146-3011-9afa-f4b98ced4ba3 | -3.56931 | -51.08998 | 2025-08-12 04:57:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| baca91c8-3a84-308a-9378-3dc0695aef7f | -8.5673 | -54.70779 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6eab9a09-be01-33c8-a564-10324b3c27ae | -8.52019 | -43.31601 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| f47547bd-9fc7-3fe7-916a-28e7f1e2a5a8 | -8.5264 | -43.3169 | 2025-08-12 04:57:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Cerrado | 21.1 |
| 6e429d27-4d84-368c-ab12-5704b3e71d49 | -8.56393 | -54.68591 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dc380b7a-f877-3e25-b61f-25021a6c3c72 | -7.28605 | -57.64926 | 2025-08-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 80ef4483-9dbd-3738-82a2-37562ab86139 | -7.06767 | -59.20842 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1f50a862-eaed-3f57-8b32-a7c101129bbd | -6.61119 | -43.88437 | 2025-08-12 04:57:00 | NOAA-21 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 16.8 |
| c57b0a14-11e8-31ac-8f89-c102a0ef3d5a | -9.70828 | -49.48071 | 2025-08-12 04:57:00 | NOAA-21 | MARIANÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1712504 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 704eee73-244b-3dff-88de-011282dbaf59 | -3.8404 | -47.74981 | 2025-08-12 04:57:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 0dbbc9e9-7f75-306d-aaea-c65bddad4bef | -8.06688 | -49.71191 | 2025-08-12 04:57:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 953ea50a-3831-3f44-81b1-00f7df840f0c | -4.32708 | -48.39943 | 2025-08-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 599aff66-5e1b-37d7-bcef-b5a88a80f2f5 | -6.30635 | -51.39961 | 2025-08-12 04:57:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5070fedc-f4fa-3c7f-82b4-68d22a12c11f | -7.12982 | -60.11861 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| e0c4d71d-2ba8-3a8c-889a-1e0deeafd446 | -5.88978 | -57.74533 | 2025-08-12 04:57:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b70ce75-e1be-3d5e-a83f-2e77e1f37fb4 | -5.49471 | -43.98539 | 2025-08-12 04:57:00 | NOAA-21 | GOVERNADOR LUIZ ROCHA | MARANHÃO | Brasil | 2104628 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d172a79e-67eb-3af4-9663-bde3a805c04d | -4.31464 | -48.1037 | 2025-08-12 04:57:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| ac34d0b6-3c01-3108-9ecd-20d3f9a15ac8 | -7.06461 | -59.20265 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0218f2c7-b9c1-391e-abfb-ab86cb30f2b7 | -8.57607 | -54.69493 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 30711a0b-38a2-31b1-8801-bc12e341d226 | -8.57559 | -54.71976 | 2025-08-12 04:57:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 8b7732a3-921f-3d47-9785-1c9bdb2a743f | -7.55952 | -47.04406 | 2025-08-12 04:57:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 76b9d5cb-8f81-3747-81d4-b1f96c0ab98f | -9.0667 | -45.05962 | 2025-08-12 04:57:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 089c9ffb-b074-31cf-a9ce-b0217ff14950 | -3.42887 | -49.0477 | 2025-08-12 04:57:00 | NOAA-21 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 75271be7-d313-37f8-b09c-e30baa001ea4 | -6.57828 | -44.57201 | 2025-08-12 04:57:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7b4a68e0-cf4b-3fa3-8aee-ff2f8e02cae1 | -9.66712 | -49.86251 | 2025-08-12 04:57:00 | NOAA-21 | CASEARA | TOCANTINS | Brasil | 1703909 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f9c744cf-0b0f-3a2e-a619-8a1f98cb93eb | -7.12786 | -60.13002 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 60527791-27ec-3891-8c8c-8d06361dd24e | -7.06939 | -59.19827 | 2025-08-12 04:57:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |


[Clique aqui para ver as próximas entradas](README22.md)
