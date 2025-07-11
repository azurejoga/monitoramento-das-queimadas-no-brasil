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
| 546d8bb8-24f6-3470-bead-bbbbf25e6a7e | -5.5429 | -43.8864 | 2025-07-11 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 646f0ef4-d85c-3925-8e57-01250733ac02 | -10.5776 | -49.1316 | 2025-07-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 6b3ad460-b657-3150-aaeb-7322da01d749 | -7.2025 | -43.1171 | 2025-07-11 01:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 96.8 |
| c40cc1fa-a611-3f49-9ac7-b18df5868334 | -10.6859 | -49.509 | 2025-07-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 55.1 |
| b5dc6bfe-8b10-36a0-b5a4-805b82b446ac | -9.9148 | -47.8282 | 2025-07-11 01:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 221.0 |
| bbc32d6e-1a5c-3178-aaf8-aca4cee7608d | -22.2852 | -54.9409 | 2025-07-11 01:10:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 73.6 |
| b8cbe9ca-fb75-379b-8eff-ef4621e1fec8 | -10.6672 | -49.4895 | 2025-07-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 55445f57-6fb7-3bb8-bcc7-49ad75ad7700 | -9.9337 | -47.8261 | 2025-07-11 01:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 69.8 |
| f92c9d9a-9669-3803-b7c0-e27d88b6878b | -10.6862 | -49.4874 | 2025-07-11 01:10:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 198.3 |
| 1b169ca8-cc3c-3413-af92-dd2815273b09 | -9.9151 | -47.8062 | 2025-07-11 01:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 59.0 |
| 3ec28d78-1e38-323c-af16-826304dcd8b0 | -5.5616 | -43.8851 | 2025-07-11 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 75.9 |
| 5eaf61fd-dac0-394a-9dd3-f96cd1a677c5 | -5.5614 | -43.9082 | 2025-07-11 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 26761eee-3418-32c8-bf6f-5bb39e75f002 | -9.8958 | -47.8303 | 2025-07-11 01:10:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 92.7 |
| 96f4d0ec-71a9-3168-a89d-c698e8902331 | -5.5427 | -43.9096 | 2025-07-11 01:10:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 184.7 |
| 57ec1a8a-9f86-3c69-9e07-486094168181 | -9.9337 | -47.8261 | 2025-07-11 01:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 70.7 |
| 672b36c6-81fd-3f55-a99e-1c502a941765 | -10.6859 | -49.509 | 2025-07-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 68.6 |
| cb387bed-973c-3036-bb29-f950d0430c9f | -5.5427 | -43.9096 | 2025-07-11 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 173.0 |
| c550ae31-8c21-3576-9041-faa2d5911cf7 | -9.8958 | -47.8303 | 2025-07-11 01:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 81.7 |
| d8d47f34-abb5-35fd-a050-0b882b73d8d4 | -7.2025 | -43.1171 | 2025-07-11 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 100.2 |
| 2bdacc54-997e-3489-a98a-419adef9185b | -10.6862 | -49.4874 | 2025-07-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 179.8 |
| e4bc518f-38cb-3d7e-97e3-c8070080a3d9 | -10.6669 | -49.5111 | 2025-07-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 58.6 |
| e31e60f7-6564-34ab-b2d1-28480769c955 | -9.9145 | -47.8503 | 2025-07-11 01:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 65.0 |
| 459f2edb-9a64-3e32-9c74-012add9073fa | -5.5614 | -43.9082 | 2025-07-11 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 77.6 |
| d10703bc-487f-3e2c-b100-cf0f0e86ba7d | -10.5776 | -49.1316 | 2025-07-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 149.8 |
| 8f063063-421a-34de-8e3c-6dd1bf208bfa | -10.6672 | -49.4895 | 2025-07-11 01:20:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 146.4 |
| 837001e9-4b74-3797-90c8-7e63cda12c51 | -5.5429 | -43.8864 | 2025-07-11 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 139.3 |
| f755d020-4585-32a3-9e07-49bec60890b4 | -5.5616 | -43.8851 | 2025-07-11 01:20:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 0d4e8d67-cab6-38a0-b593-22afaabc2cad | -10.8429 | -49.1236 | 2025-07-11 01:20:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 64.4 |
| 3090188e-7395-35be-b41e-6d271add9952 | -9.9148 | -47.8282 | 2025-07-11 01:20:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 240.8 |
| 6821eaad-7f25-3595-be8d-769f6cf70c4f | -21.6867 | -49.49391 | 2025-07-11 01:20:00 | TERRA_M-M | CAFELÂNDIA | SÃO PAULO | Brasil | 3508801 | 35 | 33 | nan | nan | nan | Mata Atlântica | 44.9 |
| c43e0c17-c836-344b-bf87-5d18a49113f9 | -22.2716 | -54.95123 | 2025-07-11 01:20:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 19.8 |
| d4e9fbac-a64b-3f8d-a861-db316b616564 | -22.61227 | -54.95073 | 2025-07-11 01:20:00 | TERRA_M-M | CAARAPÓ | MATO GROSSO DO SUL | Brasil | 5002407 | 50 | 33 | nan | nan | nan | Mata Atlântica | 9.6 |
| 8c42c6fc-5f91-3836-a5c9-5a51ca456e0e | -22.28078 | -54.94957 | 2025-07-11 01:20:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 8e8e71c7-0622-366a-854e-ac906e0a1ed2 | -22.28233 | -54.95992 | 2025-07-11 01:20:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1d391f0d-2adf-34ab-8850-f70a8fb0b943 | -22.27006 | -54.94097 | 2025-07-11 01:20:00 | TERRA_M-M | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 0e87b781-4320-3fa1-8c63-db373ace1e14 | -10.85887 | -49.12127 | 2025-07-11 01:22:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 42.0 |
| 2f4531e9-4ce2-302e-8b9e-7c313893a10d | -10.5866 | -49.15561 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 78.6 |
| 90f5667f-b69f-37b0-9a7f-63d6a6b3433e | -16.95047 | -49.44254 | 2025-07-11 01:22:00 | TERRA_M-M | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 39.9 |
| c60211f8-9099-3a84-a0b8-4dc575311a86 | -10.84197 | -49.12452 | 2025-07-11 01:22:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 76.5 |
| c4a39f14-1a5a-3b5e-b92d-3099e7553005 | -10.58246 | -49.10948 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 46.0 |
| f078de1c-826b-3c8d-856c-8b860232c54e | -18.64957 | -55.71716 | 2025-07-11 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 9.0 |
| 0d2abdbf-7006-34e5-a85c-63b75217af48 | -10.67154 | -49.51976 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 70.2 |
| 4e12065b-8bcb-3bf3-9054-22fa9403ccdb | -11.86471 | -58.71034 | 2025-07-11 01:22:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 22b07399-7337-3e55-a54c-77f7dde7c53b | -10.68176 | -49.48024 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 171.3 |
| 5f5be50e-c223-3d71-bd7b-3d6011766b05 | -10.57229 | -49.15121 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 71.7 |
| c5710fc1-fb6f-3790-ba54-72500ac0dbd2 | -10.68803 | -49.51661 | 2025-07-11 01:22:00 | TERRA_M-M | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 88.8 |
| 55b3d0e7-f80b-37c1-815e-1936e1abf30d | -19.08669 | -56.04916 | 2025-07-11 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 12.6 |
| 3de2a8a9-6bc7-3479-aaeb-8d65537849ce | -10.58002 | -49.11681 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 95.9 |
| 0116db5c-8166-3a1b-8cf4-c0dacffbb76e | -11.32518 | -55.21137 | 2025-07-11 01:22:00 | TERRA_M-M | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| fe1ea563-994a-356a-a0ce-e898ef0c9998 | -11.96165 | -51.70405 | 2025-07-11 01:22:00 | TERRA_M-M | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 26.9 |
| dda96a55-24d7-3cf0-af0d-215b056d1287 | -10.67663 | -49.51372 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 2125325b-ad8a-3328-aa13-4af662942526 | -18.66031 | -55.72575 | 2025-07-11 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 16.4 |
| 37bd658f-d96e-3abe-ba9a-d1972df010db | -10.67009 | -49.47744 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 242.6 |
| c8fe2420-6f32-35a7-9801-8552de960b5e | -18.65109 | -55.72731 | 2025-07-11 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 13.2 |
| 5a337857-4a11-3d7c-a626-32570cf72aea | -10.85596 | -49.12679 | 2025-07-11 01:22:00 | TERRA_M-M | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 78.8 |
| 75c9e17e-a1cd-3f0c-9303-28dee3a875f3 | -10.66523 | -49.48343 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 133.7 |
| 913bf2e2-15a6-32d3-a473-be1cca74b093 | -10.58931 | -49.14836 | 2025-07-11 01:22:00 | TERRA_M-M | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 79.5 |
| 57e2949f-4a66-30f7-80ca-2b306527807c | -11.87483 | -58.71806 | 2025-07-11 01:22:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 8dc4c862-a270-35d8-9b6f-04845748a3b1 | -9.94956 | -64.969 | 2025-07-11 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 64d0ab2a-8a36-3cbc-8ab1-6d3086d02084 | -10.97506 | -58.66614 | 2025-07-11 01:24:00 | TERRA_M-M | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 7544b783-ccd3-35c5-b7c4-27b00e072866 | -9.941 | -64.95962 | 2025-07-11 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 30.8 |
| c6d6698e-f8c5-3afc-a3ca-81436cb115b1 | -9.9614 | -64.96748 | 2025-07-11 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 41.2 |
| ff88f62e-072d-3b1e-ac1f-efb20ba89ba9 | -9.94755 | -64.95235 | 2025-07-11 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 21.4 |
| a8bf726c-fd8f-3810-88e2-39f8b842a1ab | -6.62498 | -56.28247 | 2025-07-11 01:24:00 | TERRA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 786e67c5-6c45-3da7-bb2a-6f28c930396c | -10.8429 | -49.1236 | 2025-07-11 01:30:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 61.6 |
| 5eefc2fb-63cd-39ab-9a87-acca7cda1837 | -10.6862 | -49.4874 | 2025-07-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 225.0 |
| 8026af08-1a1d-364f-936f-6c9601def9b9 | -10.5776 | -49.1316 | 2025-07-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 103.6 |
| 6d156cdb-3eec-37c9-8810-f6e75bd4563d | -6.1674 | -47.2638 | 2025-07-11 01:30:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.3 |
| bc5aa6ad-ada0-34bb-9991-dd6b21900557 | -10.5965 | -49.1295 | 2025-07-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 54.0 |
| 4a8a83be-cd90-37d8-b16b-742ec2e46af9 | -16.956 | -49.4237 | 2025-07-11 01:30:00 | GOES-19 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 766b3919-5bd8-38d6-8e9b-2d76754bc255 | -10.6672 | -49.4895 | 2025-07-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 115.9 |
| 78b53be7-2cff-36e9-8320-ea9d2072db50 | -10.6859 | -49.509 | 2025-07-11 01:30:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 85.9 |
| 71406ee2-7588-35a1-a9e5-7d8d9ad91f51 | -7.2025 | -43.1171 | 2025-07-11 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 87.5 |
| 84af549f-81f3-3154-bace-c36bbae62302 | -9.9145 | -47.8503 | 2025-07-11 01:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 53.6 |
| 71a19229-c0bd-3ddb-acb9-3122defb3676 | -9.9148 | -47.8282 | 2025-07-11 01:30:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 274.0 |
| f61e7c21-ed72-3615-9e11-7e307d87d902 | -22.2733 | -54.919998 | 2025-07-11 01:33:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| becfb7be-2051-3847-a0e3-190d948f565c | -22.279301 | -54.941002 | 2025-07-11 01:33:00 | METOP-B | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 5e93db03-facd-3fee-b5d8-35e2792da835 | -10.8716 | -68.483299 | 2025-07-11 01:34:00 | METOP-B | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| 7022d3e9-384c-39bb-a380-61b630d0ce19 | -9.9503 | -64.948196 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 34e47249-1ab8-3371-9337-12a5abad37d0 | -9.9717 | -64.951599 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b94bc772-8698-3b87-8690-6748a90adeb3 | -9.9522 | -64.9562 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b175d892-0ace-3b7b-82ef-7dd2c7f489c0 | -9.9638 | -64.961899 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| b22581d2-6132-3004-b0af-19e23da2cb4e | -9.9736 | -64.959602 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| fd2cefac-9c49-30c4-b31d-7729d8a9fedf | -12.0977 | -64.2407 | 2025-07-11 01:34:00 | METOP-B | COSTA MARQUES | RONDÔNIA | Brasil | 1100080 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 799a428c-ef81-3c07-878a-04902e7a9e9b | -10.8732 | -68.490402 | 2025-07-11 01:34:00 | METOP-B | EPITACIOLÂNDIA | ACRE | Brasil | 1200252 | 12 | 33 | nan | nan | nan | Amazônia | nan |
| ce21310d-be8e-3071-821b-89b3762752e2 | -9.9424 | -64.958504 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| e64fa779-affb-3c04-b158-ea77479481ed | -9.9619 | -64.953903 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 6cc21b16-32d2-34fe-80af-e10d0f639981 | -9.9698 | -64.943604 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5609aae5-4921-3705-8aa8-1efd19e5079c | -9.9656 | -64.969803 | 2025-07-11 01:34:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 78462161-023a-3fc5-ab0d-edc43e09587a | -16.9555 | -49.446 | 2025-07-11 01:40:00 | GOES-19 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 00eede9c-2684-387b-93e1-2d85b7ba3923 | -9.8958 | -47.8303 | 2025-07-11 01:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 84.7 |
| 3a7f1924-d3d7-3351-b775-434369f5ad9f | -16.9362 | -49.4272 | 2025-07-11 01:40:00 | GOES-19 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 83.8 |
| dc1c5430-3e33-309a-bfe9-ea3e54d708b4 | -16.956 | -49.4237 | 2025-07-11 01:40:00 | GOES-19 | ARAGOIÂNIA | GOIÁS | Brasil | 5201801 | 52 | 33 | nan | nan | nan | Cerrado | 171.2 |
| 2e01e641-97c5-3a9d-b109-c2cb151448ae | -9.9148 | -47.8282 | 2025-07-11 01:40:00 | GOES-19 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 200.0 |
| f2bdc66f-95b6-3214-adce-a9ce697d991c | -10.6862 | -49.4874 | 2025-07-11 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 142.6 |
| 109074b8-57db-3c11-9354-b72e046acca5 | -22.2847 | -54.9627 | 2025-07-11 01:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 49.2 |
| cdf6e44b-4496-3481-a272-75f14f5654a4 | -10.6672 | -49.4895 | 2025-07-11 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 172.6 |
| a2f9ac3f-54bc-32e1-8dfb-0e7e097d0ecd | -22.2852 | -54.9409 | 2025-07-11 01:40:00 | GOES-19 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 57.8 |
| 26402a32-a7c8-3329-8be7-3b563f51f3e9 | -10.6859 | -49.509 | 2025-07-11 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 60.4 |
| d6c6fbd9-e269-3585-9fc3-10d78a90fc88 | -10.5776 | -49.1316 | 2025-07-11 01:40:00 | GOES-19 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 130.0 |


[Clique aqui para ver as próximas entradas](README5.md)
