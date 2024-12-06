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

## Dados Diários - Página 8

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b2b59989-4f44-3e6e-9863-0dc4ec2fbd2d | -1.53782 | -52.67844 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b86c4256-7b22-331d-ac7c-78c8faa739cc | -0.15951 | -60.86865 | 2024-12-06 05:14:00 | NOAA-20 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6b122648-c911-36d2-b3df-21d15139bdbe | -1.70696 | -52.79052 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3b7ff70-1997-397b-a36a-e40089420e2d | -1.70016 | -52.62284 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9fafe562-3da9-3e0d-9bed-ab03a9c4c73a | -1.51649 | -60.32516 | 2024-12-06 05:14:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f2a17581-e7aa-3675-9fef-dfcead795e27 | -1.67479 | -52.78563 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6936331-f72f-38db-9188-c50ec4463a28 | -3.82354 | -54.76395 | 2024-12-06 05:14:00 | NOAA-20 | RURÓPOLIS | PARÁ | Brasil | 1506195 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0e650e11-7637-34c8-b915-60ae113c87a1 | -0.58858 | -60.92501 | 2024-12-06 05:14:00 | NOAA-20 | NOVO AIRÃO | AMAZONAS | Brasil | 1303205 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 57144c60-cf5a-350b-a544-097fb6c19d19 | -3.06629 | -54.06794 | 2024-12-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 89801c1b-8400-3439-af06-3709641d94f7 | -1.69625 | -52.64788 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a81bd7f8-38dc-3ff6-85e6-50eba6818514 | -1.70822 | -52.79109 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 105d25cb-862e-3dc3-8f2c-04c88d52ba2d | -1.81179 | -52.73487 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c370f1d4-532a-33ca-9a9b-d785df3307dc | -1.51524 | -60.33299 | 2024-12-06 05:14:00 | NOAA-20 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 7a5d9c45-80f6-3d17-a97b-d8e53085da24 | -1.46954 | -52.6866 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c41c97b3-baed-39e5-a84d-1ca98d500917 | -1.69032 | -52.79157 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8e09c36d-4759-373f-a4fa-4040b863fb4a | -1.69576 | -52.57063 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 49ade4c4-e53f-3d02-8e9f-83158658b688 | -1.81583 | -52.73549 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| adac0bc1-4bba-3218-9eaa-b33e23e15619 | -1.67944 | -52.56815 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| d80bf5b5-96f9-3e50-bef1-8ea68ebad576 | -7.08138 | -45.20755 | 2024-12-06 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cb31333e-9267-3f75-8812-e9aa184cd16a | -1.70349 | -52.78642 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c0d46138-aa7e-35ce-b47f-50d145f099e8 | -3.57636 | -54.6954 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 81af21bc-57b1-3bb7-8650-8277440e58dd | -8.01883 | -47.69021 | 2024-12-06 05:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| fff20c46-9795-3823-8b36-da3e1c72bf97 | -3.60494 | -54.55136 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 87f2ecdf-7bfb-3952-9527-a20775b5f064 | -1.67732 | -52.74291 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| bbb16f16-ec78-325d-8185-9af135915efc | -7.08763 | -45.2151 | 2024-12-06 05:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a200facb-4134-3e5b-bf1c-6aabc804d069 | -3.60124 | -54.55075 | 2024-12-06 05:14:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| d814a886-b4f9-30f8-a4bd-1b9d0e93154c | -2.63847 | -54.37747 | 2024-12-06 05:14:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 69386783-f46c-3c2f-88d0-594a2438ffc4 | -1.70404 | -52.78292 | 2024-12-06 05:14:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a2db75f8-e3c3-35cc-bb26-d64309a8eb1a | -1.53378 | -52.67781 | 2024-12-06 05:14:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c592ca6-0bf6-3d01-91b2-3d4325fe94d3 | -11.82557 | -57.82743 | 2024-12-06 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| af8d6103-5c8e-3385-a158-ca4f0b729cc9 | -11.32156 | -54.04865 | 2024-12-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a97d994-93b2-3cb4-a073-a7ba109e3374 | -10.76668 | -54.78223 | 2024-12-06 05:16:00 | NOAA-20 | NOVA SANTA HELENA | MATO GROSSO | Brasil | 5106190 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 36d5c492-3d81-311e-8a65-b40cfbf49733 | -13.92265 | -59.60905 | 2024-12-06 05:16:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| d4a0b36a-b54f-3185-a96c-5f7e4861909f | -11.73347 | -54.30945 | 2024-12-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 034760b0-1ce7-3d29-b76b-6094b7496349 | -12.2438 | -52.45934 | 2024-12-06 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7a375150-1c7b-3fd8-a4bf-a311b99c41be | -11.72871 | -54.31277 | 2024-12-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 119b6eb8-76eb-3290-aeae-e603dc8c7e93 | -11.72926 | -54.30883 | 2024-12-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 6f7ebd5d-4ec3-3145-80d3-a71d31b65568 | -11.82614 | -57.82357 | 2024-12-06 05:16:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2133e405-15ce-3541-9857-fb4d5380caa3 | -11.73292 | -54.31339 | 2024-12-06 05:16:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 83fe1898-ca08-3e2c-aa8b-90438b43bff1 | -12.24313 | -52.46464 | 2024-12-06 05:16:00 | NOAA-20 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d293c568-39ea-3d77-956d-b6c23acb0643 | -1.6786 | -52.5642 | 2024-12-06 05:27:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.4 |
| 4d310962-2978-3482-a1b1-7ef5ea93e6cf | -1.66826 | -52.55737 | 2024-12-06 05:27:00 | AQUA_M-M | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 669374f5-f6cd-335a-b4ec-04f104f6ad5e | -7.08679 | -45.21182 | 2024-12-06 05:27:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| a3813cc0-b5cb-3038-a29b-ebf9c078bfaf | -6.86486 | -44.76503 | 2024-12-06 05:27:00 | AQUA_M-M | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.3 |
| c1a94cb5-9137-31fd-aa60-92561f6a4596 | -7.07901 | -45.20097 | 2024-12-06 05:27:00 | AQUA_M-M | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 57ec649f-0fea-39b5-8cb6-6ca9cbdc89d2 | -12.85717 | -51.93063 | 2024-12-06 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 11.4 |
| 5bc8abbf-4c8c-3f0e-92cd-b899857dcd24 | -12.85517 | -51.94312 | 2024-12-06 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 5.5 |
| 20aa443c-c3c3-3a99-a761-ac8bd74b9b06 | -11.73031 | -54.29761 | 2024-12-06 05:29:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 15.3 |
| 46401bc4-3c27-31d8-95c1-15baf169869f | -11.73165 | -54.30309 | 2024-12-06 05:29:00 | AQUA_M-M | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 20.0 |
| 753a588a-6693-34a3-baf8-48cd10ed4902 | -12.85432 | -51.93571 | 2024-12-06 05:29:00 | AQUA_M-M | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 12.4 |
| df7ddffc-97c0-39de-9b43-63e4e9e15a7b | 2.42965 | -60.64998 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5fabc8a4-f26f-3019-9ab9-eefd3e58f0e4 | 0.75157 | -59.65762 | 2024-12-06 06:05:00 | NOAA-21 | CAROEBE | RORAIMA | Brasil | 1400233 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 68b6b355-bff7-36a4-ae6c-c2454d13310a | 2.01966 | -61.46609 | 2024-12-06 06:05:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 90d23a5f-2ae5-3011-a8e3-c8d587bf7aff | 2.01403 | -61.46376 | 2024-12-06 06:05:00 | NOAA-21 | IRACEMA | RORAIMA | Brasil | 1400282 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 23697089-10db-3686-8425-4f61c7d719fa | 3.14121 | -60.49055 | 2024-12-06 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fd3322bb-9843-3683-a73e-d41707e0ecba | 2.42372 | -60.64745 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8228a36a-78d2-33fa-85a0-41229d49ea51 | 3.23757 | -61.0307 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2be0033-0560-3a68-af25-19c380303ddb | 3.23633 | -61.03529 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ff04ddf7-6f3e-30f7-80fd-e81b54a76a64 | 2.42428 | -60.65081 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 51140888-b10b-3f77-ac22-2b3cc038ad14 | 3.23533 | -61.029 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 942d0d8c-ffbf-31b3-b445-a7277569f6c6 | 3.13816 | -60.49158 | 2024-12-06 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 0.5 |
| d3cea996-2c42-3b87-afcb-4295a8c0a699 | 3.23189 | -61.02848 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 12d7ff76-9188-31c0-8392-791cdc49cd49 | 3.23294 | -61.03472 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 144262cb-0178-3263-b6bb-67ac40975f6b | 2.48078 | -60.69344 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 436d963c-ae81-3c5c-b882-178e0ef0ad4b | 2.48024 | -60.6901 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b58354da-5ab5-365b-8ecf-eb8005a8cb08 | 2.47544 | -60.69438 | 2024-12-06 06:05:00 | NOAA-21 | CANTÁ | RORAIMA | Brasil | 1400175 | 14 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e9ff8ace-4072-39d8-b65a-27cfc8eb22f9 | 4.32485 | -60.7911 | 2024-12-06 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.7 |
| bcdfd409-8305-3e63-94c2-d6661c6290ce | 3.23583 | -61.03214 | 2024-12-06 06:05:00 | NOAA-21 | ALTO ALEGRE | RORAIMA | Brasil | 1400050 | 14 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 68729022-4208-3c31-b3ba-3a66e411d480 | 4.32536 | -60.79417 | 2024-12-06 06:05:00 | NOAA-21 | PACARAIMA | RORAIMA | Brasil | 1400456 | 14 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c2fd5045-9260-317f-917c-790f5672f483 | 3.14296 | -60.48725 | 2024-12-06 06:05:00 | NOAA-21 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 5fd7346b-c336-33e6-963b-cedb6c8caaad | -0.15726 | -60.86868 | 2024-12-06 06:07:00 | NOAA-21 | RORAINÓPOLIS | RORAIMA | Brasil | 1400472 | 14 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 50cfdd09-1ca6-3403-9c34-1763aa322054 | -7.70891 | -73.09319 | 2024-12-06 06:09:00 | NOAA-21 | RODRIGUES ALVES | ACRE | Brasil | 1200427 | 12 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 1a248c6a-0157-3ff5-be19-6218778cd4d9 | -4.4749 | -44.232 | 2024-12-06 07:30:00 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 106.5 |
| cfded9c5-0581-3f05-a1ec-3db1ea8c7949 | -4.475 | -44.2091 | 2024-12-06 07:30:00 | GOES-16 | PERITORÓ | MARANHÃO | Brasil | 2108454 | 21 | 33 | nan | nan | nan | Cerrado | 68.9 |
| 62041050-da88-3af2-ac1c-9a8557d0605a | -17.4 | -44.93 | 2024-12-06 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 8e0f747c-52f9-35b9-9d9a-30c72dcfa321 | -17.4 | -44.88 | 2024-12-06 11:00:00 | MSG-03 | PIRAPORA | MINAS GERAIS | Brasil | 3151206 | 31 | 33 | nan | nan | nan | Cerrado | nan |
| 1f4fcd79-7e3d-3cf4-a7b9-7ba378ba1d36 | -4.93848 | -43.6214 | 2024-12-06 12:57:00 | TERRA_M-T | SÃO JOÃO DO SOTER | MARANHÃO | Brasil | 2111078 | 21 | 33 | nan | nan | nan | Cerrado | 29.4 |
| 5b184084-0963-3b7f-92d0-b6f47aa7accc | -4.16077 | -43.07071 | 2024-12-06 12:57:00 | TERRA_M-T | COELHO NETO | MARANHÃO | Brasil | 2103406 | 21 | 33 | nan | nan | nan | Cerrado | 240.3 |
| 5aef5cce-0c97-3345-9388-ca242bd96812 | -5.99082 | -41.83166 | 2024-12-06 12:59:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 70.9 |
| 5193fcb2-7507-380e-a07d-7088ddd18a35 | -8.28096 | -48.02608 | 2024-12-06 12:59:00 | TERRA_M-T | ITAPIRATINS | TOCANTINS | Brasil | 1710904 | 17 | 33 | nan | nan | nan | Cerrado | 13.5 |
| d95776e5-7f97-3827-9b52-583512d3976a | -12.63961 | -47.54895 | 2024-12-06 12:59:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 54.4 |
| 70707b64-b09d-3220-b975-41cc766bab9c | -12.64163 | -47.53246 | 2024-12-06 12:59:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 45.3 |
| ddb88892-f889-33e4-bc21-0653ebdced39 | -6.46507 | -47.54359 | 2024-12-06 12:59:00 | TERRA_M-T | AGUIARNÓPOLIS | TOCANTINS | Brasil | 1700301 | 17 | 33 | nan | nan | nan | Cerrado | 8.5 |
| dc077cfb-bd28-32ed-b724-bf5328489bf3 | -5.99647 | -41.83777 | 2024-12-06 12:59:00 | TERRA_M-T | SANTA CRUZ DOS MILAGRES | PIAUÍ | Brasil | 2209153 | 22 | 33 | nan | nan | nan | Caatinga | 55.7 |
| 011aa09b-5110-3676-b615-9938141c48ab | -13.1948 | -52.65611 | 2024-12-06 12:59:00 | TERRA_M-T | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| 66c64021-b926-39a8-b335-5bbf9e701c52 | -7.0933 | -45.20206 | 2024-12-06 12:59:00 | TERRA_M-T | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 31.2 |
| d69ed34e-658e-32d6-95ca-7f2bfacf3f95 | -12.0618 | -46.69943 | 2024-12-06 12:59:00 | TERRA_M-T | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 8bafe207-bed9-32b9-96bf-bc3fa4150b9a | -6.76019 | -46.52594 | 2024-12-06 12:59:00 | TERRA_M-T | SÃO PEDRO DOS CRENTES | MARANHÃO | Brasil | 2111573 | 21 | 33 | nan | nan | nan | Cerrado | 43.5 |
| 7f53f00d-7335-30be-8732-1dab1a0215ad | -11.67828 | -54.25612 | 2024-12-06 12:59:00 | TERRA_M-T | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 4a2f3888-d632-3330-a154-68db0e5509c3 | -12.50107 | -51.76328 | 2024-12-06 12:59:00 | TERRA_M-T | BOM JESUS DO ARAGUAIA | MATO GROSSO | Brasil | 5101852 | 51 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 41585ac7-77ba-34cf-9c5d-8803d9888a71 | -11.8118 | -54.04064 | 2024-12-06 12:59:00 | TERRA_M-T | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.1 |
| bc243cf2-69b0-39f0-abb4-8a420aabee4e | -6.17053 | -45.95566 | 2024-12-06 12:59:00 | TERRA_M-T | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 20.2 |
| 723aae24-17d1-382b-ad15-c81593932bca | -15.44866 | -43.65197 | 2024-12-06 12:59:00 | TERRA_M-T | VERDELÂNDIA | MINAS GERAIS | Brasil | 3171030 | 31 | 33 | nan | nan | nan | Caatinga | 49.3 |
| a6812ea9-fa73-3838-9824-2e66a72e5f19 | -7.66494 | -49.10637 | 2024-12-06 12:59:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.7 |
| 03ccf842-c1bc-314d-9180-76fb40da8ba1 | -12.86505 | -51.93148 | 2024-12-06 12:59:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| e9360747-6cf4-3043-9d22-f157d1aa7a56 | -12.59707 | -51.73572 | 2024-12-06 12:59:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 9.0 |
| a6e3e88b-d7bd-319b-96c8-42dc51933e7b | -6.12164 | -46.92333 | 2024-12-06 12:59:00 | TERRA_M-T | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 69512851-765e-32ea-866f-b6f784824ca6 | -10.41592 | -49.24247 | 2024-12-06 12:59:00 | TERRA_M-T | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 20.4 |
| c8ddf7de-83a9-344f-8d57-f1df942f4c18 | -7.66347 | -49.1171 | 2024-12-06 12:59:00 | TERRA_M-T | ARAPOEMA | TOCANTINS | Brasil | 1702307 | 17 | 33 | nan | nan | nan | Amazônia | 6.9 |
| c84e93e2-a2d3-37a6-8ac9-fc861302302a | -13.52975 | -48.21897 | 2024-12-06 12:59:00 | TERRA_M-T | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 12.1 |


[Clique aqui para ver as próximas entradas](README9.md)
