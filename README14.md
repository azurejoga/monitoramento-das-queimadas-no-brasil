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

## Dados Diários - Página 14

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| a87c16e3-dddb-3195-b1c6-37b67e23d719 | -12.50861 | -58.34798 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| cd6e5ea7-6cee-36c8-93ae-d65b5ffe7dc0 | -10.62135 | -47.85042 | 2025-06-21 04:34:00 | NOAA-21 | MONTE DO CARMO | TOCANTINS | Brasil | 1713601 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 283e59d4-8da2-37d1-a7eb-51e3794bed8e | -14.97076 | -46.26067 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1ae922b3-eac5-3b9e-96d5-c70cdb412119 | -11.94904 | -58.75029 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 677b141c-d871-37cb-82d3-e07be545c9e2 | -12.02419 | -57.09952 | 2025-06-21 04:34:00 | NOAA-21 | ITANHANGÁ | MATO GROSSO | Brasil | 5104542 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 8e7a22fe-0158-35ce-924b-ff469e990b44 | -11.06697 | -49.62261 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 3c7c476a-083a-3234-aebd-83d7a9d96384 | -12.57815 | -58.38397 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f7028125-5074-35db-aa45-609f56444dac | -12.29494 | -50.09888 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.3 |
| adf80dd2-01e7-3548-b4db-a2e6a3dea822 | -13.36903 | -54.25517 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 157f3bb8-4b85-39eb-ac63-e9f1f329dd81 | -12.26471 | -44.60363 | 2025-06-21 04:34:00 | NOAA-21 | CATOLÂNDIA | BAHIA | Brasil | 2907400 | 29 | 33 | nan | nan | nan | Cerrado | 4.5 |
| d38dd1b5-f6f2-3f07-93e0-8c7761f24d3c | -12.63758 | -44.32777 | 2025-06-21 04:34:00 | NOAA-21 | BAIANÓPOLIS | BAHIA | Brasil | 2902500 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| d08a72df-a5bb-37ce-b587-df2455e632e7 | -14.03127 | -53.36578 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c7d7f9d4-47b1-3e13-8d10-c615969b2673 | -14.0424 | -50.51753 | 2025-06-21 04:34:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 61374d93-1847-354d-9884-cf4e82ef8a3d | -7.97829 | -46.21538 | 2025-06-21 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 5adba8a5-0322-36dc-abb8-235a4d95dfec | -13.39181 | -48.44875 | 2025-06-21 04:34:00 | NOAA-21 | MINAÇU | GOIÁS | Brasil | 5213087 | 52 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 4ac558d1-5ad8-3319-8f5d-290c67d470fb | -14.0357 | -53.362 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 60ed22ab-078b-3172-90f1-4fc633b91b5e | -14.07457 | -53.37807 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.5 |
| d0297597-6342-3356-8c0d-886ec50b94a2 | -8.02569 | -47.66074 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 56fcde9e-92b3-3093-8147-2075898fe625 | -10.45657 | -47.03226 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 3dc78c27-7a8e-3642-a399-0f4a6b4b4715 | -11.32586 | -45.22726 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7701461a-e50d-3daa-8a10-88f2d2a05ae1 | -7.95625 | -49.27731 | 2025-06-21 04:34:00 | NOAA-21 | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 095f8964-19d4-3184-8c63-3a6aed6b75f8 | -12.47776 | -60.13877 | 2025-06-21 04:34:00 | NOAA-21 | VILHENA | RONDÔNIA | Brasil | 1100304 | 11 | 33 | nan | nan | nan | Amazônia | 5.9 |
| 11e5d0a0-d2e8-3385-9404-f544dd3e2b02 | -14.81145 | -48.47304 | 2025-06-21 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 16f90f25-177e-3b0f-8b86-a9c8777065f8 | -10.2986 | -57.14113 | 2025-06-21 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 3d09d306-9db3-35b9-8a5b-97da4605fb99 | -9.2568 | -57.5315 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| d2fa3474-aa44-3bc0-b98c-694ab392cd44 | -11.52729 | -56.9832 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| f3ab466a-06e7-3f55-b47e-1b2c6e8f8ca2 | -11.87654 | -54.67451 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| fcde6089-7ce2-3996-9f5f-d05b6945686f | -9.5749 | -46.74007 | 2025-06-21 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 8fc5a28d-56db-3af2-9e06-d01599065faa | -11.79478 | -57.24401 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 4.2 |
| 3ad3988a-f8f4-30a7-ace3-71b176b0ac7a | -13.6591 | -53.94118 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 86245c95-00df-3033-a1c2-9e6cce840c50 | -7.93634 | -47.82154 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 41cbce3a-66fa-3007-9a65-bbf977712530 | -10.52497 | -53.6201 | 2025-06-21 04:34:00 | NOAA-21 | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 7.9 |
| d8030e90-1afb-339b-a4ef-db7139288da2 | -8.01521 | -47.66267 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 6af4f3c1-cd98-31c3-827e-0396b126298b | -11.79582 | -57.2384 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 9da351f7-0214-3069-8514-140114813685 | -10.45998 | -47.03281 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 9c05f6ca-3d92-3fa6-8e7b-af65025221b8 | -10.54763 | -46.77641 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 4.2 |
| 7d494a01-5093-3cd5-890a-4be8b07fa9cd | -10.44697 | -47.04983 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 7d5c9f61-dbae-3960-8492-c2eea0bb3a2c | -9.01826 | -61.22636 | 2025-06-21 04:34:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| da5be002-807d-36e1-8c97-07402fab97e6 | -10.44864 | -47.03868 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| e6bb26e0-d07c-34c4-84b0-d40cf32f0665 | -9.25737 | -57.52835 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 13.9 |
| c843c5a5-bd29-3220-b961-831c0f787f58 | -7.80643 | -46.05423 | 2025-06-21 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| c039bbc3-044c-3550-9b9b-13483ed4f5f1 | -9.46991 | -57.84384 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 885b7753-6c67-3fa3-947e-fd243624b19e | -13.6553 | -53.9405 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| fbb72b9d-0587-3204-9db9-de0171d6c8b3 | -10.5107 | -47.57596 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 5c0438e6-a3a2-3a60-90d2-952f3edc2b3b | -11.95769 | -58.7631 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| 5d9b2997-96a4-3d15-bcfc-c83bb7f5d906 | -9.09564 | -50.02774 | 2025-06-21 04:34:00 | NOAA-21 | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| b5b6ca87-8c24-360a-a8bb-d18a5cd0c47d | -8.19922 | -47.77042 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 42040c61-e143-3d7a-b149-61f1af742ac1 | -9.4733 | -57.82978 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.5 |
| 3eb55ad6-e162-3264-be4a-6c7e8416384a | -11.88064 | -54.67526 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 12.2 |
| 231a6667-a593-3f9b-9044-931342875f8d | -9.47795 | -57.8342 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| ac3b2ce6-e301-37a8-bdc4-cebeefbc2f79 | -12.57484 | -58.37325 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2841653d-7672-321e-8e9f-3aadb3ee305f | -11.13781 | -53.9227 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7d792ada-65d1-3a92-ac1e-510d3d500234 | -11.9524 | -58.76168 | 2025-06-21 04:34:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 7.1 |
| b2c8c3c4-3f6e-30f7-9369-7086c8c8f279 | -9.26122 | -46.91607 | 2025-06-21 04:34:00 | NOAA-21 | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| fb01d388-4b21-3b35-8083-64d8fd8ddb2c | -11.57436 | -51.42514 | 2025-06-21 04:34:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d4026144-e928-3e33-bca2-2fabe38b14a7 | -9.45999 | -57.83855 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 0634ba11-9322-368e-b0fb-6f825e512aef | -12.28774 | -50.10135 | 2025-06-21 04:34:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| fb6a7c01-ce20-33d5-8165-7c5a46101d35 | -10.95447 | -44.54593 | 2025-06-21 04:34:00 | NOAA-21 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| c5eeaaba-4cc1-312c-8f4f-e4129912bbce | -9.4789 | -57.82501 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| f5144472-df22-300b-8e00-bb30595f6c67 | -11.33023 | -45.22327 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1a9be14f-b79a-35c3-b622-3b60b94885cd | -9.47271 | -57.83306 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| bf5a3ef5-77ad-3998-af1b-0a7c090e683d | -12.50948 | -58.35078 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| ad359b7f-6458-3d40-9955-fdc6c0abc652 | -11.53406 | -56.97343 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 78dc51ec-9901-3ffe-9904-029ee832666f | -9.25159 | -57.53066 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 7.2 |
| 76c1fbc8-80c6-392c-9896-22bcc651c69c | -13.04492 | -53.71189 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 4.4 |
| b8e066c3-5541-3140-a3f6-69bec3a78085 | -11.87784 | -54.66702 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 31.1 |
| 2d009828-f2c9-31ad-83bd-ff450e684b3d | -11.94076 | -48.42522 | 2025-06-21 04:34:00 | NOAA-21 | PEIXE | TOCANTINS | Brasil | 1716604 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 92a59824-dcd4-31ce-b114-2f0c9471374a | -8.37844 | -46.97925 | 2025-06-21 04:34:00 | NOAA-21 | CAMPOS LINDOS | TOCANTINS | Brasil | 1703842 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6ca59995-8b4f-31b6-8144-ac879c57530b | -14.97124 | -46.26338 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0eab022d-e886-33ad-87a3-847302cded06 | -14.96756 | -46.26277 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 9f518ba2-b5a5-3fee-b4e0-76583d894f50 | -11.78993 | -57.24301 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 31.3 |
| ce44856a-d898-3dd7-bed1-4677120a88d6 | -10.52022 | -47.58112 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 995aae06-a301-3386-9c7d-e24323ae9127 | -11.8718 | -54.67752 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| ea766ae4-f5d1-3c70-a14c-2dd60b4f1847 | -13.65604 | -53.94217 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e0535282-34a1-3035-be07-b7e7e16474ff | -14.97015 | -46.26519 | 2025-06-21 04:34:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.1 |
| ed1b5059-6972-37ee-8dbd-9ddd31f774c0 | -12.16706 | -48.67832 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| b2e700a8-9e07-3ac8-aa1b-c676d08b4436 | -11.78611 | -57.23649 | 2025-06-21 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 36.1 |
| af1fb81f-f99b-390f-828d-ebca336b6e3b | -12.50922 | -58.34475 | 2025-06-21 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 40a66028-87e6-3389-a7cb-1637878d7d68 | -12.16265 | -48.68485 | 2025-06-21 04:34:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| b19ee1da-1da3-3b59-9745-0a9808dfb110 | -9.47516 | -57.84496 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| 1291e1ec-8256-337f-9a35-c44b1cc21f79 | -11.07933 | -55.05187 | 2025-06-21 04:34:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 0e58401e-ac58-3d4c-95f3-6bcd2a1d06f8 | -13.04113 | -53.71122 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| 0a39918a-8e6e-3ff8-93af-c0876f1937ca | -12.07614 | -44.97632 | 2025-06-21 04:34:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b5e6306-34f5-3e73-8255-881a16331c8c | -10.52747 | -47.57859 | 2025-06-21 04:34:00 | NOAA-21 | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 0937b544-88b6-3a5c-8b63-a2ad7766eb91 | -14.02684 | -53.36959 | 2025-06-21 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| e0d94f81-d77c-32f8-b616-998e1ca05e1f | -11.8731 | -54.67002 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.7 |
| 13ac8d1a-f266-32cb-9c60-88706cd986aa | -13.04062 | -53.71741 | 2025-06-21 04:34:00 | NOAA-21 | GAÚCHA DO NORTE | MATO GROSSO | Brasil | 5103858 | 51 | 33 | nan | nan | nan | Amazônia | 9.2 |
| a9d6e40a-8163-38b7-94c4-a68a32e4a8ec | -9.46928 | -57.8472 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| 63305cad-b40d-36e5-92f5-7ed46f90b485 | -10.2385 | -46.80335 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 7f93a77f-ca93-3d38-9fb7-e071a2341506 | -11.57773 | -54.5631 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 03029b9f-a3ba-34bb-b899-b97cf1beb5e3 | -10.44184 | -47.0376 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 57011815-5ca3-3fcb-8c1a-8fc8d03c231a | -11.14177 | -53.92336 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| fc6d79e4-7b99-316b-a998-233c51903721 | -11.87245 | -54.67377 | 2025-06-21 04:34:00 | NOAA-21 | SANTA CARMEM | MATO GROSSO | Brasil | 5107248 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 690dde7f-5756-346a-aa27-2f31615eb4ac | -11.86892 | -52.25206 | 2025-06-21 04:34:00 | NOAA-21 | QUERÊNCIA | MATO GROSSO | Brasil | 5107065 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 770e5c65-7b78-3f59-a8d4-70be5f110092 | -10.54075 | -46.77534 | 2025-06-21 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 602053e4-7a72-3d06-b9bb-1aecde9e2056 | -11.573 | -54.56608 | 2025-06-21 04:34:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 0d5778ab-bc97-3b38-9554-97ba49640b10 | -9.47212 | -57.83633 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 3.7 |
| 63aed529-0e07-3db3-a66e-40b0b54e5db1 | -9.47578 | -57.84163 | 2025-06-21 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| d9c42696-7b1f-3918-85c2-6560cb43b390 | -10.86253 | -53.76677 | 2025-06-21 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 85791a37-b3b0-3fcd-a590-5c02004cd134 | -8.02237 | -47.66022 | 2025-06-21 04:34:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |


[Clique aqui para ver as próximas entradas](README15.md)
