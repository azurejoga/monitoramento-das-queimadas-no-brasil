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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 22489da4-d143-3a65-80e5-b3f149ac08a1 | -18.85231 | -53.62486 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2fe95506-76df-348e-b84c-846e25fbef1d | -20.47597 | -53.67644 | 2025-05-27 04:53:00 | NOAA-20 | RIBAS DO RIO PARDO | MATO GROSSO DO SUL | Brasil | 5007109 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 47b76654-6db1-348f-8b2e-3776bbec4ab6 | -18.86026 | -53.61833 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| acd53414-af8f-36c7-a7f1-af1d64b89109 | -21.26641 | -48.6147 | 2025-05-27 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.9 |
| c9e4d6d7-0e2e-3c3c-8ece-548e51565d06 | -18.83582 | -53.61818 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3a309bbd-bebc-3ee8-9dbe-1794dc90ae8b | -18.83521 | -53.59835 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 282288f8-e54d-3c90-bbd0-1f3bfa387e8a | -18.85059 | -53.61279 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| 57dea8e9-0e02-3a3a-9ffb-d58dd779f945 | -19.17298 | -57.54356 | 2025-05-27 04:53:00 | NOAA-20 | LADÁRIO | MATO GROSSO DO SUL | Brasil | 5005202 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| c2130ec1-f8a3-328e-b1c8-0085dc151f18 | -18.84661 | -53.61605 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 5deec9b9-1872-3c44-b1ad-5f3c67a1f99e | -18.84887 | -53.60063 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 45f3182f-0369-341e-988d-c47b2345e7d1 | -21.23443 | -54.60535 | 2025-05-27 04:53:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 42cde0a4-5d47-308e-ab5a-71f3bddc0ffe | -18.8597 | -53.62217 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 42e2b71d-2e52-3441-b843-231eb407effe | -21.97749 | -57.59119 | 2025-05-27 04:53:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| e29586ba-168b-3d81-94b4-e3f563e4df46 | -24.2973 | -49.9369 | 2025-05-27 04:53:00 | NOAA-20 | JAGUARIAÍVA | PARANÁ | Brasil | 4112009 | 41 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 089897db-a6aa-3022-8d2c-dd122fc472af | -18.84946 | -53.62047 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 23dceaa3-5bea-3410-aecf-e33c212ee5c6 | -21.24524 | -56.14915 | 2025-05-27 04:53:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5dc12220-3d70-3c5e-8f3a-14380725151d | -18.84546 | -53.60004 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 769b14b9-c298-36c5-a393-9e2c5d2c1a31 | -18.84261 | -53.59563 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| f01ab9e8-c8c5-34ec-8c5b-9061cbc66001 | -18.85456 | -53.60951 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| c7ce3597-8c91-3750-bf2a-a0defc9d1462 | -21.23838 | -54.60209 | 2025-05-27 04:53:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| b0a32c3b-b415-37b7-b713-a890b7c7565a | -18.83465 | -53.60221 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 317a8f6f-5978-3f42-a262-0c696371c4c5 | -19.02279 | -57.62106 | 2025-05-27 04:53:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 24eb2d3f-e2fe-3510-a98b-3657bb0c4300 | -18.85685 | -53.61776 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| fdf1325c-e105-3958-b5c9-9c0479d3d298 | -18.86139 | -53.61063 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d33e5a9f-5c7e-39a7-a335-757745517fc4 | -18.8432 | -53.61548 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| 3f1c376a-b824-39ac-bf82-0028c8bade0e | -21.22061 | -48.60391 | 2025-05-27 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 67af4c6b-2cae-3bcd-b42f-4095dd6b68f7 | -19.12508 | -51.9609 | 2025-05-27 04:53:00 | NOAA-20 | CASSILÂNDIA | MATO GROSSO DO SUL | Brasil | 5002902 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 04256b8c-2581-3326-b779-c4f40a956d17 | -18.83409 | -53.60606 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0aae9413-4e8f-3821-8eb7-c95a46b8d586 | -18.85798 | -53.61007 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 883075c4-be20-3732-bb10-4ec3df434620 | -19.42491 | -54.77911 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1530cfc3-bdc6-3f53-8e93-b97401318248 | -18.84433 | -53.60777 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| d1657fa2-a21a-3c36-b65a-6d714d0b50ed | -18.84605 | -53.6199 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 56e44b30-cc1f-3d0f-8240-300367fe0e33 | -18.84204 | -53.59948 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bb7011cd-b9b8-3e32-bd23-8f15e25a8c44 | -21.22005 | -48.60895 | 2025-05-27 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 06c8436e-5de7-3d29-95cc-7e489b9e6b40 | -18.84718 | -53.6122 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 9.9 |
| be4bd943-410f-3217-add8-8c132c3b1cbe | -22.2122 | -56.19731 | 2025-05-27 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ebfbab7d-eb4b-3162-a699-ec9db0f19f37 | -18.83979 | -53.61491 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a3fe958b-06a7-3ccf-9204-1df1f8fc515e | -18.83867 | -53.6226 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0b7f5691-26e3-3a4d-b897-21e943093ded | -18.85516 | -53.62926 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| fabf6300-51ae-3da5-9ec4-bb23c483817f | -18.85288 | -53.62103 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 82.9 |
| f112e6ba-2af5-3851-8c0b-498d5b562c73 | -18.854 | -53.61336 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 0cd351c0-6940-3cf8-82b1-19f419f325dd | -18.85175 | -53.62869 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.4 |
| eb566aeb-23b2-3e66-9026-7bfd952a0bc5 | -18.83863 | -53.59893 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 4013bc73-84f6-32f5-ba12-735e690e5c02 | -18.85741 | -53.61393 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.9 |
| d2b1df44-52e0-3c3d-8cbb-459df3414341 | -18.86312 | -53.62272 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 3386ccc0-8ff8-3a73-8bd2-5f0e14d27347 | -19.43548 | -54.7771 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| c730d7bb-9fbb-3c01-96a7-b5e4f57fc80d | -18.84831 | -53.60448 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 72684b6e-fb68-348d-8ef4-6bfa7e2119d7 | -19.43492 | -54.7808 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 6aab7c46-99ec-38f0-a2e2-035cdd74367e | -18.85858 | -53.62983 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 714b95f1-72f1-3a94-a577-34dd6d38b726 | -18.86083 | -53.61449 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d2f2c8a1-301f-3fee-920e-bb5bd9647daf | -22.21493 | -56.20163 | 2025-05-27 04:53:00 | NOAA-20 | ANTÔNIO JOÃO | MATO GROSSO DO SUL | Brasil | 5000906 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9b65a038-7f17-370a-b720-79dfdb447f98 | -18.84602 | -53.59619 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 5.3 |
| b7069ccd-97f6-313a-b629-d4ae3595775c | -18.83694 | -53.61049 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 6a6ff513-482f-35a5-b694-d401bac3e0ce | -22.03926 | -56.81305 | 2025-05-27 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a5b77eb4-1d8f-3706-b145-e1bbe0fd2d26 | -18.83923 | -53.61875 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| d780e509-db12-36b2-8ec3-d5fc5bcb0203 | -22.03866 | -56.81677 | 2025-05-27 04:53:00 | NOAA-20 | BELA VISTA | MATO GROSSO DO SUL | Brasil | 5002100 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bc74cc4d-9bfb-3a07-8ee5-6da4786c8d11 | -21.26179 | -48.61401 | 2025-05-27 04:53:00 | NOAA-20 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 6f987a43-c986-38d4-a923-04e8655b0ebb | -18.86255 | -53.62656 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2b11ab5d-c330-3717-b7e3-be6214795a05 | -20.81594 | -54.95177 | 2025-05-27 04:53:00 | NOAA-20 | SIDROLÂNDIA | MATO GROSSO DO SUL | Brasil | 5007901 | 50 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d0ffe6f5-852e-38c2-9948-63fbe4baa3f2 | -18.83919 | -53.59506 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 6.6 |
| 23a5342f-1724-3782-87d7-d09deab66124 | -18.84148 | -53.60334 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| b24ed336-cb08-38f5-9e3e-3826156f4427 | -18.84489 | -53.60391 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 1a29727e-124e-35e1-b2d9-8b956fc506c6 | -22.15971 | -55.2769 | 2025-05-27 04:53:00 | NOAA-20 | DOURADOS | MATO GROSSO DO SUL | Brasil | 5003702 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| afe4489d-b92c-3c18-97c5-d58d46597699 | -18.83807 | -53.60278 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 01c1abb0-170d-3ec2-903f-94d11de292ef | -19.42825 | -54.77968 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 57854022-a633-3d97-8353-9e0d342b9209 | -19.43882 | -54.77766 | 2025-05-27 04:53:00 | NOAA-20 | SÃO GABRIEL DO OESTE | MATO GROSSO DO SUL | Brasil | 5007695 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3cb73acc-47a2-36ac-9f3c-8d45e419444e | -18.84264 | -53.61933 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 12.9 |
| a7fda409-4df1-365e-8fa1-9d481e9b3117 | -18.84834 | -53.62814 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a4785c7f-8582-31c7-af4d-a419784db4fd | -18.86424 | -53.61503 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 65e3e823-2a61-35bf-adb2-3a7a7207e84f | -18.84092 | -53.6072 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 56b6c322-14a3-3447-a911-59f8889e11f4 | -20.60872 | -55.70462 | 2025-05-27 04:53:00 | NOAA-20 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 5e57dc36-ed13-3bc2-b130-6cd661f538ff | -18.8557 | -53.60178 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c2878b57-2dfb-3bdb-9bf3-1cdc815e1776 | -18.85513 | -53.60565 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 248251c9-7274-3632-a690-a5f07d37b998 | -18.84035 | -53.61105 | 2025-05-27 04:53:00 | NOAA-20 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 19.4 |
| 1cd04bbc-1360-32a9-829a-0705f44a87ca | -23.60204 | -54.76189 | 2025-05-27 04:53:00 | NOAA-20 | TACURU | MATO GROSSO DO SUL | Brasil | 5007950 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| e29eb79c-414a-345a-b5c7-54fa4be691c3 | -18.8284 | -53.6067 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 83.1 |
| 1102d588-9c5b-3f17-b0ba-354861b594ff | -18.8679 | -53.6218 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 178.8 |
| 4b9d3011-c79a-3800-9f47-35957ce657e2 | -18.8484 | -53.6035 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 335.8 |
| 9abe81da-8f4d-3d45-ae4e-175571d85617 | -15.8955 | -43.4523 | 2025-05-27 05:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 67.0 |
| 61f4ce5d-7774-3b53-bcd5-1e5c1f6dbe70 | -15.8757 | -43.4566 | 2025-05-27 05:00:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 59.0 |
| a0b9b7dd-b0c3-39e9-b3f1-aa6f0c5beef2 | -18.8479 | -53.6251 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 335.2 |
| b46b028f-88b7-3ec7-897b-04d15f4c26cd | -18.8684 | -53.6003 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 156.7 |
| 9780700b-3770-3d56-a38e-f17a1937e960 | -18.8488 | -53.582 | 2025-05-27 05:00:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.3 |
| 017b4047-eb58-333d-8d27-8836e9277aab | -7.20633 | -43.12062 | 2025-05-27 05:01:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 21.2 |
| 31bc40ee-5c72-375c-b7e8-d39152eb19ed | -6.22093 | -43.34653 | 2025-05-27 05:01:00 | AQUA_M-M | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 24.1 |
| 08aaeabd-4dc0-3147-9835-7c3f57df29e5 | -7.22293 | -43.10165 | 2025-05-27 05:01:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 27.3 |
| 09705a5e-a946-32fc-ac70-6914b8f737f2 | -7.19667 | -43.09747 | 2025-05-27 05:01:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 28.5 |
| 79e040ee-61d3-3ddc-9bf2-3fe63c051ae1 | -7.19319 | -43.11849 | 2025-05-27 05:01:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 33.7 |
| 854c552d-4ba9-3997-82a4-2ba9b0266873 | -15.87733 | -43.44208 | 2025-05-27 05:04:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 17.4 |
| f0d0b000-49ac-3ea7-a38d-60601f3fe032 | -15.88535 | -43.45063 | 2025-05-27 05:04:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 127.3 |
| 49469fdb-f8f2-3239-9822-fd8cb5096345 | -15.87461 | -43.45804 | 2025-05-27 05:04:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 1a4dca22-aada-3b62-99f5-6a461fc281d5 | -15.88254 | -43.46651 | 2025-05-27 05:04:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 18.5 |
| 959ebcdd-abdf-3188-96fb-154f2842e815 | -18.8284 | -53.6067 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 63.1 |
| 4a78e6d9-35af-3100-94d9-1c9f02b693a6 | -18.8484 | -53.6035 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 277.9 |
| 1569d85a-1ae9-3662-aed4-b7bf39c6b5e4 | -18.8488 | -53.582 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 56.0 |
| 104cffdf-cb4f-358a-86a6-bb90a14745e7 | -15.8955 | -43.4523 | 2025-05-27 05:10:00 | GOES-19 | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 75.3 |
| b5b58192-0cc7-33ed-9e81-ff2a300d3352 | -18.8679 | -53.6218 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 172.3 |
| 3d93269e-04a6-36d2-a146-2841f3b6e25e | -18.8479 | -53.6251 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 230.2 |
| 361f3bcf-ff8a-35aa-8ca4-1a149fd37b74 | -18.8684 | -53.6003 | 2025-05-27 05:10:00 | GOES-19 | FIGUEIRÃO | MATO GROSSO DO SUL | Brasil | 5003900 | 50 | 33 | nan | nan | nan | Cerrado | 179.8 |
| 5037d962-3d03-3b84-a813-8b56e6ed8d66 | -22.439 | -48.4226 | 2025-05-27 05:20:00 | GOES-19 | MINEIROS DO TIETÊ | SÃO PAULO | Brasil | 3529807 | 35 | 33 | nan | nan | nan | Cerrado | 67.9 |


[Clique aqui para ver as próximas entradas](README19.md)
