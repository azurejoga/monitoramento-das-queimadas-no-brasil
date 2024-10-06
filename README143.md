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

## Dados Diários - Página 143

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 663b0e63-47cf-39bf-bb5d-f202a8d33aeb | -17.02332 | -56.73208 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| c6172896-f34e-34e9-9885-74d95a008439 | -17.02311 | -56.70872 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| ae37f21f-1adf-3455-96dd-ba0de5acffce | -17.02295 | -56.73549 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.4 |
| 3f212cf5-f231-3f2f-9bf6-ce4a71641838 | -17.02272 | -56.71214 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.0 |
| 0b791871-6566-3995-90ec-cb162b8dfed7 | -17.02232 | -56.71556 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 95ab6da0-05f1-34aa-a12f-2ae0291f1fc8 | -17.02193 | -56.71899 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| da0249b7-c14b-3ff3-9334-76d34b7f29d5 | -17.02154 | -56.72241 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 3ffe7497-7f67-347d-8c60-b01c98973cdc | -17.02131 | -56.70056 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0ea6eb6c-860f-3ec9-b59e-2d611d2cdbac | -17.02114 | -56.72585 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b4895148-e6d3-3442-bb86-89961dcdd8d8 | -17.02094 | -56.70401 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 0276d446-1c9e-3be0-897a-5d14e76ae02f | -17.02075 | -56.72926 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 6e000aab-9f2c-3d31-8f5e-bdf79c75d81c | -17.02057 | -56.70742 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 1ae5fece-f174-3db7-a505-9748ad00555a | -17.02035 | -56.73268 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 30875101-b152-312d-8b24-294cc482c1fb | -17.0202 | -56.71085 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c9786f6f-8658-3a55-9e9d-31d9ed11949c | -17.01984 | -56.71426 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 3928c85b-810d-3163-9222-31f7d93e39ac | -17.01947 | -56.71769 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| c2cb0483-04b2-3545-b789-3bc7610ad89a | -17.0191 | -56.72112 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 7b9d1790-4df5-3c79-a7d8-2e1c7ea4e335 | -17.01873 | -56.72455 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| a1962a41-5ea4-352b-af54-be9866312f9a | -17.01856 | -56.70121 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 4919d224-5e55-3d95-9f49-62a15d462511 | -17.01836 | -56.72799 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| d129fb1c-4ca0-3d52-8fe2-773c2b744309 | -17.01816 | -56.70465 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 823b08e8-4ce9-3ece-af1a-273dac170a7d | -17.01799 | -56.73141 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 62952de5-abef-3d70-b891-9769bd70457e | -17.01777 | -56.70807 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| b73c5c94-7f23-33f3-8563-31bda4838ffe | -17.01738 | -56.71149 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 151bde72-a9b3-3ee2-bd0e-ab18f49a78ef | -17.01699 | -56.71491 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| c4d5f9ef-a40a-387f-b9ca-11356d04da36 | -16.92699 | -57.69495 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 63900b4e-74ae-3b2d-9d75-4d2dd819cd77 | -16.92632 | -57.70083 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 01865a12-e85f-3cc5-8d24-4c614e1205db | -16.9225 | -57.69416 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 1896dd92-add0-3995-9d1e-2a0e24d59506 | -16.92199 | -57.69431 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 9b4eba42-295c-33c3-aeda-1c91daa2b5d6 | -16.92179 | -57.70003 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 18fe7ef8-a307-3eb9-9d33-f3f4286e34dd | -16.92133 | -57.70018 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.0 |
| f160e8a8-d71c-3487-9c72-618b3428cadb | -16.91751 | -57.69353 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 67738818-ba4e-349a-a3db-b7f8b87e6524 | -16.917 | -57.69366 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 5e43940e-8aad-3170-a666-6d2fb211d9dc | -16.91322 | -57.68704 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.5 |
| 8f4c09a6-88b9-3f9a-b5e4-d4e4259feeb6 | -16.91266 | -57.68714 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 323a1e92-4e25-338d-837e-08d3616ce99b | -16.91251 | -57.6929 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.7 |
| 80bea667-4826-370e-86b8-851bf9fca7e2 | -16.89267 | -57.68457 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| e4112f4a-fc58-3add-931a-48c5483bf76e | -16.85292 | -57.45966 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.4 |
| 6fb1b279-a6f2-386e-a229-a5b6a9943e02 | -16.83899 | -57.45926 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.5 |
| 79c8ca42-1223-3ed0-9424-3b36cb493260 | -16.83771 | -57.4577 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 7cad8ffd-c725-3b9f-b8bf-2f8587c507bf | -16.83446 | -57.45407 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| d1f1963b-fb38-3f9b-8cf8-0b03d975e67e | -16.83392 | -57.45863 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| c52d4f48-e041-3c65-9e52-436300495380 | -16.83339 | -57.8067 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.4 |
| 3bb2df0a-e130-3d1b-ac68-05bfd0d58cce | -16.83332 | -57.45097 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| cdaa3474-1b42-367e-8514-918d719cc43a | -16.83264 | -57.45705 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.1 |
| 0867dae8-4275-321f-9f00-3b5c0c9c7842 | -16.82975 | -57.4504 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.0 |
| bd71c7be-a69b-3050-ae16-7a93cb3a6188 | -16.82378 | -57.45736 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| 13195944-c3f2-3920-b9ae-cbcfdad539fe | -16.82317 | -57.44969 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.7 |
| d4875bbe-3613-39ed-9903-e612b03fbf86 | -16.82215 | -57.4588 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.1 |
| 0562bddb-f765-312c-b06b-35c4c45a9bb3 | -16.81925 | -57.45218 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.4 |
| 045a863f-6efd-316b-bb26-7ec0487989ac | -16.81871 | -57.45673 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 7.3 |
| a5572f77-9f6f-3c24-b63e-35c42fea788e | -16.81454 | -57.44849 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| bad08b41-9e1e-3edb-97c0-366124a04a30 | -16.80065 | -57.39104 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 27cf11b9-36d6-32de-8c12-773a2d4d6091 | -16.80029 | -57.3941 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e5f895d0-e71a-3e63-a847-3372d2a368bc | -16.7952 | -57.39346 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| b20b4242-c535-34d5-a010-e67f32b8436a | -16.78953 | -57.44225 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 821245bb-f2ee-3c6e-8526-e873a411be18 | -16.78688 | -57.465 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 7ff2bc5a-4003-34ed-9d04-dd8097b1c9d6 | -16.78411 | -57.44464 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 2c5c21e2-4af6-39da-aafa-92947955c0a5 | -16.77761 | -57.50058 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 2ddcacee-7922-3619-bac3-fa21dec1e9a0 | -16.77465 | -57.48188 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 61dcef1f-af83-3a67-804e-3582440ce7e9 | -16.77239 | -57.45702 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| fb43f364-5069-31dd-9370-d59271fd087f | -16.77099 | -57.46914 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.3 |
| 5c1927c5-ec3e-3262-9031-6a78b00bb187 | -16.76959 | -57.48123 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 899a01ff-c133-3ce2-89f5-106ccce4af17 | -16.7689 | -57.48726 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 6a79288b-256b-3578-a49c-792021db5c8b | -16.7682 | -57.49328 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 2de230e1-e244-337a-9928-decb76f99f1b | -16.76454 | -57.48059 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.9 |
| 225f40ee-107f-3fd5-a5b5-099714146e42 | -16.76384 | -57.48662 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| d0c19e57-a133-35dc-aa9a-dcfa4541d71d | -16.76315 | -57.49265 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.6 |
| 10ae989a-6baf-3cca-ae0c-6e5e458041b7 | -16.71531 | -57.46201 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3e541f63-5589-37be-98d2-06d4e53472e6 | -16.70957 | -57.46742 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 50621816-afce-33f0-a16b-23d5f8c11753 | -16.70659 | -57.46538 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 5.1 |
| a39ff8f0-0157-3c66-8433-c912ba45ef1d | -16.70452 | -57.46677 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| f8eed663-961f-3bf9-8687-2cee88de12d7 | -16.68777 | -57.45074 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| c5ee7832-25f6-3229-ba05-eca7ca083ff0 | -16.67554 | -57.46757 | 2024-10-06 05:38:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| a9eb0438-1153-39cb-8a35-1cc87e3b9a3f | -16.98034 | -56.75196 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 08dc05d4-9ccf-3e34-9ca4-dd1f1964880a | -16.97996 | -56.75537 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.3 |
| 2e25c5e7-9cb0-3a13-b021-91b852fe0ad4 | -16.9799 | -56.80351 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b721f87a-f67b-3c92-a4fd-7f524bc88910 | -16.97957 | -56.75877 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 42563ffa-ec0c-3ecf-9d9b-9f0c5168412b | -16.97919 | -56.76217 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| e73c4081-305b-3bb5-a148-4af504b40140 | -16.97881 | -56.76557 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| b0aa79b6-44cc-3646-88d7-cabb68ba54d6 | -16.97497 | -56.79949 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| 181c5794-841c-3168-818a-ecb0c677ebc0 | -16.97459 | -56.80287 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| c85d7ec4-0913-3a89-b342-95ef121a93e0 | -16.97421 | -56.80625 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 9fb79afa-1ff1-3abb-895f-0da927166bed | -16.97387 | -56.76151 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.2 |
| 6a04ea78-a21c-30d9-9a70-4aada94c16da | -16.97349 | -56.76491 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 6.8 |
| ba8791f2-7c0f-31d5-ab9b-627b0bae1cc6 | -16.97081 | -56.78868 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.2 |
| 215c94fa-747c-3158-a531-a5732b9dfea5 | -16.97043 | -56.79207 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.2 |
| 113cc2ec-f95a-3a20-8b56-80c18b62fc10 | -16.96929 | -56.80223 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 3.3 |
| b346834f-b053-3e19-9d70-146c1e00a137 | -16.96855 | -56.76086 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 4.8 |
| 3dd18642-77b4-391e-853c-9d9e0e80a2a7 | -16.96817 | -56.76425 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| a62e55b7-a25e-375b-9d08-1b80c2d00946 | -16.96588 | -56.78464 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.0 |
| 1bdcbdee-d0af-3e14-a518-2cf3426dbf82 | -16.96247 | -56.76701 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 5.8 |
| 7a91f704-d3a2-35f2-bf5c-bd0396d8e5f0 | -16.96209 | -56.77041 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 84c79fbd-3d5f-343e-8f60-8ac34573df66 | -16.96171 | -56.77381 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 11.7 |
| 824ce1be-71f1-3d14-8fe4-a16cecae92d9 | -16.86587 | -56.72833 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 8f9e308d-d078-3e09-82bf-21d7c39ece22 | -16.86549 | -56.73172 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| d079fe61-0d04-3d0d-bcea-8710f3014644 | -16.86207 | -56.71405 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9024c4d3-c275-3e5e-ab5e-d4901fc2b972 | -16.86169 | -56.71746 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 2.8 |
| a401ad2c-da93-3ac9-ba05-cf12bea5ad3b | -16.86017 | -56.73108 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 18d3f1eb-4bb1-3ed1-b31d-e81d9848b746 | -16.85979 | -56.73447 | 2024-10-06 05:38:00 | NPP-375D | POCONÉ | MATO GROSSO | Brasil | 5106505 | 51 | 33 | nan | nan | nan | Pantanal | 1.5 |


[Clique aqui para ver as próximas entradas](README144.md)
