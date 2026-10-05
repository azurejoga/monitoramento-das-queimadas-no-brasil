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

## Dados Diários - Página 141

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2ad68dbf-93d1-3eb8-a291-b962d29671fb | -12.76174 | -62.05236 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 3da7b289-836a-339d-ba81-7ad309be1bff | -3.67004 | -54.53797 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 9a58aa8b-c415-36df-b282-642fb80cdec4 | -2.99735 | -58.44093 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 40786527-6232-3d0e-b6ac-62f22221e803 | -10.95692 | -60.90122 | 2026-10-05 17:34:00 | NOAA-20 | RONDOLÂNDIA | MATO GROSSO | Brasil | 5107578 | 51 | 33 | nan | nan | nan | Amazônia | 4.8 |
| d306cea8-7c8f-361b-8871-84fe22987728 | -3.82767 | -59.40641 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 2d9bb08c-16a4-3a2e-a4a6-8e6eed568963 | -3.28769 | -60.10967 | 2026-10-05 17:34:00 | NOAA-20 | IRANDUBA | AMAZONAS | Brasil | 1301852 | 13 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 32a56964-f056-3676-9cf3-5abe10115778 | -3.74973 | -59.62666 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d8d93c3e-7b78-3fe0-8828-80d9e97eb2fc | -2.92909 | -54.12673 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 32.9 |
| b88f38a5-7bf5-39e0-b111-870554c7407c | -7.94181 | -72.29879 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.9 |
| a395b17c-8cfe-3d78-88e5-d17652595a64 | -11.34572 | -46.65417 | 2026-10-05 17:34:00 | NOAA-20 | RIO DA CONCEIÇÃO | TOCANTINS | Brasil | 1718659 | 17 | 33 | nan | nan | nan | Cerrado | 8.3 |
| 30500581-aa8f-338a-9956-99fa6cf00f3c | -5.96168 | -55.35455 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 5c729500-38f5-3e3b-81b9-5c70133a18c7 | -3.47283 | -55.43166 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 0c24abe7-3be5-3fec-8b8b-86ec5af08cd6 | -10.72127 | -64.96122 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 9cfe12cb-2e6a-3488-b01c-f2aada59486c | -3.47161 | -54.59335 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 8d8a652a-9547-3063-b2e2-fe0458327be4 | -10.51641 | -46.05654 | 2026-10-05 17:34:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 14.4 |
| cb6d55f4-4402-3fa1-89fd-c23d9c09587a | -3.7211 | -59.68533 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |
| f45494a7-30c2-3bef-8cff-650e822f4f20 | -12.14203 | -63.179 | 2026-10-05 17:34:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 12652a17-3719-3115-9546-de504b8c54ff | -3.35057 | -59.72249 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.3 |
| a93f84a3-ebb4-3760-8e9e-310b5482a379 | -3.32733 | -59.48177 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 0319a9ea-9284-34d9-b051-375bbe752afa | -2.98233 | -57.90145 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 155eb1a8-2161-3d61-a2dc-2bc9b5d9f823 | -3.07072 | -54.16284 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| a766e297-9b6b-38ab-87fd-521eb74dc9d7 | -3.97063 | -52.21531 | 2026-10-05 17:34:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 787cac32-172d-34fb-b635-ed01e40c1abf | -8.11724 | -70.18806 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 4d31c8f2-c4e2-3a40-bdde-63c7369b3161 | -9.51145 | -46.81805 | 2026-10-05 17:34:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 10.6 |
| 5f567efa-97c6-3166-b82e-3b6ac2a07359 | -3.07263 | -54.16914 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 22.5 |
| d8ebc3b7-1036-3965-a125-9a59bcb0f507 | -11.72481 | -47.49686 | 2026-10-05 17:34:00 | NOAA-20 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| fe720993-ac12-3628-b323-f6fb41d4840a | -3.09614 | -54.17032 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.5 |
| b82433cf-97fa-35c2-a98b-51abe53b4825 | -10.30138 | -63.40137 | 2026-10-05 17:34:00 | NOAA-20 | MONTE NEGRO | RONDÔNIA | Brasil | 1101401 | 11 | 33 | nan | nan | nan | Amazônia | 22.4 |
| 4145da41-6da9-3e99-a498-52cdd7869816 | -3.4914 | -57.7797 | 2026-10-05 17:34:00 | NOAA-20 | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| 3911855d-45be-37ff-b62e-7dd9ba084e9f | -2.90788 | -54.08199 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 6.2 |
| bb616e89-6fb4-320c-a9e1-d80b1785ef28 | -7.06108 | -69.68205 | 2026-10-05 17:34:00 | NOAA-20 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| ac9dc1e5-d557-3410-9da8-421c8c50c908 | -2.96829 | -54.10741 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 12.9 |
| 0fa45b67-98d4-36e2-bf4b-46e9ac094297 | -8.19654 | -72.98416 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 8.6 |
| 41bc58fd-57bb-3916-b28d-6fabe6c2b4f9 | -3.06473 | -54.15438 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 75.0 |
| a91e17a8-0442-3156-a411-5cd37ec7b84c | -10.48856 | -47.23918 | 2026-10-05 17:34:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 48eda256-047f-375d-9130-a4036fbf0131 | -2.49096 | -49.41354 | 2026-10-05 17:34:00 | NOAA-20 | CAMETÁ | PARÁ | Brasil | 1502103 | 15 | 33 | nan | nan | nan | Amazônia | 38.4 |
| c411ef12-d2ee-33b2-ae9b-dd9874ac4357 | -3.51157 | -54.61783 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 9fa63d13-d3e0-331f-b4e6-a8c6dc42b44d | -6.19214 | -55.33609 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 31f94862-2dc0-30a5-b18e-c440cbafc014 | -3.70678 | -59.63046 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.5 |
| cdfe62bf-218b-3d2f-97bd-8f843b84b9fc | -5.89851 | -55.52856 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 1453b6a6-7564-3b8c-b6a9-295a7266d9e9 | -3.11798 | -57.6643 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| f15897b3-0d7d-3f97-a109-60c00c87f97c | -10.36683 | -45.02008 | 2026-10-05 17:34:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 4c472a1b-2160-39f7-9e0e-ab07d2ff32d6 | -7.39822 | -70.11231 | 2026-10-05 17:34:00 | NOAA-20 | ENVIRA | AMAZONAS | Brasil | 1301506 | 13 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 744d3263-2c74-3568-ac75-30bf6f5a84b0 | -3.06959 | -54.15068 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 27.0 |
| 3b24e39c-a6f1-3320-a67e-353737e23bda | -4.05738 | -54.03979 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8f77a437-47bc-3d13-a505-8c487fa0631d | -3.63537 | -58.93369 | 2026-10-05 17:34:00 | NOAA-20 | NOVA OLINDA DO NORTE | AMAZONAS | Brasil | 1303106 | 13 | 33 | nan | nan | nan | Amazônia | 17.1 |
| 605bf0d0-c5e6-36c4-af93-7dfda0d26e69 | -3.65005 | -55.31769 | 2026-10-05 17:34:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 17dbf70c-af13-3c33-b0c7-adf81140cb89 | -6.17184 | -55.37327 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a1f6277b-6b34-3e19-bf05-9fec3ae073d0 | -3.51731 | -54.62561 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 28.9 |
| 3e843c79-ae14-3260-9014-f11277e3e15e | -4.26976 | -59.5442 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d0c08c56-4da8-366d-ba02-bf4a7f387b1f | -3.42849 | -59.56821 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 5.1 |
| ff8250fa-603e-38bf-a7af-e6b49fdfe2b1 | -14.42584 | -59.87963 | 2026-10-05 17:34:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| d03679b3-4296-3273-bf72-b4a1f1607bad | -3.53621 | -59.40507 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| d7a3d7b3-3e01-33aa-a04f-ae07c4944f18 | -3.54833 | -59.48396 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 11.7 |
| e468a372-f1f7-372b-9644-69ffef41e0f1 | -7.36799 | -72.60826 | 2026-10-05 17:34:00 | NOAA-20 | GUAJARÁ | AMAZONAS | Brasil | 1301654 | 13 | 33 | nan | nan | nan | Amazônia | 14.5 |
| 56e2cfdc-a63f-3c09-b792-ceb5e17f195e | -7.89794 | -73.17287 | 2026-10-05 17:34:00 | NOAA-20 | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 6.6 |
| 9269413a-825b-34e0-945e-1aeb3029af0e | -4.2684 | -59.20095 | 2026-10-05 17:34:00 | NOAA-20 | BORBA | AMAZONAS | Brasil | 1300805 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 43d3cdf5-7dc4-3026-9648-0a604ac7d988 | -3.64521 | -58.65645 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 7.9 |
| c40ab955-ca2e-381a-945f-cfe1626ba70f | -8.27674 | -71.11755 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 2f7db16c-f12d-3514-82e3-1a90ea33a1b8 | -3.66451 | -60.59626 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 4.4 |
| 1690e0b5-8529-3196-b2c8-1907ed422485 | -7.61043 | -73.01136 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 9.9 |
| ba0b3be9-3ef4-3e4b-8336-05d4cc1d16be | -3.37563 | -58.19886 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 105.7 |
| bd97d01d-bc55-342c-a2e8-f7e12080f7ba | -2.95175 | -54.15168 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 26.3 |
| 2d84cb7d-14f0-3cd6-b26e-e34c94060948 | -3.27381 | -59.58141 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 2864015b-d05c-32b2-80df-db74378c5aa4 | -3.69226 | -59.14298 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 18c34fb3-8f38-30f0-b809-576f7690bb48 | -11.36768 | -47.71124 | 2026-10-05 17:34:00 | NOAA-20 | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| ddeb6654-4582-3d7b-bafc-cbd6eea94def | -8.125 | -70.15792 | 2026-10-05 17:34:00 | NOAA-20 | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 5d85d434-bea4-3001-887b-bf0d8b65a92f | -3.72804 | -59.59732 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 6.6 |
| dff036ba-99fa-3545-b29d-1f51def8a84b | -2.9563 | -54.15089 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 6cbdd66b-2cad-3255-91be-67b7cc476028 | -12.92467 | -62.17999 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 4.3 |
| bdbae033-877f-38ab-b139-03e611f46457 | -3.79691 | -59.31925 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 20.7 |
| a9c56c57-2fb3-35b1-b839-4902f18041a9 | -3.54606 | -59.49162 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 93e30ba8-3229-3312-a08e-95e20063fa0f | -3.67442 | -54.53724 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 18.8 |
| bff6218f-3201-32e4-9d8b-14259d872560 | -12.8808 | -62.15967 | 2026-10-05 17:34:00 | NOAA-20 | ALTA FLORESTA D'OESTE | RONDÔNIA | Brasil | 1100015 | 11 | 33 | nan | nan | nan | Amazônia | 11.9 |
| da2c9c1e-e4ca-39ac-9efd-fd0bd420d66f | -3.43417 | -58.60378 | 2026-10-05 17:34:00 | NOAA-20 | ITACOATIARA | AMAZONAS | Brasil | 1301902 | 13 | 33 | nan | nan | nan | Amazônia | 19.7 |
| 7abb4430-d236-3cb5-ad5b-00dc6d08c4b1 | -3.6776 | -60.61541 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 7.1 |
| 5f49015a-ac63-33a8-a208-1daaf1252075 | -3.32231 | -59.47152 | 2026-10-05 17:34:00 | NOAA-20 | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 1271392a-c0ec-3c54-9bba-b91f1d3010a1 | -6.18703 | -55.35467 | 2026-10-05 17:34:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 7.2 |
| a4d151ab-7d37-3462-bdba-95d8ca896434 | -3.63807 | -54.50711 | 2026-10-05 17:34:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| b1ab7c0b-4729-3d06-8dc3-6cb7b3682b29 | -4.05886 | -54.04884 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 68be7bd2-8482-36f8-a3ef-c6cd610a96be | -3.11738 | -53.6987 | 2026-10-05 17:34:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 8.6 |
| ce3c3e3a-1c57-36df-a43d-e91301861018 | -7.8214 | -71.91903 | 2026-10-05 17:34:00 | NOAA-20 | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 15.8 |
| 43d8092a-3b8e-3713-b28a-4e20c9ff709b | -3.54025 | -60.51681 | 2026-10-05 17:34:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 13.6 |
| 9f8e22ba-7f4e-3615-b283-2e29858647b5 | -4.0319 | -54.88721 | 2026-10-05 17:34:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 8.2 |
| b605e2cf-30d8-37e4-b545-7576c93c1aad | -2.98584 | -54.09996 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.5 |
| e1c2c7f7-172e-36e9-8942-6c62b3812350 | -3.6479 | -59.53762 | 2026-10-05 17:34:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 2759a1c9-2276-314e-b29c-b21e29c34e08 | -7.45871 | -73.64394 | 2026-10-05 17:34:00 | NOAA-20 | MÂNCIO LIMA | ACRE | Brasil | 1200336 | 12 | 33 | nan | nan | nan | Amazônia | 13.6 |
| e6aef2b0-ec40-3b0c-8255-8cea09be1b65 | -3.08626 | -54.16693 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 13.9 |
| 311e371f-23fe-34d1-8120-5feeca822004 | -3.11004 | -57.66119 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 5.6 |
| b55fe8e6-8660-362f-8fe6-42d8b11261bd | -7.33359 | -67.96993 | 2026-10-05 17:34:00 | NOAA-20 | PAUINI | AMAZONAS | Brasil | 1303502 | 13 | 33 | nan | nan | nan | Amazônia | 20.2 |
| 29609e0d-b338-304b-883c-5b0027292a04 | -3.10209 | -57.65809 | 2026-10-05 17:34:00 | NOAA-20 | BOA VISTA DO RAMOS | AMAZONAS | Brasil | 1300680 | 13 | 33 | nan | nan | nan | Amazônia | 8.4 |
| 500883e3-8362-3710-993a-3e09e91376be | -3.06618 | -54.16362 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 24.1 |
| 1ae27be8-9676-3bbe-b837-c96b849cc825 | -6.35431 | -60.01001 | 2026-10-05 17:34:00 | NOAA-20 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 5601beaf-9fa6-3521-b34d-776be19cd402 | -2.95029 | -54.14237 | 2026-10-05 17:34:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 29.9 |
| e5e075a9-0098-3c8b-8267-4c05bedf5738 | -2.7923 | -54.09422 | 2026-10-05 17:34:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| 350186dd-c4a8-3c1e-a733-9ccbacdad4ca | 2.49126 | -50.93254 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 19780efa-9c2d-385f-8d58-2b7f6942ad06 | -2.07868 | -56.83644 | 2026-10-05 17:37:00 | NOAA-20 | NHAMUNDÁ | AMAZONAS | Brasil | 1303007 | 13 | 33 | nan | nan | nan | Amazônia | 9.4 |
| 5baf94c8-2154-3d8a-9da1-7071966dca0e | -1.2845 | -55.41194 | 2026-10-05 17:37:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 29.4 |
| d3549cc3-24fc-327b-9bcc-aaedade396f8 | -7.33708 | -55.73933 | 2026-10-05 17:37:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5c881347-d7f3-3b1f-819b-62d485db95ed | 2.49054 | -50.93727 | 2026-10-05 17:37:00 | NOAA-20 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 6.3 |


[Clique aqui para ver as próximas entradas](README142.md)
