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

## Dados Diários - Página 21

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 8f920365-7234-34f6-92de-71220dd4bf62 | -14.3146 | -51.9183 | 2026-08-21 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 106.2 |
| 1e94e889-dcba-3bf0-b270-0bce014e25e8 | -6.2155 | -55.6316 | 2026-08-21 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 64.0 |
| e6539d81-1b15-3f7f-a8a3-dd6532cb1a67 | -5.598 | -43.9978 | 2026-08-21 03:40:00 | GOES-19 | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 81.4 |
| dc3abeef-68a1-3a9b-9c87-c27d260e1512 | -6.8388 | -59.3993 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 66.9 |
| 5bca3341-ec33-3148-9818-c2255380536e | -7.3415 | -45.8152 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 54.5 |
| ac655d84-6b3c-305c-8566-97b3a87be0da | -6.2341 | -55.6109 | 2026-08-21 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 73.8 |
| 1cc7e510-23da-3ea3-8653-33e990ae2c78 | -6.8203 | -59.4001 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 121.4 |
| eee8ace9-a5e2-38d1-ba07-eebbdb3eadfb | -11.175 | -54.001 | 2026-08-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 332f815f-4e6b-347b-a300-262e6b7653af | -14.3343 | -51.8944 | 2026-08-21 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 91.9 |
| 4795c3c3-1905-343c-97e7-bcd656e0c8e9 | -6.2156 | -55.6118 | 2026-08-21 03:40:00 | GOES-19 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 84.8 |
| 1aa4a6b7-36fc-30df-8ea2-270bd160afc0 | -6.8939 | -59.4356 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 57.8 |
| 90145fb2-7c12-334c-bfb0-7de1ddaf26d2 | -14.3149 | -51.8969 | 2026-08-21 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 283.1 |
| 511bf6b9-1738-30f7-b324-8f8d41ac1d9f | -7.3603 | -45.8136 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 262.0 |
| 85bd6e54-fe1b-3f98-810b-ad3d9eca43ba | -6.6938 | -58.942 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 60.4 |
| fbd2af03-3599-37ea-8b56-ddc1f088fd89 | -7.3791 | -45.8119 | 2026-08-21 03:40:00 | GOES-19 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 134.4 |
| 9e84cf3c-fe2d-3536-8b03-cc92d84c5118 | -3.5407 | -48.1673 | 2026-08-21 03:40:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 55.4 |
| 6af1e731-16e9-36f6-9af5-7d81c0fced47 | -8.3903 | -62.6963 | 2026-08-21 03:40:00 | GOES-19 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 62.8 |
| 9d35e1f4-4bba-35ac-8d59-d844232403c0 | -14.3339 | -51.9157 | 2026-08-21 03:40:00 | GOES-19 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 54af989e-5a71-31b6-9c5a-ab82c522bc0b | -11.1558 | -54.0233 | 2026-08-21 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 02232789-4a50-3cb3-b3da-197c121da6b3 | -6.8756 | -59.4171 | 2026-08-21 03:40:00 | GOES-19 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 64.0 |
| cc50e56f-3b6c-3683-96d5-1d63cda976e2 | -4.46348 | -38.51022 | 2026-08-21 03:40:00 | NPP-375D | OCARA | CEARÁ | Brasil | 2309458 | 23 | 33 | nan | nan | nan | Caatinga | 0.9 |
| d55bce54-048a-35d0-a314-ab0ede24ff63 | -5.60488 | -44.00347 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 31.4 |
| 3d69a9ae-8350-3efb-89e5-49c0a2a71c57 | -5.38162 | -36.82215 | 2026-08-21 03:40:00 | NPP-375D | ALTO DO RODRIGUES | RIO GRANDE DO NORTE | Brasil | 2400703 | 24 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 28e892e4-9def-320e-bd39-b17861b3c62e | -5.60392 | -44.00813 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 3a60deb4-db46-39eb-ae55-af24bcffaf59 | -4.09798 | -42.5006 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| 359d8a49-9f31-3b40-b146-83b29f4e3a50 | -4.71625 | -42.7732 | 2026-08-21 03:40:00 | NPP-375D | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 7443604f-a7e3-3dc5-8c1a-b778e148b6ed | -5.59752 | -44.00681 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 17.2 |
| 37aa4070-8ce3-37e4-b058-41128f99d952 | -4.0912 | -42.50401 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59f92e58-59d7-3a7c-b063-bb091f7a6da5 | -5.60485 | -44.0029 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 5ecfe678-2f43-3420-aef6-0a8473523481 | -4.09643 | -42.50949 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| b423c67b-1cc2-3057-b421-95bf0cd50e84 | -4.0972 | -42.50506 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 5.5 |
| a618a214-0de4-336a-abd3-42b29e341ba2 | -5.61039 | -44.00905 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 23.0 |
| 42326285-659a-3401-a2f7-68934c1f1362 | -5.26036 | -36.69525 | 2026-08-21 03:40:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| cc46f347-c745-3602-93de-f807a35c4ec5 | -5.59847 | -44.00222 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 10.1 |
| 0d7493ad-e32e-37df-b26d-16d5bcb77105 | -5.61039 | -44.00959 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| 9f8483e8-f822-332a-a7cd-f5a5c52b6b3d | -5.60392 | -44.00867 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 34.8 |
| e8714e9c-f59c-3c68-b6d8-024b7c96c266 | -4.09043 | -42.50843 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 742293b3-1e3f-3efb-a26c-3fad7e722836 | -4.09875 | -42.49613 | 2026-08-21 03:40:00 | NPP-375D | BARRAS | PIAUÍ | Brasil | 2201200 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| dcd017d8-7df5-3967-95a1-2b06027f79b0 | -5.59752 | -44.00738 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 20.9 |
| 48c4880b-5e7e-3f0e-967e-e4aca36bfb7c | -5.603 | -44.0133 | 2026-08-21 03:40:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 35.0 |
| 39540e34-e12a-34f0-9101-a774efa214d3 | -5.26176 | -36.6973 | 2026-08-21 03:40:00 | NPP-375D | PENDÊNCIAS | RIO GRANDE DO NORTE | Brasil | 2409902 | 24 | 33 | nan | nan | nan | Caatinga | 1.0 |
| d45c92a9-f0af-3c78-9d34-49386f3c235d | -12.26996 | -43.16037 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| c9e79f3b-a8f4-3d5b-a7c9-b2d0a57d64bb | -7.77719 | -46.03885 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 19e61610-e126-3dbd-9aad-4b15893d4eaa | -7.36644 | -45.81116 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 622febad-f4de-3183-bbf9-620ae4b75f4f | -7.37906 | -45.8205 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 79cbf59d-b1f6-3a74-9f30-2a116f22670a | -12.25693 | -43.1692 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| a8b16651-01fa-38f9-bf43-96471ccbe706 | -12.25549 | -43.17662 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| c3aebc6b-0de8-37cc-98e8-2c4805597039 | -6.86904 | -43.73417 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 5f6f77f0-24ea-38a7-9b3a-d086698f51e3 | -12.26299 | -43.16714 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 383a9980-691b-3182-a5fd-e7f069a3673a | -7.45773 | -46.1571 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9f236e07-22e8-3c60-9a4b-5bab5d604a56 | -12.25007 | -43.17533 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 3415daba-c17b-34d5-a0d5-a8ce4d76dd71 | -12.23046 | -43.15983 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| fd8baacd-bf8d-3921-9d62-8a7155ca48b1 | -11.48511 | -45.1108 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 44e61992-88ae-30c2-a999-38ec2cf3d190 | -12.25621 | -43.17291 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| c2777d6a-46ea-3998-a348-883a646611da | -11.63316 | -46.55172 | 2026-08-21 03:42:00 | NPP-375D | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| d5d7d9ce-7777-3f5b-9ab6-c814d5887577 | -6.3441 | -44.08413 | 2026-08-21 03:42:00 | NPP-375D | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 065d880c-99cb-3555-9439-7b5e37649450 | -12.25083 | -43.17147 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 6b390479-b7fa-349b-8009-8e55393f235d | -11.48304 | -45.08933 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de6db07e-bf9c-356b-a822-af29a6dfedcb | -11.49476 | -45.10771 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| b898e20e-59b9-38c8-9e8d-6b9600aabd2e | -6.86726 | -43.74382 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| e6ee889b-8646-380e-9937-4b3e5e647015 | -7.73193 | -46.16126 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 9b1052df-e62d-3c15-b102-6dd3eccba76d | -7.36222 | -45.82298 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| f22bf9e5-3dae-314e-a8e6-2c47f76a8cf7 | -7.36393 | -45.82432 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.7 |
| 839f946f-4d90-329c-83b0-9123fe44b063 | -7.37605 | -45.82595 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 0de0b43f-85e8-3bf9-b322-faaf44cb6586 | -10.73127 | -44.78357 | 2026-08-21 03:42:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c80d8b49-4272-3fe2-b697-a21ad85f7c69 | -11.48743 | -45.11205 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| bcb1950e-3a08-33d9-9913-32693e74d7b6 | -7.36912 | -45.82454 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| 0dbb8ad7-a131-3832-915a-d33904f3ab02 | -9.01454 | -40.99667 | 2026-08-21 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 692dc6ee-92f0-364d-ac64-929f63d0e826 | -6.87879 | -43.75081 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 69e01de6-83bb-3fd2-8784-85707159226b | -7.35132 | -45.81491 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 16.7 |
| df3ba143-ca02-3c92-8520-dc9076b3844c | -6.47733 | -43.53925 | 2026-08-21 03:42:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 04e3f1f7-89ee-31ec-9e3d-467585b4b49f | -11.49139 | -45.11182 | 2026-08-21 03:42:00 | NPP-375D | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6c353f0a-ace4-3c0a-8ced-7ab8c3f1c8e9 | -7.37083 | -45.82595 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 14.0 |
| 25380f02-7e27-3afc-8566-78ef4bccde14 | -7.78172 | -46.03874 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4556c6d-53c2-3628-a459-2dba34d4c2aa | -7.63005 | -45.76344 | 2026-08-21 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e3959da8-5de6-31ca-abdb-31fa7626d1bc | -12.26223 | -43.17107 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 10.1 |
| 8003f2f4-eeb4-35cd-9b6c-156f0df0fc27 | -6.34392 | -44.07699 | 2026-08-21 03:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 72c3fbeb-b261-3e55-b71a-675607a9f0ab | -11.3225 | -45.01344 | 2026-08-21 03:42:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 67acc32d-9381-341e-8e35-526bf03e0c38 | -6.86816 | -43.73894 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 020238f0-afb1-3824-b49f-86b87e9264af | -6.34513 | -44.07865 | 2026-08-21 03:42:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 00a2e36a-f33b-30bd-8e4e-7f6043e78977 | -12.26919 | -43.16435 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| b4335df0-e6f8-3fa9-b072-b1d2c42675b0 | -7.6288 | -45.76981 | 2026-08-21 03:42:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42828321-79a4-3762-936b-565aee83f485 | -7.37045 | -45.81782 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.7 |
| ca262be3-43e2-351e-bd27-8d72c2d34e2d | -6.87349 | -43.7448 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| ac2cb3f5-48de-3060-a8cb-021b3b719e9f | -6.87437 | -43.74002 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 1a44e7ed-62c9-3596-9c3f-249956a0f6d5 | -6.87258 | -43.7497 | 2026-08-21 03:42:00 | NPP-375D | GUADALUPE | PIAUÍ | Brasil | 2204501 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 021772f3-683c-3933-a991-85ceb36d0dda | -7.37739 | -45.81916 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| d18c2e24-acac-3a16-8c15-4ff16d40dc4a | -7.35826 | -45.8163 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| a5832678-5dff-3843-89f3-76330fc8ffd6 | -8.1609 | -46.73238 | 2026-08-21 03:42:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8992d998-5e2a-350f-9874-91ca5747062e | -7.78049 | -46.04496 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 70ceca47-498a-3798-986d-106dfa215d45 | -12.27073 | -43.1564 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e323e461-dcad-32f8-90f6-9d80e667f4e0 | -7.72489 | -46.15988 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| d9ba1ad4-d2b7-385e-abd7-7331abcc95d2 | -7.36479 | -45.80996 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 34.1 |
| 9fb9b843-d66c-3cd9-ac40-c86c3a24ff5b | -9.00954 | -40.99572 | 2026-08-21 03:42:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 92be35c9-8aee-34c4-a61b-cc748d7fbeb1 | -7.35949 | -45.80983 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 49.2 |
| 58f83aaa-b71e-3115-a95e-cb6dcbe61412 | -7.37212 | -45.81912 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 6d68ad73-e65c-305a-8669-959413f95cff | -12.22579 | -43.15482 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 76c9f0e4-572d-328f-9f1b-04283a0143ab | -12.26459 | -43.15891 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 1.4 |
| b87e368f-d489-380b-b518-fcf39041635c | -12.26377 | -43.16311 | 2026-08-21 03:42:00 | NPP-375D | IBOTIRAMA | BAHIA | Brasil | 2913200 | 29 | 33 | nan | nan | nan | Caatinga | 4.5 |
| 6a25ac93-086d-3db6-8e36-f7edee054d1c | -7.78305 | -46.04613 | 2026-08-21 03:42:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |


[Clique aqui para ver as próximas entradas](README22.md)
