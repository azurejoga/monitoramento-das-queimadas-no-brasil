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

## Dados Diários - Página 62

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 306e6faa-f7e5-35ec-8f5e-3c5b3f7ac7b8 | -6.74484 | -58.72461 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.1 |
| eaf225ee-7166-3240-86ab-1305f00dc8b8 | -6.59564 | -44.31381 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c9e87cd4-ecd4-31f5-8973-a70fb48cfb27 | -9.96028 | -51.6338 | 2025-09-04 04:53:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| e53d3955-f632-3ffc-8f36-9214095db16c | -5.28425 | -55.95669 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 2a4a4ccf-97d1-3183-a99a-0f7b63e73886 | -7.68964 | -48.7278 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 10.7 |
| c841468f-5b6d-3b6f-88bd-b30dc8601b00 | -8.73121 | -47.00139 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 29e25709-732d-3fcb-a643-11360c90deec | -6.76242 | -63.13338 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 3.1 |
| 50f83577-d59c-34e7-8460-d932ca4c2bca | -9.72294 | -48.3103 | 2025-09-04 04:53:00 | NPP-375D | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 3e871fab-6a26-3320-90bd-658abeb73a4d | -5.26741 | -50.76374 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 094f680b-e0f7-358e-8555-b7b13632cdc5 | -5.89434 | -44.34898 | 2025-09-04 04:53:00 | NPP-375D | JATOBÁ | MARANHÃO | Brasil | 2105450 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 48aa74ae-37cb-3ccb-92e5-57f33f935249 | -10.65218 | -44.844 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO BARROS | PIAUÍ | Brasil | 2210623 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 9ba37907-e60f-32ba-8fd8-f319e78ea34b | -6.75142 | -58.73856 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a5f8d292-05fd-385c-84a2-1cf7eb863d31 | -8.86092 | -52.02408 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| c4ebaef2-c239-321e-b52e-dc7d16abeb0e | -6.79035 | -44.44815 | 2025-09-04 04:53:00 | NPP-375D | SÃO DOMINGOS DO AZEITÃO | MARANHÃO | Brasil | 2110658 | 21 | 33 | nan | nan | nan | Cerrado | 5.7 |
| 5bed4377-3e4b-3293-b22b-cc8f038298e4 | -10.97739 | -46.85306 | 2025-09-04 04:53:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 9aee00cd-4b34-3358-81a5-f962acf6b545 | -6.34132 | -53.4497 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2091c08-24b4-3e0c-9cfc-dee0977b8a9c | -5.86685 | -46.1156 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| eb53fd82-4d48-3977-ae04-2316900ba3b5 | -6.46651 | -53.3977 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 4fb267da-1025-3f91-bb81-e6d0d8bd0323 | -9.48417 | -47.61494 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 6d11084d-6432-360c-a079-ae3e11f4b2aa | -6.79358 | -44.09001 | 2025-09-04 04:53:00 | NPP-375D | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 436baa79-2786-31ef-8f43-3a6c3c05dcd5 | -6.22368 | -43.54683 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 4e4a9308-bd6f-3121-83bf-31ec02dbbd90 | -7.74885 | -48.7671 | 2025-09-04 04:53:00 | NPP-375D | BANDEIRANTES DO TOCANTINS | TOCANTINS | Brasil | 1703057 | 17 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 0c09c01f-68b4-3895-a13f-e088d6ec56d5 | -5.86184 | -46.11909 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| a5762df6-2ee7-3a9b-902e-3946e3a913b3 | -8.53501 | -51.32868 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 7.5 |
| 53a7e51b-c78e-37c2-be96-357a4ba8ad60 | -8.87982 | -45.84634 | 2025-09-04 04:53:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4fa41532-3ef3-37e1-95f0-77bcd8861335 | -9.60668 | -47.0393 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 04b0ea8f-c6c0-3be5-b1f5-d85774f1b9db | -6.78492 | -63.14201 | 2025-09-04 04:53:00 | NPP-375D | TAPAUÁ | AMAZONAS | Brasil | 1304104 | 13 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 116acabb-c5a2-38fd-8baf-7e456a991150 | -8.00127 | -50.07236 | 2025-09-04 04:53:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 229914f4-bb8b-31fc-a7f2-568d9cb110e5 | -6.26191 | -43.58269 | 2025-09-04 04:53:00 | NPP-375D | PASSAGEM FRANCA | MARANHÃO | Brasil | 2107902 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| d4ef3f76-e8c2-30fb-acdf-fd8bbacded29 | -9.76939 | -49.44732 | 2025-09-04 04:53:00 | NPP-375D | DIVINÓPOLIS DO TOCANTINS | TOCANTINS | Brasil | 1707108 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 56be45d8-4bcf-3129-b0db-4c3da7548317 | -10.04085 | -48.14026 | 2025-09-04 04:53:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| dd2e9405-3185-30af-8f02-46b93764e23f | -8.44148 | -47.3354 | 2025-09-04 04:53:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| f3dc392c-3cfe-3550-af64-22e136690a40 | -10.15052 | -46.25983 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 4c868fc3-93ef-30be-9deb-4cb145c7a017 | -11.0423 | -45.12258 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| f038c0d5-3abb-3c33-95b3-0fcf59cf5958 | -6.74778 | -58.73363 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 10.9 |
| a22fc265-69d8-3f7c-965b-84afb2dbb963 | -5.31094 | -55.86156 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 92c15b4c-eaea-34d7-8bf3-a86c01268e2a | -10.02795 | -46.093 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.8 |
| e4d517d7-18f3-38af-8295-0e5875c7dd11 | -7.72415 | -44.61127 | 2025-09-04 04:53:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 586bfe7d-9a88-30c0-95ee-ec1af0209054 | -8.02309 | -44.14501 | 2025-09-04 04:53:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 8d6401e8-378c-3779-ad3b-985c85d31e4f | -5.39149 | -45.94464 | 2025-09-04 04:53:00 | NPP-375D | ITAIPAVA DO GRAJAÚ | MARANHÃO | Brasil | 2105351 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 84708acb-1281-3bb3-8193-e2e75ba6c0e1 | -7.93825 | -44.93445 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 5.7 |
| c416bd86-d2a4-35ef-b95a-1622781ec010 | -5.28052 | -55.9561 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 864f7fc3-1d4b-38cb-bf67-6fedf42f645f | -9.63966 | -47.85102 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 5a522897-3a68-3721-91e0-85352069fb32 | -8.61248 | -40.30603 | 2025-09-04 04:53:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 04de2bb3-d22a-334d-a4a6-7e0d5fa795ae | -5.30794 | -55.85658 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.1 |
| 0de252bf-e860-36a2-8895-7a271ad97cb3 | -9.34139 | -55.21248 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 1.4 |
| e3798ae8-36d2-3c2e-a96e-45a57402d7c8 | -5.30951 | -55.8595 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 0de5e5d8-439b-3873-8978-3abd9b2c0018 | -8.73061 | -47.00551 | 2025-09-04 04:53:00 | NPP-375D | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| fe6a7f21-953a-324a-94e2-336c465b5e30 | -9.49248 | -47.61484 | 2025-09-04 04:53:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3f2bf9db-ef42-327b-acd9-c8b1661e806d | -10.74722 | -46.34567 | 2025-09-04 04:53:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87c0306d-bae4-3a14-9441-50baf822c2af | -6.28848 | -43.50959 | 2025-09-04 04:53:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 1c91e200-8d1a-31cf-a78c-3eb96a114921 | -5.74979 | -45.53571 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 0110c911-3ab1-332d-b95f-f457da886d39 | -9.43487 | -46.7635 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 5afc8d03-4b24-3a70-af07-e6d0d75e7aef | -6.23229 | -43.4049 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 56a2e864-d848-3f88-a93b-faa1a3cb07bf | -5.77314 | -44.86858 | 2025-09-04 04:53:00 | NPP-375D | TUNTUM | MARANHÃO | Brasil | 2112308 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 15414beb-04fd-3a2b-88aa-669d38eb6574 | -8.86297 | -47.93003 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0856dcb0-0dab-3ce2-885f-2a92eb602db7 | -9.5776 | -53.56071 | 2025-09-04 04:53:00 | NPP-375D | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 47b16426-f8c4-35a0-9c9e-d04ad67ce1a4 | -6.33536 | -45.67773 | 2025-09-04 04:53:00 | NPP-375D | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f3016ae0-86f9-3842-ad88-3f031a910103 | -6.22638 | -42.44146 | 2025-09-04 04:53:00 | NPP-375D | JARDIM DO MULATO | PIAUÍ | Brasil | 2205250 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 84e0ec19-4143-3ff9-b2b1-6c90ef0f19c2 | -8.52642 | -51.31623 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 2.7 |
| 1526bb01-a44e-374c-959d-be3d8483bcdc | -8.02945 | -44.06025 | 2025-09-04 04:53:00 | NPP-375D | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| df143c51-307b-3d9a-b67c-6640114c317c | -5.18432 | -46.07295 | 2025-09-04 04:53:00 | NPP-375D | ARAME | MARANHÃO | Brasil | 2100956 | 21 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 48ab252f-8166-333f-9467-190ca8c1a811 | -9.445 | -46.75598 | 2025-09-04 04:53:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| dc3a9c24-7d89-3f0c-b332-df0bdd148cf1 | -8.86654 | -47.9342 | 2025-09-04 04:53:00 | NPP-375D | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 405afb35-ed32-383c-9ad4-f925bc04e7e7 | -6.8206 | -45.67195 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 3a3c9979-d0b4-39a5-be0b-ad535cde9a12 | -5.02725 | -56.11261 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 2990e0b0-cad9-3399-8217-a2ada8485011 | -6.69777 | -48.41692 | 2025-09-04 04:53:00 | NPP-375D | XAMBIOÁ | TOCANTINS | Brasil | 1722107 | 17 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f5187b6e-8bff-3c8e-881f-bb967309e5b3 | -9.69374 | -51.04534 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 1.5 |
| 7e3ad57e-eefc-399c-8341-c444e9271035 | -9.26926 | -56.89618 | 2025-09-04 04:53:00 | NPP-375D | PARANAÍTA | MATO GROSSO | Brasil | 5106299 | 51 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 172f2016-b8a2-30ba-bed4-63e109bb31ec | -6.16583 | -55.71533 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 84894f93-e24a-3878-a05a-07578774881e | -6.24435 | -42.60063 | 2025-09-04 04:53:00 | NPP-375D | REGENERAÇÃO | PIAUÍ | Brasil | 2208809 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 8d1b095e-1267-35c0-9d99-73753c4fea3d | -7.30772 | -57.156 | 2025-09-04 04:53:00 | NPP-375D | JACAREACANGA | PARÁ | Brasil | 1503754 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| dd360865-75f3-3e01-9f4c-4051d92a941b | -5.93819 | -51.97262 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| f6a255f2-ba0a-327a-90b7-6dd8f424d78d | -6.88852 | -45.56271 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b2c74a9a-3933-3db1-90de-b08c4ce035a8 | -6.54617 | -43.9119 | 2025-09-04 04:53:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 315da298-304a-3e2f-aded-0faf0412d975 | -6.54599 | -42.95173 | 2025-09-04 04:53:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 6b7090dd-3512-3f7e-bce6-c4fade04444f | -9.70651 | -51.05509 | 2025-09-04 04:53:00 | NPP-375D | SANTANA DO ARAGUAIA | PARÁ | Brasil | 1506708 | 15 | 33 | nan | nan | nan | Amazônia | 2.2 |
| 3ea72609-6719-3552-a32a-d8362ee62b8d | -5.80243 | -45.62566 | 2025-09-04 04:53:00 | NPP-375D | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 0296802a-21d6-3235-9832-cb8bb6cffc69 | -5.65227 | -51.27032 | 2025-09-04 04:53:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.6 |
| 9a3d17bd-4bd5-3f19-9fe4-5649bbc87fd2 | -6.75282 | -58.73027 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 6.3 |
| 8b2c41b3-0194-345c-8101-0dd9a0ad27cd | -4.61276 | -56.17189 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 7d42dbee-6cb1-33f8-8ccf-696f2ddbedc6 | -6.67623 | -58.75964 | 2025-09-04 04:53:00 | NPP-375D | MAUÉS | AMAZONAS | Brasil | 1302900 | 13 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 9ba64d76-bb0d-33ec-bac9-16acb623706d | -8.53267 | -51.32113 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 4.6 |
| a11d9383-0a64-36a5-b034-2e9befc68910 | -7.07255 | -46.19376 | 2025-09-04 04:53:00 | NPP-375D | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| aaa43a54-1e07-3d22-a79f-2403c189c88a | -5.39199 | -55.91364 | 2025-09-04 04:53:00 | NPP-375D | ITAITUBA | PARÁ | Brasil | 1503606 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| ad641d43-9ce1-305c-9d59-2458d790d905 | -6.22812 | -43.55386 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 241fea68-a232-37e8-9ac5-f8c285d225fc | -6.03073 | -46.67793 | 2025-09-04 04:53:00 | NPP-375D | SÍTIO NOVO | MARANHÃO | Brasil | 2111805 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 3b76150d-2b66-3be8-9177-1c255cf1968d | -6.76495 | -45.93093 | 2025-09-04 04:53:00 | NPP-375D | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 5a3094b9-5c74-3486-abf3-2af7b213b2b8 | -9.32794 | -55.22965 | 2025-09-04 04:53:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 95602b23-fea8-390d-9d0c-1771545a57e0 | -4.8895 | -55.8476 | 2025-09-04 04:53:00 | NPP-375D | TRAIRÃO | PARÁ | Brasil | 1508050 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f17ba479-d6e1-337e-890b-3cde8210186a | -9.69253 | -49.00246 | 2025-09-04 04:53:00 | NPP-375D | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6c059b80-e5f7-3b19-a7c9-e7f18ee9a27f | -7.71237 | -50.29295 | 2025-09-04 04:53:00 | NPP-375D | PAU D'ARCO | PARÁ | Brasil | 1505551 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 41ea163b-5d44-3f36-9bce-d23d8d0f8c1c | -3.43032 | -59.57434 | 2025-09-04 04:53:00 | NPP-375D | CAREIRO DA VÁRZEA | AMAZONAS | Brasil | 1301159 | 13 | 33 | nan | nan | nan | Amazônia | 3.7 |
| f94aca43-ca98-3a71-8275-8e28a5c1a2fa | -8.08606 | -45.36462 | 2025-09-04 04:53:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aa9ade3d-3f94-3964-be00-7e8cc25509c5 | -5.69807 | -45.15259 | 2025-09-04 04:53:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.3 |
| fcc43516-af1b-3d86-a52a-dec29731d6ff | -6.22325 | -43.54993 | 2025-09-04 04:53:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 63d904bd-d02f-3ee0-9a6a-544883d94de0 | -7.77744 | -50.97239 | 2025-09-04 04:53:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 8d324c60-987e-3715-8663-b7324674de22 | -10.15387 | -46.27018 | 2025-09-04 04:53:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| fa9ac838-6e3c-3eec-ba69-21400686d4f1 | -11.0419 | -45.12566 | 2025-09-04 04:53:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 348ee650-6dc2-3934-a323-dfff48c40c65 | -11.13073 | -44.6384 | 2025-09-04 04:53:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |


[Clique aqui para ver as próximas entradas](README63.md)
