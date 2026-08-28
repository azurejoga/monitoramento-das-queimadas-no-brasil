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

## Dados Diários - Página 190

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7f958f40-5bcf-3301-8797-897670e1d512 | -7.2847 | -45.8652 | 2026-08-28 22:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 71.8 |
| 47136025-1568-32f6-910f-5f9ea4c58ee6 | -3.7013 | -39.5792 | 2026-08-28 22:20:00 | GOES-19 | ITAPAJÉ | CEARÁ | Brasil | 2306306 | 23 | 33 | nan | nan | nan | Caatinga | 58.6 |
| 664d3487-e14e-383a-a999-44c47df4c7ee | -12.43 | -43.4182 | 2026-08-28 22:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 189.2 |
| 9e73f466-a459-3848-8cc5-3de5d0ce7de6 | -17.6195 | -51.5995 | 2026-08-28 22:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 60.7 |
| 8efafe6d-96ba-3641-8149-a509d7d92483 | -14.9386 | -56.3216 | 2026-08-28 22:20:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 93.2 |
| f76d9898-ad3e-3d70-bfcf-82598fe359e3 | -6.6317 | -43.73 | 2026-08-28 22:20:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 78.9 |
| 21244f05-2fce-3152-849e-0b5444f96ab5 | -11.1913 | -51.292 | 2026-08-28 22:20:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 73.7 |
| a0a6640d-d6c5-36f2-8a43-c2fa43d3113d | -17.5997 | -51.6028 | 2026-08-28 22:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 106.8 |
| 2ad5b92c-8444-3187-90db-b55518f6d1e0 | -12.7603 | -44.2608 | 2026-08-28 22:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 66.8 |
| 09649455-d95b-3cd9-a065-4d45f7569f20 | -9.1461 | -43.3027 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 150.0 |
| d20ba662-1034-3b91-96bf-7bb6703865bf | -7.5137 | -55.3051 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 410.4 |
| b7425179-d68b-303f-b151-52b0a94ea8a3 | -11.269 | -54.0334 | 2026-08-28 22:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 87.0 |
| f7b57a75-613b-3206-8c72-cdb704057564 | -12.7797 | -44.2576 | 2026-08-28 22:20:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 61.4 |
| 693003dc-f301-328c-a569-37ccc6df57b2 | -11.7165 | -54.5449 | 2026-08-28 22:20:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 69.2 |
| d6d9b961-9f06-3c47-a4f8-1be64f2e8dab | -12.4498 | -43.3911 | 2026-08-28 22:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 44.7 |
| 2facc7fc-08c0-35c8-80f1-9bba1efbd21e | -15.1173 | -53.5687 | 2026-08-28 22:20:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 68.0 |
| dbfff016-0dff-3630-9546-7cb094791007 | -6.7343 | -55.4671 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 457.2 |
| e24a30f0-ed87-3ef1-93cc-3b7220172036 | -6.7528 | -55.4661 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 7f39d8e4-148b-31e0-a16f-eea841334178 | -9.1657 | -43.2532 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 125.2 |
| 04cb07ba-717f-3083-9697-c271f1c31fd4 | -7.2993 | -49.9676 | 2026-08-28 22:20:00 | GOES-19 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 67.4 |
| e8fcfc5e-ed73-3457-8055-5f102cbe28e1 | -19.0146 | -47.4521 | 2026-08-28 22:20:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 77.3 |
| d8732cec-37b0-37bb-a746-b82eb7006421 | -8.5971 | -54.7553 | 2026-08-28 22:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 79.3 |
| 5fc3bc4f-7c2b-3822-b329-7b319637e093 | -8.5966 | -54.8159 | 2026-08-28 22:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 71.5 |
| bab33e6c-bd07-39d4-8cfa-1bf531467739 | -18.995 | -47.4332 | 2026-08-28 22:20:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 68.9 |
| e8ed41c1-36d9-3f25-8e04-19a6e2bb7266 | -5.5964 | -44.1822 | 2026-08-28 22:20:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 78.0 |
| ee0fcac0-5101-396b-957f-61dc7568e013 | -20.941 | -57.5694 | 2026-08-28 22:20:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 109.1 |
| 49d3f872-1838-3c9e-bf16-2669d2a5c2ba | -19.0152 | -47.4288 | 2026-08-28 22:20:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 124.8 |
| 215f17b9-f63a-3544-b404-6d243813af4e | -7.5139 | -55.2851 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 411.2 |
| b529f6a6-d892-301d-8fe6-682877489196 | -9.1467 | -43.2556 | 2026-08-28 22:20:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 67.3 |
| 8cc45d97-1dad-30f2-a783-8543d9b3cd08 | -3.757 | -53.3612 | 2026-08-28 22:20:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 118.3 |
| 97153906-14c7-3889-8057-09f8fa3cdfbe | -14.9015 | -52.6055 | 2026-08-28 22:20:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 67.6 |
| 2b6b94b7-061c-3570-827e-56d69e746fdb | -6.7157 | -55.468 | 2026-08-28 22:20:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 78.2 |
| 6d8b6f06-f1bb-3e4b-86b6-19147c9b4306 | -6.1558 | -53.4843 | 2026-08-28 22:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 30.2 |
| 2df2871b-dc2d-345c-8fc1-163bfd98b5a6 | -17.5794 | -51.628 | 2026-08-28 22:20:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 78.3 |
| 1745e151-ed1a-35a4-b16d-720729e9db35 | -12.4305 | -43.3944 | 2026-08-28 22:20:00 | GOES-19 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 124.2 |
| 372f3435-76b5-3c83-b306-b7ae118c8765 | -5.3453 | -45.1576 | 2026-08-28 22:20:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 74.0 |
| 76db7b24-f9df-3db9-853b-ade52727ae3e | -9.2644 | -45.6444 | 2026-08-28 22:20:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 70.5 |
| b2c61a50-4565-3b9c-b833-d204745996fe | -8.0113 | -48.0161 | 2026-08-28 22:20:00 | GOES-19 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 17054721-4b60-3596-926f-3c77261e308f | -8.5969 | -54.7755 | 2026-08-28 22:20:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 89.0 |
| 46e079eb-2c5a-39e6-a291-595d0f86dfd4 | -11.2693 | -54.0129 | 2026-08-28 22:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 64.9 |
| 4520d225-8cec-37b9-bcee-4e95ef6ad689 | -9.1461 | -43.3027 | 2026-08-28 22:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 75.7 |
| c3912355-2833-345e-a9cc-ce2af2ce4de4 | -14.9166 | -47.7376 | 2026-08-28 22:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 66.9 |
| 3c1f360f-8879-350a-bedc-364e8e16b854 | -11.1726 | -51.2728 | 2026-08-28 22:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 52.9 |
| 4a7aea48-ee02-3476-b2f5-7de0ad360a3a | -6.1657 | -57.7793 | 2026-08-28 22:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 77.8 |
| 76de8ddb-7f62-3f68-b955-3df01873dc7f | -9.1464 | -43.2792 | 2026-08-28 22:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 150.2 |
| 67364de2-87cb-3407-a1c8-6adba34fb4bd | -6.6581 | -53.1924 | 2026-08-28 22:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 54.9 |
| 1d4ec98c-95ee-3263-ae18-5899248862df | -17.5997 | -51.6028 | 2026-08-28 22:30:00 | GOES-19 | RIO VERDE | GOIÁS | Brasil | 5218805 | 52 | 33 | nan | nan | nan | Cerrado | 57.3 |
| e277bf52-855d-3c99-aec8-e871005eb40d | -3.757 | -53.3612 | 2026-08-28 22:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 156.2 |
| d0bdf381-6c24-341b-8a4d-c7e32258dde4 | -9.9708 | -53.9419 | 2026-08-28 22:30:00 | GOES-19 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 73.2 |
| e64ceec0-2bd2-3134-b97a-87e1e51cc5fa | -12.7603 | -44.2608 | 2026-08-28 22:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 35.4 |
| 41ef37ad-a8cd-3457-b7dc-198f21c5aeeb | -14.9193 | -56.3237 | 2026-08-28 22:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 80.4 |
| 980c35f2-96d1-35f1-b16f-1e680da43fa3 | -12.7797 | -44.2576 | 2026-08-28 22:30:00 | GOES-19 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 28.6 |
| 36c9cae8-65ce-377b-a50a-40e707398636 | -8.5971 | -54.7553 | 2026-08-28 22:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 70.5 |
| 3835db52-03bc-302d-aba7-7fbc45818b8f | -9.2644 | -45.6444 | 2026-08-28 22:30:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 78.9 |
| eb04c038-ff79-369c-9c8c-195c4258eaf2 | -14.9011 | -52.6267 | 2026-08-28 22:30:00 | GOES-19 | NOVA XAVANTINA | MATO GROSSO | Brasil | 5106257 | 51 | 33 | nan | nan | nan | Cerrado | 73.9 |
| a0d53739-5217-368c-8fe6-92b503a2967b | -14.6414 | -50.909 | 2026-08-28 22:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 105.6 |
| c2a15509-04d8-341e-ad1b-552f32003a87 | -11.0441 | -57.2421 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 138.8 |
| 8b22df73-36c3-3d28-9771-062442bc3ad3 | -17.6191 | -51.6214 | 2026-08-28 22:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 81.1 |
| 1150b2e8-9b2e-32dc-a9f3-84d64f07ebec | -8.9739 | -50.8078 | 2026-08-28 22:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 80.3 |
| f5156e18-b008-3345-bdc0-39a6a2d671b9 | -14.9386 | -56.3216 | 2026-08-28 22:30:00 | GOES-19 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 100.8 |
| eabeb6f9-5f4d-355a-8ca9-186196061f94 | -6.7343 | -55.4671 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 359.6 |
| 50bb5d2f-e772-305a-a661-304f915c4cce | -6.7341 | -55.487 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 167.1 |
| 6b66b839-9b27-3108-b81b-bc2ce0ba922b | -5.5962 | -44.2052 | 2026-08-28 22:30:00 | GOES-19 | SÃO DOMINGOS DO MARANHÃO | MARANHÃO | Brasil | 2110708 | 21 | 33 | nan | nan | nan | Cerrado | 64.2 |
| 711de750-4ef2-33df-8726-3a82319d5238 | -3.7571 | -53.341 | 2026-08-28 22:30:00 | GOES-19 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 83.1 |
| 79ec6e3c-056f-37f8-9d87-a758a038dbc4 | -7.4952 | -55.3062 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 415.0 |
| af1188bc-7b65-35b5-9b44-91f2930c28c2 | -6.6315 | -43.7533 | 2026-08-28 22:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 77.9 |
| fe30f3e8-0cd1-3b8e-abb6-5030f8c2fbb4 | -7.2849 | -45.8427 | 2026-08-28 22:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 98.5 |
| 754b5413-f4f6-3679-bbdc-759cdd553958 | -11.1913 | -51.292 | 2026-08-28 22:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 106.0 |
| 9de12343-34ed-35a7-9ebc-e03df3a834d7 | -5.3117 | -47.0558 | 2026-08-28 22:30:00 | GOES-19 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Amazônia | 46.8 |
| c633bac3-fd10-3f4d-93a9-32f01a03d569 | -17.5992 | -51.6247 | 2026-08-28 22:30:00 | GOES-19 | JATAÍ | GOIÁS | Brasil | 5211909 | 52 | 33 | nan | nan | nan | Cerrado | 108.4 |
| ff427033-b5d1-3c50-b991-d0277499c671 | -5.4177 | -43.1986 | 2026-08-28 22:30:00 | GOES-19 | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 61.0 |
| 5596352f-70e1-3771-b849-72511852729f | -14.6418 | -50.8873 | 2026-08-28 22:30:00 | GOES-19 | ARUANÃ | GOIÁS | Brasil | 5202502 | 52 | 33 | nan | nan | nan | Cerrado | 67.8 |
| 072befcc-929e-3415-96d7-65a1aa742bd7 | -19.0152 | -47.4288 | 2026-08-28 22:30:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 119.8 |
| 240f3572-bfd8-300e-a299-61b567ee3be1 | -15.1173 | -53.5687 | 2026-08-28 22:30:00 | GOES-19 | NOVO SÃO JOAQUIM | MATO GROSSO | Brasil | 5106281 | 51 | 33 | nan | nan | nan | Cerrado | 59.3 |
| 9b284b87-e7f6-38e4-90bb-5960767f49ea | -9.1651 | -43.3004 | 2026-08-28 22:30:00 | GOES-19 | CARACOL | PIAUÍ | Brasil | 2202505 | 22 | 33 | nan | nan | nan | Caatinga | 130.5 |
| eed007fc-0182-34a5-9b61-7fec4d1ceda5 | -8.5969 | -54.7755 | 2026-08-28 22:30:00 | GOES-19 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 80.4 |
| 6ea4964e-9d4f-355d-9896-21251fc4c113 | -7.5323 | -55.3041 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 91.7 |
| 8fc28659-76a5-3374-a6b8-1729955d2fc6 | -6.6396 | -53.1934 | 2026-08-28 22:30:00 | GOES-19 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 57.5 |
| df4fcfc3-c10b-3372-82ae-f3927e9f002e | -11.0252 | -57.2436 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 152.0 |
| 8c9677e1-60a9-34f8-bbef-b5e68bcf0c21 | -7.4953 | -55.2862 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 363.4 |
| 8ab765c4-6034-31ec-990c-d0354f8c1cf6 | -19.0146 | -47.4521 | 2026-08-28 22:30:00 | GOES-19 | IRAÍ DE MINAS | MINAS GERAIS | Brasil | 3131604 | 31 | 33 | nan | nan | nan | Cerrado | 76.1 |
| d7551875-419a-3004-b182-4b0731ddf509 | -11.0256 | -57.2038 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 77.8 |
| f0c15057-2875-3ff4-ae90-1ff8b606f717 | -15.6836 | -42.4766 | 2026-08-28 22:30:00 | GOES-19 | RIO PARDO DE MINAS | MINAS GERAIS | Brasil | 3155603 | 31 | 33 | nan | nan | nan | Cerrado | 78.2 |
| 24d57f58-f7b0-3b85-b475-9ba6f3c06eea | -6.0004 | -57.6884 | 2026-08-28 22:30:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 64.6 |
| dc9dc4d1-9597-3b4b-9369-0ca18153ca10 | -6.6129 | -43.7317 | 2026-08-28 22:30:00 | GOES-19 | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 64.6 |
| b7fd0ac0-47ca-387c-a24a-d58350921880 | -2.7304 | -47.0424 | 2026-08-28 22:30:00 | GOES-19 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 59.5 |
| 923071bd-e375-3886-b883-cfb0766561e6 | -5.3453 | -45.1576 | 2026-08-28 22:30:00 | GOES-19 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 65.2 |
| 5d515095-143e-3147-b640-80783f4e5ec3 | -14.2027 | -52.8432 | 2026-08-28 22:30:00 | GOES-19 | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 75.5 |
| 7d5fc7d0-23c4-3f53-8d90-464810d3035a | -11.0254 | -57.2237 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 159.7 |
| 5915b734-9405-34c3-b9d8-8a01850b48f0 | -20.941 | -57.5694 | 2026-08-28 22:30:00 | GOES-19 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Pantanal | 109.6 |
| ce0485ab-fd47-3b3c-a8c9-258888a26f1e | -11.0443 | -57.2222 | 2026-08-28 22:30:00 | GOES-19 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 207.3 |
| 14a23c73-a8dc-3270-bbd0-197297b2dc2d | -8.5358 | -55.3629 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 54.6 |
| 5d959e12-5e8b-3d73-a3ff-396335e02b7b | -7.2847 | -45.8652 | 2026-08-28 22:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 111.6 |
| a49f9866-cea2-322c-96b3-29f881f1fe52 | -11.269 | -54.0334 | 2026-08-28 22:30:00 | GOES-19 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 81.4 |
| 7d7321e1-ea78-305d-a274-3a125f59d3e0 | -7.5139 | -55.2851 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 503.2 |
| ffcc8152-8486-37ef-ad48-48e9ffbee92e | -14.897 | -47.7409 | 2026-08-28 22:30:00 | GOES-19 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 56.9 |
| ccce791a-4126-3578-b416-a745c4922c86 | -6.7528 | -55.4661 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 148.0 |
| c9b9dba6-7112-340e-9670-5a4810a1eae9 | -11.1916 | -51.2708 | 2026-08-28 22:30:00 | GOES-19 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 148.0 |
| 8c7ff374-23b6-32d7-bf44-50c41e3dd5a7 | -8.9741 | -50.7866 | 2026-08-28 22:30:00 | GOES-19 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 125.9 |
| 9b4e645f-c597-3304-a8cb-67fa46f7260c | -6.7157 | -55.468 | 2026-08-28 22:30:00 | GOES-19 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 98.5 |


[Clique aqui para ver as próximas entradas](README191.md)
