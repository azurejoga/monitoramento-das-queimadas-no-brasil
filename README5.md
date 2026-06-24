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

## Dados Diários - Página 5

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b572fa25-eaf4-3e5f-a589-81481124fe63 | -10.27977 | -60.54203 | 2026-06-24 01:22:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 15.0 |
| 7bfd0fcf-f4b7-3b2d-8e26-f3443619d515 | -9.12632 | -65.98479 | 2026-06-24 01:24:00 | TERRA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a9104175-2045-33fb-a8e8-fb4de9be1002 | -13.0827 | -53.3524 | 2026-06-24 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 58.1 |
| cc5f13b7-59e4-3b86-a624-829fecd34f48 | -6.3703 | -43.5898 | 2026-06-24 01:30:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| a0f15f7d-cc5b-355f-a3a8-cf9a2e53526e | -12.7953 | -44.4426 | 2026-06-24 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 43.8 |
| 7ff9377f-4574-3da5-908a-63acade4e299 | -13.1832 | -43.4076 | 2026-06-24 01:30:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| 5ddbd20a-a269-37b2-8472-eaf1f87626be | -11.2595 | -43.3672 | 2026-06-24 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 71.8 |
| eef42331-e2cd-3cc0-9f3a-76c3f72410d2 | -12.776 | -44.4458 | 2026-06-24 01:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 0fe8a5d5-a780-3e94-beb8-28fad2c2acc9 | -13.0635 | -53.3546 | 2026-06-24 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 138.5 |
| bd21a80f-2ac7-3122-9e5f-b3f0634e5bfd | -13.0632 | -53.3754 | 2026-06-24 01:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 54.1 |
| a60c22cc-d095-38c5-8ab2-e25eb81b4e8d | -11.2599 | -43.3434 | 2026-06-24 01:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 103.3 |
| 9232bc95-fbe2-30d5-84da-1c1ec0ca85db | -6.3703 | -43.5898 | 2026-06-24 01:40:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 99.1 |
| 7e91648e-28ed-3b03-9ca5-27bf4f36df88 | -12.7953 | -44.4426 | 2026-06-24 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 42.7 |
| 9da8e517-1b64-3e76-ae15-a32f5b33420f | -13.0827 | -53.3524 | 2026-06-24 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 59.2 |
| 67faa92d-f155-3242-a6cd-07a790c8cacb | -11.2599 | -43.3434 | 2026-06-24 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 91.9 |
| 5aae6fa3-1961-30cf-855b-8c2e2b61c0b9 | -9.212 | -45.3321 | 2026-06-24 01:40:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 55.9 |
| d1b33629-8803-3de3-aa48-fcfc42f230be | -12.776 | -44.4458 | 2026-06-24 01:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.2 |
| 82f36743-1404-3886-aa22-40b464e7e050 | -13.1832 | -43.4076 | 2026-06-24 01:40:00 | GOES-19 | BOM JESUS DA LAPA | BAHIA | Brasil | 2903904 | 29 | 33 | nan | nan | nan | Cerrado | 56.6 |
| bd4b79d4-8450-360d-8b4e-4dd64c1d4bbb | -13.0635 | -53.3546 | 2026-06-24 01:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 125.7 |
| 4073013c-dc0a-3718-8750-ef37ef59a9b6 | -11.2407 | -43.3464 | 2026-06-24 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 54.7 |
| 7ad0eeef-28ec-313c-9d7f-2458e19f2810 | -11.2595 | -43.3672 | 2026-06-24 01:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.6 |
| be49ed6e-47d0-365d-add2-cbad807c87fc | -11.2407 | -43.3464 | 2026-06-24 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| c6aa0504-a6aa-39fc-b030-d901a895cee4 | -6.3703 | -43.5898 | 2026-06-24 01:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 92.4 |
| 771bcffd-5df7-3760-a575-86ce2ba09b46 | -9.212 | -45.3321 | 2026-06-24 01:50:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 49.2 |
| dfaa5104-09c9-32bb-a487-f0d4e61ad075 | -12.776 | -44.4458 | 2026-06-24 01:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 59.2 |
| b4d0eec4-ffd1-3562-b325-827bd806b67c | -13.0635 | -53.3546 | 2026-06-24 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 108.6 |
| dd16e5d5-1c51-3ec6-b796-55e88de7cab5 | -13.0827 | -53.3524 | 2026-06-24 01:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 60.4 |
| d980e646-6a20-3f5d-aae7-832e0bab8dc8 | -11.2599 | -43.3434 | 2026-06-24 01:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 78.6 |
| 070c0d28-4a4a-3e84-932a-38031500bf08 | -6.3703 | -43.5898 | 2026-06-24 02:00:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 97.1 |
| 5e62c35f-c68f-362a-9cbe-00e7994a9bf5 | -9.2309 | -45.3299 | 2026-06-24 02:00:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 52.4 |
| e83e3319-eb1b-34c9-9da7-55a82662acf5 | -12.776 | -44.4458 | 2026-06-24 02:00:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 48.2 |
| 15819a85-10ac-3ae9-82f0-b6e23050bf47 | -13.0635 | -53.3546 | 2026-06-24 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 103.4 |
| aaa951b1-47c3-3ef4-bd79-c7eeb37faf94 | -13.0827 | -53.3524 | 2026-06-24 02:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.2 |
| 8cdcd295-fe1b-3d59-a320-f8e64c4d3b4e | -6.3703 | -43.5898 | 2026-06-24 02:10:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 84.9 |
| 4157c018-a1ff-3bd2-8f4f-07f5bef6ff57 | -12.8349 | -44.3892 | 2026-06-24 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 47.2 |
| f5894713-fdd5-3869-b526-267e1d511be0 | -12.8548 | -44.3625 | 2026-06-24 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 450.8 |
| 2642d217-37b0-3386-8db9-f7d91ec9b0f6 | -12.8354 | -44.3657 | 2026-06-24 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 665.3 |
| 86f3c558-a2e4-354a-902f-c4dbee15fb4c | -13.0635 | -53.3546 | 2026-06-24 02:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 95.2 |
| 8efc645a-7e89-3a4c-bf3c-e2dcedd7e1a4 | -13.0827 | -53.3524 | 2026-06-24 02:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 72395043-a239-3428-afb0-7899c7976835 | -9.2309 | -45.3299 | 2026-06-24 02:10:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 1b25d484-96a6-30a3-869e-f70a2c85a100 | -12.8359 | -44.3422 | 2026-06-24 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 273.5 |
| b35c33f6-baee-3131-81bd-7cf25d455d75 | -12.8552 | -44.3389 | 2026-06-24 02:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 178.3 |
| d84fe14e-e533-3b00-aa22-4ce18f742da6 | -12.8354 | -44.3657 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 567.5 |
| d587d9e5-898b-3020-8456-9578bdb9b7d9 | -13.0635 | -53.3546 | 2026-06-24 02:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.7 |
| 4a6ff0e4-ed0f-3143-80a4-d58383eb7f8c | -12.8359 | -44.3422 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 281.7 |
| fd68873b-0cbb-3f2e-8205-750c284ebbc9 | -13.0827 | -53.3524 | 2026-06-24 02:20:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 67.1 |
| b4ac7987-3fde-3ce7-bc2f-f861902dd9eb | -12.8548 | -44.3625 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 368.8 |
| 47ca5457-67ec-34bb-9065-e7b758bf6086 | -12.8552 | -44.3389 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 176.8 |
| c5de42c6-1f18-3582-bf18-af2cec04bc2e | -12.8349 | -44.3892 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.4 |
| 77ee8fc5-5d43-32e9-b8bb-7797f9e6ebbd | -12.8543 | -44.386 | 2026-06-24 02:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 57.0 |
| fce907d3-4e3c-35f2-82c0-3948c470e5ac | -11.2403 | -43.3701 | 2026-06-24 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 165.7 |
| 4f76f599-9a52-3035-8db2-1e8ea8dd82a4 | -12.8349 | -44.3892 | 2026-06-24 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.4 |
| e23a130d-b405-3592-8331-8b54eca2962a | -11.2599 | -43.3434 | 2026-06-24 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 105.3 |
| 9e009168-780e-3e21-90e5-6a2626cf09fd | -12.8548 | -44.3625 | 2026-06-24 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 383.0 |
| dddb725e-18c5-3653-9aa5-6c594285e7c2 | -11.2595 | -43.3672 | 2026-06-24 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 52ed035a-d6c9-3a71-b7b4-c6b6048921ac | -12.8354 | -44.3657 | 2026-06-24 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 640.7 |
| 8a37814a-ca4e-3762-84de-5fac16f2c5e7 | -13.0827 | -53.3524 | 2026-06-24 02:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| c34126e3-4495-323e-82ee-0ded29ae36c1 | -12.8359 | -44.3422 | 2026-06-24 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 265.5 |
| 1d1ffad6-1e7f-330f-8fd2-21696d1d7d7f | -11.2407 | -43.3464 | 2026-06-24 02:30:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 224.6 |
| f5073b0e-26f7-343f-878c-e6d4f513a084 | -12.8552 | -44.3389 | 2026-06-24 02:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 145.4 |
| b582d7ec-c643-3d4b-9425-950dceee349e | -13.0635 | -53.3546 | 2026-06-24 02:30:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| c53e09fe-5ef3-35f3-9891-304efa0cf35d | -12.8349 | -44.3892 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 67.1 |
| 5b01c426-926a-3162-9145-6a8f859855ae | -12.8543 | -44.386 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 41.6 |
| 647684b5-8027-35af-88f5-f0636e32dd1c | -12.8359 | -44.3422 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 293.2 |
| 1876a3bf-47c9-30b8-aa19-2beb10115757 | -11.2403 | -43.3701 | 2026-06-24 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 108.7 |
| 4b367ec0-dd10-305b-965b-6b860bf0bcdd | -12.8354 | -44.3657 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 536.0 |
| c2a425da-9bae-3341-aa3d-3aa6d0913b2a | -13.0635 | -53.3546 | 2026-06-24 02:40:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 83.3 |
| 74a2f8b0-b9c2-34f0-99d4-c00d842a95ee | -11.2599 | -43.3434 | 2026-06-24 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 76.8 |
| 0d2424d0-2641-37ef-be12-35f3bb0af3d7 | -12.8552 | -44.3389 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 169.9 |
| d027b0d1-0c98-334d-b568-ad66bb101c50 | -12.8548 | -44.3625 | 2026-06-24 02:40:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 319.5 |
| 11c38a0b-0fbd-3e77-89d7-3564d6af7bd1 | -11.2595 | -43.3672 | 2026-06-24 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.3 |
| aebcbe40-c41d-36d3-a3de-26ba951dac06 | -11.2407 | -43.3464 | 2026-06-24 02:40:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 119.8 |
| 96dca4de-2a45-3e8c-8bbd-e0a6d32adb10 | -11.2595 | -43.3672 | 2026-06-24 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 68.0 |
| c0b8570f-cba7-3c26-b5cf-37344a4e7114 | -12.8543 | -44.386 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 45.7 |
| 20aac3c7-fcd0-3245-adcc-c3cf47d3d33b | -12.8354 | -44.3657 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 545.7 |
| 877f7e8d-3bd7-3634-8b46-f4256209e6bc | -12.8349 | -44.3892 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 50.6 |
| b5066936-4324-3c45-baca-6c9a10744f67 | -11.2403 | -43.3701 | 2026-06-24 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 159.1 |
| c5c58d96-aba3-3fdb-9bfd-e3e30fab3638 | -13.0635 | -53.3546 | 2026-06-24 02:50:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 98.9 |
| c9a72321-fe57-3178-a8bd-b79b39f44779 | -12.8548 | -44.3625 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 385.0 |
| 9d6d3bf2-8922-3e4e-b1c3-d00935d9a045 | -11.2407 | -43.3464 | 2026-06-24 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 163.0 |
| 92a0d23b-047d-3b15-b474-1c38f3bb2a70 | -12.8359 | -44.3422 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 213.0 |
| b19c5da5-8c13-3ebf-a2c4-218129346ffc | -11.2599 | -43.3434 | 2026-06-24 02:50:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 71.9 |
| bea7abd1-0910-3aff-b271-9ff3841cc54e | -6.3703 | -43.5898 | 2026-06-24 02:50:00 | GOES-19 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 55.5 |
| fe68bbb4-8f42-3325-bd0c-779ee2c350aa | -12.8552 | -44.3389 | 2026-06-24 02:50:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 137.5 |
| b4f37466-3be9-360d-9080-5fe58f8b4743 | -5.51149 | -35.59745 | 2026-06-24 02:51:00 | NOAA-21 | TAIPU | RIO GRANDE DO NORTE | Brasil | 2413904 | 24 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 4ced24b1-0b08-3603-a2f9-544018648e8b | -11.2403 | -43.3701 | 2026-06-24 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 63.5 |
| fb3e587e-d754-348f-93b9-ea17e997c5f7 | -11.2407 | -43.3464 | 2026-06-24 03:00:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 75.2 |
| 081f5c9d-5cb8-37e9-80b0-848c7ed0a17c | -15.6928 | -49.7915 | 2026-06-24 03:00:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 71.6 |
| e8e8e118-7e25-3c64-a16f-cec0ceec3757 | -13.0635 | -53.3546 | 2026-06-24 03:00:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 96.9 |
| 0a868086-eef8-3bb8-88eb-82c223165ac8 | -12.8354 | -44.3657 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 485.5 |
| 516affe2-2655-3859-a8a8-30f86eb8ab8b | -15.6928 | -49.7915 | 2026-06-24 03:10:00 | GOES-19 | HEITORAÍ | GOIÁS | Brasil | 5209606 | 52 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 9ed5fe81-547a-3024-beac-700829fa115f | -12.8359 | -44.3422 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 210.0 |
| 23bd78f7-e41b-36d8-b3af-547033b8c150 | -13.0635 | -53.3546 | 2026-06-24 03:10:00 | GOES-19 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 89.0 |
| d0e67e17-8a34-3ed1-859a-c231d49e4028 | -12.8349 | -44.3892 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 55.0 |
| 4d1df1c5-b2af-3c15-8d81-8128cb7b9346 | -12.8552 | -44.3389 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 140.7 |
| a9a52583-2ea0-3f4b-8529-b7dedf0312fa | -12.8543 | -44.386 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 49.8 |
| 5b590837-e5fc-3b33-825f-6bee95f5ce86 | -12.8548 | -44.3625 | 2026-06-24 03:10:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 352.7 |
| c2236d06-1b8b-3474-95ca-8f84e22de00d | -11.2403 | -43.3701 | 2026-06-24 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 72.6 |
| 697bf65b-1467-3f03-8d9b-4e45168b232e | -11.2407 | -43.3464 | 2026-06-24 03:10:00 | GOES-19 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Caatinga | 85.5 |
| deb41e63-b939-3755-8c12-68c9ac068e9b | -12.8354 | -44.3657 | 2026-06-24 03:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 464.9 |


[Clique aqui para ver as próximas entradas](README6.md)
