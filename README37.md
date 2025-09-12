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

## Dados Diários - Página 37

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| c5ac7fec-5994-38fc-b829-5e6c4f255673 | -9.03302 | -47.09176 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| 48b24c20-d18c-3adc-b72e-bc9b3ce2a2b6 | -7.44749 | -44.43601 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| f0f4e790-c869-3dc8-8c16-e658aba46f1d | -8.94543 | -46.71857 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.0 |
| ec425ffa-78b4-3e7d-bc9d-4069e004359c | -10.53683 | -51.52508 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 9e5b0cb3-94b6-3153-9260-4ada08082a4c | -10.65605 | -48.65253 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 2fc1a8f2-0788-3ab0-8063-02b5e3caa2b8 | -9.7571 | -45.39786 | 2025-09-12 04:04:00 | NPP-375D | GILBUÉS | PIAUÍ | Brasil | 2204402 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| ce2e9389-39f0-3828-84e7-db4629088f17 | -10.09079 | -48.17356 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.1 |
| bd34f01f-e956-3f3a-a9fc-ed526351bfcf | -12.12177 | -44.87222 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 392009aa-ee4f-3ae9-abfc-e897af7b296b | -7.84845 | -45.39098 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRO GONÇALVES | PIAUÍ | Brasil | 2208908 | 22 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 4d7e7e35-f4bb-3cdc-8358-c15017425cc4 | -6.56305 | -43.15103 | 2025-09-12 04:04:00 | NPP-375D | BARÃO DE GRAJAÚ | MARANHÃO | Brasil | 2101509 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| f42bee48-b210-3982-b8d3-454f428436d3 | -6.49716 | -44.49257 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 3.5 |
| 3c0ff922-1568-3eb7-94a9-4802af49a76a | -11.46868 | -43.61027 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 62b72e3d-c21a-3334-870d-6acd2bfb57bd | -5.76608 | -45.51949 | 2025-09-12 04:04:00 | NPP-375D | BARRA DO CORDA | MARANHÃO | Brasil | 2101608 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| 98410160-4b90-354d-9291-467ffd68bef1 | -6.54831 | -42.40552 | 2025-09-12 04:04:00 | NPP-375D | ARRAIAL | PIAUÍ | Brasil | 2201002 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 87c72dcc-926a-308a-8082-67926068bf33 | -6.48243 | -45.15952 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| c15d76ba-cbcb-3373-8551-b4054317785e | -11.1243 | -45.11858 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 3.0 |
| ade2916e-97f4-35be-84a2-0d57dab3db3f | -8.0698 | -50.17369 | 2025-09-12 04:04:00 | NPP-375D | REDENÇÃO | PARÁ | Brasil | 1506138 | 15 | 33 | nan | nan | nan | Amazônia | 1.9 |
| b59c1ee4-b3a4-3a74-b560-d8bf3b9f4dac | -8.62288 | -40.1993 | 2025-09-12 04:04:00 | NPP-375D | LAGOA GRANDE | PERNAMBUCO | Brasil | 2608750 | 26 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 353d551c-ed96-3e9f-9c06-9b42dbbe756b | -10.13755 | -47.90859 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 2.2 |
| acfc93b8-8b0f-397d-ada7-d6f3b88e42e0 | -9.4926 | -48.65717 | 2025-09-12 04:04:00 | NPP-375D | MIRANORTE | TOCANTINS | Brasil | 1713304 | 17 | 33 | nan | nan | nan | Cerrado | 4.5 |
| 8952cce5-d3bd-3765-803b-f0da79645874 | -6.40725 | -45.14075 | 2025-09-12 04:04:00 | NPP-375D | MIRADOR | MARANHÃO | Brasil | 2106706 | 21 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 86d7b8c3-8bbc-349a-8eff-b6d757322a6f | -9.89663 | -51.87709 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.9 |
| 9e24b005-351a-3d93-8bcd-490a2b9053ce | -9.03669 | -47.09711 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 9.8 |
| b4525975-cde2-3525-9cf7-40248eed4c0c | -6.67932 | -44.13599 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 7a0ca1bb-7005-30e4-a65d-3e5e9b007c1f | -6.48092 | -43.88276 | 2025-09-12 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 6b52adb9-84df-35ba-b0e1-26d2ab613a10 | -10.53005 | -51.52201 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 5.3 |
| a8f1c6ae-cedc-3328-a3ee-e08c81d5dcc7 | -11.09238 | -48.41679 | 2025-09-12 04:04:00 | NPP-375D | IPUEIRAS | TOCANTINS | Brasil | 1709807 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 10998172-0636-3922-8984-1eb9374c2ee0 | -10.21501 | -46.24334 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| e7f8fcf5-47d2-3321-8b73-557e8d4bdc0a | -7.40325 | -44.36231 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 1740c89c-6eed-3c8c-8ee3-b9a0f9d3d663 | -6.54073 | -43.70546 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DOS PATOS | MARANHÃO | Brasil | 2111102 | 21 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b30de6a-6b2c-3414-9424-18cb9879b949 | -11.69226 | -46.5892 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 3d9d15a4-efbd-3c4c-ac45-6832e19c3d41 | -9.88201 | -46.46802 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 8741540b-4e3b-32c5-8b0f-af1a17dcf891 | -9.04601 | -47.07037 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 13.6 |
| e1911126-5e6e-34ee-bd11-2d63b8fcd897 | -10.67653 | -48.64984 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 737aa5bf-9f1a-3c66-8c5c-27b424c854b7 | -5.76137 | -52.37912 | 2025-09-12 04:04:00 | NPP-375D | SÃO FÉLIX DO XINGU | PARÁ | Brasil | 1507300 | 15 | 33 | nan | nan | nan | Amazônia | 3.2 |
| 8e473be8-804c-38a9-84e0-9e583fd7d662 | -11.6681 | -46.60467 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 2b3f890c-920e-354d-8e1f-f5c5c0e3d3e6 | -9.77665 | -47.84941 | 2025-09-12 04:04:00 | NPP-375D | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 33de598b-17a8-31e6-9930-490c1d8e35e6 | -11.48427 | -43.62531 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 4.4 |
| 0511e2a8-40ee-37a6-a04d-2b0c5478bdcf | -8.37204 | -44.84876 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 4.1 |
| 8414017b-28f0-387c-afc4-fae4fb552c9f | -9.11135 | -47.12792 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| dfd8c905-0add-34b5-ac6e-0055f1f5d6c2 | -9.887 | -46.46448 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| b13d9ba5-d550-3f96-80ac-12da8cb5e5b9 | -10.70449 | -48.63346 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 883aa8ad-4536-35f8-ad01-1d4f7efb8017 | -7.79288 | -50.77945 | 2025-09-12 04:04:00 | NPP-375D | CUMARU DO NORTE | PARÁ | Brasil | 1502764 | 15 | 33 | nan | nan | nan | Amazônia | 3.4 |
| 1fd8a7f2-a76b-34ff-8173-8a22520f9881 | -10.14091 | -47.9062 | 2025-09-12 04:04:00 | NPP-375D | PALMAS | TOCANTINS | Brasil | 1721000 | 17 | 33 | nan | nan | nan | Cerrado | 1.5 |
| bcb30afa-3e26-389a-a854-1a553b501d96 | -5.94619 | -42.56064 | 2025-09-12 04:04:00 | NPP-375D | HUGO NAPOLEÃO | PIAUÍ | Brasil | 2204600 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| 6cc55c44-5737-3a04-a11f-15e4cc455beb | -9.07384 | -47.12225 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 342f6455-f06b-3155-8275-fce69ab71c6c | -8.07773 | -42.56597 | 2025-09-12 04:04:00 | NPP-375D | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 3.0 |
| 4cd20ac7-7541-3cf6-a125-3a412f214335 | -8.17809 | -46.11786 | 2025-09-12 04:04:00 | NPP-375D | TASSO FRAGOSO | MARANHÃO | Brasil | 2112001 | 21 | 33 | nan | nan | nan | Cerrado | 2.8 |
| c6bb0e3a-157f-3654-b682-4e2f5252b237 | -11.67226 | -46.60532 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 3.6 |
| 0014ff15-3922-30ea-82c2-77658d585683 | -12.11807 | -44.87152 | 2025-09-12 04:04:00 | NPP-375D | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 5.8 |
| a51de1ae-7044-3412-ac90-0eb07cb267ea | -8.88189 | -49.93456 | 2025-09-12 04:04:00 | NPP-375D | SANTA MARIA DAS BARREIRAS | PARÁ | Brasil | 1506583 | 15 | 33 | nan | nan | nan | Amazônia | 3.1 |
| cee81385-811c-38d0-bb47-a767cf4f0492 | -6.67324 | -44.14907 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| b3a4b0c7-3afb-37b4-81e4-db929d9a6f55 | -6.48471 | -43.88337 | 2025-09-12 04:04:00 | NPP-375D | PARAIBANO | MARANHÃO | Brasil | 2107704 | 21 | 33 | nan | nan | nan | Cerrado | 4.6 |
| 4ad5450b-8d1d-37f9-8413-fd48a1df0556 | -6.25029 | -43.42607 | 2025-09-12 04:04:00 | NPP-375D | LAGOA DO MATO | MARANHÃO | Brasil | 2105922 | 21 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 351ced4e-e6b6-3f63-90c2-befdf470aec8 | -8.42706 | -47.25541 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 6.1 |
| f2af022e-6f8f-3451-b84a-fe577e8fd33a | -9.04647 | -47.04159 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 5aae6457-238e-3d56-a33f-35468c7664f7 | -6.67539 | -44.14785 | 2025-09-12 04:04:00 | NPP-375D | PASTOS BONS | MARANHÃO | Brasil | 2108009 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| 85e9ae13-4b9b-33a7-97fe-b37004f8b14f | -10.58357 | -47.21424 | 2025-09-12 04:04:00 | NPP-375D | PONTE ALTA DO TOCANTINS | TOCANTINS | Brasil | 1717909 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| f0637101-4155-37fc-a884-dc404112b956 | -11.6688 | -46.60083 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 6ba14644-326b-3aa6-a8be-cbb160ea80a3 | -11.67291 | -46.57811 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.7 |
| ef399618-d6c1-3f5c-84f5-037cab73008f | -10.65505 | -48.65787 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 5.0 |
| 61135c35-a27a-39fa-91fb-044e8a6b54d6 | -10.5341 | -51.5322 | 2025-09-12 04:04:00 | NPP-375D | CONFRESA | MATO GROSSO | Brasil | 5103353 | 51 | 33 | nan | nan | nan | Amazônia | 4.5 |
| eb4193a3-c256-3630-98c6-43b795e2fce4 | -10.17584 | -46.17388 | 2025-09-12 04:04:00 | NPP-375D | ALTO PARNAÍBA | MARANHÃO | Brasil | 2100501 | 21 | 33 | nan | nan | nan | Cerrado | 14.1 |
| bb913b46-ad98-3e92-ad5b-83431d049f3a | -10.12579 | -47.92097 | 2025-09-12 04:04:00 | NPP-375D | APARECIDA DO RIO NEGRO | TOCANTINS | Brasil | 1701101 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| b9ec26e4-dfc2-3288-b2e8-50c5dbb6f344 | -9.71687 | -46.89145 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 2.5 |
| 4f0c56ef-3bec-37da-aeac-15a02cf9d8b2 | -6.15569 | -47.28032 | 2025-09-12 04:04:00 | NPP-375D | CAMPESTRE DO MARANHÃO | MARANHÃO | Brasil | 2102556 | 21 | 33 | nan | nan | nan | Cerrado | 6.5 |
| d6bd04e3-55e5-35bc-9d70-8e0fcd66b6a9 | -6.36577 | -43.05652 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 5e667c13-7cfe-3921-b6bc-e9b36de54d0b | -7.75777 | -44.76222 | 2025-09-12 04:04:00 | NPP-375D | URUÇUÍ | PIAUÍ | Brasil | 2211209 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| e8f9d04a-b469-385f-9ff0-e5be73b182b7 | -6.18621 | -42.74195 | 2025-09-12 04:04:00 | NPP-375D | AMARANTE | PIAUÍ | Brasil | 2200509 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| a4efeb87-7550-3530-96fa-26efa479020e | -10.8598 | -44.78584 | 2025-09-12 04:04:00 | NPP-375D | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| bc721ec6-c80d-3127-bac1-a86d03d971c7 | -10.41135 | -50.59515 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| e5d17dfc-ea91-3ef3-9831-8471cf120a34 | -8.18571 | -42.41397 | 2025-09-12 04:04:00 | NPP-375D | SÃO JOÃO DO PIAUÍ | PIAUÍ | Brasil | 2210003 | 22 | 33 | nan | nan | nan | Caatinga | 1.1 |
| 223cd3e6-477e-3e1d-9b9b-1ed2e452d8b0 | -11.67255 | -46.59452 | 2025-09-12 04:04:00 | NPP-375D | NOVO JARDIM | TOCANTINS | Brasil | 1715259 | 17 | 33 | nan | nan | nan | Cerrado | 5.8 |
| 02d5ffda-ad12-34b7-9a43-4caeaa6006c5 | -5.94263 | -42.56006 | 2025-09-12 04:04:00 | NPP-375D | ÁGUA BRANCA | PIAUÍ | Brasil | 2200202 | 22 | 33 | nan | nan | nan | Caatinga | 3.5 |
| d4f3320d-efcc-3362-88cb-f7970cb63e9c | -10.44225 | -50.61292 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 2.0 |
| ce3c4985-3e88-38f8-8a0c-a1dbba05f668 | -10.21566 | -46.23949 | 2025-09-12 04:04:00 | NPP-375D | MATEIROS | TOCANTINS | Brasil | 1712702 | 17 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 1e89117a-30f8-3c6f-94af-53303d8e4fa6 | -10.4107 | -50.59849 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6b3a6d53-3626-3206-bfca-3f83c515b3c4 | -8.42627 | -47.26006 | 2025-09-12 04:04:00 | NPP-375D | GOIATINS | TOCANTINS | Brasil | 1709005 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 60c64b2c-c6d1-38b8-9927-8b77c864705e | -8.33208 | -45.40656 | 2025-09-12 04:04:00 | NPP-375D | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.2 |
| f3840742-2c93-3cef-8cd1-7dc654ca74aa | -8.07187 | -42.95042 | 2025-09-12 04:04:00 | NPP-375D | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| fca8b62a-c3cc-3026-ba9f-858b64820f09 | -9.05619 | -47.03853 | 2025-09-12 04:04:00 | NPP-375D | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 4.9 |
| ee354b0c-9052-33c3-997d-1dca52cf97bf | -9.06136 | -45.71503 | 2025-09-12 04:04:00 | NPP-375D | SANTA FILOMENA | PIAUÍ | Brasil | 2209203 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 27b8ef67-3d7a-3006-9eee-34e7df63b177 | -10.41837 | -50.61813 | 2025-09-12 04:04:00 | NPP-375D | SANTA TEREZINHA | MATO GROSSO | Brasil | 5107776 | 51 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 2f7a2321-d0e8-3d96-8108-23f225371cab | -6.27403 | -43.18636 | 2025-09-12 04:04:00 | NPP-375D | SÃO FRANCISCO DO MARANHÃO | MARANHÃO | Brasil | 2110906 | 21 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 626a3b2f-33b8-3fd9-b195-9707ae062915 | -6.30994 | -43.32697 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ce13d63a-b3f1-3a3f-9517-f9b6e3489ad1 | -9.10401 | -47.11734 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 3997e0fb-a317-38b5-a80a-9d2725ea37a2 | -11.45158 | -43.58279 | 2025-09-12 04:04:00 | NPP-375D | BARRA | BAHIA | Brasil | 2902708 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 852aaf02-3ee7-38d5-8d80-13697cede5dd | -6.31434 | -43.3232 | 2025-09-12 04:04:00 | NPP-375D | SUCUPIRA DO RIACHÃO | MARANHÃO | Brasil | 2111953 | 21 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 95f1893f-4641-3910-af86-b8caa0546b0b | -11.12049 | -45.11787 | 2025-09-12 04:04:00 | NPP-375D | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 5d546b41-5eb8-3475-b821-f382922df68a | -6.58864 | -40.29363 | 2025-09-12 04:04:00 | NPP-375D | AIUABA | CEARÁ | Brasil | 2300408 | 23 | 33 | nan | nan | nan | Caatinga | 0.6 |
| cd57975c-ed22-3a52-b41c-ec92fc8daed4 | -7.3504 | -44.3 | 2025-09-12 04:04:00 | NPP-375D | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| a12fa5e5-76e0-3757-858b-eacbf395121f | -10.333 | -48.80942 | 2025-09-12 04:04:00 | NPP-375D | PARAÍSO DO TOCANTINS | TOCANTINS | Brasil | 1716109 | 17 | 33 | nan | nan | nan | Cerrado | 3.3 |
| 58194a7e-a689-3c9f-9e3e-e4634e85c728 | -9.5154 | -54.638 | 2025-09-12 04:04:00 | NPP-375D | NOVO PROGRESSO | PARÁ | Brasil | 1505031 | 15 | 33 | nan | nan | nan | Amazônia | 10.3 |
| 589a7be2-198b-349e-980e-60b01ff70677 | -7.0721 | -44.1391 | 2025-09-12 04:04:00 | NPP-375D | PORTO ALEGRE DO PIAUÍ | PIAUÍ | Brasil | 2208551 | 22 | 33 | nan | nan | nan | Cerrado | 3.3 |
| c98c9516-cd3a-3b30-9090-4b524a0354c2 | -8.47014 | -47.27461 | 2025-09-12 04:04:00 | NPP-375D | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 1.9 |
| 3653df1b-93b9-3be8-88a1-b994488c0d00 | -6.31027 | -42.22514 | 2025-09-12 04:04:00 | NPP-375D | ELESBÃO VELOSO | PIAUÍ | Brasil | 2203503 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 48242c70-b5e5-364a-84e9-3157df486aaa | -9.09564 | -46.94362 | 2025-09-12 04:04:00 | NPP-375D | LIZARDA | TOCANTINS | Brasil | 1712405 | 17 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 7bc705e3-e49c-31a8-9171-18b1fdc827ac | -9.98901 | -51.72712 | 2025-09-12 04:04:00 | NPP-375D | VILA RICA | MATO GROSSO | Brasil | 5108600 | 51 | 33 | nan | nan | nan | Amazônia | 2.8 |
| 65fdc26e-54c1-3468-86eb-45558c469521 | -5.59506 | -42.91047 | 2025-09-12 04:04:00 | NPP-375D | CURRALINHOS | PIAUÍ | Brasil | 2203255 | 22 | 33 | nan | nan | nan | Caatinga | 0.8 |
| 5611892d-a4f3-3fba-98b3-70937f10693f | -10.66776 | -48.59631 | 2025-09-12 04:04:00 | NPP-375D | PORTO NACIONAL | TOCANTINS | Brasil | 1718204 | 17 | 33 | nan | nan | nan | Cerrado | 10.2 |


[Clique aqui para ver as próximas entradas](README38.md)
