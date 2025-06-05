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

## Dados Diários - Página 7

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 9d9ba809-84f9-36c0-a477-de6c8eb4aec0 | -7.6983 | -45.77774 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| db3720d6-99f5-3956-96da-05333b7d871d | -7.01134 | -44.59931 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 9f3ede05-747e-3073-9fb9-c49f7556fae3 | -7.077 | -43.2598 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 64a5c298-b3bf-329f-8ca5-4d64e75014eb | -6.29787 | -47.01375 | 2025-06-05 04:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 7ea55fb1-d805-374b-8ea6-280813ee2eec | -6.20409 | -43.33619 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 14.8 |
| ff492ed6-b625-35af-93cc-1ef12acbf632 | -6.20325 | -48.55742 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 0980399b-2fcf-3d4f-b285-72afeccdfe93 | -6.20294 | -43.33917 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| fc9f21ed-8822-34c9-8063-2e6548d624ba | -4.55547 | -50.30428 | 2025-06-05 04:32:00 | NOAA-21 | NOVO REPARTIMENTO | PARÁ | Brasil | 1505064 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| d328a8b5-a004-368c-89bb-0089ff78f83b | -7.20264 | -43.13699 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 5.4 |
| c3a40190-63b6-3dce-8fe8-a36a6eebed4d | -6.96381 | -42.91108 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 20.0 |
| 9fb94f49-6cd5-3cf9-8424-35531dc2bab4 | -7.58744 | -45.86354 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| d761b4c5-4392-37cf-af98-4fc419f0b444 | -7.61578 | -45.74548 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 21c795a9-bb51-33a1-bc9b-29507451ac04 | -6.98306 | -47.09151 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| cd7900b9-5bab-359c-8811-f4a84d2d032b | -7.61926 | -45.74604 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 755e1470-83c7-38a4-9c1f-88cb58a010d7 | -6.29841 | -47.01026 | 2025-06-05 04:32:00 | NOAA-21 | SÃO JOÃO DO PARAÍSO | MARANHÃO | Brasil | 2111052 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2bed3621-7e18-33d9-abbb-17e77f281975 | -7.20714 | -43.13413 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.6 |
| be2c37a7-144b-3c77-a6c6-75f01ee7912d | -6.6405 | -47.34912 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7f25241e-1e19-3148-9f88-b8eae5469c1c | -7.18152 | -43.15604 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 1.4 |
| 07acc572-9f6c-3837-9707-d616e21d59ac | -6.21188 | -43.33748 | 2025-06-05 04:32:00 | NOAA-21 | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 3894d563-f450-38e6-92d9-10984f370bd8 | -6.4023 | -45.74884 | 2025-06-05 04:32:00 | NOAA-21 | FERNANDO FALCÃO | MARANHÃO | Brasil | 2104081 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| c58b2b3e-c7ec-3680-82cc-1d8ecb521197 | -6.32945 | -47.33594 | 2025-06-05 04:32:00 | NOAA-21 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 234ac92a-bb37-3f93-ba1f-5c6577cc096c | -7.68243 | -46.09576 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 760a932e-cd0a-3537-ac34-5feadce25ef6 | -7.07842 | -43.2584 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 45ab2dff-dc7f-3a7b-a323-d7d3c4ff6f0a | -7.19612 | -43.14023 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 919a3ab9-859e-39d8-9e69-c744cedcf6ac | -6.98082 | -47.08397 | 2025-06-05 04:32:00 | NOAA-21 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f4fabfed-e974-3b6f-8911-b7f9801e16ed | -6.20601 | -48.56143 | 2025-06-05 04:32:00 | NOAA-21 | SÃO GERALDO DO ARAGUAIA | PARÁ | Brasil | 1507458 | 15 | 33 | nan | nan | nan | Amazônia | 3.6 |
| 69c77945-a7a7-36e2-a939-b8f957b16091 | -7.61868 | -45.74989 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 50276640-927c-34de-8a83-476f37f30549 | -7.54702 | -45.83456 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| c95f742a-1d64-362f-bcef-d82eaecfaf7b | -7.01246 | -44.61716 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 5.9 |
| 2014dd9f-5887-39f6-9f19-47f175e8d877 | -5.92694 | -45.53119 | 2025-06-05 04:32:00 | NOAA-21 | GRAJAÚ | MARANHÃO | Brasil | 2104800 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 55255085-b4e5-3eae-8a42-5c82e81a53e4 | -7.87662 | -45.99169 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 5525b45c-8889-3457-997d-6e32ee7d6ad5 | -4.80741 | -45.26218 | 2025-06-05 04:32:00 | NOAA-21 | LAGO DA PEDRA | MARANHÃO | Brasil | 2105708 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 462d8efb-e20e-3725-a050-a93a81ba86d6 | -7.19263 | -43.13614 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 7.3 |
| 6f56abe0-b29d-373b-aef0-595de1c69cb3 | -6.46745 | -48.02585 | 2025-06-05 04:32:00 | NOAA-21 | RIACHINHO | TOCANTINS | Brasil | 1718550 | 17 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 0a09178e-daf8-359f-8b45-17573da5ab91 | -6.96943 | -42.90085 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.8 |
| e6784d18-345d-31da-a0fc-3f5823e55ac5 | -6.74375 | -44.99116 | 2025-06-05 04:32:00 | NOAA-21 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 3.7 |
| 54325eb7-fa69-35f4-b0a4-f4150d4a7057 | -8.0812 | -46.07701 | 2025-06-05 04:32:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 25908a86-3238-3c20-a5b2-0018a911b03a | -7.70236 | -45.7744 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| aebbb15c-f529-33ce-8a36-ec5ac293f7c0 | -7.70178 | -45.77828 | 2025-06-05 04:32:00 | NOAA-21 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8282ee44-69f6-35a3-a722-7dd00509491b | -7.01071 | -44.60363 | 2025-06-05 04:32:00 | NOAA-21 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 4.7 |
| c35181c3-fb76-3abe-bfbc-d05e0d11df08 | -4.81961 | -44.35638 | 2025-06-05 04:32:00 | NOAA-21 | SANTO ANTÔNIO DOS LOPES | MARANHÃO | Brasil | 2110302 | 21 | 33 | nan | nan | nan | Cerrado | 1.9 |
| d5a31146-e9c9-3420-9a19-6846f94febd8 | -5.4183 | -47.57092 | 2025-06-05 04:32:00 | NOAA-21 | IMPERATRIZ | MARANHÃO | Brasil | 2105302 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 08fadcea-1076-385c-ad06-133720a2009b | -7.19663 | -43.13676 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| 0854edf8-8fbe-3d10-be32-55600d74e64e | -7.67555 | -46.0947 | 2025-06-05 04:32:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 404f63b8-67d1-39d5-afa1-3c1873ba22f4 | -6.96329 | -42.91469 | 2025-06-05 04:32:00 | NOAA-21 | FLORIANO | PIAUÍ | Brasil | 2203909 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 78f5955c-bda8-35f0-b8b0-3adaacded384 | -11.55147 | -47.31599 | 2025-06-05 04:34:00 | NOAA-21 | ALMAS | TOCANTINS | Brasil | 1700400 | 17 | 33 | nan | nan | nan | Cerrado | 2.8 |
| b1e438c0-8e95-3941-9190-a02a80592a86 | -12.6514 | -54.1283 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| 72835460-a2c0-3ca5-8255-fbda24a253da | -8.449 | -46.47766 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 07208363-403a-3f67-8592-5f0093cf3591 | -13.14781 | -56.80992 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Amazônia | 1.7 |
| ffab6b1e-ac0d-35b5-8b35-3582e6bd8e69 | -8.45868 | -46.48294 | 2025-06-05 04:34:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| a5a01760-45e1-3edc-954c-90b8a68b114d | -14.73179 | -45.09495 | 2025-06-05 04:34:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| dc3c9031-d121-3ade-9224-41933e8a20df | -9.50082 | -57.14706 | 2025-06-05 04:34:00 | NOAA-21 | APIACÁS | MATO GROSSO | Brasil | 5100805 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| d7c91e7d-1f7e-3c8d-b8be-46f7490b8766 | -10.30805 | -57.14173 | 2025-06-05 04:34:00 | NOAA-21 | NOVA MONTE VERDE | MATO GROSSO | Brasil | 5108956 | 51 | 33 | nan | nan | nan | Amazônia | 1.0 |
| 7ea3418e-50c2-3f3b-9088-eabead51de5a | -11.83097 | -51.2872 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 8eab4165-af47-3274-97aa-8b44650471b0 | -9.70494 | -48.90817 | 2025-06-05 04:34:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| b97da0c7-c897-331a-a247-6c674d839985 | -9.82242 | -48.04204 | 2025-06-05 04:34:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 2823eaff-f9ec-3505-9990-332216cbf207 | -13.51982 | -56.59117 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4b6d632b-18aa-33ee-994e-cf64f2f0747e | -11.14166 | -53.94803 | 2025-06-05 04:34:00 | NOAA-21 | MARCELÂNDIA | MATO GROSSO | Brasil | 5105580 | 51 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 64515386-de38-3fc7-86e1-f17ef74f9f4c | -13.53643 | -56.55895 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 7b582aa1-2fcd-34b0-9030-770d735d60a4 | -8.94809 | -47.29422 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4533004b-555a-3a4a-8874-0fad8353a2ec | -14.28335 | -47.98618 | 2025-06-05 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| d2d068cd-97e5-3d42-9baa-b9f1da754046 | -14.11757 | -45.10883 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c99f8b0c-1533-3a1a-9d79-8f4f1c8928a0 | -9.35893 | -47.69583 | 2025-06-05 04:34:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| a9b6cdeb-02a2-3db1-bd49-7be69f89ff81 | -14.22536 | -45.47829 | 2025-06-05 04:34:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ddd63186-e298-3b9b-969e-f29d065bef8c | -12.65232 | -54.12316 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 0.5 |
| f1a10915-f831-33c9-b91a-dc41c7435d33 | -12.66178 | -58.21745 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 32f418a0-27cb-3f36-b018-988cce22ba95 | -16.06901 | -43.6554 | 2025-06-05 04:34:00 | NOAA-21 | CAPITÃO ENÉAS | MINAS GERAIS | Brasil | 3112703 | 31 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4ea451d4-1577-3f19-b3bd-4a7a21197313 | -8.9442 | -47.29727 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 70a58725-062b-386a-aed9-39ce2299a004 | -10.05184 | -49.66122 | 2025-06-05 04:34:00 | NOAA-21 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| c6696933-89a2-3bfa-ac29-ac089a1c6c32 | -13.53192 | -56.55806 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 8eed242c-033d-35f1-afec-4a44d7b87a6b | -12.12466 | -54.6602 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| b6d68fe7-15fb-3531-925a-5b69189aa98e | -13.5147 | -56.55012 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 725b8ce6-e8e9-3691-9f62-251a4f4cff73 | -10.85369 | -46.85154 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| f505a883-9010-3b71-8b9e-529fc4b02682 | -13.50348 | -56.57801 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 4b480e57-1bd2-3b11-88ed-5d6aa7e1a330 | -10.8491 | -46.8353 | 2025-06-05 04:34:00 | NOAA-21 | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 064d2387-c403-3674-9899-1bc55455d2a0 | -13.51877 | -56.57117 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 18.0 |
| 4153b3b8-ceba-337d-b9e8-67668467395c | -13.51206 | -56.56404 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 19.1 |
| b5232efa-1dcc-3511-beed-a09f44fdc795 | -12.64718 | -54.13001 | 2025-06-05 04:34:00 | NOAA-21 | PARANATINGA | MATO GROSSO | Brasil | 5106307 | 51 | 33 | nan | nan | nan | Amazônia | 1.3 |
| f85c9133-453f-39f4-a869-20a6ca63869c | -12.12407 | -54.65978 | 2025-06-05 04:34:00 | NOAA-21 | FELIZ NATAL | MATO GROSSO | Brasil | 5103700 | 51 | 33 | nan | nan | nan | Amazônia | 0.6 |
| f51ff4f2-a01b-3e27-8d13-812421bf2932 | -11.8316 | -51.28339 | 2025-06-05 04:34:00 | NOAA-21 | SERRA NOVA DOURADA | MATO GROSSO | Brasil | 5107883 | 51 | 33 | nan | nan | nan | Cerrado | 2.3 |
| be367ed0-3644-33b4-9514-8f375d937531 | -13.09166 | -52.04689 | 2025-06-05 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7cdd1726-72f0-3840-83e0-759408155f28 | -13.52751 | -56.54874 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| be38ee6c-e013-3932-aef8-16b56c811f29 | -8.73262 | -47.98465 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 3888bf5c-a86c-39bf-9546-267b1daa4d89 | -11.43209 | -45.10503 | 2025-06-05 04:34:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 2cbdd1c3-e985-3c55-b475-7904a4040fa2 | -11.57117 | -47.44719 | 2025-06-05 04:34:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a355102b-6354-3722-9b15-9e60af6fb46c | -13.09646 | -52.03955 | 2025-06-05 04:34:00 | NOAA-21 | RIBEIRÃO CASCALHEIRA | MATO GROSSO | Brasil | 5107180 | 51 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 02ada086-fc47-3c99-93e6-2dcb7bc37ba5 | -14.28281 | -47.98985 | 2025-06-05 04:34:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.8 |
| b3e4bb1d-37f9-3dae-95ce-64a3674069f0 | -12.66823 | -58.2233 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.5 |
| 873bbabe-124b-38b9-a7b2-7b1db4e252e8 | -8.95698 | -47.28094 | 2025-06-05 04:34:00 | NOAA-21 | CENTENÁRIO | TOCANTINS | Brasil | 1704105 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| e7b696cd-bc13-3e4a-83be-8878a15e07b4 | -13.3133 | -47.93278 | 2025-06-05 04:34:00 | NOAA-21 | CAVALCANTE | GOIÁS | Brasil | 5205307 | 52 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 685f75c8-1a7e-3cc5-bbc9-08610149a5a1 | -13.5275 | -56.5815 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 0.9 |
| e7dcc432-10b6-397d-9637-c715b37484aa | -12.37557 | -45.92522 | 2025-06-05 04:34:00 | NOAA-21 | LUÍS EDUARDO MAGALHÃES | BAHIA | Brasil | 2919553 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 92648e60-ebc8-30b9-a59e-e46bc541e9c0 | -13.51029 | -56.57336 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 7.3 |
| 62a31f1c-b7b0-37a8-9825-3d34ba6d0bec | -13.53035 | -56.55889 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 41c73892-53cb-3083-9a54-f2d8f8b29109 | -10.00814 | -47.67376 | 2025-06-05 04:34:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 6784fd7a-dd9b-361f-80f4-35cf9e8b0c29 | -11.96312 | -49.52164 | 2025-06-05 04:34:00 | NOAA-21 | FORMOSO DO ARAGUAIA | TOCANTINS | Brasil | 1708205 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| dff8c1c8-983e-33fc-aa6f-7a0919e42d65 | -8.74541 | -48.03292 | 2025-06-05 04:34:00 | NOAA-21 | SANTA MARIA DO TOCANTINS | TOCANTINS | Brasil | 1718881 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| f4596c27-f037-30bf-bd0e-e79bc8cdbb61 | -11.54875 | -56.43244 | 2025-06-05 04:34:00 | NOAA-21 | PORTO DOS GAÚCHOS | MATO GROSSO | Brasil | 5106802 | 51 | 33 | nan | nan | nan | Amazônia | 3.9 |
| cf1ae007-6455-3202-9b5f-11c4e9034cda | -13.51166 | -56.58455 | 2025-06-05 04:34:00 | NOAA-21 | SÃO JOSÉ DO RIO CLARO | MATO GROSSO | Brasil | 5107305 | 51 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1784ab47-d287-3872-be4e-834d47786328 | -12.66689 | -58.21851 | 2025-06-05 04:34:00 | NOAA-21 | BRASNORTE | MATO GROSSO | Brasil | 5101902 | 51 | 33 | nan | nan | nan | Cerrado | 7.9 |


[Clique aqui para ver as próximas entradas](README8.md)
