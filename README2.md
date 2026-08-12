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

## Dados Diários - Página 2

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd64bd2c-7e0c-3be3-88b4-d8e4b65f002a | -8.9602 | -60.4973 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 89.2 |
| b5c57735-e29b-31dd-a4e6-34861a3f60e6 | -11.8285 | -51.8359 | 2026-08-12 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 88.7 |
| c5e8aef5-95bc-332d-b03d-c114ac66ce32 | -8.9598 | -60.555 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 102.0 |
| eda408dc-5a13-3280-89f4-316d13850413 | -8.96 | -60.5358 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 164.8 |
| bb6773b3-4b96-3c72-ab2a-0cff8de0bbc7 | -11.4677 | -44.5791 | 2026-08-12 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 67.5 |
| 3bce1d6b-1b4f-3e1b-8f18-94a0d071bba3 | -11.8282 | -51.857 | 2026-08-12 00:30:00 | GOES-19 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 92.0 |
| aea46e21-3fac-30ca-a8f1-d467232356ba | -8.9601 | -60.5165 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 131.0 |
| 00e190e4-9a88-3879-b4dd-af202b1b912f | -13.8989 | -53.8217 | 2026-08-12 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 147.5 |
| 7c78f3c4-259c-333a-bacb-875ea7e5abec | -9.1408 | -46.402 | 2026-08-12 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 121.9 |
| 90e2a944-a82c-3897-bbbe-9827d4e4a5cf | -11.9531 | -46.3672 | 2026-08-12 00:30:00 | GOES-19 | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 95.6 |
| 6a85bbfe-62fd-3fd3-bc41-039ff651e1e8 | -8.9415 | -60.5174 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 8755f350-245d-3315-80b3-c6dece5d858e | -11.4686 | -44.5325 | 2026-08-12 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 59.4 |
| abfb1aec-ffa3-3a8a-a376-1c5cd5123128 | -11.4681 | -44.5558 | 2026-08-12 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 207.3 |
| 13581812-670d-3f85-aa84-d40c112499f1 | -13.8986 | -53.8426 | 2026-08-12 00:30:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 126.5 |
| d604b9f7-9100-341b-8fe5-4d7644be7564 | -11.4873 | -44.553 | 2026-08-12 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 90.7 |
| d2d83bfe-e41b-3e06-b932-24b89c167fb7 | -8.9414 | -60.5367 | 2026-08-12 00:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 83.0 |
| 3c9dbbbf-8aeb-3e7d-9b89-278e7e266116 | -11.449 | -44.5587 | 2026-08-12 00:30:00 | GOES-19 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 61.2 |
| 2700bc65-3429-347e-8d93-0e9c8ce49ff3 | -9.1411 | -46.3796 | 2026-08-12 00:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| 6e402b7a-0cb1-3c34-9ef4-72b85b5f2ae5 | -12.84864 | -52.04227 | 2026-08-12 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 21.2 |
| 39bb7aeb-5823-3848-809e-b237ad7ba508 | -14.35229 | -54.88005 | 2026-08-12 00:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 312b6ba2-2918-3f81-92ad-cd9245e7f7b2 | -11.7877 | -51.86895 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 263c4f9a-b18e-335c-9446-698a69c56dd4 | -12.46876 | -51.28714 | 2026-08-12 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 9.0 |
| e60d3b47-989d-31e3-bcf0-25f46b024abf | -13.88202 | -53.82391 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 19.0 |
| 9fe00420-2659-36b3-9375-805a47739cbe | -12.40991 | -51.17987 | 2026-08-12 00:30:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 30591e5c-aa29-3b87-85c8-189e06cbd713 | -13.89889 | -53.80557 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.1 |
| 4fbd4120-9d40-3cfd-8f0d-c0cafa3747d5 | -11.8277 | -51.86264 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 0dc8ddf4-eca3-3cc5-8c72-06c827dda4bc | -10.105 | -46.232 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 64.7 |
| d5d9baa1-f6c1-36ad-ba1f-95ccef0e4f46 | -10.09095 | -46.2067 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| ac58afeb-d952-37cb-a0d7-1adadc0a6482 | -11.60372 | -54.66867 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 8.4 |
| fd31bea4-f476-3ffd-97bd-0e5ab463922d | -14.35715 | -53.20892 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 4dbd1053-540e-3739-beb3-64f8946ba3ab | -11.98353 | -46.36583 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 31.1 |
| c300d09a-8aab-33e6-9de9-fbebcc02898b | -11.81419 | -51.84066 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 122e083e-e8a7-32db-8e5a-9f11ac904364 | -10.83981 | -50.35617 | 2026-08-12 00:30:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 18.9 |
| a15c9d1f-ec75-3565-bcc2-bb9b8e47b22f | -11.46216 | -44.5926 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 56.9 |
| 6dd09b9e-8da2-335c-b7e5-4cd082cf552b | -13.82856 | -53.83192 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 8fd6df64-ed7e-3342-8de4-87e4a595d129 | -13.8655 | -53.83575 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 6b05d81a-05a3-369b-aef1-9a4233be850e | -10.09654 | -46.23996 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 48.8 |
| aaabdaf8-ac37-36cb-aaa7-ea0ba9d74cd4 | -11.60247 | -54.65965 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 4486f233-97d7-3758-bff8-4f6203f21b65 | -13.89392 | -53.83456 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 54.3 |
| 0e038e9c-c53d-34d3-b8e6-00f396a9c20c | -11.47197 | -44.55401 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 321.2 |
| 4682de5d-c203-33db-a57f-fb495077947c | -13.84115 | -53.79234 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 50ce4d7d-443d-30c0-b6f0-76fe1639e63a | -11.80516 | -51.57094 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 51b72266-b732-3d5a-b741-949837efeab4 | -14.42255 | -53.02556 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 6ba6197d-5240-3554-8542-d12b0ab37379 | -12.86002 | -52.05176 | 2026-08-12 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 8.6 |
| fa16d7ee-7fb1-3abf-9a7f-c9e1d6d9b724 | -10.09902 | -46.19774 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 46.9 |
| 727ffb28-29f6-395d-a9d6-6e97e51c7aa7 | -14.35855 | -53.21848 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| ca4434fb-c694-3f1b-a51c-b057d7c3056c | -11.82945 | -51.87441 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 51.2 |
| be08f6c2-5709-38b3-93de-cd754682d6b9 | -13.90282 | -53.83319 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 166.1 |
| baaabe46-bd95-35fb-a9a8-2639f5258476 | -14.73343 | -56.35646 | 2026-08-12 00:30:00 | TERRA_M-M | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 6.9 |
| 93fe24c4-f0ad-3d74-88a8-adf8de335ff4 | -10.64009 | -47.481 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 42.6 |
| e3186d0a-521a-3474-980b-73fa6088ea4b | -13.83617 | -53.82145 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 81a10fd7-6d8d-37f1-a262-13c5a3c0051d | -14.33876 | -54.05216 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 18.6 |
| d1cfa79b-27a8-3048-9c6a-fceba367520e | -11.4941 | -54.60773 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 16.6 |
| 38893eaa-de5f-3786-a74a-3ddcd9d3e371 | -13.89626 | -53.78714 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 82fabf26-5514-3cc0-b530-ad7f0db005cd | -11.81242 | -51.8288 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 11.1 |
| b9de447f-3860-3633-b274-4ff9aa85f412 | -13.90413 | -53.84241 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 15.3 |
| 4685d2ad-2a58-3dca-bb93-d57f8889fbd2 | -13.89759 | -53.79642 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 9950f328-e035-38f9-81c6-0358da7eb2a3 | -14.42114 | -53.01593 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 00edfd4c-ccf6-3a56-af26-b745dc0a4702 | -12.32346 | -53.18192 | 2026-08-12 00:30:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f8e60aea-8728-3607-afd4-8c0b49906f95 | -10.64439 | -47.50681 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 25.0 |
| 939a27f2-efc3-3994-b8d1-423a04c0cc0e | -11.45438 | -44.55027 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 662a819c-0958-3277-a167-71df479e4b31 | -11.47942 | -44.59641 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 86.5 |
| 8b79c0fd-e132-3047-a9af-375fdd08cc95 | -11.9525 | -46.3679 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 156.3 |
| ab774004-05b3-3507-a435-3a8747e44bb8 | -14.55607 | -50.39318 | 2026-08-12 00:30:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 19.6 |
| a1925f4c-dcaa-3cf8-b552-e5962149a18f | -12.8503 | -52.05335 | 2026-08-12 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 54508d0b-9956-3f09-b314-6f7010f8c004 | -14.36619 | -53.2075 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9f9234ee-e916-3710-8592-539e44953688 | -14.55815 | -50.40663 | 2026-08-12 00:30:00 | TERRA_M-M | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 51.7 |
| efbb2888-aba5-302e-b821-2a650d49ecd2 | -11.98815 | -46.39326 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 34.6 |
| 66fdd769-dbd9-38b8-9cb9-ff19810b5802 | -14.43023 | -53.01449 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 05c22455-2611-36eb-887f-4e4afdb59e61 | -11.9493 | -46.36168 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 183.4 |
| 5e3fdc1b-094e-335f-8809-a5d38478ad4c | -14.32864 | -54.0444 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 870629f1-e167-31f6-b407-762fb8956042 | -11.78593 | -51.85727 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 26.4 |
| f55c2a93-f93b-3ad8-b7fe-988735bd71e6 | -12.85837 | -52.04064 | 2026-08-12 00:30:00 | TERRA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 0750890c-ee9f-3b64-8855-d872f36489c3 | -11.45449 | -44.55739 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 112.9 |
| dfae6dbd-8e70-3ca3-b8ca-368fdf564cc4 | -11.78413 | -51.84542 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 13294986-d391-3a8f-a83b-cecb5abc52c0 | -11.60121 | -54.65062 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e4131ddb-2529-3813-95b8-9ec17ebc4dfd | -13.88735 | -53.78848 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| f974e85b-3ab7-3373-a26e-b124d54e3457 | -13.83983 | -53.78304 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 16.5 |
| 1271eb4e-cd84-37df-a290-49f2069c7d77 | -11.97285 | -46.39537 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 72.8 |
| ffe1666e-654e-3db0-a460-6ce7888e0dca | -14.33748 | -54.04303 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dd5493fc-7591-32be-bac1-326306b0b81d | -12.32491 | -53.19177 | 2026-08-12 00:30:00 | TERRA_M-M | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d7b2181a-1e23-3ea6-a351-609ada4542a7 | -14.36133 | -53.23758 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 90.2 |
| 61609c5e-5110-3d29-b626-f4d1393efc4b | -13.84247 | -53.80167 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| bf3f316e-a0c4-39b6-8fd4-07a9c760ee2f | -11.61364 | -54.6609 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| dab582ef-6df9-3d6f-b016-a438d628031b | -11.4796 | -44.58929 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 154.4 |
| d9068e6e-2dda-3d33-9d98-ec32c34322db | -13.87312 | -53.82532 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 7.2 |
| e15b0607-b4a6-3135-a8f3-b71806eeef00 | -11.94754 | -46.33886 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 103.1 |
| bc8b4748-946f-3b59-8417-0c19ecd80a73 | -13.9002 | -53.81477 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.0 |
| 788fd3be-f989-3ed3-b738-775ba9e60567 | -11.61238 | -54.65187 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 29ca98b9-aaf4-3548-a4c4-5f796e594d49 | -11.82421 | -51.83912 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 100.1 |
| 0914765f-32c3-353e-8b73-b0df060eb266 | -13.83747 | -53.83059 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 611f5b50-6278-3225-b63d-b40b5b17a20d | -11.98518 | -46.38701 | 2026-08-12 00:30:00 | TERRA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 56.8 |
| 04e81a7e-a6ad-380b-a55f-a94e9303faf5 | -13.90151 | -53.824 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| 88f397b0-2c2d-3c0a-9da5-c540681d85df | -14.35105 | -54.871 | 2026-08-12 00:30:00 | TERRA_M-M | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 19.9 |
| 06f464fc-8bd2-3f4e-8164-3329fe46ba77 | -11.82596 | -51.8509 | 2026-08-12 00:30:00 | TERRA_M-M | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Amazônia | 106.0 |
| 7aa7db1a-cebb-3f9b-a01c-02a72fc91c26 | -11.49284 | -54.59869 | 2026-08-12 00:30:00 | TERRA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 65c266f0-9213-3e39-a97b-27c45599f427 | -11.47188 | -44.54695 | 2026-08-12 00:30:00 | TERRA_M-M | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 218.9 |
| 1029c0b9-d29b-3812-8483-403cb4c4dfd5 | -14.36759 | -53.21711 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 48.7 |
| f9f34c96-586f-3390-869e-41181919e24f | -13.89262 | -53.82544 | 2026-08-12 00:30:00 | TERRA_M-M | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 25.6 |
| b7ba6327-b110-3ebe-97ba-802916f1677b | -14.35994 | -53.22806 | 2026-08-12 00:30:00 | TERRA_M-M | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 63.9 |


[Clique aqui para ver as próximas entradas](README3.md)
