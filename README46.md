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

## Dados Diários - Página 46

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3a382212-d77c-35be-b4f0-442ac0596950 | -6.81694 | -59.66824 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 27c507af-d26f-38c1-9281-1ee2f85a68f5 | -4.93398 | -55.77893 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c7a74ed7-f311-3889-8322-81c3ac6e38c3 | -8.95502 | -60.58878 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 8acb49f1-85dd-3163-becd-d5cb808898c4 | -8.62909 | -54.74072 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e893b3e8-dd83-3e72-b6ca-1fe73abc5b9f | -6.69788 | -59.45731 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce39d7b0-644d-3caa-829a-a53f917a5cd1 | -8.526 | -54.83463 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 8e10a7ec-40d6-3d8c-a2da-774fb6f32629 | -9.18163 | -59.44801 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 352f46e2-6f4f-3b83-98fe-3a256da63a93 | -6.10945 | -59.93572 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 18acdfcd-f897-300f-833c-a1c67b9072a1 | -6.89779 | -55.71407 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5f196c5e-d228-30b6-b1e4-6215ec434591 | -6.92226 | -59.43843 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8941de4c-9aa0-3948-8d52-517e645219d3 | -7.4922 | -55.33192 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7cb5a39d-e65e-37df-beb3-b8d12b27760e | -6.79723 | -59.66085 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 6961ea03-2573-36cc-9531-e080b62c5caa | -8.92764 | -60.71966 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 53951b00-5d9e-3146-a326-01396a1df536 | -8.5315 | -54.82126 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5d5cc684-4c04-3f8a-9059-76b498a70c66 | -6.76316 | -58.66636 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fd2cf2af-8970-3d9d-89b0-c51d1bf68129 | -6.13854 | -57.77051 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 95b0db07-6d72-31b0-8aea-5162c7455e66 | -6.97279 | -59.06411 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 92fc6516-702a-35ca-b725-dfe530f196cb | -6.81049 | -59.68161 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 447f6371-bb29-3484-b7b6-8a79ee12e41c | -9.12489 | -60.33672 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 26725a7e-925b-3f3c-a4ad-84d1d30a7b8d | -6.67014 | -58.73582 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 33.5 |
| 3a47cf8a-9e61-36a6-8777-d8983aac42cc | -7.3981 | -45.99091 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 8e8239b0-4d72-3562-9b87-8bb162a5a553 | -9.53745 | -63.56681 | 2026-08-23 05:04:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 36c2a7b5-f09f-315a-8817-744f75b9eb88 | -6.25795 | -55.37875 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 36b91917-210c-37f0-a08e-cef20b5667d0 | -7.48013 | -46.09546 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 6060addc-7071-32dc-a15a-fdc0137c584f | -6.79566 | -62.91668 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2158218b-d388-3f83-bd9a-6819ccb523b8 | -6.66773 | -58.75008 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 27d6c21c-371c-3f4e-b22a-187f471e2cd7 | -7.59861 | -60.94338 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a3473dc7-ab50-341f-ac44-4c1a5dfd28ab | -6.55806 | -55.0965 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a688367-f795-3d81-917a-39cf88563134 | -5.01554 | -47.06584 | 2026-08-23 05:04:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 76f47456-7013-3328-8437-85f4eae799cd | -4.99927 | -56.13823 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 455e8f5a-5a68-3ce1-a340-087ac59dd506 | -8.52929 | -54.81379 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b2d14953-770b-34db-bf05-0826fc1cc258 | -6.76697 | -58.66703 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| ae501649-3f00-312f-ac3f-1d3acdffc89c | -6.84005 | -59.45266 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0ef951c9-f493-394a-ac80-deefe15155b6 | -6.78979 | -59.43336 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ca7b26c1-f59a-3f87-837a-735310d110f2 | -8.09635 | -50.0513 | 2026-08-23 05:04:00 | NOAA-20 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c40095a0-7ff1-3fda-84bf-dd548ab343af | -6.12294 | -57.8434 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 17.0 |
| 224e3986-ab15-3a7e-a0e1-d41a95f7bc25 | -6.90006 | -55.69983 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253dee8e-16fd-38de-87b7-81f7c1c5ce69 | -8.10964 | -51.66105 | 2026-08-23 05:04:00 | NOAA-20 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d2241193-45f4-3138-9e62-6999b787b03a | -5.928 | -53.64728 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 633cf094-02dc-3d1c-b0ea-eae215e01180 | -6.68244 | -58.73302 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 54249877-acd8-3284-b315-0f851cc5e4cc | -8.89355 | -60.5403 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a0e4f812-92c9-3f16-9b06-38530b8efa19 | -6.86738 | -59.44697 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0554619b-2115-3989-9016-22bbb83db8d9 | -6.96276 | -59.05227 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 886ecfa7-e93c-37d3-8515-50815d13ee3e | -6.85617 | -59.41645 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| f47c4ccb-156a-3a67-925f-5f56cb9371c5 | -6.704 | -58.72194 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 28731eb5-2a2d-3f1e-855f-f358d630080e | -6.80045 | -59.59148 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f47e4aae-ec1c-3888-80d0-73bf013c9113 | -7.67998 | -63.33666 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b3e221c-fde0-30d9-a4f0-5503ef45a26d | -12.28488 | -43.16981 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 17e3c47e-d9f2-3e50-af64-59351d65a053 | -12.29215 | -43.16465 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| b396c49f-7cf2-33f4-ac9a-20bc2d4a1d6a | -9.52375 | -51.64075 | 2026-08-23 05:04:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a4dce350-753d-3d95-a8a4-aa7363d63d10 | -5.78311 | -50.19172 | 2026-08-23 05:04:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1a3f3d7-dba5-3617-98a7-06e86b221492 | -8.58387 | -54.79044 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c76504e9-fc4e-3bf7-9322-b57c45ab79e1 | -6.76014 | -58.66103 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1e3066f7-ae5f-3a16-827b-694f543236b7 | -8.98067 | -50.7583 | 2026-08-23 05:04:00 | NOAA-20 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 863cd446-77fd-3229-b00a-e488186406bb | -6.19514 | -55.4338 | 2026-08-23 05:04:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9698a18e-2bc3-36ff-8792-188b4cdd8faa | -6.75773 | -58.67514 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b46dc2f-e009-3a78-8828-880a189616af | -6.11009 | -59.93189 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| db38f512-3db3-3016-9652-5ec52aadb6de | -6.1409 | -59.90933 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 322ba9e7-bc8b-3ad2-a586-4d55e283df47 | -8.55788 | -54.71866 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 4ce3f494-9162-3703-af85-7cd6b233d4db | -6.80355 | -59.42491 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a938a1d7-a876-3162-852e-dcc92407d77c | -8.20021 | -54.98178 | 2026-08-23 05:04:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f2b975a6-a6a7-3688-8e9d-155580122271 | -6.54429 | -58.51661 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3777c8dc-0f6f-3af9-96fd-d3f18335895a | -9.45895 | -56.90898 | 2026-08-23 05:04:00 | NOAA-20 | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1383a19d-b32a-36eb-a5cf-d9f09d7671ef | -11.43301 | -44.53473 | 2026-08-23 05:04:00 | NOAA-20 | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 68ff4f97-4aa8-3899-810f-f4af90696adc | -4.95975 | -56.2748 | 2026-08-23 05:04:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| aa9a77e2-d559-30ff-a876-4f69770753de | -9.17765 | -56.99749 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f0ab180f-bcc0-3124-b0b4-e0eaadfd5857 | -7.77542 | -61.07053 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5d61a345-3a9d-36e8-9716-53cec98c414f | -6.79603 | -59.66806 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 4c890340-4600-3333-bd8d-d934fe846fe4 | -6.78605 | -58.67019 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 292d7614-0dd4-3048-8f1c-72a899fb50ea | -6.67781 | -58.73713 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 30.1 |
| a549c0a6-4119-346c-bce0-7d22890cff40 | -7.50293 | -60.07285 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5691395-e767-3d02-9e25-4a6c6cb337c1 | -6.83493 | -59.95847 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| edaf99f3-7034-3bae-a623-3f1a9e897883 | -6.89949 | -55.7034 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 68edd1d9-706a-3391-84ea-47559f296a7e | -12.24252 | -43.12989 | 2026-08-23 05:04:00 | NOAA-20 | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 9bc10a34-2326-3e27-8ec2-a6a022680f02 | -9.10139 | -60.92186 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a6180f95-c3e4-3fb0-85d1-99c783c7822d | -6.94857 | -59.06513 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ef265ec9-e18f-3ebc-bb25-adbd4c317cbe | -11.16261 | -54.01376 | 2026-08-23 05:04:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 365e7cdb-5a09-3fb7-beef-5d88b8a2d8ec | -6.781 | -59.65805 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8273af7d-6305-3b4d-bab6-b78e1eb8be21 | -6.90171 | -55.71106 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4dc7927f-f7b9-3ac8-bbb2-e33b62dd44c7 | -10.38453 | -50.41114 | 2026-08-23 05:04:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 25.8 |
| 596a3aed-2347-3818-ab1b-9068bd2207fd | -6.12732 | -57.83966 | 2026-08-23 05:04:00 | NOAA-20 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1bf2e7e7-76ea-3e10-9da6-63e1f5361a83 | -7.0139 | -48.01873 | 2026-08-23 05:04:00 | NOAA-20 | WANDERLÂNDIA | TOCANTINS | Brasil | 1722081 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9db019f3-4d50-3bc7-bfa3-81b9af6454c8 | -9.03584 | -60.44315 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9d4158d9-e440-3546-b858-c1331895b135 | -6.78001 | -59.44249 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6255c659-7628-3d05-9418-cc5cb1681fbf | -6.68468 | -58.74317 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 11372ccd-415e-31b4-9ac6-109cb1c2693a | -11.05433 | -49.50999 | 2026-08-23 05:04:00 | NOAA-20 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 80caabaf-2da4-34ba-8575-179bf84b291d | -9.04347 | -60.44818 | 2026-08-23 05:04:00 | NOAA-20 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0849c8d4-d817-3565-b8ae-a3a396a1b4c0 | -6.86593 | -59.40744 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.0 |
| fbe63746-16e3-330b-b16f-03bb91a5d3ae | -6.83905 | -59.95925 | 2026-08-23 05:04:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a8d02a39-0997-3dea-ac1a-4312a30a12a6 | -6.88068 | -59.41718 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 800d6f5f-4688-3de5-ba1f-73fda47038f6 | -9.79482 | -46.60608 | 2026-08-23 05:04:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| a2f49af1-329e-3c51-84d0-6a7bc7700b89 | -6.76376 | -58.68587 | 2026-08-23 05:04:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0316bdbe-c07a-3c8e-acba-e0006987d942 | -6.8099 | -59.6852 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 4e456292-c33e-3074-97f2-65b91909a68d | -6.89557 | -55.70641 | 2026-08-23 05:04:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c3e87b16-344d-3a62-86ba-ce8752caefec | -7.43654 | -59.78076 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 89da3b47-f82b-309e-9cb6-6287c5a88633 | -6.80231 | -62.9087 | 2026-08-23 05:04:00 | NOAA-20 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4cb8cce-c5f2-3d27-b751-520967e0be86 | -6.82444 | -59.67322 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25dc27de-dea4-33b3-b5c1-044b1eb874a4 | -6.95247 | -59.06578 | 2026-08-23 05:04:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 5c7025f5-7dcf-3dee-925c-930a4c8376e0 | -7.62352 | -61.60701 | 2026-08-23 05:04:00 | NOAA-20 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 66d04162-7d97-317f-9098-94851faa49fb | -7.39855 | -45.98782 | 2026-08-23 05:04:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README47.md)
