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

## Dados Diários - Página 149

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 584352cf-dfba-3dd2-af59-7d452325e9cf | -10.6513 | -50.6484 | 2026-09-21 16:00:00 | GOES-19 | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 65.3 |
| f230f71d-66f4-3719-a387-afe34a3680c3 | -8.58 | -44.5552 | 2026-09-21 16:00:00 | GOES-19 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 190.0 |
| ed3c30e7-b638-3ebe-b9c3-1900cae6b6ca | -6.2948 | -47.6274 | 2026-09-21 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 105.2 |
| cb1f5761-c23c-3257-bc93-4636222868de | -6.1653 | -47.5052 | 2026-09-21 16:00:00 | GOES-19 | TOCANTINÓPOLIS | TOCANTINS | Brasil | 1721208 | 17 | 33 | nan | nan | nan | Cerrado | 107.3 |
| 8b60200d-fb59-31ec-946d-59062a31eb1c | -11.0048 | -49.7325 | 2026-09-21 16:00:00 | GOES-19 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 101.6 |
| 363d4c4a-b2f1-3b37-bef3-3876563611c7 | -3.6076 | -59.0769 | 2026-09-21 16:00:00 | GOES-19 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 43.4 |
| 404cd046-ef62-3b38-a17c-68738ce6f58c | -6.3012 | -59.9962 | 2026-09-21 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 59.7 |
| 38be1395-335c-3319-8048-9084c0e0ed30 | -10.2982 | -50.2158 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 102.9 |
| 6019fd63-84df-3d09-b999-9d16a8775f34 | -10.9361 | -50.5759 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 82.8 |
| 6fa7808b-f83a-3126-a85d-589a6b945779 | -3.1698 | -58.5859 | 2026-09-21 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 124.0 |
| d21482ae-4b98-3218-89bb-01de183a01bd | -8.0894 | -55.331 | 2026-09-21 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 135.8 |
| b5912a00-5519-3b9b-87eb-9069b14ff8bd | -6.4302 | -59.9724 | 2026-09-21 16:00:00 | GOES-19 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 79.2 |
| 6420994b-b142-31ad-800f-a80a9edacbb9 | -10.6881 | -50.7297 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.4 |
| bfd0f78a-e90f-3370-a933-b74a92fd643c | -6.8263 | -55.5421 | 2026-09-21 16:00:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 138.3 |
| ec7f42d7-7f57-3ccb-b064-80b0d226d1f6 | -10.6568 | -50.2426 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 95.5 |
| 1094f3ea-9ca9-3031-b869-bbb0d54fd262 | 1.2608 | -50.9552 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 82.7 |
| b4baade4-306e-3906-a39c-527cffc90bd1 | -6.7666 | -59.1129 | 2026-09-21 16:00:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.2 |
| 21daa212-87cd-3bdf-bfcf-298919849d0d | -1.0243 | -48.83 | 2026-09-21 16:00:00 | GOES-19 | CACHOEIRA DO ARARI | PARÁ | Brasil | 1502004 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 9c5a95a7-46d7-3f9b-8d08-a6a3784609e4 | -3.4461 | -58.0199 | 2026-09-21 16:00:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 65044864-f761-3da6-896c-6ce207230b59 | 1.2424 | -50.9346 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 71.9 |
| 1d5bf3d4-8124-3312-a930-1ef66dfa96f3 | -10.3919 | -50.2702 | 2026-09-21 16:00:00 | GOES-19 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 98.3 |
| f369605b-dda9-3176-8776-8f1d591c0d12 | -10.6944 | -50.26 | 2026-09-21 16:00:00 | GOES-19 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 77.8 |
| 132f97d7-45b2-3df0-bcbd-1cc86ec94c1e | -6.392 | -45.1948 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 105.5 |
| 5bc5486a-7554-386d-ad4e-f25af97b99c7 | -10.7064 | -50.7703 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 328.7 |
| 86a5f05f-bc07-387c-971a-24bc822174dd | -6.5449 | -44.8871 | 2026-09-21 16:00:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 109.5 |
| 72920e07-c4b6-3037-b11c-654993472c52 | 1.2423 | -51.0178 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 76.5 |
| ffad87cc-0932-3f86-a4a7-4daceb52f7da | -2.9525 | -57.7394 | 2026-09-21 16:00:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 00da6550-184a-3982-bd50-2be8b8a873b6 | -1.2082 | -49.2539 | 2026-09-21 16:00:00 | GOES-19 | MUANÁ | PARÁ | Brasil | 1504901 | 15 | 33 | nan | nan | nan | Amazônia | 64.9 |
| abe441db-e7f2-3ddb-b4d9-44a19f6b6cb5 | -10.6875 | -50.7722 | 2026-09-21 16:00:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 104.9 |
| 15f1986b-7262-3d9f-8dd1-30eba50fe170 | 1.2239 | -51.018 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.8 |
| 326fd172-d6ac-35e2-9caa-418db5de6c8f | 1.1319 | -50.9982 | 2026-09-21 16:00:00 | GOES-19 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 86.4 |
| df9234f6-c74f-3925-85d8-51374b3ed6b4 | -8.7706 | -45.8567 | 2026-09-21 16:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 152.8 |
| 1ee267fd-8854-3855-a4f9-28ccafb97135 | -3.1514 | -58.644 | 2026-09-21 16:00:00 | GOES-19 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 1b95d2e5-fd71-3a4a-a863-c7465e34fe35 | -9.2939 | -60.6345 | 2026-09-21 16:00:00 | GOES-19 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 53.8 |
| 92709e7f-4963-3d88-8597-5465a93e4d64 | -9.11101 | -44.70314 | 2026-09-21 16:01:00 | NOAA-21 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| f17f63d8-9b6f-3b1d-bfdb-14a6751bd65b | -12.29999 | -50.71399 | 2026-09-21 16:01:00 | NOAA-21 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| 6d5ecb28-8858-3c3e-ae87-ff0809c9e337 | -10.43067 | -40.18313 | 2026-09-21 16:01:00 | NOAA-21 | SENHOR DO BONFIM | BAHIA | Brasil | 2930105 | 29 | 33 | nan | nan | nan | Caatinga | 4.3 |
| 6a69d1eb-5a7c-3e39-b906-aaf7bed8942a | -13.42783 | -46.32927 | 2026-09-21 16:01:00 | NOAA-21 | SÃO DOMINGOS | GOIÁS | Brasil | 5219803 | 52 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 4cfb190b-3966-3a56-831a-037fd874a649 | -11.79605 | -49.84013 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f69a3abf-c25e-3f17-855a-2986c8d6b6d0 | -9.89285 | -48.40801 | 2026-09-21 16:01:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 2321f2ca-2313-355d-99ce-a49bbecae514 | -10.16605 | -45.55298 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 11.1 |
| 84a36512-6dfb-37ee-8edd-b90f25668339 | -9.38865 | -48.28777 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 43f0f53d-f4ef-3072-b1f0-daea0d1d5060 | -10.39028 | -48.90127 | 2026-09-21 16:01:00 | NOAA-21 | PUGMIL | TOCANTINS | Brasil | 1718451 | 17 | 33 | nan | nan | nan | Cerrado | 17.3 |
| cc526a41-0657-3922-a657-b3b9a778a0bc | -9.90637 | -45.83022 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 7.9 |
| b96debf7-725a-36e4-a09a-4a56829a85ba | -10.00926 | -45.21207 | 2026-09-21 16:01:00 | NOAA-21 | SÃO GONÇALO DO GURGUÉIA | PIAUÍ | Brasil | 2209757 | 22 | 33 | nan | nan | nan | Cerrado | 25.2 |
| 30a7c0f0-5e36-3893-9136-c3146630acb4 | -10.1154 | -45.82956 | 2026-09-21 16:01:00 | NOAA-21 | BARREIRAS DO PIAUÍ | PIAUÍ | Brasil | 2201309 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| f457a320-0c6b-33eb-a69c-e879aa9a02c7 | -11.08496 | -49.74934 | 2026-09-21 16:01:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 39.9 |
| adc7d868-7387-30c4-9da1-ed514d29103f | -10.40681 | -50.33337 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 13.9 |
| 56699167-6f4f-3038-bac9-93a7020cc67c | -11.67201 | -43.43413 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 15.7 |
| 72381987-4c73-3766-87c1-0c3415f65ab3 | -11.67248 | -43.41189 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 23.1 |
| 8ce4c40c-ac10-3faa-ae38-6cb4e8f3cec6 | -11.05552 | -46.57512 | 2026-09-21 16:01:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 21.9 |
| 0e16ff03-440e-39ec-aa27-a081f149dc25 | -11.81819 | -50.03385 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 2a1a90b2-c534-30e2-a3d0-da203b5e6404 | -11.66491 | -43.4487 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 906e5e48-b9ec-3c31-9a47-fcca7dd20e1a | -11.8707 | -46.85351 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 38bbc8c5-5f74-37b0-ba0a-8e52fa5496e0 | -8.76014 | -44.2867 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 16.0 |
| 6a7399c9-c794-3ca1-8723-ff8d7a841923 | -8.78609 | -44.27393 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 216.9 |
| 24e72795-deef-3204-b410-76fb174b83cf | -9.44757 | -45.41668 | 2026-09-21 16:01:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 48.4 |
| 82ff595b-46eb-33ab-942f-d9ebcce7804b | -13.2291 | -46.93026 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 9.6 |
| 57348450-5116-365f-9be1-d3e9775ada5b | -11.4205 | -47.32234 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 19.1 |
| 3c912bc1-82db-30ff-a6ae-4b2f8b65cac1 | -11.09921 | -48.31201 | 2026-09-21 16:01:00 | NOAA-21 | SILVANÓPOLIS | TOCANTINS | Brasil | 1720655 | 17 | 33 | nan | nan | nan | Cerrado | 10.3 |
| be80a733-eb54-329c-9bf2-25d2912e79ee | -8.94834 | -49.05765 | 2026-09-21 16:01:00 | NOAA-21 | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 370e35db-b537-3bfd-ba0d-9f85e46f6000 | -9.9771 | -50.26104 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 3d9fc1bc-6a75-3f1d-b140-a5d77bc6c90e | -12.43198 | -47.02681 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.4 |
| f42b4be9-9d38-36a9-bfb7-9f58b8c3229d | -9.57738 | -46.54562 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 7ac0cd69-1e96-3e03-8a8a-7d8952924f18 | -12.06092 | -50.06845 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.3 |
| 1c573a2b-87fc-3dab-af55-f507621d1f36 | -11.67535 | -43.43419 | 2026-09-21 16:01:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 14.0 |
| e20e2a95-234f-33b1-ba4f-c17eb4c04484 | -9.24884 | -46.24857 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 65ab0c00-509e-3650-a93c-bcce814eadfc | -12.42717 | -47.0356 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 44191e54-3df4-3536-b358-6fc429506184 | -11.66186 | -47.77645 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| f8100a04-aa18-3cf3-a994-f48db1ebd967 | -13.9027 | -48.56817 | 2026-09-21 16:01:00 | NOAA-21 | CAMPINAÇU | GOIÁS | Brasil | 5204656 | 52 | 33 | nan | nan | nan | Cerrado | 12.0 |
| d20c6d9d-b8bc-314a-9006-e4b56286c8b2 | -8.77539 | -44.30766 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 23d54f44-f370-36cf-b0ac-ee36a2a223e2 | -11.87624 | -49.98582 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| e342f0b5-d517-3f50-b8b4-3e5763278156 | -11.46011 | -47.65948 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 9c09cd11-0f00-3126-853d-e8a66d863f57 | -12.80502 | -44.23022 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| b4834011-b1c2-314e-997b-b0a6be0901df | -10.20163 | -44.15244 | 2026-09-21 16:01:00 | NOAA-21 | CURIMATÁ | PIAUÍ | Brasil | 2203206 | 22 | 33 | nan | nan | nan | Cerrado | 16.2 |
| c071000f-c108-3e0c-bdc6-ca6bc6926ebc | -10.07346 | -50.24088 | 2026-09-21 16:01:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 52.7 |
| 8fcc26b3-fd0f-3019-9904-a1340ec70372 | -11.82433 | -50.02684 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| bd184f8a-6703-3400-985e-1e06589bb806 | -12.42374 | -47.02111 | 2026-09-21 16:01:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 0b14cc7f-474d-3c3f-ab2e-55863a8bf570 | -12.04002 | -50.07279 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 6f9a9cd5-f5e2-394d-835b-6246b2c33043 | -8.88989 | -37.06711 | 2026-09-21 16:01:00 | NOAA-21 | BUÍQUE | PERNAMBUCO | Brasil | 2602803 | 26 | 33 | nan | nan | nan | Caatinga | 8.0 |
| 62d00821-8bea-3686-952f-462ebc158364 | -13.47696 | -46.93146 | 2026-09-21 16:01:00 | NOAA-21 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 8b869b05-0836-3e00-86bb-dd6d781ab146 | -8.14992 | -37.65028 | 2026-09-21 16:01:00 | NOAA-21 | CUSTÓDIA | PERNAMBUCO | Brasil | 2605103 | 26 | 33 | nan | nan | nan | Caatinga | 6.6 |
| 0e58d4f9-5348-3025-b3a0-a1a49276328d | -12.42166 | -40.9704 | 2026-09-21 16:01:00 | NOAA-21 | LAJEDINHO | BAHIA | Brasil | 2919009 | 29 | 33 | nan | nan | nan | Caatinga | 4.8 |
| f782c329-fc12-364d-8a97-105e010d149b | -11.14412 | -42.79359 | 2026-09-21 16:01:00 | NOAA-21 | GENTIO DO OURO | BAHIA | Brasil | 2911303 | 29 | 33 | nan | nan | nan | Caatinga | 10.7 |
| ccab82ed-83a7-3c41-965b-6f61ee52cf98 | -12.80024 | -44.23081 | 2026-09-21 16:01:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 81.0 |
| aadcecfb-0bda-349d-a387-b629106e69cc | -10.72513 | -50.78012 | 2026-09-21 16:01:00 | NOAA-21 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 98.3 |
| ec183cb0-f54c-3403-b904-ab9df5ae9270 | -11.47611 | -47.74492 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| b39372a3-de85-3ad6-860e-0307219edda8 | -9.2388 | -46.17451 | 2026-09-21 16:01:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 93ccadf9-45db-34ae-b1bc-23facba793ce | -11.45551 | -47.66005 | 2026-09-21 16:01:00 | NOAA-21 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 5c2ff285-238b-3e65-a3e7-1481456a6602 | -11.8524 | -46.84405 | 2026-09-21 16:01:00 | NOAA-21 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| e8873b36-5e4f-30a5-837b-f1f90e38d0f2 | -11.93136 | -49.80402 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 6039525d-6b89-352c-aa76-a1d75c4edc68 | -8.75891 | -44.27743 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 390a8764-1bc0-34f3-8b7b-626eff6822ff | -9.3684 | -35.84811 | 2026-09-21 16:01:00 | NOAA-21 | MESSIAS | ALAGOAS | Brasil | 2705200 | 27 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| 35fbf961-3d88-3f93-b269-0e2838013454 | -8.76949 | -44.2986 | 2026-09-21 16:01:00 | NOAA-21 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 58.9 |
| afd505ac-f7ef-305f-afb8-a82294f1c8c1 | -9.39987 | -48.32752 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c9d1eda8-45eb-3cbd-b7d5-b6fa2440481c | -12.26674 | -50.15556 | 2026-09-21 16:01:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 24.8 |
| 0f0610be-1299-385b-a6ca-e79d13a845de | -9.40643 | -48.3311 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| eadca3b7-08dc-36f5-a6ba-62a6d578f32e | -9.38614 | -48.31548 | 2026-09-21 16:01:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 14.2 |
| c54565ec-fbf8-3192-aaa0-44ce960e8a95 | -11.4194 | -47.32294 | 2026-09-21 16:01:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 11.8 |
| bc86a63d-f073-3985-9cef-9aa047356f3d | -11.71339 | -42.76168 | 2026-09-21 16:01:00 | NOAA-21 | MORPARÁ | BAHIA | Brasil | 2921609 | 29 | 33 | nan | nan | nan | Caatinga | 5.3 |


[Clique aqui para ver as próximas entradas](README150.md)
