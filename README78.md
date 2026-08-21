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

## Dados Diários - Página 78

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1323a0d5-c898-34ea-b4a0-2e4e43db02e2 | -8.52554 | -55.33356 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9aa3d533-1be9-373d-9239-2d501f48faf5 | -6.42671 | -52.72445 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 062ef13c-1f7e-3173-b6d9-e5ccba9f427b | -9.11598 | -61.59811 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6dca4e86-1afd-321d-9f18-c925b6beee73 | -6.65897 | -56.35156 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 924ab13d-b541-3328-a803-1b17d6c73645 | -7.86485 | -63.76329 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6e604d37-8684-35bc-a8cd-bcc3c1301a02 | -5.81119 | -55.71761 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cdbd41ba-d471-332c-a111-4816f170ccb0 | -7.44506 | -60.00401 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fa39f072-6584-3ce0-bb61-4c63807f443c | -8.18535 | -63.88537 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 81f2c0b9-6305-309c-a21e-fd383e231fe5 | -6.72128 | -59.09394 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 881abd9a-bad1-3add-9790-9d52ac11a2d2 | -11.18735 | -54.01439 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b18b1ce-fb0e-3f60-a90e-8644d3db8d92 | -8.54455 | -55.31243 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5f7b4581-e9a5-38c0-becf-28962460e5b0 | -6.2489 | -55.41343 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cb28dd1a-0171-3816-acb8-a3cddf87c455 | -6.85977 | -59.02534 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb01bbe8-94f5-3db7-bf9f-e0661e5f0f19 | -7.43518 | -59.79013 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 57172919-56c0-396f-b2d6-92881fed8014 | -8.58076 | -54.78099 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 725ecd53-877c-3249-aaad-2b3b536207ec | -7.89123 | -61.66548 | 2026-08-21 05:42:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a77c130d-4a0e-3d48-85d4-c2f238600445 | -6.3854 | -54.95045 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2f17eabc-48d0-31f4-8726-8a26f2f75d11 | -7.60257 | -60.95989 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3af6a7f-8aff-394f-9176-ca0cb60830b1 | -9.1118 | -61.60162 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6b31f774-fd95-3b31-8a87-28d277546730 | -9.12373 | -61.59515 | 2026-08-21 05:42:00 | NOAA-20 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c7f58d3-1b73-3140-9ad3-6bd2c8365d5e | -8.39384 | -62.70149 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c2383e54-71e1-3b9b-b48a-d6bf1f7602ed | -6.6081 | -58.38757 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 182e2e0b-872e-3ed8-bc00-a0dcdff8ca11 | -9.44484 | -51.61036 | 2026-08-21 05:42:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 46708108-a07c-39f9-9fc0-005822de2782 | -11.20046 | -54.00678 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0f75a358-2d0e-39bf-9f9e-4a8bbd024588 | -11.1759 | -54.0084 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| caac9ee1-cee5-3194-b445-d005fc65a97e | -6.87069 | -59.44053 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 0f599eb2-8baa-3763-a5b4-1f3c98d5c531 | -7.7474 | -61.08759 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd89cef8-ffe4-33c6-b93c-70ea9ec1884e | -9.41414 | -60.43822 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| d958e87b-2c81-3960-8791-430aea92ab70 | -6.90124 | -58.99543 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 99c12663-dcd9-3b7d-b5ce-eb660e01b862 | -6.38447 | -54.95696 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5e32acb8-aded-375c-bf6d-dc9a08499f5b | -6.5812 | -58.96719 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 685efc24-3acd-3dd1-85c3-46144600e683 | -5.81536 | -55.72386 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e94e39b-387c-347a-b0d7-dd453f011f2b | -6.43897 | -54.94894 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5e78ec12-95a4-300f-851a-7c8ce363eb2f | -6.57317 | -58.96597 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c35072dd-27bd-3c7f-9a4e-cbd4e0936810 | -7.06455 | -59.96598 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 56d32083-e442-35f0-89a3-7c70b6be209b | -11.20102 | -54.00226 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8d6fdef0-c446-3baa-a04a-2e18f391d696 | -7.05149 | -59.84416 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 21008665-f35c-39a2-bae9-0e26f4e4915c | -10.38593 | -61.20456 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| de84bef8-4b7c-38b1-a014-933ee8054aad | -7.33758 | -55.68618 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8059f9db-59d6-380f-b696-4dcde0bebf57 | -6.16617 | -55.44699 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b302e87-3534-3980-80a1-b3cf215b313c | -9.40271 | -60.4365 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a0f1150a-8a11-3aad-a3b2-ffae82ba18e1 | -6.65901 | -56.34835 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 84057cfa-d7ff-3a9e-b26d-27ab0ee8fed1 | -6.11447 | -59.9049 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ed383a09-63d7-3f96-a828-27262634b190 | -6.89175 | -59.43343 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| afc85b45-3b9b-32f8-9f72-7aa8da11a376 | -9.05406 | -60.44037 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e6d7615e-b64f-3bea-a6d9-7fe76d9fb1c7 | -10.92152 | -57.17622 | 2026-08-21 05:42:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41d9a7af-1fa3-3d9c-a10c-1fa54a048d44 | -9.41319 | -60.54578 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| e7694bee-c7e1-3bd7-b2c7-1cac7eab79c6 | -6.86681 | -59.41203 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 35b574d4-aa33-3e58-b744-a2eaa6a85e02 | -8.3944 | -62.69783 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| f462436f-ee36-32b3-a48b-f8cc135234f4 | -10.24693 | -54.36779 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 49008b04-ab09-31bd-a2f6-5a6cf929693c | -6.86693 | -59.43752 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1452a937-d3d6-39a7-82e9-324ff844e3a8 | -7.5751 | -60.86651 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 136595b4-edb5-3826-a2e1-fcf69dcae8e8 | -6.57212 | -58.97296 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5b455007-8d0c-3716-8a22-1c3bae538356 | -6.23056 | -55.39624 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3aea9698-fee4-3378-ae90-304f4e241ef5 | -9.54875 | -56.79758 | 2026-08-21 05:42:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3422bbec-d9cb-308e-9e40-c0c4aa978f4f | -7.86372 | -63.74882 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7fccd792-1424-3aae-9e33-0046f1a01c58 | -11.16827 | -54.02122 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| f17caf0b-9f43-3b83-8e23-76ef50e8f2ab | -9.06685 | -60.43266 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 50110fe2-07fc-3106-848e-200ad7902833 | -6.22836 | -55.62074 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 48.5 |
| 330c7c26-be5f-3ce7-8c8e-427e866f8649 | -9.54238 | -63.56583 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b0644ce8-dbf7-3477-9689-872de2b5c56e | -6.66303 | -56.35736 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 926b28da-d070-39e1-8876-7e6313fe2911 | -6.85835 | -59.44133 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 848edc9c-4ce8-3930-a45d-fd6a57d37194 | -6.57674 | -55.44326 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 19a96448-9193-371e-8b93-85e64ef27d4a | -6.80428 | -59.42819 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bd987a6b-5f8d-3027-87c8-abbadd84bcdf | -6.86276 | -59.03294 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8814b228-c05f-3e38-a447-1f5238f247fe | -11.1868 | -54.01893 | 2026-08-21 05:42:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 128689f5-f0e6-3a75-8bd3-cdd5ccfb7251 | -6.91609 | -59.34993 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b2df8c8d-b2f3-3186-a182-846ad8238af8 | -9.11529 | -60.33586 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 50132a3f-dea0-3445-8d7f-94dff08bf671 | -8.58011 | -54.78863 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6b2ebc99-2d74-3e3c-8952-35e3615c380a | -10.24131 | -54.36401 | 2026-08-21 05:42:00 | NOAA-20 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| d67ff2c2-ed5b-3620-b225-53a7a6ee8d0c | -6.86224 | -59.03647 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd6360ad-df8f-3436-a0d2-0d7776a213d7 | -8.28746 | -62.8975 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bed95037-373f-34c8-a0b7-31f75fc3240e | -9.22067 | -59.76728 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 56a8cfb4-f154-3699-8492-7b26b965fbdf | -7.77988 | -61.16458 | 2026-08-21 05:42:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 4b0446d5-8091-3139-8790-ea6d89192f2b | -8.58104 | -54.78146 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5741d241-6787-3971-94c6-7411dbeafbbd | -6.87461 | -59.44109 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f1e3713c-3a15-3593-8d0e-5f0ae317ce28 | -9.21565 | -59.65986 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 94c09d68-747b-34a9-bf8c-dadaf65bdb25 | -6.57946 | -55.44518 | 2026-08-21 05:42:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9636d5ee-fcec-3771-a328-ec84e16bfef6 | -9.08233 | -59.48326 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 527a660c-618c-333f-bdc5-7fe9cdec3069 | -6.88709 | -59.43788 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 4ff3f836-7888-3775-8988-f6a37f581bd1 | -6.58155 | -58.99219 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e07406dd-bc48-3022-98f2-d36a7550c244 | -6.6983 | -58.93417 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 84626ef7-d01a-3eea-852d-fc4786658395 | -6.23014 | -55.39914 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 79e7c759-451f-3c2a-a2c4-9d161709e705 | -6.79963 | -59.43261 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d4f32883-ec2e-39b5-a5ea-4a49689d2f6b | -6.8276 | -59.40616 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca63cee2-dbe6-3daf-acb0-d16e5b1554ef | -6.86997 | -59.4176 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| cefe0a0a-7b19-30a4-a397-84afc9ecdc4b | -6.79498 | -59.43698 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41ba0ac6-4cb3-3a6c-ba17-7d1412a0efc9 | -7.8643 | -63.76677 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9dc58ebc-436d-3585-b893-d2eaf4203bba | -8.40629 | -62.68841 | 2026-08-21 05:42:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c22cbb98-47d4-3662-a6ca-fbd70a32e865 | -6.22283 | -55.48577 | 2026-08-21 05:42:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8e7c30dc-52cb-3635-aa73-66a6a0286502 | -6.89772 | -58.99135 | 2026-08-21 05:42:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 02dc787d-7552-3b90-ae16-262d48133b43 | -6.09025 | -57.91645 | 2026-08-21 05:42:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a3dc3b8b-5492-3b1e-b577-3a25b421d597 | -10.8209 | -50.99288 | 2026-08-21 05:42:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 072c5359-8201-3119-812a-554951fc86aa | -9.401 | -60.42175 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8f26f2ba-918a-37de-9586-654e263f7924 | -8.58608 | -54.78582 | 2026-08-21 05:42:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6012298d-922f-3df4-88a3-5d76fbcbcd07 | -10.38356 | -61.21128 | 2026-08-21 05:42:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c4c5b916-3c82-34db-9b7b-024d590473b3 | -8.25996 | -63.99353 | 2026-08-21 05:42:00 | NOAA-20 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9f3eb807-a533-3117-b554-014f2ac33dea | -8.89179 | -60.5462 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| e12e0667-eb69-3a5d-a8d6-f3989225a35a | -9.38836 | -60.55881 | 2026-08-21 05:42:00 | NOAA-20 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 408f9a81-877e-306d-91bb-fdbf23ddea31 | -9.07134 | -60.42858 | 2026-08-21 05:42:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |


[Clique aqui para ver as próximas entradas](README79.md)
