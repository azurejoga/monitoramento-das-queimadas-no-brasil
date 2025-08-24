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

## Dados Diários - Página 85

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9490800d-c4d8-323c-ab0b-17f35c9d10c4 | -8.92668 | -62.43647 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5ac41a72-e4b5-3d92-8ef6-bc995d931548 | -8.91308 | -62.44438 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2b53e3dc-18f5-376a-bd99-c40d61fe52f6 | -9.01747 | -65.38654 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8d99a5ca-1250-34ae-80fa-eb8213d4a2c7 | -9.01345 | -65.72393 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c539c686-44f5-3d9a-8bc0-fbbec17f629e | -8.13376 | -62.86226 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 62be3fa5-331c-3cfe-a4c8-e5b5ec2b964b | -8.89626 | -62.43707 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| c3af724e-d32d-36f7-b0f7-3632553ce761 | -8.90303 | -62.423 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| cf930eb7-0bfa-3664-8016-582700624b9b | -9.0108 | -65.70586 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e8e671ec-d975-38c7-bbbd-49c594ac392a | -7.94004 | -63.06271 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c4d9cdda-95fe-3203-b53a-7b6a5a753cb7 | -5.42356 | -60.17094 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 1daa2f7e-1a5f-383b-bf1d-47c61c05490b | -8.82634 | -69.39774 | 2025-08-24 06:14:00 | NOAA-21 | MANOEL URBANO | ACRE | Brasil | 1200344 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7613e41c-a165-3bb4-91ce-a7088a7e9e24 | -9.02168 | -65.6987 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.4 |
| bcbbaf1a-016b-3dbc-903c-ed8ad3f1083a | -8.90184 | -62.44282 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4cb48e8e-8da7-3776-994f-17c33f9f719e | -9.02874 | -65.72321 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 70e80029-17d2-3ef8-8dba-b62ada1ce421 | -9.02371 | -65.72259 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7d7a57d6-64b8-3d68-91b9-6205120fc13b | -5.61209 | -60.23648 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 5.7 |
| fe830ae1-08c0-3b94-9a58-896e86942003 | -8.91366 | -62.43955 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| f3c2754f-4cad-32fc-a477-50cc60c9545e | -9.0345 | -65.71813 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a27c466e-03f8-3195-b786-7666ef7678ab | -7.55377 | -63.86185 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0253f3d9-48dc-343f-88d4-9d17cb5a6fb3 | -7.97251 | -63.07875 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| d1367944-6997-31d0-9bbc-3e154490dac6 | -8.212 | -69.86467 | 2025-08-24 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 481d4208-4903-373a-8c5d-bb8f496580ac | -8.67183 | -68.68687 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9cc6fb80-7309-33c7-b126-0994348a1a9c | -9.23716 | -60.47885 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 02ea0278-5dd8-35f4-a3d1-fc01755e08ac | -9.02667 | -65.70207 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 600e6152-fcf5-3440-8cf4-bc7240a45219 | -5.4318 | -60.17335 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| fd2b01de-72ff-30b2-ac43-47a284fa0bb1 | -7.94059 | -63.05844 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 757c0c0d-79fa-3447-8477-0a3fe955c01a | -7.54466 | -63.84547 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 91840c4a-26eb-33e9-8e4a-c09218175e78 | -9.02092 | -65.70457 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 869727ed-c310-3852-aa52-163e98fe7230 | -9.02949 | -65.71741 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 028d4daf-fa74-3368-b903-968f4e6f12f0 | -9.20842 | -60.78801 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 48d10453-3f6b-3b16-8570-8b09e2f1415e | -7.43637 | -60.62968 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8f30b231-b362-3b79-b881-5372ed757a7c | -9.00236 | -65.69262 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e6625905-4e14-3ccb-a71f-e561c8e65c5e | -8.78518 | -68.65025 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| bd21d86c-e4a3-3222-8a28-0717f01c086d | -9.00502 | -65.71078 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a0324c33-fc49-32f2-b7fd-e1d4427e5727 | -7.57032 | -63.44125 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| dcc52ea5-849f-3e86-a337-b9576774003b | -6.91836 | -62.91216 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a1f1c9ff-7f80-3495-b488-b029fa1e7605 | -9.01787 | -65.38344 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.4 |
| d2972644-93ee-330d-adb1-ddb46b2ab625 | -7.55074 | -63.84254 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| bc2cddd6-4075-3d61-a015-0f0054e8c3c0 | -9.00737 | -65.69337 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ac046e14-4eee-3fa5-a94c-666db7885c33 | -9.33173 | -63.18852 | 2025-08-24 06:14:00 | NOAA-21 | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 14.8 |
| e00fc53e-13be-36d7-a9ea-9219a9f6a2e6 | -8.62793 | -62.63063 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.3 |
| 01a1ad79-fa51-3080-875f-2a46eff6e99e | -7.9181 | -63.04663 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 0b7ce39a-ec6c-35d1-893f-bb334954b07f | -5.6189 | -60.23742 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e57c14e7-08a5-3361-9a87-5312c4794178 | -5.61325 | -60.24174 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 42bea830-7f82-3961-b8ad-d72e923c4e34 | -8.61313 | -62.59986 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 152f505a-fde1-3d04-a0df-9a9dd49d1721 | -8.90687 | -62.44347 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e88ef494-2a35-3dde-8f22-87fdc658cedb | -9.00578 | -65.70513 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 6b2a5eb3-cffd-3e3c-88fb-f0299388e357 | -7.55823 | -63.86251 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| db621867-00f3-34a6-809e-62488b7f90b0 | -9.02204 | -65.6985 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 89bbbcbf-5edc-321d-bb7c-b0515f139036 | -7.54871 | -63.8574 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c8dd2178-4008-3b48-b241-07e4871a3c05 | -8.89751 | -62.42732 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 5.1 |
| dde0c65c-c1cd-38c5-8685-fd97cf16fd55 | -9.01119 | -65.70298 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| d7c4e156-fa9b-39c7-bfdc-ca6b222199ef | -9.25039 | -60.48773 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| dc51e07b-dd30-3a77-882e-620b813d26b8 | -6.58137 | -59.87722 | 2025-08-24 06:14:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 280a7262-24c0-35d7-b982-575ab88bc978 | -7.43711 | -60.62363 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 841a0d2f-46fc-33d8-8819-983e3a4823be | -8.58807 | -68.15056 | 2025-08-24 06:14:00 | NOAA-21 | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d1a1ed59-7072-334e-8540-89b83d3c8359 | -6.57635 | -59.87785 | 2025-08-24 06:14:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| dd00b705-d242-35f0-992c-5d344511de86 | -9.05456 | -65.72118 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2841c7b2-a57d-3288-b34f-da3c78b1139e | -9.20156 | -60.78869 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| d4eb54b2-fc6d-3c67-8bc5-ffa9c582316f | -7.94706 | -63.05499 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 38805086-e827-3e64-a4c0-6c1ca787e709 | -5.45736 | -60.18988 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| a6a784e5-193f-30cc-8961-fa1c27a90289 | -7.42835 | -60.62381 | 2025-08-24 06:14:00 | NOAA-21 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2bb56bee-4f80-3ef1-8106-b4e6c4300376 | -9.0132 | -65.68816 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 842f208a-b9f1-3e31-b884-568bdebec090 | -8.90361 | -62.41816 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 07917cdd-1bbe-3d97-b1c3-5af5e1730f16 | -9.23912 | -60.47789 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dbd0ec38-23e8-3fbe-94d8-0b8e22a7d810 | -8.21644 | -69.86064 | 2025-08-24 06:14:00 | NOAA-21 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 644648a6-d554-3674-ac80-2dae9f9cfeb1 | -8.13317 | -62.8667 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 08204210-da94-3d8b-b7dc-f5d6e9ed6c57 | -8.90122 | -62.4477 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a72dec8c-d9e4-347b-9da6-514c11692626 | -5.42499 | -60.1723 | 2025-08-24 06:14:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| c64bd9cd-24f0-3eed-83c2-d2f8a9224900 | -8.90867 | -62.43886 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b21dfd11-108e-3b74-a663-b2fea042f644 | -9.17087 | -60.80923 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 24b2fae2-075c-3c67-9a84-d0dfc844f872 | -9.01543 | -65.70941 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| c6403d07-92f0-33c1-93dd-5d44d88f69f0 | -9.00884 | -65.72027 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a9f21b9d-d016-3b81-b4cb-87ec212274c7 | -9.07036 | -65.71766 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c5eec7cd-a7bc-3835-a541-8561edd4fd8f | -7.55985 | -63.85894 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |
| a8d6aa93-3096-33b1-a818-9820c21b9184 | -7.96716 | -63.07362 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 85852ca2-2415-3294-a537-7a08a077c3f0 | -8.90497 | -62.41843 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 968828e1-4965-3d55-a941-608d96e29909 | -9.23472 | -60.92233 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 6b78f336-ab3a-3c9c-9509-bc1effb9fecf | -8.90746 | -62.43861 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| dee15147-d4d5-3755-b9c4-bb61b0b3ddaf | -7.97484 | -63.072 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 6d5a5a53-4366-3ada-a316-09cd168c9e91 | -9.14024 | -60.76906 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 52712b2d-0859-339e-b5cb-3262acf29718 | -9.01504 | -65.71227 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 8322461f-c46f-3083-9ef3-87fec3d406fe | -8.14213 | -62.8649 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 201c5b82-7c54-3ab8-b8a9-24225255a937 | -9.05417 | -65.72411 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c8c3629e-d574-3979-941d-f6ceeac507ab | -9.01582 | -65.70657 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1e69478a-774c-38b7-93b5-0a17018899a1 | -9.20073 | -60.79361 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 12.3 |
| 7e14497c-cdc7-3e5a-abba-7bdfab79c606 | -6.74652 | -62.87173 | 2025-08-24 06:14:00 | NOAA-21 | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c6d244dd-d2ba-3401-a842-a6c9bfcceb0f | -8.61332 | -62.64773 | 2025-08-24 06:14:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 382cdb9b-74d6-3b18-b7a2-4f88c2d1e4fa | -9.02055 | -65.70746 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 00a536ad-b2c8-3fa6-b8be-134308d2d869 | -9.02627 | -65.70501 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 2bab9a7d-4032-3b23-b6ea-46e2277f3ea8 | -9.47555 | -63.13292 | 2025-08-24 06:14:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| bcd922ac-5464-3b13-aec7-ac577e806b8c | -6.58338 | -59.87886 | 2025-08-24 06:14:00 | NOAA-21 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c2890831-d9c6-3a74-95db-182ff40363b8 | -9.20081 | -60.79521 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| 917247c4-0e7b-32de-ab9f-583c457a6690 | -9.03914 | -65.72179 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ebbdfe69-d161-3dbf-b0d7-a5a8b4087ce6 | -8.91363 | -62.44944 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbdbfabf-3a73-3629-8f5d-014c1f48b7f9 | -8.90247 | -62.43793 | 2025-08-24 06:14:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 146af765-7551-37e9-8053-8026f6340136 | -9.02468 | -65.71655 | 2025-08-24 06:14:00 | NOAA-21 | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 3.2 |
| c7f13726-40e8-359c-96b4-3d7b5093ff60 | -9.20697 | -60.80243 | 2025-08-24 06:14:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 7882eb8b-f7c7-320f-aa5b-27c208e938f5 | -9.00269 | -63.63342 | 2025-08-24 06:14:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 601228a1-a021-38d8-803d-3637d2f65bb0 | -7.54709 | -63.86094 | 2025-08-24 06:14:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 2.9 |


[Clique aqui para ver as próximas entradas](README86.md)
