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
| 0c75cc98-8c19-3306-9fbc-f3fd77fe2fa9 | -6.5039 | -43.634 | 2025-06-22 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 086fe215-20e9-399e-81d1-3620ec684534 | -6.92584 | -46.41103 | 2025-06-22 04:14:00 | NOAA-21 | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d2cd77a8-4001-3fbf-8e41-c67141b6305e | -9.14782 | -47.15643 | 2025-06-22 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 011a2f72-93d1-3359-b59b-a5056a3ec581 | -8.07042 | -43.10386 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 6919e51c-6625-3529-9e56-0c6e4739e476 | -9.39115 | -47.50082 | 2025-06-22 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b41f95c1-e30c-3bca-88ee-5caaeb2da8f4 | -7.29434 | -47.83909 | 2025-06-22 04:14:00 | NOAA-21 | BABAÇULÂNDIA | TOCANTINS | Brasil | 1703008 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 85ddcc89-ec8f-3bcc-9c2c-da90abd2f40f | -9.3307 | -47.82262 | 2025-06-22 04:14:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 2caaec93-c163-3abf-a08b-55ec634834c1 | -4.59509 | -47.89026 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b1edbe34-4f3f-315d-bd18-7d9386ba48dd | -8.45404 | -47.0104 | 2025-06-22 04:14:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4b29cd0f-82c5-35f4-91b7-6477a4a32a41 | -8.02601 | -47.65012 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2c0ec895-00c8-354a-bfd3-993316e04f21 | -7.33545 | -45.34916 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 511b6d7b-285f-3ac0-bbef-fab7dd113702 | -7.23232 | -44.66941 | 2025-06-22 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| e8712990-9856-3dbd-aea0-a802581ee192 | -7.23289 | -44.66584 | 2025-06-22 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| c5606ce6-9a47-3ffa-8dff-cfbec56d3adc | -8.097 | -43.1507 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| cc5f2436-bd82-37a8-9556-04e3a1f34427 | -8.07663 | -43.15107 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 61c6512b-6cd1-3ae2-b344-98bb90a605a2 | -10.76056 | -44.0914 | 2025-06-22 04:14:00 | NOAA-21 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4b47f7a2-12c5-31d1-880e-6b700c7f2280 | -8.07319 | -43.10785 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| e9b4300a-5faa-328e-9dae-e3da04368952 | -5.07297 | -43.73035 | 2025-06-22 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51085131-5f7a-3f36-8850-1734a031ae35 | -7.31616 | -43.18361 | 2025-06-22 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 4ff626ae-e6d7-3560-a52b-2b949369093b | -6.86174 | -43.15371 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 0d1dc277-8352-3ac7-931a-1f8c552489d7 | -9.0999 | -50.02342 | 2025-06-22 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 1340660a-9a4f-3d72-bf64-8c3e7d68934c | -8.41764 | -48.30198 | 2025-06-22 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 04a20256-b1a4-37f1-9357-35d8e419d541 | -4.54149 | -48.0137 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6d74fe2b-d066-3f12-850f-34c3913c4fb7 | -9.41632 | -48.42767 | 2025-06-22 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 7612ed9a-9890-35ad-8fa8-50b25b140634 | -7.22825 | -43.57299 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 7e646910-8baa-3ce2-a478-73509e4485ff | -8.43879 | -49.54877 | 2025-06-22 04:14:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 589920dd-9d1a-3c6e-b4a7-153827921bff | -8.01991 | -47.66352 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 643e96f7-c4ac-3e85-84a2-85ada0638e91 | -8.01235 | -47.66228 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| de72719e-929a-3587-b10f-41d66885c305 | -9.46079 | -48.61758 | 2025-06-22 04:14:00 | NOAA-21 | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b036ef08-93a6-3621-8db7-8dad10af557b | -7.87377 | -47.88847 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| cc323519-c280-3393-8d83-a291b4602895 | -10.96584 | -40.88253 | 2025-06-22 04:14:00 | NOAA-21 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 5c8359f9-a5fa-3adc-823e-812e1cf396de | -8.60461 | -51.58735 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f234239c-7080-3b97-83e5-d1c953b29335 | -7.10708 | -43.7161 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b49f28d0-c65d-3f45-ad96-744d63f8423b | -4.33679 | -46.78032 | 2025-06-22 04:14:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 18511aec-ef16-30ee-a317-18926cdee15a | -7.33604 | -45.34545 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c1bf3bfd-cd7e-32f9-a2e4-95aed351eb62 | -7.90243 | -46.23152 | 2025-06-22 04:14:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| faed710d-60bc-31ac-91ab-c6d7339c8abb | -6.85736 | -43.16009 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 5735d456-bf17-3e16-954e-add129973dea | -9.8832 | -48.05584 | 2025-06-22 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5f9f2b7-4d83-3455-8e16-0da3baa4bcde | -5.57547 | -45.21792 | 2025-06-22 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a1cf0f5d-e56a-3e18-bf68-54ee4e424299 | -8.09369 | -43.15019 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.8 |
| a49d7e72-6965-3f19-8e75-b39a6d2f72e2 | -8.42155 | -48.30264 | 2025-06-22 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 3bfd366c-b4dd-30b7-b261-5e79f3f9e54e | -7.11038 | -43.71661 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 12b7fbe8-4e78-33aa-bfeb-44554b80c230 | -7.09194 | -44.37137 | 2025-06-22 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f3ebad17-9fae-3be3-bbcb-f5e7906f0e2a | -7.31724 | -43.17669 | 2025-06-22 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| b885c014-d3bb-3eaa-8c36-7b4f4c885661 | -8.59484 | -51.58609 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| e68f7881-b7d0-3954-b30d-90d4526687e6 | -6.86504 | -43.15422 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 1f4feb46-7065-3971-94e8-c1e7e89be306 | -9.99929 | -48.05912 | 2025-06-22 04:14:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 51ff0e21-fc5a-3f27-943b-573251facc9a | -6.5072 | -43.63453 | 2025-06-22 04:14:00 | NOAA-21 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| bca5dfc7-6be3-3372-9fc1-913d6f522339 | -7.15792 | -43.19713 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| c3a046bc-a691-3a07-986a-644f364b3380 | -8.07994 | -43.15159 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.3 |
| 8d4fb546-a39d-308a-81e4-7a464cb0e2ff | -9.42184 | -48.41854 | 2025-06-22 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 2678c3d6-63b4-3f8b-97ba-885ba2481ba2 | -8.10084 | -43.14775 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 1758b1f4-0232-3590-aa6b-376b3bd392e9 | -5.77064 | -46.56933 | 2025-06-22 04:14:00 | NOAA-21 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4d7a5342-bf86-3cfb-844d-ee6e6b8a63d4 | -8.07373 | -43.10438 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.3 |
| 171c46d7-a480-3500-b4ef-a9b5a063fc33 | -8.01157 | -47.66694 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d8f48816-bf74-3249-b1ec-cebdaef17849 | -8.03131 | -47.64148 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5c63433a-9d5f-3ed8-9de1-2504a286f684 | -4.42855 | -48.14152 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 03c22c19-696f-368a-914a-29e522e656c8 | -5.33085 | -45.23061 | 2025-06-22 04:14:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| feb1fc5a-dc21-34ee-9b26-b7380e48657c | -8.81299 | -38.39311 | 2025-06-22 04:14:00 | NOAA-21 | PETROLÂNDIA | PERNAMBUCO | Brasil | 2611002 | 26 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 3945ae09-c913-3829-a83c-d1756caa932d | -9.42102 | -48.42344 | 2025-06-22 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d6a9f27-bdee-3d93-92f7-df9091096b44 | -8.06988 | -43.10734 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 9.9 |
| dbfa4eda-db2c-369a-88f2-0fd0f2e14b73 | -8.10414 | -43.14827 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 514b8fbf-373f-35f7-991f-64b3138cbcb2 | -8.24969 | -44.94914 | 2025-06-22 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 5d6b0c0f-07d2-3358-b82c-d2e5dc82657b | -7.08805 | -44.37434 | 2025-06-22 04:14:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 71123ed7-c486-3969-a7e9-d2ff33ffe4e9 | -9.56066 | -50.78023 | 2025-06-22 04:14:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 67cca56d-9271-3f59-9c1a-25d6aba91a51 | -8.01613 | -47.6629 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2010fce3-8d54-38ff-a4cd-6193ec1d3e1a | -7.27667 | -45.36646 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| daf549cf-29ce-3632-954f-6d731403bbc4 | -6.86066 | -43.1606 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| b5d8523a-8bf2-31d0-bdb6-d2354e4ef707 | -5.15835 | -46.09184 | 2025-06-22 04:14:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ce22e277-31ef-3931-b6da-0d340d6ecea1 | -8.60066 | -51.58149 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| fbd2e1c2-96a5-3f5c-a3c9-b4eee7d9d46e | -5.37209 | -47.29642 | 2025-06-22 04:14:00 | NOAA-21 | JOÃO LISBOA | MARANHÃO | Brasil | 2105500 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fcb47cf3-ca9b-3b6c-a1ed-8ac100f1cb7d | -4.54557 | -48.01431 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 06db30bf-b9be-3f47-8930-ca414fe32ce6 | -8.59581 | -51.58071 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 58ea011f-6973-3566-b668-a69fff83656d | -8.11459 | -43.14635 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.0 |
| 25d6c24e-2592-3fe4-8ce9-005a9584bca2 | -7.2206 | -43.20692 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7864c4a3-db83-3932-ab55-d5fbbb287b4a | -5.07352 | -43.72687 | 2025-06-22 04:14:00 | NOAA-21 | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08782654-ac3b-39d4-9f70-e18fc5f9edd5 | -8.00856 | -47.66167 | 2025-06-22 04:14:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| db84e597-3192-376b-993a-14bd00548cfc | -8.42239 | -48.29765 | 2025-06-22 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 703ae7c3-3070-39d7-ade4-1c1c851987c5 | -6.35285 | -42.22377 | 2025-06-22 04:14:00 | NOAA-21 | FRANCINÓPOLIS | PIAUÍ | Brasil | 2204006 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 18e11afb-4f05-3e37-8ac0-907f057d8dae | -7.33945 | -45.34599 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a8f762fd-ad43-35e7-a577-e5c4d1e72bff | -7.21784 | -43.20295 | 2025-06-22 04:14:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 0.2 |
| f36bd7e8-697f-34e0-b669-c661772886e1 | -10.05126 | -44.38423 | 2025-06-22 04:14:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 0.3 |
| aa30b418-006f-3a41-ab61-25b943433cba | -9.42266 | -48.41364 | 2025-06-22 04:14:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| a9da692a-fbd8-36ef-b74c-2d774599edca | -9.14853 | -47.15218 | 2025-06-22 04:14:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| a9af98d5-7e25-3d39-abc1-3a9a9d61d4df | -4.54497 | -48.01793 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0c284531-8a96-3428-b3f0-f60c6457f68f | -8.1179 | -43.14686 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 52a71a3f-3b81-3ba5-a219-e38969b6510d | -7.10432 | -43.71212 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0e9465be-8b29-3fe5-b95a-ad0ccc54b0e3 | -7.32222 | -43.18809 | 2025-06-22 04:14:00 | NOAA-21 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 1cc8f236-daba-348e-8d63-9e17db88c3d7 | -7.22867 | -43.52711 | 2025-06-22 04:14:00 | NOAA-21 | JERUMENHA | PIAUÍ | Brasil | 2205300 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| bd597f7f-c2e6-37b4-ab04-0dbb75031918 | -4.42793 | -48.14526 | 2025-06-22 04:14:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 11625803-b97b-3072-905a-ef0a8fc36c6f | -7.27445 | -45.35847 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 61d4376f-1694-31bf-bd91-c5f638eebf68 | -8.10798 | -43.14531 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.7 |
| 21ff243b-bb32-30e3-a319-25e23e00dd5e | -10.64989 | -44.49539 | 2025-06-22 04:14:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f2a42c9d-9d82-33ab-8d9b-ee3f11193c61 | -9.52977 | -46.29634 | 2025-06-22 04:14:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 98748440-01f8-3847-9332-ca14fb91490e | -5.63447 | -45.79928 | 2025-06-22 04:14:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 6196ecc8-f37f-3e03-a466-4863da7324ec | -7.27104 | -45.35792 | 2025-06-22 04:14:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8be7caf9-a3b1-36ee-8027-da41a2d6b6b0 | -8.10745 | -43.14878 | 2025-06-22 04:14:00 | NOAA-21 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 10.5 |
| 6d35f4ed-8bb3-391f-a5b5-968c6bc00b23 | -8.42545 | -48.30329 | 2025-06-22 04:14:00 | NOAA-21 | PRESIDENTE KENNEDY | TOCANTINS | Brasil | 1718402 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 302798f0-264c-377f-8a81-df8f4aee1354 | -8.5939 | -51.59127 | 2025-06-22 04:14:00 | NOAA-21 | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4cf979a7-2fc3-3b53-8eaf-8181b82a0649 | -9.19277 | -45.33387 | 2025-06-22 04:14:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |


[Clique aqui para ver as próximas entradas](README5.md)
