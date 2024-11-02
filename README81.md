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

## Dados Diários - Página 81

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 29260d7c-9cb5-38a0-9085-26d29247a67d | -2.56075 | -53.96964 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc80eacb-a275-32a6-b756-7349b5bf5af0 | -2.55851 | -53.96214 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c68a3ada-ea5e-3a6b-8bd9-6435cf7f1ace | -2.55841 | -54.00554 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| bfb4369c-2fbd-3d98-91e6-89162b93ec53 | -2.55787 | -54.00903 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 160b9ebe-08fd-327f-a4c2-0c649e18db70 | -2.55743 | -53.96911 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1943607a-96ec-30fa-9708-c428f8fc6893 | -2.5553 | -54.00453 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| b5bd8707-6d97-3765-baa3-675cebad5c20 | -2.55476 | -54.00801 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9746e8e7-6dfd-3124-bd22-1ae8b736aa0a | -2.55198 | -54.00401 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 2fe75c84-024e-31c3-85e0-997d2e6e3ac7 | -2.55143 | -54.0075 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8c186543-99d5-356b-b184-53b2c88b947f | -2.54865 | -54.00351 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 775ffcbe-fc0e-34a2-be90-58f3aa8db093 | -2.54479 | -54.00647 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f59756a-639a-3d91-bda0-5c7d0110daf6 | -2.54201 | -54.00246 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 496341df-62f2-3939-a114-992d63933904 | -2.54147 | -54.00593 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6db2341c-a242-32e2-8066-3489ba8443a8 | -2.53674 | -54.07992 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 55c28d74-4374-33da-9018-d153b7a614fb | -2.53342 | -54.0794 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f7359ad0-9926-3baa-9ed8-0e617344b6ca | -3.1098 | -54.17957 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4ee3762e-e1ad-38d1-98ca-44201ce18b0b | -3.10208 | -54.18551 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b381760d-07f5-3eed-93d6-b2ced93818c0 | -3.09822 | -54.18849 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fcd04fe0-fc4b-3d57-9e73-97a6669b2e27 | -3.08151 | -54.16451 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d85c6f3b-72c8-3ae4-9019-1865abf94de2 | -3.08097 | -54.168 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 353cce84-7d1d-3583-83c2-123cf9d26949 | -3.07819 | -54.16399 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 46b08382-1896-3af1-83e5-ee6ce60d91ad | -3.07765 | -54.16749 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| a6163f34-bb53-3947-a163-4478ee500a8a | -3.07477 | -54.16366 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 89a7699d-d49b-3db2-bfb7-398fe4ceeb73 | -3.07422 | -54.16715 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e75e9a15-fb67-310d-a1df-1f8ab3c5b705 | -3.07144 | -54.16316 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| f1cbe2ce-2392-392b-8045-6f99cdd67d9f | -3.0709 | -54.16665 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| e328a224-d587-3df7-850a-cc568cbd4350 | -3.06812 | -54.16265 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 60076ab9-9a64-3cc3-aeb4-af022e0045df | -3.06758 | -54.16614 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e46a156c-e826-3216-a3c4-271ffbb37ba8 | -3.06703 | -54.16962 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| e4b36377-ebe0-3c98-9859-453943774aae | -3.0648 | -54.16215 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a81dd853-2c21-3495-b2cf-96e21a53ecfa | -3.06426 | -54.16563 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| b5a47e70-4924-3ec1-a59c-e82ba57fc683 | -3.05043 | -54.16707 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 32b7669e-bebb-373e-9dfa-9e302b3caa7b | -3.04989 | -54.17055 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2d881cdc-2d41-39cd-8964-c530a446f106 | -3.04657 | -54.17003 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2394ea5f-3e42-3422-860c-88871f9955cf | -3.04602 | -54.17352 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9167058c-4918-3bb9-adc1-e16db2a54a1e | -2.99593 | -54.10161 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cf321db7-c1fc-3c0d-adcd-06ab9f2f9241 | -2.9632 | -54.2035 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 65ace068-f0a4-3606-bdc5-5b3cf7b6d593 | -2.9578 | -54.08504 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8ad6fc7f-96e1-36f0-b3bb-52bb9828c84f | -2.95726 | -54.08852 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e742597c-c47f-37e1-bcba-744ea600bf07 | -2.95129 | -54.12683 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 048d27a9-0271-33a5-8d09-98cb2a6d17c2 | -2.95103 | -54.21579 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d602ab2c-df8e-3bee-b365-37072c1f5abb | -2.94873 | -54.18699 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 597a02b1-8cf5-38fb-b699-909c268c33ba | -2.94818 | -54.19048 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ca12d2bd-946a-399f-814b-0e57cbb9de73 | -2.94797 | -54.12633 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e18b54b2-98f3-3f77-82ef-d7c5aebda51d | -2.94602 | -54.20438 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 599b28fd-454f-3f84-9453-67e9f8fd73ff | -2.76903 | -54.07335 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| da9f2682-d55f-34f5-a87e-0b20ee314ef9 | -2.75866 | -54.09671 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c82ac2bb-988f-323b-93c3-783b50d3700a | -2.7449 | -54.11953 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c8cc77f0-f555-3292-967b-16c8f748a938 | -2.74382 | -54.12649 | 2024-11-02 05:04:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| c8971fe0-b61c-3a4a-8c4c-ff9f29d1370a | -2.74212 | -54.11555 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ea3084eb-1f6e-3ace-9c48-ea25ee49873f | -2.74158 | -54.11903 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f858a9b8-c3ad-3bdc-96e3-7e33b3063c88 | -2.74104 | -54.1225 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c968d42a-1676-3333-8fe9-ae56488e36a3 | -2.73772 | -54.12199 | 2024-11-02 05:04:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c9bb40a2-d2e7-35bd-a6cc-66b971824da7 | -3.13987 | -53.68011 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| f845c930-392e-3695-926b-f0d780ea5974 | -3.13651 | -53.67959 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 96b86e08-98cb-3ebe-a1f0-d9ae6965620b | -3.117 | -53.71674 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f719a3d6-41f8-3728-9b6a-240d47f1f0ca | -3.11645 | -53.7203 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f8514c37-32a0-32c6-b5e4-96d2300ea8f9 | -3.11309 | -53.71978 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 98f48db3-f57f-3324-86a0-b6853e80ed80 | -3.11254 | -53.72333 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6280c871-48f1-3bb2-9f9d-95251c6ff1b2 | -3.10694 | -53.71519 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b8348270-cb6b-30fb-992a-517861926cd6 | -3.10358 | -53.71468 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 6a8a8f98-997a-3a1c-a85a-5135d450f336 | -3.10023 | -53.71416 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0cffc6bb-5882-3bb1-9d5b-2d90e33aa0a4 | -3.09968 | -53.71772 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 889101a6-bb43-39ea-b1eb-db777f576ff1 | -3.09913 | -53.72127 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| da2f1d0f-92c3-33b3-bcec-040c5cb200b3 | -3.09688 | -53.71365 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 58d831c6-6a8b-3540-bca9-cd814b036b7c | -3.09633 | -53.71721 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9955ee70-60bb-35af-8b87-44a163d8930f | -3.09352 | -53.71314 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 258356f7-5a16-3ed2-904b-a6d7f83bac76 | -3.09297 | -53.71669 | 2024-11-02 05:04:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cc11d34e-6df7-382f-bee3-fc17ac936af2 | -2.97454 | -53.73492 | 2024-11-02 05:04:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 0c19cf9b-251b-3020-8776-71a038cc929d | -3.13114 | -54.26116 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5ba4a369-d97d-30d5-9b1c-9a96e7b97ffd | -3.12836 | -54.25718 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 471ee702-8b66-36e0-a843-196eed08748a | -3.12782 | -54.26065 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 784cd0a1-9cad-3b92-a799-57d4fcf79a59 | -3.12728 | -54.26413 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f64ff49c-af3f-34cd-bb5e-5d673af42545 | -3.12558 | -54.25319 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| c8f82b31-b5c2-38b9-82da-d8264b34e30d | -3.12504 | -54.25668 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| a5850611-9561-3cde-9fbe-4279bea0fb79 | -3.1245 | -54.26015 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cd2d201d-6494-362f-8f22-114bd5c121a2 | -3.12396 | -54.26363 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 7744a3b7-6fe5-37ec-833c-af2ea797b196 | -3.12342 | -54.26711 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68264784-0089-3b58-a45c-02d78d0cbbd7 | -3.12226 | -54.25269 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| fa38a3c4-7dac-37cc-a775-2707d363a7c8 | -3.12188 | -54.29886 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 52586b14-2861-3aeb-ba17-fc99d5ad1e69 | -3.12172 | -54.25617 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| b437d2b0-4d2f-36b8-bb7a-9e5411882ca2 | -3.12134 | -54.30232 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 11.2 |
| 5933c330-88bd-3328-bbf6-c1829c066c96 | -3.12118 | -54.25965 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6038699b-7806-3a24-9a66-0f1ab5184c22 | -3.12064 | -54.26313 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b63eef13-c3d8-3a94-934b-573bb03c3a5f | -3.1201 | -54.26661 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c92c4395-64b9-37b8-bb0c-d422f3568549 | -3.11956 | -54.27008 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 863137b8-74fa-38ab-8f0f-03c0e30c9967 | -3.1191 | -54.29488 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0b7b7163-5b84-3b24-ab65-38de018cc2c0 | -3.11902 | -54.27356 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa98d6ba-95f4-33ec-9ddd-13764ff18285 | -3.11857 | -54.29835 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 011f8fe2-c038-3eca-9f4b-2cbd1556d45e | -3.11848 | -54.27703 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 483ebd38-4f18-3ee8-baf7-ab9af20d0e87 | -3.1184 | -54.25566 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 12.7 |
| 468e1342-7fda-328c-acea-865c410e190e | -3.11786 | -54.25914 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 6a617928-c219-3fe9-ad3d-1f8bc295544b | -3.11732 | -54.26262 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 68598fb7-d496-36d8-9d1c-40c71d2a44b1 | -3.11678 | -54.26609 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 9e5dfad9-2220-3e3e-8c9a-02f95e21b491 | -3.11624 | -54.26957 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4522fc3d-188d-306c-8fcc-12d4fc0f39a7 | -3.11579 | -54.29437 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 55f35973-6ecc-3668-97af-382518a1afd6 | -3.11525 | -54.29784 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| fad4abf0-51bc-39c9-b1d3-bc408b7e8a3f | -3.11454 | -54.25864 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| ae7f5af0-482e-3f1d-a390-3a15b4bde22f | -3.114 | -54.26211 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e8bd604b-e283-3601-8231-08df90f21c11 | -3.11346 | -54.26559 | 2024-11-02 05:04:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |


[Clique aqui para ver as próximas entradas](README82.md)
