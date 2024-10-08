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

## Dados Diários - Página 119

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cb6f9f45-7cb2-3e3b-8337-3cc3192907b3 | -16.80075 | -57.43136 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 1801e173-8a34-313b-b5a7-bb955ca37327 | -16.80026 | -57.43517 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 3b05a17b-dc63-353e-9f8d-b76b23582b0f | -16.79762 | -57.42318 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 25b47575-2ce4-35ad-ba25-9ae4c5836aa0 | -16.79665 | -57.43079 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b4bf4eca-3210-3132-939c-9d2ef3446a5f | -16.79422 | -57.44976 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ea1e04b6-a269-30fa-bdab-3b0a3fc55cbd | -16.79254 | -57.43021 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| f8a3d927-c3a7-30be-a2af-714eb50eeae0 | -16.79206 | -57.43402 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 5e48b7db-629a-3e22-a610-2a6bd7a45c07 | -16.79061 | -57.4454 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 56c2e241-6bd6-3107-89c8-9bcdf11e5f3a | -16.79012 | -57.44918 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.5 |
| 3283a888-62fe-3cec-baf5-37af9e7d361e | -16.78385 | -57.43285 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 4b6b3648-1351-3f0d-ade7-a3c160887daa | -16.77618 | -57.46725 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 511f143c-1c43-36db-ad44-929b894918ca | -16.77568 | -57.47103 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| d1e0ea0d-2482-3889-8621-6fcf33360ad4 | -18.63995 | -57.2266 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 54f91343-1f17-35a2-b4f0-6ccce7bf00c2 | -16.77542 | -57.46639 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 6.9 |
| 71bbead6-4e4a-3a41-83a7-f02490ecac60 | -16.77494 | -57.47018 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 3f15a45a-1569-3483-a49a-e438471a28c8 | -16.77446 | -57.47396 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| 131a30b1-8db9-33b4-8580-d3e7856e5e70 | -16.77209 | -57.46669 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.9 |
| 008304e6-69f0-3a35-ac3d-98e8b1d7fc3d | -16.77159 | -57.47046 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 314a86ce-20df-37d1-83a2-d760ee656e1d | -16.77085 | -57.4696 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.1 |
| f8cb5866-39ad-3117-86d4-1bd9dd78963f | -16.70564 | -57.46504 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 62ac50e2-0e6a-3d97-a612-5a7fe41d4321 | -16.70155 | -57.46446 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 3f6f0b61-f0f1-315f-a888-c664b0a2c584 | -16.69843 | -57.45634 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| d01067e2-7fa5-3f70-bf59-6af53d87bf4e | -16.6958 | -57.44443 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| d72d83ea-82e4-38c8-bec0-fa7e89e0d052 | -16.69482 | -57.45198 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 2af2e794-81ba-3988-b5ef-f9cfaf5a6df1 | -16.69434 | -57.45576 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 59bfd790-b7b9-38db-acc8-6db827a8e229 | -16.6917 | -57.44386 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 29436a8b-64c8-3dd9-884b-f4032633f463 | -16.69073 | -57.45141 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 0e8977fe-714a-3798-8c9e-febf96a4fa2b | -16.69024 | -57.4552 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.7 |
| 466e1b67-4c9c-3e4c-b891-26db0f14875a | -16.68976 | -57.45897 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| df15b5d8-f37a-3675-876b-17ab47687cfe | -16.68664 | -57.45084 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.3 |
| 41656c5a-781b-3552-898d-96d7bd83cda9 | -16.93596 | -57.47721 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 1cd6762e-0375-359e-947d-ceea9853f73d | -16.93546 | -57.481 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 9a95d9a9-2da9-37c6-972c-ae410a26cfec | -16.93497 | -57.48478 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6df6b001-daa6-3a5d-a024-1c9ebbd1a994 | -16.93448 | -57.48857 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 643684cc-f5d0-3bdb-98d0-8e3a07721335 | -16.93235 | -57.47285 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| a92d1189-8517-3412-b8ac-b562e0a1e6ee | -16.93186 | -57.47664 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 7d8f6c3c-c004-36e0-935d-ca09c4c4aab1 | -16.93136 | -57.48043 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 1c6c1b7d-d27c-3b57-98df-6c633f667fd1 | -16.93087 | -57.48422 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 4e03acf9-d8dc-3084-83dc-0df25798442e | -16.93038 | -57.488 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 98a38875-84e0-32da-a389-71080ed5eb1a | -16.92989 | -57.49179 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 60c4fa29-011e-33fb-9ca1-b6c0c3d1efa6 | -18.63569 | -57.22602 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 4a4bdf02-ca98-3ccc-aec2-a44557177c9b | -16.92825 | -57.47228 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.8 |
| 487391f7-35cb-37a5-840d-16fc7e2de221 | -16.92787 | -57.69661 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| f3081641-298d-3d48-b0a5-c0415dd40333 | -16.92776 | -57.47607 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| ed3ca9bd-feee-3941-a57e-63bc43fd90a9 | -16.92727 | -57.47986 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 10.8 |
| 6b251a3b-9a0e-3b45-a0a8-421aced6f3f1 | -16.92677 | -57.48364 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 8d11def4-8ea1-39a8-bcfd-88c3faaad680 | -16.92628 | -57.48743 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 13.5 |
| 392407ca-511c-36c6-919d-42f1a95c732c | -16.92579 | -57.49122 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 8076ee96-2679-3d96-8e52-323f040da0ad | -16.9248 | -57.68868 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 0a983716-f7d8-3681-95e2-5969f28732c0 | -16.92431 | -57.69236 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 079a3176-eda4-3f52-9009-c9e491c91cc8 | -16.92366 | -57.47549 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 82c614c7-0537-35d2-8975-49bbb041cce2 | -16.92316 | -57.47929 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 617d800c-85c8-33f2-b729-0009bbd2da0e | -16.92267 | -57.48308 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 9ca0b11c-dc23-3fa3-87d8-539bfdf1a962 | -16.92219 | -57.48686 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 01e51f57-87c6-3984-bf20-02f55d9f21b1 | -16.9217 | -57.49065 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 3d0f9be9-b105-3868-a308-c8aec5539d40 | -16.92076 | -57.68811 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.0 |
| 58f56aa9-167a-3635-8558-5666755c750c | -16.91858 | -57.4825 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| a90a68ba-d96a-358e-abae-7bdf68584290 | -16.91809 | -57.48629 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 37f30492-d333-3925-8e44-5032d6e81922 | -16.91267 | -57.68697 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 1.6 |
| 6a902d16-1776-3b56-a79f-395f8e6a9198 | -16.86866 | -57.67699 | 2024-10-08 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.7 |
| 5d8e5407-92e4-3980-b3a5-cae21e9ec56d | -18.87601 | -57.7411 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9b7a75a5-ef1e-3ff9-ba45-b02dc2c3c076 | -18.73116 | -57.29408 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 22c5e601-e01f-3bdb-8cab-ee4c860fe85c | -18.72691 | -57.29351 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.6 |
| c2ffa5ba-3224-34ad-8c87-8c254837fdaf | -18.72627 | -57.2919 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| e9ba0978-031b-3a3c-8b18-6e1de82ceaad | -18.71095 | -57.28291 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| b85d97ac-3005-3274-af3a-db72accffedd | -18.63594 | -57.23131 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 52000c6e-87f1-3a3c-aa70-b1794e8de55f | -18.61147 | -57.25337 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 9dcdda7d-e30c-3735-ad16-a12eef79931d | -18.60616 | -57.2611 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| b1f415a5-64c8-3200-8e5e-d739ec08a8bf | -18.88548 | -57.74943 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| aa827e76-341a-3666-a64c-35e82535d4dd | -18.87551 | -57.74501 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 567cbbcb-ebb3-3913-9865-280525c57830 | -18.62635 | -57.23848 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 264391a5-f603-3b82-a3c9-a5545ee3d455 | -18.62565 | -57.23736 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| e95e22f0-5671-31d5-ace6-cf8145961a88 | -18.61625 | -57.24979 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 3c2cb96c-16d0-3932-86d6-d8c29578cb0b | -18.61041 | -57.26167 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 4f39eda2-2661-3bde-b6e4-47c1b13ebed7 | -18.60989 | -57.26581 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| f0d9762c-0237-309b-b472-0e4d31b05c93 | -18.60669 | -57.25694 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 4.8 |
| a0a3b0c4-4ec3-3bc0-945f-4fa8f1140f46 | -18.885 | -57.75333 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 6e5542b7-a8be-351a-9779-d2a87d2950f0 | -18.88327 | -57.75006 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 727d1074-fbf5-3cf0-8bff-7540981d8f66 | -18.72424 | -57.28049 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.0 |
| d7fa5a58-9e0f-33b9-a171-77a2fdcb39ba | -18.71626 | -57.27518 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.8 |
| d8037214-d45c-3634-935e-1844d4ca5609 | -18.63518 | -57.23019 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 23ebc5f3-71eb-374a-8364-e0f847ecb476 | -18.63468 | -57.23436 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c1b4e0e7-dd4d-304a-a283-8d6304a3a4b7 | -18.63168 | -57.23072 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 0491f7e0-ce01-3058-8015-f2bcafd1eba4 | -18.63115 | -57.23489 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.7 |
| bf347b48-6f22-32c1-ae34-1f350f14a443 | -18.62515 | -57.24153 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 9524394b-0544-35e3-b5a2-bf6bd465649c | -18.61199 | -57.24921 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| b27822f6-ddaa-3e68-a960-fc5ae8be4ab5 | -18.60774 | -57.24863 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |
| 5972489d-93ed-3c26-9fee-983a5c9cd643 | -18.89789 | -57.75116 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.9 |
| 7f279694-f70b-3797-8b67-00bba461c180 | -18.88277 | -57.75397 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 5eb2ebba-ddc1-3079-9ed8-668d69bf0b10 | -18.87187 | -57.74051 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| a6836b8d-6528-31da-ad39-3dcf583d9703 | -18.73053 | -57.29247 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 7a945154-ccdb-30bc-b36e-3d76dada5165 | -18.71999 | -57.27992 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.2 |
| 0caa0c4f-a68d-3452-8283-75ddfc0e35f6 | -18.63945 | -57.23078 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| c806af7d-1028-3de1-8b00-eebe5dd1e089 | -18.63648 | -57.22715 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 084edeb6-4329-3704-8887-732a268a14ca | -18.63614 | -57.29369 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| b1c6c12a-eac3-3e95-9a69-f5338a930886 | -18.63564 | -57.29784 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.9 |
| 9554d78f-1d75-36e2-abd2-669983606971 | -18.61467 | -57.26225 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 61198a15-b626-3204-bd87-41b8241c35f2 | -18.61414 | -57.26639 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.5 |
| 97793605-29db-30ad-b7fb-f7f0072c2578 | -18.61094 | -57.25751 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 5.0 |
| 081655d9-76d2-39b7-a3fd-e96f3a0bcc06 | -18.60721 | -57.25279 | 2024-10-08 05:23:00 | NOAA-20 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 8.4 |


[Clique aqui para ver as próximas entradas](README120.md)
