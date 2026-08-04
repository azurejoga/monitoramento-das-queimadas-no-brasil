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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 224b8fb2-d5b7-3634-b271-27fc63a0f976 | -11.2015 | -54.900002 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2ed07007-2447-3da9-a2eb-cf67999f09ea | -6.5612 | -55.177502 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ad5cbefc-cb8c-32e4-a143-be4e0da04bd0 | -11.1973 | -54.8437 | 2026-08-04 01:09:00 | METOP-B | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 54f07162-686b-3ba8-a7c1-515b7cb73771 | 2.5385 | -60.357399 | 2026-08-04 01:09:00 | METOP-B | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 9db51284-ebe1-3083-ace4-8f7d817e822a | -6.5708 | -55.175098 | 2026-08-04 01:09:00 | METOP-B | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1cb50ac9-ed46-377c-b17b-8dccda49f522 | -11.2213 | -54.855 | 2026-08-04 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 63d0a87e-2672-3b7b-a3f3-268d34b9c27a | -5.1506 | -46.2026 | 2026-08-04 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 130.0 |
| bd79813c-8ad3-3898-be32-b29c12bc499c | -3.6639 | -49.4686 | 2026-08-04 01:10:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.7 |
| 46979a0f-a8d8-3e75-b403-ce3e2624ae59 | -6.5514 | -55.1569 | 2026-08-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 72.9 |
| ef9df6cf-cf45-36cc-a645-6eff5c3fb705 | -11.2022 | -54.8771 | 2026-08-04 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 103.9 |
| f6c6bb8a-b12b-3a1f-bdd1-cb59e5b80147 | -6.5512 | -55.1769 | 2026-08-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 58.8 |
| 69fb4f6e-fe82-35dc-8acd-5de5ed2e29ae | -5.1319 | -46.2037 | 2026-08-04 01:10:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 102.5 |
| 01ed2fdd-c34b-3bc2-96c3-195f11b96d69 | -11.2024 | -54.8567 | 2026-08-04 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.7 |
| bed3de7a-577e-315e-b000-024e7f6b500f | -6.5697 | -55.176 | 2026-08-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.0 |
| f672f323-d9e6-3ade-af87-31bd1beb9845 | -11.2211 | -54.8754 | 2026-08-04 01:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 60.9 |
| 2643062f-0482-3c99-bdfe-bf176c48642a | -6.5699 | -55.156 | 2026-08-04 01:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| b70d4bf5-45fd-3b99-992f-b2e3872a02a6 | -8.3544 | -45.9897 | 2026-08-04 01:10:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| 48ed45bb-7132-3d9f-b84d-570ca38bb6f0 | -6.5697 | -55.176 | 2026-08-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.2 |
| a80fdd48-3414-3d65-a37d-805fc2d2d8cf | -6.5514 | -55.1569 | 2026-08-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.3 |
| ea83ed44-a195-3589-ac91-be7d636ef8c0 | -5.1319 | -46.2037 | 2026-08-04 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 480f3122-a26e-38c5-a820-9df455d74de7 | -11.2024 | -54.8567 | 2026-08-04 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 61.5 |
| dc0976cb-52c8-30dd-bab4-9bfaae15b898 | -8.3546 | -45.9671 | 2026-08-04 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.0 |
| 50bbc35d-3900-3754-9767-648c806a46f5 | -13.4448 | -43.8604 | 2026-08-04 01:20:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 40.0 |
| 0a096f1f-d3e5-3bb9-a20e-5f4265c2ccf2 | -6.5512 | -55.1769 | 2026-08-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.1 |
| 127ba263-8d43-3beb-a7df-0256b1bd8b05 | -6.5329 | -55.1578 | 2026-08-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 45.8 |
| a6f684cc-0060-3465-9c2b-d6fa9742f729 | -11.2213 | -54.855 | 2026-08-04 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 84.3 |
| b9b4ce1a-d0c7-3138-98bc-a99f2cf75939 | -11.2022 | -54.8771 | 2026-08-04 01:20:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 65.3 |
| 7678652a-2057-3968-8d0c-42711e3bf4a3 | -8.3544 | -45.9897 | 2026-08-04 01:20:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.8 |
| aa83e17c-2ab1-3b1d-b687-d6e2486bce5e | -6.5699 | -55.156 | 2026-08-04 01:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 67.5 |
| 6c82f7f4-1e5a-3819-9d87-931ff159f62c | -3.6639 | -49.4686 | 2026-08-04 01:20:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 56.3 |
| 95514c26-b500-39c3-908e-3f971271228a | -5.1506 | -46.2026 | 2026-08-04 01:20:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 75.8 |
| 2b286ffa-a5c6-3435-8cc8-88f644aebe49 | -3.6639 | -49.4686 | 2026-08-04 01:30:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 52.8 |
| f493adb8-20b8-3e58-a523-664618d089d8 | -6.5514 | -55.1569 | 2026-08-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 62.2 |
| e1666427-9d72-3898-96f4-937270bc09ba | -6.5699 | -55.156 | 2026-08-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 57.4 |
| 678c1e77-91c7-38b6-bcbe-e4b81b10129d | -10.5741 | -46.7745 | 2026-08-04 01:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 67.3 |
| dcef6a2a-42df-3fbe-8819-a1a780838ad3 | -6.5512 | -55.1769 | 2026-08-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.1 |
| ffca6f3c-516d-34aa-b004-d6d229ac4389 | -6.5697 | -55.176 | 2026-08-04 01:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 64497c25-81b3-3a1d-8194-75e50dd855a4 | -13.4448 | -43.8604 | 2026-08-04 01:30:00 | GOES-19 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 52.0 |
| 85f3291b-0898-3fae-b78c-80fe4d362abd | -11.2213 | -54.855 | 2026-08-04 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 81.3 |
| 61941c57-ca3b-3f2d-ad45-5ec9cca1ee17 | -8.3544 | -45.9897 | 2026-08-04 01:30:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.0 |
| c0b3539a-0467-333b-9697-8945a52955e4 | -5.1506 | -46.2026 | 2026-08-04 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 76.3 |
| aedbf454-97ee-358b-8d3b-09dedcc09066 | -5.1319 | -46.2037 | 2026-08-04 01:30:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.8 |
| d9322f28-f749-3fdc-95c0-dabaf80b75b8 | -11.2024 | -54.8567 | 2026-08-04 01:30:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 172335ec-26f3-39c1-9aad-291da1bb4302 | -11.2241 | -54.849701 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 7315a737-7202-3084-a42a-fc58985258fd | -11.9216 | -55.911098 | 2026-08-04 01:30:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fdef0a7a-e96b-39eb-b704-88f2164fa8a1 | -11.2046 | -54.854698 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 83e9d047-3e97-3ba1-9b50-4807a020a506 | -11.2209 | -54.878201 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| edec82eb-ee3c-35f3-86ce-935fd59f6299 | -11.2111 | -54.880699 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 82446376-d4c7-375c-8202-4819799b1ec4 | -11.2079 | -54.867699 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| adf86e2c-4924-36fc-bef0-f49fec4fce83 | -11.2273 | -54.862701 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 197888aa-d1c0-38fa-9c46-453e6383110a | -11.9189 | -55.9002 | 2026-08-04 01:30:00 | METOP-C | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 096b8629-8b6b-307d-811d-f41cbcd7b369 | -11.2111 | -54.8391 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9227d435-3c2d-3792-84ad-7e76101db012 | -11.2144 | -54.8522 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| a4a609a7-18b4-338a-a19c-44c740caa1a2 | -10.8207 | -65.095802 | 2026-08-04 01:30:00 | METOP-C | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 622a6d51-a044-34e4-8934-3c80ec4cce06 | -11.2306 | -54.875702 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| b88de4dc-9f55-3c05-8f67-1c97f5dcb543 | -11.2176 | -54.8652 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2cefd116-c6e7-3c1d-b236-d95b6667ec2b | -11.2014 | -54.883099 | 2026-08-04 01:30:00 | METOP-C | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 254e1701-d272-3a4f-a800-d05475109549 | -6.5499 | -55.1791 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a9c7e67b-da9d-3dd0-b25d-8e549afbf3d4 | -1.6392 | -54.472 | 2026-08-04 01:33:00 | METOP-C | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 6a5c51e1-3e04-33d2-ba75-2f82c5fa1dff | -6.5366 | -55.166801 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e51614ba-9440-3b75-80f9-32099d1c6891 | -6.5596 | -55.1768 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d8990d2a-a73f-34b4-9cef-0e619e3d94b3 | -6.579 | -55.172001 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2d030ce1-1b66-341b-8268-85cfc2fe851a | -6.5693 | -55.1744 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2af64ed3-5bf6-35b8-9dfa-c6fd49902652 | -8.7774 | -63.6395 | 2026-08-04 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| d22d8811-aa99-3cf9-b14e-d1b4c71b3d4b | -8.4578 | -64.146103 | 2026-08-04 01:33:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| 352c470a-c8a2-39af-abf4-eac4c7dee6cc | -8.4594 | -64.153603 | 2026-08-04 01:33:00 | METOP-C | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | nan |
| a2b84230-d60e-3169-9ca4-2d942fc5fdfb | -6.5561 | -55.162102 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8188e2f-ad4e-3d9e-a49a-0b395a42acf8 | -8.779 | -63.646801 | 2026-08-04 01:33:00 | METOP-C | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 4708a942-f8c3-3528-b4d7-43eb5a38cab2 | -6.5464 | -55.164398 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 29dcd7f8-63ad-3714-aad6-61d89df65845 | 2.5303 | -60.364899 | 2026-08-04 01:33:00 | METOP-C | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | nan |
| 48d221b5-fa99-3f00-b4bb-130da6b43abb | -6.5658 | -55.159698 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f9a1f4ab-9e6d-3978-9b75-54dca9786f31 | -6.5755 | -55.157299 | 2026-08-04 01:33:00 | METOP-C | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 28574cb5-4ee5-3ecf-82d5-d89a747e6782 | -5.1506 | -46.2026 | 2026-08-04 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 59.4 |
| 4f95063f-4a21-3764-9270-5051a8d4d165 | -10.5741 | -46.7745 | 2026-08-04 01:40:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 62.6 |
| cf9ecef9-488d-31ed-89bf-a916fb183266 | -6.5512 | -55.1769 | 2026-08-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 2dc5f23f-230f-38ba-8009-647bff09e1eb | -8.3544 | -45.9897 | 2026-08-04 01:40:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 59.9 |
| c5bd84de-b870-3386-9af7-40a4076a203a | -6.5699 | -55.156 | 2026-08-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.7 |
| e4319f93-6f62-3da7-95f8-75394a001bf7 | -6.5514 | -55.1569 | 2026-08-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 59.6 |
| a332e5de-ce60-3bbe-b44a-0c163a4a309c | -5.1319 | -46.2037 | 2026-08-04 01:40:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 63.4 |
| 65b8f546-c1e4-3248-a18a-f0769e59ca4d | -3.6639 | -49.4686 | 2026-08-04 01:40:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 51.3 |
| 88d3fb6a-7c53-351a-a47b-65205a20d017 | -6.5697 | -55.176 | 2026-08-04 01:40:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 51.5 |
| 65e7c399-60e3-3d11-9832-7d26a36c8ad4 | -11.2213 | -54.855 | 2026-08-04 01:40:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 76.4 |
| 3b8c2bdb-acf1-3964-af35-e8a6b048dfe5 | -3.6639 | -49.4686 | 2026-08-04 01:50:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 58.3 |
| 1b3763c7-b23a-3f14-80fa-a0ca4a8706e5 | -8.3546 | -45.9671 | 2026-08-04 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 38.4 |
| 4553cce4-166d-3501-a118-87c30f62ca16 | -5.1506 | -46.2026 | 2026-08-04 01:50:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 54.2 |
| 7c53d45a-4251-3a9e-b634-4eb26b257fcd | -11.2213 | -54.855 | 2026-08-04 01:50:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 72.8 |
| 1d016743-263f-3414-9675-e47890249195 | -6.5699 | -55.156 | 2026-08-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 56.7 |
| 36c0c0ec-6807-3a16-a4f1-f81af0d8827b | -8.3544 | -45.9897 | 2026-08-04 01:50:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 13441101-4a28-35d1-8cde-3a6c63d5351b | -6.5514 | -55.1569 | 2026-08-04 01:50:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 9030b3f2-a311-3fe5-b329-9af33e41636c | -10.5741 | -46.7745 | 2026-08-04 02:00:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 65.1 |
| 24aef021-600a-3317-bea3-8bb5ff21cfa9 | -6.5699 | -55.156 | 2026-08-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 55.2 |
| b76ff5bb-b181-3f85-b30e-cf4a6899af27 | -3.6639 | -49.4686 | 2026-08-04 02:00:00 | GOES-19 | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 2ed90b4b-b335-3eae-b5e9-d52c90699684 | -6.5514 | -55.1569 | 2026-08-04 02:00:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 66.1 |
| 033f891a-fd32-37e1-b072-a9f9a440ced4 | -11.2213 | -54.855 | 2026-08-04 02:00:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 66.8 |
| 1219205e-7c78-3c67-b121-7cd12cee1569 | -8.3544 | -45.9897 | 2026-08-04 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 50.8 |
| f8e43883-c67e-3cd7-a8bc-695ed0bd87a6 | -8.3546 | -45.9671 | 2026-08-04 02:00:00 | GOES-19 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 41.5 |
| 2623fcc4-c27a-3692-85ca-a201fbb733d9 | -5.1506 | -46.2026 | 2026-08-04 02:00:00 | GOES-19 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 56.8 |
| b502461c-0236-39e2-a9ce-30f790f9b344 | -6.5699 | -55.156 | 2026-08-04 02:10:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 54.8 |
| bd9e7b76-d3d6-3b8a-bdec-32f9e18e0e96 | -11.2213 | -54.855 | 2026-08-04 02:10:00 | GOES-19 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 5daff9e1-14dc-309e-91ba-36b52869f7b0 | -10.5741 | -46.7745 | 2026-08-04 02:10:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 86.4 |


[Clique aqui para ver as próximas entradas](README5.md)
