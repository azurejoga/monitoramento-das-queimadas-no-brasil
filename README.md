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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e7eb6ecc-cb04-3946-bf87-ad0806f986dc | -9.8854 | -36.6438 | 2026-02-07 00:00:00 | GOES-19 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Caatinga | 93.4 |
| 0982fc33-597e-366f-b166-d6b659189cdb | -9.8859 | -36.617 | 2026-02-07 00:00:00 | GOES-19 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Mata Atlântica | 80.5 |
| 6321f00b-59ef-3bc3-8499-00e7a4dcd06d | 2.1949 | -61.9096 | 2026-02-07 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 46.3 |
| 627092ab-594d-34ea-86f9-4cb7b64cabce | 2.1766 | -61.9286 | 2026-02-07 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.5 |
| fbe57a6f-9156-38bf-9767-00058607ddd6 | 2.1948 | -61.9284 | 2026-02-07 00:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 3afdecd1-41ce-366b-a463-7426d216cc02 | -9.8661 | -36.6472 | 2026-02-07 00:00:00 | GOES-19 | FEIRA GRANDE | ALAGOAS | Brasil | 2702603 | 27 | 33 | nan | nan | nan | Caatinga | 60.0 |
| 3a36928e-fb27-36fb-a3f5-e679be7f7bd4 | 1.3585 | -60.065 | 2026-02-07 00:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 57.1 |
| e9815ffe-6bbf-3cbc-8fc3-07e6b8e9acbc | 1.3585 | -60.065 | 2026-02-07 00:10:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 56.5 |
| dbd8d3f3-6d72-32c0-bffc-076383524c51 | 1.3585 | -60.065 | 2026-02-07 00:20:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 87d5cbfe-c52e-3a32-8dd3-24b2e2e25823 | -13.9409 | -39.9629 | 2026-02-07 00:20:00 | GOES-19 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 66.1 |
| 2008da15-4a66-3da9-a9bd-825a30793616 | -22.02931 | -49.49986 | 2026-02-07 00:24:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| c46b2631-e9dd-312b-b7bc-c19d4a6dae28 | -24.69953 | -47.89613 | 2026-02-07 00:24:00 | TERRA_M-M | PARIQUERA-AÇU | SÃO PAULO | Brasil | 3536208 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 9f35e654-c2ae-37e4-a11b-059422cdc55d | -22.02333 | -49.50711 | 2026-02-07 00:24:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 19.1 |
| 895a9606-75eb-35f9-aa26-fbe81e27c9c1 | -22.02198 | -49.4966 | 2026-02-07 00:24:00 | TERRA_M-M | PIRAJUÍ | SÃO PAULO | Brasil | 3538907 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.0 |
| c72daf9e-4752-366e-afcf-26db2fa90b92 | -16.27326 | -43.75495 | 2026-02-07 00:24:00 | TERRA_M-M | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 6085963c-65a9-3630-bbf4-ec6638534ff5 | -17.41188 | -39.3452 | 2026-02-07 00:24:00 | TERRA_M-M | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 34.6 |
| 7d1a5b58-9cea-3d11-b44d-de3b351482a0 | -13.93605 | -39.96363 | 2026-02-07 00:26:00 | TERRA_M-M | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 158.7 |
| f42690ce-29fb-3a01-885c-fdcbe73e0795 | -3.53857 | -45.52141 | 2026-02-07 00:28:00 | TERRA_M-M | MONÇÃO | MARANHÃO | Brasil | 2106904 | 21 | 33 | nan | nan | nan | Amazônia | 37.7 |
| d20db91a-ebea-3af3-941c-715b315d7f03 | 2.1766 | -61.9286 | 2026-02-07 00:30:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 46.4 |
| fe7fa4fc-5060-316d-8710-4a085e922c4b | -13.9409 | -39.9629 | 2026-02-07 00:30:00 | GOES-19 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 65.4 |
| d7f9924e-3681-3608-a2a6-829f7cfde6df | -10.0433 | -36.4285 | 2026-02-07 00:30:00 | GOES-19 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | 135.0 |
| d9194332-5a47-301c-88d0-488a86f7b4dd | -1.45575 | -46.10123 | 2026-02-07 00:30:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 13648ad0-aa41-3f5d-b476-378c18a317bf | -1.45943 | -46.09418 | 2026-02-07 00:30:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 27.1 |
| 21fcc9bf-6e31-3dab-be58-19c14ad5d0be | -1.45327 | -46.0835 | 2026-02-07 00:30:00 | TERRA_M-M | CARUTAPERA | MARANHÃO | Brasil | 2102903 | 21 | 33 | nan | nan | nan | Amazônia | 17.2 |
| d34c5990-5f24-377b-9fed-c49cce93e989 | 2.08903 | -60.21041 | 2026-02-07 00:32:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 67ed65f4-54b9-36f9-ac92-fc8e7a693775 | 2.80396 | -60.27206 | 2026-02-07 00:32:00 | TERRA_M-M | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 05386b50-f985-3e00-8fdc-91d4dd504a5e | -9.8537 | -36.2736 | 2026-02-07 00:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 77.1 |
| 5940da37-1b7c-397a-91fb-bd1c7d481194 | -9.8349 | -36.2499 | 2026-02-07 00:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 186.6 |
| 53627951-26c0-35fa-9c53-55a43152a850 | -9.8542 | -36.2465 | 2026-02-07 00:40:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 185.1 |
| e2bbeb39-9c03-3f02-af89-6a3d8394ed50 | -13.9409 | -39.9629 | 2026-02-07 00:50:00 | GOES-19 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 77.3 |
| c0234f7a-4729-3872-88ae-c2647c04c1e9 | -9.8349 | -36.2499 | 2026-02-07 00:50:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 230.0 |
| 2558dc8f-dfa3-3e54-abf4-51a5622b6358 | 2.1766 | -61.9286 | 2026-02-07 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.2 |
| 64796b03-9f6c-3000-859d-1ce8d0f0c48b | -9.8542 | -36.2465 | 2026-02-07 00:50:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 171.2 |
| 420371aa-8971-33e8-921f-c3c6cf97b6e0 | 2.1949 | -61.9096 | 2026-02-07 00:50:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 47.4 |
| 2b7ea76c-009b-3152-9fe7-048e792be11e | -9.8542 | -36.2465 | 2026-02-07 01:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 85.1 |
| c6226e0a-1006-300e-b145-cb95c75b0568 | -8.889 | -35.405 | 2026-02-07 01:00:00 | GOES-19 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 79.7 |
| 40736df5-f2f0-318c-97a0-6086fe3e32f7 | 1.3585 | -60.065 | 2026-02-07 01:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 45.9 |
| 26ae29c4-34f2-3fcf-a902-14d80ae92f87 | -9.8349 | -36.2499 | 2026-02-07 01:00:00 | GOES-19 | CAMPO ALEGRE | ALAGOAS | Brasil | 2701407 | 27 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| c77e4e3f-9935-3558-a364-0d6972c91c55 | -13.9409 | -39.9629 | 2026-02-07 01:00:00 | GOES-19 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 68.1 |
| d31f4730-43b0-345a-94c1-7d37f9de038a | 2.1948 | -61.9284 | 2026-02-07 01:00:00 | GOES-19 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 48.8 |
| b24591d6-a97b-3019-92f2-7be0dbd0002a | -8.8698 | -35.4081 | 2026-02-07 01:10:00 | GOES-19 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 78.7 |
| 7e4d2042-f84f-3655-8c8e-ae6e6d1f6099 | -8.889 | -35.405 | 2026-02-07 01:10:00 | GOES-19 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 96.0 |
| d9c30353-3692-306c-b5f7-d88dac23572f | -13.9409 | -39.9629 | 2026-02-07 01:10:00 | GOES-19 | JITAÚNA | BAHIA | Brasil | 2918308 | 29 | 33 | nan | nan | nan | Mata Atlântica | 76.6 |
| 18da0a08-8d5f-3042-9528-49b3ea81d9c9 | -27.520399 | -50.990002 | 2026-02-07 01:15:00 | METOP-C | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 03a1d9c1-fc22-32c6-be19-cbc63ed8034c | -20.7281 | -55.144501 | 2026-02-07 01:15:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 3fb83e8d-758d-3de6-be89-e58a9c0f56ab | -24.138201 | -51.6297 | 2026-02-07 01:15:00 | METOP-C | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 70756a20-240b-3a2d-ae32-9b912b9ec26d | -6.5817 | -51.070702 | 2026-02-07 01:15:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b82d7d68-022c-395f-9aa4-eac284a9fffb | -20.7265 | -55.137199 | 2026-02-07 01:15:00 | METOP-C | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 63c17adc-ef1a-30ef-850a-2e74c4c3488f | -27.518499 | -50.9818 | 2026-02-07 01:15:00 | METOP-C | VARGEM | SANTA CATARINA | Brasil | 4219150 | 42 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 66d6799d-e51c-37dd-80f8-045d48e9de86 | -15.8936 | -58.266602 | 2026-02-07 01:15:00 | METOP-C | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| c1fb0bec-e122-3b99-9a25-6d876e7a8f50 | -6.5719 | -51.073101 | 2026-02-07 01:15:00 | METOP-C | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac6eaced-8666-3be0-9fea-182bec3a08b3 | -15.8919 | -58.258801 | 2026-02-07 01:15:00 | METOP-C | GLÓRIA D'OESTE | MATO GROSSO | Brasil | 5103957 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 9f8cf589-9bac-3b06-8153-9810dc930ce4 | -24.136299 | -51.621498 | 2026-02-07 01:15:00 | METOP-C | LIDIANÓPOLIS | PARANÁ | Brasil | 4113429 | 41 | 33 | nan | nan | nan | Mata Atlântica | nan |
| 1df9cae8-f3ae-3d6b-915f-29b16552813a | -8.889 | -35.405 | 2026-02-07 01:20:00 | GOES-19 | JACUÍPE | ALAGOAS | Brasil | 2703502 | 27 | 33 | nan | nan | nan | Mata Atlântica | 62.0 |
| 1410894a-1a0d-3ea6-8c87-ba5504d4f166 | 1.3585 | -60.065 | 2026-02-07 01:30:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 46.2 |
| ad6668b4-10a9-35e3-9c9a-1e7a75d5efdd | -12.39115 | -37.91163 | 2026-02-07 03:14:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| ee7c7500-7e31-3eea-b336-62be71a23bde | -13.4986 | -41.3786 | 2026-02-07 03:14:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 968a43d0-21e3-3b4c-9364-375d0ac1e1fc | -13.50599 | -41.37504 | 2026-02-07 03:14:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 8a976970-5bab-3764-9933-e6bd3cf00966 | -12.39054 | -37.91488 | 2026-02-07 03:14:00 | NOAA-20 | ITANAGRA | BAHIA | Brasil | 2915908 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7556ba7c-c19d-3ebf-87dc-8e89e666e9e1 | -10.1738 | -36.69481 | 2026-02-07 03:14:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 500ea73e-2e87-3752-b783-7f0d763795a6 | -13.50494 | -41.38 | 2026-02-07 03:14:00 | NOAA-20 | BARRA DA ESTIVA | BAHIA | Brasil | 2902807 | 29 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 4adccdb8-9ffb-34d2-8221-a4e0969f62b5 | -10.17326 | -36.69769 | 2026-02-07 03:14:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d78f79dc-92e1-3548-8e76-1563ab87d161 | -11.01069 | -37.65522 | 2026-02-07 03:14:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 814c9061-cda2-33cc-8f70-764be868648b | -11.01131 | -37.65196 | 2026-02-07 03:14:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9d16a8b9-4153-3530-8df7-469a28593826 | -16.28852 | -40.77852 | 2026-02-07 03:14:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 6c94f1f5-a0ec-3acf-b51c-88e10be5f73a | -14.78546 | -40.39365 | 2026-02-07 03:14:00 | NOAA-20 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 0b70fb5d-9d45-3e07-8934-310c6038e0cf | -11.00603 | -37.65096 | 2026-02-07 03:14:00 | NOAA-20 | LAGARTO | SERGIPE | Brasil | 2803500 | 28 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 05d18891-ec75-307b-89ca-fb55d2121012 | -10.17435 | -36.69187 | 2026-02-07 03:14:00 | NOAA-20 | IGREJA NOVA | ALAGOAS | Brasil | 2703205 | 27 | 33 | nan | nan | nan | Caatinga | 1.3 |
| e931be01-d6c0-3ba6-a2c3-dec46bdec321 | -10.00664 | -36.02999 | 2026-02-07 03:14:00 | NOAA-20 | JEQUIÁ DA PRAIA | ALAGOAS | Brasil | 2703759 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| 1f0bb54d-d3d6-3d9e-8a2c-feca43d161fa | -16.28741 | -40.77741 | 2026-02-07 03:17:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a17eb8d8-73c8-3c0d-bed3-709ebf54ee32 | -16.28642 | -40.78203 | 2026-02-07 03:17:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| 0cce7c93-323a-3731-a4f7-031ac29e04c3 | -17.41607 | -39.35624 | 2026-02-07 03:17:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 26a40e54-3fe4-3330-a96f-7fb5d8962ece | -16.29225 | -40.78329 | 2026-02-07 03:17:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 719309a4-0d9f-36af-9301-9f96b2908841 | -16.29326 | -40.77862 | 2026-02-07 03:17:00 | NOAA-20 | JEQUITINHONHA | MINAS GERAIS | Brasil | 3135803 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 61109e23-9ba0-3b94-8d2a-0c7416b287d1 | -8.99966 | -35.43874 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 5c27b77c-014d-3237-af59-a2c0355f21f4 | -9.86144 | -36.52576 | 2026-02-07 04:01:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 8ab28f72-6c26-37e4-bc26-4eca7079ff5e | -8.99911 | -35.44254 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| e0a89eb0-6f49-35a6-a749-ceadd52d8c19 | -5.81701 | -43.96978 | 2026-02-07 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 33924800-d565-3767-971a-f61219702108 | -5.85489 | -44.94639 | 2026-02-07 04:01:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3d185660-fe4c-326c-8c60-af482607db38 | -8.99098 | -35.44131 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 4326d085-fe8c-3a8b-9732-41de9da0a71b | -5.78898 | -43.7416 | 2026-02-07 04:01:00 | NOAA-21 | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 3360be7f-2ac8-39e9-90f3-cae98503ee82 | -7.01882 | -42.86772 | 2026-02-07 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 71e93068-83c0-3677-8060-9b4c9fbf944b | -7.02233 | -42.86827 | 2026-02-07 04:01:00 | NOAA-21 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 021c0807-5826-3ca9-b859-cb00ccd09d13 | -9.86075 | -36.53064 | 2026-02-07 04:01:00 | NOAA-21 | SÃO SEBASTIÃO | ALAGOAS | Brasil | 2708808 | 27 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 5c146cc8-13d1-3f72-b885-0c7f4e8e96f0 | -8.99153 | -35.43755 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| d910332c-5442-3334-9712-c11964feabff | -5.96342 | -43.52795 | 2026-02-07 04:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 00e276f7-f2fc-3acb-a0fc-3eb164bf15a1 | -5.85145 | -44.9423 | 2026-02-07 04:01:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 351ce165-29b1-32e4-8c14-46160706d22c | -5.96709 | -43.52853 | 2026-02-07 04:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 014ab6ef-3eb2-38ba-8184-83c8e1d2cb3e | -7.02168 | -42.87221 | 2026-02-07 04:01:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 5b0cdae4-0b89-352e-a583-b9f6d31c34fe | -6.46967 | -43.55452 | 2026-02-07 04:01:00 | NOAA-21 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78ab25a8-b712-3499-9cc4-da00690e3cb8 | -8.99856 | -35.44631 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.4 |
| 1911bf9c-84d0-368b-a770-c4702eba9e2f | -8.99559 | -35.43817 | 2026-02-07 04:01:00 | NOAA-21 | PORTO CALVO | ALAGOAS | Brasil | 2707305 | 27 | 33 | nan | nan | nan | Mata Atlântica | 4.3 |
| 304510e8-af98-3988-9a45-69161814a647 | -6.25447 | -42.5843 | 2026-02-07 04:01:00 | NOAA-21 | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 0.4 |
| d834a905-27a8-32e5-b575-6ec294fe1fe7 | -9.81331 | -38.1058 | 2026-02-07 04:01:00 | NOAA-21 | SANTA BRÍGIDA | BAHIA | Brasil | 2927606 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 031a154a-5cbd-3492-b437-a2bcda218929 | -5.9678 | -43.5242 | 2026-02-07 04:01:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6fab10bb-c4a5-305a-beef-32fd0cbf7806 | -10.5598 | -38.98403 | 2026-02-07 04:04:00 | NOAA-21 | EUCLIDES DA CUNHA | BAHIA | Brasil | 2910701 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| dffba325-f8c2-349b-aac0-926f513f888c | -15.42972 | -41.43077 | 2026-02-07 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 706cc73b-bca9-37b4-be5d-54735d8c5ec6 | -13.25188 | -43.60357 | 2026-02-07 04:04:00 | NOAA-21 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 94fc27e9-485f-30e6-a0cc-57065a651e68 | -15.42364 | -41.42609 | 2026-02-07 04:04:00 | NOAA-21 | CÂNDIDO SALES | BAHIA | Brasil | 2906709 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| c7300394-4f57-33ff-9024-9a0fc9a2a7eb | -14.78555 | -40.39527 | 2026-02-07 04:04:00 | NOAA-21 | PLANALTO | BAHIA | Brasil | 2925006 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |


[Clique aqui para ver as próximas entradas](README2.md)
