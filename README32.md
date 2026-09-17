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

## Dados Diários - Página 32

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 10cb93ad-893e-3f6e-85c2-cb3e4470465d | -18.88746 | -46.84585 | 2026-09-17 03:57:00 | NOAA-20 | PATROCÍNIO | MINAS GERAIS | Brasil | 3148103 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 483f4aa7-3aad-32ea-9de4-09bb9f616b8b | -14.33118 | -48.93451 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 36a59072-4646-3385-90d8-264ba0a916ed | -14.14217 | -48.74522 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.4 |
| beccbbf2-b72c-3755-a587-ed98482b0d2d | -15.68262 | -41.46253 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUAS VERMELHAS | MINAS GERAIS | Brasil | 3101003 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| f501b7d7-b2a7-3345-b9e9-e2adcf4f0a6a | -14.33249 | -48.93451 | 2026-09-17 03:57:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 4.0 |
| fb7f0671-2525-3147-960b-b5fbbc99604d | -17.77275 | -46.47448 | 2026-09-17 03:57:00 | NOAA-20 | LAGOA GRANDE | MINAS GERAIS | Brasil | 3137536 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 92de34c6-987f-3dca-902a-960274510dec | -14.18317 | -45.14508 | 2026-09-17 03:57:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| c4edc071-1e70-3f94-a606-33c642b49a19 | -16.26391 | -43.51473 | 2026-09-17 03:57:00 | NOAA-20 | FRANCISCO SÁ | MINAS GERAIS | Brasil | 3126703 | 31 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b35866ab-02ab-3723-8c71-1ce7a3452e63 | -14.86003 | -47.91705 | 2026-09-17 03:57:00 | NOAA-20 | ÁGUA FRIA DE GOIÁS | GOIÁS | Brasil | 5200175 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c7d4be15-0287-360b-9faa-6780e02a5e16 | -17.82819 | -46.72227 | 2026-09-17 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ea1b5968-b988-38a7-ac1f-9f551d47bc18 | -17.82753 | -46.71952 | 2026-09-17 03:57:00 | NOAA-20 | VAZANTE | MINAS GERAIS | Brasil | 3171006 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f2a0a223-d2b9-3981-bf13-81083912ca8e | -8.4982 | -57.6468 | 2026-09-17 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 4fbd7647-5d9f-370b-b93c-89aa190f32e9 | -8.4796 | -57.6478 | 2026-09-17 04:00:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 69.1 |
| c32fab9e-da5c-3366-805a-7e921fca233e | -21.46143 | -48.67811 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 11.8 |
| 2d445307-3616-3a50-861b-565cf9ba32ed | -27.5635 | -48.66027 | 2026-09-17 04:00:00 | NOAA-20 | SÃO JOSÉ | SANTA CATARINA | Brasil | 4216602 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| f5269ae9-3464-3a0c-8163-299bfd95c1e2 | -21.46073 | -48.68405 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| db8ff580-9232-3275-b3c9-4d9740fa13d9 | -21.45668 | -48.677 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 5d81ae40-c854-386c-b8dd-4238b41a2689 | -21.45598 | -48.6829 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| d6c9012a-8719-3717-97e2-b7919af4028e | -21.46023 | -48.68376 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 12.2 |
| 1895f533-678f-3290-8ed2-47c5bf1514a9 | -21.46189 | -48.67837 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 10.3 |
| ee654f8e-2008-3f43-a207-4c78df55f34c | -21.45714 | -48.67725 | 2026-09-17 04:00:00 | NOAA-20 | TAQUARITINGA | SÃO PAULO | Brasil | 3553708 | 35 | 33 | nan | nan | nan | Cerrado | 6.8 |
| 7fe448c2-1bcc-3872-96a3-b0b0c5faab0a | -26.72135 | -49.34162 | 2026-09-17 04:00:00 | NOAA-20 | RIO DOS CEDROS | SANTA CATARINA | Brasil | 4214706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 2.8 |
| 2f4130b5-e35f-3aee-82e8-d1f3a0a079b8 | -27.02977 | -51.91233 | 2026-09-17 04:02:00 | NOAA-20 | IRANI | SANTA CATARINA | Brasil | 4207809 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9fdb7979-a305-37a5-b5e4-83546699013a | -8.4796 | -57.6478 | 2026-09-17 04:10:00 | GOES-19 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 72.3 |
| f58ce460-adbe-320a-a21a-67cff6f99b05 | -12.49 | -50.85 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b036c7cd-43ad-31f6-862b-f18e875d3864 | -12.46 | -50.84 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| ef6e7720-da5e-3f70-b005-7419b0aaa4d5 | -12.49 | -50.8 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 9b431ef8-fe8d-34ae-8a4a-3a3a6dfe6ba2 | -12.46 | -50.9 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| f3301da0-fb97-3875-8357-4f16553d6c69 | -5.76 | -45.09 | 2026-09-17 04:15:00 | MSG-03 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 4d5a6072-d899-3ed8-a62a-003027e36e88 | -12.46 | -50.79 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| b72769ad-a2e3-3864-b4e3-b02e128be4f6 | -12.43 | -50.83 | 2026-09-17 04:15:00 | MSG-03 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| a189e2d4-2efc-300a-9861-d1c9fbd5b55f | 2.7622 | -60.8841 | 2026-09-17 04:20:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 65.1 |
| 18f58668-438a-39e4-8cc2-20f1e32d9d89 | 2.7621 | -60.903 | 2026-09-17 04:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 52.5 |
| 58dadbd5-25ab-3548-b393-0b257f584278 | 2.7439 | -60.8843 | 2026-09-17 04:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 55.8 |
| e69d72ae-dae1-3adf-b5f1-f5073df5c814 | 2.7622 | -60.8841 | 2026-09-17 04:30:00 | GOES-19 | BOA VISTA | RORAIMA | Brasil | 1400100 | 14 | 33 | nan | nan | nan | Amazônia | 80.0 |
| 37100709-8cfd-36ee-8627-385d9b8ab693 | -2.90665 | -54.17772 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| fdc4e647-f98e-37aa-af21-cb4b0c90408a | -3.20238 | -50.75366 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6d1a9485-c9df-32e9-948e-67572ac61acc | -3.02324 | -51.33575 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 8fa3d54d-5681-3a3d-b248-1d9f81cc7cd9 | -2.90397 | -50.4202 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7242e077-3c0c-37d0-839c-44089dc7cb06 | -3.46942 | -54.70581 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 33d7f3ba-b67e-3177-9694-de43bc0c0b14 | -1.98292 | -47.05732 | 2026-09-17 04:38:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9873359e-e68f-3e81-9d4a-08397918b37f | -3.37745 | -52.79382 | 2026-09-17 04:38:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7e36a1f5-df20-329e-accb-7051fc6202c7 | -2.95526 | -50.31388 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 15.6 |
| b52f9f60-424e-3f4a-80bf-e8ccebdf9204 | 2.51152 | -50.84718 | 2026-09-17 04:38:00 | NOAA-21 | CALÇOENE | AMAPÁ | Brasil | 1600204 | 16 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c18b545a-5582-3bca-8cbc-48e410b0a11b | -3.17218 | -53.92942 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 12bdef07-e04d-3850-ad8c-41989886aa98 | -1.22886 | -54.12392 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 01a3cac7-a9fc-3a57-b082-24ef34bf7192 | -3.02673 | -51.33628 | 2026-09-17 04:38:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 84d35b22-4bb9-370f-bcfd-2d328126654e | -2.89959 | -54.16907 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| dcb86c91-7ae3-333e-8310-2faa4c993c35 | -3.47301 | -54.71046 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| f12bdebf-12d6-3dff-acf1-feebf2da86e4 | -3.54108 | -53.99527 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f6728db3-c8bd-333c-909e-95dda33d4d88 | -4.56007 | -42.94275 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 9caaf062-215c-3c57-b3e0-68b5ff9a772a | -2.75375 | -54.67664 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 104578b2-fa81-321b-890f-c83bb8bbbce7 | 1.29013 | -50.89428 | 2026-09-17 04:38:00 | NOAA-21 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9b8d61e7-c4af-3023-9c40-5328eb4e87ee | -2.82058 | -51.34068 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 434e4490-5977-39c7-9bb4-8971a5e3e33a | -4.55017 | -42.94373 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 58adde16-2a2d-3a57-8b2b-1c0247950e66 | -1.81709 | -54.93637 | 2026-09-17 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 2e09b8a5-dce2-31af-9dd9-a18254f8474c | -2.90607 | -54.18143 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 433df74b-a7ce-3e63-ac4f-b3623bae11ce | -4.95893 | -45.1438 | 2026-09-17 04:38:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| d48a226e-4226-3632-8592-5fa10c3c7867 | -3.21485 | -53.94654 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 129bd336-2a89-3344-8602-07eb0562c8ae | -2.89154 | -50.43308 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3c316fc4-35dc-3207-a76a-524d64f672a9 | -3.48439 | -54.72076 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| a753d0d7-d29c-368a-8a6a-f42ab13e11a4 | -2.58521 | -48.43793 | 2026-09-17 04:38:00 | NOAA-21 | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 1389e528-400f-3b51-a4eb-2f8f5fa5cdb3 | -2.102 | -52.04914 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| f599f24e-363b-39c0-a542-dbad70534342 | -1.15164 | -54.17309 | 2026-09-17 04:38:00 | NOAA-21 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 65c8327c-c0a2-3144-be3a-e96be5f153bb | -2.9665 | -50.3303 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 12.3 |
| dd204d0e-9a03-3af9-a735-a9adb91b0724 | -1.34336 | -55.84526 | 2026-09-17 04:38:00 | NOAA-21 | ORIXIMINÁ | PARÁ | Brasil | 1505304 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 09560291-faaf-31fb-9331-2da123382886 | -2.8212 | -51.3368 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 62644120-0eaa-352e-8573-d282ec6cc3c2 | -3.48211 | -54.70833 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| b939c957-8cc3-3257-b596-b912f9f99a6d | -2.91487 | -54.17229 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eec3d306-8466-3600-b3cc-2b4dbcf1aa39 | -3.26822 | -54.26203 | 2026-09-17 04:38:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| ebf8190f-6590-327f-a423-e511ab3a1cf7 | -4.18591 | -49.40686 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 401e3a95-01a7-3010-ab40-3aa429daed79 | -2.90792 | -50.41712 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c4d43882-02ee-354e-983d-6b51599b747d | 1.91823 | -50.83382 | 2026-09-17 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 693e8b23-b944-3d71-8883-773858a4677d | -0.96352 | -47.5808 | 2026-09-17 04:38:00 | NOAA-21 | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 5f4dc1d6-df32-383c-aa9c-ac4314a886fd | -1.899 | -52.14768 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| aed4442d-4673-32d0-b8cd-95de9c40cc6f | -2.09767 | -52.05283 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cf5c65ef-ecd9-3b96-805e-7e1a90bf702a | -2.91073 | -50.42126 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b4459f59-c7e8-39ea-abe2-ec0f3db7b0c5 | -2.90002 | -50.42329 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 57f8d3cf-66c9-31f2-97ff-1418d91a95af | -3.1784 | -48.58363 | 2026-09-17 04:38:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 33ef968b-481d-3308-8e6a-8a0f884e4261 | -2.80137 | -52.08161 | 2026-09-17 04:38:00 | NOAA-21 | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 10.6 |
| 454204da-3593-3228-b887-10b5cb1b3777 | -4.19044 | -49.29129 | 2026-09-17 04:38:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| ac597722-d843-315e-ad2a-6c2f79c05853 | -2.96706 | -50.32672 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 1bbcd780-7c0e-3d85-b44c-d9b95e9f7d8a | -2.10497 | -52.05398 | 2026-09-17 04:38:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e06efb47-e050-3710-9e1c-575954a18f55 | -2.91076 | -54.17167 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 801c7582-f7fb-3b06-9a2a-3f062cc0326e | -2.96425 | -50.32262 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| 34f25c30-b30e-3e2a-bade-9f7864e37f15 | -2.47161 | -54.67996 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 9e8060c9-4682-357f-ad62-94d5a65764ad | -1.60615 | -55.56683 | 2026-09-17 04:38:00 | NOAA-21 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0494e523-bf0e-38e2-8a93-bb89e593e9b8 | -3.2154 | -53.94317 | 2026-09-17 04:38:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ff21cb0b-74d9-3531-86ba-ab335a3fb8f3 | -2.91077 | -54.17836 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| afa1c66e-539c-3ba2-bdf3-32e201484e06 | -3.48574 | -54.68475 | 2026-09-17 04:38:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ffc5cf45-401f-3cc3-a6f5-9364e42d757b | -2.91749 | -50.4223 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| b0edf016-446b-3241-9d45-24c293f5b596 | -1.81719 | -54.93591 | 2026-09-17 04:38:00 | NOAA-21 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 77179d00-e3ac-380c-bb34-698cd12912ab | 0.09912 | -51.06677 | 2026-09-17 04:38:00 | NOAA-21 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.5 |
| a9322e71-ad00-3729-a6c8-5c59b3ed1f43 | -2.90312 | -54.1734 | 2026-09-17 04:38:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ff62f064-7888-3384-8709-487dd7d3d1cd | -2.90226 | -50.43104 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 8d85f1e9-e55f-344d-a1a3-8eb149ba4add | -4.54952 | -42.94797 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 1baec564-3212-3243-b4a0-13cdbf9a8afa | -4.55946 | -42.94698 | 2026-09-17 04:38:00 | NOAA-21 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 16.1 |
| 1bad01ee-693c-3c5c-b54d-a2c9fb2cca91 | -2.85135 | -49.54369 | 2026-09-17 04:38:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d6d66c9d-bd1c-3867-9ac2-fdde95ebf119 | -2.97099 | -50.32366 | 2026-09-17 04:38:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 833d1d80-2dfa-30ee-b8ad-12c1bc1811d9 | 1.95917 | -50.98026 | 2026-09-17 04:38:00 | NOAA-21 | AMAPÁ | AMAPÁ | Brasil | 1600105 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |


[Clique aqui para ver as próximas entradas](README33.md)
