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

## Dados Diários - Página 58

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 6a1cf83f-46cb-3607-abfa-4a5653297b1e | -3.91118 | -46.53268 | 2024-11-23 05:12:00 | NOAA-21 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 86deb45b-bd85-37a9-b6f6-1583866be099 | -3.29069 | -53.68401 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 23e60efd-29a1-3e3b-b13b-cdf62190521e | -2.82004 | -54.03262 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 7f96e114-e84f-34b3-b312-df6396a72e2c | -3.98287 | -53.64049 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 94752c35-7a10-3db7-9a50-451dce169121 | -4.10414 | -47.80607 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3a757051-d7b6-39e4-b9c6-755f6d0dd337 | -4.25623 | -48.70314 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 8.5 |
| 3af3b083-587b-34b2-8b73-a36e7ed6850d | -3.24071 | -54.24347 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| d9b9b957-3364-3f4f-80d6-18bd25588b7c | -3.21358 | -51.41959 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9a41635b-a7cc-3a96-8705-9aa1fb5e83e2 | -3.30679 | -54.18869 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c88b21d7-3c0c-39cc-bdec-efef7bf10aa2 | -4.37049 | -47.8286 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 05063efe-bb3f-3da4-8bb7-0e188ccf5cbd | -3.81206 | -52.00543 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| e7e2eac8-669e-368e-b3a2-381dd04c05a5 | -2.82362 | -54.00994 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 0e286ca4-61cb-3a21-9e13-19f758990b15 | -3.06314 | -53.28645 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 4073ca38-91a5-34dc-a334-d23801beea31 | -4.17925 | -48.63609 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0d03b6b9-1c7a-3dd3-8e9b-a7e4b94fb2e3 | -3.29363 | -54.72743 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6cef679a-4836-3b4d-b7ab-df8da3c4b7fc | -4.72875 | -45.49729 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d63e3797-878e-347e-a2e3-5fd8b82781de | -3.04329 | -54.85066 | 2024-11-23 05:12:00 | NOAA-21 | BELTERRA | PARÁ | Brasil | 1501451 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a747a6be-b348-340b-9c55-e006e7726abb | -3.68121 | -50.11563 | 2024-11-23 05:12:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 8056980b-80ea-3317-8496-859a61b11050 | -3.2133 | -54.01974 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 5068f1e9-169a-3a2b-a066-8cdff3f0035a | -6.14596 | -46.687 | 2024-11-23 05:12:00 | NOAA-21 | LAJEADO NOVO | MARANHÃO | Brasil | 2105989 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| b51b31be-3e5b-3726-8939-06093dce3c66 | -3.2696 | -53.82047 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| d5feb7f8-3f5f-3e69-9d13-e6cb9b178f30 | -2.94557 | -54.30075 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 8575f163-be18-3931-ad5d-772800e282cb | -3.52719 | -52.90368 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f4967ce6-c739-3c4e-975d-a754f4453a8d | -3.503 | -53.81191 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 9e2587a0-3dec-30c8-8b14-2b5d69342088 | -3.24189 | -54.23564 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| 25dab721-243a-3998-a5c7-af9e08d6f718 | -3.31745 | -53.28996 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 2157a041-c4cc-3798-b94b-eebb7cc902a8 | -4.10367 | -47.80933 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a0d382e1-0e89-37ba-b31e-1ca80a5c1216 | -3.23015 | -54.24182 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| d4676fe7-a9e7-34f0-b224-f5ee6503ee96 | -3.50363 | -53.80781 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 3026d244-7f37-3bfa-a1f6-d53f361d7315 | -3.57469 | -51.55938 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 77933941-5acd-3bec-9c32-615b087d6620 | -3.21367 | -54.25165 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f642eca2-0607-3e04-bbdd-078dffd8054c | -3.12141 | -53.10163 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 6.0 |
| dcab7adc-837e-3d30-b941-70a7fdad9831 | -3.1805 | -54.3266 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 25cebce4-baf8-3a7a-b342-527287c6c2a7 | -4.70606 | -45.84735 | 2024-11-23 05:12:00 | NOAA-21 | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| c09c86d6-e48c-31ff-a981-58d82d6d7b3a | -3.94695 | -47.96449 | 2024-11-23 05:12:00 | NOAA-21 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7e48f693-c474-3d92-a6c3-58eb01ef6d6a | -6.50164 | -47.04729 | 2024-11-23 05:12:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 8e650ec6-2f23-35ea-aeae-c302a1c0324d | -3.70166 | -51.7956 | 2024-11-23 05:12:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| 76fca28f-12d5-3ad2-b301-50f978c20892 | -4.45063 | -48.19839 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 1b570fd3-d360-38e8-ba2f-c89dd6cffdb0 | -3.25485 | -54.22149 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d90c1baa-011d-3ff2-8283-4b7ec5583642 | -4.41601 | -44.11101 | 2024-11-23 05:12:00 | NOAA-21 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50977c1c-2d7c-36e7-a3c7-2661e0c216cd | -3.25361 | -53.2691 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 5.1 |
| 09892840-f488-3f0f-a3bc-36b7d6a3b352 | -3.28707 | -53.68347 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 2f01321f-9255-3181-b3f6-59e2980da016 | -3.67431 | -54.27346 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 8fb232a0-11ea-347d-bbf2-ffd2784d51fe | -3.2313 | -54.258 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9bb74d52-75b7-3cc8-be05-c5943e01a4c4 | -3.25185 | -54.24124 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| b88bbcf0-1aa8-3794-b64a-1e79cc602ba7 | -2.80406 | -54.0192 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 0ecc6624-4cff-34d2-83dd-75aba88e1139 | -3.25537 | -54.24179 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 40417eca-5c61-3e52-8f48-eaf18545dbad | -3.27677 | -53.82164 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f26f30c5-7aa1-3ab4-be6f-947aeba0390b | -4.61513 | -46.49994 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 21.3 |
| a77824e1-fe08-3c47-8513-04e61b94f11d | -4.54461 | -45.88282 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 235e364f-9e69-3eaf-b037-881db0208b60 | -3.22313 | -54.23716 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a2923c4c-1640-3312-84fe-e9fe35a62c7f | -3.06431 | -53.22829 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 91ea7b7b-1cb1-3fd0-ad0b-35012d338203 | -3.21773 | -51.42019 | 2024-11-23 05:12:00 | NOAA-21 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 85fc64f9-457c-386e-8fab-451a68ee9e52 | -4.21768 | -46.16087 | 2024-11-23 05:12:00 | NOAA-21 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ba63b445-7634-386e-840f-283e942bdb41 | -5.57256 | -46.28902 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 9ff1592c-dc0a-3ccc-9cdb-d45827af3cdf | -2.8076 | -54.01975 | 2024-11-23 05:12:00 | NOAA-21 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 3308acf0-5c85-3fcd-9068-fd8d88f2aaf5 | -4.16379 | -54.58141 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| e0867e25-2c20-33be-b8be-9c91dc995ae1 | -4.1995 | -53.49854 | 2024-11-23 05:12:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| db949362-ac15-3255-b49c-75d56f34ea8e | -3.26537 | -53.82409 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 95f9b428-1012-3ed7-8e69-58de7afa2266 | -3.27987 | -53.83833 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4c9c5614-90eb-39e1-bf25-3ab9d36ebc59 | -3.26831 | -53.82879 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a0c59acc-cce3-346b-b579-2fb0beec91ca | -3.65814 | -54.4277 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 044d61ff-5bbe-348c-889c-c29d32d6445c | -4.02821 | -48.87007 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| b6f537ac-41dc-3874-8e41-e3da504b1370 | -3.43187 | -54.53333 | 2024-11-23 05:12:00 | NOAA-21 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 82eeac00-ede3-3506-b392-7352afeeae75 | -4.61387 | -46.50895 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| e4523938-2bc1-34bc-9a6a-4859471cb1b5 | -5.01136 | -45.50435 | 2024-11-23 05:12:00 | NOAA-21 | LAGOA GRANDE DO MARANHÃO | MARANHÃO | Brasil | 2105963 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1e49ae8d-5479-38a3-b4c3-4285b6e4e840 | -2.8951 | -54.01564 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| c1b03dd1-4e12-3993-bf8b-6f39503aa3bb | -3.29597 | -53.85344 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5480defb-94fc-3712-9d36-85aa8e2c333c | -4.27193 | -46.29568 | 2024-11-23 05:12:00 | NOAA-21 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 6f23dda7-4dd2-37e7-9bfc-acab4e119f23 | -4.45258 | -48.1852 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 76c9f17f-f5db-3f04-a3f2-8809e8114bb4 | -4.25925 | -48.6946 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 6ef41292-78bd-3ee7-9699-327a1d7902b5 | -3.10388 | -54.00051 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| fbed0530-ba78-3d76-afd1-7ed7d911735b | -5.5841 | -45.20412 | 2024-11-23 05:12:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 15185be5-8421-3d3e-9523-86d79ab65fe8 | -3.2847 | -53.83066 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a09e1f93-3630-3a99-9c55-1d194aa04e49 | -3.32502 | -54.09391 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3d937a06-7b9a-3827-b32a-fbb62e24174b | -3.12074 | -53.10605 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| d7670b43-d3ad-3c81-a12c-5881fff61e37 | -4.27775 | -48.60498 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 4b6e7264-4064-36fb-8211-97f7f56be50c | -3.24423 | -54.24401 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c168b230-4bcf-34da-9f8f-fb5b83d6539b | -5.11561 | -45.83672 | 2024-11-23 05:12:00 | NOAA-21 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 38fa3b7d-c3f1-3dde-8cb6-66c9b9306d70 | -3.22929 | -53.93933 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.8 |
| 7c5e54b3-96f8-37de-a312-0ab0c50f98d7 | -4.44332 | -49.83727 | 2024-11-23 05:12:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b7c797b5-26aa-39b5-aac0-940535c4060f | -3.97655 | -49.01192 | 2024-11-23 05:12:00 | NOAA-21 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| ccbba377-4697-304f-a485-59f7fe802a61 | -4.23669 | -48.63547 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9f1cb752-cc0d-353d-a3cf-0213a6be8a37 | -4.25416 | -48.69384 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 20.5 |
| 4994bbf6-6e58-3256-9d11-351cd5edec3d | -3.32182 | -53.28616 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 5ea635da-df71-3b83-845e-c7ab64dc46de | -3.22131 | -54.24883 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 93f6ca56-87f9-3801-847a-35318a164cfe | -3.21075 | -54.24726 | 2024-11-23 05:12:00 | NOAA-21 | SANTARÉM | PARÁ | Brasil | 1506807 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 74d3fe20-46da-377b-96f2-058fefb5bcd5 | -3.32115 | -53.29053 | 2024-11-23 05:12:00 | NOAA-21 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| cdec4d82-aabf-3f0d-b236-218ad1860394 | -3.1881 | -54.32381 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 407f4ef3-739d-3465-960e-cca1f47af611 | -7.07556 | -49.20895 | 2024-11-23 05:12:00 | NOAA-21 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| f6f2fc01-8aaa-398c-935c-66fc34b452b3 | -4.27264 | -48.60416 | 2024-11-23 05:12:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d5f0822-5408-321b-9e18-32becc5937d7 | -3.27383 | -53.81692 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| faf84977-dcf2-3aca-99bb-e57455eba225 | -3.52472 | -53.80064 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| a9905645-7419-3d91-b9a1-3c43124f04f1 | -4.61449 | -46.50454 | 2024-11-23 05:12:00 | NOAA-21 | BOM JESUS DAS SELVAS | MARANHÃO | Brasil | 2102036 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| bf605c7d-501b-3d23-a607-f62b4dc8367d | -2.96901 | -53.88615 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 77390c62-1100-3463-bae5-c7e6f86a05f8 | -3.198 | -54.32937 | 2024-11-23 05:12:00 | NOAA-21 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 148376e3-cb3a-3665-a5c4-025eaad0770d | -5.97065 | -46.30806 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 059241eb-c790-3fc7-b514-13d6e3494c6e | -3.90283 | -47.94252 | 2024-11-23 05:12:00 | NOAA-21 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 2e9afa80-4a08-33d3-ae31-bed166b4c1f7 | -3.28433 | -53.84398 | 2024-11-23 05:12:00 | NOAA-21 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b09673f5-2a70-3c41-84fe-0d4e49e2f259 | -5.744 | -46.26659 | 2024-11-23 05:12:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |


[Clique aqui para ver as próximas entradas](README59.md)
