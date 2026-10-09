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

## Dados Diários - Página 72

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fb88f79e-a1f5-319d-ad06-a0bc23ef9129 | -8.7234 | -45.1355 | 2026-10-09 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.5 |
| 65f4118e-02ac-3231-a7d0-d5007ae27350 | -3.1787 | -50.5807 | 2026-10-09 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 46.9 |
| fbc10a01-bf69-345b-acb0-b940925f377e | -9.297 | -47.4313 | 2026-10-09 04:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 123.1 |
| 39fc943b-8e91-3033-a596-09f0eeafbe63 | -12.2158 | -57.0887 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 333.0 |
| e87567fd-cc42-3fca-84f4-a403d5cdd6ea | -12.2156 | -57.1087 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 134.7 |
| 45c73e23-265a-3ebe-a8f2-cb415b37a441 | -6.0021 | -40.9594 | 2026-10-09 04:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 169.5 |
| a129cecf-2836-3e62-a965-b2daa1df063e | -7.3909 | -44.7445 | 2026-10-09 04:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 58.3 |
| 314d513c-a5e5-381f-b573-1110013cbab7 | -18.3335 | -42.3598 | 2026-10-09 04:20:00 | GOES-19 | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 71.1 |
| 35014534-0239-3874-9580-ca3d53272b61 | -3.5493 | -54.6752 | 2026-10-09 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| 6d59f482-bdbb-31e4-9909-258a46df2dd1 | -12.2161 | -57.0687 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 113.8 |
| 9ee4f643-3c63-3885-88e8-930900fc165c | -4.7404 | -55.672 | 2026-10-09 04:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| cdc7fcd5-77b4-3682-8e07-66755caf480e | -3.0926 | -53.9254 | 2026-10-09 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| b79c8868-95e1-350c-bd55-be17f11a8f43 | -3.3455 | -50.4078 | 2026-10-09 04:20:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.9 |
| cb9bb7e7-a580-32f5-9708-0a72df032181 | -8.7423 | -45.1334 | 2026-10-09 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 74.1 |
| 5732a2c0-647c-383f-98e1-dce84dbcbcaf | -3.0925 | -53.9455 | 2026-10-09 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 60.8 |
| 28e51e39-403d-3e87-a309-53c9a39c8220 | -3.1101 | -54.1661 | 2026-10-09 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 88.2 |
| 463c2d8c-f9b7-3703-929c-e128ba2af8aa | -3.1285 | -54.1657 | 2026-10-09 04:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 59.2 |
| f95299bb-90bc-3eac-bff0-cd5d895031d7 | -2.7429 | -54.0945 | 2026-10-09 04:20:00 | GOES-19 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 57398b64-5ac1-3c79-be83-ed579016e5ca | -3.5676 | -54.6946 | 2026-10-09 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 57.7 |
| 58b11cb5-ccb3-3fc3-aab0-8967a669800b | -2.499 | -56.0675 | 2026-10-09 04:20:00 | GOES-19 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| af1353a8-0764-3200-88fc-5fb30bf18d47 | -11.3107 | -44.8105 | 2026-10-09 04:20:00 | GOES-19 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 52.4 |
| 7b3aec81-f700-3028-8554-e036dbbe2485 | -6.021 | -40.9577 | 2026-10-09 04:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 156.1 |
| a95e0714-0566-3f8c-8039-e3785f8aa245 | -3.5677 | -54.6746 | 2026-10-09 04:20:00 | GOES-19 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 699a6322-04d1-3a44-a74b-60e1ad8707de | -9.2973 | -47.4092 | 2026-10-09 04:20:00 | GOES-19 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 110.0 |
| cc586d1d-7a9c-3a8b-9de9-e4db6132c3f5 | -13.1639 | -54.3385 | 2026-10-09 04:20:00 | GOES-19 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 61.8 |
| 1c238991-064c-3c78-9b7a-a563b52a0d0e | -6.0024 | -40.935 | 2026-10-09 04:20:00 | GOES-19 | ASSUNÇÃO DO PIAUÍ | PIAUÍ | Brasil | 2201051 | 22 | 33 | nan | nan | nan | Caatinga | 87.8 |
| e9f0ce37-29ee-3e44-a1e8-064ee0a037e8 | -12.2348 | -57.0871 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 437.3 |
| 2b135c7e-d5fe-3313-8945-26255fc348ef | -12.2346 | -57.1071 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 153.3 |
| 0821a482-a828-3c0f-89f5-1134592831c0 | -8.9687 | -45.1542 | 2026-10-09 04:20:00 | GOES-19 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 63.8 |
| 889b8282-d60d-35ac-b006-af9ebfe7f7ba | -2.8047 | -58.2841 | 2026-10-09 04:20:00 | GOES-19 | SILVES | AMAZONAS | Brasil | 1304005 | 13 | 33 | nan | nan | nan | Amazônia | 77.9 |
| 1b56e4bf-83e0-3719-b510-7b186ee61722 | -3.0007 | -53.9075 | 2026-10-09 04:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 56.0 |
| 3183b607-ba9e-30a1-b8b1-e457e03b14e8 | -12.235 | -57.0671 | 2026-10-09 04:20:00 | GOES-19 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 141.9 |
| 95a7b9ed-2a59-3fef-accb-0303bfd778b2 | 2.41851 | -50.81723 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e3f84126-6f10-3020-aaa4-3373b2dbdc58 | 3.51046 | -51.25117 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f0c1113a-c99a-3e9e-8219-24893fa95efe | 3.557 | -51.27854 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1b2cc9d9-4864-31fb-a700-e8384d0765f0 | 3.55165 | -51.27443 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 89075881-eeb9-3b88-a661-d32c8e6b29d1 | 2.41438 | -50.82192 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 80040512-8167-3e2d-b22a-e37d1f09891e | 2.4157 | -50.83042 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 261dd3d5-a75b-38b9-ab27-41a31d06513d | 2.41944 | -50.82554 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7f89c783-d4f3-3860-8a8a-7aaf1f05878c | 3.52889 | -51.2485 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0304c91a-51a9-3dca-a161-08e076e7f6b3 | 3.55617 | -51.2764 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| dbf985ae-c137-3c6f-8118-7ab02573506e | 3.73027 | -51.64462 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a10e6af5-cf29-35f0-bb6f-0449350bc0a9 | 3.55686 | -51.28119 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 44f70db6-b6de-3fda-a22b-767eda8f84ee | 3.55238 | -51.2792 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 8bd306ba-99b1-3afd-9190-1aac4a8c2a2b | 2.41474 | -50.82216 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4b01f941-96cb-3240-85a3-e54cecc31532 | 2.41914 | -50.82151 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| e29c4f78-7f33-3596-b458-b471da9c20b0 | 2.41537 | -50.82642 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 9f0b434b-4935-3fca-b901-71900c1643e3 | 3.55627 | -51.27377 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d08d63f-53b6-38f9-bd11-c04e4a4cc4f9 | 2.4229 | -50.81658 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 062b9c95-e150-3328-bba7-3d2394f7956b | 3.51896 | -51.24509 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 5136724c-20bb-342b-815f-b56fa0d92bd3 | 3.52428 | -51.24917 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 08e80966-6813-32c1-885f-3fb72e3f8956 | 3.73105 | -51.64971 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c783face-3d0d-39ca-8a26-e4598d6e78c5 | 2.41811 | -50.817 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 7ea384bd-8d4e-3523-a115-eb49d05629c8 | 2.41504 | -50.82617 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 13.4 |
| f4bf1657-f64f-36be-95e5-f8cbf9311665 | 2.42317 | -50.82063 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| f58acf0b-55e8-389a-961c-1865ed70ef48 | 2.416 | -50.83068 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 49899e98-9573-38cd-b688-e7dcac8a4f6a | 3.52961 | -51.25326 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f3436fa9-155b-3868-aaaf-682ec1a9d919 | 3.55772 | -51.28332 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e901ce1c-241d-38ab-9a88-ccfc42410027 | 3.51967 | -51.24984 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| c23a99d5-57aa-3bbd-b3c6-9a245b81fdff | 3.85849 | -51.77881 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8b6137bd-e06d-358e-aa1b-c3c66d5132a7 | 2.42251 | -50.81635 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| ca84e5fb-bd60-3f62-8a1a-5b5cd6dc5b0e | 2.41878 | -50.82127 | 2026-10-09 04:23:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 8.2 |
| d3913167-0554-363a-873c-9557459a2796 | 3.51967 | -51.24983 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 67347fff-d2b8-3ee1-94da-9352a93034fb | 3.55627 | -51.27376 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 216e856b-a63b-374e-b6f0-2b2e79cf73e2 | 3.55165 | -51.27442 | 2026-10-09 04:23:00 | NOAA-21 | OIAPOQUE | AMAPÁ | Brasil | 1600501 | 16 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 250b2952-d343-316e-8d34-d3f1fdde56eb | -6.75149 | -46.89315 | 2026-10-09 04:25:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8f96accd-0392-33a5-a19e-47d72ec73e87 | -6.06563 | -44.10584 | 2026-10-09 04:25:00 | NOAA-21 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0e3ccba3-b49c-30ae-9c88-2a8143544f94 | -2.56877 | -56.18053 | 2026-10-09 04:25:00 | NOAA-21 | JURUTI | PARÁ | Brasil | 1503903 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| afe961b6-58dd-315c-bc82-d314997b97f2 | -2.74407 | -54.13129 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 65aa8eff-b873-3c1c-8c48-993831a75a8c | -3.08831 | -53.9445 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f626462a-9fe5-3468-b84c-3bb0b99001f4 | -2.89206 | -54.16344 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 6cb40ce4-80a4-3c8b-b1fc-676d8b457394 | -3.01074 | -54.06926 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 29bdeb00-0a61-3597-80c2-ed6b9a734c0d | -2.86951 | -40.01068 | 2026-10-09 04:25:00 | NOAA-21 | ACARAÚ | CEARÁ | Brasil | 2300200 | 23 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 1b2a8285-0125-3b46-af39-a0841aff8a75 | -2.89293 | -54.16872 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| bbbd3eca-1a20-3509-9d2f-c923b315330b | -5.5988 | -50.05329 | 2026-10-09 04:25:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 087ea74e-a2cf-3df1-be47-7d7da6a410a2 | 0.50521 | -50.78186 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 5bd36656-f61c-3fbb-849e-fa9eb582fcfc | -5.70435 | -53.46476 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 2ecb3f7e-6a6c-31b4-9490-afa28d29d93c | -3.17182 | -50.45076 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bc3ad470-7a67-3b62-a7a4-d8839b2c7817 | -5.07571 | -44.73463 | 2026-10-09 04:25:00 | NOAA-21 | JOSELÂNDIA | MARANHÃO | Brasil | 2105609 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 3ab57068-2728-3bcc-897c-cc05a24870e6 | -3.58468 | -54.66411 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a228a2f6-1457-34f5-b8a5-9feedae8fcb2 | -3.55362 | -54.6855 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 4bad556c-1368-3254-b2ad-caa53b38b6c5 | -4.45363 | -47.92317 | 2026-10-09 04:25:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 21627ccc-e3ea-351a-a93b-093a79703985 | -5.1077 | -46.22017 | 2026-10-09 04:25:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 4.3 |
| ddaaef24-759a-3482-a582-7ae3fa123f66 | -2.99162 | -53.84516 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| fa5aa87b-fff9-3cd5-b7bd-e44aef471ede | -3.92665 | -56.02382 | 2026-10-09 04:25:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 9d2b38bb-cb04-317d-9e31-6e3f77894526 | 1.1599 | -52.73434 | 2026-10-09 04:25:00 | NOAA-21 | PEDRA BRANCA DO AMAPARI | AMAPÁ | Brasil | 1600154 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 27335f8a-c657-3d84-a429-226873a17f80 | -3.5752 | -54.68839 | 2026-10-09 04:25:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 4be1f418-eecb-36d6-a592-4c92894357bf | -2.98492 | -54.07441 | 2026-10-09 04:25:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3167fe4a-8a88-357c-892a-14331d0948bb | -1.15046 | -54.21691 | 2026-10-09 04:25:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f522a52e-89ca-3b5b-93db-5b6513b2ec80 | -6.67845 | -46.94902 | 2026-10-09 04:25:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6e0a3c93-e7b8-321e-9b4d-60d39efda60e | -3.1758 | -50.44855 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ee9973f8-c5fb-3e24-8d93-2908eb41f5c2 | -2.08411 | -46.577 | 2026-10-09 04:25:00 | NOAA-21 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 39eb28c3-ea49-3d93-baec-f4527b82096b | -5.6959 | -53.46538 | 2026-10-09 04:25:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 0f6b2e71-baab-3f08-a252-dbef140adcf9 | -3.27409 | -54.06588 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 931be675-7c8b-39a1-b723-7a136566361d | -3.26961 | -50.39129 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 25dd2d0d-e1aa-343e-a0dc-6653af41a951 | -3.09381 | -53.94227 | 2026-10-09 04:25:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f98c8bc1-74f3-3c05-9bd1-5d86011dea45 | -2.3408 | -48.86427 | 2026-10-09 04:25:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a554432c-deb9-31da-a902-5c65e6fa22d5 | -3.10456 | -54.27826 | 2026-10-09 04:25:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 4fba62c5-0f2f-39e9-9a1f-01ca66132474 | -3.35558 | -50.40791 | 2026-10-09 04:25:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 3f3ff358-3b53-3d79-8951-29ba10bce979 | 0.50947 | -50.78119 | 2026-10-09 04:25:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 4.7 |


[Clique aqui para ver as próximas entradas](README73.md)
