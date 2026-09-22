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

## Dados Diários - Página 121

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 033a436b-ecb9-34b1-8585-408655826ee3 | -6.70987 | -58.99335 | 2026-09-22 07:39:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4899a0fc-051e-3ca3-b2a0-7cfe0f39b69e | -10.61261 | -53.99514 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 15.6 |
| 1104fcb8-2da9-37d9-95c8-4554aa7328cf | -3.60799 | -60.56541 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| f23272d6-fd7b-3ca2-a189-08191e306a01 | -6.61906 | -59.91278 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 68.5 |
| f5daa8f5-b873-3be2-b4e7-170fd2342407 | -2.85924 | -57.80004 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 98cd0b3e-02ee-3b14-b303-40bdbe1eb138 | -3.03999 | -61.25659 | 2026-09-22 07:39:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 3b5dd60c-0ac5-3862-b3b4-1d3ab55be477 | -6.63402 | -59.93312 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| d6164945-3ac6-33ce-9eab-639e09939a11 | -3.90019 | -60.59103 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 7da66add-602e-3f75-894e-3b6061f95932 | -6.03572 | -57.81774 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 18.5 |
| dea80c85-5887-316d-8f88-050a5c1a6289 | -5.81498 | -57.73047 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| eb7c0ffc-0b50-323b-b573-cad66e09755e | -10.60167 | -53.96905 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 46.3 |
| ddc5b1c7-9b14-3b19-9559-dab4c3e5f656 | -6.6952 | -59.95771 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 141938fd-bf69-394d-a417-4b11bee34b9b | -10.59381 | -53.98571 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 24.5 |
| cc06f3da-7805-35fe-82fb-80772a05387b | -3.39669 | -59.51907 | 2026-09-22 07:39:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 11.3 |
| f4c530b0-56a4-3516-b968-ddad7e7d4e72 | -6.30965 | -60.00268 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 9b3e8e31-e54c-3b9b-82cc-000452c142e1 | -3.05793 | -54.41527 | 2026-09-22 07:39:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 108965e5-c96e-3898-8673-ff79c6b19c6b | -6.70849 | -59.00279 | 2026-09-22 07:39:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 0c40cc38-9093-3e1b-a204-355ff189b79e | -6.39102 | -60.02045 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 11494f1b-572f-3654-9eae-08b2feb9dd71 | -4.08764 | -62.08752 | 2026-09-22 07:39:00 | AQUA_M-M | ANORI | AMAZONAS | Brasil | 1300102 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 22bc6ec0-7122-3ea9-ae16-d443e391488a | -6.6367 | -59.91535 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 50efa235-c3d5-39f1-b597-cb675a25b506 | -6.64417 | -59.92554 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 70.1 |
| b2abb593-b768-3c42-831e-ac24d538c2af | -6.63536 | -59.92425 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 42.8 |
| 6f42b74b-13d7-39b6-b542-05958d9725c2 | -6.03415 | -57.82827 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 7e3de893-26e0-3fb7-b713-a281f3bf6358 | -8.64202 | -62.48083 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 9943828e-3c55-3729-9012-5b7635740c1a | -4.96139 | -55.82818 | 2026-09-22 07:39:00 | AQUA_M-M | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 2879abf5-1086-3618-a7c6-59c0f6023bb0 | -2.8607 | -57.7903 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 14.2 |
| bf7bb851-ea89-3ca9-9e44-020e4e972651 | -3.22962 | -53.94987 | 2026-09-22 07:39:00 | AQUA_M-M | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 255efaca-43e9-3f32-a7c8-bb27746e2469 | -6.46413 | -59.96559 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| ccfa21d4-97a3-3d01-8d58-f7a0dd17e0aa | -3.36735 | -61.28684 | 2026-09-22 07:39:00 | AQUA_M-M | CAAPIRANGA | AMAZONAS | Brasil | 1300839 | 13 | 33 | nan | nan | nan | Amazônia | 13.0 |
| 76c7049f-780f-3726-bbaa-53eb8b9457c7 | -2.40844 | -58.2798 | 2026-09-22 07:39:00 | AQUA_M-M | ITAPIRANGA | AMAZONAS | Brasil | 1302009 | 13 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 894199ee-8b78-317e-83f5-5321729a027a | -6.29373 | -57.74257 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 6407cbf4-fe4c-3e67-86b9-729afdaee64e | -6.13055 | -59.96387 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a4a1cb9b-4d74-3289-8765-db676135f7d1 | -6.61772 | -59.92165 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 86.3 |
| 5303bcc4-1a83-33a4-bc0a-35136c64f9fa | -3.68938 | -60.5833 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 08dd3328-3aef-3ec3-adba-74823ff5c8da | -2.95354 | -57.72045 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 7.0 |
| f5f141d5-b85f-3f59-a700-0c7382145e90 | -6.30833 | -60.0115 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 07778fe8-1a16-3131-848d-9f5b2b9f11ee | -6.04802 | -57.82607 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 12.4 |
| 94f70e8d-5aea-3f12-b0d2-7745803dd05c | -3.39537 | -59.52782 | 2026-09-22 07:39:00 | AQUA_M-M | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.8 |
| b8a6af4c-1a3c-3665-bb18-5f35bcb24e64 | -10.59868 | -53.9935 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 36.2 |
| cdfc33cd-2813-30b3-a590-08510d740070 | -7.32803 | -55.58805 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 08a01976-6187-387c-94ba-928eb3346792 | -8.61827 | -62.51531 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 21ecab56-4bce-3958-a885-bf59fe4280ec | -5.81343 | -57.7411 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 11.7 |
| d2eb1d2d-f48f-396f-9b6d-8d6f43a5f87b | -6.62521 | -59.93181 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 47.7 |
| 968fdbe3-fbdd-3e21-9b81-1238f1c4ae4b | -3.7171 | -60.57842 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| d2ff4580-b3a0-39a8-8287-13c29f45c1de | -2.93263 | -57.79747 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 1fb99673-9a20-38c7-b729-1f3bb3bf6645 | -6.36028 | -58.2855 | 2026-09-22 07:39:00 | AQUA_M-M | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3ea41d58-7d27-39d7-9409-fbfc5b2550c9 | -6.42537 | -59.97136 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b7a625a1-72ab-38ef-b914-1735beb03c46 | -3.08097 | -61.16891 | 2026-09-22 07:39:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 2fdc9a9d-a09c-3791-a89b-002966964807 | -7.58494 | -57.67472 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 559c422f-3286-3b0c-b956-c0120cac2c97 | -4.67881 | -55.62066 | 2026-09-22 07:39:00 | AQUA_M-M | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 12.8 |
| 7372e6f7-8374-3a0d-912a-c1fce94d3ce5 | -6.46149 | -59.9833 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 20.3 |
| 641caaa2-ca34-3442-ba3a-a0afb86fd562 | -8.64058 | -62.49014 | 2026-09-22 07:39:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 16.2 |
| 95e40d68-48ed-3abc-a894-06c21c1f7755 | -3.06554 | -61.26979 | 2026-09-22 07:39:00 | AQUA_M-M | MANACAPURU | AMAZONAS | Brasil | 1302504 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 7b4f399f-47a3-33c8-9ff0-9ce6629999a1 | -3.45557 | -58.32053 | 2026-09-22 07:39:00 | AQUA_M-M | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 22c6c429-ce7e-3102-b74c-b2a4efd781fe | -2.86993 | -57.79165 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| f44f83b9-3732-3543-8065-5d97f60d95ff | -2.92484 | -57.78637 | 2026-09-22 07:39:00 | AQUA_M-M | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a8eb8e42-c5d4-3506-a849-0caa78c93cd1 | -6.04954 | -57.81544 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 7eca0cd5-eb1f-302c-97b4-eec7dfc9959b | -6.46016 | -59.99215 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 7fa522d0-a7ff-34cd-a6ef-ec98be84db26 | -10.60776 | -53.98727 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 61.4 |
| d275981b-8e44-3b46-8998-d26c289b1148 | -3.68265 | -60.62731 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 196d65b9-4e13-3385-b0ac-6cff1e4d6cc6 | -10.61562 | -53.97081 | 2026-09-22 07:39:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 19.3 |
| 2e44d1da-f8fe-3e28-88d0-850e6cd91fb3 | -3.58486 | -59.06583 | 2026-09-22 07:39:00 | AQUA_M-M | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 9.3 |
| acf04797-8eac-37cb-902f-53044f4a85ff | -6.64551 | -59.91666 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 32.6 |
| 32fcaedc-1a0b-3bb7-9b8d-74d6294fcabd | -2.2747 | -58.00059 | 2026-09-22 07:39:00 | AQUA_M-M | SÃO SEBASTIÃO DO UATUMÃ | AMAZONAS | Brasil | 1303957 | 13 | 33 | nan | nan | nan | Amazônia | 12.1 |
| fb0c0825-8127-3440-9a0d-c6afb1a5d3dd | -5.93479 | -59.97662 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 986dc5d0-386e-3bfb-8290-4c0614863c4c | -3.71232 | -60.55076 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 354b9d32-fb56-350a-8df8-3a693817af32 | -6.92029 | -59.62808 | 2026-09-22 07:39:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| c65d0c57-340f-3d62-b8cf-6b8139063eb6 | -7.32576 | -55.60435 | 2026-09-22 07:39:00 | AQUA_M-M | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 12.1 |
| 5360aeba-4a02-35d9-a3ec-f25c452764a0 | -6.18729 | -57.7757 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| af71a4b0-aabd-3ba6-8316-a78db41fb9cf | -3.69072 | -60.57451 | 2026-09-22 07:39:00 | AQUA_M-M | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 6.7 |
| a212f233-6f60-3388-9b28-3a6c20e4ba3b | -6.30339 | -57.74395 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a45ff651-9ce5-39e5-87ec-aeda8a2f07bf | -6.62654 | -59.92295 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 40.7 |
| 8f9ab4a6-e784-3b61-8eb6-faf18e7ff168 | -6.61639 | -59.93053 | 2026-09-22 07:39:00 | AQUA_M-M | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| c1ff0236-a75f-39d3-b066-86b50970b4fc | -2.27612 | -57.99113 | 2026-09-22 07:39:00 | AQUA_M-M | URUCARÁ | AMAZONAS | Brasil | 1304302 | 13 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 2db31ccf-b3fa-33bf-8186-3f540bf4dbcc | -6.19692 | -57.77707 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 16.7 |
| ea9c3797-e000-3978-a41e-559d41e12649 | -6.03994 | -57.81416 | 2026-09-22 07:39:00 | AQUA_M-M | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 41b0331e-2c55-3821-b5b1-97352030bcf3 | -3.06037 | -54.39832 | 2026-09-22 07:39:00 | AQUA_M-M | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| a2c1d6d0-3cfa-3548-babc-7b57a33e40d1 | -6.6515 | -59.9258 | 2026-09-22 07:40:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 76.6 |
| 703e1dcc-a9ba-3aad-aa7e-0a5f64dffbc9 | -12.8715 | -50.9291 | 2026-09-22 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 89.5 |
| fead7a10-664c-3754-9f73-f06ddd708239 | -12.3021 | -50.6988 | 2026-09-22 07:40:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 97.2 |
| a1b37e4c-b88e-34fe-ae21-82eabda39e76 | -6.6148 | -59.908 | 2026-09-22 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 59.4 |
| abdc33cc-2a7a-34c7-867e-208556b38f56 | -12.8906 | -50.9267 | 2026-09-22 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 58.8 |
| 9fbdd6b9-912a-31dc-a10f-9cc8be2f04ec | -12.8718 | -50.9076 | 2026-09-22 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| 3fa3e333-faa9-3d0c-a2eb-86eca580ac3b | -12.891 | -50.9052 | 2026-09-22 07:40:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 48.0 |
| 7e8a6fae-fcb8-3e29-a8f9-bcef4037d56f | -6.6146 | -59.9272 | 2026-09-22 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 97.0 |
| f645f311-1248-31ed-ac04-433332c29079 | -10.6094 | -53.9902 | 2026-09-22 07:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 47.8 |
| 93d95cd0-5c84-3bab-a330-1b748c9492e4 | -6.6331 | -59.9265 | 2026-09-22 07:40:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 99.3 |
| e2428f5f-9187-3817-8cbc-722eba2f13be | -9.13597 | -67.95013 | 2026-09-22 07:41:00 | AQUA_M-M | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 62713ee2-71c2-3355-ac93-2b22e304d5f3 | -11.32319 | -54.03335 | 2026-09-22 07:41:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e9786c7f-3c56-314c-ab94-4f4e3f01b8d4 | -9.12379 | -65.86434 | 2026-09-22 07:41:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 9473025d-836b-306c-bcd0-774d0cb56b2f | -9.1854 | -65.85062 | 2026-09-22 07:41:00 | AQUA_M-M | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.9 |
| b2106dda-4dd4-3dab-b2ab-23a02e7b2eda | -9.55782 | -66.0419 | 2026-09-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 562141a0-44aa-3828-a22a-003e8626504a | -9.56021 | -66.02721 | 2026-09-22 07:41:00 | AQUA_M-M | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 13.7 |
| 3fd07584-8aba-3f5f-8ef0-f18e925025f2 | -6.6515 | -59.9258 | 2026-09-22 07:50:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 74.2 |
| 368d1fec-da78-3888-adf6-c8c4b5a440a6 | -6.6146 | -59.9272 | 2026-09-22 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 71.2 |
| d209da48-bdef-3700-a0d8-832516bca793 | -12.3021 | -50.6988 | 2026-09-22 07:50:00 | GOES-19 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 60.9 |
| 55771d98-18de-325b-ae88-2509f1791b35 | -12.891 | -50.9052 | 2026-09-22 07:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 117.6 |
| 4603cf5b-3a9c-3bd1-8d7a-412d43ff1bb9 | -12.8718 | -50.9076 | 2026-09-22 07:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 165.0 |
| cb7c232e-fb7d-3e92-b352-f22a0538952f | -12.8906 | -50.9267 | 2026-09-22 07:50:00 | GOES-19 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 116.6 |
| dab3bd63-fe77-34bf-b467-123ae4236c59 | -6.6331 | -59.9265 | 2026-09-22 07:50:00 | GOES-19 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 127.1 |


[Clique aqui para ver as próximas entradas](README122.md)
