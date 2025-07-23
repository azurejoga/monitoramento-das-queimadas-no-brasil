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
| 20ea88c5-ffbf-3727-9531-6dbe53d37aba | -3.87007 | -54.23252 | 2025-07-23 04:57:00 | NPP-375D | PLACAS | PARÁ | Brasil | 1505650 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 837aef9e-5f24-3be1-8f34-989687f5e862 | -2.45967 | -48.15283 | 2025-07-23 04:57:00 | NPP-375D | TOMÉ-AÇU | PARÁ | Brasil | 1508001 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| cabef439-0bd7-3408-9a37-393554ea3730 | -0.746 | -47.75464 | 2025-07-23 04:57:00 | NPP-375D | MARAPANIM | PARÁ | Brasil | 1504406 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 18ac49ab-d1ea-3550-a574-e46480a51437 | -8.08765 | -50.08373 | 2025-07-23 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 3.7 |
| c3a02d37-9377-319e-9dd9-8559cdcf3068 | -7.07282 | -55.4136 | 2025-07-23 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 03072bba-594d-345c-8e3a-6272ebf7a5e8 | -7.27407 | -44.36612 | 2025-07-23 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 809fe0f5-052f-3265-b36c-d8961c716093 | -8.95871 | -62.21349 | 2025-07-23 04:59:00 | NPP-375D | MACHADINHO D'OESTE | RONDÔNIA | Brasil | 1100130 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 253db7b3-3751-3a26-938b-88dd2942edea | -7.75687 | -44.03006 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 56e64fb2-9b77-3052-ae13-aa69b889614f | -7.14471 | -46.0981 | 2025-07-23 04:59:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 7.0 |
| 7c0c3256-4726-3953-8e36-6a5876022871 | -10.64172 | -45.23162 | 2025-07-23 04:59:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 063ee697-137b-3968-8fcf-c268e42ab24c | -7.89673 | -45.55983 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ad6b6109-69e3-330c-8316-55e996669464 | -9.76676 | -48.57867 | 2025-07-23 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| a0f8cd34-8945-34ba-89cc-c8b1bc950d0b | -6.56147 | -45.61712 | 2025-07-23 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 5133b2be-afe7-350a-9c55-bf94572decfa | -6.96527 | -44.37832 | 2025-07-23 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| f9e9b536-3961-3127-8b13-c4e66d72c156 | -7.07142 | -55.4131 | 2025-07-23 04:59:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 945e6675-a648-3d40-8161-8d55f2971a5d | -7.27591 | -60.17684 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| e846a52e-47b5-347d-8a88-4b1229fe22eb | -6.55298 | -56.24785 | 2025-07-23 04:59:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| b852848a-568c-3a79-bbc8-6b6fc8ea6fc9 | -9.74466 | -48.57574 | 2025-07-23 04:59:00 | NPP-375D | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 285598d6-e0ac-3304-a54d-b11d729a7889 | -11.81156 | -44.27048 | 2025-07-23 04:59:00 | NPP-375D | COTEGIPE | BAHIA | Brasil | 2909406 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8d572a89-fd25-3cd3-ac7d-0a6fca2994d3 | -7.04654 | -45.84969 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ae70d60e-1b1d-3b5b-b86a-01df89a04a41 | -6.97577 | -42.79115 | 2025-07-23 04:59:00 | NPP-375D | NAZARÉ DO PIAUÍ | PIAUÍ | Brasil | 2206704 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| ee69bbbc-e384-3a53-a1b4-bb8f3f719d70 | -10.05957 | -46.83072 | 2025-07-23 04:59:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd0afec4-ac03-3cb1-a64d-167b90e92f09 | -6.9348 | -44.30668 | 2025-07-23 04:59:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| e90b6c1c-2180-3e34-82e4-8a8ff3081433 | -7.89328 | -45.5567 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 11dee682-c433-35aa-99ea-cb7b19072118 | -7.02658 | -45.84309 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 492521a7-45e3-3f63-85dd-6d9b2559e193 | -9.05376 | -45.06192 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| 2459b466-f12b-3a8c-99f9-53c51c3e6678 | -7.89142 | -45.55927 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fd67b181-ec83-3cf1-a2de-8b259f24f31d | -7.25369 | -60.18511 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 318b6010-4fce-391a-a2ab-6686a23e944d | -8.87424 | -49.03611 | 2025-07-23 04:59:00 | NPP-375D | GOIANORTE | TOCANTINS | Brasil | 1708304 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7eb07e69-efed-3504-bb73-42ee0b58558c | -5.92064 | -61.30516 | 2025-07-23 04:59:00 | NPP-375D | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9127e88b-1636-3ade-8206-c29f59353871 | -8.29452 | -44.96635 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 44e1557b-c4ef-36d1-8d22-a8d0f6073c3a | -7.25861 | -60.18184 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2c29e566-dde3-327c-a760-2c6cda159387 | -7.25755 | -60.18176 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 7acc66ae-0b90-37e6-8521-344538904094 | -9.05879 | -45.06667 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.4 |
| ef469b0f-8e81-36fa-ad13-4260dd3ad4a6 | -7.26673 | -60.17929 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 1b3609c1-e880-340a-825e-49e7ebcb2b9b | -7.94132 | -44.84909 | 2025-07-23 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| bed5977a-997e-3f21-a0e7-7714582af465 | -8.09399 | -50.09466 | 2025-07-23 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 1f55042a-6011-35a3-8635-404ffb09cb95 | -7.7527 | -44.01694 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| a8bd53fc-b6e0-3ef9-ad2c-93fe0e90eeb7 | -7.24876 | -60.18838 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| bab77eb9-306e-3787-acdd-d0cd040bd7b5 | -6.96474 | -44.38209 | 2025-07-23 04:59:00 | NPP-375D | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| bc2baf09-1b1d-355c-a691-a0375fbfc9e4 | -7.25407 | -44.30047 | 2025-07-23 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e23cd72a-18ac-3654-b0e1-f856d9381eda | -10.63098 | -45.22626 | 2025-07-23 04:59:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1063388e-460d-3c44-a518-bc5395bca245 | -7.91678 | -49.64511 | 2025-07-23 04:59:00 | NPP-375D | CONCEIÇÃO DO ARAGUAIA | PARÁ | Brasil | 1502707 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| d8716128-03f7-328d-93a0-9bc62c69ec62 | -7.2618 | -60.1825 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 12793c7b-d6cd-3ece-889c-8dd036d712e1 | -7.1998 | -48.23678 | 2025-07-23 04:59:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 2.0 |
| dc009bfb-a9f8-3e6a-bc8b-bd7da44e132e | -8.73483 | -49.48583 | 2025-07-23 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| b7dd1f59-4b6c-309d-bc45-e2808364501f | -8.2885 | -44.96933 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 0b3cc92e-df5f-3d6e-932a-d086ec9e3640 | -6.93018 | -44.2982 | 2025-07-23 04:59:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f4ec853c-de35-3030-9ec9-cb5dbe2f55f8 | -7.75326 | -44.01279 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| f6bec12c-0d56-3684-a548-554b10936cc1 | -7.2038 | -45.33198 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| afe6d9a1-5087-3dd2-afc7-2e8f20fd9fa3 | -5.87816 | -50.14851 | 2025-07-23 04:59:00 | NPP-375D | MARABÁ | PARÁ | Brasil | 1504208 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 13ad5db7-44bf-37d2-84ec-57a143e4c7a1 | -7.27167 | -60.17605 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.3 |
| fc87eb39-ab13-3815-afb6-ec0a81810e36 | -6.55634 | -45.61614 | 2025-07-23 04:59:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 9773ed20-22b1-31b9-a2f4-ec22e0efb074 | -9.11834 | -60.75054 | 2025-07-23 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 6.7 |
| c0d0c92a-807a-3f34-9c5a-1e7f7d5ebb34 | -7.22491 | -49.59626 | 2025-07-23 04:59:00 | NPP-375D | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 83d9c5bd-1019-38a6-8d1a-7dda2bd212ec | -9.05831 | -45.07036 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| 46373cff-90f7-35b1-ad3a-daa315b390c5 | -10.6422 | -45.2278 | 2025-07-23 04:59:00 | NPP-375D | CRISTALÂNDIA DO PIAUÍ | PIAUÍ | Brasil | 2203008 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 64006d30-ce99-3556-ab61-550d3ae8c22d | -10.06404 | -46.83158 | 2025-07-23 04:59:00 | NPP-375D | SÃO FÉLIX DO TOCANTINS | TOCANTINS | Brasil | 1720150 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 2cb8625c-cad5-3fc5-b04e-3636c14b2fac | -7.76323 | -44.02698 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb2ad543-45dc-3209-a601-04f9d7dec37a | -7.26286 | -60.18258 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 7cc284b8-3f18-31dc-97da-94fa0c3edb49 | -7.04739 | -45.84359 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| fe7b6d1d-4048-3798-97b8-c83e70ea5050 | -9.11405 | -60.7498 | 2025-07-23 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| a2151ec8-eead-393a-a7d8-64cc00a36871 | -7.89283 | -45.55994 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 34a635fa-43ae-3baf-98b1-16cb91b1d281 | -6.92963 | -44.30224 | 2025-07-23 04:59:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3323a5ba-9f7f-32db-a1f9-653375cb4f4f | -6.89034 | -45.2434 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| eba719db-56ea-37f7-b258-267994dc23f9 | -8.73074 | -49.48523 | 2025-07-23 04:59:00 | NPP-375D | ARAGUACEMA | TOCANTINS | Brasil | 1701903 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| e9db6e39-4805-3178-ac2d-e759e343e527 | -7.88798 | -45.55608 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 1d80994d-cd03-39bd-802e-4f5ebe873f33 | -9.05277 | -45.06953 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 5.5 |
| a39e1556-411e-3af0-bcc7-11d180baf063 | -7.47692 | -49.22796 | 2025-07-23 04:59:00 | NPP-375D | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.3 |
| d73a4764-a5a0-3212-9128-3be0c043b4f0 | -10.43252 | -54.37565 | 2025-07-23 04:59:00 | NPP-375D | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 83c33f06-b9b9-3276-a7fe-265e7dcfb091 | -10.88517 | -44.36704 | 2025-07-23 04:59:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| f711b700-14f1-3da7-977e-c7b62b7098a6 | -7.27098 | -60.18001 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 4f4b1896-2e29-3a36-917f-9aee92b57093 | -9.26423 | -48.55961 | 2025-07-23 04:59:00 | NPP-375D | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| e6856e66-6fa3-3a90-a86b-cbad352dc848 | -10.72967 | -49.52758 | 2025-07-23 04:59:00 | NPP-375D | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 245be427-6392-345b-9236-b0d19754e6ed | -6.27323 | -45.27606 | 2025-07-23 04:59:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| a1155010-fc71-3afe-bc9f-091c5cfcfad9 | -7.02024 | -45.85122 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e6ea1a97-dd17-3b10-9b8b-dfe15dec6682 | -9.23011 | -60.93036 | 2025-07-23 04:59:00 | NPP-375D | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 67d1dd61-ad77-3055-a635-482ccc58eafb | -6.9489 | -51.63905 | 2025-07-23 04:59:00 | NPP-375D | TUCUMÃ | PARÁ | Brasil | 1508084 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bf5abf1f-a882-3225-8f15-fe9c92f779b0 | -8.29518 | -44.96361 | 2025-07-23 04:59:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 03f46425-d778-3998-9c47-2471cdbf7b6f | -7.75159 | -44.02515 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.0 |
| 28af551c-4785-3c3a-ba26-eb32d7a3c5ea | -7.25685 | -60.18575 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 816cf17f-64b9-331f-9660-379da1529569 | -7.19846 | -45.33144 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 1ee0f991-c194-3f3c-8cb4-c47382c0bc07 | -6.88948 | -45.24964 | 2025-07-23 04:59:00 | NPP-375D | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 2bf08aed-6c4d-3dae-8816-336825278458 | -7.02616 | -45.84614 | 2025-07-23 04:59:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 653c7a29-3efa-3663-bcf3-c85682fa0652 | -9.06533 | -45.05989 | 2025-07-23 04:59:00 | NPP-375D | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 9cfeaa0f-4940-3a94-af4d-9c0c54d419c0 | -10.50253 | -44.88441 | 2025-07-23 04:59:00 | NPP-375D | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 52a6b9e5-e26f-380a-9eb2-308d70b48ca7 | -7.19313 | -45.33083 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d03b4ffa-5a71-38c6-8c8b-b22bce71afe4 | -7.88655 | -45.55534 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| c3ae1e6b-bbd3-3de5-b2dc-ec63a17b546f | -8.09472 | -50.08978 | 2025-07-23 04:59:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| a7bb4137-f28c-32f2-ae67-7576966c2954 | -9.13485 | -50.77886 | 2025-07-23 04:59:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 6fddc34f-efbe-3ca3-b46a-d600893a386b | -7.88752 | -45.55938 | 2025-07-23 04:59:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 58dd1b4b-5bcb-3804-bf0a-c29238705c88 | -7.27915 | -47.53494 | 2025-07-23 04:59:00 | NPP-375D | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 4.6 |
| a2c92728-be9a-3c0f-b039-8a08c812b0d1 | -6.06003 | -47.54737 | 2025-07-23 04:59:00 | NPP-375D | MAURILÂNDIA DO TOCANTINS | TOCANTINS | Brasil | 1712801 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| eb5a51df-248c-34bf-8497-4f6c4360e8f0 | -7.74691 | -44.01577 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 791e7ee1-6821-35e7-9091-d5d8c422af60 | -7.26111 | -60.18643 | 2025-07-23 04:59:00 | NPP-375D | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 1.1 |
| cfc1ef55-a83a-381e-8cc8-720deb7fbdcc | -7.19802 | -45.33469 | 2025-07-23 04:59:00 | NPP-375D | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 4.8 |
| 257d8c2e-cd60-3fbf-a586-6a3f33a68bbb | -7.94083 | -44.85269 | 2025-07-23 04:59:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d32f2fe6-a609-3adc-b6a9-f51e02064f9c | -7.73226 | -49.46258 | 2025-07-23 04:59:00 | NPP-375D | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 58aa93c0-b3a3-3a84-a1cd-181e3169ddb4 | -7.75796 | -44.02203 | 2025-07-23 04:59:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 52509527-9fa3-3ca9-b038-30ebef77b116 | -7.25973 | -44.30154 | 2025-07-23 04:59:00 | NPP-375D | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |


[Clique aqui para ver as próximas entradas](README16.md)
