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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f326a29e-c685-3a4e-8d4a-6e20ba86d8fa | -3.07068 | -45.80556 | 2025-12-12 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 143.1 |
| 22993846-654e-3f4f-9151-e15e4fd667f2 | -6.51815 | -55.04716 | 2025-12-12 00:52:00 | TERRA_M-M | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 03745916-187e-3c1d-9ee2-5ecf83fe2517 | -3.05434 | -45.80276 | 2025-12-12 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 27.3 |
| 24c49ebb-e57c-3610-9449-6be79727f7da | -3.47271 | -50.87349 | 2025-12-12 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 41355484-3a51-3713-9ef1-16a5a64f0142 | -3.70055 | -50.95016 | 2025-12-12 00:52:00 | TERRA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 528291cb-5bdc-3fc5-8b20-fb5f06ad78bc | -3.33846 | -53.33278 | 2025-12-12 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 3bac3a28-f12b-31a5-ac97-38e96ec0da12 | -3.06457 | -45.7648 | 2025-12-12 00:52:00 | TERRA_M-M | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | 31.1 |
| e29e8b04-b05d-367f-a058-e4900e5e3a2f | -3.17194 | -52.87628 | 2025-12-12 00:52:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| c4c47232-6fb9-3184-af00-2a07493729f7 | -2.43741 | -51.92949 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 113.2 |
| d06abfea-2ba3-3afc-ad19-3bee9b75f646 | -2.44003 | -51.92268 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 3785fd2c-b2da-3b24-a414-f44ce024c77e | 1.12616 | -60.53409 | 2025-12-12 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 187baff0-b5e8-39e2-86bd-033b786af56f | -1.53526 | -52.74236 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 23.3 |
| 7a34bbd3-9bc4-3c42-af6b-2ff054b9e62f | -1.44319 | -55.86246 | 2025-12-12 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e1bba3d5-e4e0-3406-bea5-753fafe71b25 | -2.09267 | -53.41304 | 2025-12-12 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 21.0 |
| 083bdde4-6ceb-325f-b734-087714ade759 | -2.74656 | -52.98034 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.9 |
| cf39d7ca-bf84-3e1f-a6f9-9933c60af901 | -2.50055 | -51.80124 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 271.5 |
| c3513d62-8d49-3650-9f93-18d01267597f | -2.4312 | -51.93798 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 263.1 |
| 36684bb3-8ff1-3d42-a9b7-9059b911b01a | -1.32433 | -53.48814 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2a645921-9f23-3659-9cef-f5a5a107287a | -1.2899 | -53.16851 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 16.8 |
| f9397eb0-78b5-3292-9c0f-a20279242bd8 | -2.25286 | -56.05941 | 2025-12-12 00:54:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1576a6ed-368a-361c-80f3-cb98a42da510 | -3.12447 | -54.18161 | 2025-12-12 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 590cde8c-3f1c-3f8c-bc08-3e91dff54116 | -2.09135 | -53.4197 | 2025-12-12 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 24.6 |
| 0c09109f-cc85-39a8-be23-1bf2a4fdef39 | -3.0474 | -53.00534 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 11918bf3-b3fb-3dba-9cbb-4b67a0e5f133 | -2.49861 | -51.78728 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 33.8 |
| 3b5aee41-d954-3bf4-9eee-20e1720bef1c | -1.44442 | -55.87132 | 2025-12-12 00:54:00 | TERRA_M-M | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8719f216-67d7-33d7-a7e7-c6cb5b4126c9 | -3.04738 | -53.01123 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 4eb62fd3-6e12-3b29-a125-53b04089bbf5 | -2.43931 | -51.9432 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 25.4 |
| 2be75924-e552-3e81-a3d2-014d9fdc58f0 | -1.52871 | -52.74914 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 13d357ec-a14a-3a38-ade7-8d3f612689a7 | -2.09425 | -53.42403 | 2025-12-12 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 37f3eb6d-229f-32aa-b675-176aacb20307 | -3.02193 | -52.82768 | 2025-12-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 503a5e6a-6346-3cb7-9f93-3801c94f3256 | -2.74493 | -52.96867 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 94a9bd4b-85aa-3aca-b540-c7802af54c54 | 2.0247 | -61.42425 | 2025-12-12 00:54:00 | TERRA_M-M | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 4b946f38-7493-3557-b356-54ee32212a6d | -1.52702 | -52.73687 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 26.1 |
| cf040a3e-9549-3358-aa35-c197b1e25050 | -2.42848 | -51.94478 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 1a7a226c-7c77-3098-93b1-e035688cae40 | -1.31526 | -52.53516 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7b619c26-76de-3b61-bf5b-94183c01a66e | -2.88084 | -52.69889 | 2025-12-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 650d0d97-be99-309b-ade8-c5526b38162e | -2.42465 | -51.9173 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| 08b5ffc0-7086-3b00-89f4-3b91218c69e9 | -0.97484 | -53.18409 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| b86c7f78-3d15-33da-b19b-68e7a83cc6f7 | -2.48961 | -51.80281 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.8 |
| 3cc996be-ac38-3da0-987a-8c292953151d | -2.44203 | -51.93641 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 952f7e57-8de4-312d-854c-c2ffae559853 | -1.32587 | -53.49922 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 849c2d0a-7599-33a3-bcb6-dcbc156f27ac | -2.66333 | -51.65034 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 00255ff6-c4be-3e2e-886a-1e5d58e034c6 | -2.25341 | -53.75537 | 2025-12-12 00:54:00 | TERRA_M-M | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 3e5aa76c-1029-3c05-8617-8297f9e5455f | -2.93648 | -53.02206 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 50907c3f-a067-35a2-9bde-b1c17235c13d | -2.66405 | -51.64441 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 08a0758c-b1ce-3951-b5c7-91657578ce11 | -2.48765 | -51.78886 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 2295eb37-c28a-343d-bd56-67a7a02f40d4 | -2.42657 | -51.93111 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 388.6 |
| 77c91b4f-b241-335a-97c5-13beb565ced8 | -3.04905 | -53.0167 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| bb0cf70c-594e-371d-8aa4-de9d685a7eb4 | -3.13372 | -54.18028 | 2025-12-12 00:54:00 | TERRA_M-M | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| 11dfb63d-7402-32a1-b5c5-ff6b5c5bd77d | -2.46355 | -56.03822 | 2025-12-12 00:54:00 | TERRA_M-M | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 3165293d-0e5c-39c5-bcd4-b14b233c3873 | 3.22683 | -60.00146 | 2025-12-12 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| cf1d2ec2-799c-3d9f-b808-9f70d4d841bf | -2.5025 | -51.81518 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 99ac0c7d-defd-3956-9771-e26725ae7b92 | -1.53703 | -52.75461 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 7bb69c8d-bdf2-3dbe-8bfb-931cbdacfdfc | 1.12783 | -60.52213 | 2025-12-12 00:54:00 | TERRA_M-M | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 078b015d-82e2-361c-82c4-923ae0bf7b81 | -2.93806 | -53.03328 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| c1a14b32-cb0b-3813-8baf-2a6df9ed51d4 | -2.41572 | -51.93266 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5956e9e8-9cc4-3be9-b6a0-d60ac9fb338d | 2.00221 | -55.67562 | 2025-12-12 00:54:00 | TERRA_M-M | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e8c7007a-4e5f-376d-b43f-e609ebc703ea | -3.02077 | -52.82203 | 2025-12-12 00:54:00 | TERRA_M-M | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| ad996117-1b37-357e-8c47-eb31a51501e8 | -2.50218 | -51.79528 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 216.1 |
| dc5b64e4-1687-34d0-9b70-a3d5e93fc629 | -1.70128 | -53.9297 | 2025-12-12 00:54:00 | TERRA_M-M | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 6.8 |
| efae431e-4b1d-33e8-89a9-17e030e13dfe | 3.30311 | -60.11468 | 2025-12-12 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.1 |
| b86fc3c4-fc4d-3aec-b9bd-44163c5c3545 | 3.29353 | -60.11311 | 2025-12-12 00:54:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 272a6601-3717-31bf-8dcb-59d672f1fea2 | -2.50422 | -51.8092 | 2025-12-12 00:54:00 | TERRA_M-M | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 74.8 |
| b4540513-bc33-3143-9183-b52728425f10 | -2.42918 | -51.92423 | 2025-12-12 00:54:00 | TERRA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 321.5 |
| c16a4b8e-f01a-3875-8f66-bd5dc85fa789 | -2.88354 | -53.00631 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 5037e2da-aeef-3e68-ba77-2f64994f8438 | -2.88519 | -53.01781 | 2025-12-12 00:54:00 | TERRA_M-M | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 15.1 |
| 88043d85-0a6c-3b3c-b5e7-26b920d8ae69 | -1.28828 | -53.15687 | 2025-12-12 00:54:00 | TERRA_M-M | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2278b543-b766-39cb-8769-525915e4061a | -3.0618 | -45.780201 | 2025-12-12 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ee4f3dda-a41d-379f-bcc1-a1a9fc14fc9f | -12.4011 | -58.006802 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 0a0b5a8b-10ce-369b-9099-5382067147e4 | -20.6364 | -51.673698 | 2025-12-12 00:55:00 | METOP-C | TRÊS LAGOAS | MATO GROSSO DO SUL | Brasil | 5008305 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e6531160-9ec5-3a57-b7e7-374e52d6de46 | -3.2336 | -42.058998 | 2025-12-12 00:55:00 | METOP-C | MAGALHÃES DE ALMEIDA | MARANHÃO | Brasil | 2106300 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| b23a7dbd-bde5-3445-9f80-1e04db61fe34 | -2.2348 | -45.407398 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 05ee4cff-fc3d-3b47-88d8-b5cef7611a52 | -20.4664 | -55.582199 | 2025-12-12 00:55:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 2cf37757-8b50-33c6-9342-cafb3ac461c4 | -3.6245 | -45.388199 | 2025-12-12 00:55:00 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b7365e55-afcf-3827-b286-b3dbf1d1d390 | -12.6181 | -58.074799 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| d0ebc463-03b5-3311-90d0-27fb74a7bb64 | -12.4092 | -58.047001 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ee3437db-4a88-3310-a78c-ae583f0bb8aa | -12.4038 | -58.020199 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 50c6891a-6d88-3073-84f1-cd8f8eaef42e | -3.058 | -45.764198 | 2025-12-12 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 259937fc-31ec-3723-8178-9a7e06cd5402 | -12.1998 | -49.533501 | 2025-12-12 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 312d77ca-768f-346e-b721-a82950d4f408 | -18.8407 | -51.622601 | 2025-12-12 00:55:00 | METOP-C | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| e3b810b3-a708-3c55-8f49-6dedd13b237e | -12.5093 | -58.3419 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f4c78141-7eb6-317a-8bbf-d853a101d439 | -3.0657 | -45.796299 | 2025-12-12 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 072d013b-a93e-3d2c-bbce-ab8124e50744 | -12.2015 | -49.541 | 2025-12-12 00:55:00 | METOP-C | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 93fe4524-a1bc-33ad-b6f7-0c14eceea76b | -12.4163 | -58.031601 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e429d643-ea7d-32c8-86b1-e12cba841479 | -23.302099 | -45.629101 | 2025-12-12 00:55:00 | METOP-C | PARAIBUNA | SÃO PAULO | Brasil | 3535606 | 35 | 33 | nan | nan | nan | Mata Atlântica | nan |
| d3a24041-34c7-3bbf-a42b-302ecba2c638 | -4.394 | -43.620998 | 2025-12-12 00:55:00 | METOP-C | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 605959a0-8e83-3232-9aa7-27c76b02fb7e | -12.4065 | -58.0336 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 906c692b-203a-3ef5-9c02-da2e87879780 | -3.6342 | -45.385899 | 2025-12-12 00:55:00 | METOP-C | PINDARÉ-MIRIM | MARANHÃO | Brasil | 2108504 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c2973b45-f353-3e22-af89-c48c436fcb56 | -20.385799 | -41.310699 | 2025-12-12 00:55:00 | METOP-C | CONCEIÇÃO DO CASTELO | ESPÍRITO SANTO | Brasil | 3201704 | 32 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 25bfd692-e07c-3f43-bd1f-f99ad228611f | -2.2208 | -45.392101 | 2025-12-12 00:55:00 | METOP-C | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19c2bc79-0b74-37a6-bda3-03ff15214044 | -3.8187 | -50.604 | 2025-12-12 00:55:00 | METOP-C | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 942ce28c-421e-3d3a-a925-91a4e453c585 | -12.4331 | -58.014198 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| e58c86ea-a4d8-3f47-b126-d4ba544adf8d | -12.5065 | -58.327801 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 2f1a489b-2bf5-3711-b122-3f0500a2d737 | -3.9613 | -41.501999 | 2025-12-12 00:55:00 | METOP-C | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 96ca1ade-8f9f-3c7a-9a06-c66e66061724 | -2.1383 | -45.648201 | 2025-12-12 00:55:00 | METOP-C | CÂNDIDO MENDES | MARANHÃO | Brasil | 2102606 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a37f6e7-0162-37d8-ba31-ebb3d20d0393 | -3.0715 | -45.778 | 2025-12-12 00:55:00 | METOP-C | ARAGUANÃ | MARANHÃO | Brasil | 2100873 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bc70e43f-b8a5-3012-9176-312b438ba8b0 | -20.4762 | -55.5802 | 2025-12-12 00:55:00 | METOP-C | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| daa568fe-5c66-36a2-a943-43793f8064da | -3.6655 | -45.772202 | 2025-12-12 00:55:00 | METOP-C | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0aa859d8-00b5-38fd-bf5c-cd83b28fbd8e | -12.6279 | -58.0728 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 77cbd58d-80a2-3e20-899c-2b93b2857886 | -12.4136 | -58.0182 | 2025-12-12 00:55:00 | METOP-C | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README6.md)
