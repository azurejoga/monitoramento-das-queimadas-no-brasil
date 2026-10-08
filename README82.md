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

## Dados Diários - Página 82

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dd5fc7d4-9fc7-367e-bc9a-e1a498383a34 | -4.30109 | -50.78835 | 2026-10-08 04:46:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b5823137-0cd4-3fd1-a3aa-24b1e9984bf0 | -5.99044 | -40.9431 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 5bfe2f3a-ce24-38c0-bae0-e0dac06677f8 | -3.30407 | -53.87477 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 961f5f36-7acc-3cac-99ab-f1a730a97b07 | -3.22365 | -53.88828 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 59aac8f9-32f6-3b3e-a660-77af050db55d | -2.98906 | -54.76378 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| eab1d418-9f6c-36d9-a2d2-cb365b0e108c | -3.10697 | -53.76836 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 79e47293-5993-31b0-8898-1ce0dab3781b | -3.54141 | -54.63878 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f7de9c50-26be-3289-b904-341f9c5cf2c8 | -5.96412 | -40.9225 | 2026-10-08 04:46:00 | NOAA-21 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| b99623c7-5779-3e52-817c-5211dc98de10 | -8.71337 | -62.41589 | 2026-10-08 04:46:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a32eb451-b4f3-3f9b-ab95-ca499255f9b0 | -3.29969 | -54.02138 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 7df61a24-e9cc-325b-ae87-6bacbf58dbef | -4.29203 | -49.08691 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 23e962cc-5b6c-30e4-8d6f-6c9e3a0c1f95 | -9.39937 | -49.00846 | 2026-10-08 04:46:00 | NOAA-21 | DOIS IRMÃOS DO TOCANTINS | TOCANTINS | Brasil | 1707207 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9ea0ac22-b990-34c4-b8a6-d678bee65cc8 | -3.22661 | -53.89307 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee7d9267-6fa3-3b84-b871-1c225a7c03ee | -3.65319 | -54.06374 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 01fcd2c0-2bf2-3cd4-ad13-b90438491879 | -3.52484 | -54.32757 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7ffd0669-2b04-36e8-ba08-65747f1a5ec0 | -9.36874 | -45.93898 | 2026-10-08 04:46:00 | NOAA-21 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| dd38ddf3-2f0c-3222-819e-1f387d658239 | -4.08369 | -48.95834 | 2026-10-08 04:46:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0187193e-77ac-396b-9c0a-737fb64d8ef3 | -6.99657 | -59.10681 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a185b047-6aea-36e8-a6d7-bc9205baf3a4 | -10.24801 | -49.67705 | 2026-10-08 04:46:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4d32f9c7-6821-3f04-a2f5-9b73000590af | -2.94047 | -55.78975 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b3b208c-d492-31d1-b504-652ae836f1ca | -5.48474 | -42.8479 | 2026-10-08 04:46:00 | NOAA-21 | NAZÁRIA | PIAUÍ | Brasil | 2206720 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| f1dde364-df82-305f-920c-cf29e804b506 | -3.27524 | -54.05866 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| c90e3810-1942-3352-b0e9-17ef99138c9b | -7.00328 | -59.12083 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 02ca0397-cb88-30d4-b10b-d1a1774b6eb7 | -3.05538 | -54.20929 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 04c282ec-e228-3d75-b149-2da77e011b35 | -3.11805 | -54.17392 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.5 |
| 36da560b-8471-326b-b7f4-8c159b46d373 | -11.71633 | -43.65577 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 33930fec-6851-3306-9de9-02aae007905d | -3.02374 | -53.89417 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8ed96b7a-aa1a-3921-abd8-50aeceb5fabf | -3.03095 | -54.08546 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 00812159-9283-325d-8918-f20aa171db3f | -3.47247 | -50.08184 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3939b3c9-0ab5-30b3-bbda-668f0c779be9 | -4.91738 | -55.85934 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6242a45d-993a-30bf-bfd3-02ead30fe120 | -4.92883 | -55.86467 | 2026-10-08 04:46:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 5a313102-4ec3-364b-b562-5d6f1f617585 | -3.29919 | -54.04772 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 6144f8b4-f903-3f7d-b5bd-ac4843e529bb | -3.02335 | -54.06191 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 4ab5f27c-c98e-3df4-a01f-dd075735cf52 | -6.98993 | -59.11673 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5bdfd8eb-51bc-317e-a860-5abda7a5b8bd | -2.98598 | -54.08295 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 9.0 |
| e53fa2e3-b5c4-3b49-afc4-51019c8a9bf5 | -3.10911 | -53.78473 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 509930c3-0ba6-3e78-8b70-d5ed318ee1d5 | -3.86643 | -50.41445 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 93ce28d0-69fb-3b41-98e2-0c65daa9fe87 | -3.36461 | -58.19991 | 2026-10-08 04:46:00 | NOAA-21 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dfeea3b9-b2da-3f27-98e0-8daed6d28862 | -8.9873 | -45.91574 | 2026-10-08 04:46:00 | NOAA-21 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ed344c9d-5115-35af-bdc5-039e6ff3119b | -7.21738 | -55.15993 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 1be45f69-a7fd-3a00-9e5b-ee71170d7d8d | -7.87241 | -54.96371 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82702074-1a16-3f1e-90ed-0d328ccd9d88 | -6.99084 | -59.11138 | 2026-10-08 04:46:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d9cb9c4e-66bd-3f9c-be4a-cc4b18be3831 | -3.07722 | -53.95814 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 156e3b22-73a7-3411-aa19-65f58cc84d6a | -2.99177 | -54.07042 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 10.5 |
| 8f15f963-83be-308a-9cd7-22c5f8600390 | -2.97854 | -54.17666 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bd16cfc6-4824-33a1-bc12-d7c34f1326e7 | -6.70063 | -45.28223 | 2026-10-08 04:46:00 | NOAA-21 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e5441303-d5aa-34b0-ba7f-06084565a70b | -3.51935 | -59.32439 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6c2fb1c3-cd52-3bf6-85d0-212e2c93fcce | -3.00115 | -54.13018 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 04bcd2a4-d1a4-3fab-8ae1-0480b79c236e | -3.61013 | -50.20169 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 18820073-d9a1-3243-894c-b3dc690329ef | -5.7077 | -53.49398 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 8.7 |
| f92b5bdb-def2-3b17-9b63-eb8885787634 | -5.67466 | -46.35702 | 2026-10-08 04:46:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| b4b99dbb-2cbe-330a-a68b-4a798484c13e | -3.26396 | -54.03476 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| ff77ac52-b91d-3dc8-8bb5-61ef3d0f7a7b | -3.5101 | -59.94893 | 2026-10-08 04:46:00 | NOAA-21 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 88a36d40-4694-300a-ac12-12b11ea278cd | -3.27728 | -54.0457 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea6edc7c-31d7-3f15-9d59-435ec928fb20 | -6.89968 | -55.55959 | 2026-10-08 04:46:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 27672e34-8dfb-37ff-9a11-980b0109b89b | -3.04192 | -54.20887 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 421e95e5-3b77-3cd4-b41e-4d460e0b2d35 | -2.57465 | -56.173 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 9ca70b73-a89d-399e-a794-7a73a5facb38 | -4.37051 | -54.74982 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b89c8da-46b2-3158-bae0-34a97f6c1720 | -2.57904 | -56.14555 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cd194403-ead9-391d-8d55-1d43b55395f7 | -3.01705 | -54.24601 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8e2833dd-eaa1-3331-8820-aecc8f396af7 | -3.51206 | -54.62686 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| aa388769-d409-3719-a3ea-63ea2d4b4d7c | -5.95769 | -55.35629 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| dad83fd4-022e-3d9d-90ef-a305d4f97f28 | -3.97861 | -56.21426 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 03bb8194-6a30-3109-91f1-6990d2a5f97f | -3.32707 | -50.18198 | 2026-10-08 04:46:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6bf20511-72ef-39dd-8b9f-d285483720f3 | -5.69317 | -53.49566 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| fee311f5-ef30-3e44-abc0-485a759e5eee | -2.58312 | -56.17436 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 425a48de-d277-3108-b552-578e8db65ff5 | -3.66339 | -54.28386 | 2026-10-08 04:46:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 50d0bc7f-313d-3ccf-9f1f-dceda79bf13a | -3.4968 | -51.68612 | 2026-10-08 04:46:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 47cf2a56-184f-3b8a-80e0-d7e22b97937f | -2.84057 | -57.48144 | 2026-10-08 04:46:00 | NOAA-21 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 3a50a73a-470d-3228-a16a-56cff07ec8e4 | -11.63332 | -43.69057 | 2026-10-08 04:46:00 | NOAA-21 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 67f9f0ef-bc6d-34cc-8c1e-ee42a5e57389 | -3.28679 | -54.05457 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 5acbc590-cd80-3427-89d2-6161da5da0ca | -10.44147 | -47.27281 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 889088dd-d128-36be-ad72-5a2600bd8d7a | -7.8717 | -54.96798 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19eec96a-7322-391a-9ef5-815704b22fa6 | -9.84044 | -47.47648 | 2026-10-08 04:46:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 02053872-05bb-3272-ab6f-c4eec2d6430f | -3.48174 | -55.43204 | 2026-10-08 04:46:00 | NOAA-21 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| ceaced30-01d5-3b94-a30a-25946b17622a | -3.05445 | -53.96037 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 1ae1002d-00a3-35d0-9e6e-166a8d77f3f3 | -2.50197 | -56.16568 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 6a08f745-21c1-3b0f-b369-6b75fc9a4ed5 | -3.08202 | -54.30473 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5c2e60f3-bbab-3518-9f8e-2e4020af853b | -3.35604 | -50.47809 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4fa05cb1-5190-39e2-be0f-10d453825947 | -2.49802 | -56.16469 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 6de6f511-3108-3395-a03d-40827dea9c0d | -2.57104 | -56.1684 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| da0e9b0a-121b-3736-91f2-c40f957fb334 | -3.3095 | -54.05371 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a54aabc8-55b2-3f39-821c-644d6a706c2e | -3.29011 | -54.01101 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 30d88afb-a89a-3ba3-b378-3ea9247e85da | -2.77227 | -54.10628 | 2026-10-08 04:46:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 432edb69-e5af-386f-8b86-d35442e15ff4 | -10.43351 | -47.27171 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| ba115ab5-2ea4-38d0-a362-44e036489f67 | -7.19876 | -55.13407 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| ca0fe007-8931-315b-9a0a-3a6e0bc2c8f2 | -3.36923 | -50.48012 | 2026-10-08 04:46:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 83689a02-4884-3e5d-8aa7-54bd2a2a497f | -3.94329 | -56.02107 | 2026-10-08 04:46:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c6f4f08-de27-3484-8797-9ad0e5b27b04 | -8.72198 | -45.19524 | 2026-10-08 04:46:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 30e006b5-1d8d-377d-a499-92a02e2fadd0 | -2.82879 | -54.13314 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a215ac0f-6f7c-321a-a2dd-b102f25347b5 | -9.0924 | -61.13812 | 2026-10-08 04:46:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c434f5c0-8161-3a8e-bd0d-3007ad610db8 | -3.53862 | -59.49655 | 2026-10-08 04:46:00 | NOAA-21 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 79097fdf-7b5c-3c67-9681-4df0d37e0a32 | -3.29612 | -54.68932 | 2026-10-08 04:46:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| bb0fbd69-907f-3857-a6ed-6c62a237f902 | -2.53901 | -56.42356 | 2026-10-08 04:46:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1def6b0d-52c2-3859-b07c-5a5a5d08fcc1 | -3.02403 | -54.05758 | 2026-10-08 04:46:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| f24c6129-9db4-377c-947e-793aa03e68eb | -10.50358 | -47.29239 | 2026-10-08 04:46:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 3d8fa34a-78e9-3f4e-925f-9a319ec77044 | -7.38494 | -46.23624 | 2026-10-08 04:46:00 | NOAA-21 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 1d5cf430-4369-3a6e-b117-1ce6da456d72 | -3.01439 | -53.90583 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| cbe564f5-e836-3995-93de-5de657a91df5 | -3.31684 | -54.05486 | 2026-10-08 04:46:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6d8d2792-1e53-34d6-9da8-482f26295506 | -7.22934 | -55.16979 | 2026-10-08 04:46:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |


[Clique aqui para ver as próximas entradas](README83.md)
