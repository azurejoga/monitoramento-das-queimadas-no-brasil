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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7a39fa74-e60a-3bc1-80c4-3caa774dcbda | -1.89943 | -56.61023 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 007d91f5-7ad0-3ed2-a704-c79d56c8b03f | -10.24947 | -68.30402 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| af159eff-b706-303e-9c95-bf8381a834a9 | -1.9739 | -55.67156 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 2108433e-3bd3-3d5c-95e0-c974386af68a | -8.57424 | -67.00059 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| f3d16dcf-f6ec-34ee-8fc0-4140d2d72041 | -3.08742 | -69.20657 | 2026-10-05 17:37:00 | NOAA-20 | SANTO ANTÔNIO DO IÇÁ | AMAZONAS | Brasil | 1303700 | 13 | 33 | nan | nan | nan | Amazônia | 9.7 |
| d73573f1-585b-334f-b8de-633af86a6826 | -8.65984 | -66.58866 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| a724ad10-3d39-303d-8780-efe7bb90791c | -2.15929 | -56.11225 | 2026-10-05 17:37:00 | NOAA-20 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| deb454d6-e2cb-38f7-a552-32d324d03b80 | -10.38055 | -67.95203 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| bcf0a85c-cf19-3bf2-844e-3985add80621 | -9.03232 | -67.47382 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 13.3 |
| b71fdfa7-6e0d-3eb6-9afe-8cacad453427 | -1.3562 | -55.9833 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 31.2 |
| 68f855dd-5ad3-3fd1-ba9e-67c45bddb7c4 | -9.11524 | -67.70837 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 11.0 |
| e53b8ea3-0aab-3c66-a519-a419c8cded8d | -9.34367 | -65.81519 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 3787c64b-765a-3463-b943-19df33988dac | -8.82882 | -67.38232 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| 43dcdfe9-5552-3688-8a22-886b640811af | -8.52571 | -54.6136 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| 5bb839e1-6bb9-373d-858b-349861860c50 | -8.85434 | -70.60001 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 07c43059-0501-3917-a1aa-719f566097d2 | 2.28069 | -59.74555 | 2026-10-05 17:37:00 | NOAA-20 | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 0ceed58e-54ba-3701-9224-c9116403bb6c | -2.13262 | -56.6906 | 2026-10-05 17:37:00 | NOAA-20 | FARO | PARÁ | Brasil | 1503002 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 77d76ef7-8e58-3060-a725-aee275e0e3c1 | -2.77126 | -57.67233 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 91.5 |
| 11c8b998-2947-3552-8f63-8d8ba67e9633 | -10.11807 | -68.07842 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 5758b6e3-fb9a-3ec1-88d1-04affa44d263 | -7.2252 | -55.18167 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 41.9 |
| 9aa392d7-678b-3cc3-88df-3c860337fb87 | -9.96369 | -65.12294 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 36546475-3cda-3505-98f4-5ab42532747e | -7.11702 | -55.72271 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| c31f7226-d969-3ea4-a52b-90c05835d8f2 | -3.18056 | -60.05221 | 2026-10-05 17:37:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e0c9cfc5-f10f-3b81-901b-38eb526a26bb | -1.33066 | -56.40777 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| d8db7864-c67b-3c12-9d2d-8aa3b042da3d | -9.12047 | -64.36014 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.3 |
| a2111d8a-f7e9-3d6a-8937-3069655af6ac | -9.41585 | -68.54609 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 4.8 |
| e28da49c-50e9-3545-b309-10d985f5fe3b | -8.53309 | -54.58288 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 68821e37-4a5f-383b-88f9-d2a860b6bc2b | -10.56371 | -68.34271 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 85f079e4-ac7f-3966-95b5-33e1a38f6d99 | -9.73282 | -65.07179 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| e41e55c3-9dc5-3146-9c66-0c0742208fb7 | -2.92357 | -58.06538 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| d1e3fcd4-2679-3bcf-8f74-64d8c9ef46b5 | -8.92292 | -68.746 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 3b587ad1-49bd-33ce-9266-631a1400e4f6 | -10.73134 | -69.60207 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 2d0eecfa-f5a8-3e2d-a2a3-f2ddf8f0b0d9 | -3.03393 | -59.21255 | 2026-10-05 17:37:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 17fb92cf-d451-365a-8f78-c25b6f8a03c1 | -2.76559 | -57.66011 | 2026-10-05 17:37:00 | NOAA-20 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| 8d94e887-80af-31bf-91d3-a2861559358a | -9.12014 | -65.47405 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 9ace9fb7-b9ca-3e90-bed7-289cff98531f | -1.73766 | -55.3472 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 28170066-8491-3c2f-a416-63ffacb2c61d | -9.3494 | -65.32589 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 3bebc96d-3e33-3eb4-9cd9-2e1dc1f00616 | 3.85154 | -60.28791 | 2026-10-05 17:37:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| fe9da8e9-401d-3637-a028-2bbf110b1cbd | -2.06456 | -56.87323 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 15.4 |
| ecff86a0-0bf0-3102-98d3-8b910ed0b90e | -8.59729 | -66.81767 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 82.1 |
| e0b90b15-970c-35f7-8d36-4571456203a9 | -10.57167 | -68.87434 | 2026-10-05 17:37:00 | NOAA-20 | XAPURI | ACRE | Brasil | 1200708 | 12 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 12f83713-3623-3c5c-b971-0e26ac15b1f9 | -9.34436 | -65.44856 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| e8fa21f4-af70-3614-a7c6-99a00e4cf93f | -1.84724 | -64.13329 | 2026-10-05 17:37:00 | NOAA-20 | BARCELOS | AMAZONAS | Brasil | 1300409 | 13 | 33 | nan | nan | nan | Amazônia | 585.2 |
| 4c3aaaa0-b814-38c7-a027-cf26b3aa0b6f | 3.11934 | -60.57071 | 2026-10-05 17:37:00 | NOAA-20 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 6.8 |
| b865bd95-c36d-31c1-990e-31f98584468c | -8.69967 | -69.41949 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.2 |
| bdf51492-3313-3e21-a38c-9395cf6a644d | -9.26967 | -68.37227 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 18.1 |
| 8f579cf6-a040-34e9-80a4-514631449c8b | -9.49029 | -64.69035 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 23a09e5c-f7f5-3524-a664-2190c95764f6 | -9.14912 | -65.53271 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 853a8553-06dc-300b-ad58-0694c6c1e048 | -8.87709 | -71.32905 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 3beeb7ee-70cf-3ea9-b9a8-bfaca68fe78e | -7.89822 | -54.75498 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.8 |
| d717adda-91ed-3493-bb7b-bcb2b7f2ccfb | 1.85226 | -55.7973 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 6.7 |
| dae4df9b-14ce-36ab-bdd1-f297eb410b80 | -1.3403 | -55.96283 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 4c20be2a-5e1f-3090-b4e6-065529997f57 | -9.13343 | -64.39491 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.6 |
| e9289bbd-c895-3b87-b3e2-bf1641d88856 | -8.6178 | -66.72673 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 44717b09-10cc-37b1-81dc-6387e54ffb90 | -9.37805 | -68.92619 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 122f59b8-eb59-3c88-b553-5d98fd8c3b51 | 0.64981 | -59.83636 | 2026-10-05 17:37:00 | NOAA-20 | SÃO JOÃO DA BALIZA | RORAIMA | Brasil | 1400506 | 14 | 33 | nan | nan | nan | Amazônia | 8.1 |
| e3da7279-427e-3c0b-8414-cf33eed432c6 | -10.24906 | -68.30073 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 13.2 |
| 98cd65e9-bd3a-36dc-b665-98fe12400089 | 1.05215 | -60.55622 | 2026-10-05 17:37:00 | NOAA-20 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11b9ca9f-71a5-36b7-924a-22c8afbec754 | 0.30067 | -51.0865 | 2026-10-05 17:37:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 0173db16-7eb2-3b80-b7d6-5c80eaddea5d | -9.12371 | -68.23589 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 1af0dd36-894f-3f2b-9947-cec431666f5d | -2.27638 | -57.0183 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ae45d8ce-d619-3614-9b52-7ebcbd0c3239 | -9.25505 | -67.64867 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| e49c05ac-dd9d-3f42-8b52-c932722c2794 | -2.07907 | -56.89053 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 6c988ceb-748f-392d-801c-fbf1d9321b0a | -8.94772 | -70.74412 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6c6a5918-4e3e-3ed6-a56d-080b8e8ac370 | -8.65465 | -66.58463 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 12.3 |
| d47d9f2f-518b-3cce-8052-22d4f5376d68 | -8.99713 | -67.07061 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 83.5 |
| 6e07a114-956f-3236-8bff-410f9f3b1b65 | -8.99662 | -65.39393 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 10.4 |
| ef51e159-5422-30f2-bfe1-f9446b6304be | 1.49363 | -55.64104 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 10.2 |
| 5ee27c4c-fb4a-3e51-8081-8611c662dbb6 | -9.12601 | -68.21362 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a674e3a0-95bd-3ae5-97c7-0e5cbfc9a383 | -1.124 | -57.27709 | 2026-10-05 17:37:00 | NOAA-20 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 679e87f9-386c-3855-9f9a-1a85a2b53cf0 | -1.71046 | -55.02179 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.3 |
| fd616a56-f9c5-34cb-8c40-dd92889a27c7 | -8.99768 | -65.40186 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 9.0 |
| eb153147-4d62-3cea-8059-ab4ffad90169 | -9.07743 | -66.09444 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| b3367bca-fd34-3fad-af80-b796331eb4db | -10.06565 | -68.58649 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 3dd5025f-e57e-35ce-b394-24cea12fc9d8 | -6.45608 | -55.47159 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 75c220cf-9507-3744-aab5-9eb83ab843c0 | -9.37263 | -68.92693 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 9.5 |
| 15e81d42-0c1c-3f6f-86bf-e80dfb085da9 | 1.48405 | -55.67474 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| f8d33ac9-10aa-333b-99d7-c89c7abc19c3 | -8.87772 | -71.33405 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 15.2 |
| 72047b11-31eb-317b-b7cb-4634d16d6891 | -1.48942 | -55.67146 | 2026-10-05 17:37:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 8b804bf8-6b77-3447-ab4b-b93bc7ccc9c7 | -7.86785 | -54.69728 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 255b359e-dad0-3c15-9332-ce7f2cd97632 | -0.99402 | -60.3783 | 2026-10-05 17:37:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ae5101e2-0a01-364f-ad9f-79d4efdfb769 | -8.73345 | -69.41908 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 22.0 |
| 9c54eed6-1394-30d3-94b3-519f3f05e2e4 | -8.90939 | -68.63741 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 88.0 |
| 0118e715-3465-3559-a689-7a97c060bc52 | -9.37353 | -68.80377 | 2026-10-05 17:37:00 | NOAA-20 | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 8.3 |
| 0d85da97-55d6-3bf6-bbeb-9e92295a3dc7 | -9.30144 | -67.54507 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| ea3b32bc-ff6a-300d-95a5-3e79563a1c84 | -9.01412 | -65.42779 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| e23166b9-92f3-3b2f-a05d-09f2c906e4d3 | -9.3828 | -68.33788 | 2026-10-05 17:37:00 | NOAA-20 | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d6a0cf16-3a3f-33d6-9a8b-dacfa7870d00 | -10.38214 | -67.96428 | 2026-10-05 17:37:00 | NOAA-20 | CAPIXABA | ACRE | Brasil | 1200179 | 12 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a15823d0-99ed-312a-892f-70d2453b647a | -6.80991 | -55.296 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 8.0 |
| ef2e89c6-97f5-3b70-9203-475f52b8136f | -8.78236 | -69.53321 | 2026-10-05 17:37:00 | NOAA-20 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9643a7cb-acf8-3b5a-89ab-d18986cdac16 | -9.7344 | -65.08346 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 6e83e81a-158e-3190-bfeb-ba83dab64e2d | -10.23539 | -68.23345 | 2026-10-05 17:37:00 | NOAA-20 | RIO BRANCO | ACRE | Brasil | 1200401 | 12 | 33 | nan | nan | nan | Amazônia | 10.2 |
| c5a973c8-428a-32ae-9b19-bccc7670f38c | -9.12802 | -64.38519 | 2026-10-05 17:37:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 11.6 |
| f2241ec5-ebba-38c8-90ee-795dd038f56d | -8.76001 | -68.97063 | 2026-10-05 17:37:00 | NOAA-20 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 64.8 |
| 4584aa0e-3a6b-3f49-8f7c-aecafd3487c0 | -10.81409 | -69.54478 | 2026-10-05 17:37:00 | NOAA-20 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 079be2a6-7452-34d8-a1d1-7e44670a16c5 | -9.0265 | -65.69761 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.9 |
| b7c5ab18-ccc0-3f80-b3b9-ace3e7947b17 | -8.52226 | -54.61783 | 2026-10-05 17:37:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dc4d1c81-5652-376c-b6c4-8cb399b887de | -6.45691 | -55.47666 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 8f72e070-5a44-3818-9bb1-e92e8acf6059 | -9.16389 | -70.77853 | 2026-10-05 17:37:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 4a9cf3ff-a4a2-3a1a-8276-ba1e1cb8e8ba | -9.1086 | -65.36227 | 2026-10-05 17:37:00 | NOAA-20 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 17.3 |


[Clique aqui para ver as próximas entradas](README145.md)
