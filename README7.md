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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6852798a-f6e0-3619-8846-ca6bccf80157 | -14.1861 | -47.3844 | 2026-09-14 03:00:00 | GOES-19 | SÃO JOÃO D'ALIANÇA | GOIÁS | Brasil | 5220009 | 52 | 33 | nan | nan | nan | Cerrado | 62.8 |
| a9f8cba8-c686-3ce1-8a34-092d0a0a60c5 | -2.6967 | -57.5501 | 2026-09-14 03:10:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 60.2 |
| 6a8e9b32-88b9-3036-9d3b-759ccb120030 | -6.5837 | -58.8498 | 2026-09-14 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 03863d67-29a9-3b07-9e67-a0f576b69681 | -9.4513 | -50.1282 | 2026-09-14 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 77.5 |
| 96d4c11d-1077-3614-80bd-39e7afe13206 | -2.6125 | -54.7577 | 2026-09-14 03:10:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 54.7 |
| 1798c289-8c58-31ae-91d2-b72d389d03f8 | -9.3943 | -50.1761 | 2026-09-14 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 74.7 |
| 4c26f5b9-382f-3a60-8570-cee2a1f400c1 | -6.5652 | -58.8505 | 2026-09-14 03:10:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 43.9 |
| bcc9589e-5339-3db7-a298-f12f1b5b4085 | -4.115 | -60.6886 | 2026-09-14 03:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 92.8 |
| 8bb58faa-4063-308b-a799-8f66175727d0 | -9.4325 | -50.1299 | 2026-09-14 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 63.1 |
| 6a5c2230-5456-38b5-9b3a-d0d3d8191072 | -4.1333 | -60.6882 | 2026-09-14 03:10:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 85.2 |
| 14d02a00-c49c-3a65-900c-c73a0c563755 | -6.1111 | -57.6645 | 2026-09-14 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 68.1 |
| 6793570b-b13d-335a-b4ce-909f5d560603 | -9.4132 | -50.1744 | 2026-09-14 03:10:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 186.6 |
| 9779076d-efa1-35bd-a432-ef7f187f0cd5 | -6.1109 | -57.684 | 2026-09-14 03:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.1 |
| af99cd36-dc52-3387-9284-957e748092f4 | -10.94866 | -39.266 | 2026-09-14 03:10:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 5f9c17f1-e9f2-32de-8858-2c6f5e0ae948 | -7.40807 | -35.16727 | 2026-09-14 03:10:00 | NOAA-20 | ITAMBÉ | PERNAMBUCO | Brasil | 2607653 | 26 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 8a67a974-f396-3124-b8a0-53fb16073425 | -10.94757 | -39.27144 | 2026-09-14 03:10:00 | NOAA-20 | CANSANÇÃO | BAHIA | Brasil | 2906808 | 29 | 33 | nan | nan | nan | Caatinga | 1.2 |
| e7a8e94b-029c-3d35-af1e-419279ded49a | -17.36473 | -42.63165 | 2026-09-14 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| f84a8d17-fd8d-3848-9b01-08bbed2110f1 | -16.05124 | -40.48244 | 2026-09-14 03:13:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.2 |
| a4d78c63-9152-3877-b4b8-c95cba5cb01a | -15.81383 | -42.37583 | 2026-09-14 03:13:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 2cf55ed2-a43c-36c2-9760-e59d78960659 | -17.36489 | -42.62402 | 2026-09-14 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 1fdac920-0217-3005-a4cf-037ef82028f8 | -17.36788 | -42.61802 | 2026-09-14 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 94194cf9-7e65-3c18-a0c2-6b73617196dd | -17.36652 | -42.61717 | 2026-09-14 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 641a1d51-b2b4-3b78-b2fa-a4fade7a1cba | -15.81769 | -42.37846 | 2026-09-14 03:13:00 | NOAA-20 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| b3787abc-b941-31e2-a9b3-81d48f8a5a3f | -16.04597 | -40.47636 | 2026-09-14 03:13:00 | NOAA-20 | ALMENARA | MINAS GERAIS | Brasil | 3101706 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 8bba1970-ea1b-3865-ab6f-f030689bcb01 | -17.36629 | -42.62487 | 2026-09-14 03:13:00 | NOAA-20 | MINAS NOVAS | MINAS GERAIS | Brasil | 3141801 | 31 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 876f12fc-ceb5-3070-8fe3-a69ba31b29d7 | -2.94 | -50.57 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| eae76672-80ec-327a-8983-b38182e17287 | -10.69 | -54.2 | 2026-09-14 03:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| cccc1bf8-a7c1-3385-a6d2-70935bb1480e | -2.91 | -50.4 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 1f7ce098-16c8-35df-8eab-20b587e708d7 | -2.94 | -50.46 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| a557d511-1ebc-3a92-8b26-215eefd0f8d3 | -2.91 | -50.62 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0a53e73d-2001-311e-8c0b-fa9d469a1e76 | -2.91 | -50.56 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| c55d36e8-078f-3bd7-af64-143eadea6166 | -2.88 | -50.51 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b7c0203c-e3c3-3c4c-9310-9df91d6ce207 | -2.88 | -50.45 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 181b19de-82b2-38d3-9f9c-ac3334caa6a2 | -2.91 | -50.45 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f60a2c83-89f5-3546-a1c1-4e0d39fc878b | -2.91 | -50.35 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 61ee45f3-34bd-3e92-8d5a-44ba632d098f | -2.88 | -50.4 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0b031320-58bd-387d-b88c-ed21397360ee | -10.69 | -54.13 | 2026-09-14 03:15:00 | MSG-03 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 6a306428-8aea-3ab0-acce-01a1adfa20e7 | -2.94 | -50.4 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 92a2bd4b-2ab9-3f9e-9dfb-ac314cfd350b | -2.91 | -50.51 | 2026-09-14 03:15:00 | MSG-03 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b9b64a68-45e8-3bb5-af1b-336efc0a2b24 | -4.115 | -60.6886 | 2026-09-14 03:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 94.2 |
| b480af73-908b-3934-b582-7cb0abdf52e5 | -9.4325 | -50.1299 | 2026-09-14 03:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.6 |
| a4ee4ead-0f11-3e8a-9112-4ad93601b324 | -10.6829 | -54.1475 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 262.9 |
| b36eb1e5-3413-3936-ae6c-af70189105c9 | -9.4132 | -50.1744 | 2026-09-14 03:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 108.3 |
| e7bf6b23-4fbb-33e7-aaf1-d58e768a1177 | -6.1111 | -57.6645 | 2026-09-14 03:20:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 56.5 |
| 38a666da-3e48-39d6-b1fd-7d7fdb6f2b10 | -6.1689 | -47.0877 | 2026-09-14 03:20:00 | GOES-19 | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 65.5 |
| 63af7ede-d292-33b8-82b1-3eb0fef610bc | -6.5837 | -58.8498 | 2026-09-14 03:20:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 64.3 |
| efadc00a-3473-32ae-abc0-ec74eba967fb | -9.4513 | -50.1282 | 2026-09-14 03:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 73.0 |
| 66dd4c7b-1776-38b6-829c-0e9b701c12fb | -5.1255 | -55.955 | 2026-09-14 03:20:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 61.1 |
| 6c13cf90-9c38-3e6b-9b40-9f08bca4f8d7 | -10.6827 | -54.1679 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 189.4 |
| 98389d75-a8a8-3d7a-9980-723c839ef470 | -10.6832 | -54.127 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 63.6 |
| 059c95ec-bae9-30c5-a10d-dec5d93af680 | -10.6643 | -54.1286 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 90.9 |
| 8dabbe75-a9d6-353f-a48c-b0eb1806d29c | -4.1333 | -60.6882 | 2026-09-14 03:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 70.0 |
| cc98db32-49a8-3a9a-b604-576d471ef64d | -10.6638 | -54.1696 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 161.3 |
| d0273cfe-f01e-3d4d-9104-4565f693ed13 | -2.6125 | -54.7577 | 2026-09-14 03:20:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 50.4 |
| 6c0bb323-b543-3e33-94c1-33f67e232c9e | -9.3943 | -50.1761 | 2026-09-14 03:20:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 62.9 |
| 0a2262d1-633e-3716-8dbd-2117b3797c39 | -4.1151 | -60.6696 | 2026-09-14 03:20:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 59.1 |
| f7d7cfa5-6049-351b-9217-96eca7745235 | -10.6641 | -54.1491 | 2026-09-14 03:20:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 300.8 |
| 8d8001f0-1170-3042-ab05-0e5fad24c55c | -2.6125 | -54.7577 | 2026-09-14 03:30:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 44.3 |
| 76e61bfe-be8f-3c72-bcf4-a06f0768441e | -6.1109 | -57.684 | 2026-09-14 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 52.3 |
| a833973f-b48a-3af2-b27d-a603813cd4e8 | -2.9024 | -50.4423 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1288.0 |
| 01139b8b-e7f6-37fd-a63d-d2a1299c5a45 | -2.9025 | -50.4214 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1397.5 |
| 0741107b-cfd3-36af-b4f0-1ec34fa50ad3 | -2.9023 | -50.4633 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |
| d1c6bfa4-bb36-30aa-a806-ea0727d5761d | -4.115 | -60.6886 | 2026-09-14 03:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 77.6 |
| a80c53bb-be5a-36e0-9737-ad2097134f32 | -9.4325 | -50.1299 | 2026-09-14 03:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| 8d9ac7f0-3fbd-36c1-8778-4e7a46539f65 | -4.1333 | -60.6882 | 2026-09-14 03:30:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 63.3 |
| db56350d-ff54-37d6-a09e-b18f2e928848 | -6.1111 | -57.6645 | 2026-09-14 03:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 61.0 |
| 3b199014-e1e9-378a-9813-e14925e3683b | -6.5837 | -58.8498 | 2026-09-14 03:30:00 | GOES-19 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 57.1 |
| dd4acd7c-8ea5-393e-bee2-eb9e1a042f20 | -2.9025 | -50.4004 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 387.9 |
| 496577e9-7520-3f80-98ba-8b1f2428f891 | -2.9208 | -50.4627 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 47.5 |
| 2e85a4c5-bd8f-378b-8447-2357f39ceed1 | -2.6967 | -57.5501 | 2026-09-14 03:30:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 49.2 |
| 36acea6e-55a6-3f80-9b71-b7d8fc01a9cf | -2.9208 | -50.4418 | 2026-09-14 03:30:00 | GOES-19 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 332.0 |
| b6b2407e-cffc-3b04-8276-dcfc8a9fa703 | -2.6967 | -57.5501 | 2026-09-14 03:40:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 61.7 |
| 6bfe4d7f-0f37-32aa-a00d-727dc903aa4f | -2.6125 | -54.7577 | 2026-09-14 03:40:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 49.6 |
| bb7368b2-85b2-36dc-954c-441310df9a0e | -10.6638 | -54.1696 | 2026-09-14 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 167.0 |
| 0486fac1-1e75-390e-94e2-b668351c87f1 | -4.115 | -60.6886 | 2026-09-14 03:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 75.1 |
| cfd3b9f2-30fb-3c74-b504-6351a54a6520 | -4.1333 | -60.6882 | 2026-09-14 03:40:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 81.7 |
| 99de9ca0-265d-3a5b-9b11-c61f9ba0d361 | -10.6827 | -54.1679 | 2026-09-14 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 212.9 |
| 918d8de0-b30f-379b-b5a2-d58cdb170c03 | -5.1255 | -55.955 | 2026-09-14 03:40:00 | GOES-19 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 69.5 |
| f9750aa0-aec7-3299-b6d3-3bbac245ddfe | -6.1109 | -57.684 | 2026-09-14 03:40:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 34b2af88-15f2-38b7-ab00-5d8ebeaf5dda | -10.6829 | -54.1475 | 2026-09-14 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 259.2 |
| 99fbac18-612f-3de2-80c2-5d89374561a7 | -10.6641 | -54.1491 | 2026-09-14 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 307.0 |
| 41163423-a1c4-37ad-bfc8-a11b19b73722 | -10.6643 | -54.1286 | 2026-09-14 03:40:00 | GOES-19 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 97.3 |
| 52cdb687-694e-3339-9087-9426906d3e63 | -4.115 | -60.6886 | 2026-09-14 03:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 72.7 |
| 2029503f-c89e-3009-8e6d-23f0df8577d6 | -2.6125 | -54.7577 | 2026-09-14 03:50:00 | GOES-19 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 58.6 |
| ec3e7f04-a62d-3e22-a448-ec95fd18808b | -6.1111 | -57.6645 | 2026-09-14 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 53.4 |
| 254092fe-8e4d-3f27-9d96-fa85a9bef587 | -6.1109 | -57.684 | 2026-09-14 03:50:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 0d883713-c03b-39cd-805b-75981e8593ab | -2.6967 | -57.5501 | 2026-09-14 03:50:00 | GOES-19 | URUCURITUBA | AMAZONAS | Brasil | 1304401 | 13 | 33 | nan | nan | nan | Amazônia | 85.5 |
| 6d28823c-867e-3d0a-ab3d-55bcbb4f9295 | -9.4513 | -50.1282 | 2026-09-14 03:50:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 67.7 |
| e46e211b-b1c8-34c7-ba1e-88e5ee6d0a6f | -4.1333 | -60.6882 | 2026-09-14 03:50:00 | GOES-19 | CAREIRO | AMAZONAS | Brasil | 1301100 | 13 | 33 | nan | nan | nan | Amazônia | 94.9 |
| d88c8fc4-68c9-3cde-a32b-399e2342d0ca | -2.90133 | -50.44869 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| 6b591851-cc8e-3ac3-93f3-c4cba3775e7d | -2.9291 | -50.44704 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| c562fb85-afe9-3a80-90d2-bbcb04abee8a | -2.90575 | -50.38301 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| a13a92ab-38cb-370b-bf4f-4b657bb192d7 | -2.9361 | -50.40583 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 17d3681e-4589-3282-8470-400d0c679e3b | -2.90741 | -50.41324 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 491.6 |
| e17d2bcc-f46f-32cc-81bd-83b52bdfa2da | -2.89466 | -50.4475 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 18.6 |
| cc0ade63-35fa-344c-aead-32b62824f488 | -2.95424 | -50.40366 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 639750b6-6846-31e2-bd16-d1158d19e09e | -2.91842 | -50.46941 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |
| e8052707-6d62-3ad7-b9aa-85e93ff2aebe | -2.92044 | -50.45756 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 4811e516-f35e-3ece-875f-bfa7e064f5fb | -2.88246 | -50.45923 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d88cb04d-e757-3492-9bfb-698c3113833b | -2.92512 | -50.47047 | 2026-09-14 03:53:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 21.6 |


[Clique aqui para ver as próximas entradas](README8.md)
