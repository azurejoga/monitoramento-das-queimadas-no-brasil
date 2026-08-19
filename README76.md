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

## Dados Diários - Página 76

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4c2546ed-367e-30fe-938f-904017eda945 | -6.3909 | -51.7475 | 2026-08-19 14:00:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 65.5 |
| 8d3a0ce5-7788-3c55-88db-dd1a9ec56dfa | -5.9086 | -49.273 | 2026-08-19 14:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 79.7 |
| 7d100ddf-df56-3bb2-b57f-ec92894b44d7 | -9.7533 | -43.3199 | 2026-08-19 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 61.3 |
| 781e7e82-a505-34b2-9c57-56e7a8491a8f | -14.4704 | -51.8337 | 2026-08-19 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 7db35047-a034-32ff-a437-fa076cdb6d42 | -16.5374 | -54.6831 | 2026-08-19 14:00:00 | GOES-19 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 83.9 |
| 852db524-c4a9-3115-8e51-afaf7ad2ecef | -11.0987 | -47.2678 | 2026-08-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 93.8 |
| a53666e3-b307-3336-81ee-1cd47dcba078 | -15.3838 | -52.7315 | 2026-08-19 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 172.2 |
| 65b4b8fc-0464-381a-bbe4-ecd85780074d | -7.6171 | -49.9226 | 2026-08-19 14:00:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 86.3 |
| eff3bd11-ddd8-31bf-9aa1-eeea8f133595 | -5.9994 | -57.8639 | 2026-08-19 14:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 7b30ba92-8704-361f-b710-c38685a4444b | -11.8717 | -50.1923 | 2026-08-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 67.2 |
| 8805227c-ab54-367c-9375-09f6f4af1026 | -12.2424 | -43.1638 | 2026-08-19 14:00:00 | GOES-19 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 102.4 |
| 020c759b-cd20-313c-a6b2-1ae1543f57da | -10.8075 | -50.2907 | 2026-08-19 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 03f44f39-ce5a-3346-9daa-5e59bd831fd6 | -5.9272 | -49.2719 | 2026-08-19 14:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 82.7 |
| c9a31b83-c138-3417-902d-a1e5973d877e | -11.8721 | -50.1708 | 2026-08-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 506b9c3f-b4ba-3ec1-aa69-715ac319044f | -15.2073 | -52.8401 | 2026-08-19 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 76.3 |
| ebcacfae-9a36-37c3-aaf7-578039e5af0d | -15.1684 | -52.8453 | 2026-08-19 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 4854832f-1ec8-3738-8c56-8bb82c600f1b | -10.8072 | -50.3121 | 2026-08-19 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 240.6 |
| 1ad3ac3c-91a4-31af-9c57-48665e98884f | -15.3834 | -52.7528 | 2026-08-19 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 2e3fdd69-a370-361c-9a32-5d2217173c45 | -11.4036 | -47.2511 | 2026-08-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 90.6 |
| 04a56fb6-f3fe-3c34-80fb-5aee3741d9be | -9.7537 | -43.2962 | 2026-08-19 14:00:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 63.1 |
| 4acdffa1-ad92-3adb-9ad0-45401809813b | -11.1178 | -47.2654 | 2026-08-19 14:00:00 | GOES-19 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 4ac1b863-30e6-391a-9cf5-acd34f05f9f1 | -14.221 | -52.9041 | 2026-08-19 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 252.9 |
| 9ac11f0c-acda-372a-83fa-86fe60af1f1f | -7.1176 | -47.522 | 2026-08-19 14:00:00 | GOES-19 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 82.3 |
| 0930196c-43d5-3700-93d5-5d4f8d13e558 | -11.8911 | -50.1686 | 2026-08-19 14:00:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 101.8 |
| daa55a64-d924-37d0-83fb-c9971f7b0643 | -14.2213 | -52.883 | 2026-08-19 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c357c13f-ef0f-36a1-beaa-334660db4bad | -5.4317 | -48.4212 | 2026-08-19 14:00:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 86.1 |
| ce7724ec-536a-32e6-aee1-65cdb9f28978 | -11.9961 | -53.4475 | 2026-08-19 14:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 9496e3a7-6af0-3c13-8bae-d679cef4ca2c | -13.5858 | -51.7781 | 2026-08-19 14:00:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 173.6 |
| d6ec93b4-3b37-3069-8197-d3c9659f303f | -14.2021 | -52.8854 | 2026-08-19 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 87.3 |
| ecae704a-b251-3815-8f17-3c54d13b93a7 | -10.7687 | -50.359 | 2026-08-19 14:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 139.5 |
| 0d94bffe-477d-335e-a154-c48b402c8a53 | -14.2017 | -52.9065 | 2026-08-19 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 122.3 |
| 95024ba7-c77f-3620-80c5-ecb9e1aebd8d | -14.2014 | -52.9276 | 2026-08-19 14:00:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 105.3 |
| 9a93601a-fa1f-3910-adbf-2e1e09af02de | -14.2763 | -51.902 | 2026-08-19 14:00:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.8 |
| b6356f76-4018-39a9-8737-639c1fa93d05 | -9.1078 | -46.046 | 2026-08-19 14:00:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 136.3 |
| d5a47cf2-e09e-3042-b148-879cdf262c2d | -5.9274 | -49.2505 | 2026-08-19 14:00:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 74911a1c-4c2e-3e28-b1a1-faa5dab07f3f | -15.1879 | -52.8427 | 2026-08-19 14:00:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 174.2 |
| e3772ed1-7b5d-364d-9674-30fa6c78a936 | -13.4509 | -51.8162 | 2026-08-19 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 560fc70d-baa2-39e9-b917-be01823b9f0c | -5.9272 | -49.2719 | 2026-08-19 14:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 3ed65b77-49d4-3802-afd5-d86b2f83b3de | -9.1078 | -46.046 | 2026-08-19 14:10:00 | GOES-19 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 98.8 |
| 4caf19e8-927f-37d6-8269-58db41b2f7d0 | -14.2213 | -52.883 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.2 |
| d63440ef-1bb3-3cb9-9289-aff5902130ed | -11.8721 | -50.1708 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 110.9 |
| d04ef675-557f-3960-ba8d-27aaa052b22e | -14.466 | -52.0899 | 2026-08-19 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| ce495134-51aa-3b94-a701-1a931b6546cc | -6.13 | -45.1925 | 2026-08-19 14:10:00 | GOES-19 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 61.6 |
| aae093b6-63df-30f2-988d-5af52413275d | -11.9128 | -49.9937 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 64.6 |
| 8d37ee4d-5b85-3791-96fd-872a100e835d | -14.221 | -52.9041 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 337.0 |
| fecbfbb0-026c-3d90-947f-869c27552638 | -5.4317 | -48.4212 | 2026-08-19 14:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 87.0 |
| dd3d7b30-b39f-3456-bae5-aafd6ae2b049 | -15.1875 | -52.8639 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 62.2 |
| 84b96689-ad95-3059-94ee-0ffa92f7a50e | -7.6171 | -49.9226 | 2026-08-19 14:10:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 102.8 |
| fd9800b4-5348-35ab-9670-828d52e68044 | -11.8717 | -50.1923 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 96.5 |
| 694a966b-61a0-3552-8a92-3e87b9e23d26 | -6.254 | -55.391 | 2026-08-19 14:10:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 58aa70f1-dad0-389c-b5c8-ae1fc21c46a6 | -14.4704 | -51.8337 | 2026-08-19 14:10:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 9de0341a-2ff4-38e9-92aa-3d4619d9f404 | -14.2017 | -52.9065 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 123.3 |
| d65ad92b-a34a-3134-833f-ad40ff4c6b05 | -11.853 | -50.1731 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 84.1 |
| a8b9c8bf-ec88-35cc-8320-0c2c07992e51 | -10.7687 | -50.359 | 2026-08-19 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 103.7 |
| 14455103-1487-34ae-872c-f2d4a1af01ea | -5.9995 | -57.8444 | 2026-08-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 4d8368ea-e347-3f34-901f-024f55456133 | -15.1879 | -52.8427 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 229.7 |
| 178b33f5-01a2-35df-981d-db28e151a805 | -15.2073 | -52.8401 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 82.4 |
| 2ac288aa-cc7f-3379-b16e-0b5cb308fd1f | -6.0913 | -57.8992 | 2026-08-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.4 |
| 7a5af702-cff1-3ac6-b239-d10d0f50783d | -11.9961 | -53.4475 | 2026-08-19 14:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 90.2 |
| 2f8399a9-10ac-3113-936b-32a0935055b8 | -15.0161 | -52.6962 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 125.1 |
| 51c366b4-b574-3515-aa67-b786884d3ac7 | -5.9086 | -49.273 | 2026-08-19 14:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 02f28bd6-7c4f-3e4d-872e-43881a9f3b86 | -15.0157 | -52.7174 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 92.0 |
| 2d88f586-4520-3ba2-ab8f-0fd6628f26e9 | -6.0912 | -57.9187 | 2026-08-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 136.0 |
| cc694fec-1c40-3636-9f42-f8f595be2e0a | -11.8911 | -50.1686 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 79.9 |
| 870d60a6-994a-3950-89aa-43cbf1acb7a1 | -9.7393 | -46.8504 | 2026-08-19 14:10:00 | GOES-19 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| 22c39016-1c5a-3da8-b421-aef1606f3dfe | -13.5858 | -51.7781 | 2026-08-19 14:10:00 | GOES-19 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Cerrado | 110.7 |
| 96d1a204-fb90-37a5-84ff-26266ca7ff98 | -9.4366 | -48.2955 | 2026-08-19 14:10:00 | GOES-19 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 7792e100-3c8c-3da3-8883-e653d781a533 | -6.1467 | -57.8775 | 2026-08-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 437144f6-586a-37b9-9ccb-124acdd4b542 | -14.2021 | -52.8854 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 79.0 |
| 0cc798ed-55bf-307f-a178-a56340618687 | -15.3838 | -52.7315 | 2026-08-19 14:10:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 65.8 |
| da81f2f6-6bea-35b5-987a-f08392e5da00 | -5.9994 | -57.8639 | 2026-08-19 14:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 59.0 |
| f1f58230-e84e-3bbd-b4d3-b63ce2f6cc80 | -14.1821 | -52.93 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 85.4 |
| 045c74d7-b9e6-355a-a16e-47c53cfe11c9 | -5.9088 | -49.2517 | 2026-08-19 14:10:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 64.2 |
| aa8f28f8-5651-36ef-951b-28bfe35daa1b | -9.7533 | -43.3199 | 2026-08-19 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 154.7 |
| 8e55b46d-510c-3c8c-aec2-72a4dc406f41 | -9.7537 | -43.2962 | 2026-08-19 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 101.5 |
| 8fc679ad-22bf-367d-aa0b-00e24cfa860d | -11.9319 | -49.9914 | 2026-08-19 14:10:00 | GOES-19 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 182.4 |
| cd487642-00d8-3d61-8ed1-8161bd26fe6a | -9.7343 | -43.3224 | 2026-08-19 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 112.8 |
| 941c7e87-fbf0-3a17-acc2-33f6f88c9e3f | -9.7346 | -43.2987 | 2026-08-19 14:10:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 70.8 |
| 7d5ab321-dbc6-37c0-be0d-f7a8327683bb | -14.1432 | -52.9558 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 96.1 |
| dd20bbb3-4894-3971-9eaf-9ef6ebb4da01 | -10.8072 | -50.3121 | 2026-08-19 14:10:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 2d44c968-bba4-3cd5-ba6b-1f85726574a5 | -14.2014 | -52.9276 | 2026-08-19 14:10:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 104.1 |
| 4d960855-9d29-33b2-a61e-6fd2176a55d2 | -6.3909 | -51.7475 | 2026-08-19 14:10:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 78.0 |
| c6425a07-3a07-34e4-9f22-413fbb861831 | -5.4319 | -48.3996 | 2026-08-19 14:10:00 | GOES-19 | SÃO JOÃO DO ARAGUAIA | PARÁ | Brasil | 1507508 | 15 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 0cfc24c9-d689-3b94-80fb-13dd09c1ab22 | -8.503 | -54.8625 | 2026-08-19 14:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 100.4 |
| a18aa7c1-0c3b-3379-864c-47765a294a4c | -7.6171 | -49.9226 | 2026-08-19 14:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 3a60fa02-788b-3856-bb87-7e461caf58e4 | -14.4704 | -51.8337 | 2026-08-19 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 105.9 |
| ce2b6ac1-acc1-3301-a5ad-4c8cb3f5916d | -15.0157 | -52.7174 | 2026-08-19 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 81.2 |
| 912a7ac9-46a1-3220-a7ca-6644164a7b54 | -5.9272 | -49.2719 | 2026-08-19 14:20:00 | GOES-19 | ELDORADO DO CARAJÁS | PARÁ | Brasil | 1502954 | 15 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 7a17341d-d3f8-3b1d-91ae-71fbc500e4e5 | -6.3971 | -46.6292 | 2026-08-19 14:20:00 | GOES-19 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 72.9 |
| 4de504e3-58ee-3198-8c2f-c54ef83c16a6 | -5.9994 | -57.8639 | 2026-08-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 60.5 |
| 2f06a2f7-d69d-356e-96cc-2007d3703c03 | -9.7346 | -43.2987 | 2026-08-19 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 73.2 |
| 64825b36-62cd-34e2-9546-3c370a2b7f0f | -14.2952 | -51.9208 | 2026-08-19 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| e351a70f-7cba-3c03-899c-4f0490996fec | -14.2014 | -52.9276 | 2026-08-19 14:20:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 102.2 |
| b098d1e6-c3ca-3ec6-b7bd-9a86f67a00de | -6.0366 | -57.804 | 2026-08-19 14:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 71.1 |
| c1616fe9-bd2e-342f-948c-56f08cde531f | -9.7533 | -43.3199 | 2026-08-19 14:20:00 | GOES-19 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 208.0 |
| 911dc2f3-55ab-3dc9-ba50-57b064c30d52 | -13.4117 | -54.3737 | 2026-08-19 14:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 50.9 |
| eac53626-c0d1-37c0-bf34-b2db2c6c213a | -10.7687 | -50.359 | 2026-08-19 14:20:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 111.6 |
| 485aab44-2475-38d3-9ab1-e37495ad48f1 | -14.2763 | -51.902 | 2026-08-19 14:20:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 94.4 |
| eb2f11f6-31c3-3f42-a81d-27cf57f0d3b5 | -11.9961 | -53.4475 | 2026-08-19 14:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 127.1 |
| 06b9a34b-c74f-3e8b-b85a-c630e0cc0ca5 | -15.4392 | -52.8936 | 2026-08-19 14:20:00 | GOES-19 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 68.5 |


[Clique aqui para ver as próximas entradas](README77.md)
