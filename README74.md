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

## Dados Diários - Página 74

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 844c6554-7634-342a-83f5-787e45b7db8d | -4.63419 | -48.69744 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| ea6e1c1d-f078-39ae-9ef9-04cb09984022 | -2.63915 | -47.30016 | 2025-10-28 05:01:00 | NOAA-20 | NOVA ESPERANÇA DO PIRIÁ | PARÁ | Brasil | 1504950 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4d9dab13-c2cf-3052-aa82-a24b1d404cce | -4.71431 | -46.42832 | 2025-10-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| d2e7547c-02b7-31c7-980a-f6bb76363e1d | -3.2522 | -52.91399 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 3.3 |
| a49c4ad5-baea-3e83-a236-29d19dd6afb6 | -2.80554 | -49.13955 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b0178c09-8be9-39a9-8496-3f2b995da7d8 | -5.64658 | -47.62897 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 94626554-cf0f-36ad-818c-5b4018979ee8 | -3.85741 | -54.08096 | 2025-10-28 05:01:00 | NOAA-20 | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| fabdf782-10b6-321f-be2f-2326c673d1c8 | -3.23742 | -48.77628 | 2025-10-28 05:01:00 | NOAA-20 | TAILÂNDIA | PARÁ | Brasil | 1507953 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 9dea7dca-ec62-31ee-ada0-3707ae911d0c | -5.48759 | -42.17045 | 2025-10-28 05:01:00 | NOAA-20 | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| fa06a430-8e3f-3c05-b41f-57a7b7b9659d | -4.45395 | -43.6465 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 6053a9d9-a06c-3b06-8d5e-c119520e8461 | -3.38355 | -50.15267 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| cabf4697-d96f-3a2c-8e96-24f58a0c2882 | -5.62778 | -47.62052 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO DO TOCANTINS | TOCANTINS | Brasil | 1720804 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 44d36ee0-55e8-3e34-aa16-f6486d35f59e | -3.02405 | -45.36636 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 8af6ce4c-d175-33d8-8d4c-9ede9511b6ca | -4.85424 | -50.68027 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 60579bf9-5463-324b-a1a3-4fb818cc33d6 | -3.59286 | -48.98946 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d2276173-e36b-32e2-81e3-7e0fb7bc7268 | -3.7409 | -59.44704 | 2025-10-28 05:01:00 | NOAA-20 | AUTAZES | AMAZONAS | Brasil | 1300300 | 13 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c6f791de-4a97-3b67-b20b-a14a3b106e9d | -3.57444 | -49.02443 | 2025-10-28 05:01:00 | NOAA-20 | GOIANÉSIA DO PARÁ | PARÁ | Brasil | 1503093 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c70cc2d3-87c8-3ebc-9dd7-92b90a7197cd | -2.75158 | -45.41753 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 2f208e78-f148-3c37-9af2-6218a6d7413a | -5.55734 | -49.57391 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| d56629f6-1e1d-311d-b098-e0b5850e71a9 | -3.029 | -45.37075 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 4.6 |
| 95255e55-513c-308a-8ae0-06bdccf50cf4 | -3.02399 | -45.37061 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 16.3 |
| 0a9138e4-6c54-3037-9081-5ef2dbf1d1d3 | -3.56567 | -55.43668 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 6758fc05-b67a-3c6b-b396-840a03ff81cc | -2.91212 | -49.81353 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS DO PARÁ | PARÁ | Brasil | 1505205 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| f4055a35-5ee6-3854-badf-0d95655881c6 | -4.55877 | -55.7315 | 2025-10-28 05:01:00 | NOAA-20 | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f675f713-2140-338d-9313-dd14bbdeea3b | -4.90087 | -48.5714 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 429d1768-8f91-394c-ab05-bcc0a37f5925 | -5.70188 | -49.19674 | 2025-10-28 05:01:00 | NOAA-20 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 6.4 |
| a8714520-3135-3325-89b9-ab520aee6ef8 | -1.50958 | -53.1577 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| e0353536-e426-3592-9d8f-a2a081b0d57c | 1.63434 | -55.68577 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| ce8db58a-3819-3bde-b463-3526674b1db6 | -4.25424 | -53.54319 | 2025-10-28 05:01:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| dd9e1360-de90-3aea-b91c-a04e193c206f | -3.58096 | -43.63768 | 2025-10-28 05:01:00 | NOAA-20 | NINA RODRIGUES | MARANHÃO | Brasil | 2107209 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| aac8a871-359a-39c7-a14b-32ad56a26c1b | -3.1767 | -52.49534 | 2025-10-28 05:01:00 | NOAA-20 | BRASIL NOVO | PARÁ | Brasil | 1501725 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 6b64c23a-1a42-3c87-abba-87f1752729c4 | -6.49267 | -42.22656 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 70d02b3e-a1b9-3d6f-84ce-6c3b60b35671 | 0.9705 | -51.11863 | 2025-10-28 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e0495b92-9ab3-3b8f-b2c6-555b65dca21a | -3.35245 | -50.77113 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f032b633-72a4-322f-83a5-59e094d18799 | -4.20106 | -50.09343 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| c5ad028a-6f75-3984-84d5-b2eb6e898481 | -4.50686 | -42.84158 | 2025-10-28 05:01:00 | NOAA-20 | UNIÃO | PIAUÍ | Brasil | 2211100 | 22 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 9b14367e-436d-31f7-a4de-ab1f6c83c723 | -3.53098 | -51.57848 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 0606f1f3-658f-3f81-878e-1843d56e185e | 1.14376 | -51.048 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 156af9ac-e311-316e-911f-90722bbbc72f | -1.8651 | -54.52171 | 2025-10-28 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 15be7774-a40a-375a-9326-d78bef1c5a93 | -6.48485 | -42.23175 | 2025-10-28 05:01:00 | NOAA-20 | VÁRZEA GRANDE | PIAUÍ | Brasil | 2211407 | 22 | 33 | nan | nan | nan | Caatinga | 10.2 |
| 4bf0f1f6-0acb-390f-8fb0-1b362313bb3e | -3.12963 | -53.0024 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| ab09beee-657f-35be-a9fa-331b9d5aefd2 | -4.35833 | -50.51304 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 5.9 |
| bccfdbf7-7636-32f4-ae1d-625960dea385 | -4.46371 | -43.23898 | 2025-10-28 05:01:00 | NOAA-20 | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 7986c181-7200-3f14-a939-773ca5470571 | -2.95092 | -49.34666 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 54261174-b06b-364b-a627-4f987e0e0014 | -1.58481 | -53.17273 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d6f86ffe-7040-3420-aad7-3162a48d09c4 | -5.46886 | -47.26419 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR LA ROCQUE | MARANHÃO | Brasil | 2111763 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 478cbb51-5d9f-3621-b3a6-a1d8926c44f7 | -4.91007 | -47.41748 | 2025-10-28 05:01:00 | NOAA-20 | AÇAILÂNDIA | MARANHÃO | Brasil | 2100055 | 21 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 96899485-ab21-386f-b3ef-cb66b09d4d3a | -3.57761 | -43.61752 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d07defd8-354f-3d01-bb54-7f0beaa2eb5a | -5.11105 | -48.48256 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 6.6 |
| bb824656-77f3-30d7-aacc-a6170256029e | -3.12905 | -53.0061 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f24fd8c-1168-389a-9e40-c0686681855c | -3.83647 | -50.19706 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 785744dd-ef7c-3688-9105-933eaac9577c | -3.89131 | -52.27282 | 2025-10-28 05:01:00 | NOAA-20 | SENADOR JOSÉ PORFÍRIO | PARÁ | Brasil | 1507805 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c33a6f45-e4b6-3f1d-bb02-2b2953fc4566 | -4.43768 | -45.98087 | 2025-10-28 05:01:00 | NOAA-20 | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 3c248d50-d6d3-389f-a8c7-c9c706f0fe96 | -3.02241 | -45.37713 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 13.0 |
| a44a3444-9390-3dc2-8195-aba1a1c75fa8 | -4.92564 | -48.56091 | 2025-10-28 05:01:00 | NOAA-20 | BOM JESUS DO TOCANTINS | PARÁ | Brasil | 1501576 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 3d643ade-ef4c-35ee-996f-38f6964b64ed | -1.68976 | -55.67227 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 0b1b9317-04a8-327d-8313-d0a2e9be698b | -2.74771 | -45.40614 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 4d26b95c-4bd1-3f3b-9aa3-da88c885944e | -3.46617 | -49.97355 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5dda5c9d-5a41-33c3-ab7b-14b49d1b8dce | -3.23448 | -50.65332 | 2025-10-28 05:01:00 | NOAA-20 | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| c873c4eb-3732-36e3-8cc4-5640efbc4ff5 | -3.02296 | -45.37354 | 2025-10-28 05:01:00 | NOAA-20 | PEDRO DO ROSÁRIO | MARANHÃO | Brasil | 2108256 | 21 | 33 | nan | nan | nan | Amazônia | 25.6 |
| afe1029e-51df-387a-aa0e-50d61c276df0 | -4.71387 | -46.43143 | 2025-10-28 05:01:00 | NOAA-20 | BURITICUPU | MARANHÃO | Brasil | 2102325 | 21 | 33 | nan | nan | nan | Amazônia | 2.3 |
| afa1dc8c-62b0-3711-a47e-edd426877194 | 0.40518 | -50.85186 | 2025-10-28 05:01:00 | NOAA-20 | MACAPÁ | AMAPÁ | Brasil | 1600303 | 16 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 9559a3a5-546e-3935-9f21-eba5cfc39475 | -3.5468 | -54.69352 | 2025-10-28 05:01:00 | NOAA-20 | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f9c8c257-c593-3fea-8723-6c89932a0ddd | -3.84375 | -50.97279 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7e219d9b-c72c-3b84-b399-0786a2c57681 | -4.50635 | -50.19437 | 2025-10-28 05:01:00 | NOAA-20 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 75661d81-e7cf-31e9-8996-428d52a10b44 | -3.33859 | -53.03329 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6e885e1d-50f6-3fea-bb70-fe27ba575b24 | 1.20163 | -51.07312 | 2025-10-28 05:01:00 | NOAA-20 | TARTARUGALZINHO | AMAPÁ | Brasil | 1600709 | 16 | 33 | nan | nan | nan | Amazônia | 1.5 |
| b2b1ae12-6d1f-343e-a157-266758e46085 | -2.83395 | -49.40246 | 2025-10-28 05:01:00 | NOAA-20 | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 9.6 |
| caa65438-0d8f-32aa-9e21-f9bac82a64f0 | -3.57071 | -43.62136 | 2025-10-28 05:01:00 | NOAA-20 | SÃO BENEDITO DO RIO PRETO | MARANHÃO | Brasil | 2110401 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9256c065-0092-3dc9-a567-6ff94a474f05 | -3.43977 | -50.22729 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 766091cc-67f0-3e31-9301-d004040f699f | -4.86995 | -48.52954 | 2025-10-28 05:01:00 | NOAA-20 | ABEL FIGUEIREDO | PARÁ | Brasil | 1500131 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0ee03cf5-446b-36b6-ac5f-9232c5aad49d | -3.11488 | -51.21423 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 50f7d2d9-a25d-36dd-ae86-6ea546893b5c | -6.16905 | -46.0942 | 2025-10-28 05:01:00 | NOAA-20 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 9ee42165-2fda-375d-aa31-f3147fbe9d76 | -5.19802 | -46.15338 | 2025-10-28 05:01:00 | NOAA-20 | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7f6fc6f2-6514-3324-a83c-59eeb01b9d48 | -3.53163 | -51.57417 | 2025-10-28 05:01:00 | NOAA-20 | ANAPU | PARÁ | Brasil | 1500859 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| dd4719ea-57d1-38ae-9b20-0b92c5655d60 | -6.7048 | -42.04949 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| ba90319e-775e-32e8-b25c-50a2a36f8237 | -1.38863 | -55.23537 | 2025-10-28 05:01:00 | NOAA-20 | ALENQUER | PARÁ | Brasil | 1500404 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a1f0437e-f450-362f-8669-b84b1af4519b | -3.17256 | -45.65418 | 2025-10-28 05:01:00 | NOAA-20 | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | 0.8 |
| cbc409e0-95e9-30e7-8a01-e013c478fdb2 | 0.99636 | -51.10324 | 2025-10-28 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9755e782-901b-333e-82f9-12e8e18c822d | -4.45679 | -43.64521 | 2025-10-28 05:01:00 | NOAA-20 | CODÓ | MARANHÃO | Brasil | 2103307 | 21 | 33 | nan | nan | nan | Cerrado | 14.7 |
| 107a2369-bfa7-3192-92e7-22b197897315 | -3.86551 | -55.6892 | 2025-10-28 05:01:00 | NOAA-20 | AVEIRO | PARÁ | Brasil | 1501006 | 15 | 33 | nan | nan | nan | Amazônia | 3.0 |
| dd1b527b-5ad4-3ea6-8f9b-89e22cbcc6d7 | -6.03442 | -46.56374 | 2025-10-28 05:01:00 | NOAA-20 | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7cedca8b-638a-307f-995c-aee10b4328ca | 1.62584 | -55.69836 | 2025-10-28 05:01:00 | NOAA-20 | ÓBIDOS | PARÁ | Brasil | 1505106 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 3bb2d01b-db69-33e9-91d1-77d752be27ad | -1.70043 | -53.68883 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 835d27be-982c-3ed1-bc54-e139d2e4982c | -3.09646 | -54.61938 | 2025-10-28 05:01:00 | NOAA-20 | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c78edd1d-74e8-34ab-a39b-b8b693a059c0 | -1.50065 | -53.12701 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| b085fb28-cc9c-312b-bb97-a3a5f59ccae1 | -4.20612 | -48.3582 | 2025-10-28 05:01:00 | NOAA-20 | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.5 |
| 715a3d8a-61eb-39d6-b22d-35902005648a | -3.80073 | -51.1035 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 96f4bbb2-8498-31a4-bdf4-3706e5df12e7 | -3.04908 | -53.02456 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7a629de9-5671-38e2-b9c4-3c468274de3f | -3.13647 | -53.00343 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2ded2f04-d3cb-3792-89b0-af8901a87f29 | -3.47021 | -49.97414 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| e5976ce3-63ef-326d-ab98-37b718cd7bd7 | -1.33354 | -53.60342 | 2025-10-28 05:01:00 | NOAA-20 | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| c9d58c48-7f38-3e6e-8326-11d686a5267a | 0.99701 | -51.10728 | 2025-10-28 05:01:00 | NOAA-20 | FERREIRA GOMES | AMAPÁ | Brasil | 1600238 | 16 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 3072bdfe-a19a-3e0f-9ffc-0748b035840c | -6.69468 | -42.0392 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 11.4 |
| 73564705-3c0f-313d-9387-8ec657f27da0 | -3.38409 | -50.14925 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 77da78b9-5513-32dd-bdf0-cc3c67945a8b | -6.69277 | -42.05334 | 2025-10-28 05:01:00 | NOAA-20 | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 6.0 |
| 0665592c-849b-39ca-9c2b-672df0735bea | -3.04684 | -53.01662 | 2025-10-28 05:01:00 | NOAA-20 | MEDICILÂNDIA | PARÁ | Brasil | 1504455 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 254d3719-ae2b-3b8f-990d-f665fbcabe86 | -1.43662 | -52.86596 | 2025-10-28 05:01:00 | NOAA-20 | ALMEIRIM | PARÁ | Brasil | 1500503 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8da0098c-c9ad-3cc0-b624-572220361996 | -3.9136 | -43.3253 | 2025-10-28 05:01:00 | NOAA-20 | CHAPADINHA | MARANHÃO | Brasil | 2103208 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| d5d4176f-3b90-32fc-b3ba-456b525446df | -3.4667 | -49.97003 | 2025-10-28 05:01:00 | NOAA-20 | PACAJÁ | PARÁ | Brasil | 1505486 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README75.md)
