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
| daf65d39-1640-39ed-b4b1-a0b785d335fa | -11.3996 | -46.3305 | 2026-08-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 179.4 |
| 1cf14584-37e1-3249-aeb1-dad4e2774a64 | -6.9685 | -59.2976 | 2026-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.4 |
| ba577d4e-f029-3865-9c1a-b2915a19c771 | -6.6195 | -59.0416 | 2026-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.3 |
| 99c851f9-36ef-36fd-8fb8-7504e1403176 | -11.4184 | -46.3506 | 2026-08-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 133.2 |
| c56f776f-dc14-3c66-8d25-46e9c0ae4e49 | -14.1318 | -53.6694 | 2026-08-15 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.9 |
| 6ccd87ee-f856-3941-8052-a312046ce1cb | -14.1315 | -53.6903 | 2026-08-15 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 3a79746b-fc99-3330-a627-15c7d980c271 | -6.9334 | -43.6333 | 2026-08-15 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 16de68d6-e5ac-3021-8d7e-eaaa11dabd51 | -6.6197 | -59.003 | 2026-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| a9f66d30-3107-30a2-98a9-5643957555c8 | -1.5805 | -47.7462 | 2026-08-15 01:50:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 5eb5e0b1-63aa-3d2a-b0ad-00dc2f3d8591 | -6.1222 | -44.0271 | 2026-08-15 01:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 89.9 |
| b82d179f-8cdc-39d9-b9de-2fa374a5ef7a | -6.6013 | -59.0037 | 2026-08-15 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 69.9 |
| 314f87b2-b1af-36da-b9b8-5428ff210338 | -6.9145 | -43.6351 | 2026-08-15 01:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 6aefd9b1-d8d9-30b0-ad73-1ac6991ff707 | -11.4191 | -46.3053 | 2026-08-15 01:50:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 81.2 |
| c96acca5-bbd4-37fe-8a79-21e4fa5ccd99 | -6.9334 | -43.6333 | 2026-08-15 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 100.9 |
| c90bc8ab-2ac7-39ae-9959-26c773387e65 | -6.6194 | -59.0609 | 2026-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 78.6 |
| bd6745ee-47fb-3c7b-8b35-2bb371edd0f5 | -6.9145 | -43.6351 | 2026-08-15 02:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 1e771a91-e4bf-3318-9949-94328a1632ee | -14.4302 | -51.9243 | 2026-08-15 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.7 |
| 4a79e9be-0218-3cb7-8c88-504f466e22bf | -1.5805 | -47.7462 | 2026-08-15 02:00:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 44.9 |
| 0f39c5db-06be-3012-822c-d46fa54a5090 | -6.6197 | -59.003 | 2026-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.4 |
| efb18584-a922-346d-a557-27dcf9b311df | -14.4495 | -51.9217 | 2026-08-15 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 69.3 |
| f0884320-3f5c-33f4-bf9a-e46dd9ee310d | -9.1219 | -46.404 | 2026-08-15 02:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| 38c28236-0536-3f1e-b5cf-fbb3c5884b1c | -14.4499 | -51.9004 | 2026-08-15 02:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.2 |
| eba72f16-40a1-32aa-a3e5-5b9f9d492827 | -11.4184 | -46.3506 | 2026-08-15 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 57.7 |
| 728ec047-977b-3df3-a925-c83306d394e1 | -6.6013 | -59.0037 | 2026-08-15 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 2f055167-5c86-3b87-9a49-8ba451b62b45 | -14.1315 | -53.6903 | 2026-08-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 83.7 |
| a28ab971-c508-3f2f-8aca-d6a25d3228d2 | -6.1222 | -44.0271 | 2026-08-15 02:00:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 75.3 |
| d4d6f5f8-d67c-3349-b398-6de57de2b1be | -11.4187 | -46.328 | 2026-08-15 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 226.7 |
| 26980f0a-55a3-369f-ab29-776db975514c | -11.3996 | -46.3305 | 2026-08-15 02:00:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 123.3 |
| 68f19475-0de9-3a1f-a1c5-9a8b5c90aa3d | -14.1318 | -53.6694 | 2026-08-15 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 107.2 |
| 6feb707b-0b93-3798-8a11-c67f6a94dd97 | -14.1122 | -53.6926 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 51.3 |
| 908f1e96-7273-3bf1-872e-597b79aa63bc | -1.5805 | -47.7462 | 2026-08-15 02:10:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 42.8 |
| a07f6a5e-0d5e-3ced-a7e8-939aa7ecf2a1 | -6.6013 | -59.0037 | 2026-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 1a7f3a93-1f64-3de5-a5e4-0bf966aaef77 | -11.4187 | -46.328 | 2026-08-15 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 126.5 |
| 4ebd7881-6712-35aa-aaef-3b894caf3e75 | -6.9145 | -43.6351 | 2026-08-15 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 2d5d767a-a818-3658-8050-66fc884df555 | -6.6194 | -59.0609 | 2026-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 0dbd15db-9ad3-3a97-a40d-c086113ef85c | -14.0926 | -53.7157 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 7d1c42d3-9bd8-34c4-b5e4-7c76777e3171 | -11.4184 | -46.3506 | 2026-08-15 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 91982569-e387-33a7-9a0a-48c91b14de18 | -14.1119 | -53.7135 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| de268398-1ba5-369a-ad90-5440ffc4f630 | -6.6197 | -59.003 | 2026-08-15 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 61.2 |
| b4a34708-da18-3805-b444-06c7a8c58ebc | -14.4302 | -51.9243 | 2026-08-15 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.0 |
| b4791c3f-98e5-3e5e-bc72-85bfb4580e84 | -14.1318 | -53.6694 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 87.9 |
| 512981b8-0ccc-3a8d-8572-c93a07396384 | -8.5171 | -46.5338 | 2026-08-15 02:10:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 30042bc5-6b4e-36e7-b5a2-ba0c8f63faa0 | -14.1315 | -53.6903 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.6 |
| 17306b91-5dd0-3f47-bd58-6f9413d28972 | -6.1222 | -44.0271 | 2026-08-15 02:10:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| e1e83a18-8189-366e-84de-a9b5a0b3a6e7 | -14.151 | -53.6671 | 2026-08-15 02:10:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 45.6 |
| f3e758ee-6229-3b50-baba-9cc0e706812f | -6.9334 | -43.6333 | 2026-08-15 02:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 80.6 |
| 7a7f918e-18c9-3179-80dd-804ff52acbe4 | -14.4495 | -51.9217 | 2026-08-15 02:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 57.2 |
| ffe64ccf-2e37-3235-9e91-be4cd2805bed | -9.1219 | -46.404 | 2026-08-15 02:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 69.4 |
| 9a99fd1c-7fef-3e39-a695-1ff5918512cf | -11.3996 | -46.3305 | 2026-08-15 02:10:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 87.6 |
| 25cb0d6e-35e4-34bf-b584-4ac1701e9c05 | -11.4 | -46.34 | 2026-08-15 02:15:00 | MSG-03 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 57c1c800-9277-3440-a131-6c4e75ecfd79 | -6.6194 | -59.0609 | 2026-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 5134b2a0-d265-3008-8d6b-dc9398d3c615 | -6.9334 | -43.6333 | 2026-08-15 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 26529549-308f-33b8-ae2e-758c49e4c513 | -6.6013 | -59.0037 | 2026-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 74.9 |
| 6ff92548-d854-36f3-b088-365ed4135fec | -9.1219 | -46.404 | 2026-08-15 02:20:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 63.4 |
| 20d17b88-f506-3f03-9c70-b7a50afdb9ea | -8.5359 | -46.5319 | 2026-08-15 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 41.1 |
| 8206b801-c7e1-36f2-98ee-b3aca069adc2 | -6.9145 | -43.6351 | 2026-08-15 02:20:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 61.8 |
| cf3da3ae-304c-3c0b-9a66-70db89167936 | -6.1222 | -44.0271 | 2026-08-15 02:20:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 80.4 |
| d37c49e2-2a10-357f-9dc9-4c1a189f0bb6 | -14.4302 | -51.9243 | 2026-08-15 02:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.7 |
| 785b464d-769b-3903-856b-4831bce665ad | -16.8994 | -54.1509 | 2026-08-15 02:20:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 400af819-628a-3e25-afe1-560bc00ade4b | -6.6197 | -59.003 | 2026-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.6 |
| ee9b55b9-a196-3677-a43d-0d3fab44834a | -8.5171 | -46.5338 | 2026-08-15 02:20:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 65fbac3d-da85-3770-8915-bc665cfc27a6 | -6.6195 | -59.0416 | 2026-08-15 02:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 089c892a-2190-3b4d-9c27-5bf24c933c32 | -1.5805 | -47.7462 | 2026-08-15 02:20:00 | GOES-19 | SÃO MIGUEL DO GUAMÁ | PARÁ | Brasil | 1507607 | 15 | 33 | nan | nan | nan | Amazônia | 38.1 |
| 6cab318f-1521-3464-bb9e-d9fa4805baf1 | -11.4187 | -46.328 | 2026-08-15 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 59.6 |
| 4d354a72-762b-33c9-9f23-f7f31399f21f | -14.0926 | -53.7157 | 2026-08-15 02:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| def32601-f058-3987-92c6-efbd192857a7 | -11.3996 | -46.3305 | 2026-08-15 02:20:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 4f06221c-665d-3e37-92cc-01b20f544120 | -6.6194 | -59.0609 | 2026-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 68.1 |
| b1417f38-030c-3171-a44a-84ffaf510b64 | -16.8797 | -54.1536 | 2026-08-15 02:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| 526485d1-3d9f-3440-8021-27f019cb26c5 | -6.1222 | -44.0271 | 2026-08-15 02:30:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 67.3 |
| a28e0e57-304b-334a-b8b3-c67e48fa6fc8 | -6.6013 | -59.0037 | 2026-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 4d8b61d2-f452-3f4b-bd9f-b184cf998c27 | -16.8998 | -54.1297 | 2026-08-15 02:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 87.5 |
| 121582a3-a181-36ee-b842-59a812385d48 | -6.9334 | -43.6333 | 2026-08-15 02:30:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 71.9 |
| f2ad7969-9b1e-35ce-b786-0a93057bcfd2 | -14.4302 | -51.9243 | 2026-08-15 02:30:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 65.0 |
| e2e9d2b5-132d-3b5c-8b84-63171daf4343 | -6.6197 | -59.003 | 2026-08-15 02:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.3 |
| dbe957b1-c2ec-32b8-9ec8-a298311b44d0 | -9.1219 | -46.404 | 2026-08-15 02:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 58.6 |
| 8e659c7c-6ef9-3d22-8066-3b3b80d72d2c | -16.8801 | -54.1325 | 2026-08-15 02:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 1fd138b7-377f-3eb9-bd51-eed67e007735 | -16.8994 | -54.1509 | 2026-08-15 02:30:00 | GOES-19 | PEDRA PRETA | MATO GROSSO | Brasil | 5106372 | 51 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 05c81dc4-eff1-37fe-b94a-8cdf5849b3fc | -6.1222 | -44.0271 | 2026-08-15 02:40:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 60.3 |
| b3a149b5-46d5-33b2-b158-d9c6f4794426 | -6.9334 | -43.6333 | 2026-08-15 02:40:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 75.1 |
| 8d8ed68f-4642-3e8d-a560-ddf69017d97c | -9.1219 | -46.404 | 2026-08-15 02:40:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 89e6ae8f-a402-38b1-bea9-5edf39ea30d5 | -6.6194 | -59.0609 | 2026-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.3 |
| 217f004d-1acd-3a27-b8ec-41c6927d5914 | -14.4495 | -51.9217 | 2026-08-15 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 61.9 |
| 3d488692-6514-3562-b251-14877b806616 | -6.6197 | -59.003 | 2026-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| c86837e0-a7aa-3ad1-b961-52b543e4e873 | -14.4302 | -51.9243 | 2026-08-15 02:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 76.8 |
| 992c8514-6ddd-3272-aa51-2f06364a7154 | -11.3996 | -46.3305 | 2026-08-15 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 53.9 |
| cad02b60-546e-327b-a4ab-a5f87fa2b762 | -11.4187 | -46.328 | 2026-08-15 02:40:00 | GOES-19 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 43.7 |
| 76b2057b-1e64-37b6-94d8-819cfda9dcff | -6.6013 | -59.0037 | 2026-08-15 02:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.5 |
| fc0f2f37-46e0-39d1-8121-1961c640e70e | -14.4306 | -51.9029 | 2026-08-15 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |
| 885f72ea-5a55-3330-9ed5-3097c78252e6 | -6.6013 | -59.0037 | 2026-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 52.5 |
| e556c27a-9530-3bfd-838b-1d0e97f4d92e | -6.1222 | -44.0271 | 2026-08-15 02:50:00 | GOES-19 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 74.7 |
| 2d07811f-4cd7-353e-830f-26732b93c42d | -6.6194 | -59.0609 | 2026-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 7aa00b7a-9d40-3a1e-ac78-a11f455776da | -14.4495 | -51.9217 | 2026-08-15 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 74.9 |
| a512b4df-2de6-3338-98c9-6cdffa703398 | -14.4302 | -51.9243 | 2026-08-15 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 108.6 |
| 5b90acda-e52d-33d0-84ed-8ee2663a0b99 | -6.9334 | -43.6333 | 2026-08-15 02:50:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 72.4 |
| 2ec6d73d-a633-360c-8000-967dd0c49f27 | -14.4499 | -51.9004 | 2026-08-15 02:50:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e0ecd8cc-d6a2-3d0d-a67a-098236c096ba | -6.6197 | -59.003 | 2026-08-15 02:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 47fcc03f-ca01-380e-b422-7c6845424e88 | -9.1219 | -46.404 | 2026-08-15 03:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 51.0 |
| d1f23d1e-5aff-3800-a750-49c35829176d | -14.4302 | -51.9243 | 2026-08-15 03:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.2 |
| 252baaec-45f8-37b6-abce-2edc556b7e26 | -6.6194 | -59.0609 | 2026-08-15 03:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 4a054542-0fe4-316e-b636-187f7f0b8705 | -6.9334 | -43.6333 | 2026-08-15 03:00:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 69.4 |


[Clique aqui para ver as próximas entradas](README6.md)
