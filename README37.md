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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 4eec3424-387d-397f-8142-8a276b7c9ff5 | -3.38447 | -50.16972 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 127a5110-22cb-3ebb-8507-6feba9d55be6 | -3.43789 | -50.25431 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| de747b8b-cf00-32b4-9363-9f0dc7b6fbed | -3.16863 | -48.60601 | 2025-10-14 05:16:00 | NOAA-21 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| daad09f9-2453-355e-a2f5-c1db8fa26e14 | -7.75153 | -45.73272 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 9a02e1c2-8bbd-345d-8a1f-0796e34be307 | -2.52891 | -47.80187 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b9b19e0e-939c-3416-9a8f-e0f151cb0aad | -3.06481 | -49.40581 | 2025-10-14 05:16:00 | NOAA-21 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 745fa994-d54e-35cf-a269-65a7a9394d5c | -2.53409 | -47.8067 | 2025-10-14 05:16:00 | NOAA-21 | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| b4373740-f780-33b8-a087-c42befaccfbf | -3.15854 | -50.23109 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 1f8c2c76-5b9b-3244-b363-0142322df2ee | -3.43295 | -50.25358 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 538e5fff-bbaf-307d-a0d5-6a6a2649ae5a | -2.44359 | -47.16449 | 2025-10-14 05:16:00 | NOAA-21 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 7d7a5d8f-104a-3925-9628-4f20d778863e | -1.4791 | -52.98421 | 2025-10-14 05:16:00 | NOAA-21 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 0b9a4c5c-0598-3346-8b65-0a0b925ccc6b | -5.22785 | -50.82557 | 2025-10-14 05:16:00 | NOAA-21 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 909786b6-94be-3541-b58e-b6586193c44d | -3.13804 | -50.21128 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| bc54b4ea-7ace-3cd7-b722-0d705e86e09b | -3.9625 | -52.19571 | 2025-10-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3dec7047-5f1b-3d32-9912-3facb9231a9d | -1.1063 | -52.2673 | 2025-10-14 05:16:00 | NOAA-21 | VITÓRIA DO JARI | AMAPÁ | Brasil | 1600808 | 16 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 2b5376af-0be3-373a-ae80-b953c77a5855 | -3.13647 | -50.21037 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 1fc71aee-3ea2-3f92-ae0a-167b966c1449 | -8.11796 | -55.2866 | 2025-10-14 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 70d0fa42-29ab-3c1a-bb1b-8058393087b8 | -4.30471 | -50.3996 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 336e0c1b-af4d-3f98-ad00-6592a30c6456 | -6.53249 | -55.03281 | 2025-10-14 05:16:00 | NOAA-21 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6641c2fd-9560-3a37-b338-c46d0c76bcca | -1.89746 | -51.00801 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 0e052d82-99b9-3d5d-8058-7c661eb09281 | -7.75411 | -45.71194 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.9 |
| f5bfbbc8-2583-3b3e-8068-a5c7df5f708c | -4.87375 | -48.6608 | 2025-10-14 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 46386bca-379b-311a-a951-92c8a89b1a63 | -7.62817 | -47.83688 | 2025-10-14 05:16:00 | NOAA-21 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 1384f2a7-baa0-3847-9de9-775a01367fa2 | -3.26628 | -52.57526 | 2025-10-14 05:16:00 | NOAA-21 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 1228e92e-b671-3597-9877-d0188fd649af | -5.02157 | -46.76747 | 2025-10-14 05:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 6bc076d9-54a2-3961-80af-84f80592c772 | -4.28326 | -48.57969 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 3bcf1f07-fba8-39b3-a5e1-30f0a32689b9 | -2.07048 | -52.00444 | 2025-10-14 05:16:00 | NOAA-21 | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 1b4bfbc8-a524-316a-8355-60bebb58f6f8 | -1.43596 | -60.29892 | 2025-10-14 05:16:00 | NOAA-21 | PRESIDENTE FIGUEIREDO | AMAZONAS | Brasil | 1303536 | 13 | 33 | nan | nan | nan | Amazônia | 1.6 |
| af387a23-9c3a-3b7b-bf6f-b31e82206247 | -5.49324 | -45.41134 | 2025-10-14 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| d10e1e2f-ba9f-3257-b1b8-af896e15af79 | -4.29974 | -50.3989 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c6241670-f2de-37f0-8a05-70e27077c0f2 | -2.69088 | -51.84022 | 2025-10-14 05:16:00 | NOAA-21 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 75edc486-2b83-3e99-9ecf-61862ce6d101 | -2.88014 | -50.74163 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| acf74722-d5cb-32b3-adc1-8eee80542fba | -3.43378 | -50.24802 | 2025-10-14 05:16:00 | NOAA-21 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| e7738d17-136d-3dcd-8d7c-f35880131546 | -1.90204 | -51.0087 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 3324defe-624c-3bfd-960e-cf95ab6a5609 | -3.13155 | -50.20953 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| c229b97a-9ef3-3c48-8ed9-60902ffdf246 | -5.10224 | -56.15503 | 2025-10-14 05:16:00 | NOAA-21 | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 35d0249d-e2b6-3adf-8804-a5ce168cfecc | -5.01755 | -46.76885 | 2025-10-14 05:16:00 | NOAA-21 | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 5fdcd799-1b1c-381d-81ce-e345062cfef9 | -7.74724 | -45.72115 | 2025-10-14 05:16:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 11.5 |
| 83786ec6-1572-3f65-8612-f33ef21de722 | -4.28272 | -48.58354 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 538f97d4-6029-3b94-abfe-99edadb9af9c | -4.86813 | -48.65999 | 2025-10-14 05:16:00 | NOAA-21 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7670d8cb-fe4d-3a46-a819-9c6095de09dc | -2.87615 | -50.73581 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d4acbef2-cb1c-37d3-807b-1cd736b758fb | -4.56016 | -49.64864 | 2025-10-14 05:16:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| dd20908f-7457-30af-a658-76c06036e74f | -2.22233 | -51.7766 | 2025-10-14 05:16:00 | NOAA-21 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 20d4648e-de50-3d0f-b5e7-55459b3c75fa | -4.28436 | -48.57199 | 2025-10-14 05:16:00 | NOAA-21 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ce8dfaa8-ded9-339e-a993-fd7a96b00f07 | -3.50708 | -49.71926 | 2025-10-14 05:16:00 | NOAA-21 | BAIÃO | PARÁ | Brasil | 1501204 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 6ad6a6e5-9fcf-3b9e-8a48-f63c40151fa6 | -7.72348 | -55.20639 | 2025-10-14 05:16:00 | NOAA-21 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 3.5 |
| d695d5dc-f223-3a5b-80bc-3ade2580c0cc | -5.4941 | -45.40503 | 2025-10-14 05:16:00 | NOAA-21 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 8f0ce8f4-0303-31e2-8aab-b7f9b18a1526 | -12.81409 | -50.63697 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| ae67af0a-6eb8-3e60-8623-53b7db47cf09 | -8.84365 | -62.29449 | 2025-10-14 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c92a48c7-468c-39c7-ac65-c1ef1a0ca507 | -11.94408 | -51.33306 | 2025-10-14 05:18:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5e26a5ba-c5e7-3ed9-8432-638c19faeedc | -12.49378 | -51.29444 | 2025-10-14 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 00283b18-4528-33f5-b1bc-0fb0b35ea121 | -12.14276 | -53.61756 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3d82c6e4-1a4a-31b1-b764-c1932f5a3f3f | -12.15107 | -53.62331 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| c196423f-09b2-3068-8a9b-3feb3d400bbe | -8.97921 | -61.97949 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 21c34ea6-fd66-3b1a-a3a2-67eb83f1e477 | -8.59754 | -63.3301 | 2025-10-14 05:18:00 | NOAA-21 | CANDEIAS DO JAMARI | RONDÔNIA | Brasil | 1100809 | 11 | 33 | nan | nan | nan | Amazônia | 2.2 |
| d01f8d87-dc01-376a-a3b2-616d17b9f695 | -12.48853 | -51.29372 | 2025-10-14 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 93f95335-4c64-374c-b7c2-fff1aa5d9102 | -12.82004 | -50.63403 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.7 |
| 1c9e0e9d-37d9-3608-b773-776dfdadeec9 | -12.83061 | -50.63918 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.7 |
| 7cc8d7dc-2efb-3b65-a206-9aa89442fee5 | -9.33018 | -61.83411 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 52e5ab06-add8-3ee9-9a3f-cf061445fb4b | -9.48525 | -57.92544 | 2025-10-14 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 65f9a6aa-a46c-357a-9bcc-f134bcd24ce5 | -9.01493 | -62.00129 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 29619da4-2ab4-3292-85a0-58bab8e89913 | -12.48774 | -51.3003 | 2025-10-14 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 1c437d47-90e6-3ef6-b41e-932f3a5d3d22 | -12.82377 | -50.64946 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| f03b8385-ea79-30c8-81fe-8460d5f96449 | -12.04859 | -54.24623 | 2025-10-14 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 9a992ec0-00f1-3164-974e-7241b4534485 | -11.5993 | -54.54121 | 2025-10-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f2f597c0-455b-3f86-982b-3645a4921348 | -12.79625 | -50.64579 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| 43351af4-740e-3fb1-a673-b4cfb7a820fc | -9.41357 | -62.2951 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d7648ea9-5df6-3549-8501-e0973821f15f | -12.14723 | -53.61816 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ac594e29-c440-338a-bdc3-51739abc3898 | -8.84299 | -62.29849 | 2025-10-14 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e941325-53df-3add-9618-b29e090fd32c | -10.62141 | -54.95123 | 2025-10-14 05:18:00 | NOAA-21 | TERRA NOVA DO NORTE | MATO GROSSO | Brasil | 5108055 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 517342a5-a75f-33cc-a6e9-8ede54badf7c | -8.70794 | -64.12196 | 2025-10-14 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 2e817bb1-09f6-38d1-95d6-1e9199968794 | -10.18325 | -57.92076 | 2025-10-14 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 08ff2c53-2657-3072-97e0-8dc28084b3cf | -8.96391 | -62.02896 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 6ccc728b-e1c8-35e1-94e2-c4b547c492e5 | -12.04376 | -54.24973 | 2025-10-14 05:18:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 20a60c5c-325e-3a9f-8a68-7d7de464ca19 | -12.79668 | -50.64212 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 5ef9bed7-3cdf-396c-b096-fcafd9b27070 | -12.49339 | -51.29773 | 2025-10-14 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 17c6fbd7-8e16-372d-882e-0793bea99993 | -9.17975 | -61.81067 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c0d57528-2dae-3c01-aa65-5077203ff48e | -12.79581 | -50.64946 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 15.9 |
| ec7ee02e-1398-3338-a077-f46b1eee98d9 | -8.97985 | -61.97561 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 5315ef9c-1aaf-3cfa-829d-5a984c6ae176 | -8.97637 | -61.97505 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 2.4 |
| e5f62ca6-12a5-388f-a7cf-f4a71819c51a | -9.22496 | -62.204 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b2029fa3-3771-3164-a00c-fdd2b36bb41f | -12.80219 | -50.64286 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7e959bee-730a-3faf-b8c3-79ec1ed3477f | -12.80858 | -50.63623 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 65551fc2-249c-3aa2-b03c-c1ad5a459b9b | -12.80263 | -50.63919 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| eee09e87-70cb-321d-bb9b-2d352f13b88b | -7.48594 | -63.76716 | 2025-10-14 05:18:00 | NOAA-21 | CANUTAMA | AMAZONAS | Brasil | 1300904 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 421495f7-6136-3bac-bd67-8db2ed225daf | -8.95937 | -62.16536 | 2025-10-14 05:18:00 | NOAA-21 | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ef73f3a5-c5da-3283-8d9c-1cd6c0d11e26 | -11.60159 | -54.5418 | 2025-10-14 05:18:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c235ca2e-43dc-390d-af6a-20ec9e89d75d | -12.83017 | -50.64285 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 2c5838f4-a69c-34e8-a64b-df49ab904401 | -12.48813 | -51.29701 | 2025-10-14 05:18:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 4453f189-2636-3411-b788-5421e8ee43cd | -12.85841 | -50.64434 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 53157b73-8644-38f1-854e-a4f4a15c3374 | -12.1383 | -53.61697 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| ee43da7e-60f6-37c2-9050-8a9e8d1234d1 | -11.94448 | -51.32983 | 2025-10-14 05:18:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| fae2ef20-d1dd-39b9-a6f6-b2f27c659f90 | -12.14338 | -53.61303 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 30c1bee4-8fe2-38cf-875e-079273b22d7a | -9.13531 | -62.39818 | 2025-10-14 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e01d71e3-a14b-35e6-828c-b2af5d839777 | -8.84653 | -62.29906 | 2025-10-14 05:18:00 | NOAA-21 | CUJUBIM | RONDÔNIA | Brasil | 1100940 | 11 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c09df3ab-12ab-3aa2-815f-ca3978f3406c | -12.81453 | -50.63327 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 8.7 |
| 2121ce0d-9db5-396e-8898-d14a4fc7826e | -12.80814 | -50.63992 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 24.8 |
| cfb9e653-3fbf-3c31-858f-03b0d9109d4c | -12.14995 | -53.62043 | 2025-10-14 05:18:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 0650905c-550f-365c-9eb8-d846a4e3edd5 | -10.17984 | -57.9202 | 2025-10-14 05:18:00 | NOAA-21 | NOVA BANDEIRANTES | MATO GROSSO | Brasil | 5106158 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| e71b7ddd-d92d-3e33-8984-cc985f4ea9c9 | -12.82048 | -50.63034 | 2025-10-14 05:18:00 | NOAA-21 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |


[Clique aqui para ver as próximas entradas](README38.md)
