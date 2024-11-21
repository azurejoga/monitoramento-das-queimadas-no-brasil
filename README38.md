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

## Dados Diários - Página 38

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| d0c046c0-ffb2-34ff-840e-c7d065a7d743 | -3.71981 | -49.42776 | 2024-11-21 04:29:00 | NPP-375D | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| e8781562-7096-3a85-afe7-01a90f249181 | -2.64004 | -46.2066 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 07ff8dde-1d3d-3225-92aa-a35e6e3d0923 | -2.69112 | -46.24651 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 7fb14b71-f4c0-3cf7-8d50-76ec19d7ce73 | -2.30359 | -49.00558 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 576d4068-775c-3cf9-a31c-e4aaff605191 | -2.68501 | -46.24201 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 86245321-7ad5-331d-ba8b-648ae8a7b84d | -1.09703 | -51.74445 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 998504b1-6b71-3eab-ae19-6ed387a147ee | -1.13192 | -51.68308 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac32e845-2681-328b-a9df-c6c71f1df151 | -2.57953 | -46.54818 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| f854f22e-06c4-3048-bd94-a456a19d7c48 | -1.1147 | -48.35372 | 2024-11-21 04:29:00 | NPP-375D | BELÉM | PARÁ | Brasil | 1501402 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 19b10dd4-99ad-36ce-a180-65b7181b3606 | -2.63299 | -46.05566 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 83312249-5041-314f-b027-2efd4bd86404 | -3.34608 | -46.62576 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3504178b-8152-3ad5-a061-a136a793ca4b | -2.71888 | -49.34414 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| edab30f7-0ba8-34a0-aae4-0fc96cee6488 | -3.79304 | -46.94318 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c5a2ab97-1bec-3ed3-b35a-e99e157b093e | -1.46677 | -55.45202 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| fdc5827c-458f-38ee-8535-10f755d7d4b1 | -3.08846 | -49.47126 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 025fd694-e900-35a2-841f-0fe03c47f896 | -3.08501 | -45.97854 | 2024-11-21 04:29:00 | NPP-375D | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f362d7ae-6d19-3632-b2ad-c97c89053230 | -1.53394 | -52.22672 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dbce52e3-1b2b-3ab2-b7c7-060a8e57ecab | -3.36018 | -49.50814 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 1fb524a7-40ef-37b9-84cd-b96884cc1198 | -2.38596 | -48.9214 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| d3903847-2f01-3655-88e6-cf6015a54fbd | -1.62216 | -52.5929 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 4.5 |
| dcc1fe13-bab6-3ca6-8a9b-a19f5d0a71bc | -2.69033 | -46.08241 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48e29183-a833-3a01-a082-655c27e31fd6 | -2.16588 | -51.96783 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| bd4f2921-3050-3ab7-a2c2-6a64bee240b3 | -1.37448 | -46.50849 | 2024-11-21 04:29:00 | NPP-375D | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | 0.4 |
| 5e0dcd5e-8122-30b0-b121-fb2f2a11acdd | -1.49928 | -54.71253 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 58d055e8-6434-3f7d-8f48-9bab4011894e | -1.11978 | -53.39661 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 7.0 |
| e97dc6fe-6179-3cef-98f9-d0ec5064f735 | -2.55871 | -46.0586 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 78852b1e-5d9b-3181-b32f-038f40845e20 | -2.53632 | -46.22268 | 2024-11-21 04:29:00 | NPP-375D | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| a42cc43e-c8eb-3d7b-8df0-98ebe4f753de | -1.55914 | -51.23199 | 2024-11-21 04:29:00 | NPP-375D | MELGAÇO | PARÁ | Brasil | 1504505 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 0ad229b7-d49f-3f2e-b59e-38710d896c5b | -2.72618 | -46.08795 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 56686eae-8ea1-3fa0-8842-2d7ad628c486 | -2.57899 | -46.55163 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 63f0ceca-3e42-3edb-aedc-16d8cf2f8a92 | -1.25412 | -51.78029 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2721845-3dfe-3803-acec-a2840a10f81c | -2.60871 | -48.24871 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 9a14b3e9-1d0a-3cb5-ab51-4f90a39ab7c9 | -2.695 | -46.24355 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| d576f701-3926-37ad-bf59-3a7c5c309298 | -4.18413 | -43.93806 | 2024-11-21 04:29:00 | NPP-375D | TIMBIRAS | MARANHÃO | Brasil | 2112100 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f23ec093-d593-33e2-bfb5-650f03e2602c | -3.74496 | -47.35643 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f3b5dd4-e321-386d-b2a0-43fa096b5505 | -2.93008 | -48.33488 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 313328ec-1638-373f-b4d5-26a36484a7e2 | 0.40485 | -50.79891 | 2024-11-21 04:29:00 | NPP-375D | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 47d98f5b-bf41-352d-a5de-147af22f92ef | -2.71537 | -49.34359 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| a07bc19e-9247-3b46-821c-1e2090e63154 | -2.64567 | -46.23594 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| f087bbe9-d7bf-3221-bc41-ba846eb69233 | -2.91232 | -53.06317 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 449b7bfd-b054-372c-9636-a8f1fa9f3774 | -3.28809 | -50.53641 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 0b5035e9-ee1a-3182-a606-dd73e8df8c6d | -3.02822 | -51.52696 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b53bab87-90f5-349c-8da8-bf60385f7cac | -2.62966 | -46.05513 | 2024-11-21 04:29:00 | NPP-375D | MARANHÃOZINHO | MARANHÃO | Brasil | 2106375 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 660524fc-f16d-3aaf-be2a-998017a3dc9d | -1.26973 | -52.12299 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 9f1d3cfc-b5fb-397a-bd84-df4cf62d30e7 | -3.37116 | -50.72583 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 9a5f666c-0d86-335a-b56d-41fca987ea85 | -3.3992 | -49.78521 | 2024-11-21 04:29:00 | NPP-375D | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 8563773e-6e6c-35cc-bbae-9694799aab2e | -2.82602 | -54.02421 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 42f38690-410c-32db-9c77-83cf79f8cdf9 | -2.51573 | -45.61981 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA DO PARUÁ | MARANHÃO | Brasil | 2110039 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| cc011037-19c4-36c4-afc1-cae05164b4e2 | -3.81068 | -47.79993 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| e25b00ca-281f-3cec-98b7-77916350c219 | -2.26459 | -50.44827 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| cbfba210-33c7-3b82-997c-4a5eec7f5d9d | -2.68725 | -46.24947 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b757484e-5707-350d-9931-1b08bcb27f89 | -3.80735 | -47.7994 | 2024-11-21 04:29:00 | NPP-375D | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 4.7 |
| c15cc345-639e-349e-928c-9bd668cad1c2 | -2.67776 | -47.4729 | 2024-11-21 04:29:00 | NPP-375D | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 9ad09c37-0642-3ff7-8333-6cf489b6d870 | -2.08309 | -48.94117 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2ccbebae-d0e0-3c39-b752-e14a6393a37d | -1.60589 | -52.47454 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| cfad5d82-0411-3695-8d42-5f64a3812fc5 | -2.58378 | -51.92341 | 2024-11-21 04:29:00 | NPP-375D | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1bf36c90-fdc7-3981-ace1-e5942c1f2904 | -3.49587 | -48.22618 | 2024-11-21 04:29:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ed196500-4c52-3c63-ac08-a311a8de714f | -0.92721 | -51.63947 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 648a01c0-8c75-37a2-97d2-3c796f3b2fa3 | -3.28913 | -49.19056 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 7ec57c5a-f7eb-3906-bbd5-53809157534e | -3.06521 | -51.36792 | 2024-11-21 04:29:00 | NPP-375D | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f9478d5a-098b-3bcd-b57e-6d5835653d00 | -3.79026 | -46.93922 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a8cda0d1-8206-3818-ad36-3b8f1bab0ef3 | -1.3925 | -55.18084 | 2024-11-21 04:29:00 | NPP-375D | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d1c2ab40-9f11-34b5-a599-1c9ad02467cd | -3.32834 | -50.25739 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 73810c93-551d-3f80-96d5-ad2bbb98f8b7 | -1.96481 | -46.30392 | 2024-11-21 04:29:00 | NPP-375D | CACHOEIRA DO PIRIÁ | PARÁ | Brasil | 1501956 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| a23807d8-3671-3dc9-b24c-17575ad7758f | -2.62289 | -48.1812 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0f257ddc-0be7-3a45-9a4e-f43552ae6135 | -1.2478 | -51.78226 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dc3a632d-328a-3cd5-966d-17fff9b9138c | -0.95097 | -51.72117 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b591d65-63a6-35c3-9a3c-b7c95d81612f | -3.89335 | -46.60808 | 2024-11-21 04:29:00 | NPP-375D | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c288b381-eaa2-324a-9c25-65c09a77f3e3 | -1.5268 | -55.37992 | 2024-11-21 04:29:00 | NPP-375D | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7bdc1a49-a65a-38da-bfd7-7605c6781689 | -2.69547 | -46.21872 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 60e7ebe0-a5c6-3f20-bf02-5579947606bd | -3.54588 | -50.41308 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 58522cfb-97aa-3742-ad2a-aba8b4b0b82d | -2.13895 | -48.56688 | 2024-11-21 04:29:00 | NPP-375D | ACARÁ | PARÁ | Brasil | 1500206 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 74bcfc70-2040-3e8d-b7f5-06b935e844ec | -0.90121 | -51.72482 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 2467f41b-3571-33fc-a702-9096810ab346 | -1.47958 | -54.44936 | 2024-11-21 04:29:00 | NPP-375D | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bf554209-62ab-3dce-9dce-66037d5594b6 | -2.57546 | -48.21064 | 2024-11-21 04:29:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 5445db43-765a-3a6e-9d03-a2014588c1cf | -2.13819 | -53.64035 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| a82ded8e-9494-3793-9ff8-4b0106f77e84 | -3.09494 | -53.21053 | 2024-11-21 04:29:00 | NPP-375D | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 2e1c4071-9a82-398d-9a1c-d4691ac7f0f5 | -0.9586 | -51.72613 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 147e2971-9d06-3e02-b4ab-7a02d0a5a56b | -1.6501 | -52.66872 | 2024-11-21 04:29:00 | NPP-375D | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 7b7c5719-661d-317c-b1cc-9683eeceac49 | -1.2126 | -53.69385 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b6ea07f4-64f7-34fb-a0ae-10e0356a26e5 | -3.48716 | -50.31395 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 207c0aa9-6696-391f-a7ad-35bbab427d2b | -0.81146 | -52.49356 | 2024-11-21 04:29:00 | NPP-375D | LARANJAL DO JARI | AMAPÁ | Brasil | 1600279 | 16 | 33 | nan | nan | nan | Amazônia | 2.6 |
| cca1912b-efea-3634-8438-6102ec85f43e | -2.13936 | -53.77687 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 64be3cd9-e887-3aaf-8282-f2c15506e289 | -3.37624 | -50.28502 | 2024-11-21 04:29:00 | NPP-375D | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 20380a86-bd45-3131-aa7c-c11d38c51757 | -3.21981 | -50.58356 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 5342cf1c-01c8-35b6-8316-5b576369e233 | -2.77946 | -51.71827 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 296cabc7-292d-3e35-a509-20bf1e09fe42 | -2.66221 | -48.48234 | 2024-11-21 04:29:00 | NPP-375D | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d156e7ed-434b-386c-93db-1de27a15e9dc | -1.33429 | -51.40289 | 2024-11-21 04:29:00 | NPP-375D | GURUPÁ | PARÁ | Brasil | 1503101 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d5b70ea3-fcc8-3558-bf16-c36562abe0c5 | -2.95759 | -49.54386 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 33b50098-ef01-3800-a0cb-14c728e6428e | -2.28336 | -48.9985 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 66aca428-d1bf-3e15-8be1-da150fb50a9c | -2.6473 | -46.56937 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 93341541-12e4-3b94-865e-3a70c74d9a34 | -2.88723 | -50.42387 | 2024-11-21 04:29:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 86ae0bc8-e5d6-34f4-86f6-09ff180c68b9 | -4.24615 | -46.10293 | 2024-11-21 04:29:00 | NPP-375D | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 27844332-491a-344c-9e0f-677f22410caa | -4.15864 | -42.01809 | 2024-11-21 04:29:00 | NPP-375D | BATALHA | PIAUÍ | Brasil | 2201507 | 22 | 33 | nan | nan | nan | Caatinga | 14.9 |
| 3a81c3b3-d57c-3512-95bf-66b8216e08d9 | -0.25689 | -51.76239 | 2024-11-21 04:29:00 | NPP-375D | MAZAGÃO | AMAPÁ | Brasil | 1600402 | 16 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 54f80f19-6428-332a-8b7e-e4c59adaead5 | -3.18509 | -46.50446 | 2024-11-21 04:29:00 | NPP-375D | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 724fb105-5cf8-3eac-b1da-e1f6f96865d7 | -0.88006 | -51.72522 | 2024-11-21 04:29:00 | NPP-375D | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 80d09df8-ffb7-3acf-8fcb-539156978789 | -2.31303 | -49.08134 | 2024-11-21 04:29:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c2cf1cce-0aa3-3bae-80cd-9e06ec09383f | -2.83302 | -54.01037 | 2024-11-21 04:29:00 | NPP-375D | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 7ee8723b-fade-3395-8fcc-85b93ca38b72 | -1.29235 | -52.22484 | 2024-11-21 04:29:00 | NPP-375D | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |


[Clique aqui para ver as próximas entradas](README39.md)
