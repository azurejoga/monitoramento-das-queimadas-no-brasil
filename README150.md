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

## Dados Diários - Página 150

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 5ee940f7-44f8-33f4-a648-f361ab3917d9 | -11.89886 | -56.92876 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 34c796f9-744b-38de-b01c-044b329b3256 | -11.89817 | -56.93481 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| c27b3d8e-d94e-3930-b26d-a8ee714fb7da | -11.89748 | -56.94088 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 2c35f04f-2fe3-38a3-948a-e92f05b4ee9a | -11.89678 | -56.94692 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 844b53a0-83c1-32d5-b0d1-afb6bb2382ee | -11.8961 | -56.95291 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 874de54b-d8dd-345d-ad14-670504d9e261 | -11.89543 | -56.95878 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 20.8 |
| ba783ef1-71eb-3edc-b575-9adb32452173 | -11.89081 | -56.94001 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 9fb81f42-edde-33b5-82d2-515a7016d401 | -11.89012 | -56.946 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 01acb4c5-c990-3b46-8ac9-5f82c8a58bae | -11.88877 | -56.95786 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 8ec54bfb-a898-336c-bfad-38b3929f0a50 | -11.88277 | -56.95118 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 64817e72-55eb-38d8-afd8-5374ae1d174e | -11.88212 | -56.95694 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| c11a7a8c-f43b-3e0b-aa3a-f8f04b2afeac | -11.81808 | -56.60132 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| bf4b8c28-ff82-3dbc-8a83-e466dbadd999 | -11.81739 | -56.60741 | 2024-10-05 05:55:00 | NPP-375D | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| a593a8c0-4fd6-3a38-bc05-b12f03c15d88 | -16.57144 | -57.17062 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 49e3e245-1670-3fbd-9bef-71de8319e00a | -16.56452 | -57.16986 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 42731a48-5f01-3187-bcdb-edfd7635b2a3 | -16.55271 | -57.22157 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 65c05dc3-dcdf-3eef-b761-10db65c6e06a | -16.5521 | -57.22811 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| d8f4b7f7-7730-38fe-9029-78a50c0c9d63 | -16.54641 | -57.21431 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 16e09ff1-3cd6-3c5e-9546-52b81fd5e0ae | -16.5458 | -57.22086 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 15c1f06a-b9f5-3768-a14a-470e5f7db599 | -16.53889 | -57.22011 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| cbd97efe-dccd-3182-9a68-9dcd66ec63b9 | -16.51459 | -57.25718 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 14b01398-69a5-34cc-83c7-6728e121fb18 | -16.51425 | -57.25801 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| becc639d-7793-311b-8cf7-48ca3d38f9e0 | -16.50769 | -57.25652 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 8406bae6-ab1d-39c7-8d99-d74d0a320bb5 | -16.50735 | -57.25735 | 2024-10-05 05:55:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 4992f967-b47e-3b5b-bcc8-06e10c02985a | -15.6389 | -57.38203 | 2024-10-05 05:55:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| c77cd62e-bef4-3847-a1b3-99090123387d | -15.6384 | -57.38706 | 2024-10-05 05:55:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 74bd93d8-1a67-36c2-953a-a3136400285b | -15.63793 | -57.39178 | 2024-10-05 05:55:00 | NPP-375D | PORTO ESTRELA | MATO GROSSO | Brasil | 5106851 | 51 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5aa5ca02-096b-3a26-a730-3582731f350e | -15.57002 | -57.45632 | 2024-10-05 05:55:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.5 |
| e57b5b7d-f0cf-3d68-bdb8-67d31c71ffd5 | -15.56328 | -57.4556 | 2024-10-05 05:55:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 32f4678e-e00a-3653-b9ac-149ce48b60f2 | -15.56149 | -57.45616 | 2024-10-05 05:55:00 | NPP-375D | BARRA DO BUGRES | MATO GROSSO | Brasil | 5101704 | 51 | 33 | nan | nan | nan | Cerrado | 4.1 |
| b0a1555d-0f4c-3dec-ad89-8d783d70ac1d | -17.15781 | -56.96824 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 41537eda-9797-3351-9581-5ae393667048 | -17.15076 | -56.96749 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 30b65ce3-9a11-34f6-957b-3d11293aa81b | -17.12287 | -56.74617 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 0aff7afe-5ff6-3e53-aa1f-2169b7c49b02 | -17.11573 | -56.74548 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| f406022a-f83e-3a23-98a2-134d335b9ce0 | -17.11321 | -56.774 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 47d7b75f-dbde-3969-9286-f78f77c8e78f | -17.11258 | -56.78111 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| de0b0f82-7de1-3e45-a764-558082eb7e79 | -17.11132 | -56.79535 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| ddb136ad-f3c3-3c54-b09b-17bae36fa632 | -17.1042 | -56.79467 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| c1bbff6a-6b46-3f1a-b3ef-16513115ce94 | -17.09709 | -56.79391 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6f5e2b12-8517-3dd7-9110-fd5dae2688df | -17.08997 | -56.79321 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 0b23b709-1162-3dc9-952b-b45b6264f8ca | -17.08695 | -56.7943 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.3 |
| 5913868f-26d4-378b-9e72-656b642fad65 | -17.08471 | -56.77115 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.1 |
| 80407f9d-9a67-371b-8f78-073b2b940aba | -17.08409 | -56.77824 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 73598a31-1f3c-3758-90ca-0a539a89899b | -17.08347 | -56.78537 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| dac46338-1f26-389b-9c5a-b6f2e037f1f2 | -17.08286 | -56.79247 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 2d2ec953-b5b4-3f6d-8a4a-4d6b84b2d770 | -17.08182 | -56.77233 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 88e99132-be5a-3c11-9a29-0bacd69d3e22 | -17.08116 | -56.77939 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| a4031820-f23e-37c5-9414-e002e171bf5d | -17.0805 | -56.7865 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 42df1ac8-ce47-30bb-a1a1-f3e38648472a | -17.03651 | -56.79644 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 7586efc3-4c13-355f-853f-6da1152ed3c4 | -17.03245 | -56.79441 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| c98530af-d92b-3d1c-9c9f-eed9224d74b7 | -17.03058 | -56.70248 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 12.5 |
| 1e04d9e0-b085-3834-a520-3c46e6e398d0 | -17.03004 | -56.78862 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.7 |
| bf0db60f-dcd7-3404-855e-4c978c6df40e | -17.02994 | -56.70963 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| fe1bb306-d438-3c45-9296-928a6c3354c4 | -17.0294 | -56.79572 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.5 |
| 9c7da866-64e0-3b5d-b6c2-5049eb6338ac | -17.02739 | -56.73818 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f48605b2-07df-3c2f-9ae0-256f0d9a75e7 | -17.02292 | -56.78793 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0e99753b-4976-3b2c-8ef4-9821144bb921 | -17.02229 | -56.795 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| b53c3181-3f85-3360-9de9-c6365811b5a8 | -17.02025 | -56.73745 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| ce1cee10-4a8e-3e7e-936d-080f45d6074e | -17.01581 | -56.78721 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| e08fc838-850c-31fd-828f-0d854845a90b | -17.01518 | -56.7943 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.4 |
| 07de9c28-3d24-353e-9f73-12572f4cc6e8 | -17.01312 | -56.73675 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| cecfdccd-0eb6-37fd-9410-243166f54dba | -17.0087 | -56.7865 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 3127488e-6435-3b58-9787-76a2ea7f264b | -17.00806 | -56.79359 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| b4aeaa0a-e4d1-3c35-b4a7-9358693e5a63 | -17.00599 | -56.73601 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 8841b9aa-c69d-37a5-bc84-b5c9203d6ab7 | -17.00158 | -56.78577 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.7 |
| 276f9bc9-518c-3c5e-9ff4-2674a4f5c26c | -17.00095 | -56.79287 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.4 |
| 02d63a92-e6de-316a-98a6-85f285ee0cd5 | -16.99885 | -56.73528 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ee2678b4-16c3-3fba-9a81-75f155f7899f | -16.99823 | -56.74239 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| 00631d47-a7bb-359c-9f66-5cf174a01021 | -16.99697 | -56.75663 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 9e5dc9ba-da07-37f5-8eb3-196dab3e0b0c | -16.99635 | -56.76377 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| a8714ed5-dfd1-3b72-8322-544b3cd6b720 | -16.99478 | -56.73962 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 98107b75-7f4e-310e-8812-73f361af064c | -16.99447 | -56.78505 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| 460e3176-b8e4-35a4-92f7-60edbcb29383 | -16.99384 | -56.79213 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| ae9e882c-e8fc-398e-99d8-149150e3f22f | -16.99277 | -56.76097 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 0c1d3fa0-0b89-356a-8cf7-42f53c25827c | -16.99172 | -56.73454 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| ea10e301-1fa8-3fdd-86be-413577247015 | -16.99143 | -56.77516 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| c5f79e78-b9cc-3500-9243-09ca974f1036 | -16.99076 | -56.78223 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 4432d84b-9d77-3f69-bc67-a8bdb39d4f8d | -16.99047 | -56.74878 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 4a338119-3bc5-3c2b-ac31-f49dadd5e522 | -16.9901 | -56.7893 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e3174562-98b0-3181-9d75-6cf5dc31e3e5 | -16.98985 | -56.75593 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 503bb6a3-9dc6-3b33-8d1d-a6edd77bb32e | -16.98923 | -56.76304 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 9c54c528-6227-3267-a0e8-f537e5babc19 | -16.9886 | -56.77016 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 5ac2f4a9-9b84-384d-9726-2e8d16bec138 | -16.98798 | -56.77723 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| b47b05e4-43f0-3e24-a877-5ac7e4052b3d | -16.98736 | -56.78432 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.0 |
| ebabda32-abe0-3b28-ba28-2ee68dc3f5b7 | -16.98698 | -56.74602 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 47a468a2-297d-3cc4-9c02-bc11c9ddc042 | -16.98673 | -56.79141 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 24.5 |
| 5f723b2b-0047-3062-b893-ec89d6cfc18c | -16.98565 | -56.76028 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 23d19177-707b-32fc-a6ae-b0ab111db3ab | -16.98498 | -56.76738 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| be73797d-68e1-3fd7-9747-f37319e0020c | -16.98432 | -56.77446 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 7.4 |
| 7892ec55-c495-3c63-91c9-f682743fc4b6 | -16.98365 | -56.78154 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| e56d9fe0-95c3-3e08-b6a1-4372a38084e2 | -16.98298 | -56.78863 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 13.9 |
| 35014279-7559-39f1-ac14-39aeee7499f5 | -16.9821 | -56.76231 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| f6d4fd51-25ab-3a96-9451-89cd7aa4c890 | -16.98148 | -56.76941 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| b3ca209f-20b4-32e4-90c9-8d0f4f29d511 | -16.98087 | -56.7765 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| aae37396-0a3b-3fae-9e42-3621c4d250cd | -16.98024 | -56.7836 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 15.1 |
| 783d55f6-ae4e-321d-87e0-273a2c37ba52 | -16.97786 | -56.76666 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 871547f9-1e48-3971-ac32-4fcb4e1025ef | -16.9772 | -56.77374 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 14.8 |
| 09cd5937-6ef4-33aa-82d6-ac7bd3e0d902 | -16.97654 | -56.78083 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 9.3 |
| de7c0fd8-a2dc-306b-874b-56d6d5e6d463 | -16.97498 | -56.76157 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |
| d2958cb8-40ac-37d3-918a-beb0d2f42420 | -16.97437 | -56.76866 | 2024-10-05 05:55:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.0 |


[Clique aqui para ver as próximas entradas](README151.md)
