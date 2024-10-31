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

## Dados Diários - Página 39

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 732cc256-f35d-3afc-919b-7caddd32bed7 | -17.56953 | -52.40092 | 2024-10-31 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 8b6b8cb9-b49d-39af-940a-e36cd2058576 | -17.56894 | -52.40504 | 2024-10-31 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 7d68f831-5d88-3869-807d-76d1fc8770aa | -17.56599 | -52.40038 | 2024-10-31 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 0fa331f1-a348-3987-9059-9ac5ba1dfac5 | -17.5654 | -52.4045 | 2024-10-31 04:51:00 | NOAA-20 | MINEIROS | GOIÁS | Brasil | 5213103 | 52 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 9b07c526-f22f-3adb-b718-b72a23caac35 | -16.41908 | -54.83822 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 4b047377-c1d7-33f4-9b11-a7d8f6f49af3 | -15.09947 | -54.59085 | 2024-10-31 04:51:00 | NOAA-20 | CAMPO VERDE | MATO GROSSO | Brasil | 5102678 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 434bdc8a-7e08-3365-b14f-9bdf98045e23 | -16.97655 | -54.81328 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 36360d67-c529-34c6-97ff-3c8ad80ed00e | -16.97599 | -54.81688 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 343c67bf-f917-315f-aafb-df287dfaf580 | -16.97268 | -54.81632 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| a6e7eb05-c8cb-3a30-9f3d-3150b796de46 | -16.97212 | -54.81992 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 9c0ff531-982d-3732-a60d-6b1def6bed32 | -16.96881 | -54.81936 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| c5e8a481-2616-3caf-93e6-e79cf908b60a | -16.96052 | -54.82903 | 2024-10-31 04:51:00 | NOAA-20 | RONDONÓPOLIS | MATO GROSSO | Brasil | 5107602 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8d8c1769-1f82-39f7-afd7-676d49dd80c7 | -11.78636 | -55.12625 | 2024-10-31 04:51:00 | NOAA-20 | SINOP | MATO GROSSO | Brasil | 5107909 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0d7f7ad-f1e9-3fe9-a771-be9ca86d2a6f | -11.3198 | -54.02292 | 2024-10-31 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| da3e4670-7ff1-332a-a7e9-d3735fdec112 | -11.31924 | -54.02642 | 2024-10-31 04:51:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 375e1533-5e66-3bab-aa9f-41369a8670af | -16.55587 | -56.23518 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 479486a1-c411-38a0-88b4-26f3158043dc | -16.55527 | -56.23887 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| f1afceaa-149b-3751-90d6-3b7fa777ac64 | -16.55252 | -56.23459 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| fdc84e34-0dc7-3bf2-b0c3-670b26d99d8c | -16.55192 | -56.23829 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| ff0c3ab2-9156-3996-b8d8-93c01ece71e5 | -15.8244 | -56.38866 | 2024-10-31 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f84af2a7-0340-3413-bcd7-68d8f2f84e09 | -15.82102 | -56.38806 | 2024-10-31 04:51:00 | NOAA-20 | NOSSA SENHORA DO LIVRAMENTO | MATO GROSSO | Brasil | 5106109 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 65d47ab1-1d26-3b2e-84fa-8cc1cfa8dd05 | -16.56687 | -56.2523 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 5f80e24f-e3f2-35f3-8f9f-7ff365305538 | -16.56352 | -56.25172 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 45b7c089-2a3a-3e24-bdf8-376371820b82 | -16.56016 | -56.25112 | 2024-10-31 04:51:00 | NOAA-20 | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 60f348c0-d655-38e7-9912-4219652e6d60 | -14.71804 | -56.7321 | 2024-10-31 04:51:00 | NOAA-20 | ALTO PARAGUAI | MATO GROSSO | Brasil | 5100508 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 70131874-0c9b-390a-87e8-ec91821fa43d | -14.62049 | -57.45986 | 2024-10-31 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1576d538-4ed4-3957-8d23-8b8ee2badfd7 | -14.61979 | -57.464 | 2024-10-31 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9699d332-01ed-3712-af8a-6e85c09823ad | -13.92124 | -56.26606 | 2024-10-31 04:51:00 | NOAA-20 | NOVA MUTUM | MATO GROSSO | Brasil | 5106224 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c950ee3e-52c0-3bb1-9563-c098ca22304a | -16.46772 | -57.58899 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 9d1a8e7b-08b2-3d72-8382-4a57564943d9 | -16.42359 | -57.20416 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| efb8bfe5-c925-3a29-b085-bc2a63f55726 | -16.16999 | -56.78603 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 88e83341-738f-3efc-b390-c59467accf06 | -15.64491 | -57.6674 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 36150a43-3443-392d-a9c5-20150499dbe5 | -15.62841 | -57.50853 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| abf89f06-79df-352d-965f-1b448c9ab707 | -15.46006 | -57.51716 | 2024-10-31 04:51:00 | NOAA-20 | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 857fcf82-746d-3a85-b70c-4f66ed678314 | -15.79084 | -56.61517 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ca08aae0-fc46-357c-a3cc-dbccb6e462a7 | -15.79022 | -56.61894 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9dd94f30-8835-32a8-95d6-7f25ff19164d | -15.78745 | -56.61452 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 0ec38672-afa8-3d87-bb34-33a85447e640 | -17.04136 | -57.43734 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0f3fa2c6-d4dc-34e4-b524-a213f88fc747 | -16.97397 | -57.53991 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 063172b2-a581-3072-b48a-3d5dc111af0a | -16.92476 | -57.6594 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 581fd39f-c22b-38f6-b772-06d4f9eeca40 | -16.92372 | -57.66002 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.4 |
| b4da721c-5420-3902-ad31-f28d93e16340 | -16.92022 | -57.65937 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9d877ec9-70ca-3a30-a4da-8dbbc58f9358 | -16.91673 | -57.65873 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9d5847b3-51ae-30ea-af7a-7e1b672f9f2b | -16.89865 | -57.5103 | 2024-10-31 04:51:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.8 |
| 939e6387-689b-393c-a416-f4defd87e5f0 | -16.8301 | -56.70102 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 67d3e9fc-e846-323f-bdbd-5d2a78d4d56f | -16.8292 | -56.6853 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4e9e2f73-f6fc-3d0d-bf89-6b31e448a85b | -16.82796 | -56.69286 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 278e7792-3cc9-311a-9cab-6cf8530d0175 | -16.82706 | -56.67715 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 055a7528-4294-303f-a1e1-adecb92c045f | -16.82457 | -56.69225 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 071756b3-c523-3bf1-bf8c-c23b1b365717 | -16.82395 | -56.69603 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.0 |
| c15bc40b-fa32-322f-9711-19bb7d7f55c7 | -16.82057 | -56.69543 | 2024-10-31 04:51:00 | NOAA-20 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0bfb8f3c-3ecb-39ca-9852-c8d13fe7eade | -9.74721 | -57.98549 | 2024-10-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 500a102c-f3aa-3929-8fb2-8ac206806fec | -9.74637 | -57.99044 | 2024-10-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a27d8a79-36d5-3835-af81-2ee17a5c086a | -9.74617 | -57.9445 | 2024-10-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 32459d82-4e46-3054-afdc-e7d821d47f9b | -9.74229 | -57.94384 | 2024-10-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 44e4e851-672f-35a4-b1f7-9ffc1b4d1ce9 | -9.7384 | -57.94316 | 2024-10-31 04:51:00 | NOAA-20 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 61e274a6-a07f-3c13-8d2b-2c3cbcef1c28 | -10.39196 | -57.50256 | 2024-10-31 04:51:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d26fa08e-21a7-38d8-8d47-c6e354f7d563 | -15.16205 | -58.2226 | 2024-10-31 04:51:00 | NOAA-20 | RIO BRANCO | MATO GROSSO | Brasil | 5107206 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| e4ab34e1-c81f-371c-92b1-1d7fdeb086da | -14.90154 | -57.77055 | 2024-10-31 04:51:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| dbca8106-3273-30b5-b4ef-519dbe182d40 | -16.2117 | -59.33438 | 2024-10-31 04:51:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| cc2a2b9b-6db6-3fc8-861a-7f7e72c6f933 | -16.20395 | -59.16391 | 2024-10-31 04:51:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 56c065ae-d27b-3de6-b4d3-8ecdb8b7ac3f | -15.65761 | -59.15273 | 2024-10-31 04:51:00 | NOAA-20 | PORTO ESPERIDIÃO | MATO GROSSO | Brasil | 5106828 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fecdf43d-768a-33b3-9ee1-f5d32c9fcb2b | -15.92315 | -59.58963 | 2024-10-31 04:51:00 | NOAA-20 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e013a91b-bb96-3752-859c-c8116a2eb27a | -12.42926 | -63.27966 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| e901579f-53bb-3693-be7c-fa78bb65dace | -12.42869 | -63.27719 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 4c49847f-2767-3e2d-861e-554ce003c154 | -12.42863 | -63.283 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f76cff87-bdbd-362a-b33a-9b3c597a3d35 | -12.42804 | -63.28053 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 347a27fa-abd2-3df4-8168-fb45691f29e6 | -12.428 | -63.28635 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 4312251e-3753-392d-8ee2-21d639fef09f | -12.42738 | -63.28387 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 1b3995cc-c011-3514-86a3-166a7642cfb0 | -12.42399 | -63.27857 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 36f67c43-3fd0-39e5-a5de-87b0af33b736 | -12.42336 | -63.28191 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| e2191e8d-8ce0-364b-aabc-7c662a9f72b7 | -12.42277 | -63.27946 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 6.0 |
| fc86a714-d00c-3edc-8707-58e6f5e074b8 | -12.42273 | -63.28526 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 04ff508e-e20a-3c79-8230-96f277773d90 | -12.42211 | -63.28279 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 8.1 |
| 48d6eeb9-5b10-3e00-8f14-63f0aba94aa7 | -12.41936 | -63.27414 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 119a361e-8874-3b9d-93b7-ca93f3bc3c13 | -12.41873 | -63.27747 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b90f8a96-076a-385e-af3a-a1a8c8fe3544 | -12.41816 | -63.27504 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 050ae507-b565-3142-8d6c-9d686c10f42c | -12.41809 | -63.28082 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 288ede3c-27c9-359e-9bbc-252bd5d5c7e7 | -12.4175 | -63.27838 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c209989d-af1e-3b26-a52c-5d58b898738c | -12.41685 | -63.28171 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3889d3f9-510e-328b-85e5-99d7474ac2af | -12.41346 | -63.27637 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e1f7669d-6e68-3386-9bae-d0dfc8f18881 | -12.41283 | -63.27972 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 04cdda10-851d-3ccf-8d74-ec66f82c98f7 | -9.8628 | -63.98182 | 2024-10-31 04:51:00 | NOAA-20 | BURITIS | RONDÔNIA | Brasil | 1100452 | 11 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 11b045cd-23f9-39cb-a25c-57a93c5009df | -9.29984 | -64.25682 | 2024-10-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 3.9 |
| be9f2048-d12e-3ba6-83d0-4b8ca95450b4 | -12.32132 | -63.58519 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e744816e-ce83-39e6-860f-59b795381261 | -12.31594 | -63.58408 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4acc724a-8f8d-33b4-8413-8cffa13a8990 | -12.31526 | -63.58759 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1eb58ff1-e6ac-3e46-a4d5-92db69c2becd | -12.30988 | -63.58647 | 2024-10-31 04:51:00 | NOAA-20 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a210eccc-a3b6-380b-8a84-fd5786a8fc67 | -9.05147 | -64.45749 | 2024-10-31 04:51:00 | NOAA-20 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 89df13dd-067d-3817-8e2c-23fe72c1b4e0 | -10.68752 | -65.00337 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 909d0b91-5e75-3afe-a005-e9162237b2ed | -10.68731 | -65.00138 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| bdce65f5-2ca6-3cde-87a9-e4bc415a1f2d | -10.68641 | -65.00609 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.7 |
| e1343a09-569f-3f6d-999f-5591e0903047 | -10.68241 | -64.99741 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 5.8 |
| 5a4d5ca5-7bac-3d6c-aac4-0d408392021c | -10.68217 | -64.9954 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 954b2dab-f7d2-3041-9e39-497c448a62c6 | -10.68147 | -65.00216 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7b604e60-4dbd-390f-9bc3-db21641fa514 | -10.68125 | -65.00017 | 2024-10-31 04:51:00 | NOAA-20 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 3.0 |
| b57f0bb0-6734-31a1-82c9-10ec4e1dc572 | -20.47455 | -46.57826 | 2024-10-31 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3d788d41-5f15-3bba-ada0-c8df4eee1b5d | -20.47421 | -46.58152 | 2024-10-31 04:53:00 | NOAA-20 | DELFINÓPOLIS | MINAS GERAIS | Brasil | 3121209 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 55b679fa-9a4e-3f53-8b08-da79f41c3782 | -20.95405 | -47.17014 | 2024-10-31 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 82930904-aedf-38cc-a23f-2553030cc686 | -20.9537 | -47.17331 | 2024-10-31 04:53:00 | NOAA-20 | SÃO SEBASTIÃO DO PARAÍSO | MINAS GERAIS | Brasil | 3164704 | 31 | 33 | nan | nan | nan | Cerrado | 6.5 |


[Clique aqui para ver as próximas entradas](README40.md)
