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

## Dados Diários - Página 136

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 06ab41c3-1a51-3a18-9261-adee0ae855ea | -12.85422 | -62.79095 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 73a3a6d9-397d-3b07-ac1d-fe6b300f0f0e | -12.85363 | -62.79404 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 92043aae-3cc3-3039-9371-4e958708c14f | -12.8485 | -62.79302 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 510f2782-7cc6-322e-8e06-a23887170124 | -12.8479 | -62.79612 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cc406c74-a10e-3782-97e5-1408c66c7b4b | -12.84729 | -62.79923 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| b81adca4-0630-3714-85ce-f967fa5d6193 | -12.84549 | -62.80857 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 434e84c0-ae9e-3ae1-9fc1-5300c0240c95 | -12.84277 | -62.7951 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0bb82722-679e-39b1-8a05-20476f7d07de | -12.84217 | -62.79821 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 241e81dc-cc0f-3361-9b22-d511db8221a4 | -12.84156 | -62.80132 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 2472a7d2-7e03-3b3e-88b2-5e30823f8f34 | -12.83643 | -62.80029 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 32cdaba7-21c5-37ea-a8fd-ff6030fc46ed | -12.82206 | -62.48205 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ff29a312-1c0a-38c4-a54b-d0a96899e312 | -12.81704 | -62.48104 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3da83d91-e57b-3cdc-ae73-dcb22477a650 | -12.7924 | -62.50059 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| ca2a1cd4-2a9d-3a81-8c7b-89a96cb65051 | -12.78622 | -62.50553 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0da66a54-e95a-3566-aa27-909d93aec800 | -12.76996 | -62.75459 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e1c50c0c-f9c5-395c-9554-4b9253f5bcd1 | -12.76936 | -62.75772 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd443825-add1-3d5b-81ce-547d061c42f4 | -12.76876 | -62.76084 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e2ce18c1-0c21-3d52-a0c3-0deebfbd378f | -12.76425 | -62.75665 | 2024-10-03 04:51:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2fae85c0-11a5-3de5-b726-d7502b5a0922 | -12.90504 | -62.4729 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.3 |
| e2e8d671-60fe-3895-8e2f-73335aa0d7e6 | -12.9039 | -62.4788 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| 11e3d111-dc06-3140-9057-aa956ed2be5c | -12.90277 | -62.48471 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 16.9 |
| c31266ed-2f29-365b-b44c-13b79539116c | -12.90191 | -62.48913 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 53925570-f89f-34cb-862f-0fb5314dd0a3 | -12.9002 | -62.498 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 6.5 |
| 7d14d1c8-cea7-36fe-99d0-9c861e8058aa | -12.89964 | -62.50096 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.8 |
| f21c254e-d448-389a-a0d7-07696f59d6bd | -12.89518 | -62.49699 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bd178eb4-5ec2-3558-beb8-aba91d7e562e | -12.8916 | -62.5426 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 06c5cd2e-835e-3bb3-9b76-93e77c01da3a | -12.88599 | -62.54457 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2ac27d25-c7aa-371b-a7b0-c4fa95380d23 | -12.87841 | -62.48733 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 00084261-86b1-3cbb-9921-b45e95727c91 | -12.87625 | -62.48704 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a852a14b-29b5-3899-88db-58d51bfbe434 | -12.87181 | -62.48307 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 445b35b1-b93b-3735-b6e5-fb070bcbd7b4 | -12.83827 | -62.47907 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1b02bf2b-d28f-311d-816e-a6355e33eb35 | -12.83324 | -62.4781 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 4fa395ec-addd-3026-8998-f8831e5dba27 | -12.82821 | -62.47713 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bb74c1c0-5b7d-3ccb-a202-614b89e69a8a | -12.82797 | -62.58874 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 64063093-b59b-341e-8a63-08b9cc4afc49 | -12.82319 | -62.47612 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 8a57ac26-4e0d-3c4d-b73a-583e0ed454ea | -12.82263 | -62.47909 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fde64ba4-8b89-36d3-a6db-f3e22dc11ea9 | -12.8176 | -62.47807 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 86604198-ccfe-3942-bf10-696ecf0de0a4 | -12.80747 | -62.50375 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 33f4038b-b6b3-3353-9657-92d6a263fec4 | -12.80301 | -62.49975 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.4 |
| bdf0ee06-0fcc-3bcf-ba7f-525d29b104d4 | -12.80244 | -62.50273 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0ab9e36f-a99e-3552-ac73-b50be8405b70 | -12.798 | -62.49866 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| fac7dfce-2128-3432-afaf-3dc7805e7c6b | -12.79742 | -62.50166 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 1870f93f-d44d-33ab-84fc-0c729e45e3ac | -12.79182 | -62.50359 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 60123343-ae74-3c0b-bc8a-410a726edd7c | -12.78564 | -62.50853 | 2024-10-03 04:51:00 | NPP-375D | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 06854890-067e-3a0b-82c7-8c3a3ca5b307 | -7.5866 | -63.36054 | 2024-10-03 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 5baa1bf2-64d7-39b4-a214-4e6bdfe0af57 | -7.03538 | -63.08433 | 2024-10-03 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e1404266-22a2-3670-9f0a-ce47b4ae8b33 | -7.03465 | -63.08839 | 2024-10-03 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b8854773-c78d-3a8d-8ecb-e95d834c8a70 | -7.02887 | -63.08733 | 2024-10-03 04:51:00 | NPP-375D | HUMAITÁ | AMAZONAS | Brasil | 1301704 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 99bda408-4681-3a72-a4c7-e9998e0ddb3c | -9.19641 | -63.45084 | 2024-10-03 04:51:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 72523ef1-9403-3230-bce5-473ccb98f264 | -9.19147 | -63.44567 | 2024-10-03 04:51:00 | NPP-375D | ITAPUÃ DO OESTE | RONDÔNIA | Brasil | 1101104 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1feeab6a-9502-3d15-b244-4ec38ec79969 | -8.96387 | -63.61136 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7c53e42e-7aad-35d5-a362-2aa5b4ba0449 | -8.9631 | -63.61547 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6e673638-2348-3ba2-9eb4-d33b842e7773 | -8.95808 | -63.61023 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 77c56b4f-9e60-370e-ba7a-8fe2c7d27c8c | -8.77735 | -63.08319 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a4ba0b86-9b91-3f30-94e4-c963a5233b11 | -8.77662 | -63.08706 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6ee7862-9a85-38be-a1d0-175f4d773ea4 | -8.77526 | -63.08075 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4416ac60-689e-3fbe-9af6-b903bb9c8a3c | -8.77456 | -63.0846 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4d01fdc6-2f45-3333-bc48-0e55fe5a1668 | -8.62532 | -63.28894 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5289da0b-d37f-3c7d-93d8-91692e821eef | -8.62379 | -63.2897 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 50ecc42c-79ea-3084-9e64-28af328e01b6 | -8.61962 | -63.28785 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 7bc9c742-4be7-348d-a6e8-349b36f3c361 | -8.61809 | -63.28859 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 649a4525-f190-33b6-ab84-ea2f044567dd | -8.60147 | -63.12366 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f3bb0031-572c-3d3e-82b3-8a925fb1afe7 | -8.60075 | -63.12752 | 2024-10-03 04:51:00 | NPP-375D | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 7f99e151-84c3-300b-97ef-6c62c7f5a43f | -8.4665 | -62.65923 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 65224e0a-f14d-31b4-8412-273553187572 | -8.46234 | -62.65098 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 42e2547c-51fe-3b13-bd10-d34c1a243688 | -8.46168 | -62.65458 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 41cb8b86-ff96-3eee-9117-8219047243eb | -8.46101 | -62.6582 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3249c256-8f90-3b2d-9dbb-a181bb0cd31e | -8.46035 | -62.66181 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 3e393d8e-478b-3b8a-b8e4-e2face16c710 | -8.45968 | -62.6654 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e647bdc7-a286-31e6-bdaa-c09583b63119 | -8.39728 | -63.35783 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| c3bddaf3-9a6a-3da8-9b7b-11210a017db6 | -8.39728 | -63.35496 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8653c273-113a-38e4-a2f2-f703c979b530 | -8.39654 | -63.35904 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| b6066f43-a8a3-3491-ad6d-52da4c1d1474 | -8.39154 | -63.35668 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| a314ebeb-a25f-34ca-8e15-42d7df036f6c | -8.3908 | -63.35786 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5bc67c58-d580-3d3c-8271-25fc9960a25c | -8.39078 | -63.36072 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 2e131f05-786f-35c3-9ff0-99252bdb1805 | -8.39007 | -63.36191 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 4df8d37d-c287-3227-8ad2-0c760664cef1 | -8.38505 | -63.35675 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 570f7a69-d847-341e-ade3-e916893b9e97 | -8.24568 | -62.99117 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7a507d63-2974-3429-979e-95a33e69e15a | -8.24494 | -62.99506 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0da18652-5bcc-346e-8f2b-31e02e3221bc | -8.17464 | -62.84027 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 18ae0b04-dfad-321f-a869-7b9b44830467 | -9.77865 | -63.93997 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| ca228ea7-11ab-3107-bca5-51488a56b616 | -9.77787 | -63.94408 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| f1c3663d-93a2-3b26-a47f-ba7e4bfdc61a | -9.77202 | -63.94307 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 26e38914-8884-3c45-8875-592aa8f14cc0 | -9.77083 | -64.28964 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1383d81a-6363-39a8-b990-1bb4fa456af3 | -9.76489 | -64.2884 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b9ab8a54-376d-3670-a33e-3c25762976b3 | -9.76404 | -64.29282 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 6ae3931b-3cb8-34c9-9e0c-e02e660e82b8 | -9.75809 | -64.29161 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 4847681d-8fe3-30f9-9e20-5b30d94eaa64 | -9.75723 | -64.29605 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 33b39201-efae-3b4a-9621-8c3fef052883 | -9.75214 | -64.2904 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 6a317fe7-573f-3023-a083-7dcea441f6c1 | -9.75128 | -64.29482 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 82f8e697-f55b-32ca-a496-95f2a65391e9 | -9.73407 | -63.98358 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 12d8ca83-087b-3ff8-bf8d-c4401cf17f71 | -9.73328 | -63.98775 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 5ab6fe17-7924-3ef3-8761-337e8182b368 | -9.72604 | -64.23424 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| e24d3be6-9732-3cb4-b8b2-94a78fd6ca23 | -9.72515 | -64.23878 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 540e3732-c434-33f6-9d4d-80f321f8bb9d | -9.72298 | -64.23535 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| b407252c-985f-3436-b0ca-45d235dc1167 | -9.72211 | -64.23998 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| c83cd06d-4a64-3fcc-8ce2-894eb44f5a7d | -9.71797 | -64.2293 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4201e0dc-f208-31f6-bd66-a665ae40b4cf | -9.71706 | -64.23408 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9bb4c0fc-f192-33b2-926c-0dc2af6849a1 | -9.71618 | -64.23877 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 01bc34aa-e74a-3629-89c1-5d13fbd56d65 | -9.71112 | -64.23293 | 2024-10-03 04:51:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |


[Clique aqui para ver as próximas entradas](README137.md)
