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

## Dados Diários - Página 3

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 24600691-139c-3675-a28a-fc3bab3b5818 | -14.84641 | -52.03492 | 2025-04-11 04:14:00 | NOAA-20 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| f332ac9c-a303-318a-8a3a-fc52025ad257 | -16.55273 | -46.72966 | 2025-04-11 04:14:00 | NOAA-20 | UNAÍ | MINAS GERAIS | Brasil | 3170404 | 31 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a37eca9e-0726-3330-99d3-26f95fdeb1b9 | -21.07832 | -48.66635 | 2025-04-11 04:17:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 7d999aa5-7e90-372d-8f73-955ae4d2ca45 | -21.62769 | -43.4662 | 2025-04-11 04:17:00 | NOAA-20 | JUIZ DE FORA | MINAS GERAIS | Brasil | 3136702 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 69fe4718-4599-3cd0-b385-5793943e0122 | -22.90086 | -43.75803 | 2025-04-11 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 3e6e9ff2-3ead-34f6-972d-e0333683db06 | -22.47631 | -48.35927 | 2025-04-11 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 78086b55-ed8b-3664-af77-b5398106ad8e | -21.05103 | -55.99608 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 42c2f283-4ce9-328d-b4f3-98e73a82e228 | -21.24674 | -56.02645 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| ca3c6caf-d7e0-3650-9220-c73b7509ef83 | -22.9062 | -49.68923 | 2025-04-11 04:17:00 | NOAA-20 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.7 |
| cbab735f-593e-3180-9adc-15335c48a76a | -19.7682 | -48.93182 | 2025-04-11 04:17:00 | NOAA-20 | COMENDADOR GOMES | MINAS GERAIS | Brasil | 3116902 | 31 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 95b254e6-9aeb-3def-a6b4-0df70f78f784 | -22.78699 | -43.7574 | 2025-04-11 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 545ec253-febe-3379-9342-16eade8ecc85 | -21.04701 | -55.99186 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c1f79474-95f7-3637-b73d-689527beb39b | -22.31297 | -51.88904 | 2025-04-11 04:17:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.2 |
| c3cf5dc5-1a4c-38ca-8495-c178de897c27 | -29.77791 | -51.17472 | 2025-04-11 04:17:00 | NOAA-20 | SÃO LEOPOLDO | RIO GRANDE DO SUL | Brasil | 4318705 | 43 | 33 | nan | nan | nan | Pampa | 0.6 |
| d528f47e-e49a-3e78-8b3e-b73d4e3c2325 | -21.25931 | -56.01875 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 4289a610-a313-31ae-b3d1-55db58342b84 | -21.04654 | -55.99158 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| d4ffc276-7688-3152-ac56-bd2b0165d022 | -25.14197 | -52.79128 | 2025-04-11 04:17:00 | NOAA-20 | GUARANIAÇU | PARANÁ | Brasil | 4109302 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 55de3af0-019b-348f-a725-1531c0a3bc6d | -21.24603 | -56.02978 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 86ee3e0c-6da3-326b-8ac6-825f544f1889 | -21.05671 | -55.99769 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce81afc8-9516-3ea0-9cbb-319ae1d5d045 | -20.18889 | -51.16076 | 2025-04-11 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 4405ecfc-ee33-309f-9551-783a44f7636a | -21.25338 | -56.02093 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| c4dd6374-4827-3835-a20c-c8a7abe7da71 | -20.18495 | -51.16 | 2025-04-11 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 67354867-d362-39e6-a708-2a6da04eb947 | -21.25409 | -56.01762 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ac4c6922-82c4-3c71-8423-3d5291c7ffeb | -23.33776 | -46.77405 | 2025-04-11 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 001f3b21-756b-3aba-bc0d-08d66f1cae77 | -22.78586 | -43.75529 | 2025-04-11 04:17:00 | NOAA-20 | SEROPÉDICA | RIO DE JANEIRO | Brasil | 3305554 | 33 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| aff7f5ec-cb59-3804-a755-a402e585dac5 | -21.05623 | -55.99735 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 41c7486e-5b94-376d-abfd-9bdcb09e1456 | -20.19087 | -51.15025 | 2025-04-11 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 1.8 |
| ff4f0af3-da74-3e3a-ad77-d8c6aca4a8ad | -21.05222 | -55.99308 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 83120396-c708-30fb-bfd3-d48eb2f89588 | -21.07763 | -48.67035 | 2025-04-11 04:17:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 9.5 |
| cd548429-c7f4-3bff-b89e-8d7d622a1451 | -21.44199 | -57.13381 | 2025-04-11 04:17:00 | NOAA-20 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.9 |
| cc90e75c-afbb-37b0-8f50-98f152523e00 | -23.25685 | -47.39224 | 2025-04-11 04:17:00 | NOAA-20 | ITU | SÃO PAULO | Brasil | 3523909 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.4 |
| 525160e0-1744-3b2a-a89e-90abcfaf3cf1 | -21.35062 | -48.59739 | 2025-04-11 04:17:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 6617b880-6251-3845-a83f-27c2791cedfd | -22.90145 | -43.75366 | 2025-04-11 04:17:00 | NOAA-20 | RIO DE JANEIRO | RIO DE JANEIRO | Brasil | 3304557 | 33 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| 6e773b74-1363-3a98-88ff-7ed288aa83d5 | -21.05152 | -55.99638 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 0fae9c0f-7986-37b6-96aa-dd63ff535486 | -21.3513 | -48.59339 | 2025-04-11 04:17:00 | NOAA-20 | CÂNDIDO RODRIGUES | SÃO PAULO | Brasil | 3510104 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 9e9f5146-5d7f-3a64-9506-60776ef55080 | -22.47904 | -48.36378 | 2025-04-11 04:17:00 | NOAA-20 | DOIS CÓRREGOS | SÃO PAULO | Brasil | 3514106 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 46acfad9-2084-32cc-bd12-2da002a78102 | -23.33834 | -46.7703 | 2025-04-11 04:17:00 | NOAA-20 | CAIEIRAS | SÃO PAULO | Brasil | 3509007 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| 3b07abb4-513b-389a-b6fd-f8d8bed08436 | -21.25423 | -56.01593 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 75a958c0-83e3-3c98-a15a-0316705a8a0b | -20.18988 | -51.15548 | 2025-04-11 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 9fc21ec7-dce0-39a2-b0be-028b4e67cb60 | -21.2535 | -56.01924 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 5f2a6756-bf72-3e14-acc7-437fd77be576 | -21.05175 | -55.99279 | 2025-04-11 04:17:00 | NOAA-20 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 287b4b62-2206-3657-ad29-c2ae03d86b40 | -21.12954 | -47.80112 | 2025-04-11 04:17:00 | NOAA-20 | RIBEIRÃO PRETO | SÃO PAULO | Brasil | 3543402 | 35 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 3427f374-5f96-3d8f-8128-04e30be309bf | -20.76451 | -46.76791 | 2025-04-11 04:17:00 | NOAA-20 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 0.7 |
| 820a6bfb-771b-3acc-b21d-41b78d1700ba | -20.18595 | -51.15471 | 2025-04-11 04:17:00 | NOAA-20 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.5 |
| 9cdc3f15-58d6-33c6-90da-3ba05f7ec26b | -21.07487 | -48.6657 | 2025-04-11 04:17:00 | NOAA-20 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.7 |
| 630da3b2-1345-3e71-af2f-ad81704e3639 | -22.31175 | -51.88456 | 2025-04-11 04:17:00 | NOAA-20 | MIRANTE DO PARANAPANEMA | SÃO PAULO | Brasil | 3530201 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.1 |
| 607032b7-bb10-3a4e-9ab6-f392548f2125 | -23.59274 | -47.43774 | 2025-04-11 04:17:00 | NOAA-20 | VOTORANTIM | SÃO PAULO | Brasil | 3557006 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| cac03fa0-3d59-30d0-a8c9-1461c1c579a3 | -19.47901 | -55.44472 | 2025-04-11 04:17:00 | NOAA-20 | AQUIDAUANA | MATO GROSSO DO SUL | Brasil | 5001102 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 29959142-b5cb-38bb-b421-c41ed9a59094 | -26.86935 | -50.6818 | 2025-04-11 04:17:00 | NOAA-20 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.3 |
| dca9fe5b-f780-3079-97e4-383882438197 | -15.79826 | -43.56814 | 2025-04-11 04:40:00 | AQUA_M-M | JANAÚBA | MINAS GERAIS | Brasil | 3135100 | 31 | 33 | nan | nan | nan | Cerrado | 48.5 |
| dd96e40d-ec6a-3e6c-b151-4dcc9b232e2f | 4.9658 | -60.49854 | 2025-04-11 05:01:00 | NOAA-21 | UIRAMUTÃ | RORAIMA | Brasil | 1400704 | 14 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 6234bb8f-8a6c-3002-a9c1-8304378dd503 | -7.91852 | -61.5434 | 2025-04-11 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 061a1575-f359-3787-bc37-5d6530007ead | -10.23878 | -55.2105 | 2025-04-11 05:04:00 | NOAA-21 | NOVA GUARITA | MATO GROSSO | Brasil | 5108808 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c8932471-bfa5-34c8-b680-5a89609bdd21 | -7.91916 | -61.53961 | 2025-04-11 05:04:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| f79e6c69-a207-3450-855f-c11e5c727f2a | -6.66124 | -47.59945 | 2025-04-11 05:04:00 | NOAA-21 | PALMEIRAS DO TOCANTINS | TOCANTINS | Brasil | 1713809 | 17 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 2618d798-fd39-3dcd-9b42-2c7d6c0a3aca | -5.41277 | -49.08045 | 2025-04-11 05:04:00 | NOAA-21 | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1e765783-c0b1-34ab-be3d-cbc7c7dcde97 | -15.2493 | -47.4623 | 2025-04-11 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 0ab9c678-d584-3d33-b2ab-0a11490d00c7 | -13.05164 | -53.7162 | 2025-04-11 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3c11e08f-963b-3de3-86ed-df124ecf9554 | -15.24975 | -47.45823 | 2025-04-11 05:06:00 | NOAA-21 | FORMOSA | GOIÁS | Brasil | 5208004 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 04a26f12-2cf5-340c-9f8f-4294d74c7422 | -15.7852 | -57.37468 | 2025-04-11 05:06:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0c18eae5-ed7c-3ddb-83f5-49fbb35d3116 | -11.39705 | -52.95216 | 2025-04-11 05:06:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| c3341e1b-28ca-3473-bd8e-af7648d6f1d3 | -13.04796 | -53.71567 | 2025-04-11 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 7218f0a3-f497-3d0b-a652-132f28efb0a3 | -15.78906 | -57.37165 | 2025-04-11 05:06:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| ca67db9e-1241-3781-b01c-92d1a818c33a | -12.35204 | -54.51436 | 2025-04-11 05:06:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 38388bcd-0084-359d-8605-5f8d31671d1a | -13.04922 | -53.70679 | 2025-04-11 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| f3fb7be7-43c2-3345-931d-724d0c6071c3 | -15.78575 | -57.3711 | 2025-04-11 05:06:00 | NOAA-21 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a2a5c783-6112-390a-84c2-6dbe7a6ea702 | -14.8478 | -52.03397 | 2025-04-11 05:06:00 | NOAA-21 | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 9763e957-665f-35ed-968e-a121cebe1f4d | -13.04859 | -53.71124 | 2025-04-11 05:06:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| b157a966-e0e8-3cf4-9679-8896148f408d | -17.75644 | -56.30857 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| b03eeb32-a500-39a7-a25b-1ad5e2f37672 | -20.5857 | -56.03621 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b79b34ee-6876-392c-bea2-0121c896507a | -21.05356 | -55.99181 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 31c2cdce-2431-35eb-a8fb-1296a2c09cfe | -22.90998 | -49.69143 | 2025-04-11 05:08:00 | NOAA-21 | SANTA CRUZ DO RIO PARDO | SÃO PAULO | Brasil | 3546405 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.2 |
| d9d0e4a8-c77b-381f-8745-803c33d94e67 | -21.07686 | -48.66564 | 2025-04-11 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 4.1 |
| a18de0fd-a4e3-372f-a886-589ef74c2877 | -20.58223 | -56.04145 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1701ceed-ec5d-31b3-99c1-eeee69af2a0c | -20.19146 | -51.15323 | 2025-04-11 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| 0023d290-dde4-3dcf-a865-aa6cf3faf0a0 | -17.75301 | -56.30803 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 733e7f50-1133-3831-9987-b10e3edc6cc9 | -20.19084 | -51.1587 | 2025-04-11 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 4.2 |
| dcef4288-64a7-3251-8457-1b29cc7bf59d | -17.75988 | -56.30912 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 2.4 |
| 2c2b0293-97f2-3248-80d5-0ab65346f9c5 | -20.58284 | -56.03714 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 9a6cf403-636b-3bc0-85f0-1e566644d748 | -20.58512 | -56.04051 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c0d4c506-3885-35f4-8cae-d73b2b7b357d | -20.33537 | -48.30201 | 2025-04-11 05:08:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f62b081e-d1a1-375e-9bbf-59c231f3c7ab | -18.58821 | -55.94667 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.9 |
| 41add5f3-3856-3223-9b8b-820a6e61c3dc | -21.07647 | -48.66985 | 2025-04-11 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| 97a7ee39-1554-3475-aa56-2dfd00665195 | -20.5864 | -56.03769 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7ec14d9b-5929-35c7-8311-46c11342834a | -21.08211 | -48.67047 | 2025-04-11 05:08:00 | NOAA-21 | PIRANGI | SÃO PAULO | Brasil | 3539004 | 35 | 33 | nan | nan | nan | Mata Atlântica | 3.6 |
| ebd53c31-0e8a-3a20-a4ff-4c0eccf5911e | -20.76696 | -46.76989 | 2025-04-11 05:08:00 | NOAA-21 | ITAÚ DE MINAS | MINAS GERAIS | Brasil | 3133758 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 99d49427-bd5c-3526-9dd7-cd8923cd36f2 | -21.25021 | -56.02811 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 84f987f5-1c72-35ab-9119-216f6d1ce605 | -21.04997 | -55.99123 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 2.8 |
| fcec1cf4-204d-3704-982f-af3ea8fb13b2 | -21.05715 | -55.99237 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d9468108-c852-3530-9bc1-8da504203838 | -21.05655 | -55.99678 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5f3c160-65d1-3daa-b5e8-db64a350f858 | -20.33576 | -48.29787 | 2025-04-11 05:08:00 | NOAA-21 | GUAÍRA | SÃO PAULO | Brasil | 3517406 | 35 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e4fa4aec-e816-3cbe-a2ca-d45df38e4bb9 | -21.44293 | -57.13416 | 2025-04-11 05:08:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 586f148b-e65f-38e3-94ff-e798bed957fe | -17.76388 | -56.30577 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.5 |
| 19838e80-42a5-3bcd-8a74-98a696ea12fe | -21.25499 | -56.01989 | 2025-04-11 05:08:00 | NOAA-21 | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 1addb6f2-8d31-32f1-b87b-3e8b6d015711 | -20.18611 | -51.15798 | 2025-04-11 05:08:00 | NOAA-21 | APARECIDA DO TABOADO | MATO GROSSO DO SUL | Brasil | 5001003 | 50 | 33 | nan | nan | nan | Mata Atlântica | 5.8 |
| 871d9261-77cf-3178-b49a-71cb88891436 | -18.58763 | -55.95076 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| f132f1e9-66df-3e0c-9c7a-a77cf18f2d88 | -17.76332 | -56.30967 | 2025-04-11 05:08:00 | NOAA-21 | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 3.1 |
| 651dca26-72bf-3754-8ec6-d268cf851b46 | -20.58156 | -56.03996 | 2025-04-11 05:08:00 | NOAA-21 | ANASTÁCIO | MATO GROSSO DO SUL | Brasil | 5000708 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d32e80df-3b04-36fb-b72d-57ade13580c5 | -26.86993 | -50.68325 | 2025-04-11 05:10:00 | NOAA-21 | LEBON RÉGIS | SANTA CATARINA | Brasil | 4209706 | 42 | 33 | nan | nan | nan | Mata Atlântica | 1.4 |
| 37aa7136-717b-3b05-9562-36c74f9e7330 | -7.92068 | -61.54105 | 2025-04-11 05:29:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.6 |


[Clique aqui para ver as próximas entradas](README4.md)
