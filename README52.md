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

## Dados Diários - Página 52

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| eb14e0ee-3c2b-3edf-9dd9-57f3532c394c | -3.66384 | -64.61545 | 2024-11-01 05:46:00 | NPP-375D | TEFÉ | AMAZONAS | Brasil | 1304203 | 13 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3adc0cad-2801-3e9a-8160-5d90953a0f68 | -3.00495 | -65.45444 | 2024-11-01 05:46:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| bdfbeb4f-8738-364c-a50b-93d90e68153f | -3.00162 | -65.45393 | 2024-11-01 05:46:00 | NPP-375D | UARINI | AMAZONAS | Brasil | 1304260 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 4ef89575-076e-3527-8614-34cbf26234f4 | -9.80214 | -66.6952 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 401cda70-4763-3456-9b2f-b5a30b45e494 | -9.79879 | -66.69467 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 18d8bff8-18bf-30b5-a887-0e31c2e38300 | -9.69881 | -66.13936 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 999a83c5-12c2-31f0-a637-53072f09d81e | -9.69826 | -66.14297 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 68381887-6ee7-38fb-b725-8ad9e50d29c5 | -9.67137 | -66.5185 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 85c1d3e9-5554-37c9-ac46-9041cef40f89 | -9.6582 | -67.40405 | 2024-11-01 05:48:00 | NPP-375D | PORTO ACRE | ACRE | Brasil | 1200807 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6bb80c79-3d47-374c-b729-de4b787d01ec | -9.57118 | -66.63402 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 325e7ef1-fcdc-34e3-81a1-5eeb374ff4cc | -9.57063 | -66.63757 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 6023eb31-d559-32f4-a047-554efe7b53a1 | -9.56784 | -66.63349 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c8279a05-8ab1-35c4-b9e4-7c4807b16161 | -9.56729 | -66.63703 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5169e558-8904-3b51-ab5a-68099b1b0b71 | -9.52843 | -66.65232 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5b0d1ff3-c8f7-3470-81ec-9cfab6fae65a | -9.52788 | -66.65586 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 72230e30-f6d0-352c-bf71-8d5df7964f21 | -9.52509 | -66.65179 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 06681a0c-c10d-3b79-b9b0-4c14bd737854 | -9.52454 | -66.65533 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e380b725-c7c5-3de4-8ae9-74a7641f379b | -9.52174 | -66.65126 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7aae8d5f-e5a8-3941-bfed-9ec9b4b0da34 | -9.51166 | -66.62788 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0064c5bc-c3c9-3fcc-9d97-36ed2b8c6b68 | -9.50481 | -66.5613 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 50cee78c-249a-378b-a3c1-952b38f4efca | -9.43444 | -67.14594 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 811ddac5-f58b-3c48-858c-e076fdf6385a | -9.42964 | -67.24191 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0621c50d-0460-3bbf-8c1d-d44f96947a74 | -9.42631 | -67.24139 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.4 |
| b2a1a2f1-d336-35c1-af16-ff938e4677c5 | -9.40876 | -66.52845 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| dabb1319-12d7-3b25-8181-d109ab4d9e18 | -9.253 | -68.18657 | 2024-11-01 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dc6bdbaa-50ff-3ba5-aa3b-78d7d8e6997e | -9.13193 | -68.18186 | 2024-11-01 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 0ac1a9e4-45bb-38cb-b46b-a658b6400b3b | -8.91222 | -68.56651 | 2024-11-01 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 2.3 |
| a45a7b8d-0614-3fa4-b457-1d243958a613 | -8.81981 | -67.69972 | 2024-11-01 05:48:00 | NPP-375D | BOCA DO ACRE | AMAZONAS | Brasil | 1300706 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa1f1f5c-c17a-3019-93c4-04324fdf664c | -9.67686 | -68.35283 | 2024-11-01 05:48:00 | NPP-375D | BUJARI | ACRE | Brasil | 1200138 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| eb7331bc-db5c-3681-be65-157606e4bee0 | -9.53858 | -68.52024 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 1a5c1155-ebe2-3dac-a3b0-0e34689fbaf3 | -9.53801 | -68.5238 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d0de75a5-198a-37d1-aa48-453e6217b6de | -9.51985 | -68.59411 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f29daa9f-fadb-36d3-b9a8-aee3f88e9392 | -9.51649 | -68.59357 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 31a2d0dd-45cd-3fd1-9067-3cf67b17987c | -9.51592 | -68.59714 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3d1f1172-d556-3071-a4e7-f01c5d88d74e | -8.85344 | -64.16219 | 2024-11-01 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c55eec7f-f9e8-3d62-bf00-7d087d7e7df5 | -8.84917 | -64.16587 | 2024-11-01 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1a098868-2fec-353d-a487-75d80d2b1ef3 | -9.70518 | -64.19045 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ee9dc54e-b48b-3432-b3d7-99d124b78140 | -9.70454 | -64.19474 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8b8ced17-b1b2-346c-88fa-eecebf5be53e | -9.70153 | -64.1899 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fd05e1cb-3c06-33c6-93b6-79c16ad4ccf1 | -9.70088 | -64.19419 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d23a6209-d264-33cd-a084-1408f932fa02 | -8.83025 | -64.19304 | 2024-11-01 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c144639e-9c8e-374b-aa58-3a27890e0b6d | -8.82962 | -64.19725 | 2024-11-01 05:48:00 | NPP-375D | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9c89838-bcbe-3ec1-b2f5-7f230bae519a | -9.9186 | -64.80665 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 345f54d8-d124-36d1-ac9a-752059ed7476 | -9.918 | -64.81068 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 68871d8a-121e-3be8-80a3-661741fcb861 | -9.91565 | -64.80206 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 62755011-b225-3fb5-b17c-f555d20a1362 | -9.91504 | -64.80611 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 44f1df58-a346-313c-8bc5-0ce811f2540e | -9.91444 | -64.81013 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| dea58add-3597-340b-b0af-f87027851a28 | -9.91383 | -64.81417 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 02c1ebf3-4fad-3645-adad-61b49c31aec0 | -9.91323 | -64.81821 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 2a426183-1c5b-3a1b-b5bb-97ffcb3c7e19 | -9.91209 | -64.80151 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| ca3df7d0-8128-306e-b126-51123cf87244 | -9.91148 | -64.80556 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 97d79ccf-4148-3de3-86fd-987c66f45635 | -9.91088 | -64.8096 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 75052b0b-bbaf-3e85-9b86-ff80e0788a30 | -9.91028 | -64.81363 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 36fd0f92-ea7d-38ef-98af-a89c484cd70e | -9.90967 | -64.81767 | 2024-11-01 05:48:00 | NPP-375D | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 458151aa-5609-37b3-b21f-d7c235951b17 | -10.12317 | -64.97931 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| b3ac5fbd-f303-396a-9ebf-ab3e66c55616 | -10.12257 | -64.98331 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c412c22e-97a4-381d-86ae-e7655ea43a81 | -10.11964 | -64.97875 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| aa93e903-a897-3c30-9e0c-b6956a233130 | -10.11903 | -64.98277 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ee0fb5be-8194-3ca7-9522-a0837ee32e17 | -10.1155 | -64.98222 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dc0de6c8-5030-39a2-8a50-39a8818f42e3 | -10.11197 | -64.98165 | 2024-11-01 05:48:00 | NPP-375D | NOVA MAMORÉ | RONDÔNIA | Brasil | 1100338 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7e1dfa57-2950-39e0-ab61-b654f8fe5c10 | -9.46227 | -68.95144 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73f77adf-1168-36a0-b378-9b06638dd617 | -9.01587 | -69.13963 | 2024-11-01 05:48:00 | NPP-375D | SENA MADUREIRA | ACRE | Brasil | 1200500 | 12 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 161cd9fe-e3d8-37f4-bcf1-aa0112886c45 | -8.62573 | -69.71662 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 732b2f5f-8d8d-3e91-93dd-47a489265e64 | -8.6251 | -69.72053 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ffa0b2ac-54c2-39d3-9384-ac5ad4ed19b1 | -8.62447 | -69.72444 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 78e0701e-6b31-3282-b8c4-d22fd60398c9 | -8.62224 | -69.71603 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1701369d-47a0-339b-95e2-83f79d73ba41 | -8.6216 | -69.71995 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.6 |
| bf499371-364f-340c-9f27-747823f30f98 | -8.62097 | -69.72386 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2b206549-3918-3a49-8088-20600a4bdc1f | -8.61017 | -69.74615 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ca22b224-3e3d-334d-bdf6-8e2da8a487a5 | -8.21175 | -69.8652 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f937357a-71be-32d8-92d1-da2e986a04a6 | -8.25867 | -70.30175 | 2024-11-01 05:48:00 | NPP-375D | FEIJÓ | ACRE | Brasil | 1200302 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0a1a0b11-d205-3fa9-9d5f-e8ca7bf22d5d | -8.06936 | -70.88196 | 2024-11-01 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 898f35b9-ce94-3403-9c01-fc3036a04e69 | -8.06023 | -70.64103 | 2024-11-01 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5a22b04f-8d76-3f65-9822-5eaf8ed990d4 | -8.05141 | -70.64847 | 2024-11-01 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 73bacf5e-a023-3651-a3dd-104ce20030c1 | -8.01884 | -70.73898 | 2024-11-01 05:48:00 | NPP-375D | TARAUACÁ | ACRE | Brasil | 1200609 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3045cc7f-a45b-3a45-a167-db3535b76c60 | -7.90437 | -72.33283 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| b0d98da4-4b31-3e6a-8fa1-a81486dff2aa | -7.90029 | -72.33214 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 24b079f2-768d-399f-9b4e-8be83f39254f | -7.81343 | -73.11626 | 2024-11-01 05:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 228edf7b-e6b6-3c3b-bc87-49a3b4ac8a8d | -7.80538 | -72.93247 | 2024-11-01 05:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f556a4ce-ab53-3e47-8665-dd0771772cbe | -7.80238 | -72.89929 | 2024-11-01 05:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 90f47d4a-bf00-3f40-b1e7-ef2beb0bc68c | -7.75134 | -72.28134 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 20e28f02-3a54-3f2a-a4a0-05c7ffcdbb4b | -7.63612 | -72.46188 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| afc599a3-c4a2-3b24-b114-39c095887aac | -7.63457 | -72.46147 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b4aca579-30fb-351e-835f-de210f013bf9 | -7.63044 | -72.46077 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 11817dfb-00d5-3a6e-a815-5eef39b8042a | -7.48936 | -72.83529 | 2024-11-01 05:48:00 | NPP-375D | CRUZEIRO DO SUL | ACRE | Brasil | 1200203 | 12 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6939667a-865b-3add-b1bb-baf5aa313621 | -8.33255 | -72.60641 | 2024-11-01 05:48:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 06eeceb6-22d3-3992-a86c-66067157b6d5 | -8.33192 | -72.61013 | 2024-11-01 05:48:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 2d8765c8-c6a0-3fa7-851a-85d39c1acbe8 | -8.33129 | -72.61384 | 2024-11-01 05:48:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 94d71e17-e6fb-3f2e-88c9-fdedbc1cfe79 | -8.28864 | -72.66417 | 2024-11-01 05:48:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cf577325-e314-38fe-8f97-39cad25266a5 | -8.288 | -72.66792 | 2024-11-01 05:48:00 | NPP-375D | PORTO WALTER | ACRE | Brasil | 1200393 | 12 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c8a639bf-9815-3d3b-aafa-69d0cfb7c7f1 | -7.90749 | -72.8683 | 2024-11-01 05:48:00 | NPP-375D | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| c643166e-3698-3836-98a9-341648ba7dd3 | -9.97939 | -67.29763 | 2024-11-01 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 67b07e29-968e-33e8-a4ca-8b19ef53225d | -9.97884 | -67.30113 | 2024-11-01 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3cc95cdf-da7b-3c78-9202-94dc4e6cf639 | -9.9347 | -67.1035 | 2024-11-01 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 899ff4b7-649b-3145-b421-eadeb1662c7b | -9.93416 | -67.10701 | 2024-11-01 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| b5fd875d-1352-317a-89c6-fe9a58e3a360 | -9.91985 | -67.15513 | 2024-11-01 05:48:00 | NPP-375D | SENADOR GUIOMARD | ACRE | Brasil | 1200450 | 12 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 996d266e-cc01-3f4c-846f-537ecd8d341e | -9.40541 | -66.52793 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d539cfcf-ac7a-3511-984a-35e2d078fa21 | -9.14276 | -67.19702 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 036aa105-ff38-3a0b-9a13-d0a09aa03c6c | -8.65806 | -67.02717 | 2024-11-01 05:48:00 | NPP-375D | LÁBREA | AMAZONAS | Brasil | 1302405 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 55097fe1-25b8-379c-95d4-bc70e0bb7d55 | -9.86165 | -67.05173 | 2024-11-01 05:48:00 | NPP-375D | ACRELÂNDIA | ACRE | Brasil | 1200013 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README53.md)
