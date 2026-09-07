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

## Dados Diários - Página 15

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d5c03d0e-9a67-35fe-80c6-f10684336e28 | -12.19892 | -45.03864 | 2026-09-07 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 02009976-86f9-39c1-b1b1-1ee6e1581a3f | -11.32996 | -45.04929 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 45de07d9-70a6-3b25-be01-e98072f154f1 | -9.72763 | -43.40296 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Caatinga | 9.4 |
| 28c20fb0-cdf7-3e0e-aafc-51513fc3ea47 | -11.31776 | -45.05956 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 41db6c31-d8dc-3275-90f1-8bcd755c7d09 | -9.74696 | -43.40075 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| de2d53e8-298e-349a-ae1e-578203c3e5f7 | -11.3282 | -45.06144 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| bb6ec4f5-bca6-30d7-b48c-16dd7384cebd | -11.30983 | -45.10341 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8681adb9-1382-3d41-a9a5-8692b508caf9 | -13.30844 | -45.23806 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 04c9e923-fb26-3ca3-9e35-3ebc0a44752d | -5.32448 | -55.87608 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41d6b16b-71a5-34f9-aba2-c7a5fe3b29d7 | -11.29122 | -45.13261 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 80a1deaa-d56f-3936-9476-e455c3982410 | -5.36132 | -56.02406 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b786a43c-ec6e-320e-b8c6-e598de92249f | -11.337 | -45.09894 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| cdd5705d-97d7-3a81-ab09-07547579fd14 | -5.29603 | -60.1335 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 4.1 |
| bbe51cfc-cd41-3df4-b6ab-5bda96c2dc76 | -11.31449 | -45.09608 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cecf43cd-e09f-3a06-b90b-36813ae227f0 | -11.3312 | -45.08983 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 61821f1d-ac2f-329a-a266-c6b0f624757e | -7.37449 | -47.76294 | 2026-09-07 04:27:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c26fba8d-61dc-3455-a993-7168deb8d5c0 | -12.76341 | -52.8496 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c74a61c6-04e5-33cf-b82a-94d526b759da | -9.25063 | -46.68847 | 2026-09-07 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 6c403376-0f5b-3e76-961e-369e1f0f0144 | -12.7628 | -52.8531 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d6d51244-9dfd-3f4b-b50a-84ac24bace70 | -11.31626 | -45.06042 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 56a2cdf5-c8fa-365b-9b73-8c59eb5dc88b | -9.74323 | -43.40029 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| e4a3473f-5e04-3816-8f15-dcf5a4515f7d | -5.36433 | -56.03987 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cc3b27e8-d2d8-3d98-91e8-b54b269dbba8 | -11.77553 | -48.84122 | 2026-09-07 04:27:00 | NOAA-21 | GURUPI | TOCANTINS | Brasil | 1709500 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 54311a9f-224a-32c7-9ce6-ace02fd6a1ea | -9.99123 | -50.27817 | 2026-09-07 04:27:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 173163ae-ab2a-31d8-9435-1a6e6da95e83 | -12.76463 | -52.84256 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 6207aabd-99cc-3e5e-afda-b24b50890f97 | -7.95288 | -45.24287 | 2026-09-07 04:27:00 | NOAA-21 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| e9f1b6ec-0856-3389-86f5-ab67df17a288 | -5.29881 | -55.86026 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6b35ba6c-6e02-3b17-a298-2c438ca49aad | -8.87994 | -46.7967 | 2026-09-07 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f195ec9a-d75c-3d36-943b-66d4be10b526 | -8.94681 | -44.40607 | 2026-09-07 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 32a7d868-a74c-3733-a8a3-c19cc52eaeb4 | -12.76066 | -52.84183 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0dc634a8-86af-32f1-abcf-4b1e102831ed | -13.30196 | -45.23291 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| a1de2db9-1e95-3f4e-9bcc-f7aec2d89952 | -11.31858 | -45.06876 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ba4e578f-20b4-3301-8ca6-140172ad0ef4 | -7.10263 | -56.51112 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| e179a493-9075-3294-b286-0d1650d72303 | -11.30923 | -45.10738 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| b579b8e3-19af-32e9-bba4-802f54bc8a2a | -11.28196 | -45.09912 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ee1c877d-5b2e-398f-b53d-f7ff1a27049c | -11.32011 | -45.06791 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 7a48ef5d-db83-3040-938f-bdf4588f43a5 | -11.50974 | -49.61563 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| 51f71701-63d1-3c2e-a31f-96facf422dc9 | -5.36989 | -56.04087 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 8981656d-2bd4-3aa8-a778-28a13b886cae | -9.74568 | -43.40976 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 1b52738e-4f74-3ede-afca-69a0831c357d | -5.37053 | -56.03716 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| bb188980-dd97-3385-817a-abd0d43fe1bf | -5.36497 | -56.03616 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 4df276a4-6b9a-3e91-9bd2-3dd8d2127bb5 | -12.1754 | -42.96305 | 2026-09-07 04:27:00 | NOAA-21 | OLIVEIRA DOS BREJINHOS | BAHIA | Brasil | 2923209 | 29 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 684b1f16-bfab-334e-a1dd-a03e4913f67e | -5.35641 | -56.01937 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| bf39bf26-55a8-323a-a66e-dde043315aed | -11.51597 | -49.62055 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 201bb9d5-1dde-35ca-88c9-38bd73289688 | -9.74194 | -43.40931 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| ff4eef94-c495-3936-9112-700a82d9ffbf | -11.32032 | -45.05714 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e0bb47a-63a2-3dd9-83c8-5ead52417c69 | -13.30961 | -45.22995 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 140.9 |
| 7813e8b1-7563-33ef-b228-91b68c2f41c6 | -6.05772 | -57.78845 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 3e98f1d6-506b-3867-82d4-e0bdd813bac7 | -11.52969 | -49.62283 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fcaf3ccd-e368-3595-9432-e479cf3a38bf | -11.31095 | -45.10651 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3a431df3-77c0-3f8e-991d-2060fba69e04 | -9.73693 | -43.41776 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 2bd3d77c-9c15-34ec-8c3f-aef637d279f9 | -5.99674 | -57.70668 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| 2dfa0824-3719-36a4-a4f4-e4602911b304 | -5.29941 | -55.85669 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 017c6f09-a2bd-3167-8eec-53fb2a7ec684 | -6.13559 | -57.74314 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 4690b861-7ca9-3b9c-913c-47c14740d2b0 | -5.31897 | -55.87507 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b0c3d4cc-25f2-39a7-be91-7149a74ece36 | -11.2773 | -45.10649 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 62a93570-4a72-3174-b55f-b4c7957411be | -12.76097 | -52.86365 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| ecd08f19-af98-33f7-b2ad-f61a4b64ed72 | -9.73574 | -43.39941 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 18dbe0f6-5e99-31c7-b3a3-c1812d6fcf94 | -11.51316 | -49.61619 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 21.5 |
| ceac0923-34cd-3835-97e0-156f5645ba29 | -9.93549 | -48.047 | 2026-09-07 04:27:00 | NOAA-21 | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 4dda7b7c-8fc2-3ebb-a89f-30460304242d | -11.33007 | -45.09757 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 6.8 |
| eec4f9f0-a51d-3798-a1ac-1be85d405869 | -5.29302 | -60.13279 | 2026-09-07 04:27:00 | NOAA-21 | NOVO ARIPUANÃ | AMAZONAS | Brasil | 1303304 | 13 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 84b433a5-87fa-3f94-a290-6424b5305640 | -8.97898 | -44.40702 | 2026-09-07 04:27:00 | NOAA-21 | CURRAIS | PIAUÍ | Brasil | 2203230 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 27c51fab-c002-35ff-881a-1588853bd28c | -11.31915 | -45.06493 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 11a0eea0-ef55-3748-9a15-66d782375224 | -5.31921 | -55.87333 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| cf860bea-86f8-3d25-800d-a03b30aa12a0 | -9.7413 | -43.41379 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 56792084-0046-3d35-99a5-ba6a3d2d87c6 | -11.32472 | -45.06082 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| abc16e36-7c98-3a1c-89ac-d6dca773ed40 | -7.91338 | -47.66758 | 2026-09-07 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 054c5727-16a8-37f2-af62-a28b2b449dfc | -11.32647 | -45.04873 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5a4a2ec8-f6e4-33a9-933c-8505b9dfd397 | -5.99843 | -57.69733 | 2026-09-07 04:27:00 | NOAA-21 | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 260c1686-8a8d-31b8-99e1-207b70225007 | -9.73566 | -43.42667 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 1359b246-7d76-3281-a56c-d8f8351a3eff | -11.51878 | -49.62492 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 41e96b1d-3fe5-38ce-a53e-9c79efad1f82 | -9.57575 | -40.3522 | 2026-09-07 04:27:00 | NOAA-21 | JUAZEIRO | BAHIA | Brasil | 2918407 | 29 | 33 | nan | nan | nan | Caatinga | 6.2 |
| 2540ca74-ce8b-3f2f-92ad-10e19cbe0162 | -11.33524 | -45.08656 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 7.5 |
| f4fd1002-4a38-3847-8b72-f0f748aca7ad | -11.32829 | -45.08534 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 99bd8087-969c-32d5-848d-fb0134b95558 | -5.37116 | -56.03345 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| f6c9b225-4f0c-33ea-b827-6b4aecb372a2 | -5.35941 | -56.03519 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e20fd904-f9b2-395d-99ff-b378fbb5cb03 | -11.32415 | -45.06471 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 29.2 |
| 0d2b20a6-117c-3de9-8158-98aad3972248 | -13.31197 | -45.23859 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 83.7 |
| 258930a5-d12e-3b76-a7f0-16e5cf689ac5 | -9.73629 | -43.42221 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 28.5 |
| 3e560913-ca16-35a8-9585-6716d744f2d0 | -9.74876 | -43.41479 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 66.2 |
| 4e9c057c-648a-3a5a-be07-686683d94465 | -5.35513 | -56.02676 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1bf98ace-2415-3c51-bbe1-0f2a61b78d3a | -11.33354 | -45.09826 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 52.2 |
| ce5c2d43-58a3-3b64-a192-688c80ea387e | -13.30255 | -45.22885 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 93.4 |
| bbafd52d-453c-3751-80bf-9e50ddcf5574 | -7.70326 | -55.38261 | 2026-09-07 04:27:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| c401e698-70e9-3936-926a-4edea78da9a5 | -11.32359 | -45.06855 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 16.9 |
| 3900f994-db50-35da-8614-b0f2c01d359d | -5.35704 | -56.01571 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| ae8a80ba-b6ea-3805-ad62-e391ec18b5e9 | -14.86584 | -40.91801 | 2026-09-07 04:27:00 | NOAA-21 | VITÓRIA DA CONQUISTA | BAHIA | Brasil | 2933307 | 29 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| 1e806042-49a5-3341-aa12-d6f9ffdaf3bf | -5.36196 | -56.02037 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e44b6825-94a6-3940-a223-02b5d771aaaf | -9.74258 | -43.40483 | 2026-09-07 04:27:00 | NOAA-21 | PILÃO ARCADO | BAHIA | Brasil | 2924405 | 29 | 33 | nan | nan | nan | Cerrado | 136.5 |
| 67c428f4-cf36-3eff-a4aa-7c90d98164bb | -12.75271 | -52.84037 | 2026-09-07 04:27:00 | NOAA-21 | CANARANA | MATO GROSSO | Brasil | 5102702 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d1240258-2c9a-353d-9eb4-36bfb26e879b | -10.07156 | -49.12669 | 2026-09-07 04:27:00 | NOAA-21 | MONTE SANTO DO TOCANTINS | TOCANTINS | Brasil | 1713700 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 219b2496-358c-3e4d-8130-8a835b2e93cf | -5.34765 | -56.03686 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 3736dba2-c736-3e8a-a1d0-f9286e9866c8 | -10.66764 | -45.17522 | 2026-09-07 04:27:00 | NOAA-21 | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 310e1fc6-7206-33fb-b505-3bad561773f0 | -13.30667 | -45.22534 | 2026-09-07 04:27:00 | NOAA-21 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 19.5 |
| 8413fc56-da99-367d-8dd7-ee8b38c72795 | -7.91283 | -47.67109 | 2026-09-07 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f309c5e7-594e-34d4-960b-ae7d4ffdff04 | -8.88048 | -46.79322 | 2026-09-07 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 01b1ff7c-6a90-35f7-acec-79320361cb0d | -7.10684 | -56.51977 | 2026-09-07 04:27:00 | NOAA-21 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a216433a-a7d2-37a1-b70f-c0de27f97886 | -5.36814 | -56.0177 | 2026-09-07 04:27:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 96670336-3f09-3cdf-b753-02d6a6a6d861 | -11.51192 | -49.62378 | 2026-09-07 04:27:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |


[Clique aqui para ver as próximas entradas](README16.md)
