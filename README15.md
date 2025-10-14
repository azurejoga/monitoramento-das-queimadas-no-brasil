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
| 56bc099d-daf2-38b0-8a38-14c188f2d730 | -3.88947 | -44.91171 | 2025-10-14 04:04:00 | NPP-375D | CONCEIÇÃO DO LAGO-AÇU | MARANHÃO | Brasil | 2103554 | 21 | 33 | nan | nan | nan | Amazônia | 4.7 |
| 6c8b8fac-f5c3-3a1c-8e50-550cd15ba61e | -3.70072 | -43.21247 | 2025-10-14 04:04:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 715f7a7f-e1ca-3cc7-a8cc-6f1ad7e9b2d7 | -5.42424 | -41.34104 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9f9e322a-1f5b-3df6-ab91-76421da9e6b5 | -3.62516 | -41.62689 | 2025-10-14 04:04:00 | NPP-375D | COCAL | PIAUÍ | Brasil | 2202703 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 6faf359d-e249-3931-8c22-49dde7cb1ec9 | -3.67591 | -48.31033 | 2025-10-14 04:04:00 | NPP-375D | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8b9b10bf-b42e-3f8e-8e15-d1c458ebf3da | -7.67689 | -40.40824 | 2025-10-14 04:04:00 | NPP-375D | ARARIPINA | PERNAMBUCO | Brasil | 2601102 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 3543cb94-526c-3eb6-aab6-923a400c1d47 | -5.32441 | -41.54734 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| a8bc56ba-2170-384e-9e9f-42f2ee576f95 | -6.30036 | -42.98926 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| ad17ec7c-86d8-3a13-ab90-3e5f7455e53b | -3.0639 | -49.41056 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 70967e26-565f-3e6e-9eb5-601548cc46c2 | -7.25223 | -40.59098 | 2025-10-14 04:04:00 | NPP-375D | CALDEIRÃO GRANDE DO PIAUÍ | PIAUÍ | Brasil | 2202091 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 59feaa50-fe61-3f5b-8d73-fe2ae112cc43 | -6.18335 | -41.76587 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| d8bf5dbb-9f36-393e-8496-fa459799e7df | -5.24813 | -42.00675 | 2025-10-14 04:04:00 | NPP-375D | ALTO LONGÁ | PIAUÍ | Brasil | 2200301 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| b8ebef3e-3a08-30a2-a837-8ee5b316e30b | -5.31338 | -42.90592 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 9f5e02a0-3e1f-3a48-8dbc-855a8e18caf8 | -7.53492 | -42.70731 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 6a13a3ea-c855-36c8-97bf-4acddfd0f628 | -7.93741 | -44.11749 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 56d3a986-b1f6-3be2-ab20-7e846d4163ea | -5.5666 | -41.32231 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 3.2 |
| e6622202-9517-38ed-be94-2660d099154e | -2.68664 | -49.06844 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 44652f18-2806-326c-875c-3ed715b6870a | -7.67443 | -42.37838 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| bd0d0436-e0a3-3f18-a115-6a257c55c8c9 | -5.31405 | -42.90174 | 2025-10-14 04:04:00 | NPP-375D | TIMON | MARANHÃO | Brasil | 2112209 | 21 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 562533fc-1c32-3563-84ca-1a36b660bae0 | -2.88119 | -50.73338 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 91058e99-8fe4-33c2-b49a-fb5ec34d3952 | -5.86319 | -43.85278 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b8d2048f-1a1c-35e5-aa7d-9be9ab0e5e7e | -3.12744 | -50.21042 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 229153e0-f143-34f0-95ee-3d4eab3824d3 | -4.83673 | -41.62773 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 1794d57e-cbe3-325e-927d-c1ad2a370ffe | -4.38889 | -43.46861 | 2025-10-14 04:04:00 | NPP-375D | ALDEIAS ALTAS | MARANHÃO | Brasil | 2100303 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 22be85f1-20a9-3ca1-b70e-80073299a1cf | -5.38824 | -43.22095 | 2025-10-14 04:04:00 | NPP-375D | MATÕES | MARANHÃO | Brasil | 2106607 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 2ca2f9ab-bede-3185-89c6-17678c748f00 | -5.15165 | -46.06306 | 2025-10-14 04:04:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 1.1 |
| a9c6b3c3-e7c3-35ce-a7ff-5ca731eef204 | -7.49897 | -43.05675 | 2025-10-14 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 8d61a88d-27e9-3e29-bd5b-2adab2a2e821 | -7.68688 | -42.57196 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.3 |
| c92ce2b6-0623-34db-9dd9-5f1c032d606c | -2.44354 | -47.16456 | 2025-10-14 04:04:00 | NPP-375D | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 5.4 |
| 15091041-0439-3aaa-ba1f-c36759a0b5d3 | -3.7529 | -41.68248 | 2025-10-14 04:04:00 | NPP-375D | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | 0.9 |
| 0d328b2d-06e5-357a-bf6b-25c1781e510e | -7.55918 | -42.69125 | 2025-10-14 04:04:00 | NPP-375D | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9dca7044-1545-3935-8282-26a0c48efe8b | -7.07957 | -41.94961 | 2025-10-14 04:04:00 | NPP-375D | OEIRAS | PIAUÍ | Brasil | 2207009 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| f0c378bf-4937-3964-8bd9-886f65f80194 | -9.32863 | -40.87658 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |
| c71a25c2-e98f-303a-8e7f-6a685f28cd40 | -7.1604 | -42.18469 | 2025-10-14 04:04:00 | NPP-375D | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 4bcb5458-271e-305c-b0f8-b7407ee98eb4 | -7.31679 | -45.75616 | 2025-10-14 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 3c6f03e0-8c4d-3872-b282-f85b90d15933 | -5.01519 | -46.76666 | 2025-10-14 04:04:00 | NPP-375D | AMARANTE DO MARANHÃO | MARANHÃO | Brasil | 2100600 | 21 | 33 | nan | nan | nan | Amazônia | 6.1 |
| 8b9888bd-ba56-3aa8-8f8d-6f3640ee2038 | -3.27551 | -50.04537 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| f4d527ab-ac18-3bf9-8c98-95be0f5f23e3 | -1.95687 | -50.81267 | 2025-10-14 04:04:00 | NPP-375D | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | 4.3 |
| f2cad5a2-c17f-39dc-b124-1aab719e5041 | -7.43726 | -45.40532 | 2025-10-14 04:04:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| eef1d9fd-9b05-31c6-8536-0755c9cb318f | -6.22698 | -41.56136 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 77d3212a-98ee-328e-b3c9-b13810f1e965 | -5.54147 | -44.91048 | 2025-10-14 04:04:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 493e3be1-f44d-3785-87a1-79208a3a0159 | -6.56059 | -43.93584 | 2025-10-14 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5dbfa6aa-cc6a-39bb-81de-95eaf45188fa | -3.06396 | -49.40837 | 2025-10-14 04:04:00 | NPP-375D | MOJU | PARÁ | Brasil | 1504703 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 10a24613-31cb-317e-9cbe-f696f05e9874 | -3.70146 | -43.20794 | 2025-10-14 04:04:00 | NPP-375D | MATA ROMA | MARANHÃO | Brasil | 2106409 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| d54ac958-1904-3cad-ba15-97e33057784d | -5.83022 | -42.31456 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 2.3 |
| 9f631f96-4a91-345f-9596-8dbc18150b1c | -5.72124 | -45.27541 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 9856bd33-f427-3236-aca4-2a67e039cde8 | -6.15954 | -41.72061 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| b4409f90-471a-3603-afc5-4af7fd7b8239 | -0.90248 | -47.54889 | 2025-10-14 04:04:00 | NPP-375D | MARACANÃ | PARÁ | Brasil | 1504307 | 15 | 33 | nan | nan | nan | Amazônia | 5.2 |
| a518951b-f2ef-3125-a129-ab3cea6d9890 | -7.48699 | -44.63961 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3a638c5c-9ef0-37e5-a3fd-ead61d5c57f4 | -4.05469 | -47.25737 | 2025-10-14 04:04:00 | NPP-375D | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 8fc39b95-8c55-32b6-b4bb-0391037cc7c0 | -5.26782 | -41.00853 | 2025-10-14 04:04:00 | NPP-375D | BURITI DOS MONTES | PIAUÍ | Brasil | 2202026 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| adaafc81-919d-37a7-8fa4-e6b9a20ef9a7 | -6.42371 | -42.43788 | 2025-10-14 04:04:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 3.1 |
| 87442aa8-d217-3cdd-a559-11325c459338 | -5.94086 | -43.73217 | 2025-10-14 04:04:00 | NPP-375D | BURITI BRAVO | MARANHÃO | Brasil | 2102309 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e1a52881-2b5e-373b-9ef9-d689d08182f1 | -6.30508 | -46.93961 | 2025-10-14 04:04:00 | NPP-375D | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e68c8c02-d8d4-3c74-8bad-07d8b268f161 | -5.406 | -40.88437 | 2025-10-14 04:04:00 | NPP-375D | CRATEÚS | CEARÁ | Brasil | 2304103 | 23 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 3e721479-64c4-388e-aaf3-c434b3b86e09 | -9.51518 | -41.70284 | 2025-10-14 04:04:00 | NPP-375D | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 9008cde0-cecb-358c-bbcb-92ad1cd09966 | -4.28559 | -48.57275 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 05439b00-1ba8-348e-b12a-09a52a3fe1ec | -6.15472 | -41.76883 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 60c2b12d-fc9b-3cdf-a7d9-f4c0a4edc114 | -7.15094 | -42.51577 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO PIAUÍ | PIAUÍ | Brasil | 2209708 | 22 | 33 | nan | nan | nan | Caatinga | 6.1 |
| e6846a67-a93b-3e93-a719-ddd12397a253 | -6.16519 | -43.75507 | 2025-10-14 04:04:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb79f827-b88c-373c-b249-3341dbac2a81 | -7.76064 | -44.72736 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| be92de10-e5f6-30db-a275-09524d5d7a61 | -6.24179 | -41.55622 | 2025-10-14 04:04:00 | NPP-375D | PIMENTEIRAS | PIAUÍ | Brasil | 2208106 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 0b3637d2-8aee-3a31-8ca6-ca3462c5384a | -7.89816 | -45.00023 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| c18a12cf-deb2-3ae6-a63b-39d0bc2e171a | -5.4254 | -41.33384 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| efc1d657-cdc6-3eda-826e-efce32be7b9d | -4.66654 | -43.11971 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| f18b5159-46a4-3a64-b225-97015ee5934a | -7.91309 | -45.00792 | 2025-10-14 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7bee2ca4-b258-3a40-85a5-d4b85317280a | -6.29903 | -42.99733 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 8.6 |
| acd1ae6c-cfa2-3eed-a3aa-e6b57e90165f | -5.9758 | -43.56502 | 2025-10-14 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 99d67030-119d-37d0-82a0-2b292a7468d6 | -4.62319 | -45.78595 | 2025-10-14 04:04:00 | NPP-375D | MARAJÁ DO SENA | MARANHÃO | Brasil | 2106359 | 21 | 33 | nan | nan | nan | Amazônia | 1.5 |
| a6e542f6-4673-3ba7-ae71-8d1550145a9a | -6.15815 | -41.76941 | 2025-10-14 04:04:00 | NPP-375D | AROAZES | PIAUÍ | Brasil | 2200905 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 86344d2a-34b0-31b2-a81a-4b624919f2ac | -5.56603 | -41.3259 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DO TAPUIO | PIAUÍ | Brasil | 2210409 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 519f9cb0-b7ee-3d17-b9e3-e54ea09e88c2 | -7.49076 | -42.15174 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 9b32614a-2424-3d1b-8c3e-575a423018ea | -6.44254 | -41.82928 | 2025-10-14 04:04:00 | NPP-375D | VALENÇA DO PIAUÍ | PIAUÍ | Brasil | 2211308 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 9fe5a683-fe2a-3d04-ac2f-da65f8b8988f | -4.68801 | -43.12774 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| a5787d00-77b0-3960-aff7-e3cb086fe6f0 | -7.48732 | -42.15117 | 2025-10-14 04:04:00 | NPP-375D | SANTO INÁCIO DO PIAUÍ | PIAUÍ | Brasil | 2209500 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| e93c8e4a-d54c-39b2-95ef-b06f99f591b3 | -7.9494 | -44.11494 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.5 |
| 9ae6be2e-7b5c-3e22-a706-810e1a6aa968 | -7.24288 | -46.25377 | 2025-10-14 04:04:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| c4d2e8aa-0322-3584-a346-01c8c822e63a | -5.59578 | -42.57811 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 5fa77414-7ce5-3d63-8cd0-6d56c81f095b | -5.83987 | -42.23215 | 2025-10-14 04:04:00 | NPP-375D | SÃO MIGUEL DA BAIXA GRANDE | PIAUÍ | Brasil | 2210383 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 70e059cd-b551-3f9e-8d4e-16e6006167d5 | -6.29543 | -42.99669 | 2025-10-14 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 6.2 |
| e673b923-cdf7-377c-8932-10a77c1742ac | -5.10924 | -43.19835 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 9.9 |
| b60acad5-d474-33a0-949c-635e8faac378 | -4.42261 | -47.7567 | 2025-10-14 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| c042a7ef-c186-3202-9a78-c2d30135e8ab | -4.91527 | -41.5289 | 2025-10-14 04:04:00 | NPP-375D | JUAZEIRO DO PIAUÍ | PIAUÍ | Brasil | 2205516 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| 15c1f553-5bd5-3546-ab99-ed9590ed5054 | -4.2839 | -48.58252 | 2025-10-14 04:04:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| b6d0f852-d51b-3691-9564-be5e797f1320 | -7.95162 | -44.12456 | 2025-10-14 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 13.0 |
| 321d2c7a-e7b1-30ad-9f7a-bf160135cb58 | -7.5012 | -43.06541 | 2025-10-14 04:04:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.1 |
| 5ce1c2dd-7f72-3fd6-b1b5-93b1ced1eab7 | -6.40209 | -46.2447 | 2025-10-14 04:04:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 887c5ad3-5a07-303f-964b-0bd7dd4fac14 | -5.86652 | -42.88163 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 770d843c-6b0e-36c4-b67d-1e998d758e94 | -4.66881 | -43.12903 | 2025-10-14 04:04:00 | NPP-375D | CAXIAS | MARANHÃO | Brasil | 2103000 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 06a469d0-c4fe-3197-a66c-070fe86f36ed | -5.2176 | -41.64496 | 2025-10-14 04:04:00 | NPP-375D | CASTELO DO PIAUÍ | PIAUÍ | Brasil | 2202604 | 22 | 33 | nan | nan | nan | Caatinga | 1.8 |
| 6fc289ff-2e7f-38e6-a65d-9dae1a097e0b | -5.33303 | -45.19275 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 03fc36b3-1839-3687-a22f-06807992a9b7 | -4.86204 | -49.47373 | 2025-10-14 04:04:00 | NPP-375D | ITUPIRANGA | PARÁ | Brasil | 1503705 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f71a0314-592c-3745-ac95-b0fd97c08c94 | -5.87539 | -42.82819 | 2025-10-14 04:04:00 | NPP-375D | PALMEIRAIS | PIAUÍ | Brasil | 2207504 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 0cf7352a-56db-330f-bc6f-ad1ed910523c | -5.62491 | -42.57874 | 2025-10-14 04:04:00 | NPP-375D | MONSENHOR GIL | PIAUÍ | Brasil | 2206407 | 22 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 640fa2db-c58d-3f0c-b0b2-fcb5d6c4ac41 | -7.75981 | -44.73224 | 2025-10-14 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 10f15ed7-2400-3750-81d7-9616c54af551 | -4.0772 | -48.03722 | 2025-10-14 04:04:00 | NPP-375D | DOM ELISEU | PARÁ | Brasil | 1502939 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| cb839259-71db-3270-96a3-8c5d9db55ffe | -5.40683 | -46.01737 | 2025-10-14 04:04:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 8cdb9cfe-a75b-393e-8114-a51f42d329dd | -7.3992 | -39.79065 | 2025-10-14 04:04:00 | NPP-375D | EXU | PERNAMBUCO | Brasil | 2605301 | 26 | 33 | nan | nan | nan | Caatinga | 19.3 |
| 1f93bbe0-996b-3eac-b3a6-41049bb2b426 | -5.49102 | -45.41087 | 2025-10-14 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.7 |
| 6782d35a-4efe-30ad-86b3-0b3a20ed9723 | -7.32033 | -45.76073 | 2025-10-14 04:04:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |


[Clique aqui para ver as próximas entradas](README16.md)
