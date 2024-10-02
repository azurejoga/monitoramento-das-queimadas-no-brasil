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

## Dados Diários - Página 124

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| e0d04486-f731-3455-a9ab-2c35cfac0089 | -17.19449 | -56.23127 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57591d73-b710-3c8d-a754-77fcb80bc58d | -17.19383 | -56.27759 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| f7f49e32-8b4c-33e0-91df-2d3dbc33fc5a | -17.19379 | -56.23536 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 73cd521d-6cec-369c-bf34-dcf02a79c337 | -17.19243 | -56.2858 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a2097a05-9264-38fd-b89c-6d27a4cdbb48 | -17.19171 | -56.26875 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| cd726ef3-4940-3a33-95cd-3798b1eaf1a7 | -17.19168 | -56.22654 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 786269f8-5d84-3de4-ba65-f621f56d650b | -17.19098 | -56.23064 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 61230e76-9821-3f49-9e7a-4ac92dc4e2af | -17.18677 | -56.213 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 5be78c48-6a56-36be-aca0-39d8fe514bdf | -17.18609 | -56.25926 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 7482681a-3f07-32a8-892e-b6e721239e76 | -17.18469 | -56.26745 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| b658eb0f-9abd-3666-b79d-d8b256d92206 | -17.18399 | -56.27155 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| fde81062-c3bc-3cc2-8ce3-8ea828fd6d2b | -17.18398 | -56.25043 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 4208dce2-da96-36ff-9ffb-92afa002deda | -17.18329 | -56.27565 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 2c5d9ee7-00dc-3ddb-9a86-b8fd37dc7fda | -17.18328 | -56.25452 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 1f6601be-92b5-39ac-9b79-dc16182f5778 | -17.18327 | -56.21235 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 57741aa0-76ed-307f-a567-a10e0cbe5664 | -17.18117 | -56.22461 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| d6f997bc-bb4e-3342-822f-b507ae9cd24a | -17.17766 | -56.22397 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a767406e-45a6-312f-be86-1ad477b79965 | -17.17626 | -56.21107 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| efc31ea2-91c6-3141-8ee2-3b75cd35e6b6 | -17.17206 | -56.2145 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 10264f03-9a23-3ed7-81bb-7535a160bd0b | -17.17135 | -56.2186 | 2024-10-02 04:51:00 | NOAA-21 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| bbae7ad7-2b27-345e-b34d-6a3580201683 | -19.5799 | -56.53076 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 78f22724-1516-301a-b672-706d388e6a07 | -19.57576 | -56.53414 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 0a239c59-c0a3-3a28-adb5-4cede43e256a | -20.04343 | -55.97246 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 75c444fc-64e8-3bdc-98cb-61aa5c677186 | -20.04148 | -55.98404 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8e3e9bf2-ab0c-3d10-a4ed-3a2d5dd19900 | -20.04134 | -55.96412 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| c611866c-f648-3c21-aefc-e80f752ab6e2 | -20.04084 | -55.9879 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 463a0239-8e7b-3e53-b53d-8512ce465518 | -20.04069 | -55.96798 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3fb1f6a9-8f23-31b5-bed5-b2cf5aa70d3a | -20.04004 | -55.97183 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 403611b9-98c4-3466-b2aa-afc63d964006 | -20.0394 | -55.97569 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cec754c7-bb0d-3cf6-94e7-abcd3a5a5f73 | -20.03875 | -55.97955 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 8665ea56-f33a-34da-9ef1-4b057d4a4875 | -20.0381 | -55.98341 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d6d733c8-51bc-3a68-97f3-d3416b928cf8 | -20.03731 | -55.96735 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| be1067f0-f5d6-337a-89e8-ad32a925afe8 | -20.03666 | -55.97121 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| aac84dd0-4ba4-3487-abe1-22f8baa5fa9b | -20.03601 | -55.97506 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2e1f3f1e-9de2-3c90-9d20-c36fdaa7f2a3 | -20.03536 | -55.97892 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e55ad251-0347-3bd5-83b4-ac31d9d49f82 | -20.03471 | -55.98278 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 8bb85de0-8707-378c-bf49-8890f0c147d8 | -20.03392 | -55.96672 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 9bc7f00f-465a-3498-9b9b-69f25e035708 | -20.03327 | -55.97058 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 5470935a-274b-35a5-9929-a73c52fcc59c | -20.03262 | -55.97443 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| cd382401-71c5-3539-ab0d-8000385bbbf9 | -20.03197 | -55.97829 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 35bf6dd5-cdcb-3fad-97a1-f9c2b3048939 | -20.03132 | -55.98215 | 2024-10-02 04:51:00 | NOAA-21 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 6a3414fc-404a-3b31-b081-baca30c096ce | -21.42674 | -57.24095 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| cacdfd71-12e7-3dcc-8a90-fabfd7822db4 | -21.42601 | -57.24521 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 5814c600-23e1-3dea-8aaf-cdbaa93ff3ec | -21.42327 | -57.2401 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| a4b8bbc9-75c6-30ca-ae08-2fe0d937fe84 | -21.42255 | -57.24435 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 35c96fce-697b-3efd-8e4a-109a949c1ec8 | -21.42181 | -57.24865 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 02fe3f6f-5347-3d78-b7ed-23c28939e043 | -21.41981 | -57.23926 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 66a4c296-e4b6-3280-83eb-d21c4e97b11d | -21.41833 | -57.24787 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| e394ad3a-1716-3fa3-9ec2-742c50b6d9f6 | -21.41706 | -57.23429 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 08e546be-414b-3ef3-a48a-8ffa1a747f7d | -21.41485 | -57.24713 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 79560caf-7cda-3340-9ff4-ae33210e2539 | -21.41358 | -57.23355 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| a7527a49-f220-3156-a6c3-952790bf150c | -21.41009 | -57.23286 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e2871a63-374b-3348-b281-a3f7a5e9ae1e | -21.40592 | -57.23617 | 2024-10-02 04:51:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 0d2b2bef-546c-3516-8aa4-a3d868025d8e | -19.11192 | -57.50379 | 2024-10-02 04:51:00 | NOAA-21 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| ed220e2b-cb1c-3348-996c-c4389f54ca8c | -19.11076 | -57.48934 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| dc56fb90-17aa-3cbf-b26f-60bcc8c52bf0 | -19.11 | -57.49358 | 2024-10-02 04:51:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.7 |
| bd47d478-df7d-36b0-b571-bf54224b876c | -17.05538 | -56.70702 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1aca7c76-8503-3d3b-9f71-7885dfca2c80 | -17.05466 | -56.71131 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e6fe9641-edf0-3f4d-b17a-3c4780d66604 | -17.05298 | -56.71023 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| e880d778-4361-3793-8f46-ad06b3bab4d1 | -17.05223 | -56.71452 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 4a1553e8-94ee-31ec-96b1-eb51cf570335 | -17.0518 | -56.70635 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| ab2b9f07-81a5-3953-819f-ebfa5e5f7ec5 | -17.05107 | -56.71064 | 2024-10-02 04:51:00 | NOAA-21 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 41a4ce72-ee33-3d8f-96e3-4228cd104527 | -17.42708 | -57.86663 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| ee2557c2-9be6-3d4a-8e0f-ff3c57fadf66 | -17.42417 | -57.86106 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 18fc1af6-1bc9-350f-93f7-9f82b60f8205 | -17.42038 | -57.86033 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| dc3f4b45-e5a7-3fbe-aa53-a7666493ad91 | -16.90645 | -57.70404 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 4c4becb1-4776-3d0b-8efc-eed8994e9d80 | -16.90353 | -57.69851 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 5c9a974f-3a77-3038-a307-4fc071d515b0 | -16.90266 | -57.70332 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| fae58a88-936f-3ce5-bf20-bab48fdc3196 | -16.90148 | -57.68818 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 74c7faaa-061f-3b4b-878a-c164cfed4bf3 | -16.90062 | -57.69299 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 166a9fd7-df42-30a8-9c66-191956a4b3d5 | -16.89975 | -57.6978 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| 5302f692-c4bc-3b50-a4c9-7629c9d28220 | -16.89888 | -57.70261 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.3 |
| e1ca206b-f80a-3ef7-9885-0d2062fd8f89 | -16.89857 | -57.68266 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| a35de268-637a-3f05-9275-667880e0ba17 | -16.8977 | -57.68746 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| e6b34bb2-ef0c-3210-a137-ad347ec6e476 | -16.89684 | -57.69226 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 961e6fd6-75fb-34ad-aef9-1645ddf6b245 | -16.89597 | -57.69707 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 2143cb6b-9b8d-3e30-af8e-d53c93762e0c | -16.8951 | -57.70188 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| c6fea07a-c038-3f83-9ee9-f8ef4662ab24 | -16.89479 | -57.68195 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.6 |
| ee6e48a8-7414-330a-b195-b87dbb72f6ff | -16.89392 | -57.68674 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 83dd9bdb-b616-3f1f-9051-afe5806271ea | -16.89305 | -57.69156 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 35.3 |
| 93991006-02a3-3b3a-8537-e36cd4d2c762 | -16.89219 | -57.69636 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| 79ce8917-7bce-3a75-a1d6-c7502fa242cb | -16.89132 | -57.70117 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.9 |
| eda31309-edf4-3736-a43f-e816fa6acaa9 | -16.89006 | -57.68772 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 4247a50b-bf62-3f0d-949b-451211bd0563 | -16.88927 | -57.69084 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 3ec5789f-1000-3ead-9607-75dd91c61280 | -16.88922 | -57.69255 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| a354ae86-01ba-3dc1-8269-bae659f10a0a | -16.8884 | -57.69564 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| ce59aaea-e741-3dbe-9159-fc73bc1ff497 | -16.88838 | -57.69737 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| e9f67e15-375c-375f-9cc4-8db09c5fd282 | -16.88754 | -57.70219 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 213325c8-ae9b-3d0b-8470-fc398025f9b3 | -16.88636 | -57.68531 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| a977896f-15e3-33d1-abbf-7151078e5f68 | -16.88628 | -57.687 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| 91d77f6c-1638-3497-aa5d-2a6e85dd1243 | -16.88549 | -57.69012 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 14.1 |
| 7c66556c-9ca7-30b7-bc17-8cad9b059241 | -16.88544 | -57.69182 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.8 |
| b05d79cb-e4bf-36bc-932f-4e0aee1dcf75 | -16.88462 | -57.69492 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| 1039b234-53a8-373c-8070-804021858350 | -16.8846 | -57.69664 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2f1ff6c0-2d3e-3be5-846e-977421e636b5 | -16.88258 | -57.68459 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| 0a83042e-2c52-3177-9565-9f992e1716a7 | -16.8825 | -57.68628 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| b003699c-e48a-3bde-b205-61b5bd01f41c | -16.88171 | -57.6894 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.0 |
| fcdd33be-2eed-3a6a-a9ef-a21878d57d10 | -16.88166 | -57.6911 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 8.1 |
| d96eeebd-3230-3ae4-9de3-709498957228 | -16.88084 | -57.69421 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| e4baab31-3437-30c8-95b7-4b5985aad911 | -16.88082 | -57.69592 | 2024-10-02 04:51:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |


[Clique aqui para ver as próximas entradas](README125.md)
