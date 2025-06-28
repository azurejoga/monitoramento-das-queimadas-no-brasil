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

## Dados Diários - Página 28

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 2988d0f1-3582-3246-a2b5-2dae5ccb4d5e | -11.88625 | -58.73315 | 2025-06-28 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b0f2b26-6186-3125-8775-0ccd101f0719 | -9.70394 | -56.18203 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| f0c1c97b-102c-3fea-ac60-917f27c3f719 | -11.05844 | -55.37688 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| a295f4ac-8a14-3a91-ba40-3cc16ab28c5c | -9.70025 | -56.18316 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 3ff7b73c-4398-3e3a-aef3-c8bd97d40bbe | -13.29691 | -57.09004 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 86cc2de5-66f4-31c7-ad8e-1512f39e1edb | -9.13465 | -63.91525 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 0546fd7e-e30a-3ad1-b4ef-b6a4a74232e9 | -9.17271 | -61.40632 | 2025-06-28 05:44:00 | NOAA-21 | COLNIZA | MATO GROSSO | Brasil | 5103254 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 7e845e04-f46b-3ba0-b998-2159219f3ae4 | -11.04946 | -55.38467 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 10c4f78c-0117-3fa3-bf5b-e4e50ef3f124 | -10.05715 | -59.35822 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 8d3546f9-4209-311f-b7de-972efa132672 | -11.26637 | -52.75428 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 12.5 |
| 46a15bc7-13b3-3853-b90b-5155ef725f2c | -11.04978 | -55.07268 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| e46d03d7-1b74-3a68-a855-356cb3de2386 | -9.92043 | -59.90745 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 5753964f-dbf6-398e-80fc-619c8cf3b813 | -10.83798 | -53.76048 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| b543ef27-ebef-3c7a-b33c-6dd8145c6e96 | -10.29054 | -57.01161 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| c554c938-1632-3b43-b557-ae97c693092f | -9.69975 | -56.18695 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 29ead4ae-76c0-3f60-af9c-da97bd752924 | -9.70908 | -56.18678 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 1258c31f-2202-3c1f-bae7-e5c8364a8852 | -10.0526 | -59.3575 | 2025-06-28 05:44:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 92ce3aa5-9064-3990-bb28-8a15aef67ce5 | -11.44273 | -54.48063 | 2025-06-28 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| c5299ee2-d924-3cc2-ad1f-016dc05b4b0e | -12.11292 | -54.57887 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 619ce96d-a9f5-3240-b84c-26daac0fa353 | -12.11003 | -54.66489 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 9200c938-3ee3-3887-95b0-b50c3521685f | -10.03196 | -54.31892 | 2025-06-28 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 4.3 |
| 4046da1f-7e70-38ee-9ca7-26f648440e6f | -11.04399 | -55.3793 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 16.5 |
| 5e3817eb-a0bf-367f-9a0a-8bf3cd447aff | -9.43784 | -63.46371 | 2025-06-28 05:44:00 | NOAA-21 | ALTO PARAÍSO | RONDÔNIA | Brasil | 1100403 | 11 | 33 | nan | nan | nan | Amazônia | 1.4 |
| ffd9928b-972a-3f7d-8aa5-f0933d9d540d | -10.81731 | -57.74904 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 861a098e-9130-3d23-8cd4-37758c665ca8 | -12.10715 | -54.67099 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| a3de0f77-cfc8-367e-a06a-28d75195068b | -10.81573 | -57.76159 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 2.3 |
| 49300577-28e7-36b8-8a02-fffa9382550e | -11.05188 | -55.38068 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 1ee9d763-dcb0-3f19-9bb8-3fe137576f29 | -12.1106 | -54.58526 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| 4dbfd04f-e9f1-3faa-98b1-2270c4458aae | -9.72032 | -56.18834 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| c4203ca3-9b20-3e98-a76e-563721a08ccf | -9.70956 | -56.18291 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| 0722c596-1e35-3a7b-bc8f-27dfd010d04f | -10.81246 | -55.87164 | 2025-06-28 05:44:00 | NOAA-21 | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| d1a822bc-e1a8-3036-9fa8-d8d4b51067ca | -11.04455 | -55.37468 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 17.6 |
| a2e2ac59-260d-3cd8-b933-10e3eaa3c245 | -14.53782 | -53.84111 | 2025-06-28 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5941cc4-72a8-3935-945c-1f5c76d17a12 | -9.71518 | -56.18373 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 903b8e8b-7a51-35c6-9d8d-cfde203b3e92 | -11.88139 | -58.7323 | 2025-06-28 05:44:00 | NOAA-21 | JUÍNA | MATO GROSSO | Brasil | 5105150 | 51 | 33 | nan | nan | nan | Cerrado | 2.5 |
| a738da02-0d4c-3876-8ae0-41b06b0ef1a0 | -9.70586 | -56.18406 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| 2a80d69b-bd2b-383f-9bf6-e82ee750d181 | -9.70347 | -56.18586 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.1 |
| e0dd9339-c701-33b4-b61d-2d48005c28bb | -13.14362 | -56.80858 | 2025-06-28 05:44:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 2.2 |
| efc3e7d2-6bc5-3adc-8458-7af1877819d6 | -10.03964 | -54.33168 | 2025-06-28 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 3.3 |
| d470c86b-5b6b-395b-b137-84d40e8cb1a6 | -10.28517 | -57.01091 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 54bfb48b-7c17-3058-920a-df1827703723 | -10.81612 | -57.75846 | 2025-06-28 05:44:00 | NOAA-21 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| a88f7f7d-a64f-3f0e-ba6b-c0165d8a2f38 | -11.44335 | -54.4752 | 2025-06-28 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 3.0 |
| 9cc56334-6798-3c9c-bf75-fc0b14e3fd8f | -13.29647 | -57.09373 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d3cd964-2283-3db0-93d8-1498838a5ac1 | -10.03705 | -54.32995 | 2025-06-28 05:44:00 | NOAA-21 | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| c0ad2307-962e-353a-a35d-80189fcbfec6 | -11.03799 | -55.37828 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 15.7 |
| 37a4c3d5-f875-3834-adcf-5b532804ed49 | -10.8403 | -53.76123 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f914d320-1ff4-3631-965f-b4c7623650c6 | -11.06208 | -55.38162 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 4dbbe9b1-9434-3ed5-b745-c1435c05ff8a | -12.11233 | -54.58427 | 2025-06-28 05:44:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| ee619b6d-ec5d-3d32-a00f-36ede91db1bb | -9.13121 | -63.9147 | 2025-06-28 05:44:00 | NOAA-21 | PORTO VELHO | RONDÔNIA | Brasil | 1100205 | 11 | 33 | nan | nan | nan | Amazônia | 0.7 |
| dab28a26-5448-3b61-ac61-94d944848937 | -9.71469 | -56.18761 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 8.0 |
| 73f1fa7b-c421-3207-99f2-16912fee7faf | -10.83298 | -53.76609 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 5aa8facd-6a31-31b6-aa03-6cb2eb27227c | -11.28136 | -52.74873 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| cfc62d94-02e7-3dbd-be85-d68573a8efc4 | -11.43696 | -54.47429 | 2025-06-28 05:44:00 | NOAA-21 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 1.9 |
| 180a54f9-7700-39f1-b43b-d4b17363a1c5 | -10.29142 | -57.00468 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 456474c7-a335-37d2-8dc4-7ce2f287ccdd | -10.84101 | -53.75527 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 5642322f-fd8f-30e2-9a51-39a777166000 | -10.30214 | -57.13282 | 2025-06-28 05:44:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 2.7 |
| d46e699f-94bf-3a45-bb6d-318e6f99f109 | -7.89199 | -61.46416 | 2025-06-28 05:44:00 | NOAA-21 | MANICORÉ | AMAZONAS | Brasil | 1302702 | 13 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 07ef5123-904b-3886-bcda-a0b77d868854 | -11.27204 | -52.74539 | 2025-06-28 05:44:00 | NOAA-21 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 15.5 |
| ce455a80-3da6-326c-a91f-ea901fb6fd27 | -9.70536 | -56.18785 | 2025-06-28 05:44:00 | NOAA-21 | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| c7ba207e-0548-387c-add8-72e8d7bf1af8 | -14.5385 | -53.83462 | 2025-06-28 05:44:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 78bbad3a-a48f-3ad3-be3e-ff8472f34808 | -10.84462 | -53.76136 | 2025-06-28 05:44:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 4.0 |
| 97aa706b-753d-360e-8371-9070003416de | -11.05791 | -55.3815 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 10.8 |
| 38bc6727-2577-3d31-98c8-d86c8aa823c7 | -11.05607 | -55.38074 | 2025-06-28 05:44:00 | NOAA-21 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 6.2 |
| 78e98b7a-37c6-3eb9-9353-c6a0e720ea1f | -21.61328 | -57.56844 | 2025-06-28 05:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 40bb495d-d478-3629-b19b-57b55e0df6bb | -21.60729 | -57.56813 | 2025-06-28 05:46:00 | NOAA-21 | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 769885e1-ba51-32d5-8e3d-d056ca0fb752 | -11.2664 | -52.7527 | 2025-06-28 05:50:00 | GOES-19 | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 44.1 |
| 89dc2a05-b76a-3991-87f7-20eb2efb8f9b | -11.0455 | -55.3773 | 2025-06-28 05:50:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 99.1 |
| 2eebeffd-7fa9-3314-9526-5aa3e21136f6 | -11.0455 | -55.3773 | 2025-06-28 06:00:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 88.5 |
| 149688ab-0f5c-367e-befb-c57588431ace | -4.54396 | -48.02866 | 2025-06-28 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 14.3 |
| 80ad9eca-edc0-3110-9af2-e7cf4d2db032 | -4.5456 | -48.01736 | 2025-06-28 06:08:00 | AQUA_M-M | RONDON DO PARÁ | PARÁ | Brasil | 1506187 | 15 | 33 | nan | nan | nan | Amazônia | 37.7 |
| c6b48c57-e8a4-3296-988e-ab33b9c5c9fc | -7.2153 | -43.07056 | 2025-06-28 06:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 60.4 |
| ef835de9-7755-324c-ad0c-1385275a1d59 | -7.0996 | -52.58494 | 2025-06-28 06:08:00 | AQUA_M-M | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 5.0 |
| b4247431-b007-3193-b969-bcf141c30b50 | -6.89971 | -43.97662 | 2025-06-28 06:08:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 52.6 |
| 28e7b641-d69e-306d-9f4b-a9cf223664d2 | -7.21249 | -43.07496 | 2025-06-28 06:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 53.5 |
| 6b07d7cd-20c7-3558-8a5c-85ce887109d2 | -7.54414 | -45.82219 | 2025-06-28 06:08:00 | AQUA_M-M | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 22.9 |
| a329fb1f-41fe-3d16-be6e-e7999d589742 | -6.94959 | -42.86903 | 2025-06-28 06:08:00 | AQUA_M-M | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 36.1 |
| e0cde74c-20b4-37eb-891e-72fce2deb64a | -6.89565 | -43.97092 | 2025-06-28 06:08:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 20.0 |
| 23ca123f-ec77-3339-b397-81aa02cf1c54 | -6.90991 | -43.97267 | 2025-06-28 06:08:00 | AQUA_M-M | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 35.8 |
| 0d80d3ae-ac95-323f-a27f-049858ba91ad | -11.0455 | -55.3773 | 2025-06-28 06:10:00 | GOES-19 | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 95.5 |
| af64536a-2c70-3257-a634-4e646b82efbb | -12.10849 | -54.57798 | 2025-06-28 06:10:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 8.2 |
| 0a7dbe85-2c53-3adc-97a6-b08b7461173e | -11.04943 | -55.3803 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 26.2 |
| bd093c87-1e8e-3079-a9b3-a99e9b21e91a | -15.25719 | -51.47014 | 2025-06-28 06:10:00 | AQUA_M-M | JUSSARA | GOIÁS | Brasil | 5212204 | 52 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 326085a6-edf0-33c6-91cd-fa2857421565 | -10.29569 | -57.13376 | 2025-06-28 06:10:00 | AQUA_M-M | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 11.6 |
| addbdaa3-6e2b-375c-b174-7bd7d31c18f5 | -12.10699 | -54.58768 | 2025-06-28 06:10:00 | AQUA_M-M | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 9.9 |
| 9686e43b-29a7-3d03-bdc5-5b4638aaa608 | -11.57741 | -52.11648 | 2025-06-28 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 11.8 |
| 39f6e8ec-ba16-31d2-9b41-cd72f7fc8c9e | -11.57874 | -52.10747 | 2025-06-28 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |
| 596994f4-7b4b-3eb0-99c5-efb9efb0d73b | -10.83798 | -53.76161 | 2025-06-28 06:10:00 | AQUA_M-M | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 6.5 |
| e3d8d347-f8ac-3ab4-b850-c36376298832 | -9.70999 | -56.18291 | 2025-06-28 06:10:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 65.0 |
| 8aac0f13-a787-3f31-92e5-0939f8044eff | -11.05113 | -55.36953 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 36.0 |
| 9d7781c1-1bab-329a-a235-ba297774f487 | -9.69959 | -56.1813 | 2025-06-28 06:10:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 23.9 |
| 8536e371-aa56-3278-b8b3-d5c93c211386 | -14.68362 | -53.38787 | 2025-06-28 06:10:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 6.2 |
| a69f28f5-89b4-3778-90de-aac786e90fa6 | -11.26873 | -52.75507 | 2025-06-28 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 20.1 |
| 628ae44d-33ea-3ec4-b404-c7a07691010c | -14.69243 | -53.38924 | 2025-06-28 06:10:00 | AQUA_M-M | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 8.2 |
| e62daf0a-4206-3c41-97fa-3e2c594c3e37 | -9.72038 | -56.18462 | 2025-06-28 06:10:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 13.4 |
| c76b9827-8906-3dc1-ae51-7e24b6405806 | -11.04149 | -55.36797 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 68.3 |
| 9fd93515-1a11-378e-bce1-f6b3b617e835 | -11.27007 | -52.74615 | 2025-06-28 06:10:00 | AQUA_M-M | SÃO FÉLIX DO ARAGUAIA | MATO GROSSO | Brasil | 5107859 | 51 | 33 | nan | nan | nan | Amazônia | 48.9 |
| 169c320e-384c-3210-be7a-3d7b109b43da | -12.26028 | -46.7658 | 2025-06-28 06:10:00 | AQUA_M-M | PONTE ALTA DO BOM JESUS | TOCANTINS | Brasil | 1717800 | 17 | 33 | nan | nan | nan | Cerrado | 37.0 |
| a9870df1-9108-3d8f-ab9a-00c42e346712 | -11.03184 | -55.36652 | 2025-06-28 06:10:00 | AQUA_M-M | ITAÚBA | MATO GROSSO | Brasil | 5104559 | 51 | 33 | nan | nan | nan | Amazônia | 11.2 |
| c25a7db0-0a3e-343b-ba33-47d90de98837 | -10.02994 | -54.32134 | 2025-06-28 06:10:00 | AQUA_M-M | MATUPÁ | MATO GROSSO | Brasil | 5105606 | 51 | 33 | nan | nan | nan | Amazônia | 6.3 |
| afc0a8c3-c0b5-3bc2-a9e1-e1100f25762f | -9.712 | -56.17036 | 2025-06-28 06:10:00 | AQUA_M-M | ALTA FLORESTA | MATO GROSSO | Brasil | 5100250 | 51 | 33 | nan | nan | nan | Amazônia | 10.9 |


[Clique aqui para ver as próximas entradas](README29.md)
