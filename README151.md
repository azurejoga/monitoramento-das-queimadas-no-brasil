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

## Dados Diários - Página 151

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ec07c7ad-1c0a-3c8d-9872-5c2bed2fd19e | -6.1653 | -47.5052 | 2026-09-22 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 77.6 |
| c1bdce34-9695-3603-a2eb-8efcb5d19f0f | -3.6763 | -60.5839 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 120.6 |
| 6107537c-1af7-3739-85e4-0e6809c10e64 | -2.9723 | -57.214 | 2026-09-22 15:30:00 | GOES-19 | BARREIRINHA | AMAZONAS | Brasil | 1300508 | 13 | 33 | nan | nan | nan | Amazônia | 62.5 |
| 1151ec05-1963-3917-a715-2bb325729913 | 1.4001 | -56.0634 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 49.7 |
| d67a0319-bf07-3f39-a42a-380e87892f4b | 4.1314 | -61.3134 | 2026-09-22 15:30:00 | GOES-19 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 69.9 |
| daa488a3-a3a4-3a90-804d-b49723fec8f7 | -6.6782 | -58.4584 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 42.5 |
| 72a1b526-8cf8-3e57-9482-94c213400d4d | -10.744 | -50.7876 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 103.4 |
| 8fa67dd9-8614-30bc-af5e-f51d53cf127b | -10.6875 | -50.7722 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 97.8 |
| d4ba5bad-5a80-3394-bdfe-cf769a5dac43 | 4.0595 | -60.8795 | 2026-09-22 15:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 0ea5aca2-d728-31b3-a237-a13086d4998f | -3.2818 | -57.8491 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| a0630e1e-1bd7-3b3c-a9dd-4e4f962e743d | -7.0428 | -59.2173 | 2026-09-22 15:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.2 |
| 9a264806-9aad-3ef0-9f44-b1c3377519b9 | -3.6764 | -60.5649 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 112.3 |
| 5f6265b9-59e4-3fee-94d5-49a54bd33049 | -4.2042 | -56.3412 | 2026-09-22 15:30:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 191.3 |
| 3cbb4718-69b9-38f2-aeec-31f79f4df5e1 | -6.737 | -55.0674 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 1f06e627-22eb-3c1e-92be-2b5212138a60 | -3.132 | -59.0482 | 2026-09-22 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 77.5 |
| a712ac8f-c1ab-3697-90f8-65f3a2d0ca8d | -6.3195 | -60.0147 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| 556da9b2-9d56-3fa2-928c-58e9caec243d | -11.44 | -47.3579 | 2026-09-22 15:30:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 166.0 |
| 133fe35c-132f-3247-b9b8-037da25652ad | -3.0582 | -59.2797 | 2026-09-22 15:30:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 49.7 |
| 1a1aabba-6b96-3b24-941a-e024f7993b72 | -3.1357 | -57.697 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| 6f936989-cd63-3943-a12b-cc3ff83c614d | -11.3976 | -44.2167 | 2026-09-22 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 305.8 |
| 5540a3ce-2b8d-305f-a7de-623ef46ecd0e | -3.1096 | -60.6892 | 2026-09-22 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 49.5 |
| f7add520-e9d0-3118-9804-c5ca4dc451cb | -3.6997 | -58.9019 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 07d1667c-fa4d-33e3-a0cf-188cbfb351f7 | -13.9448 | -47.8494 | 2026-09-22 15:30:00 | GOES-19 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 156.8 |
| 3c45a877-232c-3f94-a3b8-f1fe165d2653 | -3.6452 | -58.7685 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 54.3 |
| 5ed8f81a-8bab-3e82-aecf-d71969fa7fce | 1.5836 | -55.7856 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 57.9 |
| ad6e1f13-e9cb-3edb-b1ac-2fb85c3baa4b | 3.9716 | -59.7393 | 2026-09-22 15:30:00 | GOES-19 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| a65e0d20-2810-37e1-941e-57a952db0c6a | -2.5687 | -57.5135 | 2026-09-22 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 110.7 |
| ff8e3fe3-c47d-32d3-b3b1-08dde1c4b4a0 | -2.9997 | -60.8047 | 2026-09-22 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 58.3 |
| f0540595-18d1-3635-8fc4-8bff00d4be23 | 2.4397 | -50.9344 | 2026-09-22 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 645ca25f-25d3-3206-8020-f3df8454d09c | 2.4028 | -50.9561 | 2026-09-22 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.0 |
| cb09564d-86cb-3778-bbc4-6c73b2a290dd | -6.3135 | -57.7342 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 92.1 |
| e2ef637d-28d0-3f5a-8f5b-10b9bbedf9f1 | -6.3567 | -59.9559 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 43.1 |
| 32654e0d-639a-3f42-ad42-9a9fc8c456c9 | -7.9172 | -61.329 | 2026-09-22 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 861d8fd1-c5fa-3762-9ed2-748d3cc36898 | -12.2827 | -50.7226 | 2026-09-22 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 103.3 |
| 049ed8dd-ddac-39c6-a6ce-92498c1ae7c6 | -10.336 | -50.2119 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.7 |
| bae2707e-07e7-3a59-afd3-31e831b7254d | -10.2982 | -50.2158 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| f15cc28b-1892-3f8d-8de2-aa13819616e1 | -2.4206 | -58.2712 | 2026-09-22 15:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 62.1 |
| 2d018010-7e53-39e5-8051-d3c2abdfa535 | -11.3784 | -44.2195 | 2026-09-22 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 578.3 |
| 6cf79df1-cf97-32ad-bed8-a295cdd5b93b | 2.2187 | -50.8769 | 2026-09-22 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 81.4 |
| dee5cee5-4a6d-3807-8087-37236687caf4 | -6.0926 | -57.6652 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 107.4 |
| acdfc16d-1ed9-3cbc-b834-1601f65bfc56 | 1.9977 | -50.8605 | 2026-09-22 15:30:00 | GOES-19 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 66.6 |
| 1f76de34-e80a-3446-a8a9-62ab55ee4688 | -9.247 | -57.1488 | 2026-09-22 15:30:00 | GOES-19 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 139.6 |
| 2f9d7e22-1bff-3ee0-90b2-5810f743f031 | -1.0244 | -48.8087 | 2026-09-22 15:30:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| cec1bd4d-898b-3fd9-bd53-e25563317430 | -2.9525 | -57.72 | 2026-09-22 15:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 95.3 |
| df1c9404-f531-34f3-87c5-15a65657b5b9 | -8.7706 | -45.8567 | 2026-09-22 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 15d8874a-1d60-3696-a0b2-90ab230fae79 | -9.8404 | -46.3911 | 2026-09-22 15:30:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 96.1 |
| 97d7241d-a5c7-3254-be44-c40084040f64 | -8.845 | -45.9391 | 2026-09-22 15:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 54.4 |
| b9b38b35-5fa1-398d-bbc5-d07142aca388 | -3.6066 | -59.4221 | 2026-09-22 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.2 |
| 09240c92-b8c8-3203-b625-2017a0988b5b | -12.3206 | -50.7394 | 2026-09-22 15:30:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 114.0 |
| 3b6b1fc3-7a3c-3fa6-b424-094a0f4fbe00 | -3.3492 | -59.867 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| 2293a3ab-8ca7-308f-bfb8-61a01a31f195 | -10.5748 | -46.7296 | 2026-09-22 15:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 120.1 |
| 7b48ad03-a228-3677-9d3b-ca5d9f558abe | -3.2211 | -53.9623 | 2026-09-22 15:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 55.5 |
| ac936d66-9c6b-3843-bcc1-9a3e5b9e8825 | 2.6715 | -60.6012 | 2026-09-22 15:30:00 | GOES-19 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 90f80bb6-6a92-3324-bbeb-002a03c2aa77 | -6.1111 | -57.6645 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 187.2 |
| 9bf0ae07-758f-3ded-b1d7-cac30ed55cb4 | -2.5873 | -57.3965 | 2026-09-22 15:30:00 | GOES-19 | PARINTINS | AMAZONAS | Brasil | 1303403 | 13 | 33 | nan | nan | nan | Amazônia | 46.3 |
| aa6970d7-db9e-3c89-b37e-87308bfb06a8 | -3.3139 | -59.3898 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 44.6 |
| 624d1a95-defe-3d11-a698-65719ed1e1fd | -10.6881 | -50.7297 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 118.3 |
| 8636fe79-d59a-3df4-bbe5-3019ccf0c1a3 | -6.0925 | -57.6847 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 232.9 |
| a9080edd-764b-349a-8fb7-2a8abe34336a | -1.9484 | -56.5868 | 2026-09-22 15:30:00 | GOES-19 | TERRA SANTA | PARÁ | Brasil | 1507979 | 15 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 85978880-1b48-3489-b8cb-4a9e072de731 | -12.8 | -44.2073 | 2026-09-22 15:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 129.1 |
| 523753e2-63e1-3d8d-9a02-68d091aaf31d | -9.3797 | -48.3232 | 2026-09-22 15:30:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 86.6 |
| 3d4e8156-d0e3-35d7-9108-54073fd02e0e | -3.1901 | -57.8704 | 2026-09-22 15:30:00 | GOES-19 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 63.0 |
| 76ed5e49-ee0a-39b3-b446-17c07e1a7a6c | -6.0993 | -59.9076 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 61.5 |
| ff295524-092c-3b48-ae79-8f338af95f8a | -6.5763 | -45.4968 | 2026-09-22 15:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 98.6 |
| 56b8e986-6dc5-300c-9e84-ab1c6ebf6e06 | 4.096 | -60.9167 | 2026-09-22 15:30:00 | GOES-19 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 23fef5b7-8e64-3fed-a380-a55ab9f64b31 | 1.3634 | -56.0638 | 2026-09-22 15:30:00 | GOES-19 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| d7a50a91-06d0-3d93-8269-e4e6d359dabd | 2.4027 | -50.9769 | 2026-09-22 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 59.8 |
| b87d0026-8557-3d80-b832-eadbf1be4c1b | -3.6447 | -58.9224 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 92.4 |
| d65610a9-b55a-3ea6-9dad-75fe901fc7c4 | -6.3501 | -57.7717 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 998e8089-ed6c-3b2a-b05c-56d94adf44da | -2.4023 | -58.2715 | 2026-09-22 15:30:00 | GOES-19 | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 834970d6-135e-31d0-9dbd-b4d23ea8911e | -3.3183 | -57.8677 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 67.4 |
| 2ab159f0-a3d9-3cea-8656-f3f45f00c66b | -10.8343 | -54.0933 | 2026-09-22 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 087d9954-142f-32ed-a639-2838be1d8cbb | -6.3382 | -59.9566 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 15c87fbc-ecd1-306b-b24e-aae1c523b507 | -7.6942 | -61.5473 | 2026-09-22 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 07134690-1dd8-3da2-a46e-55d977121fc7 | -11.378 | -44.2429 | 2026-09-22 15:30:00 | GOES-19 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 136.4 |
| d4bc9352-129a-3df8-9f03-2cbe86486aa8 | -8.0092 | -61.4015 | 2026-09-22 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 56.8 |
| 2fc7ab78-061c-34cb-89d9-af4add561674 | -6.4855 | -59.9704 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 41.7 |
| 67f5c01e-1d35-301d-8fda-999222c99d61 | -3.1358 | -57.6775 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 58.5 |
| a48adfbd-d188-3c7d-9b05-2465de1c3b2c | -10.3921 | -50.2488 | 2026-09-22 15:30:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 66.7 |
| 8fe194c6-f4df-37b5-ae72-e6c6517f219d | -10.6978 | -54.4932 | 2026-09-22 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 48.4 |
| 46c3a719-0b48-3f53-84db-32e0da2cd813 | -7.5705 | -57.657 | 2026-09-22 15:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.7 |
| 760e80b7-a0d3-3199-a7d5-9494aaa90930 | -3.1278 | -60.6889 | 2026-09-22 15:30:00 | GOES-19 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 66.2 |
| 30fb4c1a-3a4b-3a68-b7e4-b1c106665664 | -3.6065 | -59.4413 | 2026-09-22 15:30:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 50e54690-a7d5-35ba-8b57-65dbf57638e7 | -6.1651 | -47.5271 | 2026-09-22 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 83.1 |
| e133a0b2-b700-3635-90cc-1d03e2d253f4 | -11.118 | -54.0268 | 2026-09-22 15:30:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 69.9 |
| d0703c42-1d21-3f8c-8bc9-19ae85a70ad9 | -10.8177 | -50.9286 | 2026-09-22 15:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 95.8 |
| fc4717a0-7159-3779-a949-d756a2284c77 | -3.6813 | -58.9216 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 66.7 |
| 234b365d-91b4-32b0-ab1c-15a8f95d2b8c | -6.3013 | -59.9771 | 2026-09-22 15:30:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 96.5 |
| 93360fd9-4338-35c3-a59c-a6534b41b630 | -14.1258 | -45.5904 | 2026-09-22 15:30:00 | GOES-19 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 203.6 |
| 7052a916-a6d2-3d14-98fe-d4505523b65a | -8.0466 | -61.3237 | 2026-09-22 15:30:00 | GOES-19 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| a821e5e1-8677-33bb-b545-78c01bb25a48 | -12.4182 | -45.0385 | 2026-09-22 15:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 338.8 |
| 7cf0c687-2c55-392e-9680-a467b469a076 | 2.2003 | -50.8773 | 2026-09-22 15:30:00 | GOES-19 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 79.2 |
| d1726ead-2378-3a01-8353-fdbcc17b4e3f | -3.7313 | -60.5638 | 2026-09-22 15:30:00 | GOES-19 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 71.5 |
| 93b66020-dbb7-3061-9753-64e1251e8ee8 | -3.2955 | -59.4284 | 2026-09-22 15:30:00 | GOES-19 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| 166665f0-cd71-3053-a18a-288f44d728d3 | -3.6264 | -58.9228 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 124.9 |
| a82a22d4-593a-345d-b676-fc8a568a0825 | -3.3001 | -57.8487 | 2026-09-22 15:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 94.5 |
| 6c85a3f0-a641-3810-8797-a23b16def278 | -6.1839 | -47.5039 | 2026-09-22 15:30:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 70b4ead7-66eb-3017-ab88-0925146c0405 | -3.6264 | -58.9036 | 2026-09-22 15:30:00 | GOES-19 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 45.8 |
| 33c9bb51-da0b-3637-a5ec-93a3a0e20473 | -6.1634 | -47.7239 | 2026-09-22 15:30:00 | GOES-19 | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 58.5 |
| 4d24e3d2-78fb-3e30-a4a5-f045e66aa068 | -8.1871 | -54.7824 | 2026-09-22 15:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 50.8 |


[Clique aqui para ver as próximas entradas](README152.md)
