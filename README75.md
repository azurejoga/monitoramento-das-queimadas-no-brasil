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

## Dados Diários - Página 75

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c16c8e42-b431-30d6-b3cc-b2a8969219c2 | -13.48755 | -46.88754 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 9ebf54a2-f7c3-305f-97b2-e145d6af361c | -13.42536 | -46.91566 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f8b0d6fd-08dd-37c4-8819-f5350cb07558 | -14.38511 | -51.94371 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3e68ddb-41c6-3a01-a514-53939f11970f | -15.6354 | -52.71063 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| dc3561ae-7ebf-3f78-9151-0ae5b854af73 | -13.51002 | -46.89795 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| cc444ccf-5f69-3554-9961-212d3ce3aea9 | -10.32835 | -67.36473 | 2025-08-25 05:06:00 | NOAA-20 | PLÁCIDO DE CASTRO | ACRE | Brasil | 1200385 | 12 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 760f0f46-d6eb-3010-96e2-fb85247dfb53 | -13.43597 | -46.9262 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 08be7213-cffc-369e-9dbb-53c07876966c | -15.14832 | -59.59578 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7986c038-acb7-36ae-97b4-77b91c119ec6 | -15.11528 | -48.68361 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ee3b7783-ec88-333f-95cb-e4b9debf796c | -14.74378 | -55.93141 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a7618ce9-6680-3c64-8539-9aa771c8ffb6 | -13.50892 | -46.90633 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f00c23a4-7251-37bb-9625-4241cefab769 | -14.28614 | -60.37068 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8113b561-3688-3598-a788-f6e4c59497ab | -13.01067 | -56.88724 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 30da186b-cfdd-3bf9-91e2-02e32bff4f21 | -13.4421 | -46.924 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2ba8e945-472d-381e-b2a1-a8e986ffc76a | -12.51453 | -53.81699 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1dd72467-57c1-35b9-a205-b6abb1e830e7 | -13.00238 | -56.89679 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 02a099b5-fe39-31bd-b38a-5cf129da7ae8 | -15.06861 | -48.67754 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 51726bfe-1c42-3ab2-bba9-49b93ddc786b | -15.75862 | -49.96999 | 2025-08-25 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f401469b-ac88-34dd-ae75-43ef5b329026 | -11.69535 | -60.18511 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7f29a82-f239-3246-98db-37b6448cd5cf | -12.85583 | -60.16082 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 15428031-6810-36a3-ab3e-e6b377d3a343 | -13.15703 | -53.73698 | 2025-08-25 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 20254c75-438d-3170-93ea-788a8117b5bc | -11.59945 | -63.49117 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| ad935afa-1953-3297-bfb3-3d0c86e865f1 | -13.50419 | -46.89742 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| f5ee7f99-91ee-315e-8d4f-338a99142d01 | -13.34192 | -54.39139 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 4486fb0c-ec7f-3826-a3ce-71f66e7d3015 | -15.03433 | -48.52131 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 1.0 |
| aad2f974-586b-31dd-955b-f7de0af4a21f | -14.69952 | -54.6815 | 2025-08-25 05:06:00 | NOAA-20 | PLANALTO DA SERRA | MATO GROSSO | Brasil | 5106455 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5acf2ba4-f4c3-3167-a306-15ce49a27b70 | -13.00625 | -56.89379 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| ca65f15d-4f1e-3fe8-9800-588434aa3f44 | -18.44804 | -47.55997 | 2025-08-25 05:06:00 | NOAA-20 | DOURADOQUARA | MINAS GERAIS | Brasil | 3123502 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 5609b704-faa8-3228-84e5-19058e6f90cf | -13.426 | -46.91049 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| eb24e007-34bc-3ba9-9f7a-71f031ec8728 | -15.13751 | -59.59777 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 3.1 |
| a9102c31-d44b-338a-a284-7daf47ff5f18 | -14.43593 | -56.46579 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 7734d55c-268b-3c7c-a23c-79a3837cb937 | -14.77529 | -48.21761 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 049a8e82-4093-3466-a712-61d27eaf8af1 | -14.27869 | -58.61224 | 2025-08-25 05:06:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 922698ae-6daf-370f-93bc-2bce41ed6452 | -13.41313 | -51.77721 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 6ba6dec7-3566-32be-9209-a43c11c367a2 | -15.07386 | -48.67844 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dca2c97f-c9d5-384c-b541-4ea7e2c5366a | -13.15639 | -53.74141 | 2025-08-25 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 48eba02a-0105-30e6-9276-f988202cc052 | -14.10033 | -53.99673 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| f73c23b7-4376-37aa-9933-2027fc6e1157 | -13.00017 | -56.88916 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 264450a3-ec4f-35dd-bd49-8a579adc6642 | -14.30382 | -60.3732 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 0d9df04b-16e9-3f6d-a343-b3b5cd35bac8 | -15.14162 | -48.64071 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 834e51f2-bf5f-3567-9eca-ab58d9ef5e0e | -13.50752 | -46.91818 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5e2e77e5-2def-3698-9bb5-bccf1df83950 | -15.03271 | -48.52165 | 2025-08-25 05:06:00 | NOAA-20 | MIMOSO DE GOIÁS | GOIÁS | Brasil | 5213053 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d739a98d-8338-33d6-a9ee-6e2f4fb3860c | -12.50161 | -53.83031 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 85376ae4-2ee5-38f1-b225-8383275f6726 | -14.42976 | -56.46108 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7051278e-74d6-3a2a-a124-6346cf85eeaf | -13.15269 | -53.74088 | 2025-08-25 05:06:00 | NOAA-20 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cb96197b-acf0-3c4a-a0aa-d9c2ac3e725d | -14.11794 | -53.99776 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 77a5b461-de0b-3f03-bb5a-d53ea63f9598 | -14.10098 | -53.99225 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e48d0c43-b901-3692-80a3-65176c3402ff | -14.43201 | -56.46894 | 2025-08-25 05:06:00 | NOAA-20 | DIAMANTINO | MATO GROSSO | Brasil | 5103502 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| dd5354a7-56cf-3daa-bff0-0057bfbbaa0c | -12.15917 | -60.74979 | 2025-08-25 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75998d19-f883-38c0-b080-0dd9564de5c1 | -12.5934 | -60.35932 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 22ea41c3-cc5c-3627-8bd4-85c99fde2ac2 | -13.05982 | -56.92023 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 60bc5ced-7305-3483-b52a-725c6f72bafb | -13.00183 | -56.90034 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6c2e1e22-9c14-3e19-8fc1-5e378b7f132d | -13.4084 | -51.78059 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7e03a7fa-bb85-369b-a162-3788a4d732a9 | -14.50727 | -51.93488 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 10.8 |
| edb91284-c490-3929-9497-7c76e553c726 | -13.50214 | -46.91382 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 95b63d56-d7f2-360c-bc4a-ccecb0632743 | -14.72616 | -55.93243 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| b2dfedbf-eba4-3ecb-8ff5-5f500ba58fc1 | -14.11204 | -53.99397 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.2 |
| aeb1fcfb-62d2-3e02-bb95-9cd87b88a92c | -12.43181 | -56.50714 | 2025-08-25 05:06:00 | NOAA-20 | TAPURAH | MATO GROSSO | Brasil | 5108006 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6cff4177-69ce-366a-9352-9a6754692f6e | -14.26422 | -48.03866 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 82837697-07b5-37a4-a256-4a0dbc1d637e | -13.39575 | -51.81101 | 2025-08-25 05:06:00 | NOAA-20 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 11.9 |
| cd75bd15-23dd-33ec-9eea-5037904231de | -13.44057 | -46.88587 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3d501c66-7574-3707-ae97-8c62afe62b36 | -14.38913 | -51.95175 | 2025-08-25 05:06:00 | NOAA-20 | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6d42e1a3-b881-3d3b-8e1c-b33480bcfb7f | -13.50916 | -46.90568 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5b8632e3-fba5-33e2-88f9-d0c65bd2d4e0 | -13.4306 | -46.92176 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 9bc95604-f89d-3456-8cb7-535ecfdd03ce | -14.76028 | -55.93785 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6f800159-fcf5-3d0f-afb1-4862018baff2 | -11.69676 | -60.17674 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 71200017-f9a7-3088-a667-93fed49d219f | -13.42555 | -46.9144 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 49a4f750-78d7-3208-9526-f6bc7035f4ed | -13.43097 | -46.91854 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2f77d3cb-ad26-35dd-a212-6c495a9992b4 | -14.25809 | -48.04385 | 2025-08-25 05:06:00 | NOAA-20 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7ee2b7b5-bff3-3f1e-b914-3438a7652c71 | -14.71307 | -55.92647 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0004cb87-bd45-361b-bb06-1eb2d5a6c08b | -18.29806 | -49.53122 | 2025-08-25 05:06:00 | NOAA-20 | ITUMBIARA | GOIÁS | Brasil | 5211503 | 52 | 33 | nan | nan | nan | Mata Atlântica | 6.0 |
| 3cc8f5e0-9b72-3073-a311-1584556a26a7 | -15.75795 | -49.97556 | 2025-08-25 05:06:00 | NOAA-20 | ITAPURANGA | GOIÁS | Brasil | 5211206 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f41256af-c3e3-3ba2-9071-ee6cec12b218 | -14.75687 | -55.93732 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a7425178-1a36-3850-896d-905dd85a656b | -14.3166 | -53.07351 | 2025-08-25 05:06:00 | NOAA-20 | CAMPINÁPOLIS | MATO GROSSO | Brasil | 5102603 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| bbb11909-b367-32eb-b7f4-7cd338cd8a8d | -15.0812 | -48.66165 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 11.4 |
| e4be231a-3991-3197-89f2-6b9581c4dd5e | -11.70324 | -60.18216 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| d855245f-d699-3c5a-ad20-7a9b9dacb903 | -14.29035 | -60.36721 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 240ad2cd-e9f4-3fdb-a823-a93056f95072 | -15.08933 | -48.68356 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.3 |
| fb65ed02-3d1a-3216-90fc-66de03fbd8f9 | -13.00072 | -56.88562 | 2025-08-25 05:06:00 | NOAA-20 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 950f4619-72e5-3371-b526-964bb8520062 | -13.44913 | -46.91408 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e25d1a07-d10c-3df5-ac4e-e6300eb390fe | -14.29742 | -60.36823 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f4a70191-95d7-3b7e-bb4f-f0e2575fe126 | -12.05864 | -63.1489 | 2025-08-25 05:06:00 | NOAA-20 | SERINGUEIRAS | RONDÔNIA | Brasil | 1101500 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d6f0c770-ab68-3437-ba4c-7810ec5a4b6d | -13.42633 | -46.90764 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 707d97a7-0e96-3e9f-bd87-a9326ccbb322 | -15.65013 | -52.72429 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c8d11713-87c4-3e67-9741-b6189d289858 | -13.43603 | -47.02777 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| db877ef5-a8bb-3176-b303-13c2f573ff28 | -12.59698 | -60.35996 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c65b52be-e835-3535-893b-9b6cdc8a0903 | -14.10401 | -53.99733 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 33e03fb2-4c85-315a-8a5f-dbccfe890064 | -15.63794 | -52.72264 | 2025-08-25 05:06:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1609c5cf-0c1d-3638-80db-64eafef4e70f | -12.4943 | -53.82922 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a203994e-1405-3c0d-88bd-4a2fe30a2f5c | -13.61512 | -48.1756 | 2025-08-25 05:06:00 | NOAA-20 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 2b0022b0-02a0-3e24-998a-8c25660c1bb2 | -14.27906 | -60.36971 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 1eccd5fd-d495-3d85-ba19-e5be7ab68892 | -15.07104 | -48.65675 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3ddd60d4-c55d-3338-b7e5-a343f022a2e2 | -11.70254 | -60.18635 | 2025-08-25 05:06:00 | NOAA-20 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| db698404-3926-38be-861f-047531040c4a | -13.34253 | -54.38719 | 2025-08-25 05:06:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 5ff026d9-d97c-3389-8b40-21d4b318f549 | -15.13876 | -59.59023 | 2025-08-25 05:06:00 | NOAA-20 | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c9ed3f1b-7659-3a88-8a1e-13cf3274b169 | -13.49873 | -46.89281 | 2025-08-25 05:06:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0895f9b6-22d5-3a42-820f-8019d8b4486e | -15.11407 | -48.64674 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9595e3a8-8ae5-3492-bbec-c8552bc4ecd7 | -12.16284 | -60.75049 | 2025-08-25 05:06:00 | NOAA-20 | PIMENTA BUENO | RONDÔNIA | Brasil | 1100189 | 11 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 6f974dd8-7f38-33fc-8597-673d6bb5bb66 | -14.72218 | -55.9357 | 2025-08-25 05:06:00 | NOAA-20 | ROSÁRIO OESTE | MATO GROSSO | Brasil | 5107701 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5797a0a6-49c8-326a-9718-db321385cc5a | -15.11125 | -48.6795 | 2025-08-25 05:06:00 | NOAA-20 | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |


[Clique aqui para ver as próximas entradas](README76.md)
