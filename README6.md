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

## Dados Diários - Página 6

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 1d42906b-2565-34ed-a78f-5a36b084b60b | -23.18769 | -47.10823 | 2025-05-26 04:23:00 | NOAA-21 | ITUPEVA | SÃO PAULO | Brasil | 3524006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| 558bdd19-dceb-3bc7-9db1-b1f15a4672bc | -22.7171 | -47.37389 | 2025-05-26 04:23:00 | NOAA-21 | SANTA BÁRBARA D'OESTE | SÃO PAULO | Brasil | 3545803 | 35 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 82946f71-8ff2-3214-b7d4-45ca5e248766 | -21.27499 | -45.40575 | 2025-05-26 04:23:00 | NOAA-21 | COQUEIRAL | MINAS GERAIS | Brasil | 3118700 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| f2af2a7a-6a7d-35a2-9bc4-e4097a6e629e | -23.58994 | -47.38543 | 2025-05-26 04:23:00 | NOAA-21 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.3 |
| cb9fd6ed-75cf-39c3-9ea9-4887321fdd3e | -21.27794 | -48.61554 | 2025-05-26 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| 90540838-f648-3470-b891-a91ae386008a | -20.76541 | -46.77126 | 2025-05-26 04:23:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.8 |
| c11cf371-a2e0-3253-a5f8-042bda8cfbdc | -19.71336 | -54.61676 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 576ab92e-648f-31e1-a374-f1cdf47fd036 | -19.87568 | -54.3636 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 05d2f873-a909-3ee5-9dc7-e8ced9457b40 | -23.98236 | -48.9445 | 2025-05-26 04:23:00 | NOAA-21 | ITAPEVA | SÃO PAULO | Brasil | 3522406 | 35 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 08b2bddb-2cdf-3efd-bf52-8ea6a1376979 | -19.71415 | -54.61313 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 122b170d-55e6-3107-8364-3d8a729897d5 | -22.7849 | -43.7572 | 2025-05-26 04:23:00 | NOAA-21 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 40e61b28-feaf-3557-866f-61f9ec4a50f3 | -19.33677 | -47.54458 | 2025-05-26 04:23:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4430e417-6b11-3d12-9dc6-3d381ecb6914 | -19.2739 | -47.61974 | 2025-05-26 04:23:00 | NOAA-21 | SANTA JULIANA | MINAS GERAIS | Brasil | 3157708 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 1dd4848f-6a40-3cf6-8413-7e8745bb0de5 | -21.27464 | -48.61495 | 2025-05-26 04:23:00 | NOAA-21 | MONTE ALTO | SÃO PAULO | Brasil | 3531308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.5 |
| 8da05020-4ed8-3ee2-bf53-d1345535f213 | -20.41663 | -43.55396 | 2025-05-26 04:23:00 | NOAA-21 | OURO PRETO | MINAS GERAIS | Brasil | 3146107 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 7fd198d8-c136-3a37-a910-e0562d332a8a | -18.14648 | -47.80141 | 2025-05-26 04:23:00 | NOAA-21 | OUVIDOR | GOIÁS | Brasil | 5215504 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 70645a9b-6d80-3745-b4e3-8af1c65e974e | -23.40747 | -46.55785 | 2025-05-26 04:23:00 | NOAA-21 | SÃO PAULO | SÃO PAULO | Brasil | 3550308 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| d05fa3db-90d7-3e33-b3c3-34b6f444994e | -19.87251 | -54.36629 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 9.2 |
| 6a3944a7-4092-3675-9a94-c28e767435a0 | -20.58102 | -44.57547 | 2025-05-26 04:23:00 | NOAA-21 | PASSA TEMPO | MINAS GERAIS | Brasil | 3147709 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.5 |
| 70bc73ae-0cb7-3079-8025-ba597bdb52f4 | -19.87482 | -54.36808 | 2025-05-26 04:23:00 | NOAA-21 | BANDEIRANTES | MATO GROSSO DO SUL | Brasil | 5001508 | 50 | 33 | nan | nan | nan | Cerrado | 10.9 |
| 606a68fb-d8a6-362e-9d01-f7eefab1f088 | -19.45423 | -45.30628 | 2025-05-26 04:23:00 | NOAA-21 | MARTINHO CAMPOS | MINAS GERAIS | Brasil | 3140506 | 31 | 33 | nan | nan | nan | Cerrado | 0.9 |
| c3e69eef-5ca4-33e6-94e6-3b4b34b89904 | -20.6041 | -47.54999 | 2025-05-26 04:23:00 | NOAA-21 | RESTINGA | SÃO PAULO | Brasil | 3542701 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 200e7c48-9908-3021-972b-308519cd0d5f | -19.96938 | -44.21754 | 2025-05-26 04:23:00 | NOAA-21 | BETIM | MINAS GERAIS | Brasil | 3106705 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 67111e48-3674-32c8-8bfb-1d47805a86e4 | -24.24362 | -50.7401 | 2025-05-26 04:25:00 | NOAA-21 | ORTIGUEIRA | PARANÁ | Brasil | 4117305 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| b5fcb5c6-88d1-3e3b-9a75-088f598c9255 | -28.58789 | -49.44316 | 2025-05-26 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| f74acc11-e987-3ae7-9fe8-71ac723d6f60 | -28.58457 | -49.44252 | 2025-05-26 04:25:00 | NOAA-21 | SIDERÓPOLIS | SANTA CATARINA | Brasil | 4217600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 747ecc25-4432-3ca6-84ef-5b3fb76578c1 | -8.0123 | -43.1984 | 2025-05-26 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 109.3 |
| 795083bf-638e-39a7-a3dc-b7d3670ba397 | -6.5631 | -51.1126 | 2025-05-26 04:30:00 | GOES-19 | OURILÂNDIA DO NORTE | PARÁ | Brasil | 1505437 | 15 | 33 | nan | nan | nan | Amazônia | 49.0 |
| f4ae5427-7f2e-3d05-9e71-e124ac8a9693 | -8.0312 | -43.1964 | 2025-05-26 04:30:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 141.0 |
| 7a110213-ecc0-3dcd-81b5-292444fb8ece | -8.0123 | -43.1984 | 2025-05-26 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 64.4 |
| de95d1b3-26c3-32e8-ac62-e2c8b7476daf | -8.0312 | -43.1964 | 2025-05-26 04:40:00 | GOES-19 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 154.5 |
| 8a36935f-5b86-3c0f-802a-3ce6ecfabf8f | -8.0218 | -43.19421 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| 50c3af21-63d0-353a-9d83-d4da09f100d8 | -4.29183 | -48.27496 | 2025-05-26 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| df5733d5-d0cb-38c1-85d2-a03ae9ba925f | -7.63754 | -46.11611 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4f9e53c3-5319-31e6-8f0f-790b2da88ed5 | -8.4456 | -49.6285 | 2025-05-26 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7a8576c8-b207-31cf-a072-65330017e4ca | -8.07116 | -43.13465 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 7.1 |
| 94ab25c3-a3a4-3f72-b631-53cc9181bd86 | -3.26572 | -54.23134 | 2025-05-26 04:46:00 | NPP-375D | URUARÁ | PARÁ | Brasil | 1508159 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| c4e5b1c6-6f1e-3ad3-ad6d-42d8ff813999 | -7.60112 | -46.28199 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e552d78b-1699-38ec-b084-c29afb80431d | -7.68131 | -46.10398 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 2de2ee92-bc03-3587-ad05-7a37a1249705 | -7.59513 | -43.37925 | 2025-05-26 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1677a88e-e928-312a-9cb4-9aa7e202606a | -8.02765 | -43.18903 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 299b0aff-0f8e-3c84-aeea-ca35ca5f1e50 | -7.35782 | -43.69024 | 2025-05-26 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 1febb6a8-6407-315f-a0aa-ab2f46a92856 | -8.44503 | -49.63225 | 2025-05-26 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 8d5dae5a-d77f-38dd-bcf0-df92682eb4b3 | -8.07236 | -43.12591 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.4 |
| be92299d-9a93-31ed-ae0b-dce417fbccea | -6.30621 | -46.05645 | 2025-05-26 04:46:00 | NPP-375D | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 370af2c5-9891-3d1e-afdf-3693cdc9bcf2 | -7.353 | -43.6895 | 2025-05-26 04:46:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| dad24255-9d50-3eb8-9ff3-55a7611c091a | -5.79714 | -46.30476 | 2025-05-26 04:46:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| eb0a2d05-47d8-30d4-8871-3b8af7b78a09 | -8.02687 | -43.19479 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| d260f954-e35f-3f5f-81d9-6209b3cc2d7c | -8.03192 | -43.19546 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| e2e0d691-c5b6-3ad7-a7bf-fe956c17aff6 | -8.02357 | -43.1938 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| fbfc14aa-c62c-3163-bfac-3fdfb8c44030 | -7.59435 | -43.38488 | 2025-05-26 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| f2bb6fdb-c975-3200-ac02-15e732b5c45e | -8.03271 | -43.18967 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 26.6 |
| 0b67f4a1-54ee-332b-abca-97513a8a6d82 | -8.02258 | -43.18847 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 4.1 |
| b2a90f91-d480-3818-ac7a-f81539654f13 | -7.63701 | -46.11977 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 63e25017-7ab5-3a16-ab64-b3a383720a0a | -8.02439 | -43.18807 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 01ad66f6-9eed-348d-9ec2-6387d431b9dc | -8.02781 | -43.20015 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 917b9d19-ad07-3d12-a86a-6e77e83ea980 | -7.47437 | -43.37271 | 2025-05-26 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ec170bc0-1ad0-3da2-9190-84eb7de8c713 | -7.54667 | -45.82491 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 36c32257-251b-3a29-b1b2-2738fcb10652 | -8.0185 | -43.19326 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| cab90799-aaaa-3ce7-9469-58e263b975ce | -8.02864 | -43.19437 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| b1103e69-937f-3c72-95af-cbc5e50775c2 | -7.91299 | -44.47538 | 2025-05-26 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 77bf9bff-b743-383b-a17b-e46a89358336 | -8.02316 | -43.1841 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 9fc259e6-05a0-33a3-98aa-83c77848dde5 | -8.02275 | -43.19955 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 48.6 |
| 125ffd74-87a1-3e26-8b68-894462bda74e | -4.28893 | -48.2706 | 2025-05-26 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| d8f5cefb-a97c-39c0-b1e0-ac50732da35f | -7.68077 | -46.10765 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| d714b42b-9c6a-3b84-a6e8-e0d56ffdebe7 | -8.02355 | -43.18119 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 4b381059-dbaa-3233-9197-912b97e76e99 | -8.44159 | -49.63169 | 2025-05-26 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 3b19e83a-e282-3666-895c-ecb763958e48 | -8.07195 | -43.12886 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| f0a9358b-aabd-3d0b-b1a0-f38e7248300e | -8.07155 | -43.13176 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 8.5 |
| 48ca8922-206e-35ee-a806-8bb50847b467 | -8.11998 | -45.89739 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e53e058b-e769-39e1-a9d6-4d6cc71921c9 | -8.02103 | -43.19995 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 77b5fbda-5cc0-39fe-a74a-04e0f754a1fa | -8.02521 | -43.18228 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 0ae7fbc3-4f14-359c-ade8-74df286e810e | -7.48007 | -43.36794 | 2025-05-26 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4290ac63-1b44-3e5f-8da4-e1a48c10c3dd | -7.64165 | -46.11672 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 86425ee9-25d0-3282-be2a-2fc9cb18e4e4 | -8.36596 | -47.0822 | 2025-05-26 04:46:00 | NPP-375D | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 8921c95f-dd11-3a97-a405-262e5526167d | -8.44216 | -49.62794 | 2025-05-26 04:46:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 653eb576-13f6-300f-84e6-2664b9552211 | -4.29242 | -48.27113 | 2025-05-26 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 15b5c38b-cedb-3921-995e-2c0f8731290e | -7.54611 | -45.82886 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| d56d3a5d-8be7-3e0d-a9ed-682461744a5c | -7.06594 | -44.92542 | 2025-05-26 04:46:00 | NPP-375D | SÃO FÉLIX DE BALSAS | MARANHÃO | Brasil | 2110807 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 8e8ffcc2-8880-3e36-aa91-c27c263f0a9e | -7.47513 | -43.36717 | 2025-05-26 04:46:00 | NPP-375D | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 861e766b-bad6-3497-9f44-5c3ad784d4cd | -7.60162 | -46.27847 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 39def1b7-61c5-3239-a401-4119fa48824e | -7.90838 | -44.47469 | 2025-05-26 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 2b5b1fee-b974-32db-87dc-c767381610ca | -7.54249 | -45.82425 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 20bff33e-eeac-3e42-90ae-44e2e06f01e5 | -4.28834 | -48.27442 | 2025-05-26 04:46:00 | NPP-375D | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 669daf21-8b84-3fda-aaac-c73b49c08a5e | -8.11523 | -45.90062 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 0a183705-3a96-3e65-bb6e-9031867ca60a | -5.68471 | -44.12437 | 2025-05-26 04:46:00 | NPP-375D | FORTUNA | MARANHÃO | Brasil | 2104206 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 3929ba60-14c2-376e-8820-bf18112d343a | -7.54193 | -45.8282 | 2025-05-26 04:46:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 90b1fae8-bd37-36fe-b071-9389bcbda39c | -7.91232 | -44.48008 | 2025-05-26 04:46:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 839f532a-bc6b-353c-bbbe-efb72c35e75e | -8.02609 | -43.20057 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 102.4 |
| d3855e9e-6459-3adf-aa23-8bc5fac33715 | -8.02946 | -43.18863 | 2025-05-26 04:46:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| f56d22cd-04c7-39b6-bffd-4a5f5d516747 | -11.91912 | -54.41436 | 2025-05-26 04:49:00 | NPP-375D | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| c56d13df-9410-3c12-bbf2-dfdc7ffe9e96 | -14.04557 | -55.1374 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 288f8d56-fe2e-3a61-a422-59eec78ea792 | -14.68029 | -48.1015 | 2025-05-26 04:49:00 | NPP-375D | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 97c1e662-b959-3fcf-9e48-b349c97fb8d6 | -14.03927 | -55.13221 | 2025-05-26 04:49:00 | NPP-375D | SANTA RITA DO TRIVELATO | MATO GROSSO | Brasil | 5107768 | 51 | 33 | nan | nan | nan | Cerrado | 3.0 |
| da652fcb-e9d4-3eee-8e10-9460c605722d | -11.86967 | -52.25323 | 2025-05-26 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 899d4064-0dee-3455-8464-1c9d320aac12 | -11.86856 | -52.2603 | 2025-05-26 04:49:00 | NPP-375D | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| d703cb71-7f8b-3a60-bbe1-e744b079ee84 | -9.18665 | -49.63807 | 2025-05-26 04:49:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d56b1ec3-b4c0-34b6-9947-b4207dcc3b12 | -10.45669 | -47.94055 | 2025-05-26 04:49:00 | NPP-375D | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 801f1e6c-162a-310c-b208-97865ad7e425 | -10.64585 | -46.96292 | 2025-05-26 04:49:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 97b53eed-5bcd-375c-9a11-3be91e8cd80b | -11.36983 | -55.1178 | 2025-05-26 04:49:00 | NPP-375D | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |


[Clique aqui para ver as próximas entradas](README7.md)
