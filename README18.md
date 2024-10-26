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

## Dados Diários - Página 18

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3885768a-ee34-3f8f-9fe2-16c9879418b1 | -17.0079 | -56.0051 | 2024-10-26 01:27:05 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f342df5b-8406-32fc-848e-c6f163f0dc79 | -17.294901 | -57.294102 | 2024-10-26 01:27:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 55b9b2ef-7237-3292-9109-0f776f4a3b7a | -17.296499 | -57.3013 | 2024-10-26 01:27:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 426f247d-bc15-3b0e-91db-b0806c18a075 | -17.285101 | -57.296398 | 2024-10-26 01:27:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 37a09a0d-e2bf-3899-a579-e7cc65583390 | -17.240101 | -57.185398 | 2024-10-26 01:27:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 93b04329-a4eb-3ff9-b7a9-418b229a02a5 | -17.241699 | -57.192699 | 2024-10-26 01:27:05 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4394b52b-27fa-3ae9-af94-095b0ad827b1 | -17.230301 | -57.187698 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2a8c16e4-fab8-337a-a1fd-2a89e0811a4f | -17.231899 | -57.194901 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1552eea5-7a7f-30b9-a2f2-5ac6f8448965 | -17.2335 | -57.202099 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e9b723b5-03c6-3f84-be86-f592b182b929 | -17.2237 | -57.204399 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 81ef9574-3ba4-30d6-8b23-8a99e99d3842 | -17.2253 | -57.211601 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 66d7fa87-4b5a-3135-8749-9fbb17bbb141 | -17.2269 | -57.2188 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0432cc85-eaa9-3174-b526-4d013c5dbece | -17.2171 | -57.2211 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9e03e83a-6db4-3252-8ebd-0395a4959da4 | -17.2187 | -57.228401 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38ae1974-16f9-3d52-a3cf-d52033e5d340 | -17.220301 | -57.2356 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 476dd7c9-88f6-328c-9ee4-2a52bb7f76e5 | -17.221901 | -57.242802 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5309abae-3d57-3bcd-a329-c92cad96ff34 | -17.212099 | -57.245098 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4ff94c1-e4a3-3362-beb6-d13b7f1621b4 | -17.213699 | -57.2523 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 43d60c4b-48ff-3838-af73-93c5dfd716b2 | -17.266001 | -57.4916 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| adada816-43d9-37b5-bee8-4127c083b8f2 | -17.267599 | -57.498798 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 22008fdb-dc0e-3dca-9fb9-d201cc1901fe | -17.2691 | -57.5061 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 16b43604-63de-38b4-b96a-5dfe963586b5 | -17.2707 | -57.513401 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7e4e2278-add4-3d8e-b9bb-3cdf150f41ea | -17.203899 | -57.254601 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 8889bce0-96e7-3aa5-a59c-31c4564dff1e | -17.2055 | -57.261799 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc05358e-8e35-35df-9a1d-044e8597e53b | -17.2071 | -57.2691 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 857709c7-9ed8-3007-97f4-10657ac744eb | -17.2087 | -57.276299 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 38cde75c-be3f-3b20-8a60-33bfbd336831 | -17.254601 | -57.486599 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e7e67e8-61c6-39c9-8563-fbf9c7ee1516 | -17.256201 | -57.4939 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 11686e06-b0a0-3e91-8d42-c121562a7f47 | -17.257799 | -57.501099 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| ab9e4257-058e-3537-af10-4b64a3051175 | -17.259399 | -57.5084 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 126f6bdc-d5d5-3d16-93e4-224df4e5691d | -17.261 | -57.515701 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d537f87f-eefa-3ca2-8f51-605efa11a316 | -17.1973 | -57.271301 | 2024-10-26 01:27:06 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3c8ab988-df2f-3dcc-a7b8-7c9fefa7b457 | -17.2449 | -57.4888 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 24697c33-c348-3373-bb74-8c478ca62c43 | -17.2465 | -57.496101 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4aea3b82-3abc-3aef-bac5-df01e76540ef | -17.2481 | -57.5033 | 2024-10-26 01:27:06 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6548837e-433c-3aea-b93c-f723dda87805 | -17.017799 | -56.507301 | 2024-10-26 01:27:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 89431315-df08-3242-8359-1afe2a380a32 | -17.1891 | -57.2808 | 2024-10-26 01:27:07 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 104d423c-6211-3981-8529-de5429ea6b45 | -17.2351 | -57.4911 | 2024-10-26 01:27:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f92ae7f1-a026-3a64-9057-6d483f22f1cc | -17.007999 | -56.509602 | 2024-10-26 01:27:07 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f5617000-531f-3783-9567-7b2d800aa5eb | -17.2253 | -57.493401 | 2024-10-26 01:27:07 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 41c7d97e-d774-3c25-a7b5-cbd37cecbfe9 | -17.108 | -57.4748 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2e21fc59-9e37-3181-bf61-fddd9a40ea01 | -17.072701 | -57.406799 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| d49395aa-6f3e-3736-897e-57113961ce2e | -17.077101 | -57.4743 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| eab1501c-ff6a-3e3f-8614-ae2c764e7880 | -17.078699 | -57.481602 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 227f2b5f-2e6f-3796-937a-3b739a8515a6 | -17.0483 | -57.389702 | 2024-10-26 01:27:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1d0b29af-c2e2-35eb-aa70-2a77c8577e56 | -17.0499 | -57.3969 | 2024-10-26 01:27:09 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 26112713-bede-3eba-9ad2-672d0aa03365 | -17.062599 | -57.4548 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd2dea07-b884-3eee-9efd-7768ad32f91a | -17.064199 | -57.462101 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| bbaab6a0-c8ff-3916-83b4-a0bd62caa139 | -17.067301 | -57.476601 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a6c5b557-9e29-371d-ab02-713dd631883c | -17.068899 | -57.483898 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| be410e38-3c65-3777-876b-ed91bf5deb03 | -17.051201 | -57.449902 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| fdcb66fb-a42c-3788-ae14-18af6d1531c1 | -17.0576 | -57.478901 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b87a0cc2-9cc9-3731-9e1c-719e5915cdbd | -17.059099 | -57.486198 | 2024-10-26 01:27:09 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e0173b0-2906-3cef-84a2-4bff81febb5e | -16.9965 | -57.341 | 2024-10-26 01:27:10 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dc4c26f6-bc93-3a8c-97ae-413d27d559ad | -17.0361 | -57.521999 | 2024-10-26 01:27:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ed7d017-e427-32ff-a267-5ec331267a42 | -17.037701 | -57.529301 | 2024-10-26 01:27:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 0177d894-edba-3285-a879-7b0d43c345b6 | -16.9914 | -57.364899 | 2024-10-26 01:27:10 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c5e261d9-b99d-3837-b74e-03fcffcd3c30 | -17.0247 | -57.516998 | 2024-10-26 01:27:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 950bb8d4-bdbf-322c-a95f-53a97c9dbebc | -17.0263 | -57.5243 | 2024-10-26 01:27:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1b477333-c444-3ec4-9223-7ee4f449b07e | -17.027901 | -57.531601 | 2024-10-26 01:27:10 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b4e44602-ad01-3dc9-a857-64c5178e8c0e | -16.9848 | -57.381699 | 2024-10-26 01:27:10 | METOP-C | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 6e5316c1-ed40-3182-8aee-44fdfa1f5ddd | -16.9856 | -57.5261 | 2024-10-26 01:27:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| e0d40265-f10a-3adf-bd8f-a936dfc55218 | -16.9758 | -57.5284 | 2024-10-26 01:27:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| b346109d-a9ca-345c-afd3-e758ce54247b | -16.9774 | -57.535702 | 2024-10-26 01:27:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 2339b401-12fe-3736-b5cf-ed8a703d0d25 | -16.966 | -57.530701 | 2024-10-26 01:27:11 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 421502be-9485-34d2-bf3c-5399100cc4c6 | -16.9303 | -57.508499 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 03b8b988-ec50-3391-9379-9662113b70bc | -16.931801 | -57.515701 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a300b123-3a53-3b2a-95ef-b27401ffe25a | -16.933399 | -57.522999 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 1e228fbf-6a4c-3cec-95f8-02d073a0853d | -16.934999 | -57.530201 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| dd259ca1-13f9-30c0-9fe9-ab5e159758eb | -16.9366 | -57.537498 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 46ab8b0d-b9d7-30b4-ae9e-8a8a68a46e7c | -16.9205 | -57.510799 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3ea20bfc-dce8-3a6f-8754-852d3a1b533c | -16.9221 | -57.518002 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| a218611a-a168-3564-b0ae-3c26f898a398 | -16.9237 | -57.525299 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 354d32a5-9447-340d-b82a-57a626e9a2b6 | -16.925301 | -57.532501 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7c5828c8-6796-324b-bd53-851b4713c14d | -16.9028 | -57.4767 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| cae92c3e-0a09-3a94-aed3-a6fef131e191 | -16.906 | -57.491199 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 539231c4-546d-31f0-89e5-c8e0f5cb4d04 | -16.9076 | -57.498501 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9302f7a1-a424-33e2-894e-78341d2b88ae | -16.909201 | -57.505699 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| c90e9ea0-d3f5-3418-92ad-bacbcdea9cd8 | -16.9107 | -57.513 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 3d50721e-aa9e-31f5-bf97-d1cc14d7776c | -16.8978 | -57.500801 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9f40fa87-e35f-3310-8540-2975269109a8 | -16.899401 | -57.507999 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 736c1096-eee9-3b3a-a913-8e9ef221e5ce | -16.9422 | -57.704498 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4a6701af-fcf9-397a-a56f-477f43925a76 | -16.9438 | -57.7118 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 5c367783-245c-3a37-a429-a67c6ea9fba2 | -16.9116 | -57.658001 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 9a7e5258-d9e5-3d9a-8df9-c34aef3cfb1a | -16.913099 | -57.665298 | 2024-10-26 01:27:12 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 4179c0a1-1da5-33ae-80db-3117707aa673 | -16.564199 | -56.2323 | 2024-10-26 01:27:13 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 211fddda-f95a-31db-b77e-99a5551602de | -16.5658 | -56.239498 | 2024-10-26 01:27:13 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 683f99c7-6210-3a1f-80c2-68e24fceb313 | -16.8822 | -57.6647 | 2024-10-26 01:27:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| f46c4cd7-fc21-3761-b33d-3f4323ead960 | -16.883699 | -57.672001 | 2024-10-26 01:27:13 | METOP-C | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 7ee004fd-1b52-3bd9-8063-9dfa2171c8b6 | -16.554399 | -56.234699 | 2024-10-26 01:27:13 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 57b296fa-ffbe-3b1b-a2d2-bbccc39b3f98 | -16.556 | -56.241798 | 2024-10-26 01:27:13 | METOP-C | BARÃO DE MELGAÇO | MATO GROSSO | Brasil | 5101605 | 51 | 33 | nan | nan | nan | Pantanal | nan |
| 21e4567f-e798-3596-b291-e23930b9a345 | -15.7861 | -55.715099 | 2024-10-26 01:27:24 | METOP-C | SANTO ANTÔNIO DO LEVERGER | MATO GROSSO | Brasil | 5107800 | 51 | 33 | nan | nan | nan | Cerrado | nan |
| 00a3c138-c0d2-390d-a6b9-26f906e9668a | -16.091499 | -60.117001 | 2024-10-26 01:27:34 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| fc8db05d-f76f-3d7e-a951-1628f210a626 | -16.0933 | -60.125702 | 2024-10-26 01:27:34 | METOP-C | VILA BELA DA SANTÍSSIMA TRINDADE | MATO GROSSO | Brasil | 5105507 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 373bf025-4ef9-3493-b67e-8e6881f24a3a | -9.4984 | -47.800499 | 2024-10-26 01:28:33 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| df5e4ea1-4b04-3e22-bc61-a6e01a1e2122 | -9.5047 | -47.824699 | 2024-10-26 01:28:33 | METOP-C | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | nan |
| 8fec54e7-0c9c-3158-9877-d9cb4ea576a9 | -11.1675 | -56.280399 | 2024-10-26 01:28:40 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f8b9ac24-4209-3224-a4a7-d4d40e0e7f93 | -11.1692 | -56.287701 | 2024-10-26 01:28:40 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| f30397d8-764a-3265-9297-ca3b9ab2c180 | -11.1577 | -56.2827 | 2024-10-26 01:28:40 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |
| 25d2c601-7952-34bf-8895-a98cac621f13 | -11.1594 | -56.290001 | 2024-10-26 01:28:40 | METOP-C | TABAPORÃ | MATO GROSSO | Brasil | 5107941 | 51 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README19.md)
