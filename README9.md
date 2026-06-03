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

## Dados Diários - Página 9

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 94d3ff79-44b7-30b3-8964-099ab0bafe7c | -18.72038 | -56.57719 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.1 |
| 60ab2d05-843b-3594-a9da-b57e90636895 | -18.72098 | -56.57349 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 23267d44-6821-3bc1-ba28-216b7699a46c | -15.23478 | -48.56891 | 2026-06-03 05:04:00 | NPP-375D | VILA PROPÍCIO | GOIÁS | Brasil | 5222302 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 639374dd-66bf-3a47-bee5-285ab709f9cf | -16.57708 | -45.87994 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2b9bd110-02f9-3e42-813b-e9bddfad3e4a | -20.88723 | -48.98212 | 2026-06-03 05:04:00 | NPP-375D | TABAPUÃ | SÃO PAULO | Brasil | 3552601 | 35 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2a3e8ab0-78bf-3afd-b8c7-e0c37927ff77 | -19.16789 | -55.18759 | 2026-06-03 05:04:00 | NPP-375D | RIO VERDE DE MATO GROSSO | MATO GROSSO DO SUL | Brasil | 5007406 | 50 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 293f6d23-498d-3e7b-bd16-b22c5b70bc66 | -16.17923 | -58.47607 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 96a5fee2-7b95-3144-ba3d-06b216423208 | -17.44336 | -42.62688 | 2026-06-03 05:04:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 97c792a1-e32e-3601-8aeb-e8ace4834a6b | -18.48758 | -55.54353 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.5 |
| ee9cb75d-f9bc-30a8-8350-d45cd05eb535 | -18.72494 | -56.57039 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 154b9b34-60b3-35b5-b66b-6f47305ffe50 | -16.13898 | -58.49117 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| b4456da7-639f-3d88-990e-f6d7288a4c11 | -17.43798 | -42.63223 | 2026-06-03 05:04:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 6778f4a9-9994-3562-b7b9-46d7edb41ca0 | -16.58484 | -45.88378 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| bf940b4c-91e7-3f58-9126-5d946a507be6 | -16.58559 | -45.87696 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 922ecee6-c9d9-3466-b9c9-14c54765b6f8 | -16.14263 | -58.49184 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 4.7 |
| 5ed6b296-a65b-3d18-8e26-e2ad45977966 | -16.57951 | -45.88308 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 832f8a5d-f290-3cc0-8ce7-9e1b22de052c | -18.71703 | -56.57659 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 0.8 |
| e894ef49-d5ef-39ea-9072-85e799f28b06 | -16.9162 | -51.85489 | 2026-06-03 05:04:00 | NPP-375D | CAIAPÔNIA | GOIÁS | Brasil | 5204409 | 52 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 04fc660e-ba10-3c5a-b18e-b2487e303dcd | -12.80838 | -54.86025 | 2026-06-03 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| ee4a0609-1146-336a-8a4c-464009ac861f | -16.58202 | -45.88406 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 5.3 |
| 780a6bea-dbc3-32b1-b0e7-ca63d5eba1a8 | -14.08671 | -59.38368 | 2026-06-03 05:04:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 8f0465df-af1d-3922-ac1b-1edd635b79e7 | -13.65988 | -55.03781 | 2026-06-03 05:04:00 | NPP-375D | NOVA UBIRATÃ | MATO GROSSO | Brasil | 5106240 | 51 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 02ef09a2-8e40-360f-ab60-ecf787fc8a9a | -17.44283 | -42.63268 | 2026-06-03 05:04:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 6.4 |
| 9959d51e-abe7-3a1e-a5da-8e09a3d9d222 | -17.44457 | -42.63306 | 2026-06-03 05:04:00 | NPP-375D | VEREDINHA | MINAS GERAIS | Brasil | 3171071 | 31 | 33 | nan | nan | nan | Cerrado | 3.0 |
| f6e7abd9-9005-32c5-a0d4-14824f67a464 | -14.08763 | -59.3786 | 2026-06-03 05:04:00 | NPP-375D | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4e5160b9-1bcf-35b4-a7ca-34c186451421 | -16.17823 | -58.47863 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 8d031a19-d150-391d-b816-385f8e6d8a2d | -16.18188 | -58.47932 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.6 |
| 7b599fc7-0d42-3436-a644-e5bc065e2dd6 | -14.18819 | -52.87773 | 2026-06-03 05:04:00 | NPP-375D | ÁGUA BOA | MATO GROSSO | Brasil | 5100201 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 9d6a2af7-1e58-30bc-affb-3cd7a815c8b4 | -18.72433 | -56.5741 | 2026-06-03 05:04:00 | NPP-375D | CORUMBÁ | MATO GROSSO DO SUL | Brasil | 5003207 | 50 | 33 | nan | nan | nan | Pantanal | 1.4 |
| 43a0b530-86e1-33fd-b617-4c395b769dc1 | -16.57748 | -45.87655 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 2.5 |
| e6fd7df0-e4b8-3837-acd7-a69efdaafd1d | -16.13822 | -58.49553 | 2026-06-03 05:04:00 | NPP-375D | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.2 |
| 6288e5b7-7895-30f1-9f25-0aa226b82c68 | -16.58025 | -45.87626 | 2026-06-03 05:04:00 | NPP-375D | SANTA FÉ DE MINAS | MINAS GERAIS | Brasil | 3157609 | 31 | 33 | nan | nan | nan | Cerrado | 3.6 |
| e1384665-4629-3a67-9227-3b10b215f60a | -20.55049 | -47.20362 | 2026-06-03 05:04:00 | NPP-375D | FRANCA | SÃO PAULO | Brasil | 3516200 | 35 | 33 | nan | nan | nan | Cerrado | 0.7 |
| c680f98b-6ed8-3d1c-919c-e9b44d7c32f8 | -21.80965 | -49.12046 | 2026-06-03 05:06:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| a5ccb30c-b365-3260-84fe-accec22c98a7 | -21.81483 | -49.11613 | 2026-06-03 05:06:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| bea71684-d6a8-3fd9-83e2-0c057ce82620 | -21.81889 | -49.12156 | 2026-06-03 05:06:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 1fb86ef4-7842-3214-8a41-60a2b57b2107 | -21.30136 | -56.87542 | 2026-06-03 05:06:00 | NPP-375D | PORTO MURTINHO | MATO GROSSO DO SUL | Brasil | 5006903 | 50 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5a2074c5-0823-3537-99fe-578e671eef0d | -22.96084 | -52.69855 | 2026-06-03 05:06:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 2a871104-d34b-3ca8-845c-dc968d0f795d | -22.96461 | -52.6991 | 2026-06-03 05:06:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| dc3f5572-1c52-3cdd-b4eb-627bc3b64afc | -22.96148 | -52.69368 | 2026-06-03 05:06:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.0 |
| 8f37d23b-96af-3dc9-a1a6-51183cffd6c8 | -21.81427 | -49.12103 | 2026-06-03 05:06:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| 6a4d7258-adee-3941-8fd6-95437f8d8182 | -22.78974 | -49.33803 | 2026-06-03 05:06:00 | NPP-375D | ÁGUAS DE SANTA BÁRBARA | SÃO PAULO | Brasil | 3500550 | 35 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 986aadd6-7ba8-3354-8f50-04cd0d8627d2 | -21.29484 | -56.10593 | 2026-06-03 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| e7340371-3bcf-3a43-b7ee-1e706cfefff2 | -21.29151 | -56.10533 | 2026-06-03 05:06:00 | NPP-375D | NIOAQUE | MATO GROSSO DO SUL | Brasil | 5005806 | 50 | 33 | nan | nan | nan | Cerrado | 0.5 |
| a3c921aa-261e-353f-b639-bbcd7f28f8ec | -22.96526 | -52.6942 | 2026-06-03 05:06:00 | NPP-375D | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 1.1 |
| 2c456b00-c284-3079-9e0b-f6a68f932460 | -21.8102 | -49.11559 | 2026-06-03 05:06:00 | NPP-375D | IACANGA | SÃO PAULO | Brasil | 3519105 | 35 | 33 | nan | nan | nan | Mata Atlântica | 2.7 |
| fca03b69-ed81-311b-a64c-30d18abd7c3a | -21.70096 | -48.41179 | 2026-06-03 05:06:00 | NPP-375D | MATÃO | SÃO PAULO | Brasil | 3529302 | 35 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 6e2d1483-8d07-3579-92dc-1a6bdea0cb4c | -27.37641 | -51.46628 | 2026-06-03 05:08:00 | NPP-375D | CAMPOS NOVOS | SANTA CATARINA | Brasil | 4203600 | 42 | 33 | nan | nan | nan | Mata Atlântica | 0.9 |
| 85052702-88f7-3e31-8f15-feef37f3cf34 | -8.06133 | -46.18658 | 2026-06-03 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 5.5 |
| c1b0627b-c87f-3f94-8069-db4eba6dd736 | -9.18132 | -58.06009 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 2.0 |
| d97e311f-e6d9-3531-a2f2-cd366e16a019 | -9.88974 | -52.44201 | 2026-06-03 05:21:00 | NOAA-20 | SANTA CRUZ DO XINGU | MATO GROSSO | Brasil | 5107743 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64b35eab-9478-3521-9a6c-a94c184eac57 | -5.72878 | -45.03547 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 6.3 |
| 3b72e441-a524-333d-84c7-cbaae835f4c8 | -5.72165 | -45.03449 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 2bc233ec-ab80-3d4e-a41a-4c32b1a59592 | -7.35185 | -49.82264 | 2026-06-03 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 3.8 |
| f2c4fafe-d415-344c-929f-92d060037078 | -7.50757 | -55.00034 | 2026-06-03 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.7 |
| 4a569218-c433-3796-9bcf-1ae4a04383e7 | -7.35138 | -49.82613 | 2026-06-03 05:21:00 | NOAA-20 | RIO MARIA | PARÁ | Brasil | 1506161 | 15 | 33 | nan | nan | nan | Amazônia | 2.6 |
| 809e4666-3e9a-3d3a-8e35-45ea01e11b5a | -5.72262 | -45.0275 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 9.4 |
| 064af94a-c375-3b79-b390-2e7e57f93cce | -7.50687 | -55.00506 | 2026-06-03 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 5.6 |
| 7e7d8560-6c5e-33d4-bbc1-24cc05d15b21 | -9.18188 | -58.05644 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| a74f0692-a45a-3eaa-9615-8f8c77ebf4c0 | -10.55403 | -46.62775 | 2026-06-03 05:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 95b89281-f8ce-3630-8033-0c70c5c0b53f | -7.50305 | -55.00445 | 2026-06-03 05:21:00 | NOAA-20 | ALTAMIRA | PARÁ | Brasil | 1500602 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 791c0ffd-248f-3f62-a471-70907e31bdfc | -6.76814 | -58.9706 | 2026-06-03 05:21:00 | NOAA-20 | APUÍ | AMAZONAS | Brasil | 1300144 | 13 | 33 | nan | nan | nan | Amazônia | 0.9 |
| bedaf76b-e2ee-3b66-8f15-75cbbc3795f1 | -9.18526 | -58.05697 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 2f22c5b4-d453-3f55-ac6c-af300ee7f8b4 | -5.72497 | -45.03439 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 857a4c22-aea2-3a38-b947-30d61b8904a9 | -7.26834 | -46.80862 | 2026-06-03 05:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 22718eef-98c8-3420-8926-fc36d0885a2f | -7.26761 | -46.81408 | 2026-06-03 05:21:00 | NOAA-20 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dbde114-2209-37e0-b44e-7ec06141d1cd | -5.72404 | -45.04146 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 11.6 |
| 29ee5f52-d3b2-3fa9-abd0-1add00d8fe2e | -10.54021 | -46.62638 | 2026-06-03 05:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 8e148bf7-57b1-323c-909c-9cec3661d0b1 | -9.17906 | -58.05226 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| e4dd7a1b-2e9b-3e6a-9fc9-b3d2b72ad0c7 | -8.06209 | -46.1806 | 2026-06-03 05:21:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 614f60bd-10f5-3ba0-a1d3-37e6d812b081 | -9.18582 | -58.05331 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| 7e461419-46dc-3993-bb0f-d309b5fce75d | -9.18244 | -58.05278 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| f1413481-e4b4-36ff-80b1-9a22550a8b0a | -10.54713 | -46.62695 | 2026-06-03 05:21:00 | NOAA-20 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 5369cd66-4c38-3518-8f18-d2e5b9ba6dd4 | -9.19258 | -58.05439 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| bf4e5c3c-b7c8-399b-a1d9-23f71b0f4649 | -9.1785 | -58.0559 | 2026-06-03 05:21:00 | NOAA-20 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 4.1 |
| 338b0a93-2713-3f27-a0c6-71f7a36ae49c | -5.7259 | -45.02736 | 2026-06-03 05:21:00 | NOAA-20 | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 14.2 |
| ed06a642-7bfc-3e5e-9f5c-aaead203585d | -11.75728 | -47.07074 | 2026-06-03 05:23:00 | NOAA-20 | DIANÓPOLIS | TOCANTINS | Brasil | 1707009 | 17 | 33 | nan | nan | nan | Cerrado | 8.6 |
| 141a6aa4-0903-3d57-9df5-1125d0b155c6 | -14.08134 | -59.37435 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 214d0586-08d5-3178-8cec-e651009ff2ea | -10.90725 | -54.13413 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 77ac32c1-9c23-302a-8aa7-a8641b799e9b | -14.08078 | -59.37803 | 2026-06-03 05:23:00 | NOAA-20 | NOVA LACERDA | MATO GROSSO | Brasil | 5106182 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7946275-6559-392f-87ca-5333602ccdb6 | -16.59723 | -58.23658 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 0.9 |
| f1734ad7-665d-3aad-b562-e462e8fb1e25 | -11.56767 | -54.5887 | 2026-06-03 05:23:00 | NOAA-20 | UNIÃO DO SUL | MATO GROSSO | Brasil | 5108303 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| aeec0d9c-3bec-30e0-91a2-85f891376b16 | -22.96 | -52.69516 | 2026-06-03 05:23:00 | NOAA-20 | GUAIRAÇÁ | PARANÁ | Brasil | 4108908 | 41 | 33 | nan | nan | nan | Mata Atlântica | 0.6 |
| e2a833fa-6132-3618-9954-86ac5d964374 | -11.62569 | -55.17601 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 8d824db2-02b7-31dc-96f7-2923fff03570 | -12.4367 | -58.40277 | 2026-06-03 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 12530b51-85bf-3685-85c8-1f67f0a370e4 | -14.02897 | -59.56028 | 2026-06-03 05:23:00 | NOAA-20 | COMODORO | MATO GROSSO | Brasil | 5103304 | 51 | 33 | nan | nan | nan | Cerrado | 0.5 |
| db56eb0e-c454-3be5-88d9-a68131f6951a | -14.1396 | -58.96544 | 2026-06-03 05:23:00 | NOAA-20 | TANGARÁ DA SERRA | MATO GROSSO | Brasil | 5107958 | 51 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 202ed38b-61b8-3855-b2aa-aaad0a7a93c0 | -16.1444 | -58.49434 | 2026-06-03 05:23:00 | NOAA-20 | CÁCERES | MATO GROSSO | Brasil | 5102504 | 51 | 33 | nan | nan | nan | Pantanal | 2.6 |
| 5a54b5de-bad7-3957-a4e2-155c4d5d34fa | -10.5722 | -57.32626 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| b62442f2-71f7-3ee4-ace7-83c13bc5b9e6 | -12.73939 | -54.20121 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 5bd692f4-69ec-36e4-8c6a-67dd773aed6d | -10.86353 | -53.74351 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 7b23ea98-1477-30d7-a851-42d0eebe63ac | -11.20877 | -54.98619 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 1f4ef094-a08a-3bcb-9c98-5668f51e8df2 | -10.85797 | -53.75147 | 2026-06-03 05:23:00 | NOAA-20 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 0.8 |
| e2616f51-fd58-3a87-8812-bfb920f28702 | -12.73823 | -54.19779 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f88f9b9-4d3e-3799-b5a7-9cec7893b856 | -12.43612 | -58.40655 | 2026-06-03 05:23:00 | NOAA-20 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| b2251a12-5916-3206-8cb8-72550a5aab0f | -12.72784 | -54.20905 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |
| db82f319-0a55-3c7a-8a38-9f56cdd91256 | -11.88159 | -57.8417 | 2026-06-03 05:23:00 | NOAA-20 | JUARA | MATO GROSSO | Brasil | 5105101 | 51 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 54af1678-7609-309f-ba45-40239054b2a8 | -11.63369 | -55.17716 | 2026-06-03 05:23:00 | NOAA-20 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| cb73eec5-1b4e-33fe-aba2-efbba6ec6d9d | -12.73649 | -54.21039 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| ad02fe85-9ed7-32e9-a80f-e03ae73eb294 | -12.73707 | -54.20618 | 2026-06-03 05:23:00 | NOAA-20 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.1 |


[Clique aqui para ver as próximas entradas](README10.md)
