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
| 8578ff50-dcc6-3542-9825-5a4d6c224254 | -17.5824 | -39.46895 | 2026-03-18 04:25:00 | NOAA-20 | ALCOBAÇA | BAHIA | Brasil | 2900801 | 29 | 33 | nan | nan | nan | Mata Atlântica | 3.0 |
| 4b721762-ea99-3e88-8374-1af5e5fbccfe | -16.5748 | -57.80049 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 69c94f01-77fa-30f2-8d97-39bcd6c80530 | -16.57957 | -57.80597 | 2026-03-18 04:25:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| c89b75f5-9c0e-3f0d-b7f8-9ee34c87c37d | -25.51621 | -50.88287 | 2026-03-18 04:27:00 | NOAA-20 | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| b6e50f3d-d56d-335f-9f40-6bf2040e2b90 | -30.475 | -56.39341 | 2026-03-18 04:27:00 | NOAA-20 | QUARAÍ | RIO GRANDE DO SUL | Brasil | 4315305 | 43 | 33 | nan | nan | nan | Pampa | 2.0 |
| a7380fee-26a4-3e91-a44c-320fccc38cf8 | -25.51555 | -50.88681 | 2026-03-18 04:27:00 | NOAA-20 | IRATI | PARANÁ | Brasil | 4110706 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f7f51391-5324-3f89-b1c7-304939f7c42a | 2.93018 | -60.16847 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e34673c3-1344-309d-b44a-fc4ab7f223da | 3.20286 | -60.32328 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06ac4638-17b6-3183-a199-ddfd564838b4 | 0.53465 | -60.26859 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| acab2669-0a51-3c7e-98c8-67cd0dc55109 | 1.13733 | -60.51899 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9ca2a699-ad5e-3a93-b247-da96c4dab923 | 1.96328 | -60.56357 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 566c8fb5-7d66-3070-b439-3db2a965932d | 2.92785 | -60.16919 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6d3dda10-4ad2-3a86-b77d-f7643aed0dca | 1.41385 | -60.7578 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 554a3b3e-6af0-3103-be66-4c4db15791d7 | 1.54927 | -60.40294 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ee65fb95-7f5c-3edc-b199-163a42f38ae8 | 3.06087 | -60.76377 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 74613814-70ac-381a-984b-2c11bbfcc88f | 2.44038 | -60.2446 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| e672e146-4f69-327d-82b1-116514c97d2d | 3.40994 | -60.17696 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 231d26d8-efec-3dce-b875-545f05869afb | 1.08117 | -60.68291 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a981cb84-116a-31ef-8a08-7aaca7c33873 | 0.54006 | -60.2777 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60b8369c-e242-3c6c-a496-5c4df758e940 | 3.05257 | -60.76502 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f0da8459-71a3-34e5-9114-9cb18da6cc05 | 2.66429 | -60.10445 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8ef20424-070b-35d7-8d52-cd8b4366f237 | 1.08866 | -60.67818 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 3bac7f1c-3806-39c4-ad82-45a1d512f2b3 | 3.42199 | -60.1752 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c282f78c-b6db-38d0-8f2a-50c22ae9ca36 | 0.86228 | -60.25526 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 37ed0781-f727-39a7-97d2-0f00bebc6e75 | 3.73484 | -60.75436 | 2026-03-18 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bcce9aba-c3ca-356c-b754-9521387c60ef | 0.83015 | -60.10179 | 2026-03-18 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0f96f0c7-85d8-33a7-92e7-71759bbc0e78 | 0.52148 | -60.2606 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 73ace77a-1f62-3773-9cdb-94b6836f3ba3 | 2.52764 | -60.13213 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 7a78d9d7-4ca2-3479-83e2-5f5383f14503 | 0.56666 | -59.90698 | 2026-03-18 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 2fad608d-087c-3e80-aa01-40888ddda7f4 | 0.82941 | -60.09705 | 2026-03-18 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad1e54bf-ada5-33a8-996e-1e93ce5f63f6 | 1.08064 | -60.67941 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1879d95-2173-30c8-8038-e09cbfcee2bb | 3.41797 | -60.17579 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 813dc8e3-9897-350d-9654-f5ef289238a5 | 1.07717 | -60.68355 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 1b16283a-91f7-30c7-b041-91bbbeac664a | 1.80139 | -61.2272 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aab15301-48f4-3ecc-a387-6b4554f3cc5d | 1.15976 | -60.32998 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a62b656c-e20f-3872-a75f-920cf19ee762 | 0.52612 | -60.26487 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| dac007ce-3f69-321e-86a9-ee77e39b7d8e | 2.43986 | -60.24118 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1928794d-a045-38b8-ba71-ffefdfa9b7d8 | 3.16781 | -60.11743 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 90457451-04b6-3e7e-befe-c25921140c93 | 2.31114 | -60.2415 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 444adcda-f51f-34bd-bcb0-afd4dfaa655e | 3.05313 | -60.76878 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27250f8e-fb43-3c0d-9adc-c625faa06196 | 1.73379 | -60.53488 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b98e3fa6-582b-3767-b85b-0ba3c49efbea | -1.34229 | -53.16105 | 2026-03-18 05:10:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4e863dee-8b34-3dce-aae6-a5a973b05998 | 1.17157 | -60.30264 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e3e20c15-bc46-345b-a389-a838504f508b | 2.248 | -60.29852 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3cb8fb54-62fa-3fd4-9cf9-e53c8cc50f83 | 1.1881 | -60.2041 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e6fd5c7c-3744-3d34-b8f6-d296421b1540 | 1.98805 | -60.889 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 195ab716-5ea4-3f96-8aff-13e0a5440d97 | 2.31035 | -60.23628 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62dbd1ec-0eec-3246-8dfb-89e7125beec2 | 1.98393 | -60.88966 | 2026-03-18 05:10:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4c8239df-746a-31e2-ba6a-1a93b97faa23 | 3.06389 | -60.75564 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47e80a9e-80cc-359f-a82b-4a058f5214b0 | 3.05729 | -60.76817 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0f04a105-b668-343a-b471-e4c8e5ce732a | 1.87892 | -61.2276 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 0e254a56-0b78-3d4b-9477-9102de7e274e | 3.08221 | -60.76448 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 86f6be8e-37a7-38d5-80bd-b7d7626fcd11 | 3.20233 | -60.31972 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| afe02f40-709a-39aa-a125-233afba1875f | 3.78614 | -61.30094 | 2026-03-18 05:10:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e121bd22-73a4-3b36-b30b-693d9a88dc25 | 1.7209 | -60.2937 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 8de7f68e-0937-3e34-8e84-2980642d429f | 0.96085 | -59.55141 | 2026-03-18 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 511edeaf-f3ac-363f-b810-41714e2d2b1a | 1.07663 | -60.68006 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 491f78de-e0e5-3a8c-9b77-fc6f3ee76b57 | 3.40698 | -60.18458 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c7c78517-835d-3b3d-958d-f4c963deda0a | 0.89309 | -59.81099 | 2026-03-18 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 674ccee5-f994-3ece-a766-ed8703be7768 | 3.20636 | -60.31911 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 028faedb-7838-3d20-9d8f-c748752a3049 | 0.83561 | -60.33989 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9efa003c-a008-31ce-af85-7d5fd205b97d | 0.46803 | -60.40386 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| bff3ea2c-7aba-37fe-8036-88d405ef56b3 | 0.77413 | -59.86941 | 2026-03-18 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 812fbc93-72b3-3eb4-9bf1-1f982e81218e | 1.64439 | -60.29503 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d5e56781-9cb9-3332-a821-4748e43664c7 | 3.20179 | -60.31617 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc92f425-ad41-3001-86f5-a53b343b4a19 | 0.95486 | -60.22889 | 2026-03-18 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 972e02af-4acd-3cfe-827a-1b3144a8113a | 0.96458 | -59.55083 | 2026-03-18 05:10:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 10fd6bef-0d79-3f0a-ae0f-b81520afd205 | 0.46727 | -60.39892 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5d736cdc-09c1-33e1-ac18-935d6d2aa270 | 3.0603 | -60.76002 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9ff207e2-9692-31a6-80e5-b689eec3b9fb | 0.97281 | -60.00218 | 2026-03-18 05:10:00 | NOAA-21 | SÃO LUIZ | RORAIMA | Brasil | 1400605 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dadba245-6b83-38f7-9949-5da7fc730e01 | 3.05672 | -60.7644 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c80d58a-c7ce-32ab-869d-d7b9f109e90f | 3.41047 | -60.18048 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 950c4686-4b70-3f06-817b-d4b2577d2c63 | 3.07749 | -60.76132 | 2026-03-18 05:10:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b21af116-278d-37b1-83a8-582310bcc30b | 3.41395 | -60.17637 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a505b718-c944-3527-83cb-51c73d253ec9 | 0.46706 | -60.40207 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7fbab5f9-0952-3f58-a293-3f7c89cde9cc | 0.86155 | -60.22546 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e97754f-6dd6-3ce0-bfd9-1cf4cc45952b | 1.15583 | -60.33058 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 073d893e-d618-37d2-92e9-86c661d3b0e9 | 1.16765 | -60.30324 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9cf84678-7cb0-32c4-83a2-3bac19e6d573 | 0.83484 | -60.33494 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 93d79e97-67f2-38a3-a650-c5127e3a0271 | 2.83068 | -60.03824 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b6bad8e0-653c-3450-abdf-9b822e9d60aa | 1.0777 | -60.68705 | 2026-03-18 05:10:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 56e4e1c0-f552-3b6e-b38e-cefd33b54477 | 3.74195 | -60.77304 | 2026-03-18 05:10:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4a6df7ba-576d-3c44-bfb3-32d7ea810cf6 | 0.51761 | -60.26119 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| b1a21a33-dd09-3dda-93f0-0c068d1a71a9 | 2.66034 | -60.10504 | 2026-03-18 05:10:00 | NOAA-21 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 78049447-1143-3c54-b740-683f4107f59f | 0.77033 | -59.87 | 2026-03-18 05:10:00 | NOAA-21 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 2311b49d-fdbe-3fff-be41-b01d57f41681 | 0.53542 | -60.27346 | 2026-03-18 05:10:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ce950f81-5d3d-319b-bc29-a11c9c2d7c11 | -16.45216 | -58.17418 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 0b74dfaf-a878-3128-b7b1-84da07963231 | -16.4516 | -58.17794 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| 1ad4e4b0-d443-3bc1-b962-49cab766af97 | -16.44823 | -58.17739 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| ac7d73b8-91ca-3e2d-8df9-330b8b8f80a7 | -16.44878 | -58.17364 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.6 |
| bc9a5de8-95eb-333b-b4f1-b92b5406a449 | -16.44934 | -58.16988 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| d68b6be3-cd60-31a7-88ed-f186656d2c08 | -16.45498 | -58.17849 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 3ef022b5-3fe7-3f64-adf6-e66cdd940830 | -15.77761 | -59.67318 | 2026-03-18 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 12a2fdf0-3cd8-3711-bb61-3ffb4014a5a8 | -16.45554 | -58.17473 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 5357e0ee-0c39-36da-9c36-73714853a11c | -16.5805 | -57.80246 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| f09486d4-4059-3ad3-8578-a3f4e654999c | -16.58814 | -58.22223 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f7db873b-eab6-3bb1-bfb2-5466834e4ed8 | -16.57708 | -57.8019 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 286bd691-d7d7-3e72-8b85-6f1f02563638 | -14.07493 | -58.53173 | 2026-03-18 05:14:00 | NOAA-21 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.3 |
| e705c19e-074d-32c8-a8dc-19ace6524231 | -16.4454 | -58.1731 | 2026-03-18 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 927459c6-4323-3922-b26b-4cc6c5905e56 | -15.59449 | -59.29896 | 2026-03-18 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README3.md)
