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

## Dados Diários - Página 125

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ac6da1f-f1b6-334b-b808-c68ccc466f7f | -4.93126 | -55.78641 | 2025-09-11 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 617d3a84-c9c1-3101-9c6b-1abb2047e32e | -7.49452 | -54.95003 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7278b4a0-4fbe-32b9-86e4-23590759fcd2 | -3.81546 | -59.66921 | 2025-09-11 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e800dd66-3b06-33d2-9322-2b8e57871053 | -4.19962 | -55.13292 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4cd705f1-87c1-37d7-bf0a-7a2ffad1b138 | -3.53292 | -59.60923 | 2025-09-11 05:36:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c9151d19-e07c-3c11-9410-4ff0da080130 | -8.09282 | -54.747 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba01c9ca-178c-304d-8b1c-6ed1a5739758 | -6.49978 | -62.93333 | 2025-09-11 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9c68b4d-c8ae-3c24-aaca-4eec5e983c40 | -7.49322 | -54.94709 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 20ded881-e600-38c1-8927-ccc575d9cc98 | -6.50419 | -62.92682 | 2025-09-11 05:36:00 | NOAA-21 | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b37210fe-79a7-338e-9efe-fdf868116b7d | -7.49405 | -54.95339 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 41039c8e-266d-3145-9d16-d175042a657e | -4.45737 | -55.0531 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3912c29b-0047-34e9-8d0a-936b21fa10e9 | -6.62791 | -62.85213 | 2025-09-11 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 205e02b1-7956-31d4-b504-15d1d305e21d | -7.49855 | -54.94786 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec0e29ff-a587-3e5d-9759-28ce49e38200 | -4.19919 | -55.13589 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 67456149-21e3-3a6f-81c6-10e19e51d0cc | -7.49278 | -54.95045 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4aa834da-308b-3cdc-ad4a-5e89840b7052 | -8.5179 | -54.76588 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9836ad7-702e-3829-86d3-8d78d11b6afd | -7.48921 | -54.94912 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25898c56-764f-330b-88fc-97df980fec5a | -7.49234 | -54.95378 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e849d889-efeb-3e19-b5ad-d0af455c9107 | -8.08148 | -54.74886 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1f6950b0-2c38-35ab-a6e5-4dbce28907f5 | -7.78577 | -50.7711 | 2025-09-11 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 4aa5e956-a1b4-3a2b-88c3-618f51ece15c | -7.4883 | -54.95564 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| be3f713b-4daa-39d8-9c73-0c8558f9a28c | -6.62845 | -62.8486 | 2025-09-11 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| abcf560d-fb29-38c6-87c9-81fca55852a3 | -6.82332 | -52.7993 | 2025-09-11 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 91e9c7f7-ca0e-3171-b3c8-55c527d7dd55 | -7.78677 | -50.76317 | 2025-09-11 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 1f120688-3a0c-30c7-9131-05beb9a77efb | -6.82449 | -52.79963 | 2025-09-11 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 984c0d65-d230-3666-bb04-6c4408541135 | -7.97918 | -61.23179 | 2025-09-11 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2a1fbf39-b7bf-3758-b1c2-64517909d134 | -4.45782 | -55.05005 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 58183615-238c-3ee8-a327-50d0f6dae2ea | -7.85765 | -61.17227 | 2025-09-11 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 88e32e5a-b374-3a6b-96d2-61bdce83c6e0 | -8.57109 | -51.3504 | 2025-09-11 05:36:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| aafb48ed-ebf3-3a62-8313-a22e0064b8d6 | -7.85826 | -61.16815 | 2025-09-11 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60e52990-94ab-3bf3-a3d1-61ee8d577b3e | -5.4862 | -60.13384 | 2025-09-11 05:36:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4a1dcff7-f7a6-3279-8a7e-b0c2241a97eb | -8.11703 | -63.69069 | 2025-09-11 05:36:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b37c15e4-6dbd-3d68-a860-3cace1237eeb | -6.27485 | -53.42368 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e313a87b-5050-3b92-a3b8-f08422414243 | -5.72812 | -53.59877 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 7138c931-459d-38e3-8e63-1d1e8f1502e8 | -8.08194 | -54.74532 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6ac8fc84-acbc-3e4b-84e1-398f4902a20b | -7.48876 | -54.95238 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 468b1242-81e2-31fb-9c32-ebc278885d95 | -6.28064 | -53.42453 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 232fdc9b-61f1-3e4e-9810-f77d298e33ee | -7.53237 | -61.6558 | 2025-09-11 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 69e3e011-72ba-38f5-8654-faed5c95e140 | -6.80996 | -52.8064 | 2025-09-11 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c683f673-6416-35d6-a1cb-458c570853e9 | -4.20422 | -55.13656 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b4af6543-359a-3d59-b87e-814599c67631 | -9.52328 | -54.64061 | 2025-09-11 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2ffc815-bc55-3dff-947b-439c4dc1c63b | -4.19877 | -55.13881 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 5a4b85df-90b8-38fd-a7c4-96f60b564047 | -10.00405 | -51.71403 | 2025-09-11 05:36:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| c4f80962-3ac2-3da1-a60e-5a10bd6abe32 | -6.81119 | -52.80674 | 2025-09-11 05:36:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ff59f252-1480-3bdd-ad7e-3e4675d55a59 | -8.08241 | -54.74174 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| fb989881-1d4d-31b9-8331-dc9cb7b3010e | -9.51811 | -54.63657 | 2025-09-11 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 00b9c5ca-7d46-33d6-a56c-2983464c892a | -4.20379 | -55.13948 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| f0bb4296-8db0-33a9-a3cd-5132da91c9e4 | -7.48704 | -54.95277 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c77ed196-2b1b-3fe1-a57f-19bce7454c7d | -7.49499 | -54.94664 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3e9775dd-57ec-3cd6-a0f7-d38ff76038bb | -9.51767 | -54.63997 | 2025-09-11 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bcc0c0af-754f-3300-8ace-7c99e0c1ecb3 | -8.08288 | -54.73814 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2be40710-673f-3452-a85b-4526f46c212a | -7.87714 | -63.28415 | 2025-09-11 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 5d8a839b-523f-30b5-a429-6b282e2792aa | -10.00259 | -51.72625 | 2025-09-11 05:36:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a5642141-cec7-35fa-8cad-f686157fc0bb | -8.52337 | -54.76667 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 39b157ad-f90a-3ee1-9ad5-6abe80eedae1 | -3.86255 | -55.9962 | 2025-09-11 05:36:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0ae81900-f919-349a-bb65-780c3f12dfe2 | -6.93847 | -62.91095 | 2025-09-11 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| dfaaf682-a1c6-3521-82ca-01a8e7fadde1 | -6.629 | -62.84507 | 2025-09-11 05:36:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b3f0dff-e0db-30b3-8057-57beeaec2ee9 | -3.44301 | -54.63879 | 2025-09-11 05:36:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c80a0404-750c-311b-b6e3-fbb8eac3834e | -8.08738 | -54.74617 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3bc3f490-347f-351a-af0f-6f0a97fdae32 | -4.92642 | -55.78564 | 2025-09-11 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| abac4fef-ef2d-32c4-a198-e321472ade99 | -4.45826 | -55.047 | 2025-09-11 05:36:00 | NOAA-21 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 08fb0fb2-41bd-3798-af13-1271a61bab34 | -9.52372 | -54.63721 | 2025-09-11 05:36:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 516a1b50-5a61-32d4-8ad6-f363cc41beff | -4.93201 | -55.78109 | 2025-09-11 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| c3116983-9d78-36a3-bf2c-a5c5b6028bd0 | -4.92716 | -55.78036 | 2025-09-11 05:36:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 702f5e4b-54df-3a0b-8254-3bb77ade1287 | -8.08102 | -54.7524 | 2025-09-11 05:36:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9caf52b2-3d92-3e16-81ee-0130f43cdfee | -10.00333 | -51.72012 | 2025-09-11 05:36:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0db27261-9baf-3900-9ef2-4420d124d855 | -7.53053 | -61.37429 | 2025-09-11 05:36:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd91f401-1f6b-31be-bfbb-b3a4211db065 | -17.3833 | -52.92807 | 2025-09-11 05:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| d7dc59c5-932c-37af-8e98-3e93626f8e31 | -9.98685 | -64.98338 | 2025-09-11 05:38:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5ad5e1c1-1c94-3565-8bf0-15b9f4021195 | -14.28055 | -54.74554 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e05a2e6e-48f6-3ed7-98c8-720c73fe3f1e | -17.38272 | -52.93436 | 2025-09-11 05:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| a3a0f6d5-678d-34b5-ad55-5356461e2cdd | -10.27027 | -63.16987 | 2025-09-11 05:38:00 | NOAA-21 | CACAULÂNDIA | RONDÔNIA | Brasil | 1100601 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d9ca3cca-16d1-34d4-b818-2b0b31505106 | -9.04135 | -65.40907 | 2025-09-11 05:38:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5932122d-1d26-3111-aa22-0d36f6e133ed | -10.29263 | -60.56646 | 2025-09-11 05:38:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3612dbfc-78d5-341c-b10f-d10e30e53c14 | -10.15239 | -64.24907 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6a12738e-6540-395d-a010-8772a06923ce | -15.56454 | -54.74292 | 2025-09-11 05:38:00 | NOAA-21 | DOM AQUINO | MATO GROSSO | Brasil | 5103601 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| f50832e3-a706-3c9a-8b41-8f44edb47600 | -14.50825 | -53.96301 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 8c0b3927-a03d-3001-98f8-b4b60ccf4817 | -12.9261 | -54.77969 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 999e9555-8e4c-360f-b7e4-ae49df311508 | -15.12548 | -52.40426 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 38ab622d-b884-39ab-bd97-56b80793d55b | -14.50307 | -53.95246 | 2025-09-11 05:38:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 552e0c61-d4a9-3f60-81e4-875465ecf0d4 | -9.97439 | -63.66208 | 2025-09-11 05:38:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e2fedaba-fe9c-3c14-ae0d-f3c910ed8f6a | -15.80309 | -52.26554 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 26ff1a92-b0aa-3a40-9f43-f5854bb6a9e2 | -12.94065 | -54.7561 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ceadb2cf-8f39-3c9e-8d78-866be6ae0d18 | -12.39913 | -63.80966 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e18cd6c7-f000-35a4-ae47-654e3dcb8efa | -17.3759 | -52.93356 | 2025-09-11 05:38:00 | NOAA-21 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| 64486cd0-64db-3d45-856e-8de5f55c4a6f | -12.97031 | -54.7561 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6911f560-4ced-3f75-befc-db869d65dcde | -12.9348 | -54.80587 | 2025-09-11 05:38:00 | NOAA-21 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| c2d79d1c-c7c8-3263-ae79-55949e874b9e | -12.45948 | -57.20048 | 2025-09-11 05:38:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 3ccbed1f-2fe3-3bc0-a481-f55f227f38b2 | -12.40626 | -63.82142 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 946b5c0c-9fa7-3eac-8a92-67a57916c0bd | -8.70612 | -64.21111 | 2025-09-11 05:38:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4907f059-a15c-3eae-b26c-8f6e97363c31 | -9.7926 | -61.52074 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca2c07cd-1b5b-3647-b310-79f95f6ec612 | -14.92847 | -55.91411 | 2025-09-11 05:38:00 | NOAA-21 | CHAPADA DOS GUIMARÃES | MATO GROSSO | Brasil | 5103007 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fcfc190c-28e9-35b3-b2d8-0a7eb3efedb7 | -13.25826 | -51.76764 | 2025-09-11 05:38:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| ec35d5c9-06b8-356f-afd6-bb37118bd5f6 | -11.05276 | -51.33404 | 2025-09-11 05:38:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 939a9a10-d643-314e-a23b-0634ca8c81d5 | -15.11902 | -52.40639 | 2025-09-11 05:38:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 24d309d1-72e9-3cb6-acc6-f7f4939b2fd0 | -12.41994 | -63.89069 | 2025-09-11 05:38:00 | NOAA-21 | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6507289c-d256-3755-ba74-17692f0f67b9 | -9.46236 | -63.03532 | 2025-09-11 05:38:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 901dfe0e-d141-3363-82dd-3a56533a5bcd | -10.01797 | -51.73306 | 2025-09-11 05:38:00 | NOAA-21 | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 48d26ea4-0a5b-3825-b858-83d4284bbc81 | -10.33535 | -54.5535 | 2025-09-11 05:38:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 45df0867-5f40-3aef-92f4-e6edfb46540e | -9.8004 | -61.51767 | 2025-09-11 05:38:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |


[Clique aqui para ver as próximas entradas](README126.md)
