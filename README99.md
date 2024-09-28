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

## Dados Diários - Página 99

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 14f3ccb3-63b2-3659-8071-efa3bcdbd8e2 | -9.08818 | -61.13195 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 127a1c6c-cabd-3d8d-914b-d942e10656f8 | -9.08684 | -61.13112 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f5e8c834-9f5b-343d-91ce-883d0112e0f4 | -9.08275 | -61.13112 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4a19e5f1-bc8e-33a8-bc0e-771c8e06b9d7 | -9.0823 | -61.13465 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6f4ea982-bc49-3fe3-9e94-e28973a066d6 | -9.0814 | -61.1303 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 336b7e5d-1666-394c-8e3c-9b8a87678b99 | -9.08093 | -61.13382 | 2024-09-28 06:01:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 28f23a30-ef2d-3e26-9cea-791504fffadf | -9.06494 | -67.80759 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 425957f4-ef14-314c-8121-f06457916a1c | -9.04497 | -62.34315 | 2024-09-28 06:01:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a70b4d00-4a62-36e0-91e0-a8a9811f3442 | -9.04125 | -67.89428 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 87d55a76-c40d-36cd-8eab-6169d9b717a5 | -9.04066 | -67.89828 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 932b79ed-697a-393c-a3e6-875c08f503ea | -9.03773 | -67.89374 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d337410e-42f7-3f20-bc28-3828a6399716 | -9.03714 | -67.89774 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| fc5482e8-1d51-33f7-8c98-6b82ddf6da66 | -9.00142 | -67.3783 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c3453565-0e6c-34fc-ab09-4c64a5b3fbff | -8.9978 | -67.37776 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b4d4623e-5876-3786-88a2-46f742d7e055 | -8.99419 | -67.3772 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 58bb8539-2f15-3192-bb0d-fd7e4065ede1 | -8.99357 | -67.38142 | 2024-09-28 06:01:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 496c920b-cf80-31e1-93a0-62a45f4fcd50 | -8.88894 | -61.76269 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 72c4746b-2347-3d80-8383-ab83fb1e1ebf | -8.88331 | -61.76517 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e6e8442a-0989-3efd-91bf-9c53996ba5b8 | -8.87417 | -61.75431 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 40fd3f1d-f95b-310c-8397-714739a055af | -8.84624 | -62.15145 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 33aaaab7-6b67-3102-a4ca-436247d50d0c | -8.84532 | -62.15099 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d0834d0-21ea-357b-8b58-97e458fcfe0a | -8.842 | -62.14478 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 073f2052-be6f-3bfc-bb04-b3b3e8ba4f6f | -8.84118 | -62.15071 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dc6b442e-d5a6-333b-8b56-f5a98682518d | -8.84103 | -62.14429 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 41256332-271b-364a-afa1-7eb938610634 | -8.84026 | -62.15023 | 2024-09-28 06:01:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 94e866ff-53b3-35b4-83ec-72537c604bf8 | -8.81147 | -58.20725 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.8 |
| d3fee867-a891-3b77-9403-70321338c660 | -8.81093 | -58.20655 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| edfcfbce-5501-356e-9ffb-2e22188b02fa | -8.81024 | -58.21236 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.1 |
| a09e1609-c3dd-3005-bf2e-d07a039c94f1 | -8.80492 | -58.20644 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 01764422-d306-3742-a626-20987b64e1d6 | -8.80439 | -58.2057 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5ecfe40c-1e30-328d-a604-a049054a6d7d | -8.80419 | -58.21225 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 57ecefd2-fc87-3c7e-8269-f2b521831c71 | -8.8037 | -58.21152 | 2024-09-28 06:01:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| ba46c7fa-37d7-3c7a-892a-df30de3f2236 | -8.611 | -61.28242 | 2024-09-28 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b7ba55fd-e1b2-386e-b9c5-300b0eaae130 | -8.61054 | -61.28584 | 2024-09-28 06:01:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 269d0558-6b28-31ae-a5ba-10083e4d477e | -8.22633 | -61.47284 | 2024-09-28 06:01:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4420b084-8571-3d4f-b7a4-ec0e13e08243 | -7.40756 | -59.80913 | 2024-09-28 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddbb0ebf-44b6-3083-872a-473d6b8d408d | -6.82915 | -59.30836 | 2024-09-28 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e579c250-a58d-331c-85cc-58320592388c | -6.82856 | -59.31273 | 2024-09-28 06:01:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| aa600805-0a39-3b87-8cd3-1243b21776da | -5.59972 | -67.77604 | 2024-09-28 06:01:00 | NOAA-21 | CARAUARI | AMAZONAS | Brasil | 1301001 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 86e59d81-8646-32eb-9fc2-dc4702b264b3 | -12.0195 | -61.22145 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bfb59876-d49e-3ecb-aa94-4b3abe83d695 | -12.01903 | -61.22536 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 6b5d6cba-0809-370c-8fe2-27c3cb204a79 | -12.01434 | -61.21683 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d73a3287-8b91-3d9e-b139-446a11878b63 | -12.01339 | -61.22469 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f3dd4e8-5d09-32c3-997f-3d0458eb111a | -12.01291 | -61.22866 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ab2baf6e-45cf-3dbe-a657-fa03b1614f05 | -12.00871 | -61.21603 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0ef249db-7303-35ff-aa5c-d703969d43f0 | -12.00824 | -61.21996 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| e68d5df9-50ba-3d8b-8b26-1b1a90c21a0e | -12.00776 | -61.22389 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 053b9214-adb0-3f0c-a837-7926694e3ed6 | -12.00729 | -61.22781 | 2024-09-28 06:01:00 | NOAA-21 | PARECIS | RONDÔNIA | Brasil | 1101450 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 559c0919-8759-300a-8ae0-c549bc42be68 | -11.74807 | -61.328 | 2024-09-28 06:01:00 | NOAA-21 | PRIMAVERA DE RONDÔNIA | RONDÔNIA | Brasil | 1101476 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0e2814fe-a249-3ed6-936a-a80fc832feb5 | -11.74221 | -62.55815 | 2024-09-28 06:01:00 | NOAA-21 | SÃO MIGUEL DO GUAPORÉ | RONDÔNIA | Brasil | 1100320 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a5c61d68-e6a3-3745-b404-d30656606b51 | -11.62885 | -65.01011 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 14b94e76-f3e0-3b25-999b-dac003a31b6d | -11.60865 | -60.36237 | 2024-09-28 06:01:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 73fade41-ef76-3097-a929-2df3dcc9ab85 | -11.60818 | -60.3663 | 2024-09-28 06:01:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ac1bb269-584e-3615-9604-cac167bd21fc | -11.60437 | -65.02814 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2554f57f-6f83-354f-b32e-9dbf7d377a3b | -11.60094 | -63.91657 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8ff291a0-e8ec-35fe-a7ea-bc53c92cb409 | -11.60028 | -63.92155 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52695dfe-7a5b-373c-a2cb-dbc8bc91cd2a | -11.59692 | -63.91108 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2be6d662-3d77-3e6b-9891-aab73b305106 | -11.59369 | -63.9709 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 17d5e866-1c5c-3549-83b4-ea64718bde54 | -11.58957 | -63.71213 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 7187f020-4105-3dae-8e76-dccf0b5ebec2 | -11.58348 | -63.72196 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.7 |
| f10c0de5-7181-3a64-a55c-db71a8cd258b | -11.57812 | -63.72618 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4b84c764-0161-3d2b-93f0-00f8edf0f48a | -11.57211 | -63.7354 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d1b17101-f162-3f97-a469-be827fcdb7c6 | -11.56827 | -63.91189 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 301e8991-7394-3a68-b2f2-c4b94993d44f | -11.56763 | -63.91684 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9af46f1c-cce5-38a9-acff-fda81b646117 | -11.56698 | -63.92179 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 10dd0bc1-ebb0-37d8-be4a-cc8390abbcdf | -11.56425 | -63.90632 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 358f624b-50d9-35d4-88a0-dec3cd917e3f | -11.55958 | -63.90566 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2a82bdef-d75b-3431-9329-10afedd5c004 | -11.55491 | -63.90501 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2aae57d0-65bf-34f0-844f-731dc4c49f6c | -11.37622 | -59.13456 | 2024-09-28 06:01:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 783f1a61-f588-314c-ad3a-fac7f55f9897 | -11.25891 | -60.61531 | 2024-09-28 06:01:00 | NOAA-21 | ESPIGÃO D'OESTE | RONDÔNIA | Brasil | 1100098 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 917759db-69f7-3a7e-aff0-44a1e12f4026 | -11.23393 | -60.47967 | 2024-09-28 06:01:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 234d4103-0bcd-38fb-94a0-bd7faee83401 | -10.90341 | -63.88309 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bfbc84f9-37a5-3d06-8e76-04843760cb2b | -10.88808 | -64.17498 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| f096130c-7691-3b63-9701-22f508022a76 | -10.88748 | -64.1794 | 2024-09-28 06:01:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 0fc39eb8-3d59-3ddc-9824-49951780137d | -10.69494 | -58.53561 | 2024-09-28 06:01:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| c752d8a1-eee1-3d22-9c62-df592311c8dd | -10.69438 | -58.53232 | 2024-09-28 06:01:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 27e186b7-5228-34e9-9cef-998e059825ec | -10.69374 | -58.5379 | 2024-09-28 06:01:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 25353745-c773-3cfb-9709-437032180e31 | -10.68838 | -58.53479 | 2024-09-28 06:01:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 5573eda4-6d82-3beb-b866-53f0e47c6ed9 | -10.68718 | -58.53708 | 2024-09-28 06:01:00 | NOAA-21 | CASTANHEIRA | MATO GROSSO | Brasil | 5102850 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| aaf37cc1-3850-3938-a79c-db8d8134a5a6 | -10.64944 | -63.9659 | 2024-09-28 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| f88bac9b-dbc0-3792-a049-667bbc01e1d1 | -10.63898 | -63.97395 | 2024-09-28 06:01:00 | NOAA-21 | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d9e13cca-8b55-3d2c-8acf-aeaba6ddfdc4 | -15.37021 | -58.17727 | 2024-09-28 06:03:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 96282564-601c-3610-93ec-542a883644f1 | -15.36518 | -58.18003 | 2024-09-28 06:03:00 | NOAA-21 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a259b583-c1d9-360c-91e2-678d068e3b22 | -14.8948 | -57.97412 | 2024-09-28 06:03:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 6ec182d5-5f2f-3c6f-9b3c-2c810e35f9b6 | -14.89407 | -57.98173 | 2024-09-28 06:03:00 | NOAA-21 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 6535c6cf-3f9d-3e4e-853a-573b3d921a09 | -13.69888 | -60.70275 | 2024-09-28 06:03:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7768bf80-4d31-328d-bc5e-fa7756c95486 | -12.99282 | -62.69849 | 2024-09-28 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 3b5e35db-eef1-3379-be82-ed2e6554c7a7 | -12.99243 | -62.70168 | 2024-09-28 06:03:00 | NOAA-21 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| feecaab7-e6c3-396e-ac77-969df1c8fc75 | -12.86272 | -62.761 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e289ee9e-458b-3cb5-a66b-0cadf666e0b1 | -12.86234 | -62.76413 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ca899f3c-7ef3-3774-9e00-d4ac816f6ab3 | -12.86021 | -62.73839 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a71b47aa-95a9-3127-919e-8c37232cf21b | -12.85983 | -62.74152 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 47fc06be-ec69-321f-a846-f905cd9b4b2e | -12.85946 | -62.74466 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| c2eaf575-e94e-3145-9095-69f2fef34528 | -12.85908 | -62.74779 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 49990357-30d0-39d6-901f-4830965e5752 | -12.85871 | -62.75091 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a838450e-42c9-302b-ba64-fb789fbf45d4 | -12.85833 | -62.75403 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 9e744d63-5288-3a07-8cca-4d718db4432a | -12.85795 | -62.75716 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| dba37007-8615-3106-8245-05bb09338bfe | -12.85758 | -62.7603 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 7d286c27-106e-373a-8ac3-385de7c7b9a6 | -12.8572 | -62.76343 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| a83bd883-ca9d-38c8-bfad-2e32fcec7861 | -12.85581 | -62.73142 | 2024-09-28 06:03:00 | NOAA-21 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README100.md)
