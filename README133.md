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

## Dados Diários - Página 133

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 651bb221-bde8-39b2-b1b7-b346dffbbc53 | -6.7989 | -43.9008 | 2026-09-22 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 92.3 |
| 4903da15-ebc2-3d44-923b-7c86a79aea8c | -11.0052 | -53.996 | 2026-09-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 150.5 |
| e12a473a-29ea-3562-8e92-98aae00412d0 | -10.4667 | -50.3266 | 2026-09-22 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 80.2 |
| 5af87aa5-d8b5-3d2c-8da2-c6f69a121e78 | 4.0425 | -60.4812 | 2026-09-22 14:00:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 72.4 |
| a6ba19fa-d181-35a2-abc8-86e25104d41f | -13.087 | -50.6231 | 2026-09-22 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 113.6 |
| 57fed91e-7bdc-3c63-a5f6-9b74d2803611 | -6.2396 | -41.6634 | 2026-09-22 14:00:00 | GOES-19 | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 158.8 |
| c9e155e8-fc62-3da9-a1ed-faa36f9f4f4d | -12.1027 | -50.0355 | 2026-09-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 1b2c887f-4224-3990-b038-41821c555cbf | -11.118 | -54.0268 | 2026-09-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 68.8 |
| e746fa26-5920-35b2-9a96-75d2584bafb0 | -9.8404 | -46.3911 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 145.7 |
| ec902832-3f0c-364c-ab00-1091f1d10660 | -12.4004 | -47.0706 | 2026-09-22 14:00:00 | GOES-19 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 9c37f2f6-0a19-3876-879c-0068459c7a31 | -6.7464 | -59.4223 | 2026-09-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.0 |
| 8be8dab2-424c-3e31-a15f-3acff6ef16b1 | -6.2948 | -47.6274 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 401c2f28-f702-3d70-a4fa-d9725a708b39 | -6.0925 | -57.6847 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 87.1 |
| f445a687-d1b6-3963-b5cb-f0e67bb8f9ab | -3.8039 | -60.7521 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 75.7 |
| 005cec39-46ba-373e-9041-367278f5904e | -13.9311 | -48.564 | 2026-09-22 14:00:00 | GOES-19 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 01f764ff-f6fc-367f-912d-78c49128da25 | -6.2759 | -47.6506 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 1dfe045e-4188-3ce1-8ee7-689fadf15ed7 | -3.3367 | -57.8673 | 2026-09-22 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 65.3 |
| f34fb95d-e0fc-355a-aa08-a8156d1e39c0 | -10.5748 | -46.7296 | 2026-09-22 14:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 158.8 |
| 42359864-904d-3938-b452-14d01fef1034 | -3.6398 | -60.5846 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 104.8 |
| c52dc59c-d4d6-3e42-9450-ff892b85cc2a | -12.3676 | -50.1755 | 2026-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| cf921652-6f66-39cd-8277-5a6740599c9f | -9.8665 | -45.8918 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 117d3363-9abf-3dea-bfb0-e2353fbd0ba5 | -12.283 | -50.7011 | 2026-09-22 14:00:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 5fa0bd94-7ab2-32b2-bef8-511fa484d348 | -9.257 | -46.1873 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 87.1 |
| 61d677aa-0697-3510-ac08-676a583ecb14 | -10.4856 | -50.3246 | 2026-09-22 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 65.4 |
| 9eea62d5-7347-36d4-89d5-722d47979230 | -13.8952 | -45.4913 | 2026-09-22 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 313.8 |
| c05567a0-d895-351c-9311-5d87223bf830 | -11.4527 | -50.2409 | 2026-09-22 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 68.8 |
| b23b958d-2b62-316f-8680-d0efa169a158 | -3.3492 | -59.867 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.2 |
| 91fde71e-2c0b-3fbe-b510-03dde77b9ea4 | -6.1838 | -47.5258 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 92c9152f-1003-3070-9749-9ce417247f21 | -10.5908 | -53.9713 | 2026-09-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| d1416774-7dde-314f-a54c-75041b38f15e | -11.4345 | -45.3919 | 2026-09-22 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 118.9 |
| 171a211e-6619-3053-b070-2cd1a22599d4 | -9.3797 | -48.3232 | 2026-09-22 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 53.7 |
| 7ffcf2fb-88bf-3a79-8724-0ce7e2ec059a | -6.2024 | -47.5245 | 2026-09-22 14:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 56.5 |
| 1942b1aa-656d-3c21-acec-fdc73d70892a | -10.4536 | -51.325 | 2026-09-22 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 80.4 |
| e5e23159-8ff6-33fa-a36b-e79f96cd9ebe | -7.4768 | -45.4646 | 2026-09-22 14:00:00 | GOES-19 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 69.7 |
| 8d217c68-e0a6-3f91-9842-e0298fbc5555 | -11.4349 | -45.3689 | 2026-09-22 14:00:00 | GOES-19 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 143.6 |
| 63c0d948-57e9-312f-926d-a896c30ce621 | -8.7912 | -44.301 | 2026-09-22 14:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 114.2 |
| 491a0e6f-e9f6-3247-b6cd-a9b57248e165 | -7.1557 | -47.4532 | 2026-09-22 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 66.0 |
| b180047e-7a31-3174-bc98-3fa028a09f96 | -7.5704 | -57.6766 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 58.5 |
| dbd4d78a-37f2-3503-8156-61172a481ec4 | -10.6094 | -53.9902 | 2026-09-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 1de046da-c3bb-3511-9ded-78948fb4777b | -3.405 | -59.522 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 127.3 |
| 92ce84c3-36f4-3128-8f91-2836c59f7105 | -13.8957 | -45.4681 | 2026-09-22 14:00:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 146.8 |
| b8215a76-f189-3a1d-86e9-45fc37bd4d8b | -5.6007 | -48.2166 | 2026-09-22 14:00:00 | GOES-19 | BREJO GRANDE DO ARAGUAIA | PARÁ | Brasil | 1501758 | 15 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 2320671b-0017-3f18-a7b5-fa55bd08404b | -7.2994 | -59.5343 | 2026-09-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 147.8 |
| c5c69d86-6fa1-31c3-b2ab-d3e55fea94ef | -9.5353 | -47.9569 | 2026-09-22 14:00:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 68.2 |
| 4fd4377e-39f1-3181-bb5b-269925483ee5 | -11.4404 | -47.3355 | 2026-09-22 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 7df0085b-79ea-3f08-aaf3-48b0370912ab | -7.0352 | -44.6396 | 2026-09-22 14:00:00 | GOES-19 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 133.0 |
| 2c4bf7bb-bc61-38d4-a851-9c6daf709a72 | -10.7437 | -50.8089 | 2026-09-22 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 100.5 |
| 22240516-1940-3306-bc0b-7aa5b69d8352 | -10.5906 | -53.9918 | 2026-09-22 14:00:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 2b0a784b-626e-3788-bd74-cc609b308144 | -12.3297 | -50.1586 | 2026-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 226.8 |
| 48958c7a-ecd0-3f8b-91fe-29d29137304a | -6.0549 | -57.8227 | 2026-09-22 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 58e6cc7c-ce5b-38cc-8728-409fbabcf6e8 | -12.0839 | -50.0162 | 2026-09-22 14:00:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 125.2 |
| 4fdd4a42-757e-3aef-bac5-8d8207cffc99 | -4.6587 | -42.0964 | 2026-09-22 14:00:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 95.3 |
| 24a34a6f-d9e4-32de-8bbe-7c79426700cc | -7.9822 | -44.0879 | 2026-09-22 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 202.2 |
| 517121d4-d5a0-39d7-99f5-6fc1ff9f9afa | -3.478 | -59.597 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| f45e43e7-e843-3791-9f24-cbd4c07ffa06 | -9.6111 | -43.9243 | 2026-09-22 14:00:00 | GOES-19 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 118.2 |
| b1766a1f-3bfb-3a76-bed0-9909670a37cb | -7.2811 | -59.5159 | 2026-09-22 14:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 8c6624d8-154d-304b-bf7e-1ffc3b085fc4 | -3.2818 | -57.8491 | 2026-09-22 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 83.4 |
| 3783ab29-5b46-3b10-b68a-f655b91e5874 | -3.4057 | -59.273 | 2026-09-22 14:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 83.2 |
| e111cf72-d6ea-3045-b29b-df4eb3675787 | -6.2165 | -45.9518 | 2026-09-22 14:00:00 | GOES-19 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 89.7 |
| e574dd61-6455-3012-ab8b-9379c04fe550 | -3.7364 | -58.8626 | 2026-09-22 14:00:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 73.4 |
| 496391e4-995e-3102-8e2c-d54eae9ca48a | -7.9825 | -44.0647 | 2026-09-22 14:00:00 | GOES-19 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 183.1 |
| 8dac2ab8-0d49-3a8f-a7d7-26eb436ac7e3 | -12.891 | -50.9052 | 2026-09-22 14:00:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 158.2 |
| d1a0476a-d3fc-3e63-b3d8-82c6a93de167 | -8.4305 | -47.4736 | 2026-09-22 14:00:00 | GOES-19 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 54.9 |
| eb095040-264f-3e58-8c09-d8484d952e88 | -10.0484 | -52.0974 | 2026-09-22 14:00:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 70.3 |
| b1cdd4ea-917a-3035-ab77-f203b3ca399c | -3.3 | -57.8681 | 2026-09-22 14:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 107.5 |
| 57d2f8a1-501d-3efc-8ce5-4a985e5c0dc2 | -8.6169 | -54.6328 | 2026-09-22 14:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 238a67f6-b87b-3742-ba45-bccc11427f25 | -10.2635 | -49.984 | 2026-09-22 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 68.7 |
| edfaa215-7ddd-3798-b8d6-6149bdb37488 | -6.384 | -55.285 | 2026-09-22 14:00:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 104.6 |
| dca20f06-19d1-3a3c-b843-fb4b63d6ea50 | -11.4113 | -46.7798 | 2026-09-22 14:00:00 | GOES-19 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 200.6 |
| 43ee5200-a7c7-3ef5-a3bd-72e41b57440c | -11.8559 | -49.979 | 2026-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 148.9 |
| 1276c961-5f8b-3878-b731-064194b15364 | -3.6032 | -60.5853 | 2026-09-22 14:00:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 52.8 |
| 61f4ea69-f384-35be-9089-0ff6799608e7 | -12.8056 | -54.0462 | 2026-09-22 14:00:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 9c53953a-ca9c-3ea1-9747-a73e4d1e1a7e | -10.4539 | -51.3038 | 2026-09-22 14:00:00 | GOES-19 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 63.2 |
| 26c3f17e-6afb-333b-baac-c996cc52fbc2 | -10.467 | -50.3052 | 2026-09-22 14:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 199155cc-9786-3ada-9b26-3b4f3805c0d8 | -6.0172 | -45.2462 | 2026-09-22 14:00:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 93.5 |
| 5bf4f246-765d-3c7e-9f0e-af093ab7239d | -9.859 | -46.4114 | 2026-09-22 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 39e9bfd2-131d-35fd-99f1-da58162ce4fd | -9.5833 | -45.8345 | 2026-09-22 14:00:00 | GOES-19 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 86.7 |
| 0ecbb7d3-9ffa-3ec5-80bd-2754e5fcaa70 | -3.4781 | -59.5396 | 2026-09-22 14:00:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 88.9 |
| eeb3e62e-ff85-3593-83e9-10724a825ef6 | -10.7262 | -50.7044 | 2026-09-22 14:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 109.2 |
| 1263a3a7-8684-3db0-9c47-23befcf1cff9 | -7.146 | -48.4352 | 2026-09-22 14:00:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 4e32c3a3-d8c4-3082-be64-acf3fc789b66 | -13.4335 | -46.326 | 2026-09-22 14:00:00 | GOES-19 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 276.1 |
| 641d0086-1964-3a1f-bfe1-40d38e74435b | -12.3293 | -50.1802 | 2026-09-22 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 152.6 |
| 0b8ed743-7f25-35ea-92e8-e91942521408 | -11.4527 | -50.2409 | 2026-09-22 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 73.1 |
| 28503091-0627-3e42-ad12-32566c12b369 | -10.1372 | -45.541 | 2026-09-22 14:10:00 | GOES-19 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 82.6 |
| 88487ca9-8af6-399d-b3dc-5793b1764714 | -14.6878 | -45.6762 | 2026-09-22 14:10:00 | GOES-19 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 214.7 |
| e1c25024-81e6-3be6-9418-b74ce03044b4 | -6.8573 | -43.71 | 2026-09-22 14:10:00 | GOES-19 | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 95.2 |
| a31ce042-8aaa-39bf-9692-40f08b49cb19 | -7.1273 | -48.4366 | 2026-09-22 14:10:00 | GOES-19 | CARMOLÂNDIA | TOCANTINS | Brasil | 1703883 | 17 | 33 | nan | nan | nan | Cerrado | 77.9 |
| 4e4c3fff-bc50-3417-ac74-be3e963cc089 | -13.2787 | -51.795 | 2026-09-22 14:10:00 | GOES-19 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 9872b5e8-a78c-399b-b0ef-90d7b2513257 | -7.156 | -47.4312 | 2026-09-22 14:10:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 62.7 |
| 58994b9f-168f-36f2-8e63-d199ada27a90 | -10.0295 | -52.0991 | 2026-09-22 14:10:00 | GOES-19 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 88.1 |
| b98bf2b7-bc9e-3026-a3cd-49d3f5eb55da | -7.4311 | -49.8516 | 2026-09-22 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 58.0 |
| b3a9bfe1-cfb6-3ca6-832e-d58c01fc4f9d | -8.4983 | -57.6271 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.3 |
| 03bb1285-1c85-350e-8471-79321298e692 | -12.9276 | -51.0076 | 2026-09-22 14:10:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 88.4 |
| 6615795a-657a-3691-a1c7-ce5840e2809b | -3.6065 | -59.4413 | 2026-09-22 14:10:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 9747a9c7-9d91-3d25-bfa7-88326cdeaa6d | -3.7547 | -58.8622 | 2026-09-22 14:10:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 50.8 |
| 9c57ca9c-9158-3a51-a37c-b3e36250ca03 | -6.0925 | -57.6847 | 2026-09-22 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 163.8 |
| 63aa704f-d42c-35a3-847f-11b0e15ae0b2 | -4.6587 | -42.0964 | 2026-09-22 14:10:00 | GOES-19 | NOSSA SENHORA DE NAZARÉ | PIAUÍ | Brasil | 2206753 | 22 | 33 | nan | nan | nan | Caatinga | 111.6 |
| 2d8dce2f-18cb-3004-81d1-adb4d4856439 | -12.0839 | -50.0162 | 2026-09-22 14:10:00 | GOES-19 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 97.3 |
| a08bcfed-4d4e-3000-99aa-d39759d7bd14 | -5.7875 | -43.7526 | 2026-09-22 14:10:00 | GOES-19 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 81.6 |
| 31f092d0-19bb-304b-9c15-5bf7d770c756 | -8.7919 | -44.2546 | 2026-09-22 14:10:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 184.8 |


[Clique aqui para ver as próximas entradas](README134.md)
