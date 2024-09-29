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

## Dados Diários - Página 68

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e3d23c2c-4db6-37e0-945a-d6f81e13235f | -11.63593 | -65.01013 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e318cfe-2ce8-3d15-8a85-e51981e47637 | -11.63312 | -65.00597 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4b40e077-1f6d-34d9-a4f2-330a6f5587a8 | -11.63257 | -65.00961 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7ea43d25-fd08-34ce-a9be-b07f620eb607 | -11.63202 | -65.01324 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c063a4e2-bf81-3686-830a-3b5939e49b87 | -11.62975 | -65.00544 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4e5fa9da-5409-3ff5-b28e-94e1aa8c3b3a | -11.6292 | -65.00907 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1b4a8bb5-ce5a-3236-8c44-0878b8aea87c | -11.62638 | -65.00491 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 4b6c7388-82c5-33e0-a823-e1761ce1d7bc | -11.62583 | -65.00855 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 8d031cfa-587f-320e-853a-08ff4ce1a5c8 | -11.61855 | -65.01115 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9deac221-fbee-3858-a4a0-e94849f30a0e | -11.61518 | -65.01063 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0fea380b-b1aa-34b6-a083-77386cb2d009 | -11.61182 | -65.0101 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ae81106f-924a-3145-a642-bd45018a4b11 | -11.60681 | -65.02052 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2f6fa3b2-eb55-30b4-8038-abf9c8014491 | -11.60591 | -65.01344 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9cc6f6e0-9b6b-35c5-928a-9379e3f46ac4 | -11.60535 | -65.01708 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0280d153-3a5e-3d26-83f2-bebca32d617b | -11.60479 | -65.02073 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 528fc881-2e7b-3966-a27e-128248ceb4a0 | -11.60424 | -65.02436 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| af3013c9-dc89-3315-85c5-d398006abfb2 | -11.60087 | -65.02383 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8497ef27-39fa-3b21-ae74-d138a63b077a | -11.60032 | -65.02747 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 78de015a-7067-3d87-98bb-1b7c8f440f75 | -11.5964 | -65.03058 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a4b0950b-a270-3ae6-a847-ea0603af36c2 | -11.29346 | -65.27509 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| c1670885-1f7e-39a3-a8f3-81d490bee91f | -11.29067 | -65.27099 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d23918b0-c347-3324-8ea5-d6b8b7487520 | -11.29012 | -65.27457 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| bc6f42e0-ff1a-3cdb-82af-dde07ce43d33 | -11.28958 | -65.27814 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 2379c845-5aab-3133-944e-459fffce40f6 | -11.28678 | -65.27404 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3e36fa1c-5e73-3167-9617-9da52f87722b | -11.28624 | -65.27761 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e1de6346-cfe1-3053-8153-d4b9253cfaf1 | -11.28569 | -65.28119 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 48a7481a-500e-3635-9d76-5037545208fc | -11.23909 | -64.96406 | 2024-09-29 05:44:00 | NOAA-21 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d31e3bea-de3c-3869-969b-19746d071368 | -10.80866 | -69.67049 | 2024-09-29 05:44:00 | NOAA-21 | BRASILÉIA | ACRE | Brasil | 1200104 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| da66726c-8f7f-33a6-ad44-f7d401e95d3b | -7.91324 | -70.91873 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 786f523e-5677-3c5f-bcbf-2837caf37f28 | -6.67153 | -69.95604 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 81bd8724-d3b9-31ed-8935-a257f31570c1 | -6.67152 | -69.95386 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 38e7198e-51fc-35c9-9761-11a7e0ec26de | -6.66762 | -69.9554 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f7d0f251-e567-3b5a-83ec-4745e8621525 | -6.6676 | -69.95322 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 9e322aed-c8be-3144-9ee0-93e58dea0c16 | -6.66679 | -69.95821 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 79758c57-1dca-39a2-8953-977ec4184b61 | -6.66677 | -69.96037 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 65786017-20c3-3d39-b83f-270d02b32126 | -6.66597 | -69.96319 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 83ea8530-dd1f-38a5-89e9-1f5e650fb473 | -6.66532 | -69.94259 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 408af611-ba74-35a3-89ae-62e6b5d22909 | -6.66451 | -69.94758 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 9d9653a5-a341-39e6-af71-bb1e565b0b37 | -6.66369 | -69.95256 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 4ecb0b72-f237-395a-b3ec-7c75c8c8f5b0 | -6.66288 | -69.95754 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 5755c2a3-8dcf-3486-8a6f-d3f0ee7de8cb | -6.66142 | -69.94194 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| fee4238a-2708-3fff-9bcf-4e8330bd0968 | -6.6606 | -69.94692 | 2024-09-29 05:44:00 | NOAA-21 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e8647f37-e27a-3aa0-babe-292f0d69b5a1 | -8.10341 | -70.63906 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 97344935-8de3-3ffe-8405-a15a3e6f7fa8 | -8.08925 | -70.62587 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f054ef3d-f0d7-3ef1-a585-cf2d80141fa8 | -8.08864 | -70.62937 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 18f9e384-2421-3759-9cfb-059818956103 | -8.08682 | -70.628 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6c90aef0-027d-3752-bf06-79faf5ed8e8c | -8.0505 | -70.57538 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2277c6dd-db7c-35f2-a232-2ee35f7b4567 | -8.04992 | -70.57883 | 2024-09-29 05:44:00 | NOAA-21 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0a1407fc-1285-303b-9512-66eb7b4ec8ef | -16.4306 | -53.95138 | 2024-09-29 05:46:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 239dd438-fb2a-3171-97f5-f756ac36d680 | -16.42997 | -53.95784 | 2024-09-29 05:46:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 5.9 |
| eb0fb2f1-c1b7-3a8a-b79b-e2fa050093d9 | -16.42368 | -53.95058 | 2024-09-29 05:46:00 | NOAA-21 | GUIRATINGA | MATO GROSSO | Brasil | 5104203 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 884cd53f-15bc-39c2-8cf4-e83465eb811c | -19.98042 | -55.49439 | 2024-09-29 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 41662f34-82af-35cb-98a8-7d91ea64e4b8 | -19.98003 | -55.49903 | 2024-09-29 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 3c3e658a-21a5-3068-a1a5-51686941457d | -19.97968 | -55.50317 | 2024-09-29 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 4.9 |
| d4ce2438-d945-3f10-b86a-4805c1cbfbea | -19.97928 | -55.508 | 2024-09-29 05:46:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 13f13c48-53e5-363b-b8f9-b3e43a7ed8c4 | -22.17229 | -56.04388 | 2024-09-29 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 604b4740-a73b-3902-bff0-6b3a464cb93f | -22.16663 | -56.03254 | 2024-09-29 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.2 |
| b31add5f-1c2d-3e2c-8c9e-07c0c2b638eb | -22.16621 | -56.03792 | 2024-09-29 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.2 |
| ed781232-b555-3b26-b30e-984e05f9e627 | -22.16579 | -56.04325 | 2024-09-29 05:46:00 | NOAA-21 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 2647456d-cfe7-3a54-b612-d06e6ed6f7ed | -16.14143 | -55.43053 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| c8cf1114-d170-36c2-acc6-67e9c92a3d99 | -16.14104 | -55.43459 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 0c0d5f08-f15d-36c4-9546-3491c8b29a20 | -16.1382 | -55.43216 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 6591b4a9-67e8-3abf-9868-cee7e57e3daf | -16.13777 | -55.43629 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 79c3911a-268d-3715-98d9-7be05e1ec78e | -16.13731 | -55.44075 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c9077021-f093-3e42-b362-d3b78b6640c1 | -16.13433 | -55.43787 | 2024-09-29 05:46:00 | NOAA-21 | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2c34c164-7bf2-3dbf-94e7-15603ab52b18 | -17.25449 | -56.44388 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| ba23350f-2b8e-31df-be8d-6daa4cb9e9ed | -17.03298 | -56.10493 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 8d5e88be-c7e7-3c4a-a3f7-66ad9d8681e2 | -17.0324 | -56.10743 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 984bd6fb-b424-333d-9c2d-a9d27d7185dd | -17.02731 | -56.09932 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| a73c2a0c-3723-3bbc-964f-8e22601c4f74 | -17.02685 | -56.10419 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 737ff82c-beb7-3c1e-ba8e-7cf51af1381f | -17.02677 | -56.10186 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fad13c91-71ce-30a6-928f-6d281bf32a4f | -17.01987 | -56.16949 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 7f226192-d082-3f07-9986-6a8e0b8e0325 | -17.0143 | -56.17128 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 36114987-48d6-3ff0-9708-bbd4dc279d1d | -17.01384 | -56.17604 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| a8ecff21-6c48-3ef0-b1e4-8b87dfa97569 | -17.01328 | -56.17361 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.5 |
| 3aff80ac-44c5-3f92-b00a-d368649731dc | -17.00107 | -56.17218 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 9eefcb81-e13b-395a-a63d-1960c5713cdf | -16.99708 | -56.08852 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 96916621-dda7-3041-8a3e-6dddbcc01ef7 | -16.99545 | -56.16666 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| f6f67a69-4b26-3614-85a6-a958113c5810 | -16.99497 | -56.17144 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 55f3042b-dcce-3f68-9141-9f93f8663519 | -16.99224 | -56.13696 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c6c6a3ae-a23a-3acb-a818-fec852f7421e | -16.99128 | -56.1466 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| f4d2ebc3-4bc1-372c-8827-f2eaa7357788 | -16.99095 | -56.0878 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 241a427d-eb93-3152-b9c0-d9b672f31981 | -16.99031 | -56.15629 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 70d7bb79-98c8-38fe-a349-09c40812922d | -16.98983 | -56.16114 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 88cfc71e-c8df-3038-87a0-e1d4286891ed | -16.98935 | -56.16593 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 5dfeb6b1-0d91-36c1-aeb9-f705194cec56 | -16.98887 | -56.1707 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 7.6 |
| 04984044-721a-3163-a3e1-e9c52f484e38 | -16.98709 | -56.12659 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| 26acde63-8df4-3427-9e0c-e31f44e95405 | -16.98613 | -56.13625 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 2992f6f6-4a0d-3ddd-ba49-71f0f33db2ce | -16.98421 | -56.15556 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 5b907888-3d4d-372a-bcaa-325f57f230bf | -16.98372 | -56.16039 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 28433273-81b1-3f81-8447-98bc1c39d295 | -16.97676 | -56.10579 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| f1ffcde6-38bd-3f59-8db3-b68e04c48dac | -16.97628 | -56.11063 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 038d35c6-1f28-304f-ba96-56e5286ebff4 | -17.1237 | -56.18926 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 782f54a7-cdb7-3d78-91f9-84d033b10e5e | -17.12242 | -56.20855 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 2c269d46-b7c9-3af5-9af4-ee40e3e04a83 | -17.12196 | -56.21338 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 8.9 |
| 9889e009-d90c-311f-9bb1-d9f57bb078a6 | -17.12175 | -56.20839 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| 53299dab-c90a-3d10-9e55-d9af694fe55e | -17.12126 | -56.21321 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| c5fa3dd0-21ce-3b1a-8f00-06fef712ee09 | -17.12078 | -56.21796 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| f8b52077-cc42-37f8-8993-7605b159ebf9 | -17.1195 | -56.17411 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| 4229ea77-5517-3c3c-b305-48d45bb2139d | -17.11906 | -56.17403 | 2024-09-29 05:46:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 5.6 |


[Clique aqui para ver as próximas entradas](README69.md)
