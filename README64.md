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

## Dados Diários - Página 64

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| ecfbed61-2c96-3833-953f-30c97cedc5d9 | -13.23371 | -51.81619 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 73.2 |
| 0fd58303-99de-3b0c-897a-f71463a08b27 | -14.03337 | -53.98822 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 36.5 |
| 1d05e145-06e2-3761-a085-51c744274769 | -12.96679 | -54.79771 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 87.1 |
| 4ffcc6f2-9267-3e00-a9b7-567f81949fd0 | -11.34416 | -50.27994 | 2025-09-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 46.6 |
| 98173eb7-c913-3c7b-91ae-2cc82bc216d3 | -15.72766 | -53.61121 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 73.8 |
| 9d7d3f35-2aa8-3092-b70c-c8756760bfb8 | -14.0402 | -54.00789 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 235.6 |
| 327ba13f-a62f-3c90-a3c9-e4b47713f31f | -10.46931 | -53.61908 | 2025-09-05 12:57:00 | TERRA_M-T | PEIXOTO DE AZEVEDO | MATO GROSSO | Brasil | 5106422 | 51 | 33 | nan | nan | nan | Amazônia | 11.5 |
| a595bb60-705b-3e54-a54e-28bb9effa7aa | -13.00053 | -54.83419 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 49.8 |
| c173717f-1c08-3a0f-bdce-6891dcda4957 | -14.03867 | -54.02002 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 99.0 |
| 560131ba-c9af-3880-802e-24499f8b509b | -13.88344 | -47.99487 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 139.7 |
| eb20d6a2-4b49-3fd2-8d1a-b4b382d698db | -13.32606 | -51.6539 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 8b59daab-9df3-3100-9416-b17b68766c2e | -12.27129 | -50.15213 | 2025-09-05 12:57:00 | TERRA_M-T | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 30.8 |
| 729d7d21-2458-3b37-bde7-fc092ad1191f | -12.5274 | -48.05192 | 2025-09-05 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 38.9 |
| f2522bdd-06cb-33de-999c-faa95e1e5fb4 | -14.1334 | -51.72472 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 23.2 |
| 0fb3d0ad-ec87-36c0-9398-8600c791e9e7 | -14.04173 | -53.99582 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 30.1 |
| 5487d65c-f50f-3455-88f0-a6a219102391 | -15.7787 | -47.68756 | 2025-09-05 12:57:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 195.8 |
| bdd6b9d1-0414-399e-998d-df7c2b648169 | -15.54543 | -53.95132 | 2025-09-05 12:57:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.8 |
| ae55946b-de75-3230-9670-effe0ca08b02 | -10.92361 | -56.83596 | 2025-09-05 12:57:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 8.8 |
| 7ce7a260-0d04-3ba7-a437-793a630c0c91 | -11.17784 | -50.03591 | 2025-09-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 78.0 |
| 684d4e05-26e0-3511-b0d4-f2c82e15de56 | -11.34167 | -50.30041 | 2025-09-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 22.0 |
| 5b0ce7dc-b69b-3bca-8f82-cc5d44d27521 | -12.96821 | -54.78719 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 24.4 |
| ed7ccf05-ca63-3e16-867a-88cdbeda508a | -17.46258 | -47.43364 | 2025-09-05 12:57:00 | TERRA_M-T | PARACATU | MINAS GERAIS | Brasil | 3147006 | 31 | 33 | nan | nan | nan | Cerrado | 190.6 |
| e4766cc4-4ebb-3664-9e69-d1440e2c2bc3 | -15.73257 | -53.619 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 109.3 |
| fbeedb26-ab6a-312c-9298-cd4bfdf75aae | -15.54706 | -53.93835 | 2025-09-05 12:57:00 | TERRA_M-T | POXORÉU | MATO GROSSO | Brasil | 5107008 | 51 | 33 | nan | nan | nan | Cerrado | 13.7 |
| 1990821e-8e76-35b1-a03a-4b3a169ddaf2 | -14.44602 | -53.47616 | 2025-09-05 12:57:00 | TERRA_M-T | SANTO ANTÔNIO DO LESTE | MATO GROSSO | Brasil | 5107792 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 99cdc3ec-657d-32b8-8de7-5464c9332953 | -15.8513 | -52.2809 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 7f757100-521a-3c8d-8502-932763e15286 | -15.59218 | -52.92016 | 2025-09-05 12:57:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 46.4 |
| 8da44e6e-0ae3-3052-834a-1a6838e26116 | -15.76625 | -47.69155 | 2025-09-05 12:57:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 81.9 |
| 2e02c649-a86d-3181-8419-a9388a82f3fe | -15.06621 | -50.07611 | 2025-09-05 12:57:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 30.6 |
| 3ce12277-251d-3dd2-841d-17fe8267c129 | -12.95729 | -54.79642 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 49.1 |
| 003cdcff-9c0c-39d9-89b0-3dff2268e88c | -15.23134 | -52.39008 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 18.2 |
| 863aeac0-2c4a-358b-9435-59f5712f8aaf | -11.83106 | -51.42417 | 2025-09-05 12:57:00 | TERRA_M-T | ALTO BOA VISTA | MATO GROSSO | Brasil | 5100359 | 51 | 33 | nan | nan | nan | Cerrado | 39.6 |
| 2f70e275-915c-3ae1-a81f-b47a0ae8d222 | -14.57229 | -48.07912 | 2025-09-05 12:57:00 | TERRA_M-T | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 0b93cd00-86a6-3d06-bafd-b0b996ea6d59 | -15.70216 | -53.60221 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 24.6 |
| 3a72225d-524b-3616-918e-abd958ee1ed9 | -15.73831 | -53.61278 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 42.9 |
| 5d0ba181-1a99-3889-a4af-3aa8c4e4761b | -13.66099 | -47.9143 | 2025-09-05 12:57:00 | TERRA_M-T | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 49.5 |
| e61b6a0f-6f65-3bc2-8b7e-74ffcfc2abdf | -13.00195 | -54.82376 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 79.3 |
| f12afb61-b166-3a04-afa6-9123832dab21 | -15.75292 | -53.67043 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 203.8 |
| 6c2a474a-d86c-35a4-8038-d5291105adee | -11.08458 | -51.99825 | 2025-09-05 12:57:00 | TERRA_M-T | CANABRAVA DO NORTE | MATO GROSSO | Brasil | 5102694 | 51 | 33 | nan | nan | nan | Amazônia | 12.0 |
| 52437f7a-e5dc-3925-8eb0-64954cd47eb6 | -15.31782 | -52.72945 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 29.4 |
| d07563fb-a7fe-3303-a954-7430de02dfef | -10.92489 | -56.82703 | 2025-09-05 12:57:00 | TERRA_M-T | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 18.2 |
| f9682082-2b1c-343a-9c77-16c1310aeec1 | -15.14031 | -52.38683 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 21.8 |
| a1e8bff9-cd89-305b-be96-5660bf3acf31 | -12.52383 | -48.08391 | 2025-09-05 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 31.3 |
| 7fcd485c-2102-3097-8eb2-9c3affe06853 | -15.14418 | -52.38058 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 40.2 |
| c8db5bbb-434c-389e-8d87-54d6f0ed9b21 | -15.72183 | -53.61819 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 44.3 |
| 827cc176-f2e5-38db-a938-05b0333e24cc | -14.0316 | -53.99446 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 59.2 |
| 2b620211-37a5-31b7-9df0-f17a2bb6d6c8 | -14.06507 | -53.9744 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 31.1 |
| c07b0b3a-9220-3391-aff8-44d6904de8c0 | -13.89955 | -47.9966 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 89.5 |
| 158a594d-a074-366d-bc6a-d62e1efded1d | -11.1804 | -50.01456 | 2025-09-05 12:57:00 | TERRA_M-T | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 56.1 |
| b0765b23-22b1-335e-ad20-642cafbd5544 | -15.20009 | -52.38025 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.6 |
| 4f634e50-f0f2-3a88-8fcf-5299a8b7599d | -11.19998 | -55.0056 | 2025-09-05 12:57:00 | TERRA_M-T | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 19.6 |
| 2481f1b4-5c43-3e93-8dc5-63fcc6b1e732 | -10.53077 | -53.62144 | 2025-09-05 12:57:00 | TERRA_M-T | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 8.7 |
| 5ef37af9-9c0b-3377-800a-6d7b4a692179 | -15.05511 | -50.10491 | 2025-09-05 12:57:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 27.0 |
| 432f888a-82f6-3b99-b432-3600d197458f | -15.7164 | -53.5753 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 14.6 |
| 461d7458-6107-3b1f-922b-d10e8e815b59 | -10.99016 | -49.77506 | 2025-09-05 12:57:00 | TERRA_M-T | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 19.6 |
| d8c2f67d-75d3-3c88-bd77-61cc66f57db3 | -15.72362 | -53.60409 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 101.9 |
| 077ae45d-3fb2-39c7-bf17-2dca37fc3892 | -10.8781 | -55.73067 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA CANAÃ DO NORTE | MATO GROSSO | Brasil | 5106216 | 51 | 33 | nan | nan | nan | Amazônia | 9.7 |
| 6c184895-3885-3f38-b1b3-5856e4203a56 | -15.05767 | -50.08088 | 2025-09-05 12:57:00 | TERRA_M-T | CRIXÁS | GOIÁS | Brasil | 5206404 | 52 | 33 | nan | nan | nan | Cerrado | 45.6 |
| 0640f357-ae3b-3b9f-a2a4-8f07cc099c36 | -12.96539 | -54.80814 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 181.7 |
| 5f71300d-ab98-364c-9b41-166a5e7f6527 | -15.7619 | -53.68511 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 47.3 |
| 0685006b-4a25-31ea-8b28-2a08b11dd667 | -15.22542 | -52.36627 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 38.9 |
| 67d2d6c6-9764-3a0c-9cf4-3001c6f46023 | -11.86663 | -50.71014 | 2025-09-05 12:57:00 | TERRA_M-T | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 25.7 |
| a234707a-c034-3947-a3f3-ad9e29a19da4 | -13.087 | -57.11571 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 43.0 |
| 4f9d2eae-9554-3b0d-b151-8cdbf23dcf68 | -12.95869 | -54.78594 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 39.3 |
| f653857c-4cfe-3713-84ef-142d02cfe46c | -13.31966 | -51.65892 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.0 |
| c60c21e2-272d-317d-a5bf-15d501830842 | -14.03179 | -54.00019 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 70.9 |
| 198a178b-716b-3a87-a8da-32e722aea844 | -15.84937 | -52.29731 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 37.7 |
| d65cfbea-6d0a-3fee-949f-211482bafb3f | -14.05338 | -53.9852 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 105.4 |
| f7cf9bb0-5862-3997-8dca-9ff70e06d257 | -13.89136 | -47.99002 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 109.0 |
| 88db2fe9-d255-323c-a778-9b88285f7d1c | -16.33106 | -52.95411 | 2025-09-05 12:57:00 | TERRA_M-T | TORIXORÉU | MATO GROSSO | Brasil | 5108204 | 51 | 33 | nan | nan | nan | Cerrado | 15.7 |
| dc2d6257-eb12-3eb9-929c-79d05a82b6af | -15.73427 | -53.60565 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 34.9 |
| adf1dc3b-7147-3118-9162-a25545e6139c | -15.7129 | -53.60307 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 127.4 |
| 63f5f70b-bda6-348f-ab99-8e3cc6250b0e | -15.14223 | -52.37008 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 26.0 |
| 36061084-5972-33d6-8e52-d7f8da896516 | -15.76694 | -53.64439 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 39.2 |
| 748fa36a-5f97-3c69-b006-74e0a06011c3 | -15.235 | -52.38458 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.8 |
| 7120cd4d-6420-387f-a26b-f513482d8504 | -12.53733 | -48.05928 | 2025-09-05 12:57:00 | TERRA_M-T | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 41.7 |
| 01034921-b90b-3927-b02e-73507478646d | -13.32391 | -51.671 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 16.3 |
| 87c685ed-6c3c-3aae-8adc-f38be35c66e4 | -11.61863 | -47.7929 | 2025-09-05 12:57:00 | TERRA_M-T | CHAPADA DA NATIVIDADE | TOCANTINS | Brasil | 1705102 | 17 | 33 | nan | nan | nan | Cerrado | 60.2 |
| 4784e31d-3edb-3f03-bf44-55c4ce7bc17d | -15.61652 | -52.90769 | 2025-09-05 12:57:00 | TERRA_M-T | GENERAL CARNEIRO | MATO GROSSO | Brasil | 5103908 | 51 | 33 | nan | nan | nan | Cerrado | 19.3 |
| 6419a74b-843e-3d5c-a19a-906bca96d29b | -14.1288 | -51.71768 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA NAZARÉ | MATO GROSSO | Brasil | 5106174 | 51 | 33 | nan | nan | nan | Cerrado | 25.4 |
| 7b85468d-83f0-3ab9-9eef-a4870bfcf30e | -13.88763 | -48.02499 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 52.5 |
| 767e5928-3fc8-3de0-88cf-ffbd1270f61c | -14.04325 | -53.98383 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 11.6 |
| a9ce008e-2753-312e-a68a-250d0651113b | -13.33165 | -51.66024 | 2025-09-05 12:57:00 | TERRA_M-T | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Cerrado | 19.2 |
| 24deaa56-ef3e-3b0f-8f76-6cb04142dad9 | -15.75459 | -53.65683 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 71.6 |
| 16aa93d4-18d6-3e65-93af-ed04f9394ff1 | -13.87892 | -47.95336 | 2025-09-05 12:57:00 | TERRA_M-T | COLINAS DO SUL | GOIÁS | Brasil | 5205521 | 52 | 33 | nan | nan | nan | Cerrado | 236.3 |
| 2fafc30c-f532-3087-a796-c39e306e4713 | -15.20213 | -52.36327 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 14.4 |
| fb36b65b-ee1b-306c-816c-111817e9a75d | -12.96962 | -54.77664 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Amazônia | 14.1 |
| 04b96a16-fa66-385e-a13b-8d331d096eca | -15.78316 | -47.693 | 2025-09-05 12:57:00 | TERRA_M-T | BRASÍLIA | DISTRITO FEDERAL | Brasil | 5300108 | 53 | 33 | nan | nan | nan | Cerrado | 117.8 |
| 1c2483b6-7a4e-3fc1-b501-bec3bcac52f3 | -14.05032 | -54.00925 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 17.0 |
| a8017d7f-d420-39be-a2e5-c25efb1c43cb | -12.95589 | -54.80685 | 2025-09-05 12:57:00 | TERRA_M-T | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 20.6 |
| be8b6dca-b1b8-37c5-b2a5-af6de30d5408 | -14.05491 | -53.97316 | 2025-09-05 12:57:00 | TERRA_M-T | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Cerrado | 44.4 |
| a009aa6a-8114-3c2d-a4d1-23a1bd192603 | -10.99326 | -51.99604 | 2025-09-05 12:57:00 | TERRA_M-T | PORTO ALEGRE DO NORTE | MATO GROSSO | Brasil | 5106778 | 51 | 33 | nan | nan | nan | Amazônia | 16.4 |
| 248c11b1-9396-3e63-ac8a-81bf302a1142 | -15.32921 | -52.73042 | 2025-09-05 12:57:00 | TERRA_M-T | BARRA DO GARÇAS | MATO GROSSO | Brasil | 5101803 | 51 | 33 | nan | nan | nan | Cerrado | 16.9 |
| b9afb574-b124-347b-96ec-433b2485c081 | -15.71466 | -53.58912 | 2025-09-05 12:57:00 | TERRA_M-T | TESOURO | MATO GROSSO | Brasil | 5108105 | 51 | 33 | nan | nan | nan | Cerrado | 110.4 |
| 123cfc2b-13ea-3d18-a1c3-992865db4803 | -22.27748 | -51.13828 | 2025-09-05 12:59:00 | TERRA_M-T | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 23.1 |
| fffecc2e-5cb1-3e8f-826c-c73e1ceac39c | -22.27637 | -51.10594 | 2025-09-05 12:59:00 | TERRA_M-T | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 55.4 |
| 8f876bfb-361d-36e1-a7a2-eec40bba907c | -23.33899 | -50.86226 | 2025-09-05 12:59:00 | TERRA_M-T | ASSAÍ | PARANÁ | Brasil | 4101903 | 41 | 33 | nan | nan | nan | Mata Atlântica | 82.8 |
| c0ba43c6-ecbd-39de-b50e-9fa85c44b032 | -22.27982 | -51.1119 | 2025-09-05 12:59:00 | TERRA_M-T | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 74.2 |
| 5b975def-4a87-30ae-ab78-1d2ce551d19e | -22.27386 | -51.13234 | 2025-09-05 12:59:00 | TERRA_M-T | MARTINÓPOLIS | SÃO PAULO | Brasil | 3529203 | 35 | 33 | nan | nan | nan | Cerrado | 43.9 |
| 50849a57-3df7-3488-985d-b5ea4cb3f735 | -8.9037 | -45.7747 | 2025-09-05 13:00:00 | GOES-19 | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 58.2 |


[Clique aqui para ver as próximas entradas](README65.md)
