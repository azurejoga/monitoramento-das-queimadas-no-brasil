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

## Dados Diários - Página 69

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7b01c363-c607-3966-ac3d-8e7a401c5178 | -9.21112 | -59.47817 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 32d21dec-12b0-3e9a-88ec-5a98732adec6 | -9.18571 | -59.63883 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| af4aeb4f-3e57-3320-9f0b-258280576cc7 | -13.37004 | -47.50068 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a766c5a-dd1a-3fcc-8b66-17979bb954a1 | -9.19781 | -59.45454 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7e395cc2-fb0f-3fc1-b8b3-58e41f8c1321 | -13.41538 | -46.2754 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d17a5a56-72bb-30ba-ac41-ac49c0ebc2bb | -9.2378 | -60.4748 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| cd54d315-d548-38ef-8ac2-8182ada9d3bc | -10.27711 | -46.75087 | 2025-08-23 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 18f27d73-9763-31b2-be42-a0dda370e94a | -7.09888 | -60.06184 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 57bae3f4-ab1b-3dd1-accd-05f34d77ff1d | -9.10289 | -61.43247 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 59b9b07b-8024-37f5-8441-ccb4cb7d5ac5 | -6.87519 | -59.82602 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 400af57c-5780-3744-a1b1-8d7454eeee84 | -12.31052 | -49.98813 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1a3bd360-d899-305f-bd93-f94d0ddeddbc | -9.25378 | -59.61388 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e008afa2-5db6-3d55-a555-9ca15bec8be6 | -9.52315 | -60.53911 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bacd6024-2f29-3b75-896a-623badc80df9 | -12.31746 | -49.99509 | 2025-08-23 05:21:00 | NPP-375D | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 51a5fc5e-b7f5-3f68-8f47-1aea73202a54 | -15.02193 | -54.87393 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 52c0764e-5142-342e-8e7b-6503372dbf8c | -9.20619 | -59.61707 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4c151657-61cc-3791-8113-e1b5323d406a | -10.27801 | -46.7431 | 2025-08-23 05:21:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 39d5bb2b-eb25-3111-be49-7f5ac9b812db | -14.6618 | -56.60997 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| b61b1603-4a0c-3c54-8ffe-34e9ef92f3fd | -15.03523 | -49.606 | 2025-08-23 05:21:00 | NPP-375D | ITAPACI | GOIÁS | Brasil | 5210901 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 861fb1c6-d360-30c7-a69c-ea626a070f15 | -9.19512 | -59.62246 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| e06d4a9f-5a90-3c16-8e65-42366fc1fb69 | -9.19013 | -59.63242 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e51a90b-cc02-3f0f-90bd-88debf689f63 | -14.66846 | -54.92775 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.8 |
| d166cb48-c5b6-38e7-b2e1-f8eef08d5989 | -14.3761 | -52.04629 | 2025-08-23 05:21:00 | NPP-375D | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6cd27423-455a-3adc-bcfe-cc56b548432a | -9.22782 | -59.69577 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3bb337a7-1238-33a0-bdb5-23447f9a88d8 | -11.97021 | -46.77173 | 2025-08-23 05:21:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 4a28b931-9452-3b26-97b0-0d0c3aed63bd | -7.79626 | -61.5829 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7c21a2ce-c59c-3630-ba07-dab3cbe5c8d2 | -11.9023 | -55.89935 | 2025-08-23 05:21:00 | NPP-375D | IPIRANGA DO NORTE | MATO GROSSO | Brasil | 5104526 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6f71604f-0558-3655-9c1c-97d605f43650 | -10.62963 | -52.34257 | 2025-08-23 05:21:00 | NPP-375D | SÃO JOSÉ DO XINGU | MATO GROSSO | Brasil | 5107354 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e176d9b2-0f96-386e-a9e8-c69eb5c53afb | -9.15689 | -59.60559 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 383effbf-eca3-3e64-b420-29adc6882281 | -8.66456 | -51.27988 | 2025-08-23 05:21:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d545cd33-967b-3b86-8166-2bd16ae97e85 | -13.37564 | -47.5121 | 2025-08-23 05:21:00 | NPP-375D | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 3.3 |
| de7a14c3-5f78-38b2-87e3-7e50bdddb9f0 | -7.54783 | -63.85587 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 2073e2d8-8734-32a6-8023-c07a8014ecbf | -12.79153 | -48.71831 | 2025-08-23 05:21:00 | NPP-375D | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 38749784-dbbd-3f43-97eb-3ebed681bb62 | -13.36966 | -54.40555 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 2e074252-b1a3-3c86-b87b-1e16f1d226dd | -9.20675 | -59.61357 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b9f91472-e630-312b-bfb5-ff551dd4a214 | -14.61914 | -54.81099 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e203719e-3348-351c-9b12-4a8c8a4790b5 | -9.16132 | -59.59913 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9dc1c46-594a-3967-841c-e9a57cc36a3a | -9.16464 | -59.59966 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f5fbc3cf-3f14-388b-9509-7f081778e3d2 | -15.07236 | -48.50635 | 2025-08-23 05:21:00 | NPP-375D | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 359fdb5f-2483-3f89-8cd8-352eff17817f | -9.37416 | -48.25538 | 2025-08-23 05:21:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| aa5237c2-6c15-32b0-a66f-867bddd555c7 | -9.19234 | -59.59694 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 45b584da-a783-3582-a5ea-a3422745b27d | -9.22339 | -59.76678 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41676d09-e30b-3fcb-8f8f-b249f0a624d5 | -9.17407 | -59.64771 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46425801-275e-35a6-9c11-7956867c389e | -9.19899 | -59.6195 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4de319e9-def9-3059-9494-30fd398ef1c0 | -9.09945 | -61.43189 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 280fc76d-0c30-3d88-9644-a3263f1ef941 | -7.81416 | -63.55596 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 39d2601b-3232-324d-8b42-f42281d4f22b | -9.20834 | -59.47414 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 31d25911-6137-35b4-ba70-edade68bcf44 | -9.18848 | -59.64285 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fccd2ae0-e277-3729-a407-09146f3828f7 | -12.49608 | -53.82356 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 41aa0a96-02c0-36ba-bc51-3b809fe34c18 | -15.03609 | -54.89879 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 48b2826e-64e8-3b59-b210-ca479fdb56c4 | -13.4621 | -47.02585 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 6.1 |
| 5119754e-7b82-37e8-b2f3-67a4bac7d563 | -11.50242 | -50.46738 | 2025-08-23 05:21:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d4a7bc75-af45-32b5-9813-144f3810b90d | -10.45978 | -59.13083 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2c19c3ca-e5a7-3462-8884-261b01ca7572 | -9.18791 | -59.62489 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| b1265779-f3e5-3bb0-8362-bda57856faae | -7.29443 | -59.6409 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bf72514-268b-3e4a-a523-9b9517c5e4de | -14.28138 | -58.52903 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9398328a-a981-3fb7-897d-5025fecda8aa | -13.04375 | -46.3323 | 2025-08-23 05:21:00 | NPP-375D | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 965d4b7d-63aa-30f6-b7c5-6a634720d4a8 | -7.50675 | -63.83302 | 2025-08-23 05:21:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1f4987bf-1a33-304a-ad3e-641a9df7aa46 | -7.29554 | -59.6339 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c15d4683-fe85-3a5b-b276-f5398ebc2e16 | -7.28634 | -57.65654 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2a36558d-5558-3e63-b28e-803dfba40fb8 | -7.78288 | -61.5767 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| fccc146b-9424-3aa1-890a-1534c39885c5 | -13.34306 | -54.39493 | 2025-08-23 05:21:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e83c4e53-a52e-3540-a7e7-96d468743d84 | -13.43003 | -57.16288 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e99057e8-33e1-35f8-9204-ca88842f02dd | -15.03186 | -54.89796 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 715067a5-fca0-3d84-8591-58374e00c707 | -9.19456 | -59.62595 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fdd06d4-ccdc-38c9-95bc-5b00a475802f | -9.51651 | -60.51606 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b7e5a771-95f4-37f3-9e3c-d5e164e5ef97 | -9.64769 | -59.64862 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| c8dd28e0-1984-3949-956d-d85918aa403f | -9.94499 | -60.18201 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e4499ca7-8112-3b8d-82ad-a3227611250f | -7.25418 | -57.68087 | 2025-08-23 05:21:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c5e632a-3dde-3ad6-9033-251d1f8ceeb5 | -7.31862 | -59.61239 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e5905459-5f0b-3dac-a426-8c080ebfd114 | -9.15467 | -59.59806 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3e706893-2027-338c-8b03-d9d88cc039c3 | -14.34015 | -58.5857 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b1b43ddd-295a-304b-a2a2-3949b2448170 | -14.66441 | -56.6123 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 14ac70e3-a96f-34e4-bb53-b5fa79d5a076 | -11.4667 | -58.16188 | 2025-08-23 05:21:00 | NPP-375D | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 87d5ca50-d589-3a77-8459-525a834b5b0d | -9.59767 | -55.34629 | 2025-08-23 05:21:00 | NPP-375D | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc15ad49-677c-3e82-a0fa-d71ea834ccee | -7.77938 | -61.57612 | 2025-08-23 05:21:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 40fa8092-47df-31d6-ac3a-8a2c530e788e | -8.87164 | -62.42367 | 2025-08-23 05:21:00 | NPP-375D | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d5d19961-48fa-31aa-affd-42fd0bf89f47 | -14.669 | -54.92372 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 7fba3708-6f24-3507-8014-9d53d0a47f05 | -9.17462 | -59.62276 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b199814d-71aa-356d-9f5d-45aac5306191 | -13.03212 | -56.87899 | 2025-08-23 05:21:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e3099e80-2c3b-3984-bd50-49843346decf | -9.18847 | -59.6214 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 1ec1eedd-4fc4-304d-abd3-dc44b96fcacd | -13.13347 | -46.90932 | 2025-08-23 05:21:00 | NPP-375D | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7fb212b8-b9b0-365b-a586-1fe01397d4b5 | -9.95996 | -60.19528 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 3d56bc82-af2a-361d-867e-8de610ea08e1 | -14.65207 | -54.9215 | 2025-08-23 05:21:00 | NPP-375D | NOVA BRASILÂNDIA | MATO GROSSO | Brasil | 5106208 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5ec7caee-38c9-3bc5-b113-66968371e7c8 | -9.17018 | -59.60772 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d4268ef7-a921-37f2-a387-07f461a4a890 | -9.21554 | -59.47171 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f066808a-186c-329d-af27-f2bdb7142c0c | -13.42336 | -46.26893 | 2025-08-23 05:21:00 | NPP-375D | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 7.2 |
| 61ca01b4-20b6-3c91-9ec5-b80701bbf220 | -14.91401 | -47.32277 | 2025-08-23 05:21:00 | NPP-375D | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 00785eee-d027-3053-84e7-8d79b7e684cc | -9.51259 | -60.51908 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f314351f-ca03-380e-b5f5-7af5ab368d43 | -14.47184 | -55.94739 | 2025-08-23 05:21:00 | NPP-375D | NOBRES | MATO GROSSO | Brasil | 5105903 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 94dd6a92-f05e-3d78-8146-3f9eb5bb4a87 | -14.6922 | -54.90911 | 2025-08-23 05:21:00 | NPP-375D | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b98a66f1-9dd8-3bfd-980b-33528ca56ed9 | -9.94667 | -60.17145 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77cb263c-fce9-3892-abbe-9db0e29cc81a | -9.22661 | -59.76366 | 2025-08-23 05:21:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d72abdf6-d5c6-3fac-930e-028ffa858769 | -15.21982 | -53.85649 | 2025-08-23 05:21:00 | NPP-375D | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 734e1b6b-d4db-3ef9-b0ea-c1acbbc92fc9 | -9.52657 | -60.5177 | 2025-08-23 05:21:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d9189848-dc30-3bd0-a135-8e13ba030045 | -14.66441 | -56.59166 | 2025-08-23 05:21:00 | NPP-375D | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| c4186136-dc02-3ea9-9b49-9a7c49e811bf | -11.18427 | -55.03487 | 2025-08-23 05:21:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7af217a4-d941-3607-a06a-eae73614c46e | -14.32692 | -58.5559 | 2025-08-23 05:21:00 | NPP-375D | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82f73ee6-7614-3b57-8012-ed90c3a73445 | -9.42948 | -62.25533 | 2025-08-23 05:21:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f46627fe-8c9d-37e2-92c5-d0d0fd6b653f | -7.04361 | -59.83528 | 2025-08-23 05:21:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README70.md)
