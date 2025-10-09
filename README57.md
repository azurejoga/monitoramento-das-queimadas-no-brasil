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

## Dados Diários - Página 57

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b1a8740b-e396-3701-96f9-361fc37092f5 | -17.26824 | -46.97844 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 11.7 |
| 04fef1a2-5aec-3d0d-9014-b264cc7293a3 | -17.93411 | -57.50908 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ae51e13b-eddd-38fe-af15-7ce6d7ea522b | -17.85522 | -57.6008 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 6ffcb6cd-8b53-3257-9a8b-cabab260f837 | -15.99096 | -50.99317 | 2025-10-09 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| acc8a463-5732-3422-a2ea-b36fe88eece1 | -15.92391 | -59.48207 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f2a4b52f-b1f2-3f36-98c5-9bc1576932bd | -17.82571 | -57.63292 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 59caf8a3-0b0b-3843-beb2-086e9cd97538 | -18.03462 | -57.51509 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 837533da-060e-3925-8600-82f67c1e6d51 | -18.02419 | -57.56327 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e2e6c138-e703-3840-ba74-e41436096903 | -18.07183 | -57.52961 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| bec306f4-e29b-37af-9773-39c306c83244 | -18.06246 | -57.54509 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d7ff6104-c7ec-3cf4-8ba1-a98944e75d72 | -17.21023 | -47.65423 | 2025-10-09 05:14:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 12.4 |
| e1f7f849-900d-3cf3-82fe-39bce02d2241 | -17.37421 | -46.89791 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a62d6971-f214-3cd0-a5dc-09e29863aaeb | -16.00242 | -59.54667 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d058afd4-a9fb-333c-bafb-eacd9bbc7f4a | -17.92773 | -57.50374 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 93af68c7-9102-3fce-8952-dcf1757cc422 | -17.82461 | -57.61593 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 8c73f7a0-99cb-30ff-85ba-bc63239c7f61 | -17.37815 | -46.89786 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 1268be78-3438-3c96-adaf-d26428cfa9fb | -17.84478 | -57.64823 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| e4a248d5-b9d2-3680-80a8-179e2566e892 | -17.91375 | -57.5017 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 62.8 |
| eeb4e1a5-7b4a-33b2-bcb6-d53bb6ae551a | -17.84603 | -57.59066 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 7b382a92-09ff-3ef8-ab1d-64045f93a9f4 | -17.82274 | -57.65349 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 848d5b03-53c5-3d9c-8fba-5ca4a804a0a7 | -18.0207 | -57.56273 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cd386895-7c36-3984-b35a-ea740a76af39 | -16.6047 | -58.1547 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| d4277bbe-eb16-3d9e-9920-45e004c4a43f | -17.26656 | -46.97635 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 6206e526-0ff9-3e4b-839d-96c6ccce0bf4 | -17.89082 | -57.6627 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ef91d540-1752-39eb-b71b-b101fdc5f0c0 | -17.82632 | -57.6287 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0c0143bd-c55d-370c-a8b8-f40deb839c1b | -17.85175 | -57.64912 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| f29336dd-b60b-3281-b956-dbf8ddb7a25b | -17.82403 | -57.61994 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.7 |
| da0fd9f7-8480-35f3-94d7-f36ef0f8de4c | -17.89139 | -57.65872 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| f89a81c4-d4c5-3d74-b306-6115edde5aa6 | -18.05498 | -57.5226 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 98ada795-150e-35dd-b630-62f2f991e30f | -15.9913 | -50.99033 | 2025-10-09 05:14:00 | NOAA-21 | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| ea45abe8-0614-3fc4-8b07-f3352f8bce46 | -19.47623 | -55.46829 | 2025-10-09 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 856a8285-3a1e-3425-b8ac-31b5a9c8a790 | -18.03815 | -57.56535 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 0be9dc8e-dc37-3627-b26a-ddffed8beb3e | -17.37474 | -46.89216 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 94fb7c96-98b5-3aaa-b182-0514b8e39b15 | -18.06188 | -57.54912 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 1ae49490-cbc5-3adf-88ac-f32771a42951 | -16.6979 | -47.59578 | 2025-10-09 05:14:00 | NOAA-21 | CRISTALINA | GOIÁS | Brasil | 5206206 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 0245f527-1048-35c1-a048-be907be560bd | -17.63371 | -47.21392 | 2025-10-09 05:14:00 | NOAA-21 | GUARDA-MOR | MINAS GERAIS | Brasil | 3128600 | 31 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 93155618-adf5-3327-a77b-885df1caa631 | -17.89889 | -57.65585 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 6449f033-323a-3ed5-a653-e3f74b4db8c4 | -17.37911 | -46.88668 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 678f0414-e882-3eaa-9103-d18ce0857901 | -17.90583 | -57.65692 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 8b8f49b5-f721-30a7-8d2b-f7406ea13da7 | -20.56146 | -54.65475 | 2025-10-09 05:14:00 | NOAA-21 | CAMPO GRANDE | MATO GROSSO DO SUL | Brasil | 5002704 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| de1764f9-0b8b-3d85-9d1c-8551c14079fa | -18.01595 | -57.49557 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 03a6afd5-95f0-3f27-8273-5ca769efb4c6 | -17.8413 | -57.64781 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7a8fe4ff-487c-3220-a319-07e9c7f45353 | -18.0253 | -57.50523 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d9558c60-becf-3e7c-b287-10bb1df30719 | -15.99856 | -59.54968 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 4fd5b905-a564-33e6-83a0-993b9c9a4f97 | -17.85471 | -57.57981 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 3f97f04c-b61e-31df-a1d2-dc3a5cb79123 | -17.82973 | -57.65417 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 233ffb94-eff1-3923-964e-0876318f1508 | -17.38628 | -46.88171 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d17a5f37-eb1e-3c95-b942-157845e68f99 | -18.02583 | -57.55185 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 9fc5c4b4-3406-3c79-91bb-6cbb7764d7ae | -16.00136 | -59.53189 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf89124b-4750-31bb-a298-d4502fc84d42 | -17.26938 | -46.96621 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.6 |
| c2da1aff-5e5c-3195-ab33-097ac8281b4f | -17.39532 | -46.88799 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.1 |
| fb5e4194-2ebd-37ce-94ce-6c33ac551122 | -17.83432 | -57.64698 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| cdd67f35-008c-3ced-87ac-ccd2798c3f4d | -15.28465 | -59.24109 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bc679b4d-02bf-3fa6-9dd7-94616b1f39cb | -17.83837 | -57.64351 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.6 |
| f0206a22-f0d2-330f-894b-490abdc23794 | -15.97603 | -59.5423 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| af954635-4f39-3b27-8a48-fc5e6fb4b9d6 | -17.83377 | -57.65078 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 7451971a-0256-302b-b4eb-9cf326d9fde8 | -18.03117 | -57.5643 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| fe1c653e-6cda-30c1-a9b8-bf05ee756df1 | -17.5271 | -46.7445 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 13.8 |
| e360ff39-73fc-351b-9601-bf9bb81951f6 | -19.4716 | -55.47306 | 2025-10-09 05:14:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 8030e8ac-e84b-34c7-9678-e235bc65ba70 | -17.94046 | -57.5395 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 33360b2a-3236-3b79-bad8-978e35c81567 | -18.06831 | -57.5292 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| c102e70d-2922-3cf4-b392-a896c2ff4a5e | -17.39301 | -46.88157 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c392d84f-85e6-3dea-86d8-af15768251c9 | -17.27318 | -46.97716 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 631fbed5-d73d-3a49-8b2f-9c6c6b592b20 | -17.39252 | -46.88721 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 233e56aa-b0c5-37be-8848-1bf86356f5ef | -17.92014 | -57.50697 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| ee1c9bcf-1451-30d6-a610-d03378dfe1f6 | -18.04161 | -57.51612 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 0021dcfd-fc50-36d7-948e-06b4c4294b9b | -18.02472 | -57.50937 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 4b9d823a-9b95-3e92-9f2b-c78c34c2d500 | -17.99411 | -57.48931 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.5 |
| e470da37-139f-3a5b-8eb7-9c5417dbc780 | -17.91664 | -57.50646 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 19.1 |
| e8e128a6-d978-32d1-9c07-9f2e8bbc37c6 | -17.92713 | -57.50799 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 1ab32072-8070-31a4-b48d-d5934eec5119 | -17.53632 | -46.75248 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 76bcf690-695e-3bad-976b-e8427642dd8d | -17.90179 | -57.66037 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9ae2e983-0694-3742-940c-8ccae9cbba46 | -17.92363 | -57.50747 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 27a98af4-ccd4-3545-aea3-2912eb532472 | -17.71225 | -56.77802 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 41e3d913-56f8-31b5-8f1e-67931d903a3d | -17.84534 | -57.64436 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 13300946-3cb0-3568-bf39-ef824983d546 | -17.85006 | -57.58738 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| d25e6b62-4a01-3134-ad71-ae7dc992cc08 | -17.88792 | -57.65815 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0b2996e0-7785-3b7a-ae6b-70b1d39b44fe | -18.24553 | -55.37844 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 6210c74b-3e9c-3f79-b9d0-571d614ea24f | -16.60077 | -58.15791 | 2025-10-09 05:14:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 020d3ba8-8e58-3a01-ac0e-8e897a79f3b6 | -18.05893 | -57.54483 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 33595dfc-3715-35b5-937c-7347eeec2250 | -17.52904 | -46.75805 | 2025-10-09 05:14:00 | NOAA-21 | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 10.1 |
| ba5f8d1b-b04b-3974-8fe3-18ae28adffe7 | -21.8748 | -56.14214 | 2025-10-09 05:14:00 | NOAA-21 | JARDIM | MATO GROSSO DO SUL | Brasil | 5005004 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8589311-fabe-3879-9e90-000b6f01e4ef | -18.0049 | -57.49792 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 6.7 |
| ec9b3d89-fdb7-3e6f-867c-9e8c98ea8959 | -17.21247 | -47.65881 | 2025-10-09 05:14:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 177a30a0-8bcd-3bba-a6af-6ba01f3bba8c | -18.02762 | -57.51405 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| b126e8b3-d6db-3fe0-bf44-4199d38f9463 | -17.21931 | -47.65421 | 2025-10-09 05:14:00 | NOAA-21 | IPAMERI | GOIÁS | Brasil | 5210109 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 02f3e114-59e8-3df2-80b6-e75e12b53dbb | -17.89832 | -57.65984 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 23e48732-52c2-3ba8-97c0-1459ebfe2d5c | -14.94681 | -59.42184 | 2025-10-09 05:14:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 04b54f49-0918-33bf-bb5f-f7066a1a25ba | -17.8223 | -57.60729 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 77273128-4b38-3b80-b62f-9bd4b157a41e | -16.00024 | -59.53902 | 2025-10-09 05:14:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e0673085-2eec-3e43-9601-76e688069f33 | -18.03522 | -57.56092 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| dbf6e26d-d499-333b-9181-0b2d6dd17f12 | -18.02821 | -57.50994 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 81c0138f-a34f-3093-a4bb-b66367d42fbd | -17.83489 | -57.64304 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 38cb5f2f-591b-3574-9e8f-64be7f81dbe1 | -18.04041 | -57.52454 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.3 |
| cadcf7ba-4883-3da8-95a2-a6f8f88bc923 | -17.98415 | -57.50867 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 83acdd1f-0a7e-3e24-aa74-ef84871e83ca | -17.83781 | -57.64739 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.0 |
| 7ac9172f-601a-3c6e-9915-16e68d56eba4 | -17.84661 | -57.58665 | 2025-10-09 05:14:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.8 |
| 2fe20da1-e9a8-38ce-87f9-18dc150ae97b | -7.50022 | -42.72742 | 2025-10-09 05:29:00 | AQUA_M-M | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 34.7 |
| 8b5cf7dc-346b-323c-8c56-58d70d4c5d19 | -9.61432 | -40.32796 | 2025-10-09 05:29:00 | AQUA_M-M | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 1a7dd8fb-f36f-30e1-9409-ddc220b3111f | -7.80192 | -44.19935 | 2025-10-09 05:29:00 | AQUA_M-M | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 17.1 |


[Clique aqui para ver as próximas entradas](README58.md)
