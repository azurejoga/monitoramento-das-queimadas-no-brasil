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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 7634ec3f-415d-3705-b035-458dd94fb89e | -3.7009 | -45.9 | 2024-10-18 00:35:27 | GOES-16 | ALTO ALEGRE DO PINDARÉ | MARANHÃO | Brasil | 2100477 | 21 | 33 | nan | nan | nan | Amazônia | 137.2 |
| 29b92c94-9ad3-3034-bf72-a687368389fd | -3.8733 | -52.0715 | 2024-10-18 00:35:28 | GOES-16 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 65.6 |
| 23dbd816-73ae-3f4e-ab50-2dcfe7aa0b6b | -4.4072 | -45.9773 | 2024-10-18 00:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 107.1 |
| 066a0f7e-7be6-37ea-8627-db186e07e74c | -4.4258 | -45.9763 | 2024-10-18 00:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 263.3 |
| cd16c21d-e552-3f75-b113-4f43b5ecfa5e | -4.426 | -45.954 | 2024-10-18 00:35:31 | GOES-16 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 128.4 |
| 2cfbaa63-a71c-3dcb-8785-002cfaf972b6 | -4.6653 | -46.3418 | 2024-10-18 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 81.2 |
| 1dbc3f04-afea-3e16-bd4c-0ff55b073145 | -4.6655 | -46.3196 | 2024-10-18 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 59.9 |
| 7cefe3a1-d490-38a3-817f-1bf51470a2bb | -4.5613 | -48.0358 | 2024-10-18 00:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 59.9 |
| f27caa6b-8674-3b1f-8d4b-e776119b99f1 | -4.5614 | -48.0141 | 2024-10-18 00:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 104.4 |
| f3c80a72-db7c-314a-bb05-def7cf4391d8 | -4.5799 | -48.0349 | 2024-10-18 00:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 67.0 |
| e2306f2b-7be9-3a0a-8c70-2b2fddc7388b | -4.58 | -48.0132 | 2024-10-18 00:35:32 | GOES-16 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 92.2 |
| 1bd5e2a1-0f80-31aa-a6ce-3701ff57e603 | -4.6467 | -46.3429 | 2024-10-18 00:35:32 | GOES-16 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 56.6 |
| 14dd6bbc-ab1b-363e-b506-d5ec22cf11cb | -4.8917 | -45.928 | 2024-10-18 00:35:34 | GOES-16 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 72.4 |
| f9c9fca3-1dce-3cce-a052-8d0a6a4995b4 | -6.6703 | -70.1174 | 2024-10-18 00:35:44 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 54.4 |
| bb359215-aa38-3b6c-9d72-5dafe18dd316 | -6.6886 | -70.1171 | 2024-10-18 00:35:45 | GOES-16 | EIRUNEPÉ | AMAZONAS | Brasil | 1301407 | 13 | 33 | nan | nan | nan | Amazônia | 72.1 |
| d4cc8669-77f5-3b70-8683-e4ae8eaa4e16 | -11.4859 | -65.1198 | 2024-10-18 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 49.8 |
| 14f0fa7e-ef41-3514-8c63-616bb06f87c7 | -11.5046 | -65.1189 | 2024-10-18 00:36:12 | GOES-16 | GUAJARÁ-MIRIM | RONDÔNIA | Brasil | 1100106 | 11 | 33 | nan | nan | nan | Amazônia | 46.9 |
| c288506e-8389-3f7a-a5e2-7d7c892cff7f | -12.4964 | -63.2258 | 2024-10-18 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 56.4 |
| c23d2c1e-14c0-32b3-896e-ebbfd669142e | -12.4966 | -63.2066 | 2024-10-18 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 89.6 |
| 12268f13-da90-3399-a9cd-ae3ed4680c56 | -12.5155 | -63.2055 | 2024-10-18 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 75.4 |
| 9bb9caaa-f481-3709-8cdb-9e242edfae80 | -12.5156 | -63.1864 | 2024-10-18 00:36:17 | GOES-16 | SÃO FRANCISCO DO GUAPORÉ | RONDÔNIA | Brasil | 1101492 | 11 | 33 | nan | nan | nan | Amazônia | 48.4 |
| d714da4d-42b5-3b3b-9922-2f04a14cc1ed | -17.189 | -45.4644 | 2024-10-18 00:36:41 | GOES-16 | BURITIZEIRO | MINAS GERAIS | Brasil | 3109402 | 31 | 33 | nan | nan | nan | Cerrado | 89.2 |
| 591db74b-bc33-3dd6-a139-a3be3c25019e | -17.0191 | -57.4768 | 2024-10-18 00:36:42 | GOES-16 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 78.8 |
| 15d8963e-c392-3f86-a514-74c6985df5dd | -17.2177 | -57.3102 | 2024-10-18 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 103.5 |
| 0da5d1c0-6426-38a5-bbd2-fae1e4b9f4d8 | -17.237 | -57.3284 | 2024-10-18 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 83.7 |
| b2b465cf-0978-3bf5-bf2e-fa084ba58a04 | -17.2373 | -57.3079 | 2024-10-18 00:36:43 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 190.0 |
| 1694d6b5-643c-3372-92b8-8d9043b73918 | -17.7855 | -57.4473 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 128.1 |
| 8e7a9ebc-6eb0-3ded-b51a-a1e2b4647a91 | -17.8045 | -57.4861 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 86.7 |
| ac255e40-797b-3dc3-91f6-7a9daec27475 | -17.8049 | -57.4655 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 203.9 |
| 920aa586-72b3-3e13-9a95-a87be8c9afce | -17.8052 | -57.4449 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 84.9 |
| 1d05e9b4-f732-3ee0-adbc-86c48808577f | -17.8246 | -57.4631 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 89.4 |
| 81a13718-2646-3bc3-9d9c-4deef58bdcfc | -17.7851 | -57.4679 | 2024-10-18 00:36:46 | GOES-16 | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 119.2 |
| c2650d39-1680-36d6-9d95-df604d2700f3 | -17.9036 | -57.4534 | 2024-10-18 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 79.3 |
| 96451350-66b1-3912-b032-88b221644f25 | -17.9234 | -57.451 | 2024-10-18 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 84.3 |
| 00328d18-b99d-3bd9-a44a-d9f012cf3859 | -18.0632 | -57.3514 | 2024-10-18 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 109.0 |
| 19c09803-7624-3890-88aa-bae618ae9ecf | -18.083 | -57.3489 | 2024-10-18 00:36:47 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 85.7 |
| 89272b30-a53b-3b8a-8e03-07ff044bcc05 | -18.5495 | -43.2208 | 2024-10-18 00:36:48 | GOES-16 | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 68.0 |
| a85cfc67-f914-3187-b8f4-cbb2620b9e1d | -18.2537 | -56.6237 | 2024-10-18 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 147.4 |
| 1547fa96-21dd-3421-883e-405397cdc2f8 | -18.254 | -56.6029 | 2024-10-18 00:36:48 | GOES-16 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 92.5 |
| de23953f-31c2-3eac-9acc-1db33fa9f81b | -23.37422 | -47.37068 | 2024-10-18 00:37:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 46.5 |
| a7ea7b16-9133-3f7c-8492-e0d041ae2465 | -21.9662 | -49.7186 | 2024-10-18 00:37:07 | GOES-16 | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 142.5 |
| 7e77656e-3a4b-36de-bed1-70b3ea0ee87d | -23.3701 | -47.3747 | 2024-10-18 00:37:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 152.1 |
| 34a7d79e-054a-322f-8276-fba7faaf7349 | -23.3709 | -47.3506 | 2024-10-18 00:37:14 | GOES-16 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 102.5 |
| bb4f22e5-24d9-3fb9-a97b-ee91d05da9d5 | -23.37032 | -47.37767 | 2024-10-18 00:39:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 147.9 |
| b3612565-94ec-3018-9f8b-fb7020837b5a | -23.36832 | -47.35863 | 2024-10-18 00:39:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 37.8 |
| 2631fb11-34c5-3973-98f3-fc10e242ef08 | -23.36389 | -47.39127 | 2024-10-18 00:39:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 24.0 |
| 0aa29091-0eef-36b7-b3b8-620d06d8eab4 | -23.36203 | -47.37214 | 2024-10-18 00:39:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 154.6 |
| 31584fe3-931d-3cbe-a0f2-ccab810b6709 | -23.35812 | -47.37907 | 2024-10-18 00:39:00 | TERRA_M-M | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 15.1 |
| bafac411-c0c6-3f3f-9863-85a954666031 | -22.40308 | -45.44281 | 2024-10-18 00:39:00 | TERRA_M-M | ITAJUBÁ | MINAS GERAIS | Brasil | 3132404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| 11545700-bc1c-3a3e-8a8b-1dc80571e36d | -22.35928 | -43.3596 | 2024-10-18 00:39:00 | TERRA_M-M | PATY DO ALFERES | RIO DE JANEIRO | Brasil | 3303856 | 33 | 33 | nan | nan | nan | Mata Atlântica | 7.7 |
| 74d4f1d3-6708-3f26-a8f1-1a2a1f950cb9 | -22.27679 | -42.59262 | 2024-10-18 00:39:00 | TERRA_M-M | NOVA FRIBURGO | RIO DE JANEIRO | Brasil | 3303401 | 33 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 6924742d-9083-33c6-9471-c037988ad8d1 | -21.96242 | -49.73192 | 2024-10-18 00:39:00 | TERRA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 178.3 |
| d1bf5c6b-f350-39b1-8347-9e013e35245d | -21.96002 | -49.70466 | 2024-10-18 00:39:00 | TERRA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 38.4 |
| 084e6df7-7638-3272-95d2-fc49aa733d48 | -21.9593 | -49.73916 | 2024-10-18 00:39:00 | TERRA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 111.3 |
| 82a3392b-87c6-3a5d-a8d2-269d11cedccb | -21.9567 | -49.71175 | 2024-10-18 00:39:00 | TERRA_M-M | GUARANTÃ | SÃO PAULO | Brasil | 3518107 | 35 | 33 | nan | nan | nan | Mata Atlântica | 94.3 |
| 4e33596c-bd90-383d-a203-094e671ebf7a | -21.33676 | -45.89322 | 2024-10-18 00:39:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.6 |
| 458e9384-32c9-3c25-a58c-513635b6e5ab | -21.33515 | -45.87925 | 2024-10-18 00:39:00 | TERRA_M-M | ALFENAS | MINAS GERAIS | Brasil | 3101607 | 31 | 33 | nan | nan | nan | Mata Atlântica | 34.4 |
| dd9ead18-3c3d-39d0-8284-2f260ca5e4e3 | -21.15815 | -44.98207 | 2024-10-18 00:39:00 | TERRA_M-M | IJACI | MINAS GERAIS | Brasil | 3130408 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.5 |
| 2ec308bf-0153-36da-b7cb-ab8cb1b044db | -21.12805 | -44.07895 | 2024-10-18 00:39:00 | TERRA_M-M | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 7.4 |
| 2c6b9110-478b-32d3-a2a5-b35c272dfdc9 | -21.1267 | -44.06818 | 2024-10-18 00:39:00 | TERRA_M-M | PRADOS | MINAS GERAIS | Brasil | 3152709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.6 |
| c796718d-6662-36a1-b21a-02126291f111 | -21.01551 | -43.84059 | 2024-10-18 00:39:00 | TERRA_M-M | CARANDAÍ | MINAS GERAIS | Brasil | 3113206 | 31 | 33 | nan | nan | nan | Mata Atlântica | 18.4 |
| 6f6bc474-108e-3d85-81b4-b7579f397291 | -20.96701 | -46.46336 | 2024-10-18 00:39:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Mata Atlântica | 15.6 |
| ec2f3cbc-935f-3f2e-a454-d1df686e03d0 | -20.83778 | -46.32483 | 2024-10-18 00:39:00 | TERRA_M-M | ALPINÓPOLIS | MINAS GERAIS | Brasil | 3101904 | 31 | 33 | nan | nan | nan | Cerrado | 10.3 |
| 84726349-8683-3f0c-be47-f95092c9171e | -20.79686 | -50.68937 | 2024-10-18 00:39:00 | TERRA_M-M | SANTO ANTÔNIO DO ARACANGUÁ | SÃO PAULO | Brasil | 3548054 | 35 | 33 | nan | nan | nan | Mata Atlântica | 57.1 |
| 7f66002e-f490-38ee-8651-088343160e30 | -20.62539 | -43.03426 | 2024-10-18 00:39:00 | TERRA_M-M | PORTO FIRME | MINAS GERAIS | Brasil | 3152303 | 31 | 33 | nan | nan | nan | Mata Atlântica | 5.7 |
| 8cad33d3-e5f7-3e08-8454-296bf39ae678 | -19.91183 | -42.25308 | 2024-10-18 00:39:00 | TERRA_M-M | BOM JESUS DO GALHO | MINAS GERAIS | Brasil | 3107802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| bd9ff734-e4ad-3873-80b9-dd8759366485 | -19.8462 | -46.02327 | 2024-10-18 00:39:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 8.4 |
| 3c6a831a-951d-346b-a3f8-4cc59af92c3c | -19.84053 | -46.02951 | 2024-10-18 00:39:00 | TERRA_M-M | CÓRREGO DANTA | MINAS GERAIS | Brasil | 3119807 | 31 | 33 | nan | nan | nan | Cerrado | 9.3 |
| 24daa19c-9040-3edc-b9a1-ce6006013886 | -19.50546 | -42.3703 | 2024-10-18 00:39:00 | TERRA_M-M | CARATINGA | MINAS GERAIS | Brasil | 3113404 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.8 |
| 5af7d3ab-997c-3f11-b768-f8bb37f5a1e7 | -19.37275 | -41.61721 | 2024-10-18 00:39:00 | TERRA_M-M | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.1 |
| 6f436c86-ff7d-3005-b11a-9b4b994e6760 | -19.36202 | -41.61583 | 2024-10-18 00:39:00 | TERRA_M-M | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 11.4 |
| 6d80f467-bef7-3bb4-aa9f-67bf8013f983 | -19.36069 | -41.60642 | 2024-10-18 00:39:00 | TERRA_M-M | ALVARENGA | MINAS GERAIS | Brasil | 3102209 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.7 |
| 9f7eb271-277c-394c-a537-f525196d8a64 | -19.32449 | -44.6368 | 2024-10-18 00:39:00 | TERRA_M-M | PAPAGAIOS | MINAS GERAIS | Brasil | 3146909 | 31 | 33 | nan | nan | nan | Cerrado | 5.2 |
| e46b356b-7b88-3782-9d40-49bb29a92367 | -19.04701 | -40.21045 | 2024-10-18 00:39:00 | TERRA_M-M | SOORETAMA | ESPÍRITO SANTO | Brasil | 3205010 | 32 | 33 | nan | nan | nan | Mata Atlântica | 12.4 |
| 14078897-96ea-306e-b02a-48da46236b9e | -18.67885 | -43.05709 | 2024-10-18 00:39:00 | TERRA_M-M | SABINÓPOLIS | MINAS GERAIS | Brasil | 3156809 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| c4b80d33-0e24-32f8-8035-76da32ea9bbe | -18.61826 | -40.25548 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 5.1 |
| c88874dc-3d57-396b-ac48-c059c6c6e210 | -18.611 | -40.25249 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO MATEUS | ESPÍRITO SANTO | Brasil | 3204906 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.8 |
| f51054a2-f2e4-3ff0-b08d-cc1ebcae7adc | -18.60152 | -41.00429 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 14.1 |
| cba15887-9e17-3c19-9211-8acf3a2c49a2 | -18.60011 | -40.99466 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 22.8 |
| c1276b17-8a9c-32de-99fe-ed0c0e10a0ad | -18.55688 | -40.95202 | 2024-10-18 00:39:00 | TERRA_M-M | ÁGUA DOCE DO NORTE | ESPÍRITO SANTO | Brasil | 3200169 | 32 | 33 | nan | nan | nan | Mata Atlântica | 6.6 |
| 7dd9596f-ec71-3b42-aa1c-e0ffbf421784 | -18.55507 | -43.23295 | 2024-10-18 00:39:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 14.7 |
| 578f2278-4160-3d02-a107-d4e605e66c28 | -18.54613 | -43.23434 | 2024-10-18 00:39:00 | TERRA_M-M | SERRO | MINAS GERAIS | Brasil | 3167103 | 31 | 33 | nan | nan | nan | Mata Atlântica | 29.8 |
| 37f681c8-7f76-3803-8cf5-378bfe7120de | -18.40571 | -42.4724 | 2024-10-18 00:39:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 26.6 |
| 52c39b7e-96b2-3fd3-a3e1-4b167feb3348 | -18.40442 | -42.46313 | 2024-10-18 00:39:00 | TERRA_M-M | PEÇANHA | MINAS GERAIS | Brasil | 3148608 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| 749beff6-8b09-33fb-81c0-bdb0b03f2b8f | -18.4036 | -42.19785 | 2024-10-18 00:39:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.4 |
| 5b548b95-2e7c-3787-a191-9bea79d532d5 | -18.39605 | -42.20851 | 2024-10-18 00:39:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 13.8 |
| 03f3c7fc-7f18-3595-80de-ee229c21b765 | -18.39475 | -42.19925 | 2024-10-18 00:39:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 307576fc-52d3-35dd-b17c-4016733915c7 | -18.3872 | -42.2099 | 2024-10-18 00:39:00 | TERRA_M-M | VIRGOLÂNDIA | MINAS GERAIS | Brasil | 3171907 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| e8efaffa-4f04-35df-88b3-df4173a229c2 | -18.3859 | -42.20063 | 2024-10-18 00:39:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 12.1 |
| b001cb27-7cd5-3d69-8526-a4f90d7198a2 | -18.31471 | -41.88886 | 2024-10-18 00:39:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 46a2e44a-e337-390b-a1f0-c42838629763 | -18.29638 | -41.89825 | 2024-10-18 00:39:00 | TERRA_M-M | ITAMBACURI | MINAS GERAIS | Brasil | 3132701 | 31 | 33 | nan | nan | nan | Mata Atlântica | 9.7 |
| bb06aed3-886c-3f0c-922e-452cbe3f5293 | -18.28645 | -42.21324 | 2024-10-18 00:39:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.2 |
| 1e0e6eec-7b1b-3467-b181-1f90242601a8 | -18.28515 | -42.20399 | 2024-10-18 00:39:00 | TERRA_M-M | SANTA MARIA DO SUAÇUÍ | MINAS GERAIS | Brasil | 3158201 | 31 | 33 | nan | nan | nan | Mata Atlântica | 25.1 |
| 3d9c143a-5f77-38fa-ad6d-e51f28ebb612 | -18.25016 | -42.67933 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO JOSÉ DO JACURI | MINAS GERAIS | Brasil | 3163508 | 31 | 33 | nan | nan | nan | Mata Atlântica | 8.0 |
| c2dedadb-0d54-330d-8869-70249556aadc | -18.10944 | -41.42524 | 2024-10-18 00:39:00 | TERRA_M-M | FREI GASPAR | MINAS GERAIS | Brasil | 3126802 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 91072d2a-1eb3-334f-baab-243bd4b9fc64 | -18.09949 | -42.85699 | 2024-10-18 00:39:00 | TERRA_M-M | ITAMARANDIBA | MINAS GERAIS | Brasil | 3132503 | 31 | 33 | nan | nan | nan | Mata Atlântica | 6.9 |
| c5a40968-d3af-3285-8354-b0c96dcce274 | -18.09925 | -42.65797 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 4.8 |
| 67173503-3a5e-3b01-9f86-17c230d7504c | -17.96911 | -42.51423 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 20.4 |
| 8e9051bc-c367-3f5c-8095-b354515f0c40 | -17.96155 | -42.52483 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 3.1 |
| fb6e724c-270e-3938-bcbb-ca422b945903 | -17.96026 | -42.51559 | 2024-10-18 00:39:00 | TERRA_M-M | SÃO SEBASTIÃO DO MARANHÃO | MINAS GERAIS | Brasil | 3164506 | 31 | 33 | nan | nan | nan | Mata Atlântica | 43.8 |


[Clique aqui para ver as próximas entradas](README4.md)
