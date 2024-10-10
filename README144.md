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

## Dados Diários - Página 144

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7fde2177-f142-3cd6-86fd-2de9d2807070 | -11.66711 | -58.89822 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 90d3974a-318d-3566-85be-e4eaceb263ff | -11.124 | -59.09088 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 020b974f-67c6-3950-9e81-daf61cf1756e | -11.1234 | -59.09571 | 2024-10-10 06:01:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9509c3ac-ad47-3365-af32-f18d8288c63f | -10.4628 | -60.0999 | 2024-10-10 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 0bc0ede6-953c-3055-a4ef-473c06cb6240 | -10.46226 | -60.1041 | 2024-10-10 06:01:00 | NPP-375D | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| c19861d7-5f58-30ea-888f-ae18baca24bb | -12.99218 | -62.74888 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f55d59a3-6dab-3223-8bfc-364048520a7e | -12.99102 | -62.74227 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8a630b46-a2ae-3f7a-99e6-d1a096fe5eaf | -12.99063 | -62.74537 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 228020f2-4c3d-333a-bbef-1a6dc9d33a7c | -12.99023 | -62.74847 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6203b6e9-1bea-3bc9-a53b-09a4d4260acf | -12.98815 | -62.7389 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| eb6593c9-ac87-3e04-902f-523953f6ce9e | -12.98777 | -62.742 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| b169dccb-c28c-3c1a-85df-c0ea0abc46c7 | -12.9874 | -62.74511 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| f3453904-54ea-3b1e-88b1-abfc571b8c0d | -12.98703 | -62.74822 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ec492c47-38e2-3587-a7ae-afd5de4c3852 | -12.98587 | -62.7416 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| a20f1d6d-ec8c-3038-adfe-8efbc3967739 | -12.98547 | -62.74471 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 5744f99c-b179-30a5-9810-0c1b0bc80d07 | -12.98508 | -62.74781 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 564f558a-e2b6-3058-a75e-5ffb77aab700 | -12.97591 | -62.696 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0113df14-d3d8-3187-8403-2754c9ad9f0f | -12.97074 | -62.69533 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b74fbd67-ab95-348d-9291-f2ef8853400d | -12.96596 | -62.69156 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 63c505a4-e0d9-3a15-8ccb-f101fe35664d | -12.92442 | -62.73039 | 2024-10-10 06:01:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2e4b38ca-66ea-348a-afdb-f33c279b635f | -12.91965 | -62.72659 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 54f67b2a-306c-3f47-adc0-e883b8821d23 | -12.91926 | -62.72967 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e30b923-dfdc-304f-899a-1de8e2c4925f | -12.72967 | -63.03856 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec83ecc8-2ede-30bb-bbee-324207028328 | -12.72892 | -63.0444 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 03490f33-fadf-3905-bc62-ed85163f3d2d | -12.72881 | -63.04036 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a35b69d3-293b-37de-92af-7b333e609e3e | -12.72816 | -63.05026 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 9f3e5e19-a8fe-32f5-98f3-640ea3462b16 | -12.7281 | -63.0462 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1fddb3fe-86d1-316f-a571-70db84ea37cd | -12.72738 | -63.0521 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 86282b00-2ed4-34fb-a9da-b543b66e4731 | -12.72514 | -63.0737 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 0845ff60-71e4-39bb-b51e-24a360de90cd | -12.72464 | -63.03787 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3d1bdd6e-a546-3afe-9982-b368a65ef257 | -12.70581 | -63.06515 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 13db7fb9-7b7c-3fa3-9e1e-cde2be190213 | -12.70506 | -63.07102 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b284d151-e70f-3e79-ac80-aa67302f7367 | -12.70264 | -62.96893 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1aaeba6a-8ac0-3f55-bb3b-414bb063f443 | -12.70079 | -63.06449 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6794044f-c44c-39ac-96d3-64bbca818b4c | -12.69725 | -63.05213 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b213719d-eb24-3af8-827f-18b2999c1d41 | -12.69684 | -62.97419 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 8b4d1bf1-c469-357b-8bb6-8bc308378598 | -12.69179 | -62.97352 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e8f27a55-c87f-390d-9396-c136fa7d5f59 | -12.68674 | -62.97284 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| be0c9b80-f760-39f1-983f-1acb25c9e604 | -12.68242 | -62.96627 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 69a74af4-7059-3f94-ab71-2f36bd13e2d6 | -12.68168 | -62.97216 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 0fd465b4-b751-3b77-90ac-24400540d7f9 | -12.67736 | -62.96561 | 2024-10-10 06:01:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 187a5386-32f9-375a-bc59-99c66c7b61b1 | -11.61834 | -63.96412 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 4a0e8251-caf9-369b-ad50-ea1f058156e6 | -11.67598 | -65.2185 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aee14a57-79f6-3129-8daf-4e4a64f5c195 | -11.53127 | -65.20361 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e3538bb3-3adf-3ea8-ba45-cbf9d68517ef | -11.53072 | -65.20761 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| df80f08b-52d9-3085-bc4a-35fd957edb57 | -11.52645 | -65.20702 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 371b246f-cf2f-3e3d-be5f-3e964b42d699 | -11.28648 | -64.90115 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5851a3a8-feb7-338c-9fcd-fe8ca925a036 | -11.28272 | -64.89635 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c876ae9b-9ac4-3add-8b2b-a93bdfd9ee38 | -11.28215 | -64.90052 | 2024-10-10 06:01:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 4d5e9f15-b8d3-377c-a489-30e15f3056c6 | -12.7247 | -63.0403 | 2024-10-10 06:26:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 67.3 |
| 16ad8f00-832a-38d7-9264-0f54af0b4e90 | -7.09669 | -59.41897 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 25.3 |
| 388fe5cb-27b3-3396-aedc-5135e2d40f98 | -7.09327 | -59.4107 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 58.2 |
| 10f48b06-4598-3fd8-a919-248ceb4f0804 | -7.07985 | -59.41676 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 38.5 |
| 6de05207-66ba-3b27-a669-587b0c5f5a36 | -7.04275 | -59.40423 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 71e69703-60c9-386e-b16c-337455d79395 | -6.78149 | -59.3167 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 72.6 |
| 16999822-2271-3d0d-bda2-5ab8a179427f | -6.76459 | -59.31467 | 2024-10-10 06:52:00 | AQUA_M-M | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 55.6 |
| e34f976e-a7fb-3d1f-8dd5-20eda1cca7df | -6.52984 | -60.05798 | 2024-10-10 06:52:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 25.2 |
| e39ca15c-69f5-39c8-8337-d8bb7e88fc0a | -6.52015 | -60.05184 | 2024-10-10 06:52:00 | AQUA_M-M | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 36.9 |
| 4b701e9f-6837-3738-ae5a-6f8d4e584f80 | -11.28758 | -64.89986 | 2024-10-10 06:54:00 | AQUA_M-M | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 13.8 |
| ff97a879-c8b7-3bc6-b9b6-709d193ca945 | -13.73898 | -60.61097 | 2024-10-10 06:54:00 | AQUA_M-M | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 62.3 |
| 32454301-8d3f-30a1-98eb-70c14fd66ed9 | -13.7346 | -60.6079 | 2024-10-10 06:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 61.9 |
| 22da126d-9e5a-3110-a794-9ee6c64fc94c | -13.7346 | -60.6079 | 2024-10-10 07:06:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 71.6 |
| 8db57f94-6d31-31bb-bcc7-e70a82b5f0b1 | -10.8567 | -63.9177 | 2024-10-10 07:16:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.6 |
| 3ef80172-6ff5-3a3f-830a-c268688b7db6 | -10.8754 | -63.9169 | 2024-10-10 07:16:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 47.6 |
| a4b96b92-a0e0-3c4b-9a1a-08a309e37a3a | -13.7346 | -60.6079 | 2024-10-10 07:16:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 50.6 |
| cede7cc6-91e0-373d-9e79-e7f26d55aea2 | -10.8754 | -63.9169 | 2024-10-10 07:26:09 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.1 |
| df83c6b2-29b7-3e55-8fd1-40ae1df3afd5 | -10.8567 | -63.9177 | 2024-10-10 07:26:09 | GOES-16 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 50.9 |
| b5e1edd5-f1be-3c10-94fd-38ddab6345c9 | -12.6875 | -62.9656 | 2024-10-10 07:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.5 |
| 2bfdf40f-25b5-3538-900e-413f99f02b1b | -13.7346 | -60.6079 | 2024-10-10 07:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 69.6 |
| 768197bc-1d05-365f-a1d9-8d2bc76b4e38 | -12.6875 | -62.9656 | 2024-10-10 07:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 45.7 |
| 4c87a572-7df9-388e-ae63-a0d8eeaaf602 | -13.7346 | -60.6079 | 2024-10-10 07:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 67.8 |
| 0f6e1dd9-a48d-3c87-9f7b-d73e35e29d12 | -12.9922 | -62.7361 | 2024-10-10 07:56:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 53.2 |
| 58d5a9f4-86d7-3b86-ac6b-410fb3c90f22 | -13.7346 | -60.6079 | 2024-10-10 07:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 81.6 |
| 96fbba4c-7d22-38e2-97ca-2cd29f326b36 | -12.9922 | -62.7361 | 2024-10-10 08:06:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.2 |
| 054281ca-c580-3d8b-a4df-f871388156e2 | -13.7346 | -60.6079 | 2024-10-10 08:06:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 71.4 |
| 9eb3a7c2-1783-33eb-b2ac-58b214fca5eb | -12.9922 | -62.7361 | 2024-10-10 08:16:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 55.8 |
| bb4dc506-7de9-3422-91e9-6c7892044019 | -13.7346 | -60.6079 | 2024-10-10 08:16:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 76.3 |
| 2519fcc3-0fe5-3a5e-a769-3b5b0ae95b2e | -12.9922 | -62.7361 | 2024-10-10 08:26:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 54.1 |
| 45e1219d-7fcf-3c32-8d24-514a158dcb1c | -13.7346 | -60.6079 | 2024-10-10 08:26:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 77.0 |
| 62a36101-eed5-3dd0-b93c-c8dc093625fe | -12.6676 | -63.0819 | 2024-10-10 08:36:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 54.5 |
| 4272807b-63e7-3600-b9df-604f3b63fe52 | -12.9922 | -62.7361 | 2024-10-10 08:36:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 52.0 |
| 30940355-2132-36ef-9b24-f667bfd43ecd | -13.7346 | -60.6079 | 2024-10-10 08:36:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 72.9 |
| 3fe58376-cca1-3ec5-bb86-e13ac8a4a28b | -12.6676 | -63.0819 | 2024-10-10 08:46:19 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 55.0 |
| 1f8e4f83-dfab-3b8b-882b-a6eff6f686c2 | -13.7346 | -60.6079 | 2024-10-10 08:46:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 74.5 |
| be639a06-cd20-387a-b819-029bcbc63fa5 | -12.9922 | -62.7361 | 2024-10-10 08:56:21 | GOES-16 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 47.3 |
| 859b3fdd-c9bc-38ff-8b63-540e91c34b93 | -13.7346 | -60.6079 | 2024-10-10 08:56:25 | GOES-16 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 68.7 |
| 139a1aa6-ffc9-3faa-945d-746a0b86b723 | -11.3087 | -51.0251 | 2024-10-10 10:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 117.8 |
| d775771a-7132-30ea-b2dd-9e4c0b88edbb | -11.3084 | -51.0464 | 2024-10-10 10:06:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 101.1 |
| 19a42ead-d842-3697-8365-3e92c8a65b6d | -11.3087 | -51.0251 | 2024-10-10 10:16:10 | GOES-16 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 122.4 |
| c7fb7977-3f30-3c7e-819e-bfd277e2477b | -13.8175 | -44.5726 | 2024-10-10 10:16:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 148.6 |
| 3897a3fa-be85-356b-9d84-7692094eb127 | -12.9734 | -46.1931 | 2024-10-10 10:26:19 | GOES-16 | CAMPOS BELOS | GOIÁS | Brasil | 5204904 | 52 | 33 | nan | nan | nan | Cerrado | 200.7 |
| cd649476-5e74-3c09-a054-13541898e9f2 | -13.8175 | -44.5726 | 2024-10-10 10:26:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 164.7 |
| 3b7a5d60-90f2-37ef-a1b5-c62d29fed79c | -13.4027 | -46.9214 | 2024-10-10 10:36:22 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 154.7 |
| b011d680-fba5-38fb-a8ed-e5e8d1c18c3e | -13.4032 | -46.8987 | 2024-10-10 10:36:22 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 148.0 |
| b47cc1c1-861d-3b64-8ebc-bc4516b6ee37 | -13.798 | -44.576 | 2024-10-10 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 134.1 |
| 04f53662-c47f-388c-8395-be578e9218c6 | -13.817 | -44.5961 | 2024-10-10 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 133.4 |
| e6dec018-5b6e-3aa9-81d5-f52054f7304c | -13.8175 | -44.5726 | 2024-10-10 10:36:24 | GOES-16 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 308.7 |
| cd342981-ea67-34ae-9d84-1666a25a9b44 | -11.2442 | -44.2392 | 2024-10-10 10:46:09 | GOES-16 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 96.9 |
| d929edb7-ee6a-3de1-9a07-0b6f12cf47c5 | -13.3834 | -46.9244 | 2024-10-10 10:46:22 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 146.9 |
| 968be259-c5e0-3bc1-9bab-3e8366728196 | -13.4027 | -46.9214 | 2024-10-10 10:46:22 | GOES-16 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 202.2 |


[Clique aqui para ver as próximas entradas](README145.md)
