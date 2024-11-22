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

## Dados Diários - Página 50

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f327428a-0ff2-30a7-ab98-14e18cc9dac6 | -1.77839 | -54.92292 | 2024-11-22 04:36:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 73b4e2eb-47a2-3983-ba3c-e6297d286ef6 | -1.18967 | -51.95368 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.9 |
| 50617cb2-09ad-366c-8d24-4bba18b9b833 | -3.59974 | -51.4738 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3d935a10-26a6-37af-962c-44b4632d9391 | -2.76839 | -54.07084 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b914a035-3c40-3a85-962f-5c66292c8f6e | -2.73847 | -47.54209 | 2024-11-22 04:36:00 | NOAA-20 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30217992-9576-3aca-a8ee-f24a449fcd91 | -1.13368 | -53.40253 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 8.9 |
| d43d3533-7ffb-3b34-a263-f5a5a3a53084 | -2.7044 | -46.23248 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dc039879-6d17-3351-b2da-f8b9033be683 | -4.18953 | -53.58255 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 10097c4d-88e3-3d10-a259-af66790d0e50 | -2.88108 | -53.96656 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2da5c5d-bdfb-35aa-b51f-7db27805c78a | -1.07663 | -53.36906 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 2ddefd39-05bd-38bb-b5d8-1c054d37ee60 | -2.56692 | -46.55502 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 18996139-a343-3f6f-9d02-e74fa84e39a2 | -0.95671 | -51.71811 | 2024-11-22 04:36:00 | NOAA-20 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 9eceff08-09e9-3ec1-ac95-558f2f63cf27 | -2.65319 | -46.13907 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3a6cc59-1618-3573-8260-b38e7ef26679 | -1.92292 | -47.0661 | 2024-11-22 04:36:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 4973b21a-4b3e-3d89-9ad1-5416a9609866 | -3.99959 | -54.33942 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c138832b-a272-3540-b66e-6a55a0b7f143 | -1.57851 | -52.93195 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 19c285db-54fd-33d1-a752-15a610dcce72 | -2.35139 | -48.55817 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 8.1 |
| ba0951df-669b-3f23-8cb8-91c6ebba1f76 | -3.60106 | -51.55564 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a7e14a1-8485-3d15-8ee8-57ee823236d1 | -3.2138 | -53.84365 | 2024-11-22 04:36:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bb884497-810d-3111-9495-fc35b1dbe33f | -2.52724 | -46.36156 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 3306b3c7-4941-3d42-a6d5-93ef1465e90e | -3.00353 | -51.55801 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a5da37b7-3db9-3f2e-b61e-42e46fc5b524 | -2.60345 | -48.29483 | 2024-11-22 04:36:00 | NOAA-20 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 901b4bba-f384-3ba8-9390-a49f1520d7f1 | -3.57052 | -54.68252 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 6.3 |
| d1782150-d3fc-3ea6-b1b1-6fa9586a3b72 | -2.25356 | -48.70462 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 2105675f-23da-3431-bcf3-745c9e0b6c2c | -2.24213 | -50.47134 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bd94d81-4a20-3e21-9ad2-6668601cd7b5 | -4.07987 | -54.05663 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cd819437-7635-3535-9511-279077c59156 | -2.14276 | -50.70275 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c275cc60-708e-3107-b52c-e98269168d66 | -2.55437 | -46.54548 | 2024-11-22 04:36:00 | NOAA-20 | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6217c475-5645-3bb2-abb3-96fe80faebc1 | -3.47132 | -54.5459 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 233b7f80-0621-3193-bb76-31244757f1ea | -1.48248 | -47.23352 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8a4a5a74-03d2-3e59-aa2b-586320fc93aa | -2.15265 | -50.46159 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f63b169b-23ba-3364-ae86-841bec24fdb9 | -2.61044 | -54.54073 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| dbf0336c-b2fb-3399-b940-253a09aea77e | -1.12552 | -53.40129 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c1490e0c-cb61-3892-9a56-78abef7d0234 | -3.91149 | -52.2558 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| a0d37fd7-a14a-3cf7-bc2f-6dedd6a3d81a | -4.88452 | -50.50333 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 8c387c09-54ed-32af-be7c-3ad4122fb70f | -4.58181 | -48.02431 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 3fbbe751-a630-3efa-b822-442e7c440243 | -1.65285 | -52.69471 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 33182e56-ae5d-3142-9969-95736a60cc96 | -2.22293 | -46.39998 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d67c024-3142-3240-9848-76e36ced25dc | -3.74626 | -52.33036 | 2024-11-22 04:36:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0d4a3d43-bebc-3806-9edb-ada5f7077aa1 | -1.63204 | -52.4178 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7f67b475-90d7-3d86-a5ce-11a02dea6882 | -2.303 | -48.49782 | 2024-11-22 04:36:00 | NOAA-20 | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 201b9a9c-b2cd-371c-b390-526f8783f74b | -3.62178 | -45.77129 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d79c031e-4820-3f13-b43d-2ab39550040f | -1.73195 | -52.39801 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 53fb5aba-6b94-32f3-a03e-d92687848e59 | -3.2323 | -54.26062 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| 5e29e4e2-1c54-31e6-a3a4-e4ef8244de69 | -2.65586 | -46.56815 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 07a952ac-1e93-38d5-9569-e0bab9c96aff | -2.43617 | -46.53883 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e13d9227-14c1-3edf-9caa-f07189279a52 | -2.22424 | -50.85188 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e6c9421-ffdd-3920-9c26-0a7b06da5e9a | -2.43084 | -49.02478 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 482ca4bc-b000-3d55-bfbd-afb1da71e723 | -3.81789 | -51.87889 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c3c7d831-6009-3cec-9ee7-5f4dceefd049 | -3.22448 | -54.24786 | 2024-11-22 04:36:00 | NOAA-20 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 7.1 |
| e3983d0f-2b38-3309-9e5a-50dfecb650a0 | -4.40271 | -50.73293 | 2024-11-22 04:36:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 548c3106-0386-31b7-9638-e5617740b147 | -1.46849 | -51.11951 | 2024-11-22 04:36:00 | NOAA-20 | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 010f105e-a4c4-3dc2-9e58-e662a610969a | -3.05053 | -51.33055 | 2024-11-22 04:36:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d78a6e47-6179-356a-bfa2-52901f12d41e | -1.41275 | -52.0468 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2887ead3-4766-3fa0-8002-9d06d647069d | -2.10333 | -50.13038 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 164936a4-e9df-35ec-8ea7-bdd7db81b943 | -2.10672 | -50.13091 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fa01c182-bd18-3ecd-b084-ae612d53f89e | -4.0684 | -46.83649 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e70f645-434c-312a-8c79-efd5da2c45cb | -3.75601 | -46.12377 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| fae56028-f09d-3f96-bb01-ff6555a3b398 | -2.44917 | -49.05952 | 2024-11-22 04:36:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1779027b-2ee6-3189-9ca6-d9904c0e9e00 | -2.68833 | -46.17517 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1690cd69-eaa8-345b-8070-faeb4c779cbb | -2.43902 | -46.54306 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| a68f4c33-c146-3a68-98a6-ea9f71024bd1 | -1.58889 | -53.81001 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 13.1 |
| 507e1ab6-1bbd-3ad1-9608-0002cdf64ef8 | -3.82816 | -52.26229 | 2024-11-22 04:36:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 7.4 |
| a25c5005-ed28-3817-9d3e-36588d855341 | -4.24903 | -46.11698 | 2024-11-22 04:36:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 444ab452-0917-37ff-a8a5-bfe72288d9e8 | -0.30189 | -51.48185 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 42612f7f-afa0-3ab3-8a08-bf3f838c3941 | -3.34749 | -42.78689 | 2024-11-22 04:36:00 | NOAA-20 | SANTA QUITÉRIA DO MARANHÃO | MARANHÃO | Brasil | 2110104 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| b80146ad-096f-3d9c-8c0e-705c4356722e | -3.75249 | -46.12323 | 2024-11-22 04:36:00 | NOAA-20 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 1cf27e6f-6ed8-3c97-beba-bfef39db51f0 | -1.51573 | -47.06548 | 2024-11-22 04:36:00 | NOAA-20 | OURÉM | PARÁ | Brasil | 1505403 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 336703df-1d68-3766-8030-24eafe2bb7dc | -3.98353 | -49.99379 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 05a74337-a341-37f9-866b-c724e2bc1d18 | -1.59359 | -52.93632 | 2024-11-22 04:36:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| de67bc51-5edb-3b24-aea3-18952d8f5ddf | -2.65644 | -46.56444 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8815abc1-f85e-30a9-a420-2a946a998445 | -1.82763 | -46.28371 | 2024-11-22 04:36:00 | NOAA-20 | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9aedd023-625e-3cb0-bced-84dd61d340f1 | -5.24577 | -42.63349 | 2024-11-22 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| 56529de5-6f39-39c0-9b44-fe7d44672020 | -1.78829 | -53.63704 | 2024-11-22 04:36:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| a6692523-d62d-3cb3-9961-7b0dc6c14c36 | -2.22031 | -50.38859 | 2024-11-22 04:36:00 | NOAA-20 | BAGRE | PARÁ | Brasil | 1501105 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 56152cd0-65c4-329a-b635-64cbed435e22 | -3.25285 | -50.40092 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| fc9a3d63-1646-3488-bf2d-4ce83986dd29 | -0.94232 | -51.64684 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ec8f5254-342c-332e-885e-0604a771c7eb | -6.38737 | -47.15096 | 2024-11-22 04:36:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| cb8dad74-dc4b-3476-b204-4850c6b68483 | -2.60338 | -46.25301 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 384c1e65-d169-3c3c-8f0f-20f3adcc47f5 | -3.91888 | -46.40259 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8e6de07f-6d0c-355a-9e55-b93057fd58d1 | -2.44813 | -46.55204 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6653424f-d633-349e-afbe-020936fd8a70 | -3.03908 | -54.84985 | 2024-11-22 04:36:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| cd9f48d0-517f-31f6-8def-469874b2113b | -3.00562 | -45.12927 | 2024-11-22 04:36:00 | NOAA-20 | MATINHA | MARANHÃO | Brasil | 2106508 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 98fe0fc7-8de6-3169-a389-089629a7d4d5 | -2.11282 | -50.60114 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b0641b31-cc95-3290-8143-666f24aa8f3a | -1.67225 | -47.38791 | 2024-11-22 04:36:00 | NOAA-20 | IRITUIA | PARÁ | Brasil | 1503507 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 525f4ee8-25e4-30d5-914f-6f260f777be9 | -4.17991 | -46.56652 | 2024-11-22 04:36:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 646d5a7a-dab4-3219-b217-9dc2934b2163 | -1.33509 | -51.85523 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 78baed47-c1a7-3b6c-9548-5f95b17925e4 | -4.00415 | -49.92841 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9e6dac85-f55f-3da8-80e4-f6e8a47144e9 | -2.69968 | -46.26299 | 2024-11-22 04:36:00 | NOAA-20 | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| ba9dbdd6-f0fb-3be0-a8d5-2f42612562b7 | -2.43447 | -46.52716 | 2024-11-22 04:36:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cabd2fe8-d2df-343b-95b0-b28bf8bbcbe1 | -2.26222 | -50.45545 | 2024-11-22 04:36:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b3c705df-fc67-382e-a3d4-30a56c687e6d | -2.21308 | -49.8627 | 2024-11-22 04:36:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| fe2a703d-bb21-3dd5-9266-546181617133 | -4.11987 | -54.34553 | 2024-11-22 04:36:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9a02d604-8eec-3ae3-bf06-3d2db155aa40 | -4.00526 | -49.92138 | 2024-11-22 04:36:00 | NOAA-20 | TUCURUÍ | PARÁ | Brasil | 1508100 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e664ae2-bbf4-3939-90eb-e725b3aa4bf1 | -5.24512 | -42.63788 | 2024-11-22 04:36:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 9.0 |
| dcc96395-8c5b-368f-99e5-c3a7bb56d56b | -4.48652 | -48.1141 | 2024-11-22 04:36:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ac719efd-fcc3-329f-b8f0-ae12faf6a773 | -1.47092 | -51.96965 | 2024-11-22 04:36:00 | NOAA-20 | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 8abb60ce-77cc-3ba0-b84d-01d3180034c7 | -0.81115 | -51.79317 | 2024-11-22 04:36:00 | NOAA-20 | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 55a5ab64-426f-3010-a8b3-0dafa8c1c7c6 | -3.23292 | -54.25687 | 2024-11-22 04:36:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 22.9 |
| d3f524fb-5a3a-38ce-92a0-723f07df2802 | -1.62288 | -52.59948 | 2024-11-22 04:36:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |


[Clique aqui para ver as próximas entradas](README51.md)
