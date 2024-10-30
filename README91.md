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

## Dados Diários - Página 91

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9f27a9f4-1c25-3ce0-b651-80fee2df2f0b | -1.4488 | -54.21481 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 5016e634-c76a-3256-93bf-25090904a9f0 | -1.44537 | -54.21429 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 501fa918-6c9b-3095-9018-3a5f04f9d2fa | -1.43565 | -54.209 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1394d64d-9402-3b35-a447-7e42670cb37b | -1.43221 | -54.20849 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c5cd74ef-cf17-39f3-95c4-ddf67b789a6d | -1.42878 | -54.20799 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 0dbc7b28-9937-3590-8c99-7a268560cedf | -1.42406 | -53.42056 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9ca5a633-3739-32d6-98d8-dbead83f6d34 | -1.42133 | -54.21069 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e1f75810-f341-341b-8e15-6661e2dc981d | -1.41789 | -54.21018 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9baef889-9864-3858-a2e8-8aa5608e2e51 | -1.4133 | -54.21715 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| dc235efe-e977-368e-9188-4c6a7ec2a05f | -1.41272 | -54.22088 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 265ea583-044c-3669-849a-5416018d1ccc | -1.41046 | -54.54882 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 85d755d3-3883-33f0-b454-9d2da92b3889 | -1.39509 | -54.1109 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 20e0dc8c-94f5-3e83-b240-6276807a85c1 | -1.35168 | -54.61425 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 263e7912-9f2e-3711-8e47-f4854588eb50 | -1.34548 | -54.60959 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| e283165f-24ca-3588-9ac5-acc748cff3a7 | -1.34491 | -54.61324 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| ad00227a-8809-3b02-b635-b671a43fb5a7 | -1.34209 | -54.60908 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18d3cf95-e138-31dd-89c6-95b5255458f9 | -1.34153 | -54.61273 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 801d1f64-e735-3418-a2d6-fbb0be5d68b9 | -1.24118 | -53.38712 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b25bf91a-49d8-3785-8238-baa2d8bb3e4d | -1.21632 | -53.38338 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 498e682a-f732-39ac-8722-5755b19ee47e | -1.19202 | -53.9078 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| a231e742-1d42-3d48-9e90-1d0d32c20427 | -1.19145 | -53.91147 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3271c13e-6f76-3f81-98bd-ec04926cd884 | -1.18798 | -53.91095 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bac97e9a-7656-3bdc-a489-a316dee17c10 | -1.17627 | -54.07522 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| bd26ea4e-b210-3ac7-9754-991e1bcf7917 | -1.17569 | -54.07893 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 22f188bb-f890-3b37-9207-ec40d833d830 | -1.16598 | -54.07344 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2c9737-b6e9-3341-a1d2-b5cf19ee23c5 | -1.16573 | -53.38478 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 66c85a3b-7b4c-3f42-bb01-deae39b413d3 | -1.1655 | -54.1881 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b45126b7-fa8f-30ea-8459-22f64dac92cf | -1.16535 | -53.66702 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d8fc62b0-c974-37a4-aa3c-7f665dcfcd0c | -1.1651 | -53.38879 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.2 |
| ab9b39ef-3fd9-36aa-b178-eba04a5a4c76 | -1.16448 | -53.39277 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d0929b56-2f16-3dbd-9037-e0f397588aa3 | -1.16254 | -54.07289 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 30c1ec76-fbf1-3be2-9447-da6d84f67dd1 | -1.16219 | -53.38423 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb61aa86-b1c4-3cfe-95a8-b88893654d59 | -1.16155 | -53.38827 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8ce66aef-5f0c-3428-82c6-3a60b8f6d4e7 | -1.16093 | -53.39223 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5febab45-e906-3b73-b3c2-0682ddb88a56 | -1.15112 | -54.05581 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3672cc25-c115-335c-9c76-8218dd5e69c6 | -1.14767 | -54.05529 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| cd587eb8-cce0-3606-9ef3-8f6fd4862191 | -1.14693 | -53.64112 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c7f4fda9-c55c-34ed-aead-123325d944c4 | -1.14422 | -54.05477 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| b5960db7-9166-3f8f-a1ae-0f1f068568a0 | -1.14405 | -53.63668 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9454a737-9724-349e-8fe1-146bca0f0321 | -1.12805 | -53.44019 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f09f0187-67b3-3cf8-8127-14e7bf2d50a3 | -1.12797 | -54.11372 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54e628d2-f9f5-3bb2-b259-8076a9f8bfb3 | -1.10991 | -53.41701 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f976a8ce-1050-3c73-9db9-082505385822 | -1.10379 | -54.17868 | 2024-10-30 05:08:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 368cad0a-ce7d-3c01-9215-3cf3fccdf0bd | -1.08786 | -53.65195 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| aaeac1cd-dfdc-39a9-99ae-64fd7382a392 | -1.08725 | -53.65586 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a797afa7-2cdd-3d46-acc1-432fcbb191d7 | -1.08664 | -53.65975 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| e2dd902e-9d2e-3040-9fe2-926d1d656bfa | -1.08435 | -53.65144 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| b95de800-30d2-3ed7-b65d-1328d0ec0286 | -1.08374 | -53.65537 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d5b39975-cecc-3a92-8ec7-27dad1d2d26a | -1.08313 | -53.65927 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a4fdacb6-3826-315d-a147-50ccf54dcd5e | -1.08024 | -53.65488 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e09fe26a-71d0-3099-bea7-23a83f2f8152 | -1.06915 | -53.65703 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6dfe9dc8-146b-3b1c-8c22-e3cd516828c1 | -1.06675 | -53.67257 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c737e112-43b4-3cdd-9005-8327633f05fd | -1.06565 | -53.65651 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| eecebe95-fa32-3df8-808d-d582c1bc2fed | -1.06505 | -53.66044 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| e57ade10-7c8b-3698-91c7-9ed782cc8148 | -0.98876 | -53.70486 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 2bd38d5c-f00b-3e92-9ec3-d7a568ee8539 | -0.98527 | -53.70432 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4d9ab320-ceef-36ce-9ce6-d4e6dddc6acf | -0.98466 | -53.70825 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 77b2a0f2-4576-3cf1-bce8-499ef46c8688 | -0.98117 | -53.7077 | 2024-10-30 05:08:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 25efcabe-8577-366d-b6a7-8036e3a1aec9 | -0.98056 | -53.71163 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 030eac1d-c033-3b65-a72b-1af4561e5d08 | -0.97706 | -53.71119 | 2024-10-30 05:08:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9fc82272-324d-3aa9-930e-767ba847574c | -3.58115 | -54.6778 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 665b4d30-950c-37ef-911a-5ac468a3cea1 | -3.52157 | -54.67647 | 2024-10-30 05:08:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 710211bd-e6e8-3e49-8d0b-b4c6408d2306 | -3.4659 | -54.8313 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 1c54635d-afb2-3799-bb42-6e9d340808b0 | -3.3081 | -54.69781 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 6e014905-c1a1-346f-9630-59f237d5a4cb | -3.30752 | -54.70154 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| b019e3d0-8b59-364e-b543-0e32af7a7057 | -3.29611 | -54.75281 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 01a24770-dd70-3c6b-b039-00865d5b135f | -3.20754 | -54.66781 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 54174358-e4bc-3d10-b51d-7cd3de28425d | -2.95021 | -54.67809 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7942fbab-36db-3a1d-a4b8-e4cfc9255ea3 | -2.95011 | -54.67854 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 30e9b1a2-ec13-337f-a6bd-c0eb94625521 | -2.94964 | -54.68179 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9808b4d-5550-37e6-8168-ea1057870551 | -2.94953 | -54.68224 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d1f1f57d-3c61-3a08-83bd-00682b87b18e | -2.94908 | -54.68547 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 9018af1b-f424-3eb3-94ef-dc826f25e717 | -2.77659 | -54.73511 | 2024-10-30 05:08:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1a2ca340-8824-3fc5-8830-ef6c94153436 | -2.68485 | -54.96055 | 2024-10-30 05:08:00 | NOAA-20 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 0ddbd46f-a3c3-3bb2-b17f-2442d8bd8d18 | -3.59333 | -53.78483 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 491d4103-a38c-300b-9a78-e02454238110 | -3.58977 | -53.78421 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 58c82079-b82e-3908-b2f9-e28784c74bd4 | -3.4613 | -53.81952 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4dbaf986-bbec-3400-b93b-8ad468ca6a2e | -3.46072 | -54.08033 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ae5b6029-f5c0-34fb-9f78-033da48c2409 | -3.45781 | -54.07588 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| eb726d7d-73b1-3f95-82fe-3dad183d79bc | -3.4572 | -54.0798 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b23c5306-da73-347a-8a7a-6330851f9b3e | -3.45659 | -54.0837 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 22d7428d-6550-35bf-ae77-21160d11b247 | -3.45429 | -54.07534 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6031de5f-1214-3938-9938-b617b0f5a581 | -3.45368 | -54.07927 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9cdaa7ba-71a7-301f-9e8c-274e8cdba504 | -3.45307 | -54.08317 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3fd3a581-b71e-3214-9e67-2d8ebcc6f097 | -3.45078 | -54.07479 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18b913fb-4b05-3cbe-96ba-d5eeb1d6d5b0 | -3.45017 | -54.07872 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 19aff38e-f055-3709-b03e-f0f228db19ce | -3.42509 | -54.17076 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0948126b-1f18-31a8-bb92-112a9e55e472 | -3.42459 | -54.15084 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c5049489-172f-3a77-908d-66b61f225a0b | -3.42399 | -54.15472 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 82ae71ad-a42a-369a-ab7a-dc4a2425a732 | -3.42108 | -54.15033 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 90e971ac-e376-3081-ac79-e1f8f4653657 | -3.42048 | -54.15422 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 2f9bb75b-daa7-3ca0-8bac-2d90819395c0 | -3.20643 | -53.85283 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 789d2de5-fd7a-3d33-9408-a78959933767 | -3.14706 | -53.90936 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 347cf175-305c-31c7-89c9-357d9fe8ffca | -3.14644 | -53.91331 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ab46c668-49ac-377c-894d-da5aa3ec6369 | -3.10431 | -53.71468 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 90d260b4-618b-334c-8dc6-506645811417 | -3.1037 | -53.71872 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 2bb6f51f-04ae-39bc-87e7-d046a882a766 | -3.10159 | -53.71544 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3d4af583-364d-365c-a542-e98f8b5d8d70 | -3.10096 | -53.71947 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8c42a007-1a71-3e72-93b4-7b9db9fb1510 | -3.10074 | -53.71414 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f4706051-945c-3e5c-ae37-bfc9a6dde531 | -3.10032 | -53.72351 | 2024-10-30 05:08:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |


[Clique aqui para ver as próximas entradas](README92.md)
