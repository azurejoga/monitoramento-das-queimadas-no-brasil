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

## Dados Diários - Página 30

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 300bbf6e-430a-3c99-80d7-4a532f595cde | -7.68766 | -42.57425 | 2025-10-14 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| fd8261ba-a0f5-3648-ac3c-5b32562b749c | -7.94785 | -44.11633 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 5d32900f-779b-3131-8234-0f079113fdbd | -7.30648 | -46.68135 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.5 |
| 65466144-4a7c-3d77-aa6b-7eca98b865a9 | -7.49945 | -43.06338 | 2025-10-14 04:25:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 4.7 |
| f6d5318f-44e5-30e7-89be-f0ff0d217c04 | -12.84048 | -50.6507 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 6cd0f0b5-2c34-31e0-a2a3-f763b26df97b | -7.48795 | -45.13129 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 00079471-fe48-3bee-b999-c929d6267e09 | -6.84754 | -47.64272 | 2025-10-14 04:25:00 | NOAA-20 | DARCINÓPOLIS | TOCANTINS | Brasil | 1706506 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 3cc354a8-7414-38b7-b572-63c9dc9d2ee2 | -10.36377 | -44.98124 | 2025-10-14 04:25:00 | NOAA-20 | CORRENTE | PIAUÍ | Brasil | 2202901 | 22 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d7e13798-9c8a-3673-ac12-180fb2d629ac | -12.85336 | -50.64004 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| e23980dd-f148-3db6-872a-76d360eca27d | -7.29135 | -41.96309 | 2025-10-14 04:25:00 | NOAA-20 | WALL FERRAZ | PIAUÍ | Brasil | 2211704 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| dfcdbd5e-8414-3579-ba82-1d7b56b20237 | -7.74969 | -42.44014 | 2025-10-14 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 3.3 |
| 972b19b9-0247-388e-84fe-29f9a5b32fc5 | -7.92586 | -44.12084 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 71553ffb-226d-305e-907b-afecdacabaf8 | -7.94091 | -44.11528 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 09d0c7fd-b780-30d8-85cd-400df1557228 | -10.15276 | -44.91871 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| a2e9ff3f-db9d-3403-8798-942f2976523e | -12.79317 | -50.64665 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 7e7f8358-d103-343a-8d25-8320bb5af4ce | -8.4246 | -46.22704 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.2 |
| baa66f4a-9d2e-31e3-9f35-25f4dfb2fba4 | -7.94209 | -44.10758 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 2b16781d-3987-3da8-ae97-82c8ea7ddce0 | -13.97684 | -42.50751 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.0 |
| f8f565ff-0eaa-32d3-908f-4e51a20afeaf | -10.20616 | -48.0761 | 2025-10-14 04:25:00 | NOAA-20 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d8a77ec2-90d9-36d8-bee2-4138a5827a17 | -7.02758 | -46.25367 | 2025-10-14 04:25:00 | NOAA-20 | NOVA COLINAS | MARANHÃO | Brasil | 2107258 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 3dea74b3-501f-35df-b870-24d6eda35c64 | -12.85407 | -50.63585 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 0571a291-b601-342c-8e9a-e2f001eef3a6 | -13.53652 | -43.01155 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 9.2 |
| 85af750c-4228-3e52-96ca-2fd5027ba824 | -7.54072 | -45.81985 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 7b890085-72af-3c9a-99bc-2507c72bc7f2 | -6.3822 | -47.26036 | 2025-10-14 04:25:00 | NOAA-20 | PORTO FRANCO | MARANHÃO | Brasil | 2109007 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 89bd5e4a-2b4e-3d4e-a535-1d230ecfd7ae | -7.74751 | -45.71339 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 934a2086-161a-303d-9316-119573e6589d | -7.75954 | -44.72298 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 887a880a-b84e-34cc-af60-4ca52d2f3927 | -10.13811 | -44.55338 | 2025-10-14 04:25:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 04954d6d-3856-37e3-ac78-8d7ce6396782 | -12.83903 | -50.6375 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c6244691-777c-305c-a749-c36b09dc64de | -12.80034 | -50.64792 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 10.5 |
| 7bc22132-7081-3de2-b0f1-586e81f3cbdc | -11.52388 | -43.52603 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.4 |
| ac771918-7af6-3a33-a0b4-1886f72ade8b | -9.48959 | -43.06536 | 2025-10-14 04:25:00 | NOAA-20 | CAMPO ALEGRE DE LOURDES | BAHIA | Brasil | 2905909 | 29 | 33 | nan | nan | nan | Caatinga | 1.6 |
| 6596eaea-fdd7-302f-8178-2e55b7f23f5a | -6.69714 | -45.9782 | 2025-10-14 04:25:00 | NOAA-20 | FORTALEZA DOS NOGUEIRAS | MARANHÃO | Brasil | 2104107 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 7043a00d-43c5-3459-9442-d8b986d46d39 | -8.45644 | -46.15364 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 3895c60e-c8c6-3d4a-a963-5aa782be7beb | -9.16207 | -41.05946 | 2025-10-14 04:25:00 | NOAA-20 | CASA NOVA | BAHIA | Brasil | 2907202 | 29 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 4229cfcf-b5dd-334d-bb81-e9b9f3a9145e | -12.83116 | -50.64042 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 6e727fc4-9911-3626-9faa-f1f4d83c0e7c | -7.75414 | -45.71445 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 7876b444-f2d7-3f43-8535-967900533d80 | -13.84354 | -42.38609 | 2025-10-14 04:25:00 | NOAA-20 | CAETITÉ | BAHIA | Brasil | 2905206 | 29 | 33 | nan | nan | nan | Caatinga | 3.3 |
| f9e2deab-868d-3b92-a45c-2d51e89e09a6 | -12.79918 | -50.64492 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d4bf6144-b2b7-3e36-8fdf-77a518c1f06b | -12.81253 | -50.64144 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| f09d8b46-198e-3e4c-9aa2-8e458bec7f09 | -12.7956 | -50.64428 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 6.5 |
| 28e318f3-ad6e-31d7-bc31-4f0b2b4c5240 | -12.20945 | -51.02657 | 2025-10-14 04:25:00 | NOAA-20 | NOVO SANTO ANTÔNIO | MATO GROSSO | Brasil | 5106315 | 51 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 17f1e6e9-5434-3299-a608-8289163f8307 | -12.80894 | -50.64081 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 25.5 |
| 1f716be5-03dc-360f-94c3-447fd7b48d70 | -7.16121 | -42.1869 | 2025-10-14 04:25:00 | NOAA-20 | COLÔNIA DO PIAUÍ | PIAUÍ | Brasil | 2202778 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| 257ad34d-66d5-39d7-aedb-0791410336a1 | -7.67359 | -42.37898 | 2025-10-14 04:25:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| 243967e8-a1a9-3a4a-94ea-0a5f04c81d46 | -12.79819 | -50.6389 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f527e6bd-034b-3a68-b40d-3a54295489f6 | -7.53078 | -45.81828 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 0537cf3f-aab4-3521-b16d-54ec11563336 | -12.83474 | -50.64105 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 12.4 |
| 0638ecaa-36bc-3275-8ee0-983e421d0ff4 | -11.01182 | -44.53532 | 2025-10-14 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 6996d732-828b-33c1-bc66-abf07dd299cd | -12.84119 | -50.64651 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 5.2 |
| 0e36ee3b-8ad3-3e69-9c89-32145cb3aa74 | -7.94379 | -44.11966 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 16.9 |
| af6ded3d-7bb5-36f6-a831-f735c21cbe52 | -6.87527 | -46.97695 | 2025-10-14 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 17b52265-320a-309a-b020-661d6aea18d8 | -10.82613 | -43.98186 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 11f8f829-31d1-3afa-bf6d-76e5ff78bd22 | -10.79702 | -44.30437 | 2025-10-14 04:25:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8d6b6301-5340-34a0-a3aa-af5e98ad1615 | -7.81145 | -42.44136 | 2025-10-14 04:25:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.7 |
| ce5a88d2-3437-3299-bbb6-8796c0b63705 | -5.7212 | -51.35489 | 2025-10-14 04:25:00 | NOAA-20 | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 0.8 |
| 681bce89-c20f-3437-b88d-1491f9f0b0fd | -6.98671 | -47.08854 | 2025-10-14 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 4.3 |
| 76ab245d-02d7-3a2c-84d2-fc91a2c68778 | -10.80815 | -43.95382 | 2025-10-14 04:25:00 | NOAA-20 | MANSIDÃO | BAHIA | Brasil | 2920452 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 0913a660-4c08-3385-a543-69ad1a72f498 | -7.95302 | -44.12889 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 12.6 |
| 2b87b172-aa48-3aad-9e22-061208f657fb | -12.824 | -50.66075 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac79bbb9-3717-354f-b9bb-1e4bf060b50c | -7.42477 | -45.41097 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 8d5a2a2f-e3dc-33e6-9ea5-afbfedb3414b | -6.90312 | -45.66246 | 2025-10-14 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 308f0081-a29e-357b-9163-f3655e1fcc9b | -7.91148 | -45.01001 | 2025-10-14 04:25:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.7 |
| dc7a4487-a563-3e54-9a20-fa9281c386fe | -7.90933 | -47.20746 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.2 |
| 9a6be4af-dfd0-3432-843a-5042a01983df | -9.25104 | -44.37611 | 2025-10-14 04:25:00 | NOAA-20 | BOM JESUS | PIAUÍ | Brasil | 2201903 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 7adc14d8-49da-35d0-92d8-7d10ed75dc7d | -6.90258 | -45.66594 | 2025-10-14 04:25:00 | NOAA-20 | SÃO RAIMUNDO DAS MANGABEIRAS | MARANHÃO | Brasil | 2111607 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 4ad45114-b0bd-3f4e-9076-1ae84ba0bbc6 | -7.74823 | -44.72873 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f2496611-3e87-3729-8a6c-d2d198d40fe6 | -7.95509 | -47.78674 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| c4f8ad29-5510-305d-b9f5-6fb24e479445 | -7.92181 | -44.12415 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 8.9 |
| 62a7a2ba-8bfd-3137-b1b9-3b9cb936beea | -7.2319 | -45.32001 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 552d00a1-9ff3-31d2-8573-7d31becfc809 | -13.63471 | -42.85307 | 2025-10-14 04:25:00 | NOAA-20 | RIACHO DE SANTANA | BAHIA | Brasil | 2926400 | 29 | 33 | nan | nan | nan | Caatinga | 1.3 |
| 7b041f81-b2a0-3fe2-9e56-57517f68c21e | -7.42422 | -45.41449 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 36db9e98-52b2-332c-a8ab-bce7f9e6c598 | -12.82614 | -50.64816 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| 50c8513c-6f9d-33bc-8eaa-8cd18006c293 | -7.52707 | -42.69762 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 3.6 |
| 5cd97076-9c17-37e9-8474-41deb9128140 | -7.87816 | -47.27461 | 2025-10-14 04:25:00 | NOAA-20 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 6a235724-e34a-33c6-9a0a-bac699c51848 | -7.75469 | -45.71095 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 32cc4a64-0f26-39d6-a238-3b7c9d68e853 | -7.93685 | -44.1186 | 2025-10-14 04:25:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 32c09f52-b334-38e5-8b3f-fc8341a003ae | -11.56256 | -44.05242 | 2025-10-14 04:25:00 | NOAA-20 | WANDERLEY | BAHIA | Brasil | 2933455 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 580ce07d-c1c0-3793-96e7-c554ee5ac55a | -12.83545 | -50.63686 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.4 |
| 0d065c6d-e0aa-3633-82d4-834797d5d711 | -7.74696 | -45.71689 | 2025-10-14 04:25:00 | NOAA-20 | SAMBAÍBA | MARANHÃO | Brasil | 2109700 | 21 | 33 | nan | nan | nan | Cerrado | 2.0 |
| bb872a92-2659-331d-a023-6d32593b5f83 | -7.55863 | -42.68877 | 2025-10-14 04:25:00 | NOAA-20 | FLORES DO PIAUÍ | PIAUÍ | Brasil | 2203800 | 22 | 33 | nan | nan | nan | Caatinga | 1.9 |
| 60dbb38b-3b0f-3044-8664-7dff82649fda | -7.62063 | -47.83625 | 2025-10-14 04:25:00 | NOAA-20 | FILADÉLFIA | TOCANTINS | Brasil | 1707702 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 5cc6921b-0850-372d-bbbe-3d0d463f8969 | -11.50384 | -43.48168 | 2025-10-14 04:25:00 | NOAA-20 | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 8e59d7dd-17bc-3215-b524-ee79d262abfa | -12.8075 | -50.64919 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 13.1 |
| 1c16ce64-e731-315f-91a8-74c403b82d83 | -8.5025 | -37.94378 | 2025-10-14 04:25:00 | NOAA-20 | FLORESTA | PERNAMBUCO | Brasil | 2605707 | 26 | 33 | nan | nan | nan | Caatinga | 2.0 |
| d8312769-d3d3-3e29-ba9e-a02d462ed45c | -7.75162 | -44.72925 | 2025-10-14 04:25:00 | NOAA-20 | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| ac01431c-4387-31c9-b714-10121d6dfa9d | -7.15713 | -46.52977 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.5 |
| d1d268c7-fa5f-309c-a83a-ac14ed314c52 | -7.2518 | -45.95193 | 2025-10-14 04:25:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| a901944b-c02a-3aa4-90fb-d0803f09f33c | -12.78632 | -50.65561 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.8 |
| 7e7051cd-243a-31bb-8478-0927153004ae | -7.68833 | -42.56969 | 2025-10-14 04:25:00 | NOAA-20 | SÃO JOSÉ DO PEIXE | PIAUÍ | Brasil | 2210102 | 22 | 33 | nan | nan | nan | Caatinga | 5.1 |
| c63aed81-5c92-3a61-81ad-5720a3d708e0 | -12.86052 | -50.64131 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 3.6 |
| eb910adf-cb50-3241-a6db-3d75d1ce62d3 | -8.11794 | -55.28463 | 2025-10-14 04:25:00 | NOAA-20 | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| f95aa329-3ba5-33be-9408-6f50accd7c8b | -6.59046 | -46.46076 | 2025-10-14 04:25:00 | NOAA-20 | FORMOSA DA SERRA NEGRA | MARANHÃO | Brasil | 2104099 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| efce3d9e-f328-351a-a7f8-b750bd04811c | -8.54755 | -44.58859 | 2025-10-14 04:25:00 | NOAA-20 | PALMEIRA DO PIAUÍ | PIAUÍ | Brasil | 2207405 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f65bee2e-c18b-31b0-bc8f-e5ef2675765c | -7.31089 | -46.67495 | 2025-10-14 04:25:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 15.6 |
| 296dcf02-23db-3e69-8e92-9140ecc97bad | -12.79988 | -50.64072 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 1.7 |
| ac7c735d-7a3b-351d-bd34-8e9fec09beb3 | -12.82543 | -50.65236 | 2025-10-14 04:25:00 | NOAA-20 | COCALINHO | MATO GROSSO | Brasil | 5103106 | 51 | 33 | nan | nan | nan | Cerrado | 2.8 |
| af0a1ed6-1f1a-38f0-9b0a-7eb7b7639dac | -7.22857 | -45.31949 | 2025-10-14 04:25:00 | NOAA-20 | LORETO | MARANHÃO | Brasil | 2106102 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 4dc9115d-e046-3688-b386-cc9a4bc01351 | -12.8937 | -44.6033 | 2025-10-14 04:25:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 43f2a1d2-4a79-3126-b4ba-49a1cfb15d62 | -7.06669 | -44.26721 | 2025-10-14 04:25:00 | NOAA-20 | ANTÔNIO ALMEIDA | PIAUÍ | Brasil | 2200806 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 2ead0e9e-13e4-34ff-88f4-b62cff1f2e6e | -6.99004 | -47.08908 | 2025-10-14 04:25:00 | NOAA-20 | ESTREITO | MARANHÃO | Brasil | 2104057 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |


[Clique aqui para ver as próximas entradas](README31.md)
