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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 757f0287-5f31-312a-a20b-74df96377d50 | -11.9919 | -43.4627 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 736a6a80-7901-3e24-958d-31cf623fbefa | -11.6479 | -43.666698 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 422e808d-cb3e-392a-bba6-c47222718052 | -6.9604 | -45.243 | 2026-10-09 00:06:00 | METOP-B | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| c6ca5bb9-1c8b-3479-8ca5-8d252c03aa4a | -1.532 | -54.5298 | 2026-10-09 00:06:00 | METOP-B | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 97240fe5-82a7-330e-9312-dcd7d62eb249 | -3.2005 | -50.819698 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1a602b07-896d-3686-ad4f-593cb4c4edc3 | -6.6633 | -55.082298 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6d5df2d8-8f5f-384d-ad7e-3cff5a0e9e19 | -9.2234 | -45.653801 | 2026-10-09 00:06:00 | METOP-B | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| d9a191b4-8a5b-314b-a415-699efdad3f21 | -13.1736 | -54.367802 | 2026-10-09 00:06:00 | METOP-B | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 66487fdf-e005-3a0a-8bad-4c2c0cbb5594 | -2.9722 | -54.0331 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c71bed7-6aa6-323d-92a3-aa92efa52cf4 | -7.2883 | -45.410301 | 2026-10-09 00:06:00 | METOP-B | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e6b695fc-0093-3244-91ea-dff81485e09d | -3.1996 | -53.855 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 19c195db-d5f1-3294-a237-392199a5d999 | -5.6819 | -53.476398 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 18610e85-ff0e-3518-ad25-f436cce868fc | 3.7446 | -51.608398 | 2026-10-09 00:06:00 | METOP-B | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | nan |
| de32700a-e576-37c6-aff3-38e872db251c | -5.1672 | -45.603699 | 2026-10-09 00:06:00 | METOP-B | JENIPAPO DOS VIEIRAS | MARANHÃO | Brasil | 2105476 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 6f485f34-918a-3da6-b906-4415bec738da | -3.0024 | -54.076599 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7c13cba8-266c-35bf-8443-44d797ff12e7 | -2.9228 | -54.134201 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 483bb26c-cc49-313f-b635-3a1c98d054d4 | -3.0056 | -54.738098 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 35d647f8-63a8-38b9-b25c-23063c7639e0 | -3.1637 | -58.604099 | 2026-10-09 00:06:00 | METOP-B | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 48da127a-57c3-380a-9f3f-ac71d3a57a82 | -7.162 | -55.123501 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 9626405b-447a-33c0-97cb-5c2da7ce6d21 | -2.4742 | -56.083698 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ce42a5ee-e1a9-30fc-abe9-abacc37df790 | -11.6372 | -43.708599 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| f79fc940-c6cd-3acc-a939-5f300aaa4948 | -3.0609 | -53.9245 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c7a5c265-22dd-3ed5-9abe-2755524159e8 | -11.7794 | -43.525101 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 6757dc82-7c84-3653-bfee-1a5d751281ce | -2.7315 | -54.105499 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 484c591e-2630-3788-b7ee-0b7bc7362bc1 | -4.1512 | -48.547501 | 2026-10-09 00:06:00 | METOP-B | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 126dc9d2-2648-3e39-ae46-0024a63be604 | -3.9437 | -55.833099 | 2026-10-09 00:06:00 | METOP-B | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3cfcb9fd-1ca7-3e35-b4da-85f6c14abc54 | -1.3 | -54.183102 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 685c6b4b-2649-3d50-9f19-d7fc081900e7 | -11.6297 | -43.720299 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 3dd62dca-9036-3686-bc73-8f9e5fd64a15 | -11.6275 | -43.710999 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 45af8cb3-8ebe-3025-b48a-82b9736ef575 | -8.1476 | -49.4529 | 2026-10-09 00:06:00 | METOP-B | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7b3f5d3f-2e80-33ed-9291-273d54a47832 | -5.7061 | -49.086399 | 2026-10-09 00:06:00 | METOP-B | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b816c1ec-2521-3a62-8eb7-1123d31361f2 | -1.1091 | -54.1576 | 2026-10-09 00:06:00 | METOP-B | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 3265f488-b73a-3ca7-9020-b3d0c2075a9c | -5.0916 | -56.178501 | 2026-10-09 00:06:00 | METOP-B | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ab14de5e-076a-3e70-b527-a5c5c6502260 | -6.0024 | -53.4883 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6f967e45-8315-3adc-b534-9d8897e7a38e | -18.781799 | -46.464699 | 2026-10-09 00:06:00 | METOP-B | LAGOA FORMOSA | MINAS GERAIS | Brasil | 3137502 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 06b01fec-e22a-3340-9a43-414b0f866cfe | -8.7899 | -47.587101 | 2026-10-09 00:06:00 | METOP-B | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 06dd23e9-0c00-3e54-a9ce-9c6ce183bb19 | -4.9366 | -45.720699 | 2026-10-09 00:06:00 | METOP-B | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c5afb44c-347a-3563-9ef1-4c719555e3ed | -10.7453 | -46.616001 | 2026-10-09 00:06:00 | METOP-B | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 14ceb5f0-f1d9-3c76-8728-1b12dea15887 | -6.1422 | -47.916401 | 2026-10-09 00:06:00 | METOP-B | CACHOEIRINHA | TOCANTINS | Brasil | 1703826 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 3692904d-dad9-3f92-a71e-b9ec7ac06ae8 | -16.5126 | -52.59 | 2026-10-09 00:06:00 | METOP-B | BALIZA | GOIÁS | Brasil | 5203104 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 0880963c-bb58-3e03-8fdd-810f12d2c434 | -10.4742 | -47.238201 | 2026-10-09 00:06:00 | METOP-B | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9232ec53-0dec-3253-9040-c820b13c1c62 | -7.2135 | -55.126099 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4c4f8f07-761a-3556-bbe1-9d9bcb34036a | -5.6126 | -44.375301 | 2026-10-09 00:06:00 | METOP-B | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| dee589db-ff12-3628-9475-9341676d7094 | -4.6572 | -49.234501 | 2026-10-09 00:06:00 | METOP-B | JACUNDÁ | PARÁ | Brasil | 1503804 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6520f916-85e7-32aa-a7ba-5cbb79a7c6d8 | -2.4951 | -56.039501 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ca63aac-514c-3abd-a896-daa6aebddba7 | -13.7865 | -52.792099 | 2026-10-09 00:06:00 | METOP-B | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 5b3cf4f1-5e3d-3a11-bd32-41eb1ef23bfd | -4.4997 | -43.627899 | 2026-10-09 00:06:00 | METOP-B | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f9437433-01ca-3780-99fe-730d2b89c2f7 | -6.4315 | -45.940899 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bbd0847d-5376-3be2-ac4a-3b029f1fd09d | -1.9945 | -56.962799 | 2026-10-09 00:06:00 | METOP-B | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 7db0721b-38ac-3ef5-8c3a-8d2f42505361 | -6.46 | -46.019699 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 3e5d5da4-1fd1-3a7b-9879-6c637f75f5f9 | -3.8647 | -55.9856 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 67b3236f-2b6d-3d3e-ba2d-c423ce634e43 | -11.6013 | -43.688 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 63cd71d3-c3fd-3b06-b7b6-7b019d9fe293 | -2.9862 | -54.049999 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7e4b6a13-85f5-3d74-96a8-c004cd2ee155 | -6.0472 | -51.723999 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1bff00f5-f79a-3de6-9c90-f19b77331a1d | -3.7777 | -58.5756 | 2026-10-09 00:06:00 | METOP-B | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| d6dd0c87-177a-3438-b056-3444a2d15068 | -3.0156 | -54.043598 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9d077e2-b49b-3c1a-8488-af33ae9e2072 | -11.6079 | -43.715801 | 2026-10-09 00:06:00 | METOP-B | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 85940adc-bf9e-3a0c-af8b-c4978a6bdc66 | -3.241 | -54.643002 | 2026-10-09 00:06:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7893bf3-26f8-33cf-b1bc-6bd088103d54 | -10.8779 | -49.140499 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8d327817-15ea-3a7f-a48f-5651d2490caa | -7.5909 | -47.0327 | 2026-10-09 00:06:00 | METOP-B | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5577f225-6fe2-3432-adaf-4c622ab05d88 | -11.2198 | -45.314701 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 4cd5f9c2-6512-36bc-a665-3985ebbb364a | -13.6328 | -44.4114 | 2026-10-09 00:06:00 | METOP-B | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| cf18e62b-9005-3b72-b4a8-eb060872be4a | -3.3002 | -53.7066 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b2ed2be-b105-3116-b2b7-ece918a5e396 | -9.0259 | -44.369801 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| e40b11d8-0a8b-3458-b5ca-73f737761e1b | -9.8905 | -44.7966 | 2026-10-09 00:06:00 | METOP-B | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| cd83dddb-401a-3e92-8055-499114d7d70f | -2.4644 | -56.085899 | 2026-10-09 00:06:00 | METOP-B | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d595c28-001c-3fc1-ac6d-90a347dc59d8 | -7.1028 | -42.5354 | 2026-10-09 00:06:00 | METOP-B | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9c1b545c-2a78-3030-aaa3-abd6f584007a | -18.584999 | -41.493401 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DE MINAS | MINAS GERAIS | Brasil | 3161056 | 31 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1f389ba1-5f6c-3603-bc66-a4bdbdee77b6 | -6.9925 | -47.6647 | 2026-10-09 00:06:00 | METOP-B | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| e2519082-85e1-3846-9ca1-5dfaa848b6f0 | -5.8523 | -47.414001 | 2026-10-09 00:06:00 | METOP-B | RIBAMAR FIQUENE | MARANHÃO | Brasil | 2109551 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e3a13ff3-8f5d-3b04-abf9-7f8c843554d5 | -13.382 | -46.6898 | 2026-10-09 00:06:00 | METOP-B | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| 45a379c6-f1d6-35c9-8942-b69b0b82969c | -2.838 | -54.122398 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42f43fa9-2a5a-31da-ac3c-dce444ffeb95 | -10.8708 | -44.793098 | 2026-10-09 00:06:00 | METOP-B | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 61fbd377-5378-3ea5-ab7e-d4340eb77545 | -13.554 | -49.155602 | 2026-10-09 00:06:00 | METOP-B | PORANGATU | GOIÁS | Brasil | 5218003 | 52 | 33 | nan | nan | nan | Cerrado | nan |
| ac06f4ce-3fe6-38cf-8fa6-229abaa7147a | -9.6809 | -48.847 | 2026-10-09 00:06:00 | METOP-B | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 9d3c87b9-1d19-3cfc-b328-e6e63e3886bb | -3.8449 | -44.128201 | 2026-10-09 00:06:00 | METOP-B | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| bec94850-1962-3875-bc8e-15709d961f13 | -13.3522 | -43.9664 | 2026-10-09 00:06:00 | METOP-B | SÃO FÉLIX DO CORIBE | BAHIA | Brasil | 2929057 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 83d053b9-5dc3-36cd-9a21-d1e8248c46c5 | -3.2549 | -54.011501 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 30bb1cef-78ad-3760-a287-a35ffe7f0017 | -11.2002 | -45.319302 | 2026-10-09 00:06:00 | METOP-B | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 98f00012-6553-3014-882c-e475c698cf6f | -2.9535 | -49.176899 | 2026-10-09 00:06:00 | METOP-B | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 372a37e5-e349-3a9e-aba6-7f2c0ecf55d4 | -3.0985 | -53.769901 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eca85952-d47c-3fe0-973d-a341296efccc | -11.7849 | -46.7869 | 2026-10-09 00:06:00 | METOP-B | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 259307f0-b532-3935-9c3a-e326774a2696 | -3.5677 | -54.682598 | 2026-10-09 00:06:00 | METOP-B | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc472444-13c8-3c84-bb73-6c371c1dc668 | -3.063 | -53.933899 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f2828195-f39b-3174-be48-a9a74d259b5a | -3.2655 | -54.059502 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c9518bf5-e077-37b9-b8e6-8f97a1a197d8 | -2.749 | -54.091702 | 2026-10-09 00:06:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| cc2d6f90-1ae1-353f-9d48-c3d58e122b90 | -12.5324 | -48.710098 | 2026-10-09 00:06:00 | METOP-B | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 6888f7c2-31b3-3fd7-a12f-77a665dad695 | -8.7151 | -45.155701 | 2026-10-09 00:06:00 | METOP-B | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| 8808f306-1b59-372f-abb8-60a040e54c3c | -11.9964 | -43.481602 | 2026-10-09 00:06:00 | METOP-B | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | nan |
| 351bf494-da52-3c32-80c8-791b5eb5026a | -2.8401 | -54.132 | 2026-10-09 00:06:00 | METOP-B | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2c6a84c7-16d8-396c-8a0a-d335310bc58f | -9.0281 | -44.378899 | 2026-10-09 00:06:00 | METOP-B | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| aa35158e-37be-392b-97aa-6c230a7386d9 | -7.194 | -55.130199 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a9237b7-9962-3848-a634-fd3dc0898033 | -3.5028 | -60.2015 | 2026-10-09 00:06:00 | METOP-B | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 1090cc35-db09-384c-8fcf-780e09e36497 | -7.9099 | -54.7033 | 2026-10-09 00:06:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 464a9620-3432-35ac-8c9b-d80aec0db2ed | -5.9548 | -55.351002 | 2026-10-09 00:06:00 | METOP-B | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4621d370-6f7c-30fd-8dd0-03c5e08665d0 | -4.5302 | -47.044899 | 2026-10-09 00:06:00 | METOP-B | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 513255eb-8304-35f8-9221-5f8b2c57a4ab | -5.4987 | -43.063801 | 2026-10-09 00:06:00 | METOP-B | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 5531008c-d3bc-35e5-b6bd-412737ee4d2e | -3.3564 | -50.4137 | 2026-10-09 00:06:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 4d7e61a8-5b82-3434-8fa0-96ab35009e37 | -17.5133 | -43.676899 | 2026-10-09 00:06:00 | METOP-B | OLHOS-D'ÁGUA | MINAS GERAIS | Brasil | 3145455 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| e73c68fd-adf4-38a3-9053-65b955c2b540 | -3.2822 | -53.995602 | 2026-10-09 00:06:00 | METOP-B | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
