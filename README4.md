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

## Dados Diários - Página 4

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2b196df2-3d2f-320f-a29e-3b97d868778f | -4.45401 | -44.14321 | 2026-01-04 04:40:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 333febe9-42f7-3092-a732-65a062f9732f | -5.55875 | -45.45079 | 2026-01-04 04:40:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e1033ac8-bf18-3f6b-a948-d1fb3ca658cd | -4.45 | -44.14257 | 2026-01-04 04:40:00 | NOAA-21 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| a2ccf745-1a25-3370-aa20-262678dbcbcc | -4.23989 | -48.73454 | 2026-01-04 04:40:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 52c5adc6-8afc-307f-9585-fee43cbef595 | -13.42818 | -43.85128 | 2026-01-04 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 3.7 |
| a0c94d33-1f49-3ed6-a765-e673b2381498 | -13.79619 | -39.00134 | 2026-01-04 04:42:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| b298890a-c0a6-3270-8fd8-2f866a4a9fc4 | -13.80262 | -39.00218 | 2026-01-04 04:42:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 7ad9a16a-f384-3e09-b6a8-a5c61bbabce8 | -13.80204 | -39.00761 | 2026-01-04 04:42:00 | NOAA-21 | ITUBERÁ | BAHIA | Brasil | 2917300 | 29 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 849587bd-eac6-35cf-9abd-32be71a2ff3c | -13.43285 | -43.85196 | 2026-01-04 04:42:00 | NOAA-21 | SERRA DO RAMALHO | BAHIA | Brasil | 2930154 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 981bc3f2-1f53-30c2-9e9b-426cb835581a | -18.55 | -52.78306 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 87ff99a6-7de6-391a-bd74-59bc0a4f4515 | -23.75709 | -54.58929 | 2026-01-04 04:44:00 | NOAA-21 | JAPORÃ | MATO GROSSO DO SUL | Brasil | 5004809 | 50 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| b113bd7d-8b0c-3ebd-902d-64c4f04ee8d2 | -18.54611 | -52.78612 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f187822c-0038-3e5b-b0ec-b7b944490a68 | -18.54669 | -52.78249 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a22cdcae-e3a0-3c34-ae79-bb80ef213c2b | -18.82304 | -51.61575 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 95c51843-065f-3cbf-b9e1-1bbc31fbfd6a | -18.55331 | -52.78364 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 361e11fd-20b6-31fc-9165-22e047814415 | -21.26712 | -48.63641 | 2026-01-04 04:44:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| e34d374b-222a-380c-89cb-3344b2527fb9 | -18.54972 | -52.74199 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 9208f119-9afa-3f99-8056-b0c6315c66d6 | -18.82083 | -51.60782 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 7068f096-e8b1-3f35-9ee2-1c35c0f83441 | -18.55303 | -52.74257 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 33d1605a-c01b-3399-9d75-0a9dea77c9dd | -21.25683 | -48.65532 | 2026-01-04 04:44:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 5.5 |
| c6d8b493-ad11-35df-9199-baa2ff7d6c20 | -18.82027 | -51.6115 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 1793233b-ec75-3228-807a-40efd78b4404 | -18.54942 | -52.7867 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a07d8e91-a792-337a-a7b4-d91044202f13 | -18.34144 | -53.54979 | 2026-01-04 04:44:00 | NOAA-21 | ALCINÓPOLIS | MATO GROSSO DO SUL | Brasil | 5000252 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 6cf47026-03a0-3b78-a0b5-c4940fbfab11 | -18.8236 | -51.61206 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| e699baf3-9645-3d3a-8551-cde28ba7b61c | -18.82416 | -51.60838 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 17.8 |
| 51a7900b-b4d9-3ad4-8bd0-a9d4911cd127 | -18.8175 | -51.60726 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 18.4 |
| 4f10a90d-0b00-3eb9-ac37-cba3edfb8910 | -18.82138 | -51.60414 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 91ed0473-4a71-38c1-8d1a-e7d04ddf9c3c | -21.25302 | -48.65469 | 2026-01-04 04:44:00 | NOAA-21 | FERNANDO PRESTES | SÃO PAULO | Brasil | 3515608 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 375ea451-227f-3f2c-9709-7ee89deea37d | -18.82637 | -51.61631 | 2026-01-04 04:44:00 | NOAA-21 | ITAJÁ | GOIÁS | Brasil | 5210802 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 79b8e3dc-879b-302b-bea5-5f11db5e8e41 | -20.81172 | -50.81017 | 2026-01-04 04:44:00 | NOAA-21 | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f1bbf606-4909-357c-93cf-d627c8732f1e | -18.55246 | -52.7462 | 2026-01-04 04:44:00 | NOAA-21 | CHAPADÃO DO CÉU | GOIÁS | Brasil | 5205471 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d73c74a-f1ba-315a-a44f-c6009705d024 | -26.48759 | -50.89457 | 2026-01-04 04:46:00 | NOAA-21 | PORTO UNIÃO | SANTA CATARINA | Brasil | 4213609 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| 11fd2bbc-2f4f-38b9-b5f4-e3dd29dc4669 | -31.77845 | -52.57797 | 2026-01-04 04:46:00 | NOAA-21 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 0.9 |
| 3ef3ca50-4efe-35d4-86c1-5d519d3d00ff | -30.47626 | -54.37017 | 2026-01-04 04:46:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| 29ee17ff-4b99-3791-9edc-7f921cdd341b | -30.4796 | -54.37083 | 2026-01-04 04:46:00 | NOAA-21 | SÃO GABRIEL | RIO GRANDE DO SUL | Brasil | 4318309 | 43 | 33 | nan | nan | nan | Pampa | 1.1 |
| c396059d-be0c-3774-bd2d-c86e0b192e84 | -26.68846 | -52.71076 | 2026-01-04 04:46:00 | NOAA-21 | QUILOMBO | SANTA CATARINA | Brasil | 4214201 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 7f9f88cd-665d-3d7b-8d9b-61ba73fd0be4 | -31.77983 | -52.57642 | 2026-01-04 04:46:00 | NOAA-21 | CAPÃO DO LEÃO | RIO GRANDE DO SUL | Brasil | 4304663 | 43 | 33 | nan | nan | nan | Pampa | 1.0 |
| bc975c33-6d6e-3583-889a-12d18be10cfb | -1.58144 | -54.34715 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e662e293-bea9-35d3-91d5-47424ea0e923 | -2.91084 | -49.37356 | 2026-01-04 05:08:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 303ebbf6-c4b8-3d4d-9c87-7a6089f6d2f6 | 3.35997 | -60.36268 | 2026-01-04 05:08:00 | NPP-375D | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5473e3a7-7320-317d-a272-02b1cab34f16 | -3.3044 | -53.35993 | 2026-01-04 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e25293f5-7845-3fc9-927b-39af840ca595 | -1.14523 | -54.17252 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 137b85dc-9bd1-3b7c-a32c-7882e984bdbd | 1.07815 | -60.38808 | 2026-01-04 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4ad473f2-afdf-3fe6-b20a-3736b40b7bb7 | -3.06699 | -54.02675 | 2026-01-04 05:08:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c79daa64-79fb-3901-9ead-35b0a922032f | -2.89613 | -52.2879 | 2026-01-04 05:08:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| d265689a-7f51-32fa-bd1a-56a66aca31cb | 0.62268 | -60.28524 | 2026-01-04 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 65690fa5-2835-3a51-a265-1e25d3079cdd | -2.77493 | -54.52713 | 2026-01-04 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 42445884-4785-3489-9f32-3e78a33a0b34 | -2.1132 | -53.47745 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3b7f732b-ee7a-3577-94a0-be6bd564fbb1 | -2.44928 | -47.10502 | 2026-01-04 05:08:00 | NPP-375D | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3234270f-7604-3fdf-b0a9-ff108c36f716 | -2.58026 | -54.72731 | 2026-01-04 05:08:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| fe34d4a6-eb33-3b3d-8f9e-8c89c37568cc | 0.67275 | -59.59028 | 2026-01-04 05:08:00 | NPP-375D | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 224a4f72-12ee-30c3-9b23-f1a26a7a6fdd | -1.8518 | -54.71541 | 2026-01-04 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 419b1005-30c0-3ce1-b4e7-e75d88587d52 | -2.85624 | -48.56396 | 2026-01-04 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 24ac2e7c-7641-3837-a073-6267d2a7998d | -1.40636 | -52.52603 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 269f9006-9196-3e87-9b1a-c34021eaeb67 | -2.45876 | -48.23391 | 2026-01-04 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| be8e6b9a-2f7c-392a-8fd5-4c38bbc3f63e | -0.09067 | -51.27819 | 2026-01-04 05:08:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 9.1 |
| 95bb230d-5d8e-3d9e-aa93-e68eecccd9f8 | -1.11938 | -53.44277 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 552a9a0b-f98f-3c32-b4b5-1a3aa271f075 | -1.21393 | -53.77933 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 157d136c-7dcd-3fc6-8498-77550c540873 | -1.52979 | -54.52329 | 2026-01-04 05:08:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3cf4ae6-60fc-3108-8783-3dbc97e427e0 | -1.19333 | -54.1055 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2805ae0b-7a4c-364e-a42e-72a9ccb73f8a | -2.77827 | -54.52764 | 2026-01-04 05:08:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 453bc84c-aedf-3ffb-b07a-9645aa9cb8a1 | 1.831 | -60.87225 | 2026-01-04 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1b25908b-e354-3c2c-a4c7-7713fa78914a | -1.6685 | -53.92561 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 6ed37b3f-9ec0-3d77-b4eb-66ef7d49464d | -2.79979 | -52.90479 | 2026-01-04 05:08:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| beea940b-770a-3a16-9384-d2f3e4421a7d | 2.54832 | -60.36342 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| 9b6948e6-a511-3628-9d07-146d111799af | -2.58259 | -51.90809 | 2026-01-04 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92e334e7-2d44-3c12-adef-0b71a202e614 | -1.35183 | -54.04858 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 34765433-61c6-3655-9c72-f4044aa92ac6 | -1.6088 | -55.16154 | 2026-01-04 05:08:00 | NPP-375D | CURUÁ | PARÁ | Brasil | 1502855 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 278d269d-7664-39b0-bd3b-0017f325de28 | 1.0775 | -60.38388 | 2026-01-04 05:08:00 | NPP-375D | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5e92bd33-bfc9-3c89-be81-b54ba2a46539 | -2.85175 | -48.56325 | 2026-01-04 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c1079e6e-ecec-3115-9f51-30e81b5f0838 | -2.46333 | -48.23463 | 2026-01-04 05:08:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7d9fb8e2-8eeb-3eec-80ce-fd1a8e101a81 | -3.49447 | -47.17109 | 2026-01-04 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 84741ea3-0c1e-35c5-89fa-7c863aab3402 | -2.11603 | -53.48158 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a40076a3-c5c9-3987-a8ee-cacd5cad6891 | -3.68392 | -52.03676 | 2026-01-04 05:08:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce88c984-a17b-344b-a168-6a80cc10dad8 | -2.18844 | -53.73455 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c56b82d5-1131-3573-a41d-3c580851230a | -5.55915 | -45.45224 | 2026-01-04 05:08:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 569ce328-3695-3b4f-adaf-5cff451bd313 | -1.19721 | -54.10255 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ef48008b-a1db-3f9b-bc64-c61fc706992c | -2.07326 | -54.25685 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 4cc93d91-9258-3877-a736-455ee3f13cf2 | 1.1263 | -60.5236 | 2026-01-04 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e93848d9-09ba-3b1e-a51a-ff331eae4b56 | 2.55439 | -60.56625 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 3.1 |
| e39edf3f-706e-3b28-84b2-d4bf0fb34692 | -1.82733 | -53.8028 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 8a951b5b-fab0-396a-b705-a4949b91fe7d | 1.12563 | -60.51929 | 2026-01-04 05:08:00 | NPP-375D | CARACARAÍ | RORAIMA | Brasil | 1400209 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c7e3cb4c-7c08-3491-807f-a40bed7f3bf7 | -1.14578 | -54.16906 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| fcf8bc87-5d0d-3970-8394-a12b5410c29a | -1.45423 | -53.3808 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da2e4f7a-689b-3317-b03e-3492b56463f7 | -1.90112 | -53.24919 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1179fdee-ead6-3072-8bb4-d729c51f3b9e | 2.55214 | -60.35842 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| cc44a7ad-2cfd-33e3-b1fa-dd8fb54339d2 | -1.22531 | -54.54662 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 770abe44-8160-30a5-9bb5-0b521cdf878d | -2.54092 | -47.47745 | 2026-01-04 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d087d62c-9e8e-3fd4-9d4a-8dced0084b2c | -1.10119 | -54.11254 | 2026-01-04 05:08:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2ae27125-d7f7-36ea-86f5-e11d90b58ee9 | -1.97078 | -53.35995 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f45d1cf8-15be-3e17-a498-f3e700f17edb | 2.54767 | -60.35904 | 2026-01-04 05:08:00 | NPP-375D | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 9.2 |
| f13c898a-cdf0-38eb-a7de-70e859c92cf9 | -2.82775 | -48.65914 | 2026-01-04 05:08:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3caa9aea-a0f8-366d-a32c-816628e6bcb9 | -2.11264 | -53.48105 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6fdc6e28-15a4-3b1e-a847-d4ab2ccce878 | -1.18374 | -53.7858 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5cb781a-589c-3a26-9bcd-c1be443e3ef2 | -2.44991 | -47.79129 | 2026-01-04 05:08:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3a9635f1-6e51-34c4-9d67-8afcd306b8e4 | -1.80308 | -55.48965 | 2026-01-04 05:08:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| b141baa1-df61-33ae-8917-b758da0a92f5 | -1.11882 | -53.44633 | 2026-01-04 05:08:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c2d6d08a-7e09-3536-a97b-9395e9aa746d | -3.49523 | -47.17041 | 2026-01-04 05:08:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3ddfb93e-2a38-3308-be90-c38dd64f4e9f | -2.47092 | -47.97012 | 2026-01-04 05:08:00 | NPP-375D | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a6a4cb29-16b0-3147-81cb-6028f08aed24 | -1.96738 | -53.35942 | 2026-01-04 05:08:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |


[Clique aqui para ver as próximas entradas](README5.md)
