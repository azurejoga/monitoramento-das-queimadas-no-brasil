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

## Dados Diários - Página 65

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| dc8c009e-f9b4-3e2e-970c-944f01145306 | -3.26838 | -50.20443 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 53143f76-a8ab-3ce8-a63c-0a88577dc00f | -3.14414 | -45.37229 | 2024-12-01 04:44:00 | NPP-375D | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 11.1 |
| 61e336e2-6bf4-3b95-b60a-6dba91235bc9 | -3.01755 | -51.23967 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 54349fa0-8fec-3ad8-b1c4-3fe6e4d4b4ba | -2.41959 | -50.35038 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 94f8e3f8-f7cb-3b74-b7cb-4c256a4a3166 | -4.49629 | -43.60656 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 171693b8-e729-3783-93b2-60d142ee1848 | -3.12584 | -51.794 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO XINGU | PARÁ | Brasil | 1508357 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91c1ee8b-04bd-3efa-80cb-7d8244c231b3 | -3.39598 | -50.3161 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 6042cf6d-556b-3d84-9a15-9c3025046078 | -3.81751 | -52.25345 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| 87fb5640-e327-3bab-9519-77464a0ca977 | -1.18566 | -54.03836 | 2024-12-01 04:44:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cb027724-3ef0-33d0-a762-02bed0499c59 | -3.77335 | -49.98267 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 1300f0fd-44c2-3725-842e-5bc43646ba78 | -3.22543 | -53.63129 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| f2731a42-f96a-3510-b811-33ddbfa1e772 | -4.12384 | -48.84645 | 2024-12-01 04:44:00 | NPP-375D | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8f4523ba-16ad-329f-a831-7b214951449b | -3.44282 | -52.04091 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| dc030d3c-b04f-306e-9808-9ee33760b42e | -1.32016 | -51.7524 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 295ab927-25f2-3f84-9927-54c175e6b11e | -4.76599 | -49.4992 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 84094e9d-7fa2-335d-b050-f3563eae92ce | -3.49497 | -53.80589 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 88191a9c-2fab-328e-aa4f-09f10ca1430b | -3.46496 | -50.26678 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 14.7 |
| cc7b8b68-76de-34cc-99a0-145ac202874f | -3.60034 | -50.37686 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7be5a585-5507-3077-9878-9c9922567227 | -1.44701 | -55.19281 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 48baf04d-1f96-378b-be31-eea3533d6cf4 | -3.85135 | -54.22531 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| f74cd504-887a-3383-9934-8dc4004a4b2d | -1.15289 | -51.70407 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 988d96b3-f8c7-3c60-bd9b-066615d9040d | -3.2135 | -53.12461 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 17.5 |
| b8ea3c32-8336-387d-bb3d-81cb3afda169 | -1.62378 | -53.86245 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7efaa37b-2d1f-3eb3-b69c-8290015e7679 | -2.59223 | -53.98552 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 622f9289-2c56-30e5-a453-3ec527ea987f | -1.07006 | -53.63076 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b549dc08-84b4-33ea-9e7d-ba8b0037987f | -1.99466 | -51.17418 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 64568cc6-95b3-39de-8ad0-78641abdaa68 | -1.56064 | -46.77147 | 2024-12-01 04:44:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bcd1a836-ae81-3060-8f5f-bbbea6fdd77a | -3.58493 | -45.67235 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c23d382f-9db7-3e23-884c-d8648ac02692 | -2.04889 | -54.67214 | 2024-12-01 04:44:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 551232f7-167d-31e0-917c-58f68d9053ae | -3.36182 | -50.51593 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 8b6327af-b538-3d37-9c18-90ed0af5d64f | -4.54728 | -43.29709 | 2024-12-01 04:44:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| d246eb75-8fd1-3642-9388-ac09297a2398 | -3.10021 | -54.04461 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ec3a3a6f-770b-3501-93b8-103f66b788a2 | -1.10279 | -53.59449 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4bb25acf-630e-341a-82ec-bf23face8a58 | -3.69592 | -51.80832 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| 18af0f97-cb72-3549-a465-ef2acc4eed61 | -2.06081 | -51.1918 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77c32513-5233-3d71-ae00-24c98692c290 | -4.00152 | -44.75203 | 2024-12-01 04:44:00 | NPP-375D | BACABAL | MARANHÃO | Brasil | 2101202 | 21 | 33 | nan | nan | nan | Amazônia | 29.1 |
| 698321bd-201a-38e1-803e-698be157dfa8 | -2.63156 | -46.19785 | 2024-12-01 04:44:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| bad36260-f0b5-3bb2-8dc1-1740de0df097 | -1.00485 | -51.73087 | 2024-12-01 04:44:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 4.5 |
| a297aee3-dc6b-30dc-aba6-25c9c7475364 | -3.04859 | -52.75773 | 2024-12-01 04:44:00 | NPP-375D | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6d745822-9ecb-3af7-84c5-6acc621e2b05 | -2.92238 | -54.26316 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 44b82322-9371-3c60-a090-db85021c43fa | -4.07134 | -46.8204 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9d866baf-aa4c-339b-b9a4-c8aecfc80195 | -3.02683 | -54.02132 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6211bd1f-4617-3c2e-889c-fc8387990e9a | -3.26438 | -53.64618 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 63ae5307-34da-3d95-9b21-db92601ee461 | -2.60624 | -51.81026 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 581f8e5b-d70c-3b38-91c5-e3a15fe5f678 | -3.23688 | -46.42612 | 2024-12-01 04:44:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 5656af74-e63f-33c9-904f-4a65790c1436 | -3.10397 | -54.04517 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 6bf0eb04-4286-3dc0-917e-a1725eec7d59 | -2.86755 | -53.97874 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 25c9f82a-cab2-384c-a1ff-043eca763d49 | -3.33335 | -50.22168 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b1de9343-b083-3863-8173-aefe822e3a1d | -3.25774 | -53.64071 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| fa0e92ce-d743-3414-a209-686cfdd9a5f0 | -1.67053 | -52.09731 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 19a64232-b81d-3b24-8461-e032cbaa8574 | -2.37409 | -50.38213 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 5c44a4d0-b73a-3801-97ed-2c135cd3536c | -1.43783 | -52.77194 | 2024-12-01 04:44:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 4.9 |
| 6ff26aee-f56b-39e6-a10a-5436d9b37b88 | -1.19856 | -51.74924 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 9667a029-72fd-3fbd-b70d-af344f434792 | -3.67167 | -50.24291 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 62340654-2e54-3ab0-831f-d7682ffc7bb8 | -3.49209 | -53.82343 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a187f2bd-5ace-346c-9eef-d767766b5b96 | -1.99547 | -52.09656 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| b7fc2e81-8bcd-3a3d-ae96-10d92a5fad20 | -3.73252 | -51.31503 | 2024-12-01 04:44:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0134edd5-7889-3f6a-bf86-7520a848bdaa | -2.80036 | -54.13099 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a2b34e26-b2d5-361b-8776-a23e0ce3a476 | -3.47786 | -59.46402 | 2024-12-01 04:44:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 85350e0a-bd2b-34ef-8890-e45ebe6f5aa0 | -3.17611 | -53.6384 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2661955f-e05c-3a74-a232-585163cd0276 | -3.1899 | -54.51518 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cd624d47-23ea-3e97-bcc9-9c5458e8ef7e | -3.03491 | -54.04332 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 2354b994-322a-396e-bf5f-0a924553a2a3 | -3.48529 | -52.10355 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e88d0fe0-6512-34db-bcb5-189dfd644f5a | -2.31877 | -50.6465 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f281169f-ee39-3f99-aee8-17b4e84431df | -3.52705 | -50.47501 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.4 |
| ac8b0360-17b5-3c8f-acf5-127d9e4dd9da | -3.30475 | -54.16603 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5f034629-5851-33aa-87fc-3b0d6c4629c4 | -3.05769 | -53.65718 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| b5a5bd9f-1447-3400-969e-92f177c3eb7b | -2.76849 | -55.34483 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 62655e36-d52e-3e75-a984-2b02a6ffcfcf | -3.42133 | -54.64092 | 2024-12-01 04:44:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| eaf5fb36-2670-383c-a003-af0b10a3c65c | -4.33735 | -50.76463 | 2024-12-01 04:44:00 | NPP-375D | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 002011c6-b56b-324d-8596-4c29006f21d3 | -2.26511 | -50.76991 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 93fb0a8b-fda3-37d4-a66d-cfbf1987881e | -3.26397 | -50.2108 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 19a5f40b-580e-3169-bba8-3cbb595f9a5e | -3.75137 | -50.06071 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 9a97c8f9-459d-36a0-8b30-287a97e41c65 | -2.61589 | -51.81553 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 94256370-777c-3ff5-b337-b8f277a4815d | -2.37644 | -50.43203 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 44a168d4-4a3d-3323-8401-bb60f8bf77f5 | -1.70239 | -52.46846 | 2024-12-01 04:44:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| ced84189-5b5a-3bed-be08-991f8a1b4086 | -1.24199 | -51.80114 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 57870de1-6e55-30af-8f07-884a46bfd17c | -2.59209 | -53.98797 | 2024-12-01 04:44:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 54ecb1b2-9f00-3db6-b122-44a4d1bac471 | -1.28011 | -51.73852 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b9d6bd19-38c7-31a9-90be-827d5082d4ac | -2.81763 | -53.05358 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5e701224-3337-372c-9809-ea6f92094648 | -2.58942 | -46.94132 | 2024-12-01 04:44:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c7ffd3d1-898e-3a76-b942-7217bb0eb994 | -5.25204 | -49.93822 | 2024-12-01 04:44:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| efafda54-886a-3ce0-9656-a6863ef43af2 | -1.23914 | -51.79688 | 2024-12-01 04:44:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 8f2b6af7-7202-3455-a5d2-8b53b801591a | -3.30397 | -53.8365 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| ce8ac554-9272-37a2-b4fa-824149f8ff08 | -3.38702 | -49.85848 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 9ccab88a-a301-3c86-9aa5-bee616802e99 | -2.90193 | -51.77432 | 2024-12-01 04:44:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f5cf07e8-7c62-3ebd-86e0-8e896b1d8b0f | -2.6293 | -54.21335 | 2024-12-01 04:44:00 | NPP-375D | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1a792a68-918b-366e-aec3-2a55871b65bf | -3.11343 | -54.2739 | 2024-12-01 04:44:00 | NPP-375D | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d58b366d-f6d4-34a6-aa50-1a7a9aedb2b6 | -3.78642 | -52.40481 | 2024-12-01 04:44:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| cdb835ec-f99a-3c4a-ab70-4a87769a4fc7 | -3.30421 | -50.27721 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6da0f478-1f73-3134-a0fe-ca4ef57b5642 | -3.58983 | -50.37876 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 739f7248-a0ea-3168-ae8e-1bff438b0ac8 | -3.35569 | -49.75775 | 2024-12-01 04:44:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 516eff3a-e360-3964-9de0-146f89711e21 | -2.4302 | -50.39093 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 75805abd-041f-3e00-a3d9-f0dfeb8680f0 | -4.31799 | -48.0859 | 2024-12-01 04:44:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d5659664-db03-3cd6-b00a-46252fc7f70b | -3.42633 | -53.89074 | 2024-12-01 04:44:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a0c537ca-4ce6-3b99-960e-1fac1c98e8aa | -3.86811 | -51.01398 | 2024-12-01 04:44:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| bb080cd7-f0ad-324a-96bf-6a36f0f35b6d | -2.37741 | -50.38265 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 1b4f7ddb-f610-3d98-85b1-6df080d84100 | -4.03684 | -46.53708 | 2024-12-01 04:44:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 7b494bfe-6389-3c90-9699-847771e01fb2 | -2.98378 | -53.34628 | 2024-12-01 04:44:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| a20e6e7c-e639-39ac-a267-f374e2c6d4c9 | -3.3739 | -50.82253 | 2024-12-01 04:44:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |


[Clique aqui para ver as próximas entradas](README66.md)
