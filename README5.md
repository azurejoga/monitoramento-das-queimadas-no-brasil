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
| cabe4f1d-57ba-320f-98b8-8420e74d39ef | -6.7194 | -44.3231 | 2025-07-16 01:10:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 68.8 |
| c1cc00ff-9a21-3b94-a9ea-c73817fc92e8 | -13.015 | -45.036 | 2025-07-16 01:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 37d1b3e9-bfba-3a62-a241-29facf99dfc7 | -13.0339 | -45.0561 | 2025-07-16 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 126.4 |
| 155acc0b-2a28-32d0-b82b-d97b6fe7da85 | -13.0146 | -45.0593 | 2025-07-16 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 297.2 |
| 2de5f122-198b-33e5-bd3b-0c9bfa22da9c | -5.7943 | -45.0813 | 2025-07-16 01:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.4 |
| 1bbbcb05-c69c-3890-9f8c-ff7f123c90e9 | -13.0141 | -45.0826 | 2025-07-16 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 5bb60f82-2fe0-3aff-ac90-a68f57b7c2d2 | -12.0825 | -43.4753 | 2025-07-16 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 71.4 |
| 64fda723-8c3c-3149-8804-474868c3e696 | -13.015 | -45.036 | 2025-07-16 01:20:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 36ec09f3-0a72-3826-ba7a-c352076468f9 | -7.2025 | -43.1171 | 2025-07-16 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 86.9 |
| 8aa1955a-6333-3541-9741-70b1f3ea2214 | -12.0632 | -43.4784 | 2025-07-16 01:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 0c4626c4-6915-36ad-b73c-b49172545f33 | -7.1837 | -43.1189 | 2025-07-16 01:20:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.7 |
| 1efe2cf7-a592-3ed6-a5e0-5c5efd374030 | -28.75811 | -55.53134 | 2025-07-16 01:20:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 6.7 |
| 278c28a8-e2bf-3af0-afa8-9abe11551cda | -21.95721 | -57.59029 | 2025-07-16 01:20:00 | TERRA_M-M | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 28.8 |
| 46dea46c-ff22-3229-896f-42a1c4d9ba9a | -28.75951 | -55.54142 | 2025-07-16 01:20:00 | TERRA_M-M | SÃO BORJA | RIO GRANDE DO SUL | Brasil | 4318002 | 43 | 33 | nan | nan | nan | Pampa | 14.5 |
| 53da388a-2242-3bea-94f5-b504fd1ae8a9 | -14.31281 | -52.74833 | 2025-07-16 01:22:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 52b3a312-fd85-3624-b13b-671112204172 | -14.45373 | -58.90165 | 2025-07-16 01:22:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 17.4 |
| 73882cb7-8cd0-3e6e-b15a-854c5957866c | -18.59661 | -52.39743 | 2025-07-16 01:22:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 08b74635-10a5-3a7f-81f4-9e5da3f734a3 | -13.15518 | -50.79534 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 60eab496-8fdc-3ecb-8816-04e4cf8853ad | -14.31024 | -52.75521 | 2025-07-16 01:22:00 | TERRA_M-M | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 16.7 |
| 54c4419b-f0f0-3fae-837c-940e42ca1fc6 | -13.16492 | -50.7651 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 31.8 |
| 8b32f1da-1d7e-3656-9dcd-86766786d68a | -18.59521 | -52.40935 | 2025-07-16 01:22:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 22.2 |
| 199f1f48-4e65-30a4-a542-2c9ea9f0aa6f | -13.15011 | -50.77336 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 35.6 |
| 64924135-a04b-3d32-8312-3f4926b78f73 | -14.44488 | -58.90297 | 2025-07-16 01:22:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 97fe1ca7-f9d4-34b9-b3eb-79e8dfae66a4 | -13.16945 | -50.79815 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 23.6 |
| 6a9c1377-a069-383d-84e5-849b0a44593b | -13.16981 | -50.79262 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 34.6 |
| ef8d06b0-c12b-3e31-8003-d30b0f5445ad | -21.03994 | -55.98919 | 2025-07-16 01:22:00 | TERRA_M-M | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 7b700e4a-a5c4-3336-a338-66e15d2ab061 | -18.59938 | -52.41413 | 2025-07-16 01:22:00 | TERRA_M-M | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 15.9 |
| fa665e3b-d304-3ffa-8d31-cd6073e85e9e | -13.16476 | -50.77059 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8ee50da7-97d3-3c03-bd9d-4b5900e90933 | -13.15027 | -50.76783 | 2025-07-16 01:22:00 | TERRA_M-M | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 26.1 |
| 82f14cc4-3589-3d95-a191-bd74874a3594 | -18.65963 | -55.72464 | 2025-07-16 01:22:00 | TERRA_M-M | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 77b712f3-9ce2-3f97-bb8d-6833bc6f642c | -14.45498 | -58.91073 | 2025-07-16 01:22:00 | TERRA_M-M | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 62e1fbe2-6d28-36c2-af7f-c04e677caa87 | -7.9453 | -49.65879 | 2025-07-16 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 120.7 |
| 45c0e9a7-a422-3056-932b-687b117c5b2a | -9.02671 | -61.22106 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 62a88ff4-5b82-3272-ae27-7442e56d3497 | -9.65175 | -63.44758 | 2025-07-16 01:24:00 | TERRA_M-M | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 9ed74565-0014-3887-adb8-9606e902f364 | -9.02798 | -61.23033 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 78d1c628-e232-36de-a896-2420c011498a | -10.06017 | -59.09811 | 2025-07-16 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 5d11261f-6ea1-3033-9719-ae5512b36321 | -6.91644 | -52.85426 | 2025-07-16 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.6 |
| 6a35140e-8042-3af6-8df3-26e5c791d858 | -9.8669 | -60.29268 | 2025-07-16 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.0 |
| d4266980-b52f-3e2b-a74e-905ba26b6578 | -9.95867 | -64.96267 | 2025-07-16 01:24:00 | TERRA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 14.6 |
| c4c3fa4d-d35e-32bd-bfa0-4d39fb802e56 | -11.87625 | -58.71663 | 2025-07-16 01:24:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 56de1904-e744-3bf8-baee-cd0f0443a9f9 | -10.23267 | -55.45858 | 2025-07-16 01:24:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 302ed3ee-8d7a-397d-b4c7-1c62735200c7 | -9.02614 | -59.54256 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 14.7 |
| 14c0b023-4a0f-35c9-b066-d31004a8db5b | -6.91229 | -52.86056 | 2025-07-16 01:24:00 | TERRA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 27.7 |
| eeb76d9b-0a49-3c84-933b-142b42b5b3b9 | -10.22193 | -55.46029 | 2025-07-16 01:24:00 | TERRA_M-M | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3c2d507f-21d2-3a7e-842b-c318dd3bedfa | -9.02739 | -59.55151 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.0 |
| ffc45a3d-7d8f-3a9a-961d-796e92b1c834 | -11.44199 | -58.77455 | 2025-07-16 01:24:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| a1a7ff09-e5fb-38e6-8cb8-94330b619de0 | -10.06145 | -59.10715 | 2025-07-16 01:24:00 | TERRA_M-M | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 14.2 |
| 1f61065d-18a2-33a7-ad65-7caf7656b75d | -9.70436 | -56.18658 | 2025-07-16 01:24:00 | TERRA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 3123bfd0-414b-3f10-8fbe-531a2fca3b79 | -9.01895 | -61.2316 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 5aa7c190-b999-3d13-af26-7a816aa37717 | -7.94541 | -49.65224 | 2025-07-16 01:24:00 | TERRA_M-M | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 106.1 |
| 84020eb2-323a-34fa-ab8d-60325ca246ea | -11.87496 | -58.70752 | 2025-07-16 01:24:00 | TERRA_M-M | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1ce03a92-c404-3449-8336-14aad1576729 | -6.88617 | -59.32954 | 2025-07-16 01:24:00 | TERRA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e7e97d94-4156-355d-97f2-76a90dcb1f87 | -9.01769 | -61.22233 | 2025-07-16 01:24:00 | TERRA_M-M | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.6 |
| 6039f672-b105-3439-b709-98162b8d3dc6 | -7.2025 | -43.1171 | 2025-07-16 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 75.8 |
| b22f663f-d99a-3ccc-aa5c-71130720dca8 | -6.7194 | -44.3231 | 2025-07-16 01:30:00 | GOES-19 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 52.3 |
| d95dfbf1-22a6-3af5-8b71-c40c9e71e666 | -5.7943 | -45.0813 | 2025-07-16 01:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 60.1 |
| f74b0767-1c84-30bf-b31e-ca62e9dab976 | -12.0825 | -43.4753 | 2025-07-16 01:30:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 79.1 |
| a1768090-ea3a-322f-aeee-271411408352 | -13.0141 | -45.0826 | 2025-07-16 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 09ab64d9-f479-3bdd-882a-5da5baaf27eb | -7.1837 | -43.1189 | 2025-07-16 01:30:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 68.6 |
| 2c9178f3-f6ea-3d51-bd7a-d1602ed5504b | -13.015 | -45.036 | 2025-07-16 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 294d6f8e-3946-3e8d-9410-e05193a7b411 | -13.0146 | -45.0593 | 2025-07-16 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 203.0 |
| 8a6ec42b-591d-3eb7-bc7f-33ddfd6fd98b | -13.0339 | -45.0561 | 2025-07-16 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 161.8 |
| 4e9d19dc-f929-3cfd-91b0-3dfb7f691b68 | -13.0344 | -45.0328 | 2025-07-16 01:30:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 50.5 |
| ae79a0bb-b666-3583-871e-bc0d7ae31f6b | -21.9498 | -57.570999 | 2025-07-16 01:30:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| 666f696c-fd5c-3bba-a94f-5ba85488da62 | -14.4428 | -58.887699 | 2025-07-16 01:30:00 | METOP-B | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 7d29904e-6135-3d68-8bcc-14f3c35a14bd | -9.9594 | -64.954002 | 2025-07-16 01:30:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 07886ad8-dd0d-3478-b215-90db96e57c68 | -9.9576 | -64.946503 | 2025-07-16 01:30:00 | METOP-B | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | nan |
| 5bebcf94-0b06-393a-af13-fcd75a98a31a | -21.953199 | -57.584099 | 2025-07-16 01:30:00 | METOP-B | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | nan |
| e8e5af34-ab0b-3ad7-8e00-e815bd09c2b5 | -9.0175 | -61.215 | 2025-07-16 01:30:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 2b3fc352-42bb-32c0-80a4-b2c8fc69c59b | -9.0077 | -61.2174 | 2025-07-16 01:30:00 | METOP-B | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f9a69dbb-a4f3-3d8d-a342-6c1df94aad05 | -13.0146 | -45.0593 | 2025-07-16 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 236.2 |
| c3595195-7e02-3082-9fb7-4113019e8460 | -7.2025 | -43.1171 | 2025-07-16 01:40:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 84.8 |
| 948373b3-18b1-39ec-85fb-32dc9bf2631a | -5.7943 | -45.0813 | 2025-07-16 01:40:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 66.6 |
| 1e3f6299-6a46-3459-9897-0bceb5e37e14 | -13.015 | -45.036 | 2025-07-16 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 46.3 |
| 2a21b5e3-d946-33a7-a4f0-2c1db7cedbf0 | -13.0339 | -45.0561 | 2025-07-16 01:40:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 137.6 |
| 913da21e-fc4d-36d1-85aa-f428430e217a | -9.4192 | -40.3695 | 2025-07-16 01:40:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 66.9 |
| bfbdf9e8-563b-32de-b519-21e77d0e7bc6 | -13.0146 | -45.0593 | 2025-07-16 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 197.6 |
| 06213cce-1b7a-322a-8522-f49bf1221552 | -13.161 | -50.7855 | 2025-07-16 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 114.9 |
| a1a03189-24fb-3eca-9c83-54d552046fd9 | -13.0339 | -45.0561 | 2025-07-16 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 95.5 |
| d1d817d8-12e6-3616-ab2f-bb2a69c833ab | -13.1418 | -50.7879 | 2025-07-16 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 2032e681-8a4f-3a8e-b848-ac0a8b0b17df | -13.1613 | -50.764 | 2025-07-16 01:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 91.8 |
| 3d37914d-06d2-3ffa-92cb-0990531102e4 | -7.2025 | -43.1171 | 2025-07-16 01:50:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 63.6 |
| 8013ee9f-b329-3c68-8052-9f592e19b0c4 | -5.7943 | -45.0813 | 2025-07-16 01:50:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 59.5 |
| ecfa8535-c452-3b11-b322-6e372e40dfb2 | -13.015 | -45.036 | 2025-07-16 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 64.2 |
| e31916ee-b470-388f-94bc-9cbdbe4b1f2d | -13.0141 | -45.0826 | 2025-07-16 01:50:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.6 |
| 52e18913-7955-3945-a982-bcb3be7f23b0 | -13.0146 | -45.0593 | 2025-07-16 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 147.4 |
| a26296ee-4c9d-33d5-b841-9b6d3167eee7 | -9.4383 | -40.3668 | 2025-07-16 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 219.5 |
| fd7cd668-5301-3b22-9447-625aa7349f5d | -9.4379 | -40.3917 | 2025-07-16 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 60.2 |
| eaa626d5-17ee-35e2-8c15-59f13838faea | -13.0339 | -45.0561 | 2025-07-16 02:00:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 150.3 |
| a4f6ec1d-0c54-3e62-a700-6c24c31c45ca | -5.7943 | -45.0813 | 2025-07-16 02:00:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 57.3 |
| 061c4f25-57c4-3d91-b02a-45594237e3e7 | -7.2025 | -43.1171 | 2025-07-16 02:00:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 64.5 |
| 151e41ad-7e27-34b9-b4fd-81ba2de90ce7 | -9.4192 | -40.3695 | 2025-07-16 02:00:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 86.8 |
| a2e1a319-6b31-366b-92f7-5b346697b2b2 | -9.4188 | -40.3944 | 2025-07-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.1 |
| c36da1e6-8691-36fc-8c26-5ecb6e0fd783 | -13.015 | -45.036 | 2025-07-16 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 53.2 |
| 705f8f97-04dc-3d34-9f26-83ed05577cfc | -13.0141 | -45.0826 | 2025-07-16 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| e7ed4e78-5211-359a-8e7a-f39f56d39931 | -13.0339 | -45.0561 | 2025-07-16 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 76.6 |
| 58878fef-ca8f-3df4-ba39-99d4a72bb6f6 | -9.4192 | -40.3695 | 2025-07-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 249.6 |
| a2da6c60-b37d-3181-a02c-96cff82c99f5 | -9.4379 | -40.3917 | 2025-07-16 02:10:00 | GOES-19 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 80.2 |
| 5f366aa2-22e5-3916-a7d4-d0cde37d64f7 | -13.0146 | -45.0593 | 2025-07-16 02:10:00 | GOES-19 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 159.6 |
| db0485a0-d273-3996-83f1-2f5b36ef6717 | -7.2025 | -43.1171 | 2025-07-16 02:10:00 | GOES-19 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 67.2 |


[Clique aqui para ver as próximas entradas](README6.md)
