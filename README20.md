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

## Dados Diários - Página 20

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 86d695b8-fdb4-35fd-a95f-a6c85a92c277 | -3.08568 | -50.47502 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 4b2fa7e9-f3ff-328b-9c2c-14e362f1f295 | -3.08489 | -50.47965 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| 3045745a-54cb-3697-b743-06f17aa49740 | -3.08409 | -50.48431 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 7e7f9e63-4eec-3eb7-854d-232fe3dc3e18 | -3.07875 | -50.4786 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e3a85e84-dbbf-320d-b4bb-fd5fe7f15cb6 | -3.07795 | -50.48329 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8a2debac-2d66-3536-af03-44babcbb14ba | -3.07286 | -50.47735 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1311d8c8-feb5-3e20-a8ad-9acfe3862c81 | -3.07261 | -50.47762 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| c578f01d-c1cb-3c38-9230-8e7387cc566a | -3.07208 | -50.48207 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| b9e527ad-69f9-370a-a725-00d11f629f3c | -3.0718 | -50.48232 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 212162c0-26a6-3d91-bfc7-8e48a36b52f4 | -3.0713 | -50.4868 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| ec1309aa-9481-35ef-9807-4c28cbac1120 | -3.07099 | -50.48705 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| a2f75451-6166-351a-9c78-8fa683e4b62f | -3.06593 | -50.48108 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 730f960c-c0a2-38eb-b871-57bf1e5b9856 | -3.06565 | -50.48136 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe706976-e22a-31c6-b246-4a0f6f48c2d5 | -3.06515 | -50.48582 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 46ddbcb0-9afd-35d8-a1cd-ec410ea2d550 | -3.06484 | -50.48608 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| e48ea532-e076-3db0-8ea2-a74a7941849a | -3.05676 | -49.5603 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| daa114d8-7ccc-3b38-8565-ea7922bf319a | -3.05606 | -49.56446 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1a14541-9dc5-3314-bb01-e21eda336bb0 | -3.03565 | -49.54428 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 7.6 |
| 2c162e32-42cb-3229-9cc8-31812f2f6e69 | -3.03495 | -49.54844 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 0e1e2946-6d67-31c4-b92a-64cc04afa773 | -2.90218 | -49.55731 | 2024-09-29 04:00:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3a17b0d3-5865-3e5e-a508-e4c1c0de5207 | -2.90151 | -49.56062 | 2024-09-29 04:00:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| e150fc6b-245d-3f4b-8e24-6dec2c99145f | -2.90149 | -49.56136 | 2024-09-29 04:00:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| add4ee55-7d72-3611-88f8-8d5e70f8a436 | -2.89876 | -49.11544 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84de88e8-c0b9-326a-91fb-0679e52022c3 | -2.89311 | -49.11455 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ac1bbab0-140d-3532-977d-9184b09b9a22 | -2.49033 | -49.0539 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 63e19ee3-9f4c-3d51-b6e2-d03ec6744e5f | -2.47861 | -49.15982 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 67d58c46-7aeb-36df-9451-ce74ed2082d0 | -2.47796 | -49.16375 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 434b91eb-4a77-3cb2-a2f9-1486e86e8fe6 | -2.47359 | -49.15485 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 124d4aa8-70a4-316e-8034-b049c56e8952 | -2.47293 | -49.15879 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f44c4223-5601-385c-9e93-d5bc1fa3aa24 | -2.47228 | -49.16273 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 993883f8-e7f7-3129-a1a1-46565e3039ca | -2.46189 | -49.085 | 2024-09-29 04:00:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4890b4f3-033d-35ce-8e9f-7ad1d697b321 | -3.29901 | -50.66665 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b3cb7351-2444-3993-9879-322ec8b5a8fc | -3.29819 | -50.67147 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| b88413f4-4d40-3086-be59-e24e3650d424 | -3.01265 | -51.0531 | 2024-09-29 04:00:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5234ee8b-8621-30a1-8b25-08a8bf45dab8 | -2.9587 | -51.64821 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 44875ec4-bf03-3acd-9deb-5591b4fd3a96 | -2.95677 | -51.64887 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 5d5552da-c20b-3519-8042-7c121c1fc9ae | -2.88396 | -51.57927 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 80bc99b3-68b2-3846-834c-f6ecc4152add | -2.88254 | -51.57793 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b9c91ad1-c0f4-3197-8cec-403ef71f7ac3 | -2.87908 | -51.67653 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 08b96b55-74dc-3fdf-9a16-263482f795ec | -2.87641 | -51.66559 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3de2eccd-44eb-348b-bbfa-f126ad8a7ca5 | -2.87452 | -51.67704 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 7de782f2-8b82-3488-840f-fb42fe906d25 | -2.87245 | -51.67543 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 66db0ed0-7f3b-3576-8dea-bd3aa65618ea | -2.87146 | -51.68116 | 2024-09-29 04:00:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c3215fed-7695-3b11-bc63-3b1876b62e79 | -1.87646 | -52.09372 | 2024-09-29 04:00:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 11.5 |
| d8806e54-d5b4-324d-8cc9-ed99773084ea | -2.6846 | -52.43383 | 2024-09-29 04:00:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 8eb30ddc-a641-3561-bbe9-5be7322278f9 | -2.68347 | -52.44046 | 2024-09-29 04:00:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dce71651-b4e8-3d05-92b3-bab59ed7397f | -5.62072 | -36.83301 | 2024-09-29 04:00:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 5.4 |
| 8046dd1d-7d11-3b26-a7c9-201bd38e28a1 | -5.62012 | -36.83704 | 2024-09-29 04:00:00 | NOAA-21 | IPANGUAÇU | RIO GRANDE DO NORTE | Brasil | 2404705 | 24 | 33 | nan | nan | nan | Caatinga | 7.9 |
| af6dbddc-6bc3-3180-a054-f4900530a89f | -5.19847 | -35.61086 | 2024-09-29 04:00:00 | NOAA-21 | TOUROS | RIO GRANDE DO NORTE | Brasil | 2414407 | 24 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 8240eece-d810-3839-bdb7-ad9fe5583d47 | -5.07175 | -37.72347 | 2024-09-29 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 5.6 |
| 5f6f0a63-9c07-3f21-8b91-416ad8680b1e | -4.91503 | -37.48769 | 2024-09-29 04:00:00 | NOAA-21 | BARAÚNA | RIO GRANDE DO NORTE | Brasil | 2401453 | 24 | 33 | nan | nan | nan | Caatinga | 2.5 |
| a164c31e-c1a1-3184-abac-5c41c7ee7c30 | -5.13146 | -38.15312 | 2024-09-29 04:00:00 | NOAA-21 | LIMOEIRO DO NORTE | CEARÁ | Brasil | 2307601 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| cab97dcf-9c3d-38c0-953c-3fb23b6b82d4 | -3.04748 | -40.1188 | 2024-09-29 04:00:00 | NOAA-21 | BELA CRUZ | CEARÁ | Brasil | 2302305 | 23 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 71dd539f-108c-36e1-a7de-5847313a41d7 | -2.95843 | -40.12281 | 2024-09-29 04:00:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 3bd97a4b-bd32-379b-a2d4-241d00eb6705 | -3.96468 | -41.48688 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 84fecab5-6035-34fa-b4f3-2b0774206eb5 | -3.96004 | -41.49387 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.6 |
| 1ba8d533-6851-3cfb-8706-a6771fa97359 | -3.9566 | -41.49335 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.6 |
| d263249f-659d-3753-9a10-8717cdeacf99 | -3.95646 | -41.51648 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 68350575-b272-3290-89ea-d3cc72b1b503 | -3.956 | -41.49712 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 219df489-bd68-36b6-8ebe-1ff0e1542ace | -3.9554 | -41.50088 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| f0eda459-0ae4-3ca6-a8b2-3393bfdf7de0 | -3.95301 | -41.51596 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 8a191946-870a-342c-95f2-b3028e45c059 | -3.95256 | -41.49658 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 57db41bc-a4a6-396f-9381-31597f8fff9a | -3.95241 | -41.51973 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| d7eff2e4-dbbf-3cfa-a8b1-51e1996281d9 | -3.95196 | -41.50035 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 8.6 |
| 1773e18b-3f49-3f2a-92ec-446e04f36c4f | -3.95181 | -41.52351 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| fa147b0d-c01b-3881-ae70-b5fd57c60e9e | -3.95076 | -41.50788 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 1ac65341-3f1b-3bff-ac8f-117f7c166ebb | -3.95017 | -41.51165 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 4f340498-9056-34bc-ad2d-1068ebe60fe3 | -3.94957 | -41.51542 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| 1ee287e1-6900-354a-98ff-247fe3ce7385 | -3.94896 | -41.5192 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 9.8 |
| 2a586a94-b8dd-391f-9b9e-f8a0c3b45d18 | -3.94792 | -41.50358 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| c2648fce-524d-3793-8af7-3f7b20222b97 | -3.94732 | -41.50735 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 7.9 |
| 88635d17-0184-37aa-bb08-71b3f51071ec | -3.94672 | -41.51111 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 24548ec1-ecbd-3319-a156-b17a048bdb84 | -3.94612 | -41.51489 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78b06924-acf4-3ace-9003-83a2c7707d3a | -3.79952 | -41.59624 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| cba590e4-3040-3f08-9a93-8a1e5c690cf5 | -3.79891 | -41.60005 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5dc895ec-b262-339d-adfa-5dd3d02af081 | -3.79728 | -41.58808 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| 8253b476-9b21-3a0e-a9bb-3cc1d52ab1bc | -3.79667 | -41.59188 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6b8b7ee-df99-38c2-8b1b-fd2627eed94a | -3.79606 | -41.59568 | 2024-09-29 04:00:00 | NOAA-21 | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 2fce5354-29b4-3f20-a8fd-5e31727632ce | -10.25812 | -43.56624 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 7c01c88a-052e-343b-9700-e4b782c0ad83 | -10.25613 | -43.57825 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 4c2e813c-d883-3dfb-a561-8b93a8b74cb2 | -10.25547 | -43.58224 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a2fd9f43-dfdc-356c-82dd-0aa4b253572a | -10.25525 | -43.56163 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5aa0b3f7-0fff-3fa0-91a0-8e5fd4bc334b | -10.25482 | -43.58622 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 6e14e4a9-bad2-3914-9032-9d192cf59d07 | -10.25459 | -43.56564 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 3da63c89-1901-3b62-b0ba-d5ea16aa2620 | -10.25393 | -43.56965 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 702423de-c62d-3412-8bed-ad83643f2f66 | -10.25326 | -43.57366 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b43cf9df-769f-3f46-aba4-2724cdadcbc6 | -10.2526 | -43.57766 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2bb2b291-d550-3bd2-a81f-3ba70a902a75 | -9.48617 | -44.07621 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 2dcee659-ff86-33c1-99fe-8d0d770155a9 | -9.48396 | -44.06705 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 95394893-993a-3a69-8035-90a03c9348ac | -9.48106 | -44.08427 | 2024-09-29 04:02:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 75befb35-4d63-3ae4-9d8b-92e12c941392 | -10.13064 | -43.37271 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 1533ee37-0876-3081-a8b2-2f03df36de69 | -10.28281 | -43.57042 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4bb6845a-c759-36a2-925f-c97ddc50559f | -10.27553 | -43.54855 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c50e61d4-fe6f-3058-85be-d4f62ff688c6 | -10.26297 | -43.55881 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 81f894e0-ea10-35fb-b2fc-b33be7eb5642 | -10.25944 | -43.55822 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e57a2b23-7397-3176-ab62-78d7846e5323 | -10.25878 | -43.56223 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2337c975-0a75-343c-805c-1a6adeeb45d9 | -10.25194 | -43.58166 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| afc0f4eb-c6fa-3d7f-9b2b-ba88d2add447 | -10.25128 | -43.58564 | 2024-09-29 04:02:00 | NOAA-21 | BURITIRAMA | BAHIA | Brasil | 2904753 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 8f8f9b51-e697-359f-954b-19da362a86bf | -10.2504 | -43.56907 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1cf7b099-5afd-35d8-ac94-9d8042ff7b90 | -10.24973 | -43.57307 | 2024-09-29 04:02:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |


[Clique aqui para ver as próximas entradas](README21.md)
