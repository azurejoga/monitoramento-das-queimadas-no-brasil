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

## Dados Diários - Página 135

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| f827af9e-753b-3ca7-992d-e5644b39e479 | -12.11966 | -58.71953 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8d8c5656-fd11-3c28-a3b0-e6bfe847db8e | -11.85205 | -59.03558 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 6bbb5e2a-9ca2-3510-a90e-8a9c65f0bf87 | -11.84911 | -59.03059 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| d60cbac6-c631-3204-8fd9-92f24a4705d3 | -11.83709 | -58.87989 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f3394ad4-7c03-33ba-b85c-1e0abae91859 | -11.83698 | -58.90249 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| fe7a8efd-9e45-35d3-9d5b-c553c81e2ab8 | -11.83334 | -58.90183 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 87abd462-2440-3846-a6c1-8c71c989c770 | -11.82907 | -58.88288 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4e37919d-afc4-3231-8d25-4f73c792e202 | -11.82834 | -58.88719 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cb733656-a834-3767-be69-0440b1dd8ea1 | -11.703 | -58.89438 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 98962693-ff46-35bb-95aa-f95989681744 | -11.70292 | -58.89527 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 3e9f0e46-a657-3862-b975-4a78019e0df2 | -11.70226 | -58.89872 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d3f8ffb8-4526-3674-87db-491b3a814efa | -11.25721 | -59.05996 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 265f362b-feaf-3188-aadd-6c11cfd2af8f | -11.25351 | -59.05927 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e32d938f-40cd-3552-9cab-d94f38254c65 | -11.66891 | -60.01209 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ec63793e-49ee-3f19-87b9-dd66fae0d3fe | -11.66501 | -60.01144 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6966d9b9-e38e-3c70-a85a-aafe344c9a79 | -11.6551 | -59.99915 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c8e3af2e-eab7-3ecd-a8de-0c1ca3aa83a6 | -11.65421 | -60.00426 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 5efcb7bf-4a42-348c-9349-7bc209483c02 | -11.6503 | -60.00363 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| bd28b861-40ae-3d11-9e54-b0dda6ed1abc | -11.64817 | -59.99285 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| fca93635-82ce-3196-9bc8-8fadeaf5cf47 | -11.64728 | -59.99794 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 7c2b72b8-fec5-331e-893a-1e3bfcb49697 | -12.2797 | -59.21885 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| caa562e5-b501-302a-a91b-9fd2b3aa89a9 | -12.27895 | -59.22328 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| e40ad2ca-7e5e-3927-a3f6-ee9059cba7b9 | -12.27736 | -59.25528 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 070b4b52-1456-3924-8174-1f2ef5271135 | -12.27676 | -59.21376 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1fa9571b-4fa9-340b-8c51-41aa7dcf8b67 | -12.27601 | -59.2182 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 4.7 |
| ac281682-a832-38a9-adb8-4d2ae17e1b63 | -11.77412 | -59.29077 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 668fe18d-56c5-3b76-b45e-a0d9a6240ccc | -11.77118 | -59.28554 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| c8896214-8987-33f4-a921-4ef63751aa38 | -11.77039 | -59.29013 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 3156533a-b0d9-353d-aafd-dd88f949a219 | -11.72691 | -59.28932 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e40b8cc4-39b8-3cec-91a4-bc4657f4f70c | -11.72613 | -59.29394 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7f001b78-0940-33fc-89c0-678a78160808 | -11.72318 | -59.28864 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 31fd9f4c-50a6-3739-ad6e-2069f6bf269e | -11.72239 | -59.29327 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f57bb0d0-63eb-3acb-bf34-1b7241838a17 | -11.27422 | -59.18454 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 647acfba-a8a1-32fe-b50d-9cfa972837d3 | -11.27126 | -59.17933 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 61642322-219d-36f3-850e-aaf7ae22644d | -11.27048 | -59.18389 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 545eeabd-72f8-33fe-8d39-a4d617257e19 | -11.26675 | -59.18324 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e3296443-486c-307b-93ef-0120dc1440ec | -11.26301 | -59.1826 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 485ee218-065b-34df-9872-4ca426b1a4e2 | -11.63292 | -60.01105 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99485c06-6f87-3256-a375-256d9adae1ad | -11.62902 | -60.01034 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7ecd6514-97d0-3f41-b93b-f7befd539b25 | -11.62901 | -60.008 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 5a30aaf9-3445-3a2a-9c6e-e77d2c8b80a8 | -11.62682 | -59.99726 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 004679ca-969a-30bf-af60-863f84629703 | -11.49883 | -59.44178 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 0283d02a-4253-32a8-a262-274b44331828 | -11.49852 | -59.44389 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 09ae366d-5aab-37a8-9e64-85692a18fee6 | -11.49802 | -59.4464 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cf70d761-3445-30c3-90be-109f848b6926 | -11.49505 | -59.44111 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| bf7604f4-4015-3db5-993c-f904611ac53e | -11.49474 | -59.44322 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6c3f9839-cddf-3c9e-9444-de46c6067726 | -13.52487 | -59.54254 | 2024-09-26 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 99bd6653-cb22-35fc-96fb-5f1b67ba4c33 | -12.25904 | -59.7066 | 2024-09-26 04:59:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| b5654761-920a-30a8-8502-4fe20215e233 | -14.80133 | -59.42404 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8c4ccda7-542b-3322-8cf9-3d3442504eb6 | -14.78615 | -59.4257 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ed803a0d-95b8-3127-97bc-de3ce8c3efe1 | -14.78254 | -59.42506 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 3063c35d-7888-33ff-98ff-ab1f9148cd48 | -14.77892 | -59.42442 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b1b21f65-5e91-319c-b40e-86b683ded6d5 | -14.77408 | -59.42491 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 886c3f10-429a-3ac6-909c-017a0bb95e1b | -14.77334 | -59.42925 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e5c9034d-188e-3ab5-9e4a-06360051d4d8 | -14.76973 | -59.4286 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e3b56a29-8bc8-3dbe-851a-79a0361340a6 | -14.50959 | -59.63281 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 5d1ca4e6-6b06-32b0-bcee-5031a9585fcc | -14.50593 | -59.63214 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c3926cfc-604a-3ae4-bc54-e90a5e18ec3d | -14.4561 | -60.10613 | 2024-09-26 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 166e68a9-9762-32a5-8dac-67a8eafab2ab | -14.44232 | -60.11817 | 2024-09-26 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 923808ee-4ab2-3e2a-8534-83942637b855 | -14.43855 | -60.1175 | 2024-09-26 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 113e25dc-a06f-3aea-9680-bc25babde820 | -14.43793 | -60.1198 | 2024-09-26 04:59:00 | NOAA-21 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| c311955b-f3aa-37f7-87f0-5cdecd9b50db | -14.42426 | -60.064 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 7.4 |
| 93700df1-9b2b-36b3-8c46-d5160d733c29 | -14.41837 | -60.05324 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 3c856e56-b1c4-31b0-b750-edd7312f7ece | -14.37094 | -59.65094 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a36ca88e-eadd-3251-abf4-40aa514e5cae | -13.74206 | -60.11377 | 2024-09-26 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ee9175a1-c105-3ddd-baff-880f5a19d82d | -13.71473 | -60.06845 | 2024-09-26 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 1045c39f-0436-39cb-b07c-6c72bd66686c | -13.71386 | -60.07336 | 2024-09-26 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7b8317e6-5368-3e42-9228-c6b03dc47c04 | -13.71299 | -60.07837 | 2024-09-26 04:59:00 | NOAA-21 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 868e3357-d9f2-381e-94ba-91cb177ed8bf | -14.49936 | -59.6264 | 2024-09-26 04:59:00 | NOAA-21 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0acca835-77e2-3bc1-bac2-41a9637d25f4 | -14.96818 | -59.41278 | 2024-09-26 04:59:00 | NOAA-21 | PONTES E LACERDA | MATO GROSSO | Brasil | 5106752 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a5ad5736-1e61-372e-bc6f-4601e76d398a | -14.79847 | -59.41905 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 36f8e6b3-5193-32db-987e-c746af5113e8 | -14.79772 | -59.42338 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e215f946-b03a-356d-8e15-2dfa6eb7ac26 | -14.79412 | -59.42271 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 64588e94-4574-31cb-a102-0464061dd779 | -14.79336 | -59.42705 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 3bafcb6b-b583-37c4-bb67-bc464bed4961 | -14.78976 | -59.42636 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 86265fb4-dc9c-3f02-afb1-3047d7a52384 | -14.77769 | -59.42557 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 4a77c066-148c-322a-bd57-b65f8a0edbd2 | -14.77531 | -59.42375 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4b93ad38-b289-368e-9ac2-6eb0c1016ffe | -14.77094 | -59.42743 | 2024-09-26 04:59:00 | NOAA-21 | CONQUISTA D'OESTE | MATO GROSSO | Brasil | 5103361 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 1be65bf0-4657-3469-84cb-bc646d01e796 | -9.3975 | -60.3045 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8c08467e-d043-3b04-b218-179e2d99e427 | -9.39546 | -60.30043 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| da7e5667-1ff0-3df3-98f1-2d7a60b121e4 | -9.39483 | -60.30417 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| e2617f23-44d2-3f78-8ed3-7e9dd9daf900 | -9.39404 | -60.30006 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f04066c-aa5f-3c45-9889-24fb82148f1f | -9.39338 | -60.3038 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aba56b6f-d071-3566-aab4-9606e5b32fb8 | -9.39134 | -60.29972 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ddd23a82-ed8d-3b04-92bb-37c13a3dd31e | -9.39071 | -60.30345 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b1214080-f17e-3ad9-bfaf-833bcdffef94 | -9.39058 | -60.29563 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1c3b56c7-b23c-380a-b71d-730348426723 | -9.39008 | -60.30718 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5f68326b-2be5-3ab3-9c15-4afdbc5d6a14 | -9.38992 | -60.29936 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 515b0da8-a892-3973-8ab7-5a82e4e11d16 | -9.38596 | -60.30645 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2756170f-18b2-3b71-9273-a5ccf00af6c3 | -9.38533 | -60.31017 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 699b9c74-1fd4-3b5b-b0a5-c624ebd54c06 | -9.38122 | -60.30944 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8f706716-d182-3a43-a1d9-76916575d802 | -9.34259 | -60.28738 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 20dd42fd-61d7-38b2-9a6f-4b35ca9a2bce | -9.32511 | -60.48804 | 2024-09-26 04:59:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c076410a-f6d2-3664-9909-e3f599dd2193 | -9.05327 | -60.429 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0501dde2-6f22-3bac-b4c8-a0a66bc8fa0e | -9.04773 | -60.43599 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.8 |
| 89249b41-4f57-34c6-88b5-1779fef9db58 | -9.04767 | -60.42868 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4e270286-685d-3890-b730-bae56b66de88 | -9.04636 | -60.43642 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 12960fa6-bb0e-323c-9ae0-242dbe4793b6 | -9.04492 | -60.42756 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ddb892d3-5f68-3f2e-ba54-8f99e23a13b1 | -9.04424 | -60.43142 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5be3472d-eaeb-3988-a941-fbce1c00b4a1 | -9.04356 | -60.43528 | 2024-09-26 04:59:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |


[Clique aqui para ver as próximas entradas](README136.md)
