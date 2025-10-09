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

## Dados Diários - Página 42

| ID | Latitude | Longitude | Data/Hora GMT | Satélite | Município | Estado | País | Município ID | Estado ID | País ID | Dias sem Chuva | Precipitação | Risco de Fogo | Bioma | FRP |
|----|----------|-----------|---------------|----------|-----------|--------|------|--------------|-----------|---------|----------------|--------------|----------------|-------|-----|
| 3b261aed-8ea9-31dd-9aa1-391d7919eece | -8.52288 | -46.18483 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.6 |
| b797ac1a-4278-38ee-ae74-88ca4c1f8576 | -8.61208 | -45.09168 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| 072e93a5-7c1b-39c2-bac4-fd200f41a90d | -2.2721 | -47.19948 | 2025-10-09 04:19:00 | NOAA-20 | GARRAFÃO DO NORTE | PARÁ | Brasil | 1503077 | 15 | 33 | nan | nan | nan | Amazônia | 0.3 |
| 01a817af-c193-3427-8beb-9427fb42b238 | -7.27845 | -49.45591 | 2025-10-09 04:19:00 | NOAA-20 | FLORESTA DO ARAGUAIA | PARÁ | Brasil | 1503044 | 15 | 33 | nan | nan | nan | Amazônia | 0.9 |
| 159ebe7f-f19e-3088-9d50-b133e6d52a25 | -14.42075 | -43.98265 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 32c6a6eb-1e8c-3463-b5db-8721f69e9e97 | -10.19913 | -44.56343 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 128b28bf-aaa5-31cc-b9ae-98116d403861 | -8.10476 | -39.47139 | 2025-10-09 04:19:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.0 |
| dac7f603-e917-33ba-ae52-3d4cbc29e6cf | -3.43065 | -42.46191 | 2025-10-09 04:19:00 | NOAA-20 | SÃO BERNARDO | MARANHÃO | Brasil | 2110609 | 21 | 33 | nan | nan | nan | Caatinga | 1.0 |
| 9dd88b3c-0bc1-385b-a4cd-41ba30dc3f77 | -8.70877 | -47.86868 | 2025-10-09 04:19:00 | NOAA-20 | ITACAJÁ | TOCANTINS | Brasil | 1710508 | 17 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 7ef7cb08-3002-385b-bb86-f3ec12794957 | -8.61153 | -45.09516 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 9.5 |
| e0ab25c9-8dd3-31b1-a398-9e01ce7cec6f | -8.51071 | -44.2224 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO GURGUÉIA | PIAUÍ | Brasil | 2200459 | 22 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 729aa16f-2887-399f-9f5e-38368903d730 | -11.78426 | -45.04639 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| d3eecd08-16e9-3d33-b868-bb69f19e4785 | -13.79169 | -45.84391 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| cd650053-4e5f-3887-ab79-1838738e719d | -14.4354 | -46.15649 | 2025-10-09 04:19:00 | NOAA-20 | MAMBAÍ | GOIÁS | Brasil | 5212709 | 52 | 33 | nan | nan | nan | Cerrado | 0.6 |
| 5f43afe4-9966-3a30-9d4f-0686a8611527 | -8.1053 | -39.46762 | 2025-10-09 04:19:00 | NOAA-20 | PARNAMIRIM | PERNAMBUCO | Brasil | 2610400 | 26 | 33 | nan | nan | nan | Caatinga | 1.1 |
| d455395d-0163-3459-ac98-0ac8f1f281e8 | -13.03104 | -43.90136 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 2.9 |
| 40b7c51d-0998-3cce-922a-ebddd2baa072 | -7.78627 | -44.18774 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 9b213ad1-cbdb-3026-8be9-5b90a4c6166c | -10.87943 | -45.07894 | 2025-10-09 04:19:00 | NOAA-20 | FORMOSA DO RIO PRETO | BAHIA | Brasil | 2911105 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 0135a501-ec13-3368-a326-0ecbc8a63690 | -14.42134 | -43.97871 | 2025-10-09 04:19:00 | NOAA-20 | JUVENÍLIA | MINAS GERAIS | Brasil | 3136959 | 31 | 33 | nan | nan | nan | Cerrado | 7.7 |
| 58d7ab30-b766-3ade-8ba1-b33663cbe28c | -13.76521 | -45.79593 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.6 |
| abc02dc2-8399-3389-be92-e83b68e85d0b | -14.79583 | -46.08764 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 2.1 |
| d059322b-0a9d-386f-a510-f40447027c13 | -11.22586 | -50.79731 | 2025-10-09 04:19:00 | NOAA-20 | LUCIARA | MATO GROSSO | Brasil | 5105309 | 51 | 33 | nan | nan | nan | Cerrado | 0.7 |
| a5ef8396-125b-3dc5-9a22-74a4ddfd028c | -8.47618 | -47.20815 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 5.1 |
| bd1fee15-7c97-3206-af22-5ecf64e04588 | -9.76333 | -47.69835 | 2025-10-09 04:19:00 | NOAA-20 | RIO SONO | TOCANTINS | Brasil | 1718758 | 17 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 9a040581-8ec4-3459-a2c4-5c01b33c5e9d | -11.15466 | -47.73816 | 2025-10-09 04:19:00 | NOAA-20 | PINDORAMA DO TOCANTINS | TOCANTINS | Brasil | 1717008 | 17 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 21f2c437-dbb2-37f5-ad34-a83ad70300aa | -13.80632 | -43.93282 | 2025-10-09 04:19:00 | NOAA-20 | CARINHANHA | BAHIA | Brasil | 2907103 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| ff4133dc-02ca-3f1b-819e-56561c01bcbb | -11.32474 | -44.87846 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 68766f51-26e3-33dd-b91a-68bf583d2660 | -13.81767 | -45.78629 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| f881e543-6874-34af-a33c-7f84c9efcb8d | -11.86894 | -45.52566 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 0.8 |
| 569f47c4-b6cc-39ac-8217-2b6e8f22819f | -10.55212 | -50.0398 | 2025-10-09 04:19:00 | NOAA-20 | PIUM | TOCANTINS | Brasil | 1717503 | 17 | 33 | nan | nan | nan | Cerrado | 0.9 |
| d302feaf-e724-3b56-a87a-ef7a172c9fa1 | -11.77983 | -45.05302 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| a82e016a-77ed-35c4-a7a9-fadbf9c61a8b | -11.89682 | -44.95457 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.1 |
| 51c888cf-2bb2-37f2-92fe-b09332620df4 | -7.78947 | -42.41974 | 2025-10-09 04:19:00 | NOAA-20 | SOCORRO DO PIAUÍ | PIAUÍ | Brasil | 2210904 | 22 | 33 | nan | nan | nan | Caatinga | 2.2 |
| b5dea199-f22d-3b6f-aa6e-1afe4f35f1ae | -8.58486 | -48.735 | 2025-10-09 04:19:00 | NOAA-20 | ITAPORÃ DO TOCANTINS | TOCANTINS | Brasil | 1711100 | 17 | 33 | nan | nan | nan | Amazônia | 0.4 |
| a52c1a10-4a3e-3987-9fcd-30301b15ea2b | -7.73327 | -42.40371 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 2.0 |
| 1b893ade-3235-3cc9-bf67-9213185889bf | -12.17144 | -47.78431 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 01dbf7f6-ac1d-3124-a577-e4025c155bff | -8.16269 | -43.32752 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 1.5 |
| 4be599a2-2d6b-3173-9ef0-3efa78da3a8f | -12.42742 | -45.70959 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 4.7 |
| 76a9d03a-7781-30ab-97f0-b20f874d73bd | -8.18641 | -43.33114 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 19.3 |
| b9406cc2-2906-39f6-99da-36512d190bb3 | -7.3236 | -44.79755 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| d720729d-6df5-37f8-8c74-03d596ca6ca1 | -11.80255 | -45.03835 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.6 |
| 7cf0f176-474e-392e-b124-95f55ecdb75e | -13.79114 | -45.84746 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.1 |
| 072986d5-178f-3646-9f97-c76e44b72676 | -11.24023 | -40.33377 | 2025-10-09 04:19:00 | NOAA-20 | JACOBINA | BAHIA | Brasil | 2917508 | 29 | 33 | nan | nan | nan | Caatinga | 0.5 |
| 7e245d0a-97d4-30f6-acdf-a4cc48a7647b | -7.80741 | -46.63938 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 793536b5-5073-3ccd-b70b-7b184e968a78 | -12.42576 | -45.72015 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 1.8 |
| 4098c0a8-c3fa-3f99-8ff7-527dba4d170d | -8.19827 | -43.3442 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 3.7 |
| 4af9f7f6-d962-30f6-b690-67b95ebea518 | -7.76658 | -44.03045 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| ecd3b6e6-0f28-3f07-9c2d-d1211ea0f149 | -8.61981 | -45.12846 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 4f0fb962-ebcb-3d2c-b0da-66355b87ad2f | -14.25593 | -44.3857 | 2025-10-09 04:19:00 | NOAA-20 | FEIRA DA MATA | BAHIA | Brasil | 2910776 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| a5bae308-efcc-3de4-b8f8-bcb0c7021fe1 | -7.31035 | -44.77417 | 2025-10-09 04:19:00 | NOAA-20 | BENEDITO LEITE | MARANHÃO | Brasil | 2101806 | 21 | 33 | nan | nan | nan | Cerrado | 1.4 |
| aefffadb-92ae-399d-bf07-a0110e4744d3 | -13.78672 | -45.85402 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 490a0a86-4638-31c6-8e05-cbd405d9786b | -13.79057 | -45.87283 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 2.7 |
| 95e7a98e-4cd6-3f52-9494-04dc4503d590 | -13.82815 | -45.80621 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 2.2 |
| 7ada1371-9aa3-3afa-aa52-c1866d2d889e | -7.76603 | -44.03395 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| 4c8055e1-410b-3b40-8b4f-dbc2caa45fd8 | -11.33988 | -49.3793 | 2025-10-09 04:19:00 | NOAA-20 | DUERÉ | TOCANTINS | Brasil | 1707306 | 17 | 33 | nan | nan | nan | Cerrado | 3.0 |
| 55730683-ec03-3a71-99a3-676d1ca633e4 | -11.78876 | -45.14856 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 4cd065c6-1d52-3493-86d8-89776c863a85 | -12.42522 | -45.70202 | 2025-10-09 04:19:00 | NOAA-20 | SÃO DESIDÉRIO | BAHIA | Brasil | 2928901 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| e1abd9d0-d721-313b-8809-4b785829a870 | -8.70368 | -47.03881 | 2025-10-09 04:19:00 | NOAA-20 | RECURSOLÂNDIA | TOCANTINS | Brasil | 1718501 | 17 | 33 | nan | nan | nan | Cerrado | 1.8 |
| f77902b3-8744-3890-b4b5-f61bf1e84eba | -7.76325 | -44.02993 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 5.6 |
| e374848d-abba-32a9-896a-face915d5585 | -7.62951 | -43.05563 | 2025-10-09 04:19:00 | NOAA-20 | ITAUEIRA | PIAUÍ | Brasil | 2205102 | 22 | 33 | nan | nan | nan | Caatinga | 2.4 |
| 352446ab-f78b-394b-a28f-a23994637caa | -8.4121 | -41.4533 | 2025-10-09 04:19:00 | NOAA-20 | QUEIMADA NOVA | PIAUÍ | Brasil | 2208650 | 22 | 33 | nan | nan | nan | Caatinga | 1.2 |
| be7cc3b6-0eab-3aaf-9afc-3e7fa8ca8a5e | -10.73274 | -49.33614 | 2025-10-09 04:19:00 | NOAA-20 | CRISTALÂNDIA | TOCANTINS | Brasil | 1706100 | 17 | 33 | nan | nan | nan | Cerrado | 10.4 |
| 233ac598-4b32-37fd-9847-cf5064e16f63 | -8.52858 | -46.27774 | 2025-10-09 04:19:00 | NOAA-20 | BALSAS | MARANHÃO | Brasil | 2101400 | 21 | 33 | nan | nan | nan | Cerrado | 3.1 |
| 18a3c49f-7892-3d7a-8599-59049358f455 | -8.6347 | -45.1415 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| d84d83fa-e7c7-3092-8771-2f0208126be4 | -7.75328 | -44.02836 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.2 |
| 6c782383-e5ad-31d2-a1a6-8fd5f94e0154 | -11.09601 | -48.55816 | 2025-10-09 04:19:00 | NOAA-20 | BREJINHO DE NAZARÉ | TOCANTINS | Brasil | 1703701 | 17 | 33 | nan | nan | nan | Cerrado | 2.1 |
| b9d6cea8-5007-3b3e-b37c-f2bb6ff73406 | -7.67982 | -42.4033 | 2025-10-09 04:19:00 | NOAA-20 | SÃO MIGUEL DO FIDALGO | PIAUÍ | Brasil | 2210391 | 22 | 33 | nan | nan | nan | Caatinga | 1.7 |
| bdffb5be-2dfd-3889-8008-afae0399e16f | -8.60989 | -45.10558 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 2.1 |
| e6dee9bc-0051-347d-a089-7252f19d1365 | -13.82759 | -45.80975 | 2025-10-09 04:19:00 | NOAA-20 | JABORANDI | BAHIA | Brasil | 2917359 | 29 | 33 | nan | nan | nan | Cerrado | 1.3 |
| 2d269385-fc92-328a-8c23-51ebe840d85f | -7.77546 | -44.03903 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| 7d69f079-cdde-3ca3-879f-744c7da3e99c | -9.17337 | -40.30838 | 2025-10-09 04:19:00 | NOAA-20 | PETROLINA | PERNAMBUCO | Brasil | 2611101 | 26 | 33 | nan | nan | nan | Caatinga | 4.0 |
| 14cad4d0-92fb-38de-8d2d-72887c5af628 | -12.25727 | -47.88018 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 4.9 |
| bfcbf512-8889-3495-a37e-26b79115069b | -7.80968 | -46.71197 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.9 |
| 1729acd3-743c-386b-98ef-e4da152b6896 | -3.25699 | -39.42094 | 2025-10-09 04:19:00 | NOAA-20 | TRAIRI | CEARÁ | Brasil | 2313500 | 23 | 33 | nan | nan | nan | Caatinga | 1.2 |
| ced9829b-293a-391f-9d79-b1d46e07faec | -7.77268 | -44.035 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 3.4 |
| e59eab55-53ee-3289-8eac-75c76d47ec5d | -8.61319 | -45.10611 | 2025-10-09 04:19:00 | NOAA-20 | BAIXA GRANDE DO RIBEIRO | PIAUÍ | Brasil | 2201150 | 22 | 33 | nan | nan | nan | Cerrado | 1.4 |
| f3f7f3d1-9d27-3f25-b0cc-ad517176e721 | -7.66636 | -42.58611 | 2025-10-09 04:19:00 | NOAA-20 | RIBEIRA DO PIAUÍ | PIAUÍ | Brasil | 2208874 | 22 | 33 | nan | nan | nan | Caatinga | 2.6 |
| 10864141-331b-3a3b-b95a-55b5e2b32b77 | -13.79224 | -45.84036 | 2025-10-09 04:19:00 | NOAA-20 | CORRENTINA | BAHIA | Brasil | 2909307 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 09621aaf-1e0d-351d-881b-90e9d7378f48 | -10.1958 | -44.56291 | 2025-10-09 04:19:00 | NOAA-20 | PARNAGUÁ | PIAUÍ | Brasil | 2207603 | 22 | 33 | nan | nan | nan | Cerrado | 1.3 |
| bccb0f16-f92c-324b-a2c2-81558bab491d | -7.99106 | -43.89592 | 2025-10-09 04:19:00 | NOAA-20 | MANOEL EMÍDIO | PIAUÍ | Brasil | 2205904 | 22 | 33 | nan | nan | nan | Cerrado | 6.0 |
| 80917afb-05be-3dcc-8895-726685bed4a0 | -11.32032 | -44.88503 | 2025-10-09 04:19:00 | NOAA-20 | SANTA RITA DE CÁSSIA | BAHIA | Brasil | 2928406 | 29 | 33 | nan | nan | nan | Cerrado | 0.7 |
| 955c6c86-6a69-337a-b22c-f4d9cf3d688c | -13.25096 | -46.4734 | 2025-10-09 04:19:00 | NOAA-20 | DIVINÓPOLIS DE GOIÁS | GOIÁS | Brasil | 5208301 | 52 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 2afade94-2a01-3ed0-903c-62b63f55c445 | -8.18923 | -43.33532 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 14.2 |
| 133a9d45-052a-3511-ae8e-a16962ae258c | -13.12841 | -43.90381 | 2025-10-09 04:19:00 | NOAA-20 | SANTANA | BAHIA | Brasil | 2928208 | 29 | 33 | nan | nan | nan | Cerrado | 4.8 |
| ba049d42-b71c-3400-b48a-13dfdb4d0829 | -11.86508 | -45.50702 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.0 |
| 966c5375-274b-3c4b-862d-b08e79ab509b | -11.87886 | -45.50568 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 1.2 |
| 3235054e-bd79-303f-be48-4ac356938925 | -14.78192 | -46.11135 | 2025-10-09 04:19:00 | NOAA-20 | SÍTIO D'ABADIA | GOIÁS | Brasil | 5220702 | 52 | 33 | nan | nan | nan | Cerrado | 1.4 |
| dd53c25f-7ed0-3705-840f-79cf39367f88 | -7.77964 | -44.18665 | 2025-10-09 04:19:00 | NOAA-20 | SEBASTIÃO LEAL | PIAUÍ | Brasil | 2210631 | 22 | 33 | nan | nan | nan | Cerrado | 2.3 |
| 44e17ba5-db2d-395a-8590-c4cb73453473 | -14.53032 | -46.63117 | 2025-10-09 04:19:00 | NOAA-20 | ALVORADA DO NORTE | GOIÁS | Brasil | 5200803 | 52 | 33 | nan | nan | nan | Cerrado | 1.7 |
| 0b93f325-8d77-374c-a634-fd9d64297844 | -13.78275 | -44.34572 | 2025-10-09 04:19:00 | NOAA-20 | CORIBE | BAHIA | Brasil | 2909109 | 29 | 33 | nan | nan | nan | Cerrado | 1.7 |
| c6491cd6-a056-3dbe-91e2-30e2da0501df | -15.32133 | -41.73837 | 2025-10-09 04:19:00 | NOAA-20 | NINHEIRA | MINAS GERAIS | Brasil | 3144656 | 31 | 33 | nan | nan | nan | Mata Atlântica | 1.6 |
| 7e412c6d-95ef-3216-80e0-06d62d9ee901 | -14.48324 | -40.62515 | 2025-10-09 04:19:00 | NOAA-20 | POÇÕES | BAHIA | Brasil | 2925105 | 29 | 33 | nan | nan | nan | Caatinga | 0.7 |
| 2569ff84-8708-3a2f-acec-7f7457ecab9e | -12.14159 | -47.75243 | 2025-10-09 04:19:00 | NOAA-20 | PARANÃ | TOCANTINS | Brasil | 1716208 | 17 | 33 | nan | nan | nan | Cerrado | 3.8 |
| d88ef199-f162-36aa-a493-abe12cabb97b | -11.86408 | -44.92369 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 783e9864-1275-3bf1-b6e8-f9ec0ed6e53b | -7.79301 | -46.72833 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO | MARANHÃO | Brasil | 2109502 | 21 | 33 | nan | nan | nan | Cerrado | 0.8 |
| e7ca2855-f408-3104-aa44-83528ebfd278 | -11.84877 | -45.06668 | 2025-10-09 04:19:00 | NOAA-20 | RIACHÃO DAS NEVES | BAHIA | Brasil | 2926202 | 29 | 33 | nan | nan | nan | Cerrado | 1.5 |
| 6f3b2f09-912d-375a-ac1a-dcf89501dc20 | -11.87115 | -45.53322 | 2025-10-09 04:19:00 | NOAA-20 | BARREIRAS | BAHIA | Brasil | 2903201 | 29 | 33 | nan | nan | nan | Cerrado | 3.9 |
| 0cae21c4-206f-3d9e-b7d3-db2d501c4706 | -8.17397 | -43.32174 | 2025-10-09 04:19:00 | NOAA-20 | CANTO DO BURITI | PIAUÍ | Brasil | 2202307 | 22 | 33 | nan | nan | nan | Caatinga | 2.9 |
| 6e38bd7c-0b02-3af9-a44f-2bc7558e3a95 | -12.23954 | -43.78854 | 2025-10-09 04:19:00 | NOAA-20 | MUQUÉM DO SÃO FRANCISCO | BAHIA | Brasil | 2922250 | 29 | 33 | nan | nan | nan | Cerrado | 2.0 |
| 9ce4b5d3-af45-3b6f-acff-290c1ad3bf88 | -13.26729 | -42.50208 | 2025-10-09 04:19:00 | NOAA-20 | BOTUPORÃ | BAHIA | Brasil | 2904209 | 29 | 33 | nan | nan | nan | Caatinga | 0.9 |


[Clique aqui para ver as próximas entradas](README43.md)
