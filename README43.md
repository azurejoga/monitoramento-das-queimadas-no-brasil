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

## Dados Diários - Página 43

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| cc083e25-7e2e-3c6f-8440-547180b06938 | -9.14074 | -47.76155 | 2025-11-15 04:25:00 | NOAA-20 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fa286a79-1b77-342c-af68-d34304a863c5 | -4.7031 | -40.12627 | 2025-11-15 04:25:00 | NOAA-20 | CATUNDA | CEARÁ | Brasil | 2303659 | 23 | 33 | nan | nan | nan | Caatinga | 3.1 |
| ef7d668a-c674-35be-a745-7f05bbf3f52e | -8.90158 | -47.89687 | 2025-11-15 04:25:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 63b1faa8-3baf-3a3b-8421-6cc7b0c80ba3 | -9.66035 | -45.3693 | 2025-11-15 04:25:00 | NOAA-20 | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 500ee6d6-7d6b-3faf-befd-74431d50d5d9 | -3.26774 | -43.61515 | 2025-11-15 04:25:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| f1c70bd7-a559-3be9-a966-c0258c608f8d | -6.11235 | -44.22672 | 2025-11-15 04:25:00 | NOAA-20 | COLINAS | MARANHÃO | Brasil | 2103505 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| a84632f3-d3a1-319c-863c-2d1691908ad9 | -7.6359 | -47.52213 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO OURO | TOCANTINS | Brasil | 1703073 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9297900a-04c3-3dbb-b6b9-13f66ce0a847 | -4.30327 | -45.8883 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 1686c4a2-6b72-3609-8a51-2f2d22ec2962 | -4.38531 | -50.43251 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.3 |
| c8de2873-83e4-3dd7-ae76-a6c5dc3b52d4 | -3.12677 | -45.18193 | 2025-11-15 04:25:00 | NOAA-20 | VIANA | MARANHÃO | Brasil | 2112803 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 80fece90-72db-30c1-9f6e-6e8ad0fcf37f | -7.5342 | -47.20041 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c78fa2f9-d30e-3d21-9ea8-bc706f30b7f5 | -8.74555 | -44.23652 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 3.5 |
| cebbeaa8-4864-3ca2-b033-4a8bfbe1539f | -4.75592 | -48.83439 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6fd4d867-936d-32ec-bc04-0d541dd631d2 | -2.73358 | -45.30672 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a13ea958-996d-3374-9891-158b1351e9d9 | -4.00038 | -47.6815 | 2025-11-15 04:25:00 | NOAA-20 | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 4aa082f2-2c6d-3479-ba4e-846fa2b4fba7 | -8.1553 | -43.81072 | 2025-11-15 04:25:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| a92bcd74-3528-34ff-a756-6c94aa83c67c | -6.66089 | -43.77179 | 2025-11-15 04:25:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6cedf80f-0273-3de2-9649-5301140cae35 | -5.8864 | -42.26855 | 2025-11-15 04:25:00 | NOAA-20 | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 26e9742e-2164-3acd-afe6-126e3c705a35 | -4.4633 | -45.64953 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 1.9 |
| dc504f27-b798-31b4-b1b7-f5e73f385040 | -7.23003 | -46.26715 | 2025-11-15 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 293662d6-a45e-37a8-bc34-b4cc01cdc834 | -2.01345 | -53.00322 | 2025-11-15 04:25:00 | NOAA-20 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| dad7ebab-0183-3959-9e45-2bc1d75ecf0d | -3.59459 | -54.67936 | 2025-11-15 04:25:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| bc121cd2-e2a4-3fd8-8453-bea5da453a47 | -4.31239 | -45.55143 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 2.2 |
| aa373efe-c533-3d3d-8e8b-55418aff91f9 | -3.2835 | -53.82008 | 2025-11-15 04:25:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| f711d43d-dc78-3efb-9cc3-4c5fac1dd335 | -6.28139 | -41.73109 | 2025-11-15 04:25:00 | NOAA-20 | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 3.9 |
| 9bda47c0-d24a-3ce4-979f-8ce33206babd | -9.15219 | -45.16428 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 7b34a9e2-5496-397e-a0a5-8a4e3514d8c2 | -7.71027 | -49.3881 | 2025-11-15 04:25:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 324f6079-0661-3ba1-903d-674c62ba89f6 | -4.44176 | -46.36596 | 2025-11-15 04:25:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 5ad0d9ca-a190-3fbc-9d98-0b4b78f243bc | -5.22702 | -44.35381 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 58ed15db-584f-3108-a60e-57d238ae4df1 | -9.72525 | -46.34068 | 2025-11-15 04:25:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e74a72e6-7153-30e2-975d-0358a791f93a | -1.33889 | -54.61223 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f8479801-7e74-3b44-b07b-9c12111ecef0 | -3.7877 | -43.37652 | 2025-11-15 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| aabe5dd5-e8f5-327d-bd62-726dcf952e7d | -7.45256 | -42.76959 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| aeb83393-aea8-3105-8d80-b59837719686 | -6.53916 | -43.40574 | 2025-11-15 04:25:00 | NOAA-20 | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Caatinga | 5.1 |
| 321d8f50-2040-305f-9f22-2e6e5c354568 | -5.10866 | -42.78027 | 2025-11-15 04:25:00 | NOAA-20 | TERESINA | PIAUÍ | Brasil | 2211001 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e98cb5b6-7613-353a-a434-48328ad13930 | -4.2777 | -46.8435 | 2025-11-15 04:25:00 | NOAA-20 | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | 1.0 |
| bd37c57a-b65c-35f3-81cc-1891b27e9db3 | -5.23041 | -44.35433 | 2025-11-15 04:25:00 | NOAA-20 | GONÇALVES DIAS | MARANHÃO | Brasil | 2104404 | 21 | 33 | nan | nan | nan | Cerrado | 5.1 |
| 1c21a974-9d79-3a80-915d-d0d3f80bbae6 | -3.69044 | -44.16422 | 2025-11-15 04:25:00 | NOAA-20 | PIRAPEMAS | MARANHÃO | Brasil | 2108801 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e3b0b34d-4137-3816-b42b-c5e34b9613e1 | -3.76412 | -45.08337 | 2025-11-15 04:25:00 | NOAA-20 | PIO XII | MARANHÃO | Brasil | 2108702 | 21 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7021f930-17ed-33de-997e-1ccb1b352140 | -9.48948 | -47.2788 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 5.4 |
| e63c707a-641d-35eb-b8bd-c41a2eff03be | -3.5303 | -53.00346 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c5d4bd41-8bc9-3ba1-96cc-829d308ec84e | -4.63468 | -44.60179 | 2025-11-15 04:25:00 | NOAA-20 | PEDREIRAS | MARANHÃO | Brasil | 2108207 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a9b09d98-8d05-322b-b70d-7654b76fa5c2 | -4.10948 | -48.01016 | 2025-11-15 04:25:00 | NOAA-20 | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| f3ad6a7a-60ff-35da-a574-ba0c2f3f725c | -7.39064 | -44.06135 | 2025-11-15 04:25:00 | NOAA-20 | LANDRI SALES | PIAUÍ | Brasil | 2205607 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| c50b18a0-5c38-3401-8b88-3ecb9837456f | -9.5209 | -47.27314 | 2025-11-15 04:25:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| fb498420-a566-3376-af79-286bf8c6526e | -2.73521 | -45.29642 | 2025-11-15 04:25:00 | NOAA-20 | PINHEIRO | MARANHÃO | Brasil | 2108603 | 21 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c0751313-17c2-3328-9a5e-d4fe7d1174fa | -3.79118 | -43.37704 | 2025-11-15 04:25:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8ba66205-359a-3c3f-8273-e482a155936a | -9.02548 | -46.88344 | 2025-11-15 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ac82e3c4-a9e6-33db-aabf-439bbccab773 | -7.76543 | -45.16287 | 2025-11-15 04:25:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 006a1f01-a8ca-31a0-9ae1-e6382f59a2eb | -3.65701 | -44.81434 | 2025-11-15 04:25:00 | NOAA-20 | VITÓRIA DO MEARIM | MARANHÃO | Brasil | 2112902 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 6b7b03aa-a300-370b-8e09-a2bd1b9dad69 | -7.72685 | -42.34446 | 2025-11-15 04:25:00 | NOAA-20 | PAES LANDIM | PIAUÍ | Brasil | 2207306 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8688d7dd-7cc8-3d63-a9a0-48b346a01ba5 | -4.47651 | -45.6516 | 2025-11-15 04:25:00 | NOAA-20 | BREJO DE AREIA | MARANHÃO | Brasil | 2102150 | 21 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 4167e796-3051-3fc7-b700-fbce0a147245 | -8.15497 | -43.80917 | 2025-11-15 04:25:00 | NOAA-20 | COLÔNIA DO GURGUÉIA | PIAUÍ | Brasil | 2202752 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| 2d29cc34-f4f3-3f25-be73-f11a94102cd9 | -5.48313 | -46.37897 | 2025-11-15 04:25:00 | NOAA-20 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| bbc837ba-3283-3390-9ed4-b0e5ae0d7b6f | -4.23885 | -48.38176 | 2025-11-15 04:25:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| fd399154-56ce-3a6c-aa48-961b75af3640 | -1.1116 | -52.60013 | 2025-11-15 04:25:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8d48a38d-4b27-3a08-93a5-97659b2e4599 | -8.32349 | -45.39955 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 415acbd2-7362-32cc-a076-015e5c05c8b5 | -8.56209 | -45.52019 | 2025-11-15 04:25:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 427f18fe-19f8-376d-aa7e-42d2ca8705bf | -4.00159 | -44.17098 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c96b5f65-8aa6-3d47-b919-f7e4d27e5f44 | -2.79305 | -52.97226 | 2025-11-15 04:25:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 69bec321-1b3c-39be-af4c-8d6afffb278c | -4.75298 | -48.83544 | 2025-11-15 04:25:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 6891a47d-e5e7-3b63-b683-ff2330589dea | -4.4218 | -43.39503 | 2025-11-15 04:25:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c398a5ad-e687-3c42-a526-4d68450d8a31 | -4.11153 | -50.06015 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 8c63903c-517b-3354-bce8-9def5a619781 | -8.57076 | -46.05811 | 2025-11-15 04:25:00 | NOAA-20 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d4909a52-17ad-3c6f-94c4-c977661dc610 | -8.34089 | -46.69883 | 2025-11-15 04:25:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 10c0faae-1e8a-3932-83f7-a3ebb00ee051 | -6.59976 | -50.0682 | 2025-11-15 04:25:00 | NOAA-20 | ÁGUA AZUL DO NORTE | PARÁ | Brasil | 1500347 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 71785679-9cf5-39b3-98b5-4d50154cfba5 | -4.4795 | -42.87768 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| acfdb64b-fb05-38ed-b122-d495b257bf02 | -7.53395 | -41.17086 | 2025-11-15 04:25:00 | NOAA-20 | MASSAPÊ DO PIAUÍ | PIAUÍ | Brasil | 2206050 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 8cddce2b-3470-32fc-889e-055ab02eb9b0 | -6.17227 | -48.04851 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 19f1f72b-0d72-331c-bd93-49c26ea5ccc7 | -4.40064 | -44.0796 | 2025-11-15 04:25:00 | NOAA-20 | COROATÁ | MARANHÃO | Brasil | 2103604 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 370f38f7-da76-363d-83d4-8603d1e791ca | -3.32547 | -44.39264 | 2025-11-15 04:25:00 | NOAA-20 | ITAPECURU MIRIM | MARANHÃO | Brasil | 2105401 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| dc1162bf-d074-39c9-9613-0ac603b594d9 | -2.95157 | -48.58622 | 2025-11-15 04:25:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5335e085-eab2-3a3e-94b3-fc30cb971cd2 | -4.91465 | -44.78613 | 2025-11-15 04:25:00 | NOAA-20 | ESPERANTINÓPOLIS | MARANHÃO | Brasil | 2104008 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6851eae1-9eb6-3512-9a28-c1c67c1499a1 | -4.59133 | -44.31626 | 2025-11-15 04:25:00 | NOAA-20 | CAPINZAL DO NORTE | MARANHÃO | Brasil | 2102754 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b160406-64ab-3d6c-8425-e4c13e356fb4 | -4.37069 | -50.88861 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 79b5b48e-e846-32a1-a75d-5d5584d23e43 | -3.14949 | -50.27006 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3f1c6508-80f0-33b2-8e14-e945664ef674 | -5.59401 | -45.17669 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 72726d2c-83d6-3ecb-b2be-03f511e435cf | -5.60678 | -45.18227 | 2025-11-15 04:25:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| be2eb1ee-a376-3d19-b798-c5258e051962 | -9.86167 | -44.71431 | 2025-11-15 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 5729733e-7ae1-34a1-afaf-630a6627c600 | -8.328 | -45.41481 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| ce4f652b-e2be-35cb-9f69-c5ec7edb5a75 | -4.82146 | -47.09578 | 2025-11-15 04:25:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 35f0573b-cebc-3cbb-8347-852ea4439477 | -5.85307 | -44.38523 | 2025-11-15 04:25:00 | NOAA-20 | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a3c01bf7-43ec-30f2-a4fc-1314bd412303 | -4.17778 | -50.42163 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 1d478fc8-5b2f-333b-936d-baaf5fba298b | -1.34582 | -54.60958 | 2025-11-15 04:25:00 | NOAA-20 | MONTE ALEGRE | PARÁ | Brasil | 1504802 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0fa64ef3-390d-3fc9-964b-1ffac0d5372e | -7.44309 | -42.7698 | 2025-11-15 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6cca7e18-8c12-3033-bbc2-02b502458b71 | -7.88365 | -48.40372 | 2025-11-15 04:25:00 | NOAA-20 | PALMEIRANTE | TOCANTINS | Brasil | 1715705 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| b9762355-b366-34a6-bc98-4926f46c8505 | -5.52135 | -41.77094 | 2025-11-15 04:25:00 | NOAA-20 | SÃO JOÃO DA SERRA | PIAUÍ | Brasil | 2209906 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 01337f55-147b-3b0b-957f-2336f8ef1e0a | -6.40227 | -46.56013 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 0fe80c02-d122-3a61-b743-add3de348f2d | -8.32685 | -45.40006 | 2025-11-15 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4fe08ee3-bb1f-3f98-90f5-3e71e667f97a | -4.17386 | -50.42093 | 2025-11-15 04:25:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| e4d97aba-223f-3d66-a963-cbeba3042c3d | -6.15466 | -48.04939 | 2025-11-15 04:25:00 | NOAA-20 | ANANÁS | TOCANTINS | Brasil | 1701002 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5fc66c6e-b561-38bd-96a2-6e7f64f455ee | -6.3973 | -46.54871 | 2025-11-15 04:25:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| ffad2178-c88b-379c-b6ae-4dd02aa5bc81 | -7.69237 | -47.18969 | 2025-11-15 04:25:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fccdaf28-6167-3be0-867f-a4ed395580ae | -6.92533 | -44.45124 | 2025-11-15 04:25:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 02dc16ed-be80-388c-9910-b986c8352265 | -4.39443 | -45.85014 | 2025-11-15 04:25:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 86563ae2-a63a-3093-a8a1-ab52e1e05230 | -3.89473 | -43.81918 | 2025-11-15 04:25:00 | NOAA-20 | VARGEM GRANDE | MARANHÃO | Brasil | 2112704 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 5633ca06-7a11-30a5-b7df-07dc4e5cfe68 | -9.12711 | -47.1206 | 2025-11-15 04:25:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6435ff37-cbb2-3aeb-b5f9-d02193b668fb | -5.22135 | -44.43449 | 2025-11-15 04:25:00 | NOAA-20 | PRESIDENTE DUTRA | MARANHÃO | Brasil | 2109106 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 13a6e36a-cdfa-3afc-a196-0d4ffeb8552f | -2.85421 | -51.27875 | 2025-11-15 04:25:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c97371c3-7489-3e44-bcb7-c35d30d4ecb5 | -4.85452 | -43.25888 | 2025-11-15 04:25:00 | NOAA-20 | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |


[Clique aqui para ver as próximas entradas](README44.md)
