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

## Dados Diários - Página 16

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 42679660-1ab4-3d06-a7cf-68df1ae8ef01 | -12.42945 | -50.01744 | 2025-07-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 8b73e7c6-d6db-3880-86bc-3f5a52fb1a8f | -8.04708 | -50.0741 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 069dfec8-f589-36fe-a30f-e6bbbc21bad1 | -13.00005 | -44.85803 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e79ae315-c1c8-3c97-87ad-3e5a32a49f7a | -12.57084 | -44.75195 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 71a3a920-bbec-3310-bea2-cf766596c53f | -12.42975 | -50.03731 | 2025-07-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 8a5998cb-33d5-3b7a-b7f0-ec942e986165 | -12.58086 | -56.96846 | 2025-07-18 04:27:00 | NOAA-21 | NOVA MARINGÁ | MATO GROSSO | Brasil | 5108907 | 51 | 33 | nan | nan | nan | Amazônia | 0.7 |
| 9ebfb347-9ec6-328c-8c1b-e9c39642526e | -8.06427 | -50.11067 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| e3dc20fa-3903-3ba1-8ff9-f95dfdce727c | -9.8029 | -47.74106 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 12aaac4d-f30f-3814-808f-496a5ee46428 | -10.88179 | -49.55131 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| d3e06b01-0dad-3d97-a0a8-689e54fa498f | -9.25659 | -47.90446 | 2025-07-18 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 1c5fac0d-e899-33e3-b7dd-77a92564d99d | -8.09542 | -47.60912 | 2025-07-18 04:27:00 | NOAA-21 | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 37fb2020-95f1-32c5-add6-5b0d0e779a23 | -9.51103 | -47.5648 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 156283db-7daa-3b3f-a674-3270882ceca7 | -10.89849 | -49.21149 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 654c5843-f2dc-3024-9473-6d693e746c1e | -12.06779 | -47.98259 | 2025-07-18 04:27:00 | NOAA-21 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b3809453-a09c-3bdf-bfd5-c9f72cc11861 | -9.25992 | -47.905 | 2025-07-18 04:27:00 | NOAA-21 | PEDRO AFONSO | TOCANTINS | Brasil | 1716505 | 17 | 33 | nan | nan | nan | Cerrado | 1.4 |
| e4b3e3ed-7c32-3328-8fed-0fcad1d881e8 | -10.71361 | -49.48479 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 39a7fb12-7de4-30d6-9ed3-1637a3f4086d | -12.43007 | -50.01358 | 2025-07-18 04:27:00 | NOAA-21 | SANDOLÂNDIA | TOCANTINS | Brasil | 1718840 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| e3a49da3-8dad-3b90-af69-6f8c1111d126 | -12.98905 | -46.92865 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 87a53a5c-7f88-3bfe-a85a-96b504cff6ee | -8.92057 | -49.8344 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.2 |
| 5c546b67-5a96-3040-abdb-cbd8a7ec4197 | -9.86167 | -44.70473 | 2025-07-18 04:27:00 | NOAA-21 | RIACHO FRIO | PIAUÍ | Brasil | 2208858 | 22 | 33 | nan | nan | nan | Cerrado | 0.9 |
| cce7c8eb-d4b6-30b5-8e43-46a44ca067f2 | -7.47553 | -49.21588 | 2025-07-18 04:27:00 | NOAA-21 | ARAGUAÍNA | TOCANTINS | Brasil | 1702109 | 17 | 33 | nan | nan | nan | Amazônia | 1.4 |
| 6001a251-60a1-3bcf-b90f-54e05170bbb7 | -11.56231 | -47.08095 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| e4d89203-35d1-38e7-aa8a-5ab3b3a9da64 | -9.27251 | -49.63685 | 2025-07-18 04:27:00 | NOAA-21 | ABREULÂNDIA | TOCANTINS | Brasil | 1700251 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| d0824a0d-97b8-32fc-a8e7-c073a122e6c2 | -9.60267 | -43.85667 | 2025-07-18 04:27:00 | NOAA-21 | MORRO CABEÇA NO TEMPO | PIAUÍ | Brasil | 2206654 | 22 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 43d7d7da-1f64-3b74-98ac-c8694021dc75 | -12.99882 | -44.86647 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| a0c42838-c7a8-391c-9fde-bb39e6429026 | -11.56398 | -47.09205 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 7e39a82f-b19f-3cdb-8e54-f65132a055e5 | -10.84376 | -48.34391 | 2025-07-18 04:27:00 | NOAA-21 | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| bb13bdef-80d5-3182-8e85-83298a15a8ce | -10.09147 | -47.24694 | 2025-07-18 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| 501ee96a-4b3a-3cb5-a9e4-61bd3211f978 | -14.77241 | -50.53249 | 2025-07-18 04:27:00 | NOAA-21 | MOZARLÂNDIA | GOIÁS | Brasil | 5214002 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 09e0e027-f41a-3645-b7ce-37772b411179 | -12.66505 | -47.09298 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 9.7 |
| e20cbba6-f200-3d67-afa9-3f88a0618baf | -11.16613 | -46.25362 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 2.8 |
| dea3ddca-4418-3b5b-9111-6829939927f2 | -8.8865 | -50.15295 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.1 |
| 696533c0-a363-3910-9fbe-ed6a06e34982 | -9.39195 | -48.40089 | 2025-07-18 04:27:00 | NOAA-21 | MIRACEMA DO TOCANTINS | TOCANTINS | Brasil | 1713205 | 17 | 33 | nan | nan | nan | Cerrado | 11.0 |
| f573ded5-3cd8-3ad3-8c48-150fe646cf9c | -11.56948 | -47.07848 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| b3befd50-f6da-3f55-b434-900c3160c5ed | -14.72805 | -45.11387 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6974e7f2-2912-3d72-a8b0-b0120803593a | -9.50772 | -47.56427 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 5a528584-8261-3b40-9104-f325ff2b05db | -14.72484 | -45.07581 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| af6e8d67-e5eb-3935-a0c1-5a63768811f8 | -12.03565 | -48.76295 | 2025-07-18 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 2.6 |
| bfb63aec-0ceb-34b2-851f-1972e3dd5e0b | -11.56122 | -47.088 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 10.1 |
| c9be0821-477e-3aa8-9b8e-b59c7d9759a6 | -9.24345 | -48.56151 | 2025-07-18 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 8defa6e9-5505-36fd-8e38-8925e52ea7d0 | -15.15627 | -46.18732 | 2025-07-18 04:27:00 | NOAA-21 | FORMOSO | MINAS GERAIS | Brasil | 3126208 | 31 | 33 | nan | nan | nan | Cerrado | 1.6 |
| e76c041b-28aa-3798-8e02-9ef1b3e23cff | -10.09532 | -47.24397 | 2025-07-18 04:27:00 | NOAA-21 | NOVO ACORDO | TOCANTINS | Brasil | 1715101 | 17 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 72fc2a97-0d9b-371b-92f6-f6427124d6d7 | -14.72621 | -45.07405 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 1e93c4ae-bfda-37d6-9b9c-1f12fc53a892 | -10.76954 | -49.59196 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5badcf7-a59b-3b1d-a556-f245e942ebae | -10.89569 | -49.20725 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| c04e91e3-119e-3064-bc7a-a43c006c553e | -14.73345 | -45.07513 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| e9fd35f0-b459-3f2d-af0d-fa62a16a89a4 | -8.65122 | -47.75262 | 2025-07-18 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.7 |
| bd1f8284-5513-3808-898c-46195e0f6a96 | -8.75688 | -46.58134 | 2025-07-18 04:27:00 | NOAA-21 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 475a73de-9c3e-3d29-97e1-dc38f4eddf0b | -14.71146 | -46.18923 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| c210d470-2d41-3482-8038-9ce543d29995 | -14.27895 | -50.50083 | 2025-07-18 04:27:00 | NOAA-21 | NOVA CRIXÁS | GOIÁS | Brasil | 5214838 | 52 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 04a23a42-99a6-3683-83a7-bb02fdd79191 | -8.91991 | -49.83842 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 1.8 |
| 1d0b1e13-5554-37bc-b087-f56fcc83284a | -8.2183 | -44.91356 | 2025-07-18 04:27:00 | NOAA-21 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6dbe1aa9-0b67-3451-9266-99c981d7943e | -11.36031 | -48.70699 | 2025-07-18 04:27:00 | NOAA-21 | ALIANÇA DO TOCANTINS | TOCANTINS | Brasil | 1700350 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 8e9b8384-05ee-31c9-a8a6-780ef4927d26 | -8.25356 | -46.07648 | 2025-07-18 04:27:00 | NOAA-21 | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 1.1 |
| cd9ad6ff-2c4b-3e91-a814-11b47e3dc5f0 | -11.56285 | -47.07743 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 11.3 |
| 2816dd59-93f9-33dc-ba39-9446846e0d0f | -13.00302 | -44.86275 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 263e9c64-f76a-3bb4-9464-4fcb59b2746c | -13.53077 | -44.28896 | 2025-07-18 04:27:00 | NOAA-21 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 6325db6d-3e47-3613-a936-87a18e29e95a | -14.72682 | -45.06971 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 83047d03-39a5-3c0e-b3c7-ecd973c4b5de | -10.81991 | -49.28637 | 2025-07-18 04:27:00 | NOAA-21 | SANTA RITA DO TOCANTINS | TOCANTINS | Brasil | 1718899 | 17 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 7df9a1a5-5bc1-314f-a167-a0a46cc24254 | -11.71674 | -47.77142 | 2025-07-18 04:27:00 | NOAA-21 | NATIVIDADE | TOCANTINS | Brasil | 1714203 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d4c9ebd8-0698-3e05-a1e1-2830a25142ec | -9.50386 | -47.56724 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 4cc8f297-5d1e-317d-a57e-720fca236d90 | -10.05307 | -59.10324 | 2025-07-18 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| f4caa9c5-ea63-3e57-8397-3956930d7c1a | -11.56675 | -47.0961 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| b3509ce9-364c-3296-8ade-be2e453605a1 | -14.7109 | -46.19309 | 2025-07-18 04:27:00 | NOAA-21 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 0.5 |
| 2ac7d4a6-27ab-3c76-af20-bba69ddd4d70 | -8.04207 | -50.08203 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.8 |
| e9b174a7-bdbc-32e4-be74-ae9f13d801de | -10.23176 | -48.06241 | 2025-07-18 04:27:00 | NOAA-21 | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 4b33f5b3-c482-3bcb-9c9d-cb4881b26c34 | -12.48135 | -46.91757 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 376fb494-c827-3d94-86ff-786b5c69f575 | -12.57144 | -44.74776 | 2025-07-18 04:27:00 | NOAA-21 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 735d0795-c04d-3a92-b5ff-e12f26066d09 | -7.71038 | -47.28967 | 2025-07-18 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| fa3ec05a-3bd5-33f8-ba4c-4be9d1fbcce0 | -9.80015 | -47.73703 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| b22856f3-ec4d-3a3a-b8b4-48997174192b | -12.03899 | -48.76349 | 2025-07-18 04:27:00 | NOAA-21 | SUCUPIRA | TOCANTINS | Brasil | 1720853 | 17 | 33 | nan | nan | nan | Cerrado | 0.4 |
| 4b52b225-fde6-3ec6-a001-7a7f9d694c3e | -13.68026 | -44.22423 | 2025-07-18 04:27:00 | NOAA-21 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| c24725a3-51eb-31f4-8afe-266f322e024b | -9.24287 | -48.56513 | 2025-07-18 04:27:00 | NOAA-21 | RIO DOS BOIS | TOCANTINS | Brasil | 1718709 | 17 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 59a83c59-b302-3466-94b6-e1cd82237c43 | -15.64333 | -41.25881 | 2025-07-18 04:27:00 | NOAA-21 | ENCRUZILHADA | BAHIA | Brasil | 2910404 | 29 | 33 | nan | nan | nan | Mata Atlântica | 0.5 |
| 119546aa-d024-3dc8-b8ff-6708a2713023 | -9.85009 | -48.06586 | 2025-07-18 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 1c98618a-1739-3725-b3cc-771d49e6d7f7 | -11.32427 | -55.21322 | 2025-07-18 04:27:00 | NOAA-21 | CLÁUDIA | MATO GROSSO | Brasil | 5103056 | 51 | 33 | nan | nan | nan | Amazônia | 2.4 |
| 1e6d36ff-f8fb-39b6-93da-a90c86e0bc92 | -7.35496 | -49.59867 | 2025-07-18 04:27:00 | NOAA-21 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.7 |
| c4ed78d9-8b13-3175-a26d-52fde0957883 | -12.48801 | -46.91863 | 2025-07-18 04:27:00 | NOAA-21 | ARRAIAS | TOCANTINS | Brasil | 1702406 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 42ab73c6-7376-3661-91ea-578e6774360f | -11.78307 | -45.22243 | 2025-07-18 04:27:00 | NOAA-21 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.4 |
| cdd871d4-6305-3eb1-a8db-3bcecc0631f0 | -8.04275 | -50.07783 | 2025-07-18 04:27:00 | NOAA-21 | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 2.0 |
| 79647df3-86dd-30d5-90a2-89f61e47bc08 | -14.72865 | -45.10956 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 741ab662-61d4-30d4-9581-4cc48081ca5c | -11.14431 | -49.73182 | 2025-07-18 04:27:00 | NOAA-21 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d6e8c71f-29a6-3c7d-b81f-16364fe3f222 | -7.70707 | -47.28914 | 2025-07-18 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| a9c66cbc-786a-35e5-b72d-958f5e237c0d | -8.87862 | -50.15591 | 2025-07-18 04:27:00 | NOAA-21 | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 5.7 |
| 8f643f50-c05c-31d6-a1eb-61d426ed2349 | -8.38019 | -44.03493 | 2025-07-18 04:27:00 | NOAA-21 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 1.2 |
| a81533a7-13b8-3fde-92f9-33ffe07fbb20 | -11.99796 | -45.30994 | 2025-07-18 04:27:00 | NOAA-21 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 42.0 |
| a7de80fe-5eee-3128-85b0-562ff8e01a2e | -14.71822 | -45.07046 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 4287ca7e-f533-3227-a9c2-a1dbe3c702cd | -8.5377 | -47.84658 | 2025-07-18 04:27:00 | NOAA-21 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2006df3d-3e8d-355c-befd-a1ec8003a994 | -10.71829 | -49.47775 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| be8093f3-d64f-36f1-832b-ef740e710aa1 | -9.37709 | -47.95985 | 2025-07-18 04:27:00 | NOAA-21 | TOCANTÍNIA | TOCANTINS | Brasil | 1721109 | 17 | 33 | nan | nan | nan | Cerrado | 0.6 |
| d127dc20-e882-3aa0-ba66-b7334a9c0885 | -7.70375 | -47.28861 | 2025-07-18 04:27:00 | NOAA-21 | CAROLINA | MARANHÃO | Brasil | 2102804 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 1842a419-6b4e-3e42-ae48-39622cc8c445 | -9.50441 | -47.56375 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 16.8 |
| 39344cda-c578-35ea-8ce6-cfc291406022 | -14.75591 | -48.27548 | 2025-07-18 04:27:00 | NOAA-21 | NIQUELÂNDIA | GOIÁS | Brasil | 5214606 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 88f27655-68b5-361c-beca-173253f0479b | -10.71767 | -49.48154 | 2025-07-18 04:27:00 | NOAA-21 | LAGOA DA CONFUSÃO | TOCANTINS | Brasil | 1711902 | 17 | 33 | nan | nan | nan | Cerrado | 8.8 |
| 89de9cb7-70e8-3986-8b30-740722aed434 | -11.85752 | -46.75352 | 2025-07-18 04:27:00 | NOAA-21 | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| f9203a04-5484-3ed2-b0d1-69c3e52a0524 | -10.05932 | -59.10436 | 2025-07-18 04:27:00 | NOAA-21 | ARIPUANÃ | MATO GROSSO | Brasil | 5101407 | 51 | 33 | nan | nan | nan | Amazônia | 1.6 |
| 7f1411a3-67fb-38b3-b2ea-1a6c7c3b7ae0 | -9.80677 | -47.73809 | 2025-07-18 04:27:00 | NOAA-21 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 99e59bf7-77a7-30d8-ad5a-b3b67135f1dd | -14.73707 | -45.07567 | 2025-07-18 04:27:00 | NOAA-21 | COCOS | BAHIA | Brasil | 2908101 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| eb2bb7d0-dafd-3bb0-bb84-4f9df960b198 | -15.47086 | -46.28525 | 2025-07-18 04:27:00 | NOAA-21 | BURITIS | MINAS GERAIS | Brasil | 3109303 | 31 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 87f047ec-6cff-3383-b569-54852cb2c256 | -11.57116 | -47.08958 | 2025-07-18 04:27:00 | NOAA-21 | PORTO ALEGRE DO TOCANTINS | TOCANTINS | Brasil | 1718006 | 17 | 33 | nan | nan | nan | Cerrado | 2.4 |


[Clique aqui para ver as próximas entradas](README17.md)
