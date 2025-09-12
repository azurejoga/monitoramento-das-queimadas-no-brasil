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

## Dados Diários - Página 115

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 17d861b5-2f70-36bf-ac85-29d3da9b9d74 | -11.19283 | -55.07306 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| dd35bd53-6ffa-3937-9542-ba654502aa20 | -14.50804 | -53.91104 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 3b9b397b-f85c-3f91-b9b0-d9c8f6d35c7a | -9.54013 | -63.57666 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2c3a1b1b-c4f8-3a28-8550-e4f2dcd504af | -12.91684 | -54.76547 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3728d7fd-810c-3838-88e6-160c2832694f | -9.89798 | -51.88966 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 8fb37724-2185-3a68-bcb9-a5919ecdbfae | -11.19065 | -55.09163 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 89e70d03-fe3d-3360-a757-4f2cfb09e720 | -11.86809 | -58.82071 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 2f3f6305-4491-3b77-bae3-bbe17882b6c3 | -9.48658 | -55.99226 | 2025-09-12 05:46:00 | NPP-375D | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2fcd32ec-edb2-3d44-b6b9-39baf492d803 | -11.776 | -64.94127 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5b4e7374-872d-335e-a3d3-a8fd0d9b93ba | -11.18113 | -55.06649 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fc1f6570-528f-31a9-92f0-03531ebe2735 | -12.92605 | -54.80916 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| aee9ffa4-8b57-34a0-a7cb-e4a6d3f53895 | -11.22081 | -54.99479 | 2025-09-12 05:46:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| f1c73ee9-4431-3dac-880e-a78cd4e69cdc | -11.19158 | -55.09067 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b38f309e-c7ce-3eb9-abc5-98ea110458bd | -14.51558 | -53.90496 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1f5bbd85-bc6d-3fac-b585-dc181710ec33 | -11.18836 | -55.06642 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bd7a804c-a266-3024-a2c5-145c742b647f | -9.29611 | -65.60006 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 5245ada8-f552-3f47-bdf8-6a715a48f260 | -7.56276 | -61.31503 | 2025-09-12 05:46:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd262c1c-8d94-3f2f-bb84-7481d63731f7 | -9.83254 | -54.53049 | 2025-09-12 05:46:00 | NPP-375D | GUARANTÃ DO NORTE | MATO GROSSO | Brasil | 5104104 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d16a8e00-7fe1-3bff-b9d0-8e13db764ddd | -11.18659 | -55.0807 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a8bf31fc-c693-3047-aab6-becfd03ab0fa | -14.50058 | -53.91634 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 84eb171d-a03c-39be-b8a4-d8e5238f11e1 | -9.34971 | -65.45392 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| be1cb5e1-b06b-3e1a-ba90-0cc3dd869237 | -10.35562 | -57.48489 | 2025-09-12 05:46:00 | NPP-375D | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fbbb8335-ee71-3613-b46c-37e184ec79bb | -11.77767 | -64.93018 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 4086bf41-a6ce-3bf3-9e34-223d1e03a64c | -11.86953 | -58.80988 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 7bb4c2df-eb2d-3ad5-830a-5ba0c30b3871 | -12.82857 | -61.94909 | 2025-09-12 05:46:00 | NPP-375D | ALTO ALEGRE DOS PARECIS | RONDÔNIA | Brasil | 1100379 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5777758b-4654-3213-97fe-7fe7361efb57 | -11.77427 | -64.92965 | 2025-09-12 05:46:00 | NPP-375D | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 78d89b1e-83b7-36f1-b513-d769a968aaf8 | -9.45846 | -65.60418 | 2025-09-12 05:46:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e5bae6e9-146e-3fef-a04d-eae69b536703 | -14.33458 | -54.12212 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 313a6d31-db2b-3ba5-81ae-a06e4b204e71 | -9.35026 | -65.45041 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 938d481f-2ab0-3424-becf-6a1d20bf55d4 | -14.32652 | -54.13439 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| d11d865b-2b7e-33ad-87d3-98af9cbcd674 | -8.64754 | -55.24984 | 2025-09-12 05:46:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6423ccbd-365e-394d-a4b5-7b2237ec5b62 | -12.91957 | -54.75058 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8e77f244-0260-3a3d-84c4-5c0bdbbce505 | -9.89913 | -51.88082 | 2025-09-12 05:46:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 2c55eba5-c03f-38bf-bbb4-a908a245740d | -11.87713 | -58.81739 | 2025-09-12 05:46:00 | NPP-375D | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e1b4fc58-9ffe-33b8-bf45-3665f684acbe | -12.95919 | -54.74425 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1ae3c853-4958-3283-9127-3e3dd67cce27 | -12.35404 | -63.64172 | 2025-09-12 05:46:00 | NPP-375D | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 374f017c-dcaa-361a-9ecf-b47626ba1301 | -11.18784 | -55.06249 | 2025-09-12 05:46:00 | NPP-375D | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| b3069a52-b54f-3184-aed0-798d0c2ade5f | -11.97208 | -63.17827 | 2025-09-12 05:46:00 | NPP-375D | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 944d56c8-3936-3b32-9da2-6090a1e09896 | -8.67073 | -64.31808 | 2025-09-12 05:46:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1b133507-243a-30b8-b98d-d1e49705d40a | -12.92596 | -54.75136 | 2025-09-12 05:46:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 45c11f84-ecc9-323d-85de-0cba532346fc | -9.21894 | -59.37747 | 2025-09-12 05:46:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3c022e30-2f43-3fdb-a5b3-6da518dcf7dd | -14.49995 | -53.92252 | 2025-09-12 05:46:00 | NPP-375D | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| b600e46a-9cc5-3593-9a9b-3f14d773d45f | -9.33971 | -65.45234 | 2025-09-12 05:46:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 92d3e240-d084-3cde-ba1a-85592b5080de | -21.61622 | -54.00294 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 38b911b0-2ab2-3a7b-93f3-0610b843ddca | -21.61788 | -53.99343 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 4718326d-365f-3520-b9e4-f4cd8fdb6f88 | -21.61736 | -54.00136 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 3.0 |
| dc0845bc-5888-3a5b-9157-6e9606f4d7d1 | -21.61679 | -53.99506 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 6e5458ba-a522-3d3b-86f7-268ba0a0fc07 | -21.63861 | -53.99767 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 5.9 |
| c532c5ad-eedc-3efa-9b08-4dfcef8d2973 | -21.63921 | -53.9895 | 2025-09-12 05:48:00 | NPP-375D | NOVA ALVORADA DO SUL | MATO GROSSO DO SUL | Brasil | 5006002 | 50 | 33 | nan | nan | nan | Cerrado | 2.5 |
| ceb1a7fc-d798-3518-b1ef-65032e8f1b85 | -11.9523 | -51.1661 | 2025-09-12 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 62.6 |
| 3a0f2d77-054f-34f4-bfdf-a16d26a1a18c | -11.952 | -51.1874 | 2025-09-12 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 48.9 |
| 3bbd12ec-81b8-3ae1-9c91-ac050938c015 | -12.9292 | -54.7538 | 2025-09-12 05:50:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 67.6 |
| 6bb4e3a6-ccb0-3495-8bd6-0e81fbd1d9e3 | -15.9268 | -51.7785 | 2025-09-12 06:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 51.9 |
| 5cc6f097-19a4-3007-9955-033ad75b0a85 | -15.9068 | -51.803 | 2025-09-12 06:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 47.1 |
| 0ca5e28e-1918-3eaf-9c34-304cfcf3812a | -12.9292 | -54.7538 | 2025-09-12 06:00:00 | GOES-19 | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 77c88197-2f46-34d7-b492-a7f261a580e8 | -15.9264 | -51.8001 | 2025-09-12 06:00:00 | GOES-19 | MONTES CLAROS DE GOIÁS | GOIÁS | Brasil | 5213707 | 52 | 33 | nan | nan | nan | Cerrado | 60.6 |
| 2c8855f1-386e-3b23-a20c-83375c7e79e4 | 2.50921 | -61.02713 | 2025-09-12 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 4.0 |
| acb532e9-f1e2-3f6a-8bc9-44bab09f0f52 | 4.11898 | -59.97278 | 2025-09-12 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 59de4572-9b01-34ee-a1dd-b3749fc2ef46 | 4.11614 | -59.97017 | 2025-09-12 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3c62a188-7ca7-3a60-927d-322b3a66b284 | 4.11843 | -59.96961 | 2025-09-12 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e66d6a5-2153-3a0f-a0b7-edda184c1642 | 4.11668 | -59.97337 | 2025-09-12 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd93d337-6341-364f-bf78-b2b593c23596 | 2.50972 | -61.03021 | 2025-09-12 06:03:00 | NOAA-20 | MUCAJAÍ | RORAIMA | Brasil | 1400308 | 14 | 33 | nan | nan | nan | Amazônia | 6.2 |
| f6357402-80ac-330c-b15a-1c1f102228a7 | 4.11362 | -59.97375 | 2025-09-12 06:03:00 | NOAA-20 | NORMANDIA | RORAIMA | Brasil | 1400407 | 14 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc160d21-dc1a-324d-ab7b-12edc2271f0e | -3.40651 | -60.39682 | 2025-09-12 06:05:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 4c01ab21-b879-3edd-a136-35d3ba61ea15 | -3.40064 | -60.39585 | 2025-09-12 06:05:00 | NOAA-20 | MANAQUIRI | AMAZONAS | Brasil | 1302553 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f790e550-b9b8-3be7-b710-f052fa625342 | -7.3871 | -59.69788 | 2025-09-12 06:05:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0c190e76-2d35-33b7-9de3-c2eb61cf3ee1 | -8.48766 | -47.26654 | 2025-09-12 06:08:00 | AQUA_M-M | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| fd9f4c54-dd88-38c3-b36d-7fdf9e2df07c | -8.07955 | -50.17705 | 2025-09-12 06:08:00 | AQUA_M-M | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| b37f886a-d0b7-397d-8458-266e70efa154 | -7.40653 | -50.64202 | 2025-09-12 06:08:00 | AQUA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 3c2b07bf-6b10-360d-a47b-3c9795f28a4e | -9.05237 | -47.03795 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 00092a6b-4519-337c-ba44-c76d92d9a590 | -9.03951 | -47.04177 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 12.4 |
| d94a2f8c-0bfb-3968-b343-a314377f9114 | -8.95336 | -46.71817 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| 5c8ad32e-9d3f-3466-85ae-4e479f0a5b7c | -9.06377 | -47.02811 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 20.6 |
| 560128d5-3689-3be7-a8c5-4c7943bc9d79 | -8.54879 | -48.94842 | 2025-09-12 06:08:00 | AQUA_M-M | PEQUIZEIRO | TOCANTINS | Brasil | 1716653 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 0dd35ae8-1cfc-3b35-9ab4-adb820a6e2cd | -3.21342 | -47.12469 | 2025-09-12 06:08:00 | AQUA_M-M | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 17.3 |
| 0d69330c-19e5-3375-b0f2-6e513f67107a | -9.68418 | -47.54971 | 2025-09-12 06:08:00 | AQUA_M-M | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 75c498f0-9ada-3ccb-b7b6-25657143eefc | -8.04528 | -52.32219 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 9.8 |
| 94d54437-92fd-3f54-b460-c573d6f7bd83 | -5.29061 | -48.12317 | 2025-09-12 06:08:00 | AQUA_M-M | BURITI DO TOCANTINS | TOCANTINS | Brasil | 1703800 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |
| 5f6541e6-5c8e-3e37-bbff-b693d6abc9a8 | -3.31511 | -50.07513 | 2025-09-12 06:08:00 | AQUA_M-M | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| ab21dd9c-dabc-3f74-89ef-df0ef95c4b7b | -6.6803 | -44.1431 | 2025-09-12 06:08:00 | AQUA_M-M | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 21.2 |
| caffb1cd-6285-35d6-8878-a70bb72e026a | -3.25478 | -48.4522 | 2025-09-12 06:08:00 | AQUA_M-M | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 9.3 |
| 5b21194d-0e28-38f7-a4d7-48ca2256160c | -6.82161 | -52.79706 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 18a286b4-df20-30e4-aae3-8eca54c73210 | -9.03003 | -47.10771 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 34.8 |
| cf2a75d1-adbf-3bb3-b833-7fb5409d9d20 | -6.17098 | -47.27808 | 2025-09-12 06:08:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 12.0 |
| 1dec5ca1-693b-36a6-abba-10a2e4949418 | -9.67366 | -46.7595 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 725c5adb-47f5-343c-8531-c819667d9f1f | -9.71243 | -48.30746 | 2025-09-12 06:08:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 8.1 |
| 715ef05c-6719-3de9-b9e8-60a6c980356d | -6.96447 | -44.81991 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 20.3 |
| f3e82e9e-2c83-3ef8-a1de-6d5d93a5d1db | -9.06221 | -47.03939 | 2025-09-12 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 48.5 |
| f34c0590-6a3f-339d-b2f2-3d21b3b579a8 | -9.07458 | -50.495 | 2025-09-12 06:08:00 | AQUA_M-M | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 0b4f1064-6def-3b5d-be3a-dc924b0e4aeb | -7.71945 | -50.35146 | 2025-09-12 06:08:00 | AQUA_M-M | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 7.7 |
| 860e8224-84c1-3f54-9877-676fb7ff879f | -6.09587 | -45.93893 | 2025-09-12 06:08:00 | AQUA_M-M | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 1dfb99dc-da5b-365e-ae83-e626adb085a6 | -7.41683 | -50.64928 | 2025-09-12 06:08:00 | AQUA_M-M | BANNACH | PARÁ | Brasil | 1501253 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 51c52271-eefd-3e2e-ba1d-37ae6b3a5715 | -9.7175 | -48.33775 | 2025-09-12 06:08:00 | AQUA_M-M | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| 7cd56ce9-a63f-3c05-bc36-39be26e9aed3 | -6.16954 | -47.2881 | 2025-09-12 06:08:00 | AQUA_M-M | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 10f5b0c5-2b02-31c7-bb2c-e62e4b09f182 | -7.78547 | -50.77593 | 2025-09-12 06:08:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| 7bc94d31-bc5f-300f-b50b-ef5b85d76b32 | -9.03163 | -47.09658 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 48.1 |
| a50a4ab2-ec00-31c3-9247-6f805e1adf6f | -8.57529 | -51.3452 | 2025-09-12 06:08:00 | AQUA_M-M | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 10.4 |
| 8b6680f4-739c-3594-ab2d-240f71abd635 | -8.89153 | -49.9333 | 2025-09-12 06:08:00 | AQUA_M-M | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 32.3 |
| e6ca6ff9-6b7a-3fbb-b4e0-93f39ff961eb | -6.96445 | -44.81471 | 2025-09-12 06:08:00 | AQUA_M-M | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 16.5 |
| d90a74c0-7399-3060-931b-e4cc246f7a6e | -9.03323 | -47.08546 | 2025-09-12 06:08:00 | AQUA_M-M | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 78.4 |


[Clique aqui para ver as próximas entradas](README116.md)
