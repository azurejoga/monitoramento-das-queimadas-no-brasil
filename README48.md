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

## Dados Diários - Página 48

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d6bab458-4c35-3693-9107-add95ae074e0 | -17.78645 | -47.15731 | 2026-09-27 05:31:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0c458179-3d85-309d-b6e0-0bc4de860e73 | -14.49623 | -48.32642 | 2026-09-27 05:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 041ecc37-7766-3253-93ad-842a27861da6 | -17.04935 | -56.58071 | 2026-09-27 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 6211fdc9-a3eb-37d2-b00a-20268dd8ce7e | -12.89712 | -61.71346 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8a4cdbfb-8f69-3003-9c39-741048959859 | -15.41678 | -47.91009 | 2026-09-27 05:31:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 86807b6d-5b9d-3c0a-b261-b65e1b9d2ccd | -12.8987 | -61.72502 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1639ea44-7487-32d1-934b-444c92874a09 | -14.49563 | -48.33219 | 2026-09-27 05:31:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 58cefd39-214d-359a-89f2-cfb3bd8a3282 | -13.44047 | -57.06737 | 2026-09-27 05:31:00 | NPP-375D | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ebb4ec11-b6bb-3aab-b438-c57bb543a922 | -17.05331 | -56.5813 | 2026-09-27 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| d8aea962-3d1c-3b48-9573-2078e912d29f | -12.89315 | -61.71654 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 995ab924-fa6e-3739-985e-80ca5b97112e | -14.68612 | -59.60958 | 2026-09-27 05:31:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 9b78024e-416e-3267-8aab-f0fddcc2456c | -17.04609 | -56.57487 | 2026-09-27 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5df02cf7-64db-34a2-b945-ced5fedc2653 | -17.79367 | -47.15834 | 2026-09-27 05:31:00 | NPP-375D | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2c394af-0571-3f0c-b3d4-baeefabeb3f3 | -17.05006 | -56.57545 | 2026-09-27 05:31:00 | NPP-375D | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 1db464d7-17cd-316f-bf85-eefaa0bea38c | -12.88977 | -61.71597 | 2026-09-27 05:31:00 | NPP-375D | PIMENTEIRAS DO OESTE | RONDÔNIA | Brasil | 1101468 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d596f3cc-d6d6-39b2-b64e-1908aae92909 | -12.68495 | -60.2791 | 2026-09-27 05:31:00 | NPP-375D | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 764296e1-1f98-39c8-bca6-8c7749a7677b | -14.6895 | -59.61013 | 2026-09-27 05:31:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| edd9c2a8-bb10-3923-880d-8ee20752b9eb | -15.4236 | -47.91041 | 2026-09-27 05:31:00 | NPP-375D | PLANALTINA | GOIÁS | Brasil | 5217609 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 9eba46d6-1510-3d4d-9ccf-9c2b32576240 | -15.9859 | -54.93549 | 2026-09-27 05:31:00 | NPP-375D | JACIARA | MATO GROSSO | Brasil | 5104807 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d049814c-0bfd-396c-8579-881934fa2002 | -19.64301 | -49.69144 | 2026-09-27 05:31:00 | NPP-375D | CAMPINA VERDE | MINAS GERAIS | Brasil | 3111101 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3aa3a42-b5ac-372b-bc88-4ff9185d4e22 | -23.00616 | -48.61585 | 2026-09-27 05:33:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8d671d82-460c-3e28-aa99-66c5e58031e8 | -22.99916 | -48.6152 | 2026-09-27 05:33:00 | NPP-375D | BOTUCATU | SÃO PAULO | Brasil | 3507506 | 35 | 33 | nan | nan | nan | Cerrado | 1.8 |
| db45dccb-fa4e-3684-9fcf-1869f3470534 | -21.28905 | -57.89761 | 2026-09-27 05:33:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 6.0 |
| cbda9b68-8652-3d42-b345-7cc2ec6a33fe | -31.86782 | -53.32584 | 2026-09-27 05:36:00 | NPP-375D | HERVAL | RIO GRANDE DO SUL | Brasil | 4307104 | 43 | 33 | nan | nan | nan | Pampa | 1.3 |
| d452033a-9ebe-30b0-95f7-3aca5188f2cf | 1.65762 | -55.93967 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ecbed6ae-4a95-3881-b3d0-b8bd65e5e6a9 | 0.47888 | -50.95483 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b923f40-5534-3753-bfff-88762e8796ce | 0.47766 | -50.95709 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4762bcc-8edd-3861-95aa-57032978b643 | 2.69076 | -60.16195 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 36c549a3-71d0-3f3e-bbcb-22c6b67952f0 | 0.47667 | -50.95087 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b2f11aef-7c60-356b-b9e0-6cc27c8e39b3 | 1.65364 | -55.94576 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff114768-e06c-3ae1-9b1b-960e656e917d | -1.14046 | -54.09146 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 5819c0f6-c71e-3198-a487-c380bd980098 | 0.69897 | -51.43565 | 2026-09-27 05:46:00 | NOAA-20 | PORTO GRANDE | AMAPÁ | Brasil | 1600535 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 3660f169-aac3-3950-b07a-23f323aa9521 | -1.33965 | -55.4782 | 2026-09-27 05:46:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d7a06341-bb3a-3c45-923f-ee43013f1305 | 1.65676 | -55.93436 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a90861f5-6c48-3998-805b-a2bdbb4b4e01 | -1.2166 | -54.56815 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36445f83-ee83-3c92-b69c-a1a5ed58dfee | 2.64495 | -60.1778 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d66a7c30-5b96-3e19-9974-94ebaeadd7fd | 2.64064 | -60.17419 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4d8b83a5-cda6-38cf-a488-42ac7f42073b | 2.64427 | -60.1736 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fb298e9a-a79d-3553-bb85-44b7c0ae2df0 | -1.14243 | -54.0875 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7b79baf1-af5a-307e-a416-ba3b12fac219 | 1.66281 | -55.97149 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 55a2e3be-0e5d-3fa6-91e6-2fd0c562128e | 0.48933 | -50.94257 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 129a9df8-6e87-3491-b58a-19d0067f8445 | -1.04962 | -53.56901 | 2026-09-27 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| bfe6f38c-b35f-3b20-a63b-a3c06182e3a3 | -1.11398 | -57.06501 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| cf575f6f-da0e-31d1-aad9-1b2b1e018b59 | 0.32847 | -51.44021 | 2026-09-27 05:46:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d0280fc4-8234-3f30-83d0-d9e90dcf2211 | -1.14063 | -54.09943 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4deaf37f-0083-3c72-bb09-53a50344d1ad | -1.11727 | -57.27695 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b574b8dc-b2d6-3d48-80d6-f6768900b1b7 | 2.94009 | -60.31628 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| d226d61a-eae9-3941-8e26-195b03492115 | 0.48467 | -50.9476 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d823f632-3782-3430-8100-60f8480f636d | 0.46902 | -50.99038 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3f4aa2ea-2607-30e9-99ef-0b6ce65d12c2 | 4.32245 | -60.8266 | 2026-09-27 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 88e62a17-46d7-34a0-b207-3e10e33986a4 | 0.4857 | -50.95381 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 353dc96f-5ab7-3295-b3be-f09fe131fa51 | -1.04365 | -53.56832 | 2026-09-27 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 197245eb-4e0b-373a-aa21-d0153a4513b4 | -1.2147 | -54.54332 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 009d8029-e8bb-300e-82a4-b4ce2d0e38b3 | 2.63701 | -60.17476 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ca824455-e73c-3eea-8618-193193fad850 | 1.17397 | -60.37201 | 2026-09-27 05:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f035db03-c28e-3d9c-ba0f-0eaa477d0879 | 0.46803 | -50.98417 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b26ce6b6-fbd1-322a-b996-ef422d377fcc | -1.21413 | -54.54706 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76762b34-4bd7-32f3-943a-30befd67080a | 0.49031 | -50.94876 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 841c7723-7fc8-3243-80ae-21bfc8ad79a7 | -1.21726 | -54.56384 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73b22cf6-0e45-3a9d-a848-fe7334af03ee | 1.17466 | -60.37628 | 2026-09-27 05:46:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| a040b73b-a840-372e-b14e-ab180d6005a0 | 2.63496 | -60.16216 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7538bf35-18b9-3c9a-8b5d-2838e0f13cc9 | -1.21849 | -54.55588 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b0fec770-dfae-382c-b2e3-97e54e89cdc1 | 2.89687 | -60.27671 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b373ffc4-eee0-3593-b9dd-1f3487bcd240 | -1.04434 | -53.56385 | 2026-09-27 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 6dd84ad2-da81-3728-8f01-b46612c7d02d | -1.0503 | -53.56457 | 2026-09-27 05:46:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e5b3471f-8f32-38d6-85f1-adc66c0ebf9a | 2.6327 | -60.17114 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64ac85dc-7118-3613-ad85-c312938dff36 | 2.89327 | -60.27728 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80574c6f-a32f-3249-aeab-68763003c389 | 2.94433 | -60.31978 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52e7ba72-0b2e-3102-be3b-49fdacda1a9d | -1.11115 | -57.06733 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 41e33090-e438-3a8c-9bea-941a775e04f5 | 0.48349 | -50.94981 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c228c2c-7e19-39d2-b510-1378542248d3 | 2.63201 | -60.16694 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca446447-ce69-3903-87a0-eb83ddc7c8b2 | 0.47785 | -50.94861 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1de8d19c-d10d-3f79-82af-16b1e264be57 | -1.14108 | -54.08752 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7cbb02c9-c235-3a7d-968c-58e18bba7d69 | -1.14638 | -54.10026 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 540b883b-9f33-3198-8309-fd6f0045710e | -1.12186 | -57.27791 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b233a72e-b454-39fd-a2b0-f787fbb0dfe1 | 0.4915 | -50.94657 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e8071ca5-3a34-3586-985e-1ab92c6912df | -1.14124 | -54.09541 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 00b07a42-0655-3428-9121-beaf75daba5a | 2.63564 | -60.16636 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c0b5d562-b1f7-34f5-ba54-df9ef96e6868 | 4.22802 | -59.86489 | 2026-09-27 05:46:00 | NOAA-20 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 1d2beaba-5377-3b6e-b0a1-11a37eb6c883 | 0.32939 | -51.446 | 2026-09-27 05:46:00 | NOAA-20 | SANTANA | AMAPÁ | Brasil | 1600600 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 89a5e45c-62b2-36c2-9f56-1c28d8c88994 | 0.48448 | -50.95602 | 2026-09-27 05:46:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 04484b64-1214-3fc0-9f31-37761ae19233 | -1.14698 | -54.09625 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 756571b1-dfc6-3711-8ec0-81b174f7c2f8 | 1.65278 | -55.94045 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 64481b50-33ba-38d1-813f-657421d1624f | -1.21788 | -54.5598 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 04a0b2cd-f979-3ada-afba-f27a464a4d37 | -1.14183 | -54.09145 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 38ac731f-a323-3b73-b8c3-e0941aee3a42 | 1.96793 | -50.90891 | 2026-09-27 05:46:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e8bda568-49f1-3685-a306-e8aa61adcdbe | 2.63633 | -60.17056 | 2026-09-27 05:46:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| f3330cd5-6521-3474-8101-49e1b192591c | -1.10931 | -57.0642 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e6718751-3bfd-3456-83b4-52a31c4068c6 | 1.96692 | -50.90301 | 2026-09-27 05:46:00 | NOAA-20 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e79f82a7-f02e-3f43-9100-eac6aca101a5 | 1.66368 | -55.97677 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 70c2a970-cf38-3ac8-ac68-500ab32a1654 | 4.31902 | -60.82732 | 2026-09-27 05:46:00 | NOAA-20 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53d550b9-e8a3-3277-82f7-879e6d0c195a | -1.14558 | -54.09623 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4982d80b-2b17-3332-bb31-499e44ae439e | 1.65104 | -55.92983 | 2026-09-27 05:46:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ba345d27-1890-3d6e-9c0f-9c92aa33a773 | -1.14577 | -54.10429 | 2026-09-27 05:46:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 26a38e1a-4b46-3fd7-925e-75c09fe42476 | -3.03389 | -54.69822 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c4b3e4bc-2ef6-3e42-8ac0-23363e8ff2f7 | -1.83608 | -54.71976 | 2026-09-27 05:48:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 0023d1b4-84c2-342b-b186-293ee963698f | -3.30111 | -54.69178 | 2026-09-27 05:48:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ec09605e-3bde-3922-9b11-33e2ebb5a280 | -3.20169 | -51.03809 | 2026-09-27 05:48:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 12054cd5-801a-34de-94d0-1d2052508dad | -3.84701 | -52.01347 | 2026-09-27 05:48:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| de50437f-9b0b-3bed-9572-af5be4136e38 | -2.06088 | -56.87306 | 2026-09-27 05:48:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |


[Clique aqui para ver as próximas entradas](README49.md)
