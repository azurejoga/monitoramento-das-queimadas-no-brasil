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

## Dados Diários - Página 35

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 15373d40-8778-3701-a599-1b99a0d89be7 | -8.193 | -46.78448 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 99042ca5-e366-3559-8478-775dbb274549 | -7.49671 | -45.3512 | 2025-09-02 04:14:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 85f1c5c3-4e5d-37d8-a7b4-829bf572b6ff | -6.86924 | -45.56213 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3e9d72b3-0867-399e-b91a-b3a07c242edc | -10.84058 | -47.27713 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| a3108a7c-daeb-34ee-a839-182b20c0ba52 | -6.80609 | -52.81332 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| a98a9cdf-c795-3699-b69e-aba090c0fd9e | -12.76721 | -48.08237 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0643a233-bd8a-364a-be73-a9a0ed62a0a8 | -8.01015 | -44.52144 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2c5913f0-1af9-3cf1-b9a5-0f76efc34c63 | -9.11888 | -46.05218 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| f1601fd7-38f1-3440-bdad-11362a854c12 | -11.1004 | -44.63828 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.0 |
| 4e156b80-9039-3556-86c6-052e7fb5bb8e | -9.74222 | -48.9692 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 43e67926-731c-30ef-afe3-de634ab824f6 | -12.94251 | -48.0889 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 6.6 |
| b64ea278-50a1-3789-a92e-071d78be1768 | -11.00667 | -46.93741 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| d0fdfd16-9adc-3714-846d-751459a36abb | -11.84573 | -51.53602 | 2025-09-02 04:14:00 | NOAA-20 | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 22edaa11-5058-3097-bc4a-5ac8a9c5028e | -7.70672 | -45.00964 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b8165f10-a699-39cc-87d3-91628ef2456d | -6.63979 | -44.10699 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ffc4d51e-8876-32b9-88bc-02ca0ec570d1 | -8.15306 | -42.47378 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 18ee07cb-e133-3482-b374-ef802170d5d4 | -6.832 | -52.82592 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 0fbfa4cb-6df9-37d3-a107-2784338feedb | -9.6428 | -47.78883 | 2025-09-02 04:14:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1010ff08-aeec-37d4-bdb9-c60ea7727a21 | -11.96427 | -45.79414 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07f310ad-ea7f-37d7-8013-db916b5d9842 | -11.67487 | -52.21563 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 7.7 |
| b77382cc-15ba-3967-956b-c6c7ce639e0f | -13.52464 | -46.9948 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1e836c30-1b10-3364-bc8d-1c950ea2fe38 | -8.77361 | -42.17252 | 2025-09-02 04:14:00 | NOAA-20 | CORONEL JOSÉ DIAS | PIAUÍ | Brasil | 2202851 | 22 | 33 | nan | nan | nan | Caatinga | 0.6 |
| ae31e052-4143-3bd7-95ad-84859fcacef5 | -7.92712 | -46.46615 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 6ee22dea-d7a2-38ba-8e31-cceda7b5ca60 | -13.66412 | -46.93851 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 6005ebb0-4c01-3a48-a779-edf8d50e0ef8 | -11.65543 | -52.19364 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 42.0 |
| 0d3c85f2-f6e5-3b17-ac41-e71507e969e4 | -11.95813 | -45.78937 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.4 |
| b2db4e04-3fe3-3858-97e7-68c1f23bd1ef | -11.67242 | -52.17601 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.4 |
| 988891f5-6c13-33bb-9be6-e40ae82770d6 | -6.78737 | -44.62222 | 2025-09-02 04:14:00 | NOAA-20 | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bc1dfa51-f7d1-3515-ad2c-333ed1e2c53c | -7.97897 | -44.05902 | 2025-09-02 04:14:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 5aa27127-2c4b-3c8e-84b4-1eeaa1258a51 | -6.98575 | -44.32127 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 2326f01e-5a9e-31fd-aaea-1c20ce599711 | -10.83805 | -47.4464 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| f43c8f03-34eb-3132-83ef-8b81110ff3d0 | -10.82936 | -47.45367 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| a8e940eb-5066-32a2-b8a0-48dc44559773 | -7.4663 | -44.80096 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c3c35185-f249-3bb8-80c3-3ca129b454a4 | -11.90753 | -46.67043 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| ef79fe39-936a-3574-bcce-72de0cf322d7 | -8.18722 | -46.79676 | 2025-09-02 04:14:00 | NOAA-20 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7639d4c5-940c-3496-a33a-80cd2a1a7336 | -7.97848 | -46.46625 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 7.8 |
| 8fdac999-8bd1-3dd6-9572-4dd0d1b03bfa | -6.81089 | -52.81797 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| b0dccb0c-f384-3db7-bcb0-229b73820ad5 | -13.69435 | -46.88366 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 741e857c-d7e9-3d0d-b39f-42aa32028843 | -9.25349 | -40.51702 | 2025-09-02 04:14:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 54c9b63a-add0-3c12-90ce-8df675a9f6c7 | -6.81689 | -43.33241 | 2025-09-02 04:14:00 | NOAA-20 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.5 |
| 19b77ad3-537e-3698-8ea4-cb8e05ef4c92 | -11.09932 | -44.62368 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| b61fe22f-f49a-3629-bd66-dcba52352b81 | -13.33906 | -46.95166 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16ae934b-416f-3eed-be92-d17ffbcd1f88 | -9.52251 | -46.50956 | 2025-09-02 04:14:00 | NOAA-20 | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e72d9816-fbb9-38e4-8938-039240523f60 | -8.81881 | -47.48906 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 01fe52a1-de62-376a-b4d6-31d741415af2 | -6.90167 | -44.23189 | 2025-09-02 04:14:00 | NOAA-20 | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 1c3e1bb7-1378-3ac8-b613-f0ada99f27e6 | -6.82111 | -52.8238 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ddca666c-0eb9-3059-97d4-f4ad1787f55d | -10.27317 | -54.26512 | 2025-09-02 04:14:00 | NOAA-20 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a8450fba-fcae-33a8-8b6d-6581b1d76a23 | -13.51859 | -47.00975 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 11791c56-b6c9-38b7-893e-ea85849646de | -8.71533 | -50.44946 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 6a056160-16fa-37e9-9a65-40bc3dca3405 | -14.05477 | -44.55243 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 50722bc0-75aa-308a-8b41-2e623a760998 | -8.83583 | -45.78828 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 2cae3dfc-4da7-3d8a-93a9-364b4bf05ec1 | -6.82719 | -52.82135 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 284cffff-c235-3641-9325-5eea0a763d4e | -7.10881 | -44.75834 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| e4ae4b28-02b3-3337-b494-1caf18afdfcd | -13.30971 | -46.8508 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 3619e221-6d9e-395d-8a17-00a7ea445815 | -12.33458 | -45.71443 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 707bcf5b-25a4-3407-a875-48bbe20ece97 | -12.88651 | -48.17461 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| a5f50a8d-6475-3c1c-922a-6378282fd2cd | -9.83208 | -48.32077 | 2025-09-02 04:14:00 | NOAA-20 | LAJEADO | TOCANTINS | Brasil | 1712009 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| ffa35722-c113-363f-8d4c-3782796a2236 | -7.10544 | -44.75778 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 48a438db-e6c3-396a-ac24-5a4b15794201 | -6.86703 | -45.55387 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| eb6cbc4b-b732-3904-8a8d-c3cc12c827d6 | -11.97358 | -45.88574 | 2025-09-02 04:14:00 | NOAA-20 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 13637b4b-4e04-3d3b-adcd-cc0bf777fcc2 | -8.81549 | -47.83579 | 2025-09-02 04:14:00 | NOAA-20 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 8b3b4957-c973-3582-a93c-182e2de0f6ce | -11.05259 | -52.06251 | 2025-09-02 04:14:00 | NOAA-20 | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a8c988dd-2f05-3561-9464-6d3329b8628d | -11.66209 | -52.21178 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 22.8 |
| bf51e16b-07ef-3c17-9d9f-82b01532d7c6 | -7.67254 | -43.8707 | 2025-09-02 04:14:00 | NOAA-20 | BERTOLÍNIA | PIAUÍ | Brasil | 2201705 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 5da86522-cbd8-3087-89d9-a46b955a963e | -8.06984 | -49.714 | 2025-09-02 04:14:00 | NOAA-20 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 7b45859c-3ada-3116-b23b-0cfa21356424 | -7.17707 | -45.76115 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 12dbb435-207a-37b4-885e-40e1f8944dfa | -9.65398 | -47.04199 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7eedbcd2-6190-3993-9afa-98514b8cdf6e | -12.61883 | -48.1866 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 28.1 |
| 6f4002a6-583b-3312-983d-a86316483875 | -6.97846 | -44.34539 | 2025-09-02 04:14:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b7676a67-2b98-3874-8b1a-f7de779ea481 | -6.59834 | -48.00554 | 2025-09-02 04:14:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 179a8a08-d071-30d1-bdac-3560da0bc241 | -7.60634 | -46.03766 | 2025-09-02 04:14:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 4f452373-6eaa-3122-acc1-866111b984e4 | -7.41678 | -44.80781 | 2025-09-02 04:14:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 5e07bea5-8846-3499-b8ab-999f337c11b9 | -12.98704 | -48.11365 | 2025-09-02 04:14:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 047c0345-6c02-3e79-8d7e-b5d05c2e1c0c | -9.65469 | -47.03781 | 2025-09-02 04:14:00 | NOAA-20 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 82994189-4687-3c71-9b75-f304d5dc2f8c | -6.8765 | -45.8472 | 2025-09-02 04:14:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 10db939a-148d-3cde-acb8-319fab40d6b1 | -11.42991 | -55.19212 | 2025-09-02 04:14:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| cda33eea-c036-3b74-a306-8f2a467d31d0 | -11.88764 | -46.68291 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 4f9fc2a7-a3c7-3d8b-81b3-377fa507e7d6 | -7.92341 | -46.44431 | 2025-09-02 04:14:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9e0eb1cc-7eeb-3b25-8d50-68f1df98234a | -6.8307 | -52.83316 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 2015fefa-e9f4-35a0-a2ae-7a6c095300b0 | -13.52269 | -47.00648 | 2025-09-02 04:14:00 | NOAA-20 | MONTE ALEGRE DE GOIÁS | GOIÁS | Brasil | 5213509 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 415f1829-175b-3276-b4be-89b504a80ffa | -11.09657 | -44.61963 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 10.8 |
| 89ad8a44-5f4f-3564-9174-b6d70fba6db6 | -7.66235 | -42.70435 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| e4eebb97-9abe-3a73-a912-23d6ab0a63d1 | -6.68592 | -44.39328 | 2025-09-02 04:14:00 | NOAA-20 | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d00b4269-d8c4-33a8-b8a7-4110a2607b94 | -12.38262 | -46.47362 | 2025-09-02 04:14:00 | NOAA-20 | TAGUATINGA | TOCANTINS | Brasil | 1720903 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b41efad-8fac-33d6-833b-e4bd99efb0ed | -6.83617 | -52.83409 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b836c8bc-8c80-3cbb-bd56-163eaf931b93 | -7.20207 | -44.22156 | 2025-09-02 04:14:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 70d81f2b-243f-3be1-a77c-ed18cbaec47d | -7.56088 | -45.71482 | 2025-09-02 04:14:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6dddd0fa-c4c3-365e-b940-08dfcb73ef90 | -9.73236 | -48.97844 | 2025-09-02 04:14:00 | NOAA-20 | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 5b529295-5a2b-3c42-876d-d1f61917cf2f | -13.69008 | -46.93135 | 2025-09-02 04:14:00 | NOAA-20 | NOVA ROMA | GOIÁS | Brasil | 5214903 | 52 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 74537b42-c7bf-357a-99da-ba5a81a56e3f | -8.15361 | -42.47023 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b1c962b6-a30a-3479-9c79-e1cfbf5bb074 | -11.91032 | -46.67502 | 2025-09-02 04:14:00 | NOAA-20 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c6a22497-a14d-3349-9821-95b66bcf9efd | -7.62336 | -42.6516 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 9c49bfe2-f303-33e3-bcb1-0d5eef503ae7 | -11.66492 | -52.22359 | 2025-09-02 04:14:00 | NOAA-20 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 38.0 |
| 0dfa3e13-e7ab-387b-a95f-e7b451075e7f | -8.46283 | -47.36925 | 2025-09-02 04:14:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 2f1f78f1-816f-3a55-a6de-cb856a98123f | -8.8723 | -45.75938 | 2025-09-02 04:14:00 | NOAA-20 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 52e28fc6-5055-355c-8336-2a12434ac79f | -14.04755 | -44.59858 | 2025-09-02 04:14:00 | NOAA-20 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 991a0035-d0d4-3874-aef5-0e946a06ca3e | -7.65902 | -42.70384 | 2025-09-02 04:14:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 79dc8d8a-afab-37f2-973b-0ee6b016982a | -11.0943 | -44.65532 | 2025-09-02 04:14:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| f870df1c-7098-363d-88e2-1cc3910a1c29 | -11.05921 | -46.90504 | 2025-09-02 04:14:00 | NOAA-20 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 976d9825-9563-3324-910d-946a5e4ff16d | -9.71711 | -48.94658 | 2025-09-02 04:14:00 | NOAA-20 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |


[Clique aqui para ver as próximas entradas](README36.md)
