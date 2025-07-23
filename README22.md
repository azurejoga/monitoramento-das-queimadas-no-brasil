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

## Dados Diários - Página 22

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| b9c3699f-beba-3a2a-a7ef-96b8231c9b95 | -7.4113 | -44.6051 | 2025-07-23 13:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 111.7 |
| 25e10b02-9176-383b-88fc-c7d4b7474876 | -4.038 | -42.5365 | 2025-07-23 13:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 87.7 |
| 59417c04-9937-3540-8edb-bc721484a4bd | -12.3439 | -63.4255 | 2025-07-23 13:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.3 |
| a9455564-e2ed-33a0-8d7e-f3be00bfb885 | -6.7452 | -45.4604 | 2025-07-23 13:10:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 75.0 |
| 0806542c-3c55-36d2-bf3b-d72a92d187ff | -10.6363 | -45.2257 | 2025-07-23 13:10:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 113.6 |
| a0f9acb3-fe80-3a6d-95f7-fd39ec6e49ed | -6.9804 | -42.7854 | 2025-07-23 13:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 114.0 |
| 2cf97a26-b59d-30c6-aa98-a87edc1e6930 | -4.0569 | -42.5118 | 2025-07-23 13:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 177.0 |
| 4a5978a4-8454-3b1f-b56d-cca770a06c9a | -12.3628 | -63.4245 | 2025-07-23 13:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 129.6 |
| 60ac39ad-6847-31e8-a0d7-3facfff24be7 | -7.4113 | -44.6051 | 2025-07-23 13:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.9 |
| aaa68140-4bdb-3fb9-89af-302267fd34ea | -5.9213 | -43.4636 | 2025-07-23 13:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 227.9 |
| 96015817-86bb-32c6-b503-625a938aa430 | -10.6363 | -45.2257 | 2025-07-23 13:20:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 112.9 |
| 5b5269d0-f4dd-3616-8333-3ea97d973f2b | -4.0382 | -42.5129 | 2025-07-23 13:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 84.6 |
| 39f5693c-eaa9-34ca-8b93-5ac9c9a0ca29 | -7.0224 | -45.8428 | 2025-07-23 13:20:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 66.1 |
| 5572c853-c80d-36bc-b762-6123011c5456 | -7.2402 | -44.7812 | 2025-07-23 13:20:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 114.3 |
| 107d07c4-8dd7-313d-ba4c-5be94a7d5420 | -12.3439 | -63.4255 | 2025-07-23 13:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 71.7 |
| 4e0687fe-6e41-3744-b209-4db51e9c03ec | -4.0569 | -42.5118 | 2025-07-23 13:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 157.0 |
| 2c0657a1-16ce-32d7-9afd-450c5195ca6b | -7.0224 | -45.8428 | 2025-07-23 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 80.2 |
| af6c2a7e-0399-3e7c-8450-5d071c20b151 | -4.038 | -42.5365 | 2025-07-23 13:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 82.2 |
| a9a64900-8171-3e68-a43e-2c3bc42f21ec | -6.9801 | -42.809 | 2025-07-23 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 102.0 |
| cf519ba9-d347-3b27-9f82-fb29dda3bc0e | -12.3439 | -63.4255 | 2025-07-23 13:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 60.2 |
| a56c5e34-3cac-358e-9475-bfa94262bebe | -7.2402 | -44.7812 | 2025-07-23 13:30:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 91.0 |
| d1c65e1e-2bf3-38b5-96a6-f48530559b27 | -10.4047 | -46.6832 | 2025-07-23 13:30:00 | GOES-19 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 28dcc34d-ecf0-3055-b636-428cf798f158 | -6.9804 | -42.7854 | 2025-07-23 13:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 154.1 |
| 02283829-90f6-3d40-b104-effe4e0edc33 | -5.9213 | -43.4636 | 2025-07-23 13:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 164.9 |
| 05eaa330-aeae-3f2b-88ef-ccba38656072 | -12.3628 | -63.4245 | 2025-07-23 13:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 145.9 |
| 210ed8d5-b2ef-33be-b2a4-ead8b111c66c | -7.0412 | -45.8412 | 2025-07-23 13:30:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 5b2d3456-05fd-3a7c-b980-2bd641b8ed3d | -10.6363 | -45.2257 | 2025-07-23 13:30:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 89.8 |
| f21a749e-42f0-3dfd-b339-5a2c45ca9bf5 | -4.0382 | -42.5129 | 2025-07-23 13:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 105.1 |
| 613f05be-7ff1-3b95-96e6-42331022a9a5 | -7.2634 | -44.3893 | 2025-07-23 13:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 77.7 |
| f50af311-ea7a-3171-b795-ba260645f477 | -6.7452 | -45.4604 | 2025-07-23 13:30:00 | GOES-19 | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 99.7 |
| 5ce523ef-3b5f-3187-b8fe-4df451b2b889 | -7.0224 | -45.8428 | 2025-07-23 13:40:00 | GOES-19 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 74.9 |
| 25267a19-db0b-3657-b971-475427c5e896 | -6.9486 | -43.9568 | 2025-07-23 13:40:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 107.7 |
| 4e79b7fd-994a-3c14-8575-301cf8e8321a | -10.0612 | -46.8359 | 2025-07-23 13:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 481.3 |
| eab27b7a-30ae-36d6-bcf1-772974c4b8db | -12.3628 | -63.4245 | 2025-07-23 13:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 107.8 |
| 64c488a0-3b98-3aee-bcf3-254aaeae1785 | -10.6363 | -45.2257 | 2025-07-23 13:40:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 118.2 |
| 12487a27-c366-3e12-970e-7807f27575d1 | -4.0569 | -42.5118 | 2025-07-23 13:40:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 154.4 |
| f525079a-38b8-389e-9802-819c34ac9b77 | -7.2822 | -44.3876 | 2025-07-23 13:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 88.7 |
| 3e99733e-5fa9-34f1-b9aa-78c47bcf3f99 | -4.0382 | -42.5129 | 2025-07-23 13:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 144.2 |
| 299ab7d6-41f8-3c3e-bc72-829b1df8385f | -12.3439 | -63.4255 | 2025-07-23 13:40:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 78.1 |
| 4a0ba5f2-d04c-3dea-b1cc-c5d5bc87a9b2 | -5.9213 | -43.4636 | 2025-07-23 13:40:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 181.8 |
| 906e4fe1-3b4c-3b2b-8fa9-91b27a66eb6a | -7.2402 | -44.7812 | 2025-07-23 13:40:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 103.1 |
| 136b3b5e-583a-3cce-8b3b-8bbb82e73352 | -6.9804 | -42.7854 | 2025-07-23 13:40:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 167.5 |
| aea2d2c2-2526-3993-9691-bd3adba4f6ab | -12.3628 | -63.4245 | 2025-07-23 13:50:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 92.4 |
| c78a436b-0a0b-3049-9a5a-13820a3f2a51 | -4.0569 | -42.5118 | 2025-07-23 13:50:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 223.4 |
| f6864316-2151-3d1e-b850-a5178ebdd433 | -7.2634 | -44.3893 | 2025-07-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 119.2 |
| 44e2b277-4ca0-36a1-b14d-62243bccbd6c | -5.9213 | -43.4636 | 2025-07-23 13:50:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 182.1 |
| e42dacf3-3312-3a91-b80e-b34630e42c2b | -10.0612 | -46.8359 | 2025-07-23 13:50:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 393.4 |
| 84926638-ad70-3ed5-a550-6014ec42d098 | -10.6363 | -45.2257 | 2025-07-23 13:50:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 105.2 |
| faa75985-952b-3cb3-9f67-b0648b8d2f94 | -4.0382 | -42.5129 | 2025-07-23 13:50:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 122.6 |
| e96b24d9-ccdc-3911-8589-93038d00241c | -6.9804 | -42.7854 | 2025-07-23 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 193.0 |
| 47779991-ac2f-36e7-a21a-37bb8464e81a | -7.2822 | -44.3876 | 2025-07-23 13:50:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 185.0 |
| c758973e-43a4-3869-bece-9d9d8aba7130 | -6.9801 | -42.809 | 2025-07-23 13:50:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 125.4 |
| 23a95a1d-fd30-32ea-9397-6b6d5cb08a1a | -6.9486 | -43.9568 | 2025-07-23 13:50:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 88.0 |
| 6fb3fc87-dae2-39d2-9ddc-2afd668fb193 | -6.9804 | -42.7854 | 2025-07-23 14:00:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 164.6 |
| 4611cd8d-8dc3-30f8-8504-c9a391f4aa4c | -5.9213 | -43.4636 | 2025-07-23 14:00:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 144.1 |
| d513c4c2-c901-39e8-a26a-674177639224 | -10.6363 | -45.2257 | 2025-07-23 14:00:00 | GOES-19 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 93.7 |
| 101aef88-9327-3916-bf3c-fefb9e07578a | -7.2636 | -44.3663 | 2025-07-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 73.6 |
| c1adc7a5-44fc-34ae-ab18-8a8f57770db8 | -6.9486 | -43.9568 | 2025-07-23 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 208.6 |
| 32f6cb6a-e3fc-3f60-8d8e-6a17cbe5e826 | -12.3628 | -63.4245 | 2025-07-23 14:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 117.4 |
| 9fddcb6d-351e-341f-9e2c-a7041ae1c7a8 | -7.2402 | -44.7812 | 2025-07-23 14:00:00 | GOES-19 | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 87.2 |
| 5901f4e8-674a-3dc3-a955-c80dab09a2a0 | -4.0569 | -42.5118 | 2025-07-23 14:00:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 164.8 |
| 2eef6ede-d3b2-39ee-94a7-173c363bb22d | -6.9674 | -43.9551 | 2025-07-23 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 85.5 |
| b00d16bc-b577-38ca-a170-04f509adf5ca | -6.9261 | -44.305 | 2025-07-23 14:00:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 91.1 |
| 60313cef-2776-39b9-893b-b52602c1f01a | -7.2822 | -44.3876 | 2025-07-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 266.7 |
| df2c9687-4037-3626-b06b-5e4335cc7e26 | -12.3439 | -63.4255 | 2025-07-23 14:00:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 63.3 |
| 578445b1-a0ad-3c42-9b32-bb69714616d5 | -7.2634 | -44.3893 | 2025-07-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 283.2 |
| da51369d-ad7d-3bc5-b491-2c19f38bf1d4 | -6.9298 | -43.9585 | 2025-07-23 14:00:00 | GOES-19 | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 123.6 |
| 53958f95-32dd-3f57-9d1b-c66bf1fd4ed4 | -4.0382 | -42.5129 | 2025-07-23 14:00:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 158.9 |
| 32b8167e-0353-3a54-8d6d-4ce38b6bfa08 | -7.2824 | -44.3646 | 2025-07-23 14:00:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 80.3 |
| 486a2996-4e55-38ac-bc0e-1813182e56ec | -5.9213 | -43.4636 | 2025-07-23 14:10:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 175.1 |
| bbbda6ee-7c0d-366d-a391-70dd49bbd9d1 | -12.3439 | -63.4255 | 2025-07-23 14:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 62.7 |
| 74e3bd95-c36b-319c-8061-1b5272d53131 | -4.0569 | -42.5118 | 2025-07-23 14:10:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 221.1 |
| d28a259b-f8d8-3dab-81c1-d9978a988887 | -12.3628 | -63.4245 | 2025-07-23 14:10:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 147.0 |
| b75a9952-9070-31b8-b59c-4627b2b943f6 | -7.2634 | -44.3893 | 2025-07-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 118.8 |
| c6557363-e86d-33a0-a09e-c6ee539e0d32 | -7.5742 | -45.1607 | 2025-07-23 14:10:00 | GOES-19 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 95.3 |
| 8808be3d-92fa-31b6-860e-56c0cd265abe | -7.2822 | -44.3876 | 2025-07-23 14:10:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 115.2 |
| e9d513e9-0589-3868-a8a1-f6cc335941f7 | -4.0382 | -42.5129 | 2025-07-23 14:10:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 119.0 |
| f3c6faa6-0054-325a-b8ba-96422e245f9b | -6.9804 | -42.7854 | 2025-07-23 14:10:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 135.4 |
| df215bd5-e7b8-33bd-bb0c-1fb746e6ae66 | -12.3628 | -63.4245 | 2025-07-23 14:20:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 118.1 |
| 072137e7-daa8-3cb0-a097-30829b605de8 | -6.9804 | -42.7854 | 2025-07-23 14:20:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 128.9 |
| 20a8c061-6936-368b-961c-bc523e566670 | -5.9213 | -43.4636 | 2025-07-23 14:20:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 148.8 |
| 789cdbc1-4551-3aea-abb2-a7e8db2bb9ae | -4.0382 | -42.5129 | 2025-07-23 14:20:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 98.7 |
| 4b69ba26-2f4e-3a6d-8717-cf158768cf81 | -10.0612 | -46.8359 | 2025-07-23 14:20:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 511.5 |
| 50286f1d-e1e7-35bc-bb2a-262eda32b650 | -7.2634 | -44.3893 | 2025-07-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 150.0 |
| 6a8f2f8b-4f32-3ce5-9cf9-80ef1ac94b94 | -7.2822 | -44.3876 | 2025-07-23 14:20:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 113.5 |
| 64baf175-1d9e-3185-b376-50cb3b81b216 | -4.0569 | -42.5118 | 2025-07-23 14:20:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 200.6 |
| 1cac5469-9eda-3eee-ae65-479182763d68 | -4.0382 | -42.5129 | 2025-07-23 14:30:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 143.4 |
| 62211729-1925-3d1a-a90d-f366333e6e17 | -7.2634 | -44.3893 | 2025-07-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 159.9 |
| 9e5f28e7-6f94-36bc-a227-94e0b842bf85 | -12.3439 | -63.4255 | 2025-07-23 14:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 84.1 |
| bc8de88f-2b61-3806-959a-89e206666db1 | -4.0569 | -42.5118 | 2025-07-23 14:30:00 | GOES-19 | NOSSA SENHORA DOS REMÉDIOS | PIAUÍ | Brasil | 2206803 | 22 | 33 | nan | nan | nan | Caatinga | 134.5 |
| bdc46e4d-4c19-3b40-975a-868cca2f3a9b | -10.0612 | -46.8359 | 2025-07-23 14:30:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 139.0 |
| 4edbe61c-24ca-3b67-99cf-bb898343204e | -6.9804 | -42.7854 | 2025-07-23 14:30:00 | GOES-19 | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 108.0 |
| d9772951-a2b9-388c-b5a0-98f4c7706a60 | -6.9261 | -44.305 | 2025-07-23 14:30:00 | GOES-19 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 77.3 |
| 9545f8cb-e0ec-3dce-976a-f536089200c1 | -5.9213 | -43.4636 | 2025-07-23 14:30:00 | GOES-19 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 140.7 |
| 7082e1a9-51ca-313a-aba5-e0cd024f0b69 | -7.2822 | -44.3876 | 2025-07-23 14:30:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 166.4 |
| cc5e5cd4-2574-3976-b338-d855384f8ad3 | -12.3628 | -63.4245 | 2025-07-23 14:30:00 | GOES-19 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 80.1 |
| c65b9f83-20f4-3440-8c56-ebb445dc3437 | -3.8107 | -43.0182 | 2025-07-23 14:40:00 | GOES-19 | BURITI | MARANHÃO | Brasil | 2102200 | 21 | 33 | nan | nan | nan | Cerrado | 86.9 |
| 34e8a2f7-e38a-3a67-95f0-912a67571330 | -4.0382 | -42.5129 | 2025-07-23 14:40:00 | GOES-19 | CAMPO LARGO DO PIAUÍ | PIAUÍ | Brasil | 2202174 | 22 | 33 | nan | nan | nan | Caatinga | 134.2 |
| da2a5576-3cf4-32b3-ac23-c9977212709f | -7.2824 | -44.3646 | 2025-07-23 14:40:00 | GOES-19 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 82.2 |
| 6259ba3f-099b-3b67-b2e8-b540ae70ff4b | -10.0612 | -46.8359 | 2025-07-23 14:40:00 | GOES-19 | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 131.6 |


[Clique aqui para ver as próximas entradas](README23.md)
