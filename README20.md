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
| fc2ada08-f260-3211-94a1-142e0c31036f | -9.68539 | -56.98651 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 651f4fc6-c13d-340e-ae82-3b212cf3b2ac | -10.65239 | -49.42544 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 1182fa0f-ba96-35f1-8ac0-ee86eeeb4973 | -11.13643 | -53.94533 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2dda59c4-d664-3d15-aa96-47c2bbf043be | -11.567 | -54.57426 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| b59baa25-5d16-3abe-b53e-6269c33ab89c | -11.07953 | -55.07287 | 2025-06-13 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fcb3d1e7-9b5e-3157-9819-cab82126c1b4 | -11.91469 | -57.46153 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 31a0021f-8b62-3c22-882e-59f145a0f31e | -10.36601 | -57.50587 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 50625692-b232-33da-a1de-d09b91e786e7 | -11.37013 | -56.55913 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6b4212c2-6cac-3587-9b1a-d47415be52ec | -12.20241 | -54.26688 | 2025-06-13 05:23:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8d3f395e-b378-3dc2-9a57-68ce4c2baddf | -9.40758 | -57.55124 | 2025-06-13 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 6aa23a6d-1b47-3094-8071-9c886f88070b | -10.30139 | -57.13982 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 95ceabff-eebd-3682-94a8-7c28bfef47d3 | -9.4074 | -48.42516 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 3a089c04-aff6-3fe2-81b0-e96690197d4f | -10.64666 | -49.42884 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 0a9d84a8-295b-35a4-b4e3-95abadb1e239 | -11.37062 | -56.55554 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d6074e14-5c63-3fbf-94d9-cde07ac749e3 | -9.22182 | -62.47554 | 2025-06-13 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6e4e652a-2eba-37eb-b97c-d89eb347d2a9 | -10.16053 | -54.89957 | 2025-06-13 05:23:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da4051d5-8948-380c-babc-ee7d17c4766e | -11.58729 | -51.33924 | 2025-06-13 05:23:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 44cb13d0-9968-3a5b-b00f-825287ae53e6 | -10.81104 | -55.87263 | 2025-06-13 05:23:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d2477dca-f685-39c0-a19a-425e3b27884a | -10.84677 | -53.7752 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 432ef3b1-3241-3da7-a5a8-6a25bb911022 | -10.70352 | -49.5016 | 2025-06-13 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 57d947aa-7953-3d3d-8695-0ab31e51df3d | -11.57631 | -54.57545 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 42750b63-2378-3800-8a1c-1f54482c4a0b | -11.36607 | -56.55856 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75e545b5-d821-304a-bdec-8f0a50868d30 | -10.04577 | -64.98114 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 690219f4-dd4d-34d2-a7f6-76d0a9f7df50 | -10.81506 | -56.95888 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e779bff1-c52f-31ea-b276-b3b8c69a1c1a | -11.91855 | -57.46209 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 88fc8ea5-9c3c-35d3-b47c-751699b5a4e3 | -10.64793 | -49.41764 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| d3a83f2c-1849-34e2-baed-b20eb4db198a | -11.12934 | -54.21731 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b67daa67-cc34-38e6-8f31-2f8666095917 | -10.92349 | -56.84181 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| df94a3c7-6d95-356d-a2b3-2bc351afda71 | -11.10295 | -60.85156 | 2025-06-13 05:23:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 770ab3ae-0ca2-3ec1-ab40-1192f4194e24 | -11.56234 | -54.57362 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 13.8 |
| 22802e43-fb9b-38c0-93f1-26e46d3c7d90 | -11.1316 | -53.94463 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| da02a8a1-9eee-35e3-8f72-56d1dae256e6 | -10.0241 | -57.32647 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 4481c84f-bf84-375c-923e-b4017f023ebe | -11.99325 | -57.21295 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| df06650f-04db-3ef9-a553-c3df441be4fb | -9.25346 | -57.53754 | 2025-06-13 05:23:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cbce8b7c-23ca-3edc-b1ad-f188acc9f2bc | -11.91786 | -57.46703 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| def73fdf-3599-3b7d-9eb1-c0428747751d | -11.81495 | -54.50435 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| be383221-95a0-3f4b-9f7b-c99232f1ce7c | -10.35483 | -51.98885 | 2025-06-13 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4f21e0c7-d14b-388f-8549-9744e55a961a | -11.07568 | -55.06773 | 2025-06-13 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e7e59a6c-159f-3509-9ae3-f7afb1d50091 | -11.57165 | -54.57487 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 6f1a9d8b-4fbe-358b-b3d5-2621e53bf6b0 | -10.29493 | -57.14235 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 32773d53-0f21-3491-9429-429e49dc701a | -10.23875 | -52.23793 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 3e454e49-a589-3bcf-a7a3-c8a5f81c5754 | -9.88281 | -61.39656 | 2025-06-13 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a7bd415c-24eb-3228-a423-07c95eef58d4 | -9.87951 | -61.39604 | 2025-06-13 05:23:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b970c705-2174-3960-8e23-00b62e02da8a | -11.57295 | -54.565 | 2025-06-13 05:23:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 83d52e35-eaeb-3fe3-b0d3-803cbc715f03 | -10.69711 | -49.5007 | 2025-06-13 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 83b2a9f2-b81e-3cfc-a422-37566f7d6389 | -9.22296 | -62.46839 | 2025-06-13 05:23:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| d1cc183f-4631-3ccc-b0ad-ee6999630176 | -10.86526 | -54.29634 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ef8c293c-8488-310e-a909-2a0be8a0c497 | -10.69837 | -49.48999 | 2025-06-13 05:23:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 9d8af780-d23b-3be5-b4ef-2706dae29dd8 | -10.65171 | -49.43103 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 16986e53-a6aa-33d2-bdcf-83aac2c7f642 | -10.64596 | -49.42447 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| d0a18756-13ec-3af9-b22a-31bcd527726a | -10.64087 | -49.4222 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| f58ee9c1-c85e-37cd-9421-52d9611dd619 | -9.3932 | -48.42921 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc0f5370-c3ef-312a-8dc9-159e2f1ebf0d | -10.86458 | -54.30141 | 2025-06-13 05:23:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 851afb94-4dca-37ad-8838-b7c67959f7c4 | -2.95564 | -60.01439 | 2025-06-13 05:23:00 | NOAA-21 | MANAUS | AMAZONAS | Brasil | 1302603 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 04fe8d79-04ad-3706-b43f-e3026f8c53f8 | -10.63821 | -49.43446 | 2025-06-13 05:23:00 | NOAA-21 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 9997dba4-d2b5-3ac3-8cbd-5c418b54d65e | -8.68085 | -64.87392 | 2025-06-13 05:23:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 9c4899a4-2528-32c5-852c-34bce4ee4e10 | -10.2764 | -60.54379 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9eb106cd-bc6c-36f9-a3fb-7057a08e311e | -11.36915 | -56.56637 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b72c2df8-04ef-3666-af56-06d836e00892 | -10.3544 | -51.99234 | 2025-06-13 05:23:00 | NOAA-21 | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4940d1b3-eeff-3f3a-abde-65a35ec87326 | -10.04505 | -64.9855 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23f31f95-4983-3aa8-940e-9cd3c9801053 | -11.91331 | -57.47141 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7b1057a0-2473-3dd1-ad48-6320178adbc6 | -9.18269 | -61.86536 | 2025-06-13 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 85a2876b-7e90-3088-86e3-2699ce76ed7f | -10.93435 | -55.31575 | 2025-06-13 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| bef9fba7-9955-38f2-afbc-3b1c2af06ac7 | -11.8434 | -57.86041 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e9a6a61c-24e4-3a4d-a014-898f5ef27dbe | -10.29544 | -52.84047 | 2025-06-13 05:23:00 | NOAA-21 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fa99feff-f7c3-3b66-93ca-914e5ad8a968 | -11.36964 | -56.56273 | 2025-06-13 05:23:00 | NOAA-21 | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 677645b8-e457-3cc5-b2eb-ef0e7ec12b8c | -9.6755 | -48.76435 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8104745-c776-34e4-8ce6-21cee1c945e2 | -10.52085 | -59.389 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b1c981bf-9c19-33b9-83bd-f70efbcf64b4 | -11.80282 | -56.97132 | 2025-06-13 05:23:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b8d93378-ca51-3674-b64c-7787c0170438 | -10.93494 | -55.31142 | 2025-06-13 05:23:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 15fc53d8-c8fa-3bd9-9422-e8d72ef17c7e | -7.89264 | -61.47525 | 2025-06-13 05:23:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ca4dff38-e57c-3b4a-967c-b279e443b194 | -10.92096 | -56.83095 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9efb79d7-a59c-3a20-91fb-9ee01e9b94cf | -10.31434 | -59.0871 | 2025-06-13 05:23:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d3c1acf9-dfaa-37ea-b7a6-dc83c370b41d | -9.66812 | -48.76963 | 2025-06-13 05:23:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 3.7 |
| b7dbd54b-cdc8-3e97-b991-3f5bde567316 | -10.29754 | -57.13926 | 2025-06-13 05:23:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 67999ba9-4087-3810-a927-00cca4c9ede6 | -9.96015 | -64.97581 | 2025-06-13 05:23:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| fd5e2e59-fb14-35ae-b3be-ccf7596daee4 | -9.17938 | -61.86483 | 2025-06-13 05:23:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6eceea8-5343-3425-adaf-4ae3750ccf53 | -11.92035 | -57.47746 | 2025-06-13 05:23:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 622f6cea-72f8-3f27-baa8-57eb4a581411 | -14.19521 | -57.41177 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| b8d9888e-15f7-3d7b-9874-aca14431315a | -13.65498 | -53.94123 | 2025-06-13 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7a2f9c3b-f545-3880-8125-4325353d3d28 | -13.89785 | -54.62908 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| ec71be84-e3e0-32eb-8a25-878404df260f | -14.19618 | -57.40451 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9b847c23-f83f-3d03-970a-d9b5ede9f82d | -14.67755 | -53.37688 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| b856184f-f195-3f76-a915-2fcafa005831 | -14.20465 | -57.40208 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 7bfe8113-74a2-3696-b10d-94315de6c021 | -14.6783 | -53.37033 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| abfbfc53-ee3d-3eb1-ba0b-471c60270019 | -14.19569 | -57.40813 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 9c105056-c0a4-3944-a7b8-f5e306a3f63c | -13.24975 | -56.53852 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| fdb48c96-eb61-3b5c-8f74-38eedeb6857a | -14.6685 | -53.36242 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8466614-f1a7-3911-ad1f-ff3eb79d8faf | -14.67376 | -53.36317 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| b6a2edd9-a7ef-339d-be05-bcfd56a6b4f4 | -13.8924 | -54.63377 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 13.4 |
| bbbca510-89e5-31b1-8341-4ec993d4baf9 | -12.43428 | -54.87369 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 87043cf1-3911-3077-a90d-dbba7d1dff6c | -13.65998 | -53.94191 | 2025-06-13 05:25:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3cab0eae-6a81-3107-8e53-feeb7e7a9258 | -14.67866 | -53.36713 | 2025-06-13 05:25:00 | NOAA-21 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 6.1 |
| b6769d73-e280-3071-adff-79dd70dcb8e8 | -13.90399 | -54.61876 | 2025-06-13 05:25:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 387d8f37-1d6b-3049-ad53-c5aa5826da5d | -12.51887 | -57.23541 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 62bd3b74-7bb0-3100-8339-0af5aa98caf3 | -14.20514 | -57.39845 | 2025-06-13 05:25:00 | NOAA-21 | NOVA MARILÂNDIA | MATO GROSSO | Brasil | 5108857 | 51 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 49608c68-f1ca-375a-b1a1-2a1406988872 | -13.46865 | -56.85683 | 2025-06-13 05:25:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 80a124ca-1d00-3b39-8bac-223d6ebd6a12 | -13.0972 | -52.28592 | 2025-06-13 05:25:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69365f79-334d-3024-a50b-9bd1e03fdc2a | -17.37841 | -53.81935 | 2025-06-13 05:25:00 | NOAA-21 | SONORA | MATO GROSSO DO SUL | Brasil | 5007935 | 50 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ab1486c2-7d80-3ffb-b0f9-b48ce9cc41df | -12.43113 | -54.8669 | 2025-06-13 05:25:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README21.md)
