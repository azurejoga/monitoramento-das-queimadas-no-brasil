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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 38f52a0e-a30d-3074-be12-87239869299f | -17.9613 | -42.728 | 2026-08-22 01:40:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 81.0 |
| 8ee53e69-fed5-3351-befa-f36823b0095d | -11.5868 | -46.5536 | 2026-08-22 01:40:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.4 |
| 7e255b5d-c6aa-3930-a8b0-1f759c0e1a7a | -6.9699 | -59.0658 | 2026-08-22 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 186.7 |
| a3f96239-78f7-33f0-84f3-0e89510763d0 | -6.97 | -59.0465 | 2026-08-22 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 165.4 |
| 5ed78ae8-f4e6-3392-a7de-39d91506f778 | -8.5218 | -54.8411 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 119.5 |
| 3b0c110e-7377-3af1-b352-400718f53e47 | -10.259 | -50.3265 | 2026-08-22 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 248b8b82-2e5f-3a6d-a6f8-e59518635ad3 | -10.2398 | -50.3497 | 2026-08-22 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 148.7 |
| bbf1f78c-c094-3dc7-8beb-2b2f511a8906 | -10.9624 | -51.4214 | 2026-08-22 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| e44721b3-9cf6-3883-a0a4-2a594e1c1c01 | -8.522 | -54.8209 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 228.9 |
| c4bb4ae5-7d42-36d8-8fd5-2ae7f5148dd0 | -10.9435 | -51.4234 | 2026-08-22 01:40:00 | GOES-19 | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Cerrado | 46.5 |
| dc853487-7297-3ac5-8166-862aaf171b05 | -10.2401 | -50.3284 | 2026-08-22 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 71.3 |
| e6ef2c3d-a2ad-387e-9ab7-635307030389 | -6.8188 | -59.6696 | 2026-08-22 01:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 102.0 |
| c9a0ef00-dcbc-36ed-b6ea-ff63aef63c55 | -6.2712 | -62.5231 | 2026-08-22 01:40:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 52376e0b-9628-3640-a409-8dc25d8bd9c9 | -10.2587 | -50.3478 | 2026-08-22 01:40:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 5c2449a5-1bf9-3c29-aab9-8122026e7fa4 | -8.5404 | -54.8398 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 6dd3c650-f2bf-3635-92aa-72d952e0e99e | -8.5406 | -54.8197 | 2026-08-22 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 153.8 |
| d46b2da5-3520-353f-bc00-c895f3bd49c6 | -8.9042 | -60.5385 | 2026-08-22 01:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.2 |
| e8454586-c146-3f56-876a-04adc6441110 | -17.9613 | -42.728 | 2026-08-22 01:50:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 135.2 |
| 0b1565d5-d405-380e-b7b4-030735e53366 | -11.5868 | -46.5536 | 2026-08-22 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 45.2 |
| dc35546e-6756-3b3e-98df-6d444e858121 | -6.97 | -59.0465 | 2026-08-22 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 126.1 |
| 2a658a84-9bfa-34d1-8d0c-573a1715891e | -11.6055 | -46.5736 | 2026-08-22 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 67.6 |
| f6bf1820-c4ab-3fd2-a47f-b34d57d56033 | -8.5218 | -54.8411 | 2026-08-22 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 95.3 |
| 6d29382a-dfb2-3175-80de-153fdca469e0 | -8.9042 | -60.5385 | 2026-08-22 01:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 7ab98611-f9a6-3e28-b81a-578f51b0257b | -6.8373 | -59.6689 | 2026-08-22 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 0f81eef2-3b76-3c79-98d1-549a9ba45016 | -8.522 | -54.8209 | 2026-08-22 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 193.8 |
| 0b92f195-1e00-3062-9871-8322b4026556 | -8.5406 | -54.8197 | 2026-08-22 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 142.5 |
| ebd7228c-7a42-3b08-b6ed-3a143be8d64c | -10.2398 | -50.3497 | 2026-08-22 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 122.1 |
| 9f6dcba0-a030-3a74-84b6-cc32894030dc | -13.9967 | -53.7062 | 2026-08-22 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 63bda741-e47a-3967-8042-9bdcafe0cb58 | -13.997 | -53.6853 | 2026-08-22 01:50:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 57.9 |
| 2e6ca214-1a17-3126-a147-a2eef27d4e13 | -8.5404 | -54.8398 | 2026-08-22 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 83.7 |
| 6055b463-2584-3bed-a57f-0fa06ec07595 | -6.9699 | -59.0658 | 2026-08-22 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 134.9 |
| d23ef81c-6c89-3a77-83e7-6bb64934efcf | -16.4971 | -47.9344 | 2026-08-22 01:50:00 | GOES-19 | LUZIÂNIA | GOIÁS | Brasil | 5212501 | 52 | 33 | nan | nan | nan | Cerrado | 49.9 |
| d5c0d4f1-29b3-31b9-b4cd-380129ada884 | -6.8569 | -59.4564 | 2026-08-22 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.2 |
| f8ea2bb5-2293-35b6-96d1-1ce39aaad410 | -10.259 | -50.3265 | 2026-08-22 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 36f0b27d-368e-3390-ae9c-46eaa10a1173 | -6.2712 | -62.5231 | 2026-08-22 01:50:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.8 |
| d20dce34-2d1b-3668-ab01-cae34d9f37a2 | -11.5864 | -46.5762 | 2026-08-22 01:50:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 106.4 |
| 58268e23-69d1-3a8c-86ac-c6770bc5c97b | -10.2401 | -50.3284 | 2026-08-22 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| 204aad96-d8cd-3450-8182-3ba79bd45ac9 | -10.2587 | -50.3478 | 2026-08-22 01:50:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 111.4 |
| c10e59ec-8769-328d-97fc-1259b00798ae | -6.8188 | -59.6696 | 2026-08-22 01:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 95.1 |
| 95673007-4885-3194-b4b5-c278aa40b7fd | -11.5864 | -46.5762 | 2026-08-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 218.6 |
| 13ad38f6-1a8b-343a-9c12-3ba7b5c0a68b | -8.5404 | -54.8398 | 2026-08-22 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 81.7 |
| ec18fb13-3afd-3da4-9d1a-f668b58a87e3 | -11.6059 | -46.551 | 2026-08-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 0468c83b-829b-39dd-860b-7af996d3836c | -9.1722 | -59.4629 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 218.5 |
| 32936152-b796-36e2-8687-62987aa3dc33 | -8.9042 | -60.5385 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 90cc832f-50bf-3fbc-ba68-57b54d280d88 | -10.259 | -50.3265 | 2026-08-22 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 49.9 |
| deff755e-7e7b-313b-8942-9e4c8d956676 | -6.8373 | -59.6689 | 2026-08-22 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| f45b7a7f-e00b-3180-be1d-949b6e7f5144 | -11.5868 | -46.5536 | 2026-08-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 87.4 |
| 2f5a969a-77ba-3d24-a8f2-2d8e835bd7c4 | -13.997 | -53.6853 | 2026-08-22 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 62.4 |
| b3b75ab3-006a-3611-95b7-fae2a841711b | -6.8569 | -59.4564 | 2026-08-22 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| 1c222094-0403-312b-9597-f0cf1123a6aa | -6.9699 | -59.0658 | 2026-08-22 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 120.0 |
| 73ec96d6-7222-38f1-ac3b-8c4619c36a14 | -17.9613 | -42.728 | 2026-08-22 02:00:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 117.3 |
| a3cbb29d-54cc-30ea-9a4b-af133df40769 | -9.1909 | -59.4619 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 78.6 |
| 7ad923bf-9174-3ac2-904f-69b82e055bcf | -8.522 | -54.8209 | 2026-08-22 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 179.3 |
| d75ef03a-6872-329f-a11b-7cea591a61c4 | -10.2398 | -50.3497 | 2026-08-22 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 44e1de57-bc68-3153-8f42-c7f44b683a9b | -6.2712 | -62.5231 | 2026-08-22 02:00:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| f4f85544-59f1-33a2-9090-2c2235e04b96 | -8.5406 | -54.8197 | 2026-08-22 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 445696cc-a0ea-38b1-ad6a-dadf5b5cbb43 | -6.8188 | -59.6696 | 2026-08-22 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 103.7 |
| aacd341f-7a26-3c44-8bfc-14adad098cf8 | -13.9973 | -53.6644 | 2026-08-22 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 65.9 |
| 1ea31503-2688-3d05-983b-1ce0cca353c7 | -10.2401 | -50.3284 | 2026-08-22 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| e41e2246-b7df-38fb-bf83-e32c94566a76 | -8.5218 | -54.8411 | 2026-08-22 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 86.5 |
| 1023090c-fb56-38d3-8c0f-72679829cfc4 | -9.1724 | -59.4436 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 124.3 |
| a8538c24-73ea-39af-9fa5-7367aee5ba31 | -9.1538 | -59.4446 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 2138916a-088d-376c-8889-5721b215ff1d | -10.2587 | -50.3478 | 2026-08-22 02:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 1af0f1e3-89e3-3234-ae15-854a351bde6c | -9.191 | -59.4425 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| ea13a112-180c-3132-b3fa-a695631c57c0 | -13.9967 | -53.7062 | 2026-08-22 02:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 49.9 |
| cf768abf-9d67-3b40-adcc-192807f25bd6 | -9.1536 | -59.464 | 2026-08-22 02:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 133.2 |
| 0d794b89-f347-3b5b-84f3-044d38a8fc99 | -8.9934 | -50.7427 | 2026-08-22 02:00:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| 6a2fda4a-59b2-3b24-8172-39854f835be0 | -6.97 | -59.0465 | 2026-08-22 02:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 117.5 |
| b346b89c-0a65-32ab-81a2-b6d21cf64be9 | -11.6055 | -46.5736 | 2026-08-22 02:00:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 70a7e8b2-7cb0-3992-ac6e-1d4d9e703373 | -11.6055 | -46.5736 | 2026-08-22 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 64.5 |
| 6e7a9c87-ddd1-307f-a411-924208a80f10 | -8.5404 | -54.8398 | 2026-08-22 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 103.8 |
| 56ae0d0a-a671-3736-b625-365dce051913 | -11.5868 | -46.5536 | 2026-08-22 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 57.0 |
| d71b6ffb-0a89-3fe6-89b2-3e907d5e970b | -9.1722 | -59.4629 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 231.6 |
| 01248ea5-e7ce-30cf-9944-4bd46f8e6286 | -9.1909 | -59.4619 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 90.1 |
| 04abb52e-8005-3e34-962f-07e15afdf406 | -10.2398 | -50.3497 | 2026-08-22 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| ac4f6810-11c1-3faa-8fd9-bd01e65199c4 | -9.1536 | -59.464 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 87.7 |
| 14fa5549-08f1-3c7a-b783-4ecd0f4cd443 | -9.191 | -59.4425 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 7c547992-3f02-3fb0-b0a8-074a9441f3b8 | -11.5864 | -46.5762 | 2026-08-22 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 148.4 |
| 4ecdb94a-f0fc-3339-9349-a9ca9aff6d7c | -8.5406 | -54.8197 | 2026-08-22 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 167.3 |
| 913b4771-1e53-3775-a44a-58053ff50781 | -6.97 | -59.0465 | 2026-08-22 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.8 |
| 094eb64d-2f71-329f-8d6a-7caf4051c353 | -6.8569 | -59.4564 | 2026-08-22 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 0dc1acf6-fa08-36ae-bc35-12d2853a6acd | -17.9613 | -42.728 | 2026-08-22 02:10:00 | GOES-19 | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 96.4 |
| 480fea1f-4149-3961-9b40-7fe644883e6d | -9.1538 | -59.4446 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 91bf5d54-8f5a-3b4d-8e42-5e2b52963007 | -8.5218 | -54.8411 | 2026-08-22 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 82.9 |
| 6d2dfdd4-4e50-3559-a5d8-01610853adf0 | -11.6059 | -46.551 | 2026-08-22 02:10:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 60.5 |
| 33e824ca-cebf-39a9-b8b6-03a31ebaec7d | -10.2587 | -50.3478 | 2026-08-22 02:10:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 73.3 |
| b97b07a7-96cb-3957-a800-711505c76f87 | -6.8188 | -59.6696 | 2026-08-22 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 98.2 |
| f8e1ab66-222f-330a-b21c-d01aef11d5df | -8.522 | -54.8209 | 2026-08-22 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 145.0 |
| f422a2d3-733e-3e4e-9e6e-1d4b33d28890 | -6.9699 | -59.0658 | 2026-08-22 02:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.5 |
| 1b7f3387-7963-379b-8536-1ca72e0203c7 | -5.9997 | -57.8054 | 2026-08-22 02:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 7c75d653-ec9b-37bd-8878-863fb5ce67b6 | -6.2528 | -62.5236 | 2026-08-22 02:10:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 58.1 |
| e007c95b-ab67-3852-8f17-0e845188b3aa | -9.1724 | -59.4436 | 2026-08-22 02:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 140.2 |
| f1b2f4e4-ae82-3357-87eb-f269b6331e54 | -11.59 | -46.59 | 2026-08-22 02:15:00 | MSG-03 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3ee11212-ae39-35cb-8109-12c25f5372c7 | -6.78 | -59.39 | 2026-08-22 02:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 4d93c562-5008-3aca-92de-dbfe11e45563 | -6.78 | -59.47 | 2026-08-22 02:15:00 | MSG-03 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 32cbb43f-000d-3db9-908a-e1f184c5f884 | -11.5864 | -46.5762 | 2026-08-22 02:20:00 | GOES-19 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 5059fcc1-cb6a-39b9-8143-34a2d81d7088 | -9.1909 | -59.4619 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 73.1 |
| a311dbff-abcf-3ff5-9546-a14ccbfc13b6 | -6.2712 | -62.5231 | 2026-08-22 02:20:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 60.0 |
| e11629f2-3a54-3ab1-8ef6-73f728b652be | -10.2587 | -50.3478 | 2026-08-22 02:20:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| c3a3474b-04d2-3d06-8a00-f15976c95353 | -9.1724 | -59.4436 | 2026-08-22 02:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 132.5 |


[Clique aqui para ver as próximas entradas](README10.md)
