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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ef35c07a-fc38-326f-919f-af4e03609a63 | -2.9417 | -54.140598 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46461534-8da4-3082-835d-ae4d518f3d30 | -3.2938 | -54.0112 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bc451309-9d46-30dd-80e0-45152237b43c | -10.3054 | -46.613899 | 2026-10-08 00:26:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 75eb9c13-cd7c-38c6-a3ec-b4bd45476942 | -7.2339 | -55.171001 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8e7f0097-4ebf-378c-bae7-6a43f89d9508 | -2.7592 | -54.1087 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 76796fd1-168c-3053-8e61-40d7c956c9f8 | -3.7423 | -59.462399 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 9b87ad8f-8551-3aed-b074-ce0b3815a811 | -9.8941 | -44.803799 | 2026-10-08 00:26:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 6c4c8fb4-f094-3190-88cd-b913f336a643 | -5.9626 | -55.334499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 934e1365-fbb0-380c-bba5-43c3bf805f17 | -3.1475 | -53.729599 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 723354c0-edd0-3534-8ce4-6a3dbc94ac64 | -2.769 | -54.106499 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 8f5ac843-5ced-3393-a673-0b21c563b3e9 | -2.3901 | -56.124599 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b649df56-7b01-3070-8634-2cf4224da424 | -3.5327 | -54.655899 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 46fea9ac-d386-3529-80f9-d36bb3444ef0 | 4.3178 | -60.345699 | 2026-10-08 00:26:00 | METOP-B | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 79fc8690-5995-3025-bb76-a00118dc12f9 | -4.1202 | -54.2453 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 36af0dd6-f59a-3a33-a9c0-63d2fc0e7954 | -3.2313 | -54.371799 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2efc9e15-5729-3297-b15a-56d87feeba2d | -6.2119 | -52.876598 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4a1f1e32-08ce-35ba-a23f-d2ef3c2d2e13 | -6.1912 | -53.148201 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 442fd9b0-3fe7-3ee2-8dce-93ad326ef9ea | -4.1192 | -59.870201 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| bb83902a-a627-3f0a-9f09-688fa59e6122 | -2.9432 | -54.147499 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e7ad38db-b8d1-318f-9bf6-66f48bbcef7d | -7.2142 | -55.175301 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 104b2435-ea26-300e-896f-09d83a6702ff | -5.2408 | -50.896999 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 48bc702d-f1ad-36b3-8d94-1a09e2ff1c64 | -3.3241 | -50.185799 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c316b7f8-d8f3-3b8f-a4e5-b757dec51e26 | -1.4578 | -54.780899 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1178c2fa-3b5a-3736-9383-22a191ab467e | -3.701 | -50.6572 | 2026-10-08 00:26:00 | METOP-B | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0e87a75-d602-37d7-9922-ba7f6501bf3f | -6.7284 | -55.1208 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 485cd566-9211-3561-ba76-520404dd9dbb | -2.8456 | -57.465302 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| ff7957bd-ec26-3dab-8544-dd68dbe68090 | -2.4675 | -56.0564 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3073ef56-bc47-350e-92d2-4f311cc87b62 | -1.2813 | -55.4133 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bbfcc1ee-22df-398a-ac5a-ad95a5a306d7 | -2.5644 | -56.1665 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0741b3c0-c637-36d7-97ec-a1e98fe977f6 | -2.3689 | -56.122002 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7fbc092e-0a53-3d77-8fee-64aa1bbe3322 | -3.688 | -55.481701 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9268aab0-66d4-3c80-a4fd-d72ab97b67ce | -6.4642 | -55.459801 | 2026-10-08 00:26:00 | METOP-B | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42d3cad4-489f-3ef7-8e79-d0a7cfd4bae7 | -6.6326 | -43.729801 | 2026-10-08 00:26:00 | METOP-B | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4ecbf9a9-3bf8-34a7-8016-708a4f04191f | -9.2071 | -57.721298 | 2026-10-08 00:26:00 | METOP-B | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 35753a19-655d-3045-8fcc-f456e5247679 | -3.3257 | -58.140301 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1f2b5b9b-fa28-36aa-b8f4-ee88abaafe1d | -1.526 | -54.5355 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a327c769-531a-39f2-9124-6c135b7b2cc3 | -12.2013 | -48.414902 | 2026-10-08 00:26:00 | METOP-B | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 67cd887c-9eb6-3522-92ac-f6bedfa52e6d | -3.8481 | -51.921101 | 2026-10-08 00:26:00 | METOP-B | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f7867542-ee4d-33aa-aad7-55a41ecb4a2e | -3.0778 | -54.240398 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7cf63164-8e45-3e61-87b8-1d06b74ee665 | -3.5895 | -54.6791 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 31bc75b8-e961-363f-a097-49864d15927c | -3.039 | -54.2057 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96739d1b-670c-3a61-96e5-3592875cf3ce | -3.0174 | -53.8834 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5c5acb76-117b-3ad6-9a9f-04e31a724c28 | -3.9622 | -59.994801 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| dd78a1ed-8137-3d25-bd9c-712edfb03295 | -6.8892 | -43.690601 | 2026-10-08 00:26:00 | METOP-B | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 3ebfb7f7-bb37-38ba-801d-2534f8cad35f | -2.7757 | -54.0905 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 543191d9-c88f-3ce0-853d-280e3210b6e5 | -2.8637 | -54.114498 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67385399-e06f-318f-b846-6e93d35b9f49 | -4.0637 | -55.319099 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3f63c347-df35-31e0-8679-7674e46cb8f1 | -3.0078 | -54.067799 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bee7810f-5fa3-3385-998a-75c63546033e | -3.0627 | -57.745499 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| fe302c45-0539-3192-bf49-df913e5558aa | -3.3294 | -58.157001 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d2c81d61-fe34-33bf-b655-94572bf6344f | -3.0244 | -54.187199 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9ef936fa-6732-3607-8eb9-c9d96a98a7cb | -3.2431 | -56.803398 | 2026-10-08 00:26:00 | METOP-B | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 3c7d9cff-5f2f-3f34-b494-560b5471c18a | -2.4769 | -56.098099 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c857901-4ee5-30d5-885d-70b31e7cd2e4 | -2.5824 | -56.155201 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fcff53cc-e9a4-3022-983f-42c329a6f211 | -3.0108 | -53.899502 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bda0aad6-9c7b-35b3-b27a-c8bbd86911f4 | -3.3032 | -53.870701 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1e21a114-55f4-38be-aea9-0909de567678 | -14.5874 | -54.335499 | 2026-10-08 00:26:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f103719f-b3a1-3bcf-9e1f-4aa03b5ec23b | -3.8494 | -55.970699 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| acee2316-ed76-3bb0-ab33-79f1b4233c9d | -7.8881 | -55.0112 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97237317-3cdd-3474-a64f-cfc533e59d07 | -2.998 | -54.753502 | 2026-10-08 00:26:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37b8c56-2c0e-31d3-95e8-ae7912537d94 | -7.1919 | -55.121201 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f414f821-2b50-3d2e-9f82-3ff3d7e24ea1 | -6.2121 | -52.7868 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c0f16745-0c9a-3d04-9996-8d7be61283f6 | -3.7225 | -54.219002 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 01f09d50-0c7a-3919-99f8-27a03083246d | -3.9178 | -59.095901 | 2026-10-08 00:26:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75eab0a4-7fba-3e7f-b001-55591127e293 | -4.5125 | -44.0485 | 2026-10-08 00:26:00 | METOP-B | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5da858d4-7331-3dca-8360-63388b25ed07 | -1.5291 | -54.549301 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7be32f30-c417-3811-8b92-024bf2184fc3 | -1.4531 | -54.760502 | 2026-10-08 00:26:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 061ad17a-91b8-3d9f-96e5-430c1df005d3 | -2.7599 | -57.6796 | 2026-10-08 00:26:00 | METOP-B | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d274ef0c-5e1c-3d01-b904-3c83a59fe755 | -3.1662 | -58.6245 | 2026-10-08 00:26:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 2a516a1a-efed-3dd4-a0af-b2ea78349010 | -3.7356 | -59.4324 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 75fba49f-6629-3d44-9f61-9e7de4f77017 | -5.6812 | -53.490299 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 407dd32b-73cd-36ba-af6d-75c46359a42f | -2.8786 | -54.089298 | 2026-10-08 00:26:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| afba5911-05ee-3407-87ac-7a6490072754 | -7.8866 | -55.0042 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fa5a5264-5889-33bc-a810-f0301e83be31 | -4.1439 | -54.031101 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 34f4bb8f-1812-3cf8-8624-b15e3cf5904e | -7.2166 | -55.093601 | 2026-10-08 00:26:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a6e634b5-0de1-31af-b800-dd7aee88973b | -3.0015 | -54.0401 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e944d9be-e840-3fa0-8bfb-2cb5eaf4c8be | -2.9495 | -54.175098 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f848b250-e177-355c-bbe4-d08e4ed2bc55 | -6.3382 | -55.310101 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 090fe793-d87a-3fb5-a252-cdc3ddb2b28e | -4.0652 | -55.325901 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2548cedc-d011-3513-8afd-650b42796e1f | -2.9526 | -54.188801 | 2026-10-08 00:26:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fc98b8d5-ab12-3dde-9dcd-3e071cde412d | -6.1312 | -53.0658 | 2026-10-08 00:26:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| bcc64a21-976f-3172-b924-f7fbb2c83dd2 | 2.8914 | -60.452702 | 2026-10-08 00:26:00 | METOP-B | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 0cb33004-b475-3221-b859-74a38ba7e98a | -3.3339 | -52.5117 | 2026-10-08 00:26:00 | METOP-B | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d37d3fb7-670e-3e4f-a5a9-53d461ce7f48 | -2.5122 | -56.1633 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e28088ec-305b-3e06-8da2-9d813e7f8163 | -4.4482 | -54.967701 | 2026-10-08 00:26:00 | METOP-B | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69c6853c-ad80-3302-a7f2-0b0fba871324 | -3.264 | -54.061298 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 02ed9a77-121f-31b4-b861-dab480c47252 | -5.9544 | -55.3437 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc74c60f-c4d2-3afd-8706-4e8d1902fe95 | -4.3665 | -54.742199 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9e3b8d49-4e5a-36b3-8b30-710fb094606c | -3.2209 | -53.962002 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 96807a1f-9280-3546-8c16-68015b5eda76 | -2.5758 | -56.171299 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 91a917f8-b6f4-340b-86d6-4c92d8b74858 | -3.5233 | -59.354 | 2026-10-08 00:26:00 | METOP-B | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 5df09b6b-4e68-3251-a860-8c026e9b569f | -3.9741 | -56.113499 | 2026-10-08 00:26:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 05a5a729-db7c-3097-960a-97da237922ff | -3.5844 | -54.565701 | 2026-10-08 00:26:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ee97aaa2-d5b6-393e-92c0-0ed472ad3036 | -3.8412 | -55.9799 | 2026-10-08 00:26:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 24e00cc1-f2fc-35fa-b10e-b2fbf8eeca2a | -2.9441 | -54.0602 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4507df05-aafa-3e91-9303-7cf5a632a588 | -2.8393 | -57.4828 | 2026-10-08 00:26:00 | METOP-B | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 03cf0019-5847-3ef3-babb-b97079623dbe | -3.2825 | -54.006401 | 2026-10-08 00:26:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| fdaf6b45-8bc8-3da5-8549-6d78d1ff0a6e | -2.5016 | -56.070702 | 2026-10-08 00:26:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 579b5129-cc50-3e18-9175-555fff89ae5a | -16.416201 | -51.860699 | 2026-10-08 00:26:00 | METOP-B | PIRANHAS | GOIÁS | Brasil | 5217203 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 11c9469c-d9be-3ee8-82a8-f19c6d7288ef | -9.587 | -47.771301 | 2026-10-08 00:26:00 | METOP-B | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |


[Clique aqui para ver as próximas entradas](README15.md)
