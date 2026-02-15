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
| 01db6f8c-6ef0-3ec0-90c8-7632c7e6b854 | -16.17978 | -43.64163 | 2026-02-15 04:06:00 | NOAA-20 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 45e4efa3-685d-37df-aca6-a1ee5494a853 | -17.84207 | -40.1449 | 2026-02-15 04:06:00 | NOAA-20 | MUCURI | BAHIA | Brasil | 2922003 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 68f14b05-3ab6-3b16-b116-44a253bbf9d6 | -19.76161 | -48.29087 | 2026-02-15 04:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b3191274-fbff-3ca3-9ffd-8db315b95bdc | -17.30051 | -41.63503 | 2026-02-15 04:06:00 | NOAA-20 | ITAIPÉ | MINAS GERAIS | Brasil | 3132305 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| f837c563-55c8-3815-84a2-1164ea580f6b | -19.7606 | -48.29636 | 2026-02-15 04:06:00 | NOAA-20 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5bcaf1c5-e48b-3c47-87ba-4fbbc0230a29 | -18.64588 | -50.26834 | 2026-02-15 04:06:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 3.3 |
| c35972e0-3113-361f-a7eb-27fa47c0253d | -17.97066 | -42.34652 | 2026-02-15 04:06:00 | NOAA-20 | ÁGUA BOA | MINAS GERAIS | Brasil | 3100609 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.9 |
| 6ff4df4c-b7e4-300b-b436-a6c380057d5d | -21.13694 | -41.24397 | 2026-02-15 04:06:00 | NOAA-20 | MIMOSO DO SUL | ESPÍRITO SANTO | Brasil | 3203403 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.0 |
| 5eab0708-8d8c-3312-8ddb-ebda8e04f60b | -20.76529 | -43.60062 | 2026-02-15 04:06:00 | NOAA-20 | SANTANA DOS MONTES | MINAS GERAIS | Brasil | 3159100 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| b75a4560-d399-3189-8750-4a0d1b31ef64 | -18.71629 | -43.0047 | 2026-02-15 04:06:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| 8f166258-bb1f-3eee-8367-8a442403908d | -18.6456 | -50.2715 | 2026-02-15 04:06:00 | NOAA-20 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.3 |
| 09d2465c-20b3-375f-81d2-d5b62554c911 | -18.71571 | -43.00832 | 2026-02-15 04:06:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 9ff6314f-9571-32e7-8f85-900ea90874a7 | -18.71183 | -43.01136 | 2026-02-15 04:06:00 | NOAA-20 | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| d759a294-bb91-3bb6-bdff-f2e704692bd5 | -19.0511 | -40.8374 | 2026-02-15 04:06:00 | NOAA-20 | PANCAS | ESPÍRITO SANTO | Brasil | 3204005 | 32 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 5fe9d776-6639-3c35-ae99-208bfd59ec67 | -22.41438 | -46.88771 | 2026-02-15 04:08:00 | NOAA-20 | MOGI MIRIM | SÃO PAULO | Brasil | 3530805 | 35 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 51c80832-2f2c-3ac3-8fa6-2e4ab26b1c64 | -10.5937 | -44.331 | 2026-02-15 04:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.9 |
| a3ce64f1-879d-3171-a71d-e325f1539b1f | 1.91764 | -60.57036 | 2026-02-15 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ed8dd29a-fd3e-33b2-970d-2b5b2c8a0555 | 4.5446 | -60.70892 | 2026-02-15 04:50:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d4cee0d6-8ef1-3535-9d1c-d7b4b49457f1 | 3.41423 | -60.3443 | 2026-02-15 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 39d01b0c-c87c-323c-927e-d18a4db902d8 | 1.66905 | -60.53265 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 32338cf3-1779-3173-9eca-223f9e87e9da | 3.45261 | -60.26348 | 2026-02-15 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| be6602f9-efff-36bc-ad72-e354ff75a921 | 1.91819 | -60.57403 | 2026-02-15 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5f959f76-6d22-387c-9d63-fe11e0230d89 | 3.45379 | -60.26675 | 2026-02-15 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 101fa163-9f8c-3466-aad7-a61c98cb56ad | 1.86854 | -60.84132 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 6a9c4b80-101c-3216-8475-41a78cb06b71 | 3.45315 | -60.26719 | 2026-02-15 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54581f87-8f26-3637-a6e4-39381b44300e | 1.91265 | -60.57489 | 2026-02-15 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 12755506-c729-333a-b9d2-8ca36af7cc87 | 1.91321 | -60.57857 | 2026-02-15 04:50:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.3 |
| ee0a7a4e-02eb-310d-a731-f2424ef3ad30 | 3.72421 | -60.91098 | 2026-02-15 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 96444cdb-c385-3e0b-beff-e6ec88921fd4 | 3.72941 | -60.90597 | 2026-02-15 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 41822c0d-2575-360b-9640-9e407d7d7ece | 1.66354 | -60.53344 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 917395e6-3c0a-3805-98b2-16dcaea24204 | 1.66882 | -60.53429 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fe4ab584-013c-3b8b-be78-e00a01238b03 | 3.93571 | -60.24627 | 2026-02-15 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 01ce1f54-3d19-33f3-9e05-652c213e8592 | 1.86739 | -60.83375 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| a4dee161-8495-30ae-bec8-a5f74af9b278 | 3.45322 | -60.26305 | 2026-02-15 04:50:00 | NOAA-21 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 13ba64ca-cafc-3749-9061-f0931c282ad7 | 3.72482 | -60.91511 | 2026-02-15 04:50:00 | NOAA-21 | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 602eef64-57db-3ac8-9c8a-171eb0d4e39a | 3.41479 | -60.34804 | 2026-02-15 04:50:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 719d957d-211d-32d5-af3a-43753a0e4245 | 1.86797 | -60.83754 | 2026-02-15 04:50:00 | NOAA-21 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 8d81fd45-5bbe-38c6-97cd-230ce895e78d | -10.67523 | -49.68789 | 2026-02-15 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0225e245-0c48-37e5-8e2d-37838aa8f979 | -10.67552 | -49.68975 | 2026-02-15 04:53:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 558d4232-da2b-324f-86b9-37a1f79d0010 | -10.99292 | -53.99015 | 2026-02-15 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bec0d224-06d7-3937-9ed4-d77ed4aad7ca | -12.50989 | -48.73611 | 2026-02-15 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d2080c78-5730-3f13-adac-cda78386d4b7 | -12.54253 | -49.10461 | 2026-02-15 04:53:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5a0bd814-6be5-37fe-8aeb-2bf3e26f8b60 | 0.90042 | -60.43729 | 2026-02-15 04:53:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d1356cf7-2006-3d62-9e69-a86d9f2a240a | -12.2909 | -49.03573 | 2026-02-15 04:53:00 | NOAA-21 | ALVORADA | TOCANTINS | Brasil | 1700707 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 5ec77341-5e53-35be-8da9-4f4fa88d814f | -4.37028 | -55.77208 | 2026-02-15 04:53:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eb11a774-cd90-3bc6-9d5c-a77dd52e33fc | -12.50578 | -48.73554 | 2026-02-15 04:53:00 | NOAA-21 | JAÚ DO TOCANTINS | TOCANTINS | Brasil | 1711506 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e5c81577-59ed-3eca-8f43-f5795aecba38 | -12.0682 | -45.32721 | 2026-02-15 04:53:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e76db8d5-39ef-38ac-8181-6b4bc8ca14f8 | -10.99017 | -53.98613 | 2026-02-15 04:53:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 43e62902-1ba0-3f5d-9606-cddec4cbbaf6 | -10.61051 | -44.33425 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2c8d1238-d88e-3071-b237-ffd74fd64975 | -15.0059 | -45.14995 | 2026-02-15 04:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 6.1 |
| cfbef0b7-883d-3f2e-b50a-9641118d2302 | -13.76886 | -53.39656 | 2026-02-15 04:55:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ca157c18-3eb9-3dd8-82f1-138de429780d | -18.84412 | -48.26587 | 2026-02-15 04:55:00 | NOAA-21 | UBERLÂNDIA | MINAS GERAIS | Brasil | 3170206 | 31 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 3e1498f4-77b1-3af5-9959-39287662cff8 | -10.59931 | -44.3362 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 34041fa3-d975-3aba-83c4-683743040d4f | -10.59974 | -44.33278 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| a7f6d2b9-4b1e-3a8d-a60a-816e883f6eb9 | -10.60469 | -44.33695 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| df59bb0b-6b1d-36d9-8615-f845e0f68e74 | -15.00009 | -45.15274 | 2026-02-15 04:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3d170969-92d6-3a65-8049-8afe076a61ec | -10.59393 | -44.33543 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 24.7 |
| 3e91d703-55fd-3f55-ba1d-dd0d181d6dea | -20.47371 | -56.72918 | 2026-02-15 04:55:00 | NOAA-21 | BODOQUENA | MATO GROSSO DO SUL | Brasil | 5002159 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 8c4f4d11-10f6-3961-be67-ed35fc5005c6 | -15.00508 | -45.15702 | 2026-02-15 04:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 6b4cc500-466a-371d-9106-388348fa84db | -15.00549 | -45.15349 | 2026-02-15 04:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 3e921410-112e-3f93-ac02-5ee2390d9f5c | -18.64721 | -50.2697 | 2026-02-15 04:55:00 | NOAA-21 | QUIRINÓPOLIS | GOIÁS | Brasil | 5218508 | 52 | 33 | nan | nan | nan | Mata Atlântica | 2.6 |
| e901b24a-78b1-3ba8-a991-69aa7395523c | -10.60426 | -44.34034 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 4a1e9407-cb22-3767-98dd-ad01a820066a | -15.0109 | -45.15421 | 2026-02-15 04:55:00 | NOAA-21 | BONITO DE MINAS | MINAS GERAIS | Brasil | 3108255 | 31 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 289e8513-16c3-3c82-b722-3fddafbc2ff1 | -19.76372 | -48.29384 | 2026-02-15 04:55:00 | NOAA-21 | CONCEIÇÃO DAS ALAGOAS | MINAS GERAIS | Brasil | 3117306 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 067c313f-275b-31b6-8a9b-4d367354e71a | -10.59436 | -44.33202 | 2026-02-15 04:55:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 6121b672-d707-3928-ae89-582870f6a4f1 | -27.8461 | -52.11413 | 2026-02-15 04:57:00 | NOAA-21 | FLORIANO PEIXOTO | RIO GRANDE DO SUL | Brasil | 4308250 | 43 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| ba079aa2-d701-3e4a-bf77-c0c01fba5a3b | 1.8683 | -60.8383 | 2026-02-15 05:00:00 | GOES-19 | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 52.0 |
| eb37e970-89ae-32eb-b0f7-78b2a9077190 | -10.5937 | -44.331 | 2026-02-15 05:00:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 62.7 |
| cf6b2964-63dd-30c4-a62c-90b8aeea74a4 | -10.5937 | -44.331 | 2026-02-15 05:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 81.7 |
| b6f273ae-fa99-3b8b-b224-ece3304cb70f | -10.5937 | -44.331 | 2026-02-15 05:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 70.6 |
| 490457e0-ffe1-33fb-bcb5-97aa1e2dcd32 | 4.1864 | -60.54061 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 75a7b8a5-5801-39be-b72c-b327874f90c4 | 4.20309 | -60.52622 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8a5e1312-60c1-3e47-a630-dc879c93b95f | 4.18563 | -60.53856 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 30031dad-c3dd-378d-9f0b-83b267373d9a | 1.91326 | -60.57226 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d05c4707-a9e7-3262-8b28-ffe08d5b9451 | 3.942 | -60.2524 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 157b57ee-b0ed-3cde-9f03-2170497886d8 | 2.15355 | -60.53417 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4e739653-98f7-33e7-a2c9-140e19aaba46 | 4.54316 | -60.71168 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ff4e0fa2-ce3d-34f0-8888-30dbe6e66650 | 1.91457 | -60.57478 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 31ba1917-cb60-3002-8642-7350feb6442d | 1.86823 | -60.83614 | 2026-02-15 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 32.3 |
| 4821168d-ee3e-38ee-828d-890cd5e2d7a3 | 3.72907 | -60.90443 | 2026-02-15 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f6f3e91d-3fa2-3aba-9d3f-f1059d4f9af6 | 1.91694 | -60.57168 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 645cd2c9-f5da-38c4-8c94-84bdb15e2aaf | 3.71971 | -60.92034 | 2026-02-15 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 49140ab3-f88d-3620-9679-7aab12f25b39 | 4.39772 | -60.06255 | 2026-02-15 05:20:00 | NPP-375D | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b559c8a-7906-3a64-9e2a-00fb8346221f | 3.72596 | -60.90976 | 2026-02-15 05:20:00 | NPP-375D | AMAJARI | RORAIMA | Brasil | 1400027 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f13405c-21fb-379a-872c-05b0bbe53e09 | 3.41004 | -60.65847 | 2026-02-15 05:20:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 738b5462-81c2-34e1-9efd-c7f197af668f | 3.95648 | -59.80722 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 918fb40e-31ff-3a6e-b17a-44ddde29deb6 | 3.95544 | -59.80605 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e642ac8f-0122-3e08-9658-9cc4af6a93b7 | 1.86451 | -60.83671 | 2026-02-15 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 47a27e34-d078-31e8-a148-bc14885dfa96 | 3.79739 | -60.5196 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcc9858e-4e7f-31d7-8a26-9e430134d3f8 | 4.53935 | -60.71236 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e82ee666-b329-3ce2-a95a-1de066409d9d | 1.91824 | -60.57419 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 803844a9-c54c-3936-88e6-adebd6458bb6 | 1.66532 | -60.53215 | 2026-02-15 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 806b63d8-4ac2-3847-bec4-616852ef6958 | 4.60354 | -60.74796 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 2.9 |
| acfee7b3-99c1-3902-93e4-3d84c7180c90 | 1.86891 | -60.84054 | 2026-02-15 05:20:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 17.5 |
| 37297afd-f227-3b8f-bfa3-bcef7aec24a9 | 1.91392 | -60.57656 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 17eb83b2-a2f9-3c9e-8591-3e5e5dec7c6f | 1.91157 | -60.57964 | 2026-02-15 05:20:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 38611867-bb96-3ba0-9c80-b3d383b91654 | 4.24051 | -60.80024 | 2026-02-15 05:20:00 | NPP-375D | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b98cf22d-90a2-3b0c-9a16-2b85259e99e4 | 2.71478 | -60.19039 | 2026-02-15 05:20:00 | NPP-375D | BONFIM | RORAIMA | Brasil | 1400159 | 14 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d32402b6-341d-34c1-b5ba-d42a5c776008 | 3.93764 | -60.24862 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 82253b12-ff56-38e8-b5f9-1af5dfbb9bd1 | 3.94266 | -60.25677 | 2026-02-15 05:20:00 | NPP-375D | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |


[Clique aqui para ver as próximas entradas](README3.md)
