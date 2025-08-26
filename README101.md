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

## Dados Diários - Página 101

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 11ed7be1-b71d-3298-82f9-d6c09dd54d53 | -21.7717 | -50.0374 | 2025-08-26 07:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 125.8 |
| 15237ce8-ac97-39c6-b2cf-f1bbad1d8d46 | -6.8229 | -58.956 | 2025-08-26 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 77.3 |
| baf1f4c3-05c5-388d-a4b3-118d731803ef | -9.1718 | -59.5211 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.9 |
| 3568ae9d-3919-3f16-ac5d-d6caaba73635 | -9.1903 | -59.5395 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.6 |
| b78d7c39-588d-3c40-be4e-de768468e5e8 | -8.8363 | -62.451 | 2025-08-26 07:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 46.1 |
| 2d4d0765-ba94-3b63-b210-a575d6439758 | -9.153 | -59.5415 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 45.3 |
| d3fe8e97-9f33-3171-a77a-90e056068b79 | -6.2459 | -60.0174 | 2025-08-26 07:10:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 77.2 |
| beb7f33b-7d03-321f-bdc5-d2cb9e1ccaef | -11.1587 | -44.7627 | 2025-08-26 07:10:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 64.8 |
| 9f0a3506-121c-3c37-8f6b-c551f9a1796f | -10.1461 | -48.8747 | 2025-08-26 07:10:00 | GOES-19 | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 59.9 |
| 4576f938-e0f6-367b-97de-3fcbac55f252 | -9.1904 | -59.5201 | 2025-08-26 07:10:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 46.7 |
| e5f05712-c8f1-38a7-8701-33d8685489da | -6.8228 | -58.9753 | 2025-08-26 07:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 93.9 |
| 4391235c-23ca-34bc-a2b9-cd0bb43b2c74 | -21.7924 | -50.0328 | 2025-08-26 07:10:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 97.4 |
| 74dc69a4-aabe-3985-9808-8f1f8c20ccb9 | -11.6277 | -46.3899 | 2025-08-26 07:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 58.9 |
| f7e4508d-5441-3b39-b1e5-3f2e6ab69ba7 | -9.1717 | -59.5405 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.5 |
| ff3c92da-839e-31b2-a9ef-b1e46a280646 | -9.153 | -59.5415 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| 00aee116-799c-30fc-9388-978866c7faca | -9.1722 | -59.4629 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 44.7 |
| 25098eab-ddf3-3ff4-9039-121a087050fa | -9.1718 | -59.5211 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 11367983-f812-3841-a7c7-68a236149a51 | -11.1587 | -44.7627 | 2025-08-26 07:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 69.1 |
| 1bb2fd6e-7507-381c-b9e6-bf3af0336c5c | -6.8413 | -58.9552 | 2025-08-26 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 27.8 |
| d21a27ff-bd06-3445-8c2a-c1d2b676d313 | -6.8228 | -58.9753 | 2025-08-26 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 62.0 |
| eef8dca0-f068-38c7-bd24-9b096faad2e6 | -8.8363 | -62.451 | 2025-08-26 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 45.1 |
| f17f8344-443f-30dd-952f-c9ab10467a73 | -10.1022 | -65.2874 | 2025-08-26 07:20:00 | GOES-19 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 0b636153-43dd-383e-a6c0-af035797915d | -9.1903 | -59.5395 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.0 |
| e20f44c0-9416-391a-b382-fe57931b9d51 | -6.8229 | -58.956 | 2025-08-26 07:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 53.6 |
| fb16cdc2-d8a8-3564-9c0e-037ecedec89d | -8.855 | -62.4313 | 2025-08-26 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 72.0 |
| cc63012f-b984-3370-9cd4-429202b86045 | -8.8364 | -62.4321 | 2025-08-26 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 38.8 |
| a4d57f6e-a185-37d9-9326-eeac91d67936 | -8.8548 | -62.4503 | 2025-08-26 07:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 94.6 |
| 95b36499-934d-3319-8658-2322a2160fc7 | -11.54 | -52.119 | 2025-08-26 07:20:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 46.4 |
| 61baea1d-17ad-3cbd-8ec3-e5ffe3e5a824 | -8.9874 | -65.4192 | 2025-08-26 07:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 35.5 |
| d85f2200-4b99-3c27-9219-1871b00cdef6 | -6.2459 | -60.0174 | 2025-08-26 07:20:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 53.9 |
| 38bfded3-780d-385e-bb66-a159e11fa346 | -9.1904 | -59.5201 | 2025-08-26 07:20:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.2 |
| 0aabead9-1695-3f93-a910-bbd08fe7aa14 | -6.8228 | -58.9753 | 2025-08-26 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 80.1 |
| 373e781d-ddec-3ce0-8d9f-bedc74720fb8 | -9.1903 | -59.5395 | 2025-08-26 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.3 |
| d5a01508-2148-3ee7-9c8c-beb3986322f9 | -21.6122 | -45.0533 | 2025-08-26 07:30:00 | GOES-19 | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 56.4 |
| 722821e0-2e33-3948-bef2-141af4f74b02 | -8.8548 | -62.4503 | 2025-08-26 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.9 |
| 226af9d8-002d-30c3-af66-722172c5b47e | -8.855 | -62.4313 | 2025-08-26 07:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 85.8 |
| fb52720d-6226-33e3-898f-7172c061c893 | -11.54 | -52.119 | 2025-08-26 07:30:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 32.9 |
| f803ec2d-0533-3895-893a-fb8f59940aa1 | -9.1717 | -59.5405 | 2025-08-26 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 531d2cef-de8b-3981-9e0a-cde7ec77a616 | -9.6366 | -59.6313 | 2025-08-26 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 34.3 |
| 706099ec-21cc-3a77-b3eb-32daba200b08 | -6.8229 | -58.956 | 2025-08-26 07:30:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 89.8 |
| 4852a434-20c0-3794-9bf9-fc8dc97eb75d | -9.1718 | -59.5211 | 2025-08-26 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 55.5 |
| 7974e7f2-85de-3d67-862b-d59a5cde292e | -9.1904 | -59.5201 | 2025-08-26 07:30:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 49.6 |
| 6481b4d0-59d2-34a3-9ce4-27318ec4eb49 | -9.1718 | -59.5211 | 2025-08-26 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.6 |
| a9ed18b5-ed28-37e5-b763-7ed42c02487c | -6.8229 | -58.956 | 2025-08-26 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 84.7 |
| a01a4a1a-f4de-3f39-85ef-bc23e0d37f3d | -9.1717 | -59.5405 | 2025-08-26 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 78893619-e7d2-3a0e-98d7-5018a3c64b1f | -8.855 | -62.4313 | 2025-08-26 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 17ea37a9-8dbc-3ec3-a0ed-305fa2cb6992 | -6.8413 | -58.9552 | 2025-08-26 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 42.7 |
| 88b75449-7b9a-33da-950b-960cbe4bb908 | -11.0493 | -52.0015 | 2025-08-26 07:40:00 | GOES-19 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 51.1 |
| ab5256f2-a9d8-3e1a-b895-766c8a070417 | -8.8548 | -62.4503 | 2025-08-26 07:40:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 100.4 |
| 95c6a8e3-75fc-341a-b00d-cd70f8d03dd5 | -21.6122 | -45.0533 | 2025-08-26 07:40:00 | GOES-19 | SÃO BENTO ABADE | MINAS GERAIS | Brasil | 3160801 | 31 | 33 | nan | nan | nan | Mata Atlântica | 55.1 |
| eb76d382-7843-30ee-9b49-3da5572af198 | -9.1904 | -59.5201 | 2025-08-26 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 72c2035e-c37c-3c6b-b3b3-9ec32fdf35fb | -9.1903 | -59.5395 | 2025-08-26 07:40:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 58.4 |
| 69a8af05-5f70-33a4-af41-fd136af3ec4e | -6.8228 | -58.9753 | 2025-08-26 07:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 91.0 |
| f0c3a97d-99bc-326e-b5a7-e791d3a5d93c | -6.8229 | -58.956 | 2025-08-26 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 88.6 |
| 2794f97e-558c-34a2-876a-08b2bc132b7a | -9.1717 | -59.5405 | 2025-08-26 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| cf78ac87-7a9f-354b-b13f-7e5216891ffc | -9.1904 | -59.5201 | 2025-08-26 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 50.5 |
| ade57e78-b203-3502-9e6b-abf5df2a6388 | -8.8548 | -62.4503 | 2025-08-26 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 83.8 |
| 163485dc-d326-32f5-91dd-034aafa28248 | -6.8228 | -58.9753 | 2025-08-26 07:50:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 81.9 |
| 55ea031a-7692-344b-a587-eb0dc274dc59 | -9.1718 | -59.5211 | 2025-08-26 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 9f77627e-67ee-3b28-8432-48efbdfb91fe | -9.1903 | -59.5395 | 2025-08-26 07:50:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.6 |
| 96444664-cd79-387c-9de1-31c86862ea37 | -8.855 | -62.4313 | 2025-08-26 07:50:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 73.9 |
| 8349241a-5914-3112-b6c0-c53b86419b57 | -8.9874 | -65.4192 | 2025-08-26 08:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 37.8 |
| 28c6f447-4651-36d4-86d6-ac9b0366225f | -9.1718 | -59.5211 | 2025-08-26 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 97ad7717-19e3-3553-a2bd-c2e997791a62 | -21.7723 | -50.0144 | 2025-08-26 08:00:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 74.6 |
| 130d3774-d972-3e88-ba29-f893b32fb78f | -6.8229 | -58.956 | 2025-08-26 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.6 |
| c191ab1b-709d-3b25-aa1b-d03bd0960724 | -6.8228 | -58.9753 | 2025-08-26 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 73.7 |
| 2341d65c-3174-3198-a2d3-d47c4a5764bd | -9.1717 | -59.5405 | 2025-08-26 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 60.0 |
| d6c258db-2e5a-34bc-a9a5-70f427a9eb22 | -6.8413 | -58.9552 | 2025-08-26 08:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 41.8 |
| 605f1941-8841-3b22-b679-e9a14d85706a | -21.7717 | -50.0374 | 2025-08-26 08:00:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 105.5 |
| 5f74ef36-6bb3-3f4a-906c-c966ccb1352e | -9.1903 | -59.5395 | 2025-08-26 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 51.6 |
| 3cb03699-2a1d-377b-aec7-adf4e30c4950 | -8.8548 | -62.4503 | 2025-08-26 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 96.2 |
| 977660a9-fcb9-356d-842f-ba8c464e2eb1 | -8.855 | -62.4313 | 2025-08-26 08:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.3 |
| 99552254-16b3-3624-8b56-dd06099d16a2 | -9.1904 | -59.5201 | 2025-08-26 08:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 52.6 |
| 12058a3c-31ca-3b6d-945d-474ee2d60158 | -8.855 | -62.4313 | 2025-08-26 08:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 56.2 |
| 2cf3c06f-7500-3c10-95cc-e190407151e1 | -8.8548 | -62.4503 | 2025-08-26 08:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| 0620f309-3d8b-3f2c-87d3-3ca01b7499bc | -21.722 | -46.8087 | 2025-08-26 08:10:00 | GOES-19 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 87.6 |
| 2fe631be-724a-3903-afac-9d56a4665873 | -21.7428 | -46.8033 | 2025-08-26 08:10:00 | GOES-19 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 75.8 |
| 4f4ea633-cba8-33e6-a945-e5ad14031e8b | -11.6465 | -46.41 | 2025-08-26 08:20:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 66.2 |
| a1f56945-702a-3a87-9046-d05bb0e78c97 | -21.722 | -46.8087 | 2025-08-26 08:20:00 | GOES-19 | SÃO SEBASTIÃO DA GRAMA | SÃO PAULO | Brasil | 3550803 | 35 | 33 | nan | nan | nan | Mata Atlântica | 93.3 |
| 54e0a940-91b3-3c00-ac2c-44f915185c50 | -8.9874 | -65.4192 | 2025-08-26 08:20:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 39.9 |
| d710d4ed-a7b9-3b67-bb77-fa67c69f4208 | -8.855 | -62.4313 | 2025-08-26 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 71.2 |
| 32e228c7-c4e0-32ac-a226-e87c19e34b3c | -8.8548 | -62.4503 | 2025-08-26 08:20:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 87.6 |
| 7a486650-8c6b-360a-bd08-c9a15dc18c94 | -8.8548 | -62.4503 | 2025-08-26 08:30:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 61.4 |
| c43eec12-fda8-38d8-9cf5-60ac4c1266ef | -11.6465 | -46.41 | 2025-08-26 08:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 7660b158-9028-32e2-9627-485494011ebf | -11.6468 | -46.3873 | 2025-08-26 08:30:00 | GOES-19 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 63.4 |
| fa188662-5746-383d-afb7-75ee60bede1e | -8.9874 | -65.4192 | 2025-08-26 08:30:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 40.3 |
| c80a957a-9f5a-33e0-bf13-327cb106933b | -6.8228 | -58.9753 | 2025-08-26 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 51.1 |
| eb17906b-caad-3d1f-9c49-0ede6f062f04 | -6.8229 | -58.956 | 2025-08-26 08:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 44.3 |
| be827b30-c8df-3ab5-9d44-ee0905943800 | -8.9874 | -65.4192 | 2025-08-26 08:40:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 41.0 |
| a8a7b06b-b5c4-3a9a-b57a-bffd0d72f6ff | -21.7717 | -50.0374 | 2025-08-26 08:50:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.0 |
| 8d90225b-2715-37eb-965e-7dd1526f98e0 | -21.7723 | -50.0144 | 2025-08-26 08:50:00 | GOES-19 | GETULINA | SÃO PAULO | Brasil | 3517000 | 35 | 33 | nan | nan | nan | Mata Atlântica | 95.8 |
| 9598368d-50e7-3c70-85fa-9cf3ce49d01c | -8.8548 | -62.4503 | 2025-08-26 09:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.1 |
| ad763c16-59e1-3e43-93f4-c03429037c28 | -6.8229 | -58.956 | 2025-08-26 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 48.2 |
| 4282b182-540c-34c0-b722-2f257c524655 | -6.8228 | -58.9753 | 2025-08-26 09:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.6 |
| 2e462860-3e52-3e89-9553-315a81656247 | -8.9874 | -65.4192 | 2025-08-26 09:00:00 | GOES-19 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 42.1 |
| 38a1dc36-d938-3c8f-a38a-b2023abf23d1 | -8.855 | -62.4313 | 2025-08-26 09:00:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 42.3 |
| 370c2d8c-d7b2-3121-b500-20f493a881f9 | -6.8228 | -58.9753 | 2025-08-26 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 63.7 |
| 19d1cc09-6f22-33eb-855c-65f153461cc1 | -8.8548 | -62.4503 | 2025-08-26 09:10:00 | GOES-19 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 52.2 |
| fc7ba20f-9375-37cb-a039-fdd35a70af86 | -6.8229 | -58.956 | 2025-08-26 09:10:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| e57a1272-4f76-3bf5-b1a4-61c488c562dd | -6.8228 | -58.9753 | 2025-08-26 09:20:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 56.6 |


[Clique aqui para ver as próximas entradas](README102.md)
