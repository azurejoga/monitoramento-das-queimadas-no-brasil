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

## Dados Diários - Página 1

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 56fd4aed-50b0-3f4b-a0dd-227b9c1fea45 | -10.14 | -36.22 | 2024-12-28 00:00:00 | MSG-03 | CORURIPE | ALAGOAS | Brasil | 2702306 | 27 | 33 | nan | nan | nan | Mata Atlântica | nan |
| a982c9f1-334d-3fbe-9524-8c7f5def0854 | -3.8964 | -46.678699 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 45504843-09cd-3231-97c7-3b4315771430 | -3.9534 | -46.748199 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4d9773a5-694e-322d-855d-c062c2ecbe97 | -5.3243 | -46.069401 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 30d28048-7726-3094-b300-4757cebad58b | -2.9144 | -54.4804 | 2024-12-28 00:21:00 | METOP-B | MOJUÍ DOS CAMPOS | PARÁ | Brasil | 1504752 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 0d3aedfa-7e1f-3b6a-af09-6ec92993da86 | -3.9066 | -46.996101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9dbf8687-acb9-3b04-b2b1-50b701c9d62d | -3.8474 | -46.689701 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ce42b85-ee24-3307-bce5-3e9848498e7d | -3.9567 | -46.762402 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 213d14c8-caf9-3995-b14e-5e128292745f | -1.6444 | -52.598202 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3fad099-bbdc-30b7-9f10-9835e4680f31 | -3.8131 | -46.719898 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dea784fb-d190-3a0f-8682-ace26f39c8ca | -2.5613 | -46.879799 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d675dc2f-67f0-374f-9cb8-824d83c21384 | -3.8955 | -46.946899 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 01f35d8d-ca35-39dc-98c7-7a982d083e95 | -9.1178 | -40.960701 | 2024-12-28 00:21:00 | METOP-B | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | nan |
| 2745bbcb-8455-3bfa-b0d0-b786a5176489 | -3.222 | -45.483101 | 2024-12-28 00:21:00 | METOP-B | PENALVA | MARANHÃO | Brasil | 2108306 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d14a0685-b561-36d0-b17c-c8af8e439979 | -2.6326 | -46.105701 | 2024-12-28 00:21:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 59a0f157-1a17-3585-83d1-7218f4edc730 | -3.2063 | -46.000801 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 53e324bb-5fa1-3d7e-ac51-b248f58cbaff | -3.9681 | -46.7673 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| affa2a52-b76c-3c38-8e3e-3b12f25806a8 | -1.6599 | -45.8591 | 2024-12-28 00:21:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0692cd33-14b6-3fc6-81ed-da1d7b179161 | -4.0198 | -46.904202 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 64636bd0-84ca-37fb-a1c3-600e9a406705 | -4.1431 | -46.6759 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f58d9d0d-cf75-3f80-a157-5d85b6b162ef | -3.9267 | -46.902901 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e0e35e48-2548-3141-80e6-82c27f7dcbf0 | -3.9201 | -46.919201 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b4f4b922-b99a-33bf-addb-c9515dc71b49 | -0.7584 | -47.198299 | 2024-12-28 00:21:00 | METOP-B | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5aaf127b-b0b9-3063-891c-a34001e336e5 | -3.9 | -47.012299 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 0a2ce780-7962-3cd3-a36b-d551ed1be687 | -3.9082 | -47.003101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 61022058-a9c4-3c59-adcd-fa8b59361319 | -3.9217 | -46.926201 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 861257fe-a2fa-3c75-ae0b-3a3a1663d762 | -3.2109 | -45.9758 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7826b19a-5969-3e63-bdef-fe2bb9de7372 | -1.7118 | -46.223598 | 2024-12-28 00:21:00 | METOP-B | VISEU | PARÁ | Brasil | 1508308 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 69d93975-92b2-30e4-b0c4-fa4a0038c744 | -2.8211 | -46.708401 | 2024-12-28 00:21:00 | METOP-B | PARAGOMINAS | PARÁ | Brasil | 1505502 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 7ba9e0f0-49ad-3625-87ed-d3808f73b29e | -0.7567 | -47.191101 | 2024-12-28 00:21:00 | METOP-B | SÃO JOÃO DE PIRABAS | PARÁ | Brasil | 1507474 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 55075a1a-34bd-358c-9c22-e60da2736ec8 | -4.7388 | -44.639801 | 2024-12-28 00:21:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 9f99dce4-beab-3c80-82b1-4fc28405934d | -3.8981 | -46.685902 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9b17d9d8-6326-3752-bf8e-97ef5956592a | -3.8229 | -46.717701 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6b6863f8-670b-34c8-bbb4-84a8562b971b | -3.9219 | -46.881802 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 32b26015-8103-322b-83a1-90264206c1a7 | -2.4688 | -49.299198 | 2024-12-28 00:21:00 | METOP-B | MOCAJUBA | PARÁ | Brasil | 1504604 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| f3e848ca-be2f-3c1f-b223-e52bddb3d14a | -1.3485 | -46.9837 | 2024-12-28 00:21:00 | METOP-B | SANTA LUZIA DO PARÁ | PARÁ | Brasil | 1506559 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 5a63ae8c-cdd3-30cd-8b2c-3c86bfef0f68 | -2.5341 | -51.843201 | 2024-12-28 00:21:00 | METOP-B | PORTEL | PARÁ | Brasil | 1505809 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 65b4595d-5846-35b8-b46a-8ea51583145c | -3.8126 | -46.854301 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 4b2369bc-2b61-3181-98ca-19343bc2ed64 | -3.9845 | -46.340801 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c427946a-9bb2-325c-a247-4f64fc108d13 | -3.905 | -46.989101 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6e77b54c-a78a-35b1-9880-d8b514d5d91c | -4.0091 | -46.720901 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| e32504d1-0b0d-372b-b360-8ec9efdd74de | -3.6982 | -47.1675 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| e8a0e400-4dda-320d-95bd-ec3e4e8a96f0 | -2.7364 | -46.018398 | 2024-12-28 00:21:00 | METOP-B | NOVA OLINDA DO MARANHÃO | MARANHÃO | Brasil | 2107357 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9db15b8b-3c8c-3fdc-a1aa-c9efca599359 | -4.4176 | -45.9804 | 2024-12-28 00:21:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 19f76adb-b9d8-34ec-bf1d-95e84b904226 | -4.2495 | -45.425301 | 2024-12-28 00:21:00 | METOP-B | ALTAMIRA DO MARANHÃO | MARANHÃO | Brasil | 2100402 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ce4a17a2-e99f-38e8-b4f6-4d16936137a4 | -3.8622 | -46.663898 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c703e74e-7d0d-3db7-a58b-d7b249c5aec5 | -2.4489 | -47.475399 | 2024-12-28 00:21:00 | METOP-B | IPIXUNA DO PARÁ | PARÁ | Brasil | 1503457 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 42167014-e61d-36c8-9493-c2eb315798ea | -2.2758 | -47.666801 | 2024-12-28 00:21:00 | METOP-B | AURORA DO PARÁ | PARÁ | Brasil | 1500958 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| b61fd501-1b55-3190-a6de-828eb4735bf6 | -3.934 | -46.6628 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c7f58d87-8485-3874-b3fc-d4f4077a0dec | -4.7603 | -44.6437 | 2024-12-28 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 33cac02d-3b74-32dc-be89-8bf9b4e1fead | -3.2044 | -46.127998 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2554d4dd-ef56-3e47-ab2f-c533202ec4d4 | -4.0904 | -46.8069 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 550f76ba-ca76-3f52-9708-9c194868edbe | -3.8541 | -47.037201 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a0545bc5-484d-35df-a3be-fa0a8f90a029 | -4.1283 | -46.701599 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c939114-63be-32ae-86a0-a0339d689930 | -4.0124 | -46.690201 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a10dcb9b-54b7-3159-9c38-8fab7b9e2ece | -4.0809 | -46.7197 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| ab58b846-727d-32d9-83fc-cee3175252fa | -3.9137 | -46.890999 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 765e735a-6a84-3cf8-ba0f-30d3370a5f2a | -1.6617 | -45.867001 | 2024-12-28 00:21:00 | METOP-B | AMAPÁ DO MARANHÃO | MARANHÃO | Brasil | 2100550 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| af800ce8-bfab-34e7-addc-90cbb83ce03d | -3.7779 | -47.201 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| d0b1c4cd-f4cb-32a6-8a06-e8864ca5e8cf | -4.8266 | -42.360699 | 2024-12-28 00:21:00 | METOP-B | CAMPO MAIOR | PIAUÍ | Brasil | 2202208 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 9b240832-3657-360c-a4f9-3c368fa42cdc | -3.2144 | -45.991001 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f8a12e33-0ef9-33cc-933f-f1e79cc16bfc | -1.6325 | -52.591202 | 2024-12-28 00:21:00 | METOP-B | PORTO DE MOZ | PARÁ | Brasil | 1505908 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 62305c42-ac14-3085-9e26-1e2b0f1cffe4 | -4.0402 | -47.0397 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| d57a5350-6e77-3891-8475-328ffb777755 | -4.7407 | -44.648201 | 2024-12-28 00:21:00 | METOP-B | BERNARDO DO MEARIM | MARANHÃO | Brasil | 2101939 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| fa4a2bab-b59d-37fc-bba8-7549cdf5adae | -3.9622 | -49.4389 | 2024-12-28 00:21:00 | METOP-B | BREU BRANCO | PARÁ | Brasil | 1501782 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 85654f4b-4815-3fc1-be6f-b07f4341acf5 | -4.193 | -45.313702 | 2024-12-28 00:21:00 | METOP-B | VITORINO FREIRE | MARANHÃO | Brasil | 2113009 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 416a3584-766f-388e-8e29-31981079e2e8 | -3.7165 | -41.705101 | 2024-12-28 00:21:00 | METOP-B | PIRACURUCA | PIAUÍ | Brasil | 2208304 | 22 | 33 | nan | nan | nan | Caatinga | nan |
| 34f1bf25-2e1b-3407-91ac-9b9e348e6ff0 | -4.5731 | -45.984299 | 2024-12-28 00:21:00 | METOP-B | SANTA LUZIA | MARANHÃO | Brasil | 2110005 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3ebd7acc-2dd0-33fd-8288-cc9f8c408f63 | -3.9864 | -46.575901 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c0064048-eb86-3b75-b277-9e7f30b19c6b | -6.7273 | -44.146599 | 2024-12-28 00:21:00 | METOP-B | NOVA IORQUE | MARANHÃO | Brasil | 2107308 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| 19d418db-71fd-3882-923c-c61c47adddaa | -4.0516 | -47.044498 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c05983cb-1678-3bad-99eb-4661585f34ef | -3.8147 | -46.727001 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 37079902-5ee3-38f7-8617-4442651beeff | -3.7323 | -47.1819 | 2024-12-28 00:21:00 | METOP-B | ULIANÓPOLIS | PARÁ | Brasil | 1508126 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| ac72d848-a216-3024-b7e8-c5afe7c38fe4 | -4.0271 | -46.7094 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| b249d850-35a6-3712-9524-572418fa3e53 | -10.612 | -44.979801 | 2024-12-28 00:21:00 | METOP-B | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | nan |
| a348d052-7a91-3982-9210-63529f5a550e | -4.7309 | -44.4715 | 2024-12-28 00:21:00 | METOP-B | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| cd0a4ad7-cb40-3f2e-a64a-dbf61031e377 | -3.1946 | -46.130199 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2c0fb59c-3844-32f5-ab55-8f163d3ad2e3 | -3.9828 | -46.3335 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bb36f588-305a-33ad-bde0-3f4087ab61be | -2.6442 | -46.111 | 2024-12-28 00:21:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 79d85e28-0010-3327-8548-138cf85b1aa5 | -3.0827 | -41.893299 | 2024-12-28 00:21:00 | METOP-B | ARAIOSES | MARANHÃO | Brasil | 2100907 | 21 | 33 | nan | nan | nan | Caatinga | nan |
| b0e0b19c-671d-3456-bf41-c2d4c6a72dc0 | -2.6424 | -46.1035 | 2024-12-28 00:21:00 | METOP-B | CENTRO DO GUILHERME | MARANHÃO | Brasil | 2103158 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| dbc080db-b57b-314e-bb89-d4ce3c0df9e9 | -3.2011 | -45.978001 | 2024-12-28 00:21:00 | METOP-B | ZÉ DOCA | MARANHÃO | Brasil | 2114007 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 43285ddb-865a-37a7-aead-d317db208bf9 | -3.1071 | -46.560699 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 6fabe395-8301-3807-b5d2-7b84f7f6bbd3 | -3.8245 | -46.7248 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 7e10d10d-59ef-3c7b-a09d-867567770815 | -4.0432 | -46.7803 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 62b780f2-3c53-3350-b941-1e74fc3caf2b | -4.0157 | -46.704498 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| eba7af19-78d1-347a-8cb1-72e5e545b96f | -3.9427 | -46.973301 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9016059-9a4e-3402-b2a2-3e4ee5434c14 | -4.0238 | -46.695202 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 802f72a9-f6f2-3225-8e74-c62a1541cedc | -2.2342 | -53.6306 | 2024-12-28 00:21:00 | METOP-B | PRAINHA | PARÁ | Brasil | 1506005 | 15 | 33 | nan | nan | nan | Amazônia | nan |
| 2481acfd-6d46-36d7-a52e-845105cd7f16 | -4.0565 | -46.702801 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| c05bccc8-7162-3c3b-a7a7-3cbefeb74aca | -2.2989 | -45.59 | 2024-12-28 00:21:00 | METOP-B | TURILÂNDIA | MARANHÃO | Brasil | 2112456 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| f9aa47cd-f6b2-31ee-8486-9bda8c3b435b | -3.9251 | -46.895901 | 2024-12-28 00:21:00 | METOP-B | CENTRO NOVO DO MARANHÃO | MARANHÃO | Brasil | 2103174 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 2fa50a70-765e-36d4-9c42-1241978c95bf | -3.8736 | -46.6688 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 1b11a6b9-cd0d-3608-b5ab-9980d2e1aa1b | -3.9978 | -46.671101 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 9d08ccf2-92ef-36d5-956a-44795562b8c3 | -4.0825 | -46.726799 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| 3974a8a8-7812-3b65-9901-c1322322d0b4 | -3.9329 | -46.975498 | 2024-12-28 00:21:00 | METOP-B | ITINGA DO MARANHÃO | MARANHÃO | Brasil | 2105427 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| bf3dc085-0028-3092-a7f6-9a424e1295a8 | -4.7505 | -44.646 | 2024-12-28 00:21:00 | METOP-B | POÇÃO DE PEDRAS | MARANHÃO | Brasil | 2108900 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| f6b4f1d6-3ab1-33d5-a4f3-a3408c8e067c | -4.1447 | -46.682999 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |
| a26b63be-2eb1-348a-b5c1-adec83971eb0 | -5.9506 | -45.562302 | 2024-12-28 00:21:00 | METOP-B | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | nan |
| e7b8729c-dbca-3816-9f67-04ae41c54014 | -3.9324 | -46.655602 | 2024-12-28 00:21:00 | METOP-B | BOM JARDIM | MARANHÃO | Brasil | 2102002 | 21 | 33 | nan | nan | nan | Amazônia | nan |


[Clique aqui para ver as próximas entradas](README2.md)
