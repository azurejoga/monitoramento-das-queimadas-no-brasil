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

## Dados Diários - Página 73

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| fbc51a5f-3f3f-3c5a-a359-e9284b7b1cc9 | -4.29198 | -55.09004 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| cd640f3f-d5c5-3b1e-a5c5-0fe5b9ceadfa | -4.28302 | -54.97383 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 8b1db337-141a-320d-b25e-2cc17ccafd25 | -4.27441 | -54.64886 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 804a4336-ef8f-3b5b-8c4e-da8552a844c0 | -3.7387 | -54.48332 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7e48c2c0-27bb-3e0e-917d-d064493cd9d0 | -3.73797 | -54.48784 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| a56fd324-52e8-3af0-b063-3985b3ded78c | -3.73491 | -54.48272 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| d4d261bd-0561-3e5b-afd9-f0f504d1beb1 | -3.73419 | -54.48721 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cec7cfca-7e89-35ed-b88c-cd9298cb2b9f | -3.67998 | -54.2933 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7ce4f2a8-da86-308a-911f-5163a05d3d65 | -3.66512 | -54.31413 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e76f7cd-4da6-3592-a219-88c59dafff1a | -3.63705 | -54.68568 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 3138b088-b78f-3f6a-b9e4-148f83b157a5 | -3.63575 | -54.68281 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 35af6f75-0c81-387a-ac7e-e7afbf9e62da | -4.12878 | -54.63655 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 3de6db83-5e4a-3a38-be29-23bfd3048a58 | -4.11472 | -54.2902 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 87b13874-6def-32d6-a275-a0f405bcfc0c | -4.0968 | -53.93365 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| f92c6547-9299-3c98-a8fc-d626d047a53f | -4.07219 | -54.43562 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 559bfa36-f224-304d-9ac7-f90f3cea840b | -4.06842 | -54.43505 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 4cc0c77d-8fa0-3dfd-9736-cd8c90fbc845 | -4.05355 | -53.87582 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| bf97fe0d-88e2-3d48-af83-c1cd87175fab | -4.03602 | -53.86866 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1c5d8b7e-29a1-3d50-ab11-64d1ff8b0f9e | -4.03461 | -54.54829 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| e780cbf7-9171-3633-a530-8a801456c831 | -4.03387 | -54.55288 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 153133bc-7002-3e54-9d62-fe1955a3000a | -4.03096 | -54.61877 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 41227fac-9ca4-3716-a031-9e8e4b42979e | -4.03083 | -54.54768 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 531f59bd-718e-3827-9de1-fccd1cfa173c | -4.03008 | -54.55228 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bb63b5d7-365e-3576-86ff-a4ffb148cd94 | -4.0279 | -54.61358 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f5689c0e-488a-3d5b-96f5-f0f2b9bfeacd | -4.02715 | -54.61818 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 842bc418-c20c-3d97-abb3-6706e6fda9ca | -4.02107 | -54.60762 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 06de32b8-b2b9-328d-8796-c385e33bb240 | -4.0142 | -54.81948 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5258f97e-0b15-30fc-80f7-56da670aa845 | -4.01034 | -54.81891 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0521bbb7-988f-3d2e-9d76-f4aa7e75b4a0 | -3.97762 | -54.34806 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5d13e7a8-9f5b-30b9-9f34-39e929ce8de6 | -3.93603 | -54.55796 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 254d348e-ec60-33c2-a70f-bab1d26e53ed | -3.92693 | -54.5421 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 4a1ff71c-df36-3a2e-9880-c3ea590d2e8e | -3.88659 | -54.14496 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f2d1e14f-af05-3662-820e-df5975878431 | -3.88288 | -54.14438 | 2024-10-26 04:44:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf12b719-f3cc-32da-b24c-033bbe66fc61 | -3.85522 | -54.08118 | 2024-10-26 04:44:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0f715663-d21e-3608-a42d-4df3fd2af3a8 | -7.30811 | -55.31074 | 2024-10-26 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 287adf1a-7295-363b-8c95-372852c32344 | -7.27089 | -55.34741 | 2024-10-26 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25987f85-6088-33fa-a927-31ff4be2b1ff | -8.20844 | -54.89471 | 2024-10-26 04:44:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e04811b2-05d5-336e-8637-33a211c5b1e6 | -9.99723 | -56.24688 | 2024-10-26 04:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6b479ed5-024b-368a-9f28-9ced1ceb5b93 | -9.99339 | -56.2462 | 2024-10-26 04:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 2ba5e41b-61d8-36e3-961e-746c760763f6 | -9.91089 | -55.72197 | 2024-10-26 04:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8627bb9a-23b5-3a97-b942-4cedf4a4e513 | -9.90792 | -55.71681 | 2024-10-26 04:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f289ecac-2317-3b58-ad1e-fd319052c45d | -9.90418 | -55.71619 | 2024-10-26 04:44:00 | NOAA-20 | CARLINDA | MATO GROSSO | Brasil | 5102793 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 676d85e3-576f-3558-9590-5b70ba84bde1 | -9.66862 | -55.731 | 2024-10-26 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48b6550b-c6cc-3f65-98db-29a7d7215b5a | -9.66759 | -55.73271 | 2024-10-26 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50ae4827-bf6f-3ef3-b2d1-0b9bbdf19f7e | -9.66487 | -55.73035 | 2024-10-26 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 018d39bb-cc87-3577-b9d6-695be11c8ff7 | -9.6646 | -55.72748 | 2024-10-26 04:44:00 | NOAA-20 | NOVO MUNDO | MATO GROSSO | Brasil | 5106265 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 00886299-7ecd-3f4a-9831-8800c1fd353e | -9.39953 | -56.00756 | 2024-10-26 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 21c0e008-a897-3fa1-87c3-8850f298e838 | -9.39678 | -56.00935 | 2024-10-26 04:44:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e5f0b2b8-3e31-3dcd-abe9-50238ed8aa6d | -10.09561 | -56.1912 | 2024-10-26 04:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ce081c35-b449-379d-8593-6bc243be2608 | -10.0948 | -56.19602 | 2024-10-26 04:44:00 | NOAA-20 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 31d2ee9d-9f58-3228-bc5b-2ed599ecd7b0 | -3.6354 | -55.51349 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| dcff19f1-5d31-36e4-b0aa-a1be7b5928bc | -3.63195 | -55.50922 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 91257fb2-ae31-3c13-95ba-46e0e7fa500e | -3.63136 | -55.51278 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 17ee4c01-3c12-3826-b181-e2afdd740572 | -3.63078 | -55.51632 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| b93ff826-a245-3e1c-a439-c696fd15a6c6 | -3.62792 | -55.50852 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ad9e659b-278d-35a1-b284-c74f5c9ba971 | -3.62732 | -55.5121 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e0429958-7c6c-3528-886b-9a1be0ec085c | -3.62387 | -55.50789 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| d0054e71-b71e-38d3-933d-0c2452b5d945 | -3.62327 | -55.51148 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a41b357e-5ef4-3226-841c-59df8ea9c5ed | -3.57481 | -55.60255 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5afe3a16-13f8-39df-a0e0-37ed69204a92 | -3.57249 | -55.61698 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a28879a5-403d-3059-a570-dfd100736246 | -3.56374 | -55.51629 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7638899d-3fa3-3d0d-915c-c93e6550b263 | -3.5574 | -55.45335 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 34de8e8a-c2a8-3431-985f-0ecd23c86cbc | -3.55683 | -55.45684 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 930375d3-4efb-3db4-9b85-3cd357785f0e | -3.55338 | -55.45263 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1a58398c-2260-348f-8c50-ee9f7308e9a5 | -5.0741 | -56.22709 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| fd07f2be-3218-3614-9574-b4b3c128e627 | -5.07348 | -56.23083 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 5185f051-1435-3d11-a603-29e1593def60 | -5.06994 | -56.22643 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d5168515-5778-349c-97e9-7307cb5e04a5 | -4.69663 | -55.70858 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5ab80448-df58-37bd-bc49-9ce31b2f9dbb | -4.61474 | -55.90164 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20286a8d-9a3c-3ff9-98fc-1082110be702 | -4.61414 | -55.90531 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c2e78bf9-5bd9-354a-8369-7d1da856bad0 | -4.60746 | -55.76694 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| ab0d8484-d68c-36cf-bc3e-c385949373fa | -4.60342 | -55.76616 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| de8208eb-d02b-3d7e-8893-8ccc640857b1 | -4.58111 | -56.10894 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3c1dbb5b-2bff-3632-949c-12013fddba45 | -4.57759 | -56.10438 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 7b5df331-3901-3478-9786-1a358878bdb0 | -4.56116 | -55.97189 | 2024-10-26 04:44:00 | NOAA-20 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9db860e0-eff2-379c-80fa-15ed523ddb75 | -4.52802 | -56.01873 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| cf97ca78-eefc-3420-b2cf-29970f280697 | -4.51453 | -55.82576 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ff1865a8-8f77-3bf3-8380-611c3f9ac6fb | -4.51395 | -55.82935 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ce917c68-a5f2-3827-ba7a-7e72b60ad258 | -4.50977 | -56.00132 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 1fa7728b-48e2-37d7-8127-1a522f49731f | -4.50915 | -56.00499 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d181b533-60b7-3b15-93dc-67c5679c19af | -4.50339 | -55.89446 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2199583f-3467-3f66-8ca1-88349517db90 | -4.5023 | -55.62125 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 671b4258-257a-3781-b0e4-ed74aa1db8cd | -4.42191 | -55.70207 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fabd0bd3-f57d-35f0-be6d-eaa775d5afa8 | -3.73604 | -56.00061 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e92714e6-d32d-3105-b8b8-2070913f72b3 | -3.69928 | -55.96357 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f42d140b-bb74-343c-b848-e8613d7b575d | -3.69867 | -55.96733 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fc901d88-2c08-3266-87f2-12e8e073a7e9 | -3.69511 | -55.96298 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 7a892af0-ebe2-3be7-8ef5-846b19bd52a0 | -4.21441 | -55.72156 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| ed9fce36-79af-32ff-bdbc-5cc0916a535e | -4.21384 | -55.72509 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f5b9dbe9-482b-3d9f-8779-479731a2b2da | -4.19943 | -55.5583 | 2024-10-26 04:44:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| acc4daa3-0a41-3e1a-8a86-ff113109b6e0 | -4.04239 | -56.25102 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 05cfbae8-7356-316d-ac24-757ea23a6125 | -4.04136 | -56.2831 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 08d8abb2-48f9-3e6d-b6ed-0b46dec27bdc | -4.03791 | -56.27947 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 5079f314-67a0-335e-81da-ddadbe0adc24 | -4.03781 | -56.27839 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3b6fcca6-f3fe-3375-a2d3-d9168212d898 | -4.03726 | -56.28352 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| db4df8ce-ea37-3c5f-8693-866da4b37965 | -4.03713 | -56.2824 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 3290b842-b62e-3805-a19c-d062a7bff590 | -3.99975 | -55.73436 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cda24cdc-50f9-3f1f-8b3e-c7d4e3d88dbc | -3.99918 | -55.73787 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 70217704-4f53-332e-aa13-84c1fc2ef486 | -3.92239 | -55.92528 | 2024-10-26 04:44:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 16514c17-72c3-3bc7-9255-9e855f253c44 | -3.91826 | -55.92459 | 2024-10-26 04:44:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |


[Clique aqui para ver as próximas entradas](README74.md)
